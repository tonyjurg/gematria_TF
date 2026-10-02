"""Check the committed dataset's hashes and independently worked BHSA examples.

Run from the repository root after fetching BHSA: python scripts/verify_dataset.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gematria_tf import __version__
from gematria_tf.bhsa import sha256, source_lock
from tf.fabric import Fabric


def main():
    output = Path("tf/2021").resolve()
    source = Path(".cache/bhsa/tf/2021").resolve()
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["source"] == source_lock()
    assert manifest["wordCount"] == 426590
    assert manifest["limit"] is None
    assert manifest["roundTripVerified"]
    assert manifest["generatorVersion"] == __version__
    assert manifest["featureNameVersion"] == 2
    assert set(manifest["features"]) == {p.name for p in output.glob("*.tf") if p.is_file()}
    for name, expected in manifest["generatorSourceSha256"].items():
        assert sha256(Path("gematria_tf") / name) == expected, name
    for name, expected in manifest["features"].items():
        assert sha256(output / name) == expected, name
    names = "gem_hechrechi_full_ketiv_ident gem_hechrechi_word_ketiv_ident gem_hechrechi_word_qere_ident gem_full_start_ketiv gem_qere_error"
    api = Fabric(locations=[str(source), str(output)], silent="deep").load(names, silent="deep")
    assert api
    F = api.F
    assert [F.gem_hechrechi_full_ketiv_ident.v(n) for n in (1, 3, 4, 5, 6, 8, 10)] == [913, 203, 86, 401, 395, 407, 296]
    assert sum(F.gem_hechrechi_full_ketiv_ident.v(n) for n in range(1, 12) if F.gem_full_start_ketiv.v(n) == n) == 2701
    assert F.gem_hechrechi_word_ketiv_ident.v(194) == 106
    assert F.gem_hechrechi_full_ketiv_ident.v(194) == 136
    assert F.gem_hechrechi_word_ketiv_ident.v(3897) == 102
    assert F.gem_hechrechi_word_qere_ident.v(3897) == 106
    assert F.gem_hechrechi_word_ketiv_ident.v(17278) == 213
    assert F.gem_hechrechi_word_ketiv_ident.v(322495) == 120
    assert F.gem_hechrechi_word_qere_ident.v(322495) is None
    assert "U+0039" in F.gem_qere_error.v(322495)
    print("All dataset checksums and independent BHSA examples verified")


if __name__ == "__main__":
    main()
