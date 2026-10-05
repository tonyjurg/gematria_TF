# Building and publishing the site

This page is for the repository maintainer. The documentation is a static website generated from the Markdown files in `/docs`, with a shared sidebar and stylesheet. No Jekyll, Ruby, or JavaScript build tools are required.

## Build and preview locally

From the repository root:

```console
python -m pip install -r requirements-docs.txt
python scripts/build_docs.py
python -m http.server 8765 --bind 127.0.0.1 --directory output/site
```

Open **http://127.0.0.1:8765/**. The build validates local links and copies only the documentation pages and their assets. Dataset files remain in the repository and are linked on GitHub.

The generated files use relative links, so the same output works under the project URL `https://tonyjurg.github.io/gematria_TF/` or at a custom domain’s root. The generated output is ignored by Git; GitHub Actions builds it again from the committed source.

## Enable GitHub Pages

1. Open the repository’s **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Open **Actions → Documentation site → Run workflow** on the `main` branch.
4. Select **Publish to GitHub Pages** and run the workflow.
5. Follow the deployment URL shown by the completed job.

Publishing is manual. Ordinary pushes and pull requests build and check the site without publishing it. For later updates, repeat the workflow with publishing selected.

See [GitHub’s Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Edit the documentation

- Edit the Markdown pages in `/docs`.
- Adjust the shared layout in `docs/_site/template.html` and styling in `docs/assets/style.css`.
- Page titles and sidebar organization are defined in `scripts/build_docs.py`.
- Existing `.md` links are rewritten to `.html` in the site. Links outside `/docs` point to the GitHub repository.
- Run the build after editing. It fails on unresolved local paths or section anchors.

The numerical generator and committed TF files are independent of this documentation build.
