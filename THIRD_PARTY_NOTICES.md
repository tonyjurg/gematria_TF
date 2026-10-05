# Third-party attribution and design references

- Tony Jurg, Create_TF-IDF_Text-Fabric_features, CC BY 4.0, inspected commit
  3ddaf37d91d1c34aaf2cb33604d851d5fca69e3c.
  https://github.com/tonyjurg/Create_TF-IDF_Text-Fabric_features
  Adapted organization (README, production notebook, tf/version, CITATION.cff),
  node dictionaries, Fabric.save, metadata vocabulary, reload verification and
  Dependabot conventions. Our exporter specifies a separate output directory.
- Tony Jurg, Create_TF-IDF_features_BHSA_TF, production notebook.
  https://github.com/tonyjurg/Create_TF-IDF_features_BHSA_TF/blob/main/create_tfidf_features.ipynb
  Adapted the clickable contents structure: explicit section anchors, linked
  contents entries, and Back to ToC links. The notebook declares CC BY 4.0.
- Avrohom Perl, Hebrew, MIT, inspected commit
  55d4d6786b87c40e5f43b7cb060b03bd5126a9b1.
  https://github.com/avi-perl/Hebrew
  Learned from method separation, Hebrew combining marks, presentation forms and
  grapheme-aware design. This tool extracts consonants rather than implementing
  general grapheme operations. Deliberate difference: Sidduri finals use positions
  of base letters, not the upstream 23-27 variant.
- Ori Hoch, python-hebrew-numbers, MIT, inspected commit
  0bfa3d83b7bc03c2fc27e3db4a0630f6770cdbf0.
  https://github.com/OriHoch/python-hebrew-numbers
  Inspiration: transparent letter maps and summation. Its 500-900 finals are
  classified here as Gadol, not the standard method. Its numeral geresh x1000
  behaviour is deliberately not used for biblical text.

The local implementation is newly written. The MIT notices below are retained
for the implementation references; neither project is a runtime dependency.
BHSA-derived data terms and attribution appear in LICENSE-DATA.md.

## Ori Hoch — original MIT notice
The MIT License (MIT)

Copyright (c) 2015 Ori Hoch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Avrohom Perl — original MIT notice

Copyright 2021 Avrohom Perl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
## TJ Engineering footer mark

The footer uses the existing TJ Engineering mark from https://tj-engineering.github.io/assets/logos/TJE_black.png to identify this TJ Engineering project. The mark retains its owner's rights; the documentation license does not grant rights to the brand mark.
