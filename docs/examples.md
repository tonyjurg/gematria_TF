# Worked examples

These examples use the committed dataset with its matching BHSA source. Run them from the repository folder after completing [Getting started](getting-started.md).

## Prepare the features

```python
from pathlib import Path
from tf.fabric import Fabric

TF = Fabric(locations=[
    str(Path(".cache/bhsa/tf/2021").resolve()),
    str(Path("tf/2021").resolve()),
])
api = TF.load(" ".join([
    "gematria_text_word_ketiv",
    "gematria_text_word_qere",
    "gematria_text_full_ketiv",
    "gematria_hechrechi_word_ketiv_identity",
    "gematria_hechrechi_word_qere_identity",
    "gematria_hechrechi_full_ketiv_identity",
    "gematria_gadol_full_ketiv_identity",
    "gematria_full_start_ketiv",
    "gematria_qere_error",
]))
if not api:
    raise RuntimeError("Could not load the dataset")
F = api.F
```

## A prefix and its full written form

BHSA’s first two slots divide <span lang="he" dir="rtl">בראשית</span> into <span lang="he" dir="rtl">ב</span> and <span lang="he" dir="rtl">ראשית</span>.

```python
assert F.gematria_hechrechi_word_ketiv_identity.v(1) == 2
assert F.gematria_hechrechi_word_ketiv_identity.v(2) == 911
assert F.gematria_hechrechi_full_ketiv_identity.v(1) == 913
assert F.gematria_hechrechi_full_ketiv_identity.v(2) == 913
assert F.gematria_full_start_ketiv.v(2) == 1
```

Both slots carry the full value for convenient querying. To count the written word once, use the slot identified by `gematria_full_start_ketiv`.

## Count each full form once

```python
full_value = F.gematria_hechrechi_full_ketiv_identity
full_start = F.gematria_full_start_ketiv

# In this pinned BHSA version, Genesis 1:1 consists of slots 1–11.
verse_total = sum(
    full_value.v(w)
    for w in range(1, 12)
    if full_start.v(w) == w
)
assert verse_total == 2701
```

This sum is appropriate for the additive Hechrechi method. For Katan Mispari, calculate and reduce the intended larger unit’s total; do not add already reduced values and assume the same result.

## Compare ketiv and qere

Genesis 8:17 has a recorded reading difference at BHSA word node 3897.

```python
w = 3897
print(F.gematria_text_word_ketiv.v(w))  # הוצא
print(F.gematria_text_word_qere.v(w))   # היצא
assert F.gematria_hechrechi_word_ketiv_identity.v(w) == 102
assert F.gematria_hechrechi_word_qere_identity.v(w) == 106
```

## Find full forms with the same value

```python
matches = []
for w in F.otype.s("word"):
    if full_start.v(w) != w:
        continue
    if full_value.v(w) == 26:
        matches.append((
            api.T.sectionFromNode(w),
            F.gematria_text_full_ketiv.v(w),
        ))

for passage, text in matches[:10]:
    print(passage, text)
```

This returns matching full written forms rather than duplicate rows for their prefixes. Use the lexeme feature instead if your question concerns dictionary forms.

## Handle an unavailable source reading

The source qere at Psalms 72:17 contains unexpected digits. The dataset preserves the ketiv and flags the qere without guessing a repair.

```python
w = 322495
assert F.gematria_hechrechi_word_ketiv_identity.v(w) == 120
assert F.gematria_hechrechi_word_qere_identity.v(w) is None
print(F.gematria_qere_error.v(w))
```

Always distinguish `None` from a valid value of `0`. The [source audit](bhsa-audit.md) documents this case and other representation checks.
