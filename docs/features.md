# Feature catalogue

The dataset provides **25 gematria values** and **11 supporting features** for BHSA 2021, covering Hebrew and Aramaic. Each table gives a readable label and explains what the feature contains. The smaller name below each label is the exact name to use in Text-Fabric.

## Reading the tables

- **Dictionary form (lexeme):** the consonants of the dictionary form recorded by BHSA.
- **Word part:** a unit stored separately in BHSA (technically, a “word slot”). This may be a complete word or an attached part. For example, BHSA stores בראשית as ב + ראשית.
- **Full form:** adjacent slots joined into one written word under the [documented grouping rule](representations.md), including attached prefixes and suffix letters already present in the source.
- **As written (ketiv)** follows the written letters. **As read (qere)** follows the recorded alternative reading when BHSA supplies one, and otherwise uses the written letters. “As read” still means consonants only, without vowels.

“Entries” counts the BHSA word units with a stored value. A full-form value repeats on each slot in its group; it is **not** a count of distinct written words. An unavailable value is `None`, while an explicitly empty reading has numerical value `0`.

## Gematria values

All features in this section store whole numbers (`int`). No letter substitution is applied: the suffix `ident` means “identity,” or unchanged letters.

Jump to [standard values](#standard-values-mispar-hechrechi), [extended final letters](#extended-final-letters-mispar-gadol), [alphabet positions](#alphabet-positions-mispar-sidduri), [reduced letter values](#reduced-letter-values-mispar-katan), or [single-digit totals](#single-digit-totals-mispar-katan-mispari).

### Standard values — Mispar Hechrechi

Add the conventional letter values, from 1 to 400. Final letters have the same value as their ordinary forms. For example, שלום has value **376**.

Feature | What this means | Entries
---|---|---:
**Dictionary form**<br><span class="feature-id">[`gem_hechrechi_lexeme_ident`](../tf/2021/gem_hechrechi_lexeme_ident.tf)</span> | Gematria of the dictionary spelling recorded by BHSA, rather than its spelling in a particular passage. | 426,590
**Word part · as written**<br><span class="feature-id">[`gem_hechrechi_word_ketiv_ident`](../tf/2021/gem_hechrechi_word_ketiv_ident.tf)</span> | Gematria of each part stored separately in BHSA. For example, the prefix ב and the rest of בראשית receive separate values. | 426,590
**Word part · as read**<br><span class="feature-id">[`gem_hechrechi_word_qere_ident`](../tf/2021/gem_hechrechi_word_qere_ident.tf)</span> | Gematria of each separate part, using the recorded alternative reading when one exists. Otherwise, uses the written text. | 426,589
**Whole word · as written**<br><span class="feature-id">[`gem_hechrechi_full_ketiv_ident`](../tf/2021/gem_hechrechi_full_ketiv_ident.tf)</span> | Gematria of the written word after joining its attached parts. For example, ב and ראשית are counted together as בראשית. | 426,590
**Whole word · as read**<br><span class="feature-id">[`gem_hechrechi_full_qere_ident`](../tf/2021/gem_hechrechi_full_qere_ident.tf)</span> | Gematria of the joined word, using the recorded alternative reading when one exists. Includes attached parts present in the source. | 426,589

### Extended final letters — Mispar Gadol

Add the conventional values, but count final ך, ם, ן, ף, ץ as 500, 600, 700, 800, 900. For example, שלום has value **936**.

Feature | What this means | Entries
---|---|---:
**Dictionary form**<br><span class="feature-id">[`gem_gadol_lexeme_ident`](../tf/2021/gem_gadol_lexeme_ident.tf)</span> | Gematria of the dictionary spelling recorded by BHSA, rather than its spelling in a particular passage. | 426,590
**Word part · as written**<br><span class="feature-id">[`gem_gadol_word_ketiv_ident`](../tf/2021/gem_gadol_word_ketiv_ident.tf)</span> | Gematria of each part stored separately in BHSA. For example, the prefix ב and the rest of בראשית receive separate values. | 426,590
**Word part · as read**<br><span class="feature-id">[`gem_gadol_word_qere_ident`](../tf/2021/gem_gadol_word_qere_ident.tf)</span> | Gematria of each separate part, using the recorded alternative reading when one exists. Otherwise, uses the written text. | 426,589
**Whole word · as written**<br><span class="feature-id">[`gem_gadol_full_ketiv_ident`](../tf/2021/gem_gadol_full_ketiv_ident.tf)</span> | Gematria of the written word after joining its attached parts. For example, ב and ראשית are counted together as בראשית. | 426,590
**Whole word · as read**<br><span class="feature-id">[`gem_gadol_full_qere_ident`](../tf/2021/gem_gadol_full_qere_ident.tf)</span> | Gematria of the joined word, using the recorded alternative reading when one exists. Includes attached parts present in the source. | 426,589

### Alphabet positions — Mispar Sidduri

Add each letter’s position in the 22-letter alphabet. Final letters share their ordinary form’s position. For example, שלום has value **52**.

Feature | What this means | Entries
---|---|---:
**Dictionary form**<br><span class="feature-id">[`gem_sidduri_lexeme_ident`](../tf/2021/gem_sidduri_lexeme_ident.tf)</span> | Gematria of the dictionary spelling recorded by BHSA, rather than its spelling in a particular passage. | 426,590
**Word part · as written**<br><span class="feature-id">[`gem_sidduri_word_ketiv_ident`](../tf/2021/gem_sidduri_word_ketiv_ident.tf)</span> | Gematria of each part stored separately in BHSA. For example, the prefix ב and the rest of בראשית receive separate values. | 426,590
**Word part · as read**<br><span class="feature-id">[`gem_sidduri_word_qere_ident`](../tf/2021/gem_sidduri_word_qere_ident.tf)</span> | Gematria of each separate part, using the recorded alternative reading when one exists. Otherwise, uses the written text. | 426,589
**Whole word · as written**<br><span class="feature-id">[`gem_sidduri_full_ketiv_ident`](../tf/2021/gem_sidduri_full_ketiv_ident.tf)</span> | Gematria of the written word after joining its attached parts. For example, ב and ראשית are counted together as בראשית. | 426,590
**Whole word · as read**<br><span class="feature-id">[`gem_sidduri_full_qere_ident`](../tf/2021/gem_sidduri_full_qere_ident.tf)</span> | Gematria of the joined word, using the recorded alternative reading when one exists. Includes attached parts present in the source. | 426,589

### Reduced letter values — Mispar Katan

Reduce each conventional letter value to one digit, then add those digits. Leave the resulting total unreduced. For example, שלום has value **16**.

Feature | What this means | Entries
---|---|---:
**Dictionary form**<br><span class="feature-id">[`gem_katan_lexeme_ident`](../tf/2021/gem_katan_lexeme_ident.tf)</span> | Gematria of the dictionary spelling recorded by BHSA, rather than its spelling in a particular passage. | 426,590
**Word part · as written**<br><span class="feature-id">[`gem_katan_word_ketiv_ident`](../tf/2021/gem_katan_word_ketiv_ident.tf)</span> | Gematria of each part stored separately in BHSA. For example, the prefix ב and the rest of בראשית receive separate values. | 426,590
**Word part · as read**<br><span class="feature-id">[`gem_katan_word_qere_ident`](../tf/2021/gem_katan_word_qere_ident.tf)</span> | Gematria of each separate part, using the recorded alternative reading when one exists. Otherwise, uses the written text. | 426,589
**Whole word · as written**<br><span class="feature-id">[`gem_katan_full_ketiv_ident`](../tf/2021/gem_katan_full_ketiv_ident.tf)</span> | Gematria of the written word after joining its attached parts. For example, ב and ראשית are counted together as בראשית. | 426,590
**Whole word · as read**<br><span class="feature-id">[`gem_katan_full_qere_ident`](../tf/2021/gem_katan_full_qere_ident.tf)</span> | Gematria of the joined word, using the recorded alternative reading when one exists. Includes attached parts present in the source. | 426,589

### Single-digit totals — Mispar Katan Mispari

Reduce the standard gematria total repeatedly to a single digit. For example, שלום changes from 376 to 16 to **7**. An empty form has value 0.

Feature | What this means | Entries
---|---|---:
**Dictionary form**<br><span class="feature-id">[`gem_katan_mispari_lexeme_ident`](../tf/2021/gem_katan_mispari_lexeme_ident.tf)</span> | Gematria of the dictionary spelling recorded by BHSA, rather than its spelling in a particular passage. | 426,590
**Word part · as written**<br><span class="feature-id">[`gem_katan_mispari_word_ketiv_ident`](../tf/2021/gem_katan_mispari_word_ketiv_ident.tf)</span> | Gematria of each part stored separately in BHSA. For example, the prefix ב and the rest of בראשית receive separate values. | 426,590
**Word part · as read**<br><span class="feature-id">[`gem_katan_mispari_word_qere_ident`](../tf/2021/gem_katan_mispari_word_qere_ident.tf)</span> | Gematria of each separate part, using the recorded alternative reading when one exists. Otherwise, uses the written text. | 426,589
**Whole word · as written**<br><span class="feature-id">[`gem_katan_mispari_full_ketiv_ident`](../tf/2021/gem_katan_mispari_full_ketiv_ident.tf)</span> | Gematria of the written word after joining its attached parts. For example, ב and ראשית are counted together as בראשית. | 426,590
**Whole word · as read**<br><span class="feature-id">[`gem_katan_mispari_full_qere_ident`](../tf/2021/gem_katan_mispari_full_qere_ident.tf)</span> | Gematria of the joined word, using the recorded alternative reading when one exists. Includes attached parts present in the source. | 426,589

## Text used for the calculation

These features store Hebrew-script consonants as text (`str`). They let you inspect exactly which letters supplied the numerical value. Vowel points, cantillation, punctuation, and spacing have been removed.

Feature | What this means | Entries
---|---|---:
**Dictionary spelling**<br><span class="feature-id">[`gem_text_lexeme`](../tf/2021/gem_text_lexeme.tf)</span> | The letters of the dictionary form that were used in the calculation. | 426,590
**Letters · as written**<br><span class="feature-id">[`gem_text_word_ketiv`](../tf/2021/gem_text_word_ketiv.tf)</span> | The written letters of each part stored separately in BHSA. Use this to see exactly what was counted. | 426,590
**Letters · as read**<br><span class="feature-id">[`gem_text_word_qere`](../tf/2021/gem_text_word_qere.tf)</span> | The letters of each separate part, using the recorded alternative reading where available. | 426,589
**Whole-word spelling · as written**<br><span class="feature-id">[`gem_text_full_ketiv`](../tf/2021/gem_text_full_ketiv.tf)</span> | The written letters with attached parts joined together; for example, בראשית instead of separate ב and ראשית. | 426,590
**Whole-word spelling · as read**<br><span class="feature-id">[`gem_text_full_qere`](../tf/2021/gem_text_full_qere.tf)</span> | The letters of the joined word, using the recorded alternative reading where available. | 426,589

## Boundaries of a full form

These features store BHSA word-node identifiers as whole numbers (`int`). They show where each reconstructed full form starts and ends. **To count each full form once, keep only slots whose node ID equals the corresponding start value.** See the [worked example](examples.md#count-each-full-form-once).

Feature | What this means | Entries
---|---|---:
**First part · written word**<br><span class="feature-id">[`gem_full_start_ketiv`](../tf/2021/gem_full_start_ketiv.tf)</span> | The BHSA ID number of the first part of the joined written word. Use it to count each whole word only once. | 426,590
**Last part · written word**<br><span class="feature-id">[`gem_full_end_ketiv`](../tf/2021/gem_full_end_ketiv.tf)</span> | The BHSA ID number of the last part of the joined written word. Shows where that word ends. | 426,590
**First part · recorded reading**<br><span class="feature-id">[`gem_full_start_qere`](../tf/2021/gem_full_start_qere.tf)</span> | The BHSA ID number of the first part of the joined word when using the recorded reading. Use it to count each whole word only once. | 426,590
**Last part · recorded reading**<br><span class="feature-id">[`gem_full_end_qere`](../tf/2021/gem_full_end_qere.tf)</span> | The BHSA ID number of the last part of the joined word when using the recorded reading. Shows where that word ends. | 426,590

## Reading checks

These two features help you identify explicit alternative readings and the one source entry that cannot be calculated.

Feature | What this means | Entries
---|---|---:
**Is there an alternative reading?**<br><span class="feature-id">[`gem_has_qere`](../tf/2021/gem_has_qere.tf)</span> | 1 means yes; 0 means no. An explicitly recorded empty reading also counts as yes. | 426,590
**Why a reading is unavailable**<br><span class="feature-id">[`gem_qere_error`](../tf/2021/gem_qere_error.tf)</span> | An explanation of a character problem in the recorded reading. Only entries with a problem have a message. | 1

One malformed qere at **word node 322495 (Psalm 72:17)** is recorded in `gem_qere_error`. Its qere text and numerical values are unavailable; its written-text and dictionary-form values remain present. This explains the coverage of 426,589 for affected features. Start/end identifiers remain available.

For exact definitions and provenance, see [Methods and conventions](methods.md), [Text representations](representations.md), the [Source audit](bhsa-audit.md), and the [Dataset manifest](../tf/2021/manifest.json).

