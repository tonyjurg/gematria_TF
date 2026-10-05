# Worked examples

These examples use the committed dataset with its matching BHSA source. Run them from the repository folder after completing [Getting started](getting-started.md).

## Prepare the features

```python
from pathlib import Path
from tf.fabric import Fabric
from gematria_tf.bhsa import fetch_source

source = fetch_source()
TF = Fabric(locations=[
    str(source),
    str(Path("tf/2021").resolve()),
])
api = TF.load(" ".join([
    "gem_text_word_ketiv",
    "gem_text_word_qere",
    "gem_text_full_ketiv",
    "gem_hechrechi_word_ketiv_ident",
    "gem_hechrechi_word_qere_ident",
    "gem_hechrechi_full_ketiv_ident",
    "gem_gadol_full_ketiv_ident",
    "gem_full_start_ketiv",
    "gem_qere_error",
]))
if not api:
    raise RuntimeError("Could not load the dataset")
F = api.F
```

## A prefix and its full written form

BHSA’s first two slots divide <span lang="he" dir="rtl">בראשית</span> into <span lang="he" dir="rtl">ב</span> and <span lang="he" dir="rtl">ראשית</span>.

```python
assert F.gem_hechrechi_word_ketiv_ident.v(1) == 2
assert F.gem_hechrechi_word_ketiv_ident.v(2) == 911
assert F.gem_hechrechi_full_ketiv_ident.v(1) == 913
assert F.gem_hechrechi_full_ketiv_ident.v(2) == 913
assert F.gem_full_start_ketiv.v(2) == 1
```

Both slots carry the full value for convenient querying. To count the written word once, use the slot identified by `gem_full_start_ketiv`.

## Count each full form once

```python
full_value = F.gem_hechrechi_full_ketiv_ident
full_start = F.gem_full_start_ketiv

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
print(F.gem_text_word_ketiv.v(w))  # הוצא
print(F.gem_text_word_qere.v(w))   # היצא
assert F.gem_hechrechi_word_ketiv_ident.v(w) == 102
assert F.gem_hechrechi_word_qere_ident.v(w) == 106
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
            F.gem_text_full_ketiv.v(w),
        ))

for passage, text in matches[:10]:
    print(passage, text)
```

This returns matching full written forms rather than duplicate rows for their prefixes. Use the lexeme feature instead if your question concerns dictionary forms.

## Handle an unavailable source reading

The source qere at Psalms 72:17 contains unexpected digits. The dataset preserves the ketiv and flags the qere without guessing a repair.

```python
w = 322495
assert F.gem_hechrechi_word_ketiv_ident.v(w) == 120
assert F.gem_hechrechi_word_qere_ident.v(w) is None
print(F.gem_qere_error.v(w))
```

Always distinguish `None` from a valid value of `0`. The [source audit](bhsa-audit.md) documents this case and other representation checks.


## Explore duplicate word values in Genesis 1

Open [the Genesis 1 duplicate-gematria notebook](../genesis1_duplicate_gematria.ipynb) for a complete runnable analysis. It downloads this repository's published TF features through Text-Fabric, compares **Hechrechi** and **Gadol**, and lists the matching full written words and **every verse in Genesis 1** containing each duplicated value. A clickable contents menu and Back to ToC links guide the workflow.

Repeated spellings are included by default. Set `ONLY_DIFFERENT_FORMS = True` in the notebook to show only equal values shared by different spellings. Full-form starts prevent attached-prefix slots from being counted twice. The committed notebook includes its verified table output.

```console
python -m pip install -r requirements-notebooks.txt
python -m jupyter lab genesis1_duplicate_gematria.ipynb
```
