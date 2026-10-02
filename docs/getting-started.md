# Start using the dataset

The `.tf` files are already generated. You only need to obtain the repository, download the matching BHSA source, and load the features you want.

## 1. Obtain a local copy

The [gematria_TF repository](https://github.com/tonyjurg/gematria_TF) is private. Sign in to a GitHub account with access, then use **Code → Download ZIP** and extract it, or clone it using your normal authenticated Git setup:

```console
git clone https://github.com/tonyjurg/gematria_TF.git
cd gematria_TF
```

The generated dataset is in `tf/2021`. A documentation website does not automatically grant access to these repository files.

## 2. Prepare Python

Use Python **3.11 or newer**. From the repository folder:

```console
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```console
source .venv/bin/activate
```

Install the runtime dependencies:

```console
python -m pip install -r requirements.txt
```

There is no gematria_TF package to install. Its scripts and notebook run locally from the repository.

## 3. Download the matching BHSA source

In Python or a notebook opened in the repository folder:

```python
from pathlib import Path
from gematria_tf.bhsa import fetch_source, load_source

source = fetch_source(Path(".cache/bhsa/tf/2021")).resolve()
_, source_info = load_source(source)
print(source_info["version"])  # 2021
```

The first run downloads the pinned source files. Later runs reuse them. Checksums ensure that the source matches the node numbering used by the generated dataset.

## 4. Load a gematria feature

```python
from pathlib import Path
from tf.fabric import Fabric

source = Path(".cache/bhsa/tf/2021").resolve()
addon = Path("tf/2021").resolve()

TF = Fabric(locations=[str(source), str(addon)])
api = TF.load(
    "gematria_hechrechi_full_ketiv_identity "
    "gematria_text_full_ketiv "
    "gematria_full_start_ketiv"
)
if not api:
    raise RuntimeError("The source or add-on could not be loaded")

F = api.F
print(F.gematria_text_full_ketiv.v(1))               # בראשית
print(F.gematria_hechrechi_full_ketiv_identity.v(1)) # 913
```

Each feature is accessed by its name. Use the [feature catalogue](features.md) to choose another method, representation, or reading.

## Understand a feature name

`gematria_hechrechi_full_ketiv_identity` means:

Part | Meaning
---|---
`hechrechi` | The standard numerical method
`full` | The reconstructed full written form
`ketiv` | The written consonants recorded by BHSA
`identity` | No letter substitution before calculation

The committed dataset uses `identity`. The local generator also supports Atbash and Albam as optional, separately named transformations.

## Where next?

Try the [worked examples](examples.md) to compare readings, find numerical matches, and count full forms once. Open the [production notebook](../create_gematria_features.ipynb) for an executable walkthrough. If you want different combinations, see [Regenerate or extend](generate.md).
