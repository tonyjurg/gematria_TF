"""BHSA word slots are not necessarily whole orthographic words."""
from dataclasses import dataclass

from .normalization import normalize

REPRESENTATIONS = ("lexeme", "word", "full")
READINGS = ("ketiv", "qere")


@dataclass(frozen=True)
class Word:
    node: int
    verse: int
    language: str
    lexeme: str
    consonants: str
    trailer: str
    qere: str | None = None
    qere_trailer: str | None = None

    def surface(self, reading: str) -> str:
        if reading not in READINGS:
            raise ValueError(f"Unknown reading: {reading}")
        # None means absent; an explicitly empty qere must remain empty.
        value = self.qere if reading == "qere" and self.qere is not None else self.consonants
        return normalize(value)

    def boundary(self, reading: str) -> str:
        if reading not in READINGS:
            raise ValueError(f"Unknown reading: {reading}")
        if reading == "qere" and self.qere_trailer is not None:
            return self.qere_trailer
        return self.trailer


def read_words(api) -> list[Word]:
    F, L = api.F, api.L
    result = []
    for node in F.otype.s("word"):
        verses = L.u(node, otype="verse")
        if len(verses) != 1:
            raise ValueError(f"Expected exactly one verse for word {node}")
        values = [F.languageISO.v(node), F.lex_utf8.v(node), F.g_cons_utf8.v(node), F.trailer_utf8.v(node)]
        if any(value is None for value in values):
            raise ValueError(f"Missing mandatory source feature on word {node}")
        if values[0] not in ("hbo", "arc"):
            raise ValueError(f"Unsupported language on word {node}: {values[0]}")
        result.append(Word(node, verses[0], *values, F.qere_utf8.v(node), F.qere_trailer_utf8.v(node)))
    return result


def full_groups(words: list[Word], reading: str):
    """Join adjacent slots only across empty trailers, never across verse ends.

    Maqaf is an explicit boundary, as is all other nonempty interword material.
    Suffix letters are already in the surface: no morphological reattachment.
    """
    group = []
    for word in words:
        if group and (word.verse != group[-1].verse or word.node != group[-1].node + 1):
            yield group
            group = []
        group.append(word)
        if word.boundary(reading) != "":
            yield group
            group = []
    if group:
        yield group


def qere_errors(words: list[Word]) -> dict[int, str]:
    errors = {}
    for word in words:
        if word.qere is not None:
            try:
                normalize(word.qere)
            except ValueError as error:
                errors[word.node] = str(error)
    return errors


def represent(words: list[Word], reading: str, *, invalid_qere="error"):
    if invalid_qere not in ("error", "omit"):
        raise ValueError("Invalid qere error policy")
    texts = {name: {} for name in REPRESENTATIONS}
    starts, ends = {}, {}
    for word in words:
        texts["lexeme"][word.node] = normalize(word.lexeme)
        try:
            texts["word"][word.node] = word.surface(reading)
        except ValueError:
            if reading != "qere" or word.qere is None or invalid_qere != "omit":
                raise
            texts["word"][word.node] = None
    for group in full_groups(words, reading):
        parts = [texts["word"][word.node] for word in group]
        text = None if any(part is None for part in parts) else "".join(parts)
        for word in group:
            texts["full"][word.node] = text
            starts[word.node], ends[word.node] = group[0].node, group[-1].node
    return texts, starts, ends

