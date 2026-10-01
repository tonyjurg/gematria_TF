"""Download and load only the pinned BHSA features required by this project."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

FEATURES = "lex_utf8 g_cons_utf8 g_word_utf8 trailer_utf8 qere_utf8 qere_trailer_utf8 languageISO g_prs_utf8 book chapter verse".split()


def source_lock() -> dict:
    return json.loads(Path(__file__).with_name("bhsa-lock.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_digest(data: bytes) -> str:
    """Hash canonical LF bytes so Git's Windows CRLF checkout is equivalent."""
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def fetch_source(directory: Path) -> Path:
    lock = source_lock()
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for name, expected in lock["sha256"].items():
        path = directory / name
        if path.exists():
            if source_digest(path.read_bytes()) != expected:
                raise ValueError(f"Existing source differs from pin: {path}")
            continue
        url = f"https://raw.githubusercontent.com/ETCBC/bhsa/{lock['commit']}/tf/{lock['version']}/{name}"
        with urlopen(url, timeout=120) as response:
            data = response.read()
        if source_digest(data) != expected:
            raise ValueError(f"Checksum mismatch downloading {name}")
        temporary = path.with_suffix(".download")
        temporary.write_bytes(data)
        temporary.replace(path)
    return directory


def load_source(directory: Path):
    from tf.fabric import Fabric

    directory = Path(directory).resolve()
    lock = source_lock()
    for name, expected in lock["sha256"].items():
        path = directory / name
        if not path.is_file() or source_digest(path.read_bytes()) != expected:
            raise ValueError(f"Missing or changed pinned BHSA source: {path}")
    fabric = Fabric(locations=str(directory), silent="deep")
    api = fabric.load(FEATURES, silent="deep")
    if not api:
        raise RuntimeError("Text-Fabric could not load BHSA")
    return api, lock

