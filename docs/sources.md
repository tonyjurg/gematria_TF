# Sources and citation

## Cite the dataset and its source

When using gematria_TF in research, identify the numerical method, text representation, and reading policy, as well as the dataset version. Cite both this project and BHSA.

**Suggested project citation**

> Jurg, Tony. *gematria_TF: reproducible gematria features for BHSA*. Version 0.2.0. https://github.com/tonyjurg/gematria_TF.

The repository includes a [CITATION.cff file](../CITATION.cff). Record the BHSA source commit from the [dataset manifest](../provenance/2021/manifest.json) with any published results.

**BHSA**

The base data and linguistic annotations are produced by the **Eep Talstra Centre for Bible and Computer (ETCBC), Vrije Universiteit Amsterdam**. The source project requests citation of [DOI 10.17026/dans-z6y-skyh](https://doi.org/10.17026/dans-z6y-skyh). See the [BHSA documentation](https://etcbc.github.io/bhsa/) and [source repository](https://github.com/ETCBC/bhsa).

## Gematria methods

- [Encyclopaedia Judaica, “Gematria,” hosted by Jewish Virtual Library](https://jewishvirtuallibrary.org/jsource/judaica/ejud_0002_0007_0_07165.html): numerical systems and variant conventions.
- [Jewish Encyclopedia, “Gemaṭria”](https://www.jewishencyclopedia.com/articles/6571-gematria): historical context and examples.
- [Chabad, “What Is Gematria?”](https://www.chabad.org/library/article_cdo/aid/5541252/jewish/What-Is-Gematria.htm): a traditional introductory explanation.

## Software and design references

- [Text-Fabric](https://annotation.github.io/text-fabric/tf/): the corpus model, feature format, and loading/export APIs.
- [Create_TF-IDF_Text-Fabric_features](https://github.com/tonyjurg/Create_TF-IDF_Text-Fabric_features), Tony Jurg: repository organization, production notebook sequence, metadata conventions, and export/reload approach.
- [Hebrew](https://github.com/avi-perl/Hebrew), Avrohom Perl: Unicode, grapheme, normalization, and method-design lessons. This project deliberately uses the 22-letter Sidduri convention rather than the upstream extended-final variant.
- [python-hebrew-numbers](https://github.com/OriHoch/python-hebrew-numbers), Ori Hoch: transparent letter maps and summation. Its numeral-specific geresh multiplication is not used for biblical text.
- [Unicode Normalization Forms](https://www.unicode.org/reports/tr15/): the decomposition model used during consonant extraction.
- [Doc4TF](https://tonyjurg.github.io/Doc4TF/), Tony Jurg: the sidebar-led structure and concise introductory pages that inspired this documentation site. The site’s implementation is newly written.

Full implementation attribution, inspected revisions, and retained license notices are in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
