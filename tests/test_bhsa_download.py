import pytest

from gematria_tf import bhsa


@pytest.fixture
def standard_source(tmp_path, monkeypatch):
    base = tmp_path / "text-fabric-data" / "github"
    directory = base / "etcbc" / "bhsa" / "tf" / "2021"
    directory.mkdir(parents=True)
    data = b"@node\n@valueType=str\n\n1\tfixture\n"
    (directory / "otype.tf").write_bytes(data)
    lock = {"version": "2021", "commit": "a" * 40,
            "sha256": {"otype.tf": bhsa.source_digest(data)}}
    monkeypatch.setattr("tf.core.files.backendRep", lambda backend, kind: str(base))
    monkeypatch.setattr(bhsa, "source_lock", lambda: lock)
    return base, directory, lock


def test_fetch_uses_tf_managed_location_and_pinned_checkout(standard_source, monkeypatch):
    base, directory, lock = standard_source
    calls = []

    def checkout(backend, **options):
        calls.append((backend, options))
        return lock["commit"], None, "local", str(base), "etcbc/bhsa/tf"

    monkeypatch.setattr("tf.advanced.repo.checkoutRepo", checkout)
    assert bhsa.fetch_source() == directory.resolve()
    backend, options = calls[0]
    assert backend == "github"
    assert options["org"] == "etcbc" and options["repo"] == "bhsa"
    assert options["checkout"] == lock["commit"] and options["version"] == "2021"
    assert options["allowExpress"] is False
    assert "dest" not in options and "source" not in options


def test_tf_download_failure_does_not_return_a_source(standard_source, monkeypatch):
    monkeypatch.setattr("tf.advanced.repo.checkoutRepo", lambda *a, **k: (None, None, False, False, None))
    with pytest.raises(RuntimeError, match="could not obtain"):
        bhsa.fetch_source()


def test_tf_source_is_validated_after_download(standard_source, monkeypatch):
    base, directory, lock = standard_source
    (directory / "otype.tf").write_text("changed", encoding="utf-8")
    monkeypatch.setattr("tf.advanced.repo.checkoutRepo", lambda *a, **k: (lock["commit"], None, "local", str(base), "etcbc/bhsa/tf"))
    with pytest.raises(ValueError, match="Missing or changed"):
        bhsa.fetch_source()


def test_tf_download_rejects_a_nonstandard_destination(standard_source, monkeypatch):
    base, directory, lock = standard_source
    monkeypatch.setattr("tf.advanced.repo.checkoutRepo", lambda *a, **k: (lock["commit"], None, "local", str(base / "other"), "etcbc/bhsa/tf"))
    with pytest.raises(RuntimeError, match="Unexpected Text-Fabric source directory"):
        bhsa.fetch_source()
