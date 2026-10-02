import json
from pathlib import Path

import pytest
from tf.fabric import Fabric

from gematria_tf.bhsa import load_source, source_lock, source_digest
from gematria_tf.generator import generate


@pytest.fixture
def corpus(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    data = {
        "otype": {1: "word", 2: "word", 3: "word", 4: "word", 5: "verse"},
        "verse": {5: 1},
        "lex_utf8": {1: "ב", 2: "ראשית", 3: "שלום", 4: "אב"},
        "g_cons_utf8": {1: "ב", 2: "ראשית", 3: "שלום", 4: "אב"},
        "trailer_utf8": {1: "", 2: " ", 3: " ", 4: "׃"},
        "qere_utf8": {3: ""}, "qere_trailer_utf8": {3: ""},
        "languageISO": {1: "hbo", 2: "hbo", 3: "hbo", 4: "arc"},
    }
    meta = {n: {"valueType": "int" if n == "verse" else "str"} for n in data}
    meta["oslots"] = {"valueType": "str"}
    meta["otext"] = {"sectionTypes": "verse", "sectionFeatures": "verse"}
    assert Fabric(locations=str(source), silent="deep").save(nodeFeatures=data, edgeFeatures={"oslots": {5: {1, 2, 3, 4}}}, metaData=meta, location=str(source), silent="deep")
    api = Fabric(locations=str(source), silent="deep").load(list(data), silent="deep")
    assert api
    return source, api, {"version": "fixture", "commit": "synthetic-test", "sha256": {}}


def test_export_roundtrip_and_complete_group_at_limit(corpus, tmp_path):
    source, api, lock = corpus
    output = tmp_path / "result"
    manifest = generate(api, source, lock, output, limit=1)
    assert manifest["wordCount"] == 1
    assert len(list(output.glob("gem_hechrechi_*.tf"))) == 3
    assert not (output / "otype.tf").exists()
    loaded = Fabric(locations=[str(source), str(output)], silent="deep").load("gem_hechrechi_full_ketiv_ident gem_full_end_ketiv", silent="deep")
    assert loaded.F.gem_hechrechi_full_ketiv_ident.v(1) == 913
    assert loaded.F.gem_hechrechi_full_ketiv_ident.v(2) is None
    assert loaded.F.gem_full_end_ketiv.v(1) == 2
    assert "@coverage=partial" in (output / "gem_hechrechi_full_ketiv_ident.tf").read_text(encoding="utf-8")


def test_qere_empty_and_language_filter(corpus, tmp_path):
    source, api, lock = corpus
    output = tmp_path / "result"
    generate(api, source, lock, output, readings=("ketiv", "qere"), language="hebrew")
    loaded = Fabric(locations=[str(source), str(output)], silent="deep").load("gem_hechrechi_word_qere_ident gem_hechrechi_full_qere_ident gem_has_qere", silent="deep")
    assert loaded.F.gem_hechrechi_word_qere_ident.v(3) == 0
    assert loaded.F.gem_has_qere.v(3) == 1
    assert loaded.F.gem_hechrechi_word_qere_ident.v(4) is None
    # Group is built before filtering: arc neighbour retained in full text.
    assert loaded.F.gem_hechrechi_full_qere_ident.v(3) == 3


def test_repeat_generation_is_byte_identical(corpus, tmp_path):
    source, api, lock = corpus
    one = generate(api, source, lock, tmp_path / "one")
    two = generate(api, source, lock, tmp_path / "two")
    assert one == two


def test_invalid_qere_is_reported_and_omitted(corpus, tmp_path):
    source, api, lock = corpus
    api.F.qere_utf8.data[3] = "א97"
    output = tmp_path / "invalid-qere"
    manifest = generate(api, source, lock, output, readings=("ketiv", "qere"))
    assert "3" in manifest["qereErrors"]
    assert manifest["featureNodeCounts"]["gem_hechrechi_word_qere_ident"] == 3
    loaded = Fabric(locations=[str(source), str(output)], silent="deep").load("gem_hechrechi_word_qere_ident gem_qere_error", silent="deep")
    assert loaded.F.gem_hechrechi_word_qere_ident.v(3) is None
    assert "U+0039" in loaded.F.gem_qere_error.v(3)


def test_output_safety_and_invalid_options(corpus, tmp_path):
    source, api, lock = corpus
    with pytest.raises(ValueError, match="separate"):
        generate(api, source, lock, source)
    output = tmp_path / "existing"
    output.mkdir()
    (output / "keep.txt").write_text("keep")
    with pytest.raises(ValueError, match="empty"):
        generate(api, source, lock, output)
    assert (output / "keep.txt").read_text() == "keep"
    with pytest.raises(ValueError):
        generate(api, source, lock, tmp_path / "invalid", methods=("bad",))


def test_pinned_source_validation(tmp_path):
    lock = source_lock()
    assert lock["version"] == "2021"
    assert len(lock["commit"]) == 40
    assert "oslots.tf" in lock["sha256"]
    with pytest.raises(ValueError, match="Missing or changed"):
        load_source(tmp_path)


def test_source_hashes_ignore_only_windows_newlines():
    assert source_digest(b"@node\r\n1\t2\r\n") == source_digest(b"@node\n1\t2\n")
    assert source_digest(b"1\t2\n") != source_digest(b"1\t3\n")


def test_short_feature_names_keep_transform_provenance(corpus, tmp_path):
    source, api, lock = corpus
    output = tmp_path / "short-names"
    manifest = generate(api, source, lock, output, methods=("hechrechi",),
                        transforms=("identity", "atbash", "albam"))
    assert manifest["featureNameVersion"] == 2
    assert manifest["transformations"] == ["identity", "atbash", "albam"]
    assert len(manifest["features"]) == 16
    assert all(name.startswith("gem_") and "_identity" not in name
               for name in manifest["features"])
    loaded = Fabric(locations=str(output), silent="deep").load(
        "gem_hechrechi_word_ketiv_ident gem_hechrechi_word_ketiv_atbash gem_hechrechi_word_ketiv_albam",
        silent="deep")
    assert loaded.F.gem_hechrechi_word_ketiv_ident.v(1) == 2
    assert loaded.F.gem_hechrechi_word_ketiv_atbash.v(1) == 300
    assert loaded.F.gem_hechrechi_word_ketiv_albam.v(1) == 40
    assert "@transform=identity" in (output / "gem_hechrechi_word_ketiv_ident.tf").read_text(encoding="utf-8")
