# Methods and conventions

All five methods operate on consonants. Vowels, cantillation marks, punctuation, and spacing do not contribute to the value. Final letter forms are preserved until the selected method determines their weight.

## Five numerical methods

Method | Rule | Value of שלום
---|---|---:
**Mispar Hechrechi** (`hechrechi`) | Standard letter values: א–ט = 1–9; י–צ = 10–90; ק–ת = 100–400 | 376
**Mispar Gadol** (`gadol`) | Standard values, but final ך ם ן ף ץ receive 500, 600, 700, 800, 900 | 936
**Mispar Sidduri** (`sidduri`) | Positions in the 22-letter alphabet; final letters share their base letter’s position | 52
**Mispar Katan** (`katan`) | Reduce each standard letter value to one digit, then sum the results | 16
**Mispar Katan Mispari** (`katan_mispari`) | Reduce the total Hechrechi value repeatedly to a single digit | 7

These are explicit conventions for this dataset. Historical and modern sources sometimes use the same names for different variants. In particular, this dataset’s Sidduri does **not** assign positions 23–27 to final letters.

## A worked calculation

For <span lang="he" dir="rtl">שלום</span> (*shalom*):

- **Hechrechi:** 300 + 30 + 6 + 40 = **376**.
- **Gadol:** the final mem changes from 40 to 600, giving **936**.
- **Sidduri:** 21 + 12 + 6 + 13 = **52**.
- **Katan:** 3 + 3 + 6 + 4 = **16**. The sum is left at 16.
- **Katan Mispari:** 376 → 3 + 7 + 6 = 16 → 1 + 6 = **7**.

An explicitly empty textual form has value **0**. An unavailable reading has no value; in Text-Fabric that is `None`, not zero.

## Text choice matters too

A lexeme, an inflected wordform, and a full form with attached prefixes can have different consonants. Choose the representation that matches your research question before comparing values. The [representation specification](representations.md) defines the exact BHSA fields and grouping rules.

Ketiv uses the written consonants. Qere uses BHSA’s explicit recorded reading where present and otherwise falls back to the written form. No unrecorded reading or corrected lexeme is inferred. Aramaic words use the same Hebrew-script letter weights.

## Atbash and Albam

These are **letter substitutions**, separate from numerical weighting:

- **Atbash** reverses the 22-letter alphabet: א ↔ ת, ב ↔ ש, and so on.
- **Albam** exchanges the two halves of the alphabet: א ↔ ל, ב ↔ מ, and so on.

The substitutions first treat final letters as their base forms and emit ordinary letter forms. They do not invent final forms. Hechrechi and Gadol therefore agree after these substitutions.

The committed dataset uses no substitution (`identity`). You can [generate additional features](generate.md) with Atbash or Albam while retaining the same choice of numerical method.

## Scholarly context

The principal numerical conventions are documented in the [Encyclopaedia Judaica entry on gematria](https://jewishvirtuallibrary.org/jsource/judaica/ejud_0002_0007_0_07165.html). Numerical equivalence is a reproducible observation about a specified text and method; on its own it does not establish historical authorial intent. See [Sources and citation](sources.md) for the research and implementation references.
