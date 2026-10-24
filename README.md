# SrotaX documentation

Task guides and implementation-derived reference for SrotaX Studio and its Runtime API.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/check.py
mkdocs serve
```

Build: `mkdocs build --strict`. Generated output is `site/`.

See [verification](docs/verification.md) for evidence and known limits. See [contributing](CONTRIBUTING.md) for refreshing the operator snapshot and rerunning the disposable end-to-end journey.

Live site: https://docs.srotax.com/

Pushes to `main` run checks and publish the generated site to `gh-pages`. GitHub Pages serves that branch at the custom domain recorded in `docs/CNAME`. Pull requests run checks without deployment.
