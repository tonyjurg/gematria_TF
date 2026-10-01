# Validation results

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
The [manifest](../tf/2021/manifest.json) records per-feature coverage and hashes.
The single source anomaly and the limits of the orthographic full-form convention
are documented in [the source audit](bhsa-audit.md) and [representation policy](representations.md).
