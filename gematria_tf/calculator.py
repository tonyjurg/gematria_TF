"""Independent numerical weighting and alphabet transformations.

Design references: avi-perl/Hebrew and OriHoch/python-hebrew-numbers.
See THIRD_PARTY_NOTICES.md for differences and retained MIT notices.
"""
from .normalization import ALPHABET, FINALS, normalize

STANDARD = dict(zip(ALPHABET, (*range(1, 10), *range(10, 100, 10), 100, 200, 300, 400)))
STANDARD.update({final: STANDARD[base] for final, base in FINALS.items()})
GADOL = {**STANDARD, **dict(zip("ךםןףץ", range(500, 1000, 100)))}
SIDDURI = {char: i for i, char in enumerate(ALPHABET, 1)}
SIDDURI.update({final: SIDDURI[base] for final, base in FINALS.items()})


def digital_root(value: int) -> int:
    return 0 if value == 0 else 1 + (value - 1) % 9


TABLES = {
    "hechrechi": STANDARD,
    "gadol": GADOL,
    "sidduri": SIDDURI,
    "katan": {char: digital_root(value) for char, value in STANDARD.items()},
}
METHODS = (*TABLES, "katan_mispari")
TRANSFORMS = ("identity", "atbash", "albam")


def transform_text(text: str, transform: str = "identity") -> str:
    text = normalize(text)
    if transform not in TRANSFORMS:
        raise ValueError(f"Unknown transformation: {transform}")
    if transform == "identity":
        return text
    # Substitution acts on 22 base letters; never invent positional final forms.
    target = ALPHABET[::-1] if transform == "atbash" else ALPHABET[11:] + ALPHABET[:11]
    table = dict(zip(ALPHABET, target))
    return "".join(table[FINALS.get(char, char)] for char in text)


def calculate(text: str, method: str = "hechrechi", transform: str = "identity") -> int:
    if method not in METHODS:
        raise ValueError(f"Unknown numerical method: {method}")
    text = transform_text(text, transform)
    table = STANDARD if method == "katan_mispari" else TABLES[method]
    total = sum(table[char] for char in text)
    return digital_root(total) if method == "katan_mispari" else total

