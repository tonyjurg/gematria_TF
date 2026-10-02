# Feature catalogue

The dataset provides **25 gematria values** and **11 supporting features** for BHSA 2021, covering Hebrew and Aramaic. Use the descriptions below to choose a feature; use its exact name in Text-Fabric.

## Reading the tables

- **Dictionary form (lexeme):** the consonants of the dictionary form recorded by BHSA.
- **Word slot:** one unit in BHSA. An attached prefix can occupy a separate slot from the rest of a written word.
- **Full form:** adjacent slots joined into one written word under the [documented grouping rule](representations.md), including attached prefixes and suffix letters already present in the source.
- **Written text (ketiv)** uses the recorded consonants. **Recorded reading (qere)** uses an explicit alternative reading when BHSA supplies one, and otherwise uses the written text.

“Word slots covered” counts the BHSA slots with a stored value. A full-form value repeats on each slot in its group; it is **not** a count of distinct written words. An unavailable value is `None`, while an explicitly empty reading has numerical value `0`.

## Gematria values

All features in this section store whole numbers (`int`). No letter substitution is applied: the suffix `ident` means “identity,” or unchanged letters.

Jump to [standard values](#standard-values-mispar-hechrechi), [extended final letters](#extended-final-letters-mispar-gadol), [alphabet positions](#alphabet-positions-mispar-sidduri), [reduced letter values](#reduced-letter-values-mispar-katan), or [single-digit totals](#single-digit-totals-mispar-katan-mispari).

### Standard values — Mispar Hechrechi

Add the conventional letter values, from 1 to 400. Final letters have the same value as their ordinary forms. For example, שלום has value **376**.

What it gives you | Feature name | Word slots covered
---|---|---:
Value of the dictionary form, shared by both readings. | [`gem_hechrechi_lexeme_ident`](../tf/2021/gem_hechrechi_lexeme_ident.tf) | 426,590
Value of one word slot in the written text (ketiv). | [`gem_hechrechi_word_ketiv_ident`](../tf/2021/gem_hechrechi_word_ketiv_ident.tf) | 426,590
Value of one word slot in the recorded reading (qere). | [`gem_hechrechi_word_qere_ident`](../tf/2021/gem_hechrechi_word_qere_ident.tf) | 426,589
Value of the full written word with its attached parts (ketiv). | [`gem_hechrechi_full_ketiv_ident`](../tf/2021/gem_hechrechi_full_ketiv_ident.tf) | 426,590
Value of the full word with its attached parts in the recorded reading (qere). | [`gem_hechrechi_full_qere_ident`](../tf/2021/gem_hechrechi_full_qere_ident.tf) | 426,589

### Extended final letters — Mispar Gadol

Add the conventional values, but count final ך, ם, ן, ף, ץ as 500, 600, 700, 800, 900. For example, שלום has value **936**.

What it gives you | Feature name | Word slots covered
---|---|---:
Value of the dictionary form, shared by both readings. | [`gem_gadol_lexeme_ident`](../tf/2021/gem_gadol_lexeme_ident.tf) | 426,590
Value of one word slot in the written text (ketiv). | [`gem_gadol_word_ketiv_ident`](../tf/2021/gem_gadol_word_ketiv_ident.tf) | 426,590
Value of one word slot in the recorded reading (qere). | [`gem_gadol_word_qere_ident`](../tf/2021/gem_gadol_word_qere_ident.tf) | 426,589
Value of the full written word with its attached parts (ketiv). | [`gem_gadol_full_ketiv_ident`](../tf/2021/gem_gadol_full_ketiv_ident.tf) | 426,590
Value of the full word with its attached parts in the recorded reading (qere). | [`gem_gadol_full_qere_ident`](../tf/2021/gem_gadol_full_qere_ident.tf) | 426,589

### Alphabet positions — Mispar Sidduri

Add each letter’s position in the 22-letter alphabet. Final letters share their ordinary form’s position. For example, שלום has value **52**.

What it gives you | Feature name | Word slots covered
---|---|---:
Value of the dictionary form, shared by both readings. | [`gem_sidduri_lexeme_ident`](../tf/2021/gem_sidduri_lexeme_ident.tf) | 426,590
Value of one word slot in the written text (ketiv). | [`gem_sidduri_word_ketiv_ident`](../tf/2021/gem_sidduri_word_ketiv_ident.tf) | 426,590
Value of one word slot in the recorded reading (qere). | [`gem_sidduri_word_qere_ident`](../tf/2021/gem_sidduri_word_qere_ident.tf) | 426,589
Value of the full written word with its attached parts (ketiv). | [`gem_sidduri_full_ketiv_ident`](../tf/2021/gem_sidduri_full_ketiv_ident.tf) | 426,590
Value of the full word with its attached parts in the recorded reading (qere). | [`gem_sidduri_full_qere_ident`](../tf/2021/gem_sidduri_full_qere_ident.tf) | 426,589

### Reduced letter values — Mispar Katan

Reduce each conventional letter value to one digit, then add those digits. Leave the resulting total unreduced. For example, שלום has value **16**.

What it gives you | Feature name | Word slots covered
---|---|---:
Value of the dictionary form, shared by both readings. | [`gem_katan_lexeme_ident`](../tf/2021/gem_katan_lexeme_ident.tf) | 426,590
Value of one word slot in the written text (ketiv). | [`gem_katan_word_ketiv_ident`](../tf/2021/gem_katan_word_ketiv_ident.tf) | 426,590
Value of one word slot in the recorded reading (qere). | [`gem_katan_word_qere_ident`](../tf/2021/gem_katan_word_qere_ident.tf) | 426,589
Value of the full written word with its attached parts (ketiv). | [`gem_katan_full_ketiv_ident`](../tf/2021/gem_katan_full_ketiv_ident.tf) | 426,590
Value of the full word with its attached parts in the recorded reading (qere). | [`gem_katan_full_qere_ident`](../tf/2021/gem_katan_full_qere_ident.tf) | 426,589

### Single-digit totals — Mispar Katan Mispari

Reduce the standard gematria total repeatedly to a single digit. For example, שלום changes from 376 to 16 to **7**. An empty form has value 0.

What it gives you | Feature name | Word slots covered
---|---|---:
Value of the dictionary form, shared by both readings. | [`gem_katan_mispari_lexeme_ident`](../tf/2021/gem_katan_mispari_lexeme_ident.tf) | 426,590
Value of one word slot in the written text (ketiv). | [`gem_katan_mispari_word_ketiv_ident`](../tf/2021/gem_katan_mispari_word_ketiv_ident.tf) | 426,590
Value of one word slot in the recorded reading (qere). | [`gem_katan_mispari_word_qere_ident`](../tf/2021/gem_katan_mispari_word_qere_ident.tf) | 426,589
Value of the full written word with its attached parts (ketiv). | [`gem_katan_mispari_full_ketiv_ident`](../tf/2021/gem_katan_mispari_full_ketiv_ident.tf) | 426,590
Value of the full word with its attached parts in the recorded reading (qere). | [`gem_katan_mispari_full_qere_ident`](../tf/2021/gem_katan_mispari_full_qere_ident.tf) | 426,589

## Text used for the calculation

These features store Hebrew-script consonants as text (`str`). They let you inspect exactly which letters supplied the numerical value. Vowel points, cantillation, punctuation, and spacing have been removed.

What it gives you | Feature name | Word slots covered
---|---|---:
Letters of the dictionary form recorded by BHSA. | [`gem_text_lexeme`](../tf/2021/gem_text_lexeme.tf) | 426,590
Letters of one word slot in the written text (ketiv). | [`gem_text_word_ketiv`](../tf/2021/gem_text_word_ketiv.tf) | 426,590
Letters of one word slot in the recorded reading (qere). | [`gem_text_word_qere`](../tf/2021/gem_text_word_qere.tf) | 426,589
Letters of the full written word, including its attached parts (ketiv). | [`gem_text_full_ketiv`](../tf/2021/gem_text_full_ketiv.tf) | 426,590
Letters of the full word and its attached parts in the recorded reading (qere). | [`gem_text_full_qere`](../tf/2021/gem_text_full_qere.tf) | 426,589

## Boundaries of a full form

These features store BHSA word-node identifiers as whole numbers (`int`). They show where each reconstructed full form starts and ends. **To count each full form once, keep only slots whose node ID equals the corresponding start value.** See the [worked example](examples.md#count-each-full-form-once).

What it gives you | Feature name | Word slots covered
---|---|---:
Node ID of the first slot in this full written form (ketiv). | [`gem_full_start_ketiv`](../tf/2021/gem_full_start_ketiv.tf) | 426,590
Node ID of the last slot in this full written form (ketiv). | [`gem_full_end_ketiv`](../tf/2021/gem_full_end_ketiv.tf) | 426,590
Node ID of the first slot in this full form under the recorded reading (qere). | [`gem_full_start_qere`](../tf/2021/gem_full_start_qere.tf) | 426,590
Node ID of the last slot in this full form under the recorded reading (qere). | [`gem_full_end_qere`](../tf/2021/gem_full_end_qere.tf) | 426,590

## Reading checks

These two features help you identify explicit alternative readings and the one source entry that cannot be calculated.

What it gives you | Feature name | Word slots covered
---|---|---:
**Alternative-reading flag** (`int`): 1 if BHSA explicitly records a qere, including an empty reading; 0 otherwise. | [`gem_has_qere`](../tf/2021/gem_has_qere.tf) | 426,590
**Reading error message** (`str`): explains an unsupported character in the source qere. Absent when there is no error. | [`gem_qere_error`](../tf/2021/gem_qere_error.tf) | 1

One malformed qere at **word node 322495 (Psalm 72:17)** is recorded in `gem_qere_error`. Its qere text and numerical values are unavailable; its written-text and dictionary-form values remain present. This explains the coverage of 426,589 for affected features. Start/end identifiers remain available.

For exact definitions and provenance, see [Methods and conventions](methods.md), [Text representations](representations.md), the [Source audit](bhsa-audit.md), and the [Dataset manifest](../tf/2021/manifest.json).

## Short feature names

Dataset version **0.2.0** shortens every feature prefix from `gematria_` to `gem_`, and the identity suffix from `_identity` to `_ident`. For example, `gematria_hechrechi_full_ketiv_identity` becomes `gem_hechrechi_full_ketiv_ident`, and `gematria_text_full_ketiv` becomes `gem_text_full_ketiv`.

Update feature lists and `F.<feature>` / `Fs("<feature>")` calls in existing scripts. Replace the old add-on directory with the new 36-file set when upgrading; do not overlay the new files on an old installation, which would leave both names present. The dataset contains no duplicate aliases. Node IDs and values are unchanged. Numerical method names, `atbash`, `albam`, and the CLI option `--transforms identity` remain unchanged.
