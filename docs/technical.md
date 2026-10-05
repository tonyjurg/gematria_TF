# Technical reference

These pages document the exact definitions and evidence behind the dataset. They are the original project reference material, now available within the documentation site.

## Feature catalogue

[Browse all 36 generated features](features.md), their data types, and the number of word nodes with available values. Each file link opens the corresponding file in the GitHub repository.

## Representation specification

[Read the representation policy](representations.md) for the exact BHSA fields, full-form grouping rule, qere/ketiv handling, Aramaic policy, normalization, and missing values.

## Source audit

[Read the BHSA audit](bhsa-audit.md) for corpus-wide checks and representative passages. The [100-example JSON audit](bhsa-audit.json) provides structured observations for further inspection.

## Validation

[Read the validation report](validation.md), covering the numerical tests, file round trips, notebook execution, fresh source download, and independent passage checks. The [GitHub test workflow](https://github.com/tonyjurg/gematria_TF/actions/workflows/tests.yml) contains subsequent automated runs.

## Provenance files

- [Dataset manifest](../provenance/2021/manifest.json): source snapshot, selected combinations, coverage, errors, and checksums.
- [BHSA source lock](../gematria_tf/bhsa-lock.json): version and checksums of the input features.
- [Source code](../gematria_tf): local calculation, representation, and generation logic.
- [Production notebook](../create_gematria_features.ipynb): the executable walkthrough.
- [Genesis 1 duplicate-gematria notebook](../genesis1_duplicate_gematria.ipynb): a complete native TF download and two-method analysis with a verse table.

## Maintaining this documentation

The site is built from Markdown in `/docs`. The builder keeps reference pages within the site and directs links to dataset and code files to GitHub. See [Building and publishing the site](publishing.md) for the local preview and GitHub Pages setup.

- [Genesis 1 duplicate-gematria notebook](../genesis1_duplicate_gematria.ipynb): a complete native TF download and two-method analysis with a verse table.
