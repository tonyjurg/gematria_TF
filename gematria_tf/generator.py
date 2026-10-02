"""Feature dictionaries -> explicit add-on destination -> TF round-trip checks."""
import gc
import json
import platform
import unicodedata
from importlib.metadata import version
from pathlib import Path

from . import __version__
from .bhsa import sha256
from .calculator import METHODS, TRANSFORMS, calculate
from .normalization import POLICY
from .representations import READINGS, REPRESENTATIONS, qere_errors, read_words, represent


def generate(api, source: Path, lock: dict, output: Path, *, methods=METHODS,
             transforms=("identity",), readings=("ketiv",), language="all", limit=None):
    from tf.fabric import Fabric

    output, source = Path(output).resolve(), Path(source).resolve()
    if output == source or source in output.parents:
        raise ValueError("Output must be separate from the BHSA source directory")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output directory must be empty (prevents stale mixed-policy features)")
    for choices, allowed in ((methods, METHODS), (transforms, TRANSFORMS), (readings, READINGS)):
        if not choices or len(set(choices)) != len(choices) or set(choices) - set(allowed):
            raise ValueError(f"Invalid or duplicate selection: {choices}")
    if language not in ("all", "hebrew") or (limit is not None and limit < 1):
        raise ValueError("Invalid language policy or limit")
    words = read_words(api)
    selected = [w for w in words if language == "all" or w.language == "hbo"]
    if limit:
        selected = selected[:limit]
    nodes = {w.node for w in selected}
    if not nodes:
        raise ValueError("No words selected")
    common = dict(author="Tony Jurg", convertedBy="gematria-tf", website="https://github.com/tonyjurg/gematria_TF",
                  coreData="BHSA", coreDataUrl="https://github.com/ETCBC/bhsa", version=lock["version"],
                  sourceCommit=lock["commit"], generatorVersion=__version__,
                  provenance="gematria-tf CLI; manifest.json contains source/output SHA-256",
                  license="CC BY-NC 4.0", licenseUrl="https://creativecommons.org/licenses/by-nc/4.0/",
                  normalization=POLICY, languagePolicy=language,
                  invalidQerePolicy="omit affected word/full values; see gem_qere_error and manifest",
                  featureNameVersion="2", coverage="partial" if limit else "complete-selected-language", nodeType="word")
    output.mkdir(parents=True, exist_ok=True)
    writer = Fabric(locations=str(output), silent="deep")
    counts = {}

    def add(name, values, description, value_type="int", **extra):
        data = {n: value for n, value in values.items() if n in nodes and value is not None}
        metadata = dict(common, description=description, valueType=value_type, **extra)
        if not writer.save(nodeFeatures={name: data}, metaData={name: metadata}, location=str(output), silent="deep"):
            raise RuntimeError(f"Text-Fabric export failed: {name}")
        path = output / f"{name}.tf"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(line for line in lines if not line.startswith("@dateWritten=")) + "\n", encoding="utf-8", newline="\n")
        # TF's feature-only API avoids loading the corpus again for every file.
        check = Fabric(locations=str(output), silent="deep").load(name, silent="deep")
        if not check or dict(check.Fs(name).items()) != data:
            raise RuntimeError(f"Round-trip data mismatch: {name}")
        counts[name] = len(data)
        print(f"Verified {name}: {len(data):,} nodes", flush=True)
        del check
        gc.collect()

    for reading in readings:
        texts, starts, ends = represent(words, reading, invalid_qere="omit")
        for rep in REPRESENTATIONS:
            if rep == "lexeme" and reading != readings[0]:
                continue
            suffix = rep if rep == "lexeme" else f"{rep}_{reading}"
            source_features = {"lexeme": "lex_utf8", "word": "g_cons_utf8", "full": "g_cons_utf8 trailer_utf8 verse"}[rep]
            if reading == "qere" and rep != "lexeme":
                source_features += " qere_utf8 qere_trailer_utf8"
            extra = dict(representation=rep, reading="lexicon" if rep == "lexeme" else reading,
                         sourceFeatures=source_features, specificationVersion="1")
            add(f"gem_text_{suffix}", texts[rep], f"Normalized consonants for {suffix}", "str", **extra)
            for transform in transforms:
                for method in methods:
                    values = {n: calculate(texts[rep][n], method, transform) for n in nodes if texts[rep][n] is not None}
                    transform_id = "ident" if transform == "identity" else transform
                    name = f"gem_{method}_{suffix}_{transform_id}"
                    add(name, values, f"Mispar {method}: {suffix}; transform={transform}",
                        method=method, transform=transform, **extra)
        add(f"gem_full_start_{reading}", starts, "First BHSA word slot in full form (value is a node id)", reading=reading)
        add(f"gem_full_end_{reading}", ends, "Last BHSA word slot in full form (value is a node id)", reading=reading)
        del texts, starts, ends
        gc.collect()
    add("gem_has_qere", {w.node: int(w.qere is not None) for w in selected}, "Explicit BHSA qere entry present (including empty readings)")
    errors = qere_errors(words)
    add("gem_qere_error", errors, "Unsupported characters in source qere; affected qere word/full values are absent", "str")
    manifest = dict(generatorVersion=__version__, featureNameVersion=2, python=platform.python_version(),
                    unicodeVersion=unicodedata.unidata_version, textFabric=version("text-fabric"),
                    source=lock, methods=list(methods), transformations=list(transforms), readings=list(readings),
                    languagePolicy=language, limit=limit, wordCount=len(nodes),
                    firstNode=min(nodes), lastNode=max(nodes), normalization=POLICY,
                    qereErrors={str(n): message for n, message in errors.items()},
                    featureNodeCounts=counts,
                    generatorSourceSha256={p.name: sha256(p) for p in sorted(Path(__file__).parent.glob("*.py"))},
                    roundTripVerified=True, features={p.name: sha256(p) for p in sorted(output.glob("*.tf")) if p.is_file()})
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest

