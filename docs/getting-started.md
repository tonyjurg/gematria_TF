# Start using the dataset

The `.tf` files are already generated. You only need to obtain the repository, download the matching BHSA source, and load the features you want.

## 1. Obtain a local copy

Obtain the [gematria_TF repository](https://github.com/tonyjurg/gematria_TF) with **Code → Download ZIP** and extract it, or clone it:

```console
git clone https://github.com/tonyjurg/gematria_TF.git
cd gematria_TF
```

The generated dataset is in `tf/2021`.

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

source = fetch_source()
_, source_info = load_source(source)
print(source_info["version"])  # 2021
```

Text-Fabric downloads BHSA into its standard data location, normally `~/text-fabric-data/github/etcbc/bhsa/tf/2021`. Later runs reuse that standard copy. The requested commit and file checksums ensure that the source matches the node numbering used by the generated dataset. There is no project-specific BHSA cache.

## 4. Load a gematria feature

```python
from pathlib import Path
from tf.fabric import Fabric
from gematria_tf.bhsa import source_directory

source = source_directory()
addon = Path("tf/2021").resolve()

TF = Fabric(locations=[str(source), str(addon)])
api = TF.load(
    "gem_hechrechi_full_ketiv_ident "
    "gem_text_full_ketiv "
    "gem_full_start_ketiv"
)
if not api:
    raise RuntimeError("The source or add-on could not be loaded")

F = api.F
print(F.gem_text_full_ketiv.v(1))               # בראשית
print(F.gem_hechrechi_full_ketiv_ident.v(1)) # 913
```

Each feature is accessed by its name. Use the [feature catalogue](features.md) to choose another method, representation, or reading.

## Understand a feature name

`gem_hechrechi_full_ketiv_ident` means:

Part | Meaning
---|---
`gem` | Gematria feature prefix
`hechrechi` | The standard numerical method
`full` | The reconstructed full written form
`ketiv` | The written consonants recorded by BHSA
`ident` | Identity: no letter substitution before calculation

The committed feature names use `ident`. The calculation option and provenance metadata retain the full name `identity`. The local generator also supports Atbash and Albam as optional, separately named transformations.

## Where next?

Try the [worked examples](examples.md) to compare readings, find numerical matches, and count full forms once. Open the [production notebook](../create_gematria_features.ipynb) for an executable walkthrough. If you want different combinations, see [Regenerate or extend](generate.md).

### GitHub download rate limits

Public BHSA downloads do not require a GitHub login. Anonymous API requests have a lower rate limit, so Text-Fabric's download of a pinned snapshot can reach that limit. Once the standard copy is downloaded, subsequent generation runs read it locally.

For authenticated downloads, Text-Fabric reads a GitHub access token from the `GHPERS` environment variable. Signing in to GitHub in a browser does not set this variable. See the [Increase the GitHub rate limit tutorial](https://nbviewer.org/github/CenterBLC/N1904/blob/main/docs/tutorial/Increase_GitHub_rate_limit.ipynb) for token setup. Keep credentials out of notebooks and repository files.

### Complete and minimized BHSA distributions

The official [BHSA releases](https://github.com/ETCBC/bhsa/releases/latest) provide a `complete.zip` asset. Text-Fabric can use an express download of that release archive, avoiding individual feature requests. This generator requests its documented commit instead, so that every required source checksum can be verified; it uses Text-Fabric's standard download directory.

The official [bhsa-min repository](https://github.com/ETCBC/bhsa-min) offers a smaller BHSA 2021 distribution. It is not a drop-in source for this generator: it omits `languageISO.tf` (used for the Hebrew/Aramaic policy) and `g_prs_utf8.tf` (used for suffix-inclusive full forms), as well as other files in the pinned source manifest. Supporting it would require deriving or supplementing those features and validating both word-node alignment and equivalent results. Until that adapter exists, use the full BHSA distribution. Loading only the required features already limits the features held in memory.
