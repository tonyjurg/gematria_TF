[![Tests](https://github.com/tonyjurg/gematria_TF/actions/workflows/tests.yml/badge.svg)](https://github.com/tonyjurg/gematria_TF/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-blue)](LICENSE)
[![Data: CC BY-NC 4.0](https://img.shields.io/badge/Data-CC_BY--NC_4.0-lightgrey)](LICENSE-DATA.md)

# gematria_TF

The complete dataset is in [`tf/2021`](tf/2021): **25 numerical features plus 11 audit features**, covering all 426,590 BHSA word slots with identity transformation and separate ketiv/qere readings. One malformed source qere is explicitly flagged; its affected values are unavailable.

Generate reproducible gematria features for the Hebrew Bible in **BHSA 2021**, still the latest upstream data version (verified 2026-10-01).
Each numerical method × text representation × reading × transformation is a separate
integer `.tf` node feature. The result is a Text-Fabric add-on; it contains no copy of
BHSA's `otype`, `oslots`, or other core features.

## Features

See the [generated feature catalogue](docs/features.md) for all 36 files and coverage counts.

Feature pattern | Type | Node | Meaning
---|---|---|---
`gematria_<method>_lexeme_<transform>` | `int` | `word` | Value of the normalized BHSA lexeme
`gematria_<method>_word_<reading>_<transform>` | `int` | `word` | Value of the actual consonantal BHSA word slot
`gematria_<method>_full_<reading>_<transform>` | `int` | `word` | Value of the reconstructed orthographic group
`gematria_text_lexeme`, `gematria_text_word_<reading>`, `gematria_text_full_<reading>` | `str` | `word` | Normalized input before transformation
`gematria_full_start_<reading>`, `gematria_full_end_<reading>` | `int` | `word` | First/last source word node of the group
`gematria_has_qere` | `int` | `word` | An explicit qere entry exists, including an empty entry
`gematria_qere_error` | `str` | `word` | Source qere normalization error; absent on valid entries

Default: five methods × three representations = **15 numeric features**, plus six
audit features plus an error feature. Adding qere gives 25 numeric features (lexemes are shared), plus eleven
audit features. Selecting all three transformations gives 75 numeric features with
both readings. Feature identifiers use `hechrechi` and `sidduri` consistently; other
romanizations such as Hekhreḥi, Hechrachi and Siduri refer to the same named families.

## Setup and production

Python 3.11 or newer. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

On Linux/macOS, activate with `source .venv/bin/activate`.

Download the exact pinned BHSA files and generate a small add-on:

```console
python create_gematria_features.py --fetch --limit 100 --readings ketiv qere --output output/smoke
```

Produce the complete dataset with both recorded readings:

```console
python create_gematria_features.py --fetch --readings ketiv qere --output tf/2021
```

Or select the extended matrix:

```console
python create_gematria_features.py --fetch --readings ketiv qere --transforms identity atbash albam --output output/extended/2021
```

The pinned download includes the source features needed for computation and the extra features referenced by BHSA's text-display configuration. The source download is cached under `.cache/bhsa/tf/2021`. Use `--source PATH` to
load an existing copy: all required files must match the local SHA-256 lock after CRLF-to-LF normalization.
An output directory must be empty; choose another output path for another policy.
`--limit` counts selected word slots, labels coverage **partial**, and still resolves
each full group using the entire source so the last selected slot is not truncated.

## Production notebook

[create_gematria_features.ipynb](create_gematria_features.ipynb) follows the setup →
inspect → calculate → metadata/export → reload/verify sequence in Tony Jurg's
[TF-IDF feature project](https://github.com/tonyjurg/Create_TF-IDF_Text-Fabric_features).
It calls the tested library and produces a small sample in a new directory each run.
Install Jupyter if needed with `python -m pip install jupyterlab`.
Run the local script directly; there is no package build or installation step.

## Methods

Method | Definition | Final letters | `שלום`
---|---|---|---:
`hechrechi` | Sum conventional values 1–9, 10–90, 100–400 | Same as base forms | 376
`gadol` | Conventional sum with extended final values | ך=500 ם=600 ן=700 ף=800 ץ=900 | 936
`sidduri` | Sum alphabet positions 1–22 | Same as base forms | 52
`katan` | Sum each conventional letter value reduced to one digit | Same as base forms | 16
`katan_mispari` | Digital root of the **Hechrechi total** | Same as base forms | 7

Katan does not reduce the final sum again. Katan Mispari does; the empty string has
value zero. The named variants are operational definitions, not a claim that every
historical author used identical conventions. The numerical baseline and variant
distinctions follow the [Encyclopaedia Judaica “Gematria” entry, hosted by Jewish
Virtual Library](https://jewishvirtuallibrary.org/jsource/judaica/ejud_0002_0007_0_07165.html).

Atbash and Albam are independent **letter transformations**, applied before any
weighting. Atbash reverses the 22-letter alphabet; Albam swaps its two 11-letter
halves. Both fold input finals to base forms and emit base forms without inventing
new positional finals. Consequently Gadol and Hechrechi agree after these
transformations. Identity preserves the source's final letters.

```python
from gematria_tf import calculate
assert calculate("בְּרֵאשִׁ֖ית") == 913
assert calculate("שלום", method="gadol") == 936
assert calculate("בבל", transform="atbash") == 620
```

## Text representations and reading policies

Representation | Exact source and rule
---|---
`lexeme` | Normalized `lex_utf8` on each word node; not a reconstructed root; no qere-specific lexeme invented
`word_ketiv` | Normalized `g_cons_utf8`, including inflection and suffix letters already present
`full_ketiv` | Concatenate consecutive word slots across **empty `trailer_utf8` only**, within a verse
`word_qere` | Normalized `qere_utf8` when explicitly present, otherwise `g_cons_utf8`
`full_qere` | Same grouping rule using `qere_trailer_utf8` when present, otherwise `trailer_utf8`

BHSA's first two word nodes are `ב` and `ראשית`: their separate word values are 2
and 911; both receive full-form value 913. “Full” is an operational **orthographic
unit**, not a claim about syntactic or lexical compounds. Maqaf terminates the unit.
No suffix is appended from `g_prs_utf8`: doing so would count letters twice.

Full values repeat on all constituent slots. **Do not sum them across word nodes.**
Use `node == gematria_full_start_<reading>` when counting groups. Start/end values
can point outside a limited or language-filtered output; they always refer to BHSA.

Ketiv is the default and explicitly named. Qere uses BHSA's recorded corrections,
including explicit empty strings and changed boundaries. It does not reconstruct
unrecorded/perpetual qere, infer readings from vocalization, or realign the corpus.
Lexemes remain BHSA's lexicon annotations for either reading.

The current upstream source contains one malformed qere: Psalms 72:17, node
322495, `יִנֹּ97ון`. Its qere word value and affected full-group values are omitted
and flagged in `gematria_qere_error` and the manifest; ketiv remains available.
No correction is guessed. An absent numeric value means unavailable, not zero.

`--language all` includes Hebrew (`hbo`) and Aramaic (`arc`) with the same Hebrew-script
letter weights. `--language hebrew` omits Aramaic slots rather than assigning zeros.
Groups are reconstructed before filtering, preserving the source orthography even
if a group contains a filtered neighbour. Unknown languages and missing mandatory
features fail explicitly. Read [the representation specification](docs/representations.md)
and [the source audit](docs/bhsa-audit.md).

## Normalization

NFKD decomposes Hebrew presentation forms. Hebrew vowel/cantillation marks,
punctuation, whitespace, and listed bidi controls are removed. The 22 letters and
five final forms are retained. A dagesh does not double a letter. This follows the
Unicode concerns illustrated by [avi-perl/Hebrew](https://github.com/avi-perl/Hebrew),
without needing a general grapheme library for consonant extraction. Unexpected
letters, digits, symbols, and unsupported marks raise errors instead of silently
contributing zero. There is no Hebrew numeral parser or geresh ×1000 rule.

## Loading generated features

Use the same pinned BHSA version and node numbering. A local example avoids any
assumption that a private repository can be downloaded anonymously:

```python
from pathlib import Path
from tf.fabric import Fabric

source = Path(".cache/bhsa/tf/2021").resolve()
addon = Path("output/smoke").resolve()  # or tf/2021 for a full run
TF = Fabric(locations=[str(source), str(addon)])
api = TF.load("gematria_hechrechi_full_ketiv_identity gematria_full_start_ketiv")
assert api.F.gematria_hechrechi_full_ketiv_identity.v(1) == 913
```

The generator writes and reloads one feature at a time through Text-Fabric and checks
**every node/value pair** against the calculation dictionary before recording
success. This limits memory use. `python scripts/verify_dataset.py` additionally
loads the committed module alongside BHSA and checks independently worked examples. Files carry the source version/commit, source features, method,
representation, transformation, reading, normalization, coverage, language policy,
license, and generator version. `manifest.json` records source/output checksums,
Python, Unicode, and Text-Fabric versions. Wall-clock TF headers are removed for
repeatable output; Python/Unicode environment differences remain visible in the manifest.

## Repository layout and validation

* `gematria_tf/`: independent calculator, BHSA adapter, representations, exporter, CLI, source lock.
* `tests/`: known numerical values, Unicode/finals, grouping and reading edge cases,
  actual TF export/reload, partial coverage, source validation, deterministic output.
* `scripts/audit_bhsa.py`: reproducible stratified source audit and JSON examples.
* `create_gematria_features.ipynb`: runnable production walkthrough.
* `tf/2021/`: complete module with both readings and identity transformation; no core BHSA files.
* `.github/`: Windows/Linux tests; manually triggered real-BHSA smoke;
  Dependabot conventions adapted from the reference project.

The reference has notebook sanity checks and Dependabot, but no standalone test
workflow. This project adds pytest and CI. See [validation results](docs/validation.md).

## Scholarly and technical sources

* [ETCBC BHSA documentation](https://etcbc.github.io/bhsa/) and
  [dataset citation DOI](https://doi.org/10.17026/dans-z6y-skyh).
* [Encyclopaedia Judaica, “Gematria”](https://jewishvirtuallibrary.org/jsource/judaica/ejud_0002_0007_0_07165.html):
  principal method definitions and variant conventions.
* [Jewish Encyclopedia, “Gemaṭria”](https://www.jewishencyclopedia.com/articles/6571-gematria):
  historical context. Computed equivalences alone do not establish an author's intent.
* [Chabad, “What Is Gematria?”](https://www.chabad.org/library/article_cdo/aid/5541252/jewish/What-Is-Gematria.htm):
  accessible traditional explanation and reduced letter values.
* [Text-Fabric](https://annotation.github.io/text-fabric/tf/): feature serialization and node APIs.
* [Unicode Normalization Forms](https://www.unicode.org/reports/tr15/): decomposition model.

Additional implementation references and differences are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
Advanced milui variants, manuscript comparisons, maqaf-chain aggregation, and
higher-node totals are outside version 0.1.0.

## License and citation

New Python code is [MIT](LICENSE). Documentation and the notebook are
[CC BY 4.0](LICENSE-DOCS.md), acknowledging the reference project's design.
BHSA-derived outputs and audit excerpts follow the source's
[CC BY-NC 4.0 data terms](LICENSE-DATA.md). BHSA's root software MIT file does not
replace the data terms stated in its README. Cite [this software](CITATION.cff),
BHSA, and the precise source commit recorded in your generated manifest.

