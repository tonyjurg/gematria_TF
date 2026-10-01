# Representation specification v1

Source: BHSA 2021 at `4db00e2157915495e1a4d3d57e41223df24775da`.
The local `gematria_tf/bhsa-lock.json` pins all loaded source files after CRLF-to-LF newline normalization, including
`otype`, `oslots`, section features, and all feature dependencies referenced by `otext` display formats. Only that snapshot is currently supported.
Changing versions requires an explicit audit and a new lock; node IDs are not
assumed compatible across versions.

The source's [lex_utf8](https://etcbc.github.io/bhsa/features/lex_utf8/) identifies
the consonantal lexeme, without lexeme disambiguation markers.
[g_cons_utf8](https://etcbc.github.io/bhsa/features/g_cons_utf8/) is the realized
consonantal slot. Although the documentation describes consonants, the actual
2021 values can include a shin/sin dot; the normalization stage removes it.

The [trailer_utf8 documentation](https://etcbc.github.io/bhsa/features/trailer_utf8/)
identifies interword material and explains why word nodes need not be separated
by spaces. This motivates our rule: join only empty trailers, with a consecutive
node and same-verse guard. Any nonempty trailer ends a group, including maqaf,
paseq, sof pasuq, spaces, and paragraph markers. Trailer letters such as paragraph
pe/samekh are never treated as words or counted. This is a project convention
for written units, not a claim that BHSA supplies a linguistic compound feature.

The surface includes pronominal suffix letters already. `g_prs_utf8` is loaded for
audit evidence only; it is not appended or used to reconstruct missing letters.
Zero-consonant slots remain empty strings and receive zero when calculated alone.
They can still participate in a full group. Missing source values (`None`) are
distinct and rejected for the mandatory inputs.

## Qere/ketiv

[qere_utf8](https://etcbc.github.io/bhsa/features/qere_utf8/) supplies recorded
reading corrections. Its [trailer counterpart](https://etcbc.github.io/bhsa/features/qere_trailer_utf8/)
can alter boundaries. The source's `otext.tf` distinguishes the full ketiv format
from a format using qere fallbacks. We explicitly select these data fields rather
than relying on a display format's fallback behaviour.

For qere output, substitute `qere_utf8` exactly when it is not `None`, including
an explicit empty reading. Independently substitute `qere_trailer_utf8` when not
`None`, including an empty trailer. Preserve BHSA word IDs, even where the qere
splits or merges what was one ketiv unit. No textual emendation or alternative
lexeme analysis is inferred. Qere perpetuum is not supplied by this algorithm.

The current pinned source has a malformed qere at Psalms 72:17 (word 322495):
`יִנֹּ97ון`, containing ASCII digits. The strict normalizer rejects this value.
Production uses the explicit `invalid_qere="omit"` policy: withhold that qere
word's normalized text/numeric values and the full values of every slot in its
group. `gematria_qere_error` records the source-word error; start/end features
remain available. The manifest records errors and actual feature node counts.
Ketiv is not affected. There is no fallback to ketiv for malformed qere: fallback
is reserved for absent qere entries. Explicit empty qere remains valid, value zero.

## Language and coverage

[languageISO](https://etcbc.github.io/bhsa/features/languageISO/) describes the
language of the lexeme: `hbo` or `arc`. Both are admitted by default and use the
same script-based numerical rules. Hebrew-only selection removes `arc` nodes
from the output, while reconstruction still sees all source neighbours. The
feature's reading, language policy and coverage are explicit metadata.

Every full group is associated with every constituent source node. Use the start
feature to deduplicate it. This also makes a prefix slot informative without
pretending it is an independently written word. Never sum repeated full values
to get verse totals. Katan Mispari also requires reducing the intended unit's
total, so sums of already reduced values are not general aggregation rules.

