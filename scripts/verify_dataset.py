"""Check the committed dataset's hashes and independently worked BHSA examples.

Run from the repository root after fetching BHSA: python scripts/verify_dataset.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gematria_tf.bhsa import sha256, source_lock
from tf.fabric import Fabric


def main():
    output = Path("tf/2021").resolve()
    source = Path(".cache/bhsa/tf/2021").resolve()
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["source"] == source_lock()
    assert manifest["wordCount"] == 426590
    assert manifest["limit"] is None
    assert manifest["roundTripVerified"]
    for name, expected in manifest["features"].items():
        assert sha256(output / name) == expected, name
    names = "gematria_hechrechi_full_ketiv_identity gematria_hechrechi_word_ketiv_identity gematria_hechrechi_word_qere_identity gematria_full_start_ketiv gematria_qere_error"
    api = Fabric(locations=[str(source), str(output)], silent="deep").load(names, silent="deep")
    assert api
    F = api.F
    assert [F.gematria_hechrechi_full_ketiv_identity.v(n) for n in (1, 3, 4, 5, 6, 8, 10)] == [913, 203, 86, 401, 395, 407, 296]
    assert sum(F.gematria_hechrechi_full_ketiv_identity.v(n) for n in range(1, 12) if F.gematria_full_start_ketiv.v(n) == n) == 2701
    assert F.gematria_hechrechi_word_ketiv_identity.v(194) == 106
    assert F.gematria_hechrechi_full_ketiv_identity.v(194) == 136
    assert F.gematria_hechrechi_word_ketiv_identity.v(3897) == 102
    assert F.gematria_hechrechi_word_qere_identity.v(3897) == 106
    assert F.gematria_hechrechi_word_ketiv_identity.v(17278) == 213
    assert F.gematria_hechrechi_word_ketiv_identity.v(322495) == 120
    assert F.gematria_hechrechi_word_qere_identity.v(322495) is None
    assert "U+0039" in F.gematria_qere_error.v(322495)
    print("All dataset checksums and independent BHSA examples verified")


if __name__ == "__main__":
    main()
