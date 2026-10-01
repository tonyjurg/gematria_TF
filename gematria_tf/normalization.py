"""Consonants only, with an explicit and deliberately strict Unicode policy."""
import unicodedata

ALPHABET = "אבגדהוזחטיכלמנסעפצקרשת"
FINALS = dict(zip("ךםןףץ", "כמנפצ"))
LETTERS = frozenset(ALPHABET + "ךםןףץ")
POLICY = "hebrew-consonants-nfkd-v1"


def normalize(text: str) -> str:
    """Decompose presentation forms, drop Hebrew marks/punctuation, retain finals.

    Reject unexpected letters/numerals/symbols rather than silently losing data.
    This is consonant extraction, not general grapheme segmentation. Dagesh is
    a combining mark and does not introduce another consonant. Yiddish digraphs
    are outside the Biblical Hebrew/Aramaic input contract.
    """
    result = []
    for char in unicodedata.normalize("NFKD", text):
        if char in LETTERS:
            result.append(char)
        elif ("\u0591" <= char <= "\u05c7" and unicodedata.category(char).startswith("M")):
            continue
        elif char.isspace() or char in "־׀׃׳״.,;:!?\"'()-[]{}":
            continue
        elif char in "\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069":
            continue
        else:
            raise ValueError(f"Unexpected character U+{ord(char):04X} in Hebrew input")
    return "".join(result)

