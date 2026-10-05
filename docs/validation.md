# Validation results

## Genesis 1 example and clean TF layout — 5 October 2026

- 53 tests passed, including provenance placement, complete duplicate verse listings, separation of numerical methods, and the optional different-spellings filter.
- The new analysis notebook executed all seven code cells in a real Jupyter kernel from a directory without a repository checkout. It downloaded the published TF features and external provenance through Text-Fabric and checked the matching BHSA snapshot.
- The chapter selection contains 31 verses and 434 full written word occurrences. The default table contains 79 duplicated Hechrechi values and 76 duplicated Gadol values. Repeated spellings are included; 42 rows also involve different spellings.
- Every ToC and return link resolves. The notebook includes its actual executed table output.
- Both Python blocks in Getting started ran successfully without a clone: the native TF download route returned בראשית and 913. The dataset checksum and independent passage checks passed with the relocated manifest.
- `tf/2021` contains only the 36 feature files. The unchanged dataset manifest is now `provenance/2021/manifest.json`; future generator runs also write provenance outside their TF feature directory.

## Standard Text-Fabric source — 5 October 2026

- 49 tests passed, including native TF downloading, standard directory enforcement, failed downloads, and source checksum validation.
- BHSA was downloaded through Text-Fabric into its standard data directory; all 23 required source/dependency files matched the pinned snapshot.
- All 36 committed dataset checksums and independent BHSA examples passed against that standard copy. Existing dataset payloads remain unchanged.
- A 100-word smoke run generated and reloaded 36 features successfully.
- All five notebook code cells and all six documentation example blocks executed successfully against the standard copy.
- A separate rerun of all ten published Python blocks (two Getting started, six Worked examples, two README) passed as written. The README loading example uses the included `tf/2021` dataset and checks for load failure.
- The documentation build checks all local links. Every page includes the subtle TJ Engineering footer credit and original brand mark.
- Historical generator source hashes in the dataset manifest describe the code used for generation; later loader changes do not alter that provenance record.

## Version 0.2.0 — 2 October 2026

- 45 tests passed, including the short feature names and distinct transformation outputs.
- All 36 complete-corpus features were regenerated and reloaded through Text-Fabric.
  Every data payload is byte-identical to its version 0.1.0 counterpart; node counts
  and the pinned BHSA source are unchanged. Only names and provenance metadata changed.
- All file checksums, generator source hashes, and independent BHSA examples passed
  `scripts/verify_dataset.py`. The renamed TF files total 59,136,362 bytes.
- All five notebook code cells and all six documentation example blocks executed
  successfully with the short feature names. The notebook generated and reloaded
  a 100-word, 36-feature sample; its committed outputs remain cleared.
- All 12 notebook navigation links resolve to their explicit anchors: six contents
  entries and six Back to ToC links.

## Original release validation — 1 October 2026

Validated locally on 2026-10-01, Windows, Python 3.13.14, Text-Fabric 13.1.0, Unicode 15.1.0.

- 44 pytest tests passed, including known values, final-letter variants, Unicode,
  transformations, empty/invalid qere, language filtering, group boundaries,
  partial selection, deterministic output, and actual TF round-trip checks.
- A 100-word smoke run exercised all five numerical methods, both readings, and
  identity/Atbash/Albam: 75 numerical features plus 11 audit features.
- The full dataset generated 36 feature files (25 numerical, 11 audit) for
  426,590 source word nodes. Each file was reloaded with the Text-Fabric feature
  API and every emitted node/value compared to its original dictionary.
- Every feature file checksum was verified by `scripts/verify_dataset.py`.
  The add-on was loaded alongside BHSA for independent worked checks:
  Genesis 1:1 = 2701 when each full group is counted once; בראשית = 913;
  suffix-inclusive למינו = 136; Genesis 8:17 ketiv/qere = 102/106;
  Aramaic יגר = 213; malformed qere at node 322495 unavailable, ketiv = 120.
- A fresh download of all 23 pinned source/dependency features passed checksum
  verification and loaded 426,590 word nodes without relying on the Git checkout.
- Every code cell of `create_gematria_features.ipynb` was executed sequentially
  using Python, including sample generation, TF reload, and assertions. The
  notebook is committed with cleared outputs. This did not require a Jupyter UI.
- Source audit: 100 stratified examples, 0 normalized pointed/consonantal ketiv
  mismatches across the whole corpus, 1 malformed qere entry explicitly flagged.
- The GitHub workflow runs these unit/integration tests on Windows and Linux
  with Python 3.11 and 3.13; fresh-download BHSA smoke is available by manual dispatch.

Generated TF files total 59,135,750 bytes.
The [manifest](../provenance/2021/manifest.json) records per-feature coverage and hashes.
The single source anomaly and the limits of the orthographic full-form convention
are documented in [the source audit](bhsa-audit.md) and [representation policy](representations.md).
