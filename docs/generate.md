# Regenerate or extend

You do not need to generate anything to use the committed dataset. These instructions are for researchers who want to reproduce it or select different methods, readings, or transformations.

## Reproduce the committed combinations

From the repository root, after [setting up Python](getting-started.md):

```console
python create_gematria_features.py --fetch --readings ketiv qere --output output/reproduced/2021
```

This writes the five methods for lexeme, word, and full representations, with identity transformation and both readings. It creates **36 feature files** and a provenance manifest. It does not overwrite the dataset in `tf/2021`.

Use an **empty output directory** for each run. The generator refuses to mix results from different policies in an existing directory.

## Try a small sample first

```console
python create_gematria_features.py --fetch --limit 100 --readings ketiv qere --output output/sample/2021
```

`--limit 100` selects the first 100 word slots and labels the output as partial. Full forms are still reconstructed from the complete source, so a group is not cut off at the sample boundary.

## Add Atbash and Albam

```console
python create_gematria_features.py --fetch --readings ketiv qere --transforms identity atbash albam --output output/extended/2021
```

This produces **75 numerical features** plus the 11 audit features. Transformation names appear in the feature names (`ident` for `identity`; `atbash` and `albam` unchanged), so their values remain distinct from the identity results.

## Other choices

Option | Effect
---|---
`--methods hechrechi gadol` | Generate only the named numerical methods
`--readings ketiv` | Use the written text; lexeme features remain included
`--language hebrew` | Omit Aramaic slots from output
`--source PATH` | Use an existing source directory matching the pinned checksums
`--help` | Show all options

Groups are reconstructed before language filtering. Start/end features refer to the original BHSA node IDs, including neighbours outside a filtered or limited output.

## Check the result

The generator reloads each `.tf` file through Text-Fabric and compares every emitted node/value pair to the calculated values. `manifest.json` records the exact source and feature checksums, settings, software versions, and unavailable readings.

To verify the **committed** dataset and its worked examples:

```console
python scripts/verify_dataset.py
```

To run the local tests:

```console
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

See [validation results](validation.md) and the [production notebook](../create_gematria_features.ipynb) for more detail.
