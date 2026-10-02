# Generated feature catalogue

BHSA 2021; identity transformation; Hebrew and Aramaic; ketiv and qere.

Feature | Type | Available word nodes
---|---|---:
[gem_full_end_ketiv](../tf/2021/gem_full_end_ketiv.tf) | `int` | 426,590
[gem_full_end_qere](../tf/2021/gem_full_end_qere.tf) | `int` | 426,590
[gem_full_start_ketiv](../tf/2021/gem_full_start_ketiv.tf) | `int` | 426,590
[gem_full_start_qere](../tf/2021/gem_full_start_qere.tf) | `int` | 426,590
[gem_gadol_full_ketiv_ident](../tf/2021/gem_gadol_full_ketiv_ident.tf) | `int` | 426,590
[gem_gadol_full_qere_ident](../tf/2021/gem_gadol_full_qere_ident.tf) | `int` | 426,589
[gem_gadol_lexeme_ident](../tf/2021/gem_gadol_lexeme_ident.tf) | `int` | 426,590
[gem_gadol_word_ketiv_ident](../tf/2021/gem_gadol_word_ketiv_ident.tf) | `int` | 426,590
[gem_gadol_word_qere_ident](../tf/2021/gem_gadol_word_qere_ident.tf) | `int` | 426,589
[gem_has_qere](../tf/2021/gem_has_qere.tf) | `int` | 426,590
[gem_hechrechi_full_ketiv_ident](../tf/2021/gem_hechrechi_full_ketiv_ident.tf) | `int` | 426,590
[gem_hechrechi_full_qere_ident](../tf/2021/gem_hechrechi_full_qere_ident.tf) | `int` | 426,589
[gem_hechrechi_lexeme_ident](../tf/2021/gem_hechrechi_lexeme_ident.tf) | `int` | 426,590
[gem_hechrechi_word_ketiv_ident](../tf/2021/gem_hechrechi_word_ketiv_ident.tf) | `int` | 426,590
[gem_hechrechi_word_qere_ident](../tf/2021/gem_hechrechi_word_qere_ident.tf) | `int` | 426,589
[gem_katan_full_ketiv_ident](../tf/2021/gem_katan_full_ketiv_ident.tf) | `int` | 426,590
[gem_katan_full_qere_ident](../tf/2021/gem_katan_full_qere_ident.tf) | `int` | 426,589
[gem_katan_lexeme_ident](../tf/2021/gem_katan_lexeme_ident.tf) | `int` | 426,590
[gem_katan_mispari_full_ketiv_ident](../tf/2021/gem_katan_mispari_full_ketiv_ident.tf) | `int` | 426,590
[gem_katan_mispari_full_qere_ident](../tf/2021/gem_katan_mispari_full_qere_ident.tf) | `int` | 426,589
[gem_katan_mispari_lexeme_ident](../tf/2021/gem_katan_mispari_lexeme_ident.tf) | `int` | 426,590
[gem_katan_mispari_word_ketiv_ident](../tf/2021/gem_katan_mispari_word_ketiv_ident.tf) | `int` | 426,590
[gem_katan_mispari_word_qere_ident](../tf/2021/gem_katan_mispari_word_qere_ident.tf) | `int` | 426,589
[gem_katan_word_ketiv_ident](../tf/2021/gem_katan_word_ketiv_ident.tf) | `int` | 426,590
[gem_katan_word_qere_ident](../tf/2021/gem_katan_word_qere_ident.tf) | `int` | 426,589
[gem_qere_error](../tf/2021/gem_qere_error.tf) | `str` | 1
[gem_sidduri_full_ketiv_ident](../tf/2021/gem_sidduri_full_ketiv_ident.tf) | `int` | 426,590
[gem_sidduri_full_qere_ident](../tf/2021/gem_sidduri_full_qere_ident.tf) | `int` | 426,589
[gem_sidduri_lexeme_ident](../tf/2021/gem_sidduri_lexeme_ident.tf) | `int` | 426,590
[gem_sidduri_word_ketiv_ident](../tf/2021/gem_sidduri_word_ketiv_ident.tf) | `int` | 426,590
[gem_sidduri_word_qere_ident](../tf/2021/gem_sidduri_word_qere_ident.tf) | `int` | 426,589
[gem_text_full_ketiv](../tf/2021/gem_text_full_ketiv.tf) | `str` | 426,590
[gem_text_full_qere](../tf/2021/gem_text_full_qere.tf) | `str` | 426,589
[gem_text_lexeme](../tf/2021/gem_text_lexeme.tf) | `str` | 426,590
[gem_text_word_ketiv](../tf/2021/gem_text_word_ketiv.tf) | `str` | 426,590
[gem_text_word_qere](../tf/2021/gem_text_word_qere.tf) | `str` | 426,589

One malformed qere at word 322495 is recorded in `gem_qere_error`; its qere numeric and text features are absent. All ketiv and lexeme values are present. Full start/end values refer to BHSA word node IDs, not counts.

See [representations](representations.md), [source audit](bhsa-audit.md), and [manifest](../tf/2021/manifest.json) for exact definitions and provenance.

## Short feature names

Dataset version **0.2.0** shortens every feature prefix from `gematria_` to `gem_`, and the identity suffix from `_identity` to `_ident`. For example, `gematria_hechrechi_full_ketiv_identity` becomes `gem_hechrechi_full_ketiv_ident`, and `gematria_text_full_ketiv` becomes `gem_text_full_ketiv`.

Update feature lists and `F.<feature>` / `Fs("<feature>")` calls in existing scripts. Replace the old add-on directory with the new 36-file set when upgrading; do not overlay the new files on an old installation, which would leave both names present. The dataset contains no duplicate aliases. Node IDs and values are unchanged. Numerical method names, `atbash`, `albam`, and the CLI option `--transforms identity` remain unchanged.
