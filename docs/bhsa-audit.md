# BHSA source and representation audit

Audit date: 2026-10-01. The newest upstream data directory and the current app
default are both **2021**. The current upstream HEAD was verified as
`4db00e2157915495e1a4d3d57e41223df24775da` (the repository release tag v1.8.1 is
distinct from the data version). The input is the current upstream snapshot,
not an older release archive.

Run `python scripts/audit_bhsa.py` from the repository root to reproduce
[bhsa-audit.json](bhsa-audit.json). This performs a full-corpus character and
representation audit and collects 100 deterministic examples, stratified by
prefixes, suffixes, reading changes, empty slots, final letters, Aramaic, maqaf,
and inflection, with additional examples spread through the corpus. These are
machine-selected examples; the table below records inspected illustrative cases.

Measure | Count
---|---:
Word slots | 426,590
Hebrew slots | 420,484
Aramaic slots | 6,106
Slots belonging to multi-slot ketiv groups | 231,810
Slots with a nonempty pronominal suffix feature | 43,175
Explicit qere entries | 1,892
Explicit empty qere entries | 25
Qere trailers differing from ketiv trailers | 133
Trailers containing maqaf | 42,275
Empty consonantal word slots | 6,488
Normalized pointed/consonantal ketiv discrepancies | 0
Malformed qere entries | 1

Example | Source nodes | Observation
---|---|---
Genesis 1:1 | 1–2 | `ב` + `ראשית` → full `בראשית`; 2 + 911 = 913
Genesis 1:5 | 61–63 | An empty article slot lies within `לאור`; no letter is invented
Genesis 1:11 | 193–194 | `ל` + `מינו` → `למינו`; suffix `ו` is already present
Genesis 1:11 | 196 | `זרעו` is followed by maqaf; maqaf terminates this project's full unit
Genesis 8:17 | 3897 | Ketiv `הוצא` = 102; qere `היצא` = 106
Genesis 9:21 | 4420 | Ketiv `אהלה`; qere `אהלו`; reading trailer is preserved separately
Genesis 31:47 | 17278–17279 | Aramaic `יגר שהדותא`; the same script weights apply by explicit policy
Psalms 72:17 | 322495 | Malformed qere `יִנֹּ97ון` is flagged and omitted; ketiv `ינין` remains 120

The full-corpus equality of normalized `g_word_utf8` and `g_cons_utf8` supports
using the latter for the ketiv consonantal representation. No morphological
suffix reconstruction is necessary. Empty slots and altered qere boundaries
justify retaining BHSA slot IDs and computing full groups before filtering.

The 100-row audit is not a critical edition or an exhaustive philological review.
It records the operational consequences of this specific BHSA snapshot.

