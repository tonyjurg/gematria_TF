"""Obtain BHSA through Text-Fabric and validate its source snapshot."""
import hashlib
import json
from pathlib import Path

FEATURES = "lex_utf8 g_cons_utf8 g_word_utf8 trailer_utf8 qere_utf8 qere_trailer_utf8 languageISO g_prs_utf8 book chapter verse".split()


def source_lock() -> dict:
    return json.loads(Path(__file__).with_name("bhsa-lock.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_digest(data: bytes) -> str:
    """Hash canonical LF bytes so Git's Windows CRLF checkout is equivalent."""
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def source_directory() -> Path:
    """Use the standard download root designated by Text-Fabric."""
    from tf.core.files import backendRep

    return (Path(backendRep("github", "cache")).expanduser()
            / "etcbc" / "bhsa" / "tf" / source_lock()["version"]).resolve()


def validate_source(directory: Path) -> dict:
    lock = source_lock()
    for name, expected in lock["sha256"].items():
        path = Path(directory) / name
        if not path.is_file() or source_digest(path.read_bytes()) != expected:
            raise ValueError(f"Missing or changed pinned BHSA source: {path}")
    return lock


def fetch_source() -> Path:
    """Let TF download the pinned BHSA snapshot into its standard data tree."""
    from tf.advanced.repo import checkoutRepo

    lock = source_lock()
    _, _, _, base, relative = checkoutRepo(
        "github", org="etcbc", repo="bhsa", folder="/tf",
        version=lock["version"], checkout=lock["commit"],
        allowExpress=False, silent="auto",
    )
    if not base or not relative:
        raise RuntimeError("Text-Fabric could not obtain the required BHSA snapshot")
    directory = (Path(base).expanduser() / relative / lock["version"]).resolve()
    if directory != source_directory():
        raise RuntimeError(f"Unexpected Text-Fabric source directory: {directory}")
    validate_source(directory)
    return directory


def load_source(directory: Path | None = None):
    from tf.fabric import Fabric

    directory = source_directory() if directory is None else Path(directory).resolve()
    lock = validate_source(directory)
    fabric = Fabric(locations=str(directory), silent="deep")
    api = fabric.load(FEATURES, silent="deep")
    if not api:
        raise RuntimeError("Text-Fabric could not load BHSA")
    return api, lock

