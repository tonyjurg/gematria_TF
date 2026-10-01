import pytest

from gematria_tf.calculator import METHODS, calculate, transform_text
from gematria_tf.normalization import ALPHABET, normalize


@pytest.mark.parametrize("text,expected", [("חי", 18), ("אחד", 13), ("אהבה", 13), ("תורה", 611), ("שלום", 376), ("בראשית", 913), ("יהוה", 26)])
def test_known_standard_values(text, expected):
    assert calculate(text) == expected


@pytest.mark.parametrize("method,value", [("hechrechi", 376), ("gadol", 936), ("sidduri", 52), ("katan", 16), ("katan_mispari", 7)])
def test_shalom_by_method(method, value):
    assert calculate("שלום", method) == value


def test_final_letter_variants():
    assert calculate("ךםןףץ") == 280
    assert calculate("ךםןףץ", "gadol") == 3500
    assert calculate("ךםןףץ", "sidduri") == 73
    assert calculate("ךםןףץ", "katan") == 28
    assert calculate("ךםןףץ", "katan_mispari") == 1
    assert calculate("כמנפצ", "gadol") == 280


@pytest.mark.parametrize("text", ["בְּרֵאשִׁ֖ית", "בְּרֵאשִׁׁית", "\u200fבראשית\u200e"])
def test_unicode_consonants(text):
    assert normalize(text) == "בראשית"
    assert calculate(text) == 913


def test_no_numeral_thousands_or_dagesh_doubling():
    assert calculate("א׳ב") == 3
    assert calculate("בּ") == 2
    assert normalize("שָׁלוֹם־לְךָ׃") == "שלוםלך"


@pytest.mark.parametrize("text", ["abc", "שלום2", "װ", "א🙂", "א\u0301"])
def test_unexpected_input_is_rejected(text):
    with pytest.raises(ValueError):
        normalize(text)


@pytest.mark.parametrize("method", METHODS)
def test_explicit_empty_is_zero(method):
    assert calculate("", method) == 0


@pytest.mark.parametrize("transform", ["atbash", "albam"])
def test_substitution_is_independent_and_involutive(transform):
    assert transform_text(transform_text(ALPHABET, transform), transform) == ALPHABET
    assert calculate("שלום", "gadol", transform) == calculate("שלום", "hechrechi", transform)


def test_transformation_examples():
    assert transform_text("בבל", "atbash") == "ששכ"
    assert transform_text("אבכ", "albam") == "למת"
    assert calculate("בבל", transform="atbash") == 620
    assert transform_text("ך", "identity") == "ך"


def test_unknown_choices_fail():
    with pytest.raises(ValueError):
        calculate("א", "unknown")
    with pytest.raises(ValueError):
        calculate("א", transform="unknown")

