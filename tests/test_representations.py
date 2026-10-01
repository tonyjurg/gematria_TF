from dataclasses import replace
import pytest

from gematria_tf.representations import Word, represent


def w(node, text, trailer=" ", **kwargs):
    return Word(node, kwargs.pop("verse", 100), "hbo", text, text, trailer, **kwargs)


def test_attached_prefix_and_suffix_counted_once():
    words = [w(1, "ו", ""), w(2, "ב", ""), w(3, "ביתו")]
    texts, starts, ends = represent(words, "ketiv")
    assert texts["word"][3] == "ביתו"
    assert texts["full"] == {1: "ובביתו", 2: "ובביתו", 3: "ובביתו"}
    assert starts == {1: 1, 2: 1, 3: 1}
    assert ends == {1: 3, 2: 3, 3: 3}


def test_maqaf_and_verse_are_boundaries():
    words = [w(1, "כל", "־"), w(2, "ה", ""), w(3, "ארץ", ""), w(4, "אב", verse=101)]
    texts, _, _ = represent(words, "ketiv")
    assert texts["full"] == {1: "כל", 2: "הארץ", 3: "הארץ", 4: "אב"}


def test_empty_qere_and_empty_qere_trailer_are_not_missing():
    words = [w(1, "א", qere="", qere_trailer=""), w(2, "ב", qere="ג")]
    texts, starts, _ = represent(words, "qere")
    assert texts["word"] == {1: "", 2: "ג"}
    assert texts["lexeme"] == {1: "א", 2: "ב"}
    assert texts["full"] == {1: "ג", 2: "ג"}
    assert starts[2] == 1
    assert represent(words, "ketiv")[0]["full"] == {1: "א", 2: "ב"}


def test_qere_can_split_a_ketiv_unit():
    words = [w(1, "ב", "", qere="בָּא", qere_trailer=" "), w(2, "גד", qere="גָד")]
    assert represent(words, "ketiv")[0]["full"][1] == "בגד"
    assert represent(words, "qere")[0]["full"] == {1: "בא", 2: "גד"}


def test_noncontiguous_nodes_are_not_joined():
    assert represent([w(1, "א", ""), w(3, "ב")], "ketiv")[0]["full"] == {1: "א", 3: "ב"}


def test_invalid_qere_is_never_silently_repaired():
    words = [w(1, "ו", ""), w(2, "ינון", qere="יִנֹּ97ון")]
    with pytest.raises(ValueError):
        represent(words, "qere")
    texts, _, _ = represent(words, "qere", invalid_qere="omit")
    assert texts["word"] == {1: "ו", 2: None}
    assert texts["full"] == {1: None, 2: None}
    assert represent(words, "ketiv")[0]["full"][1] == "וינון"

