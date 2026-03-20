# Data Explorer

Static site for exploring the benchmark recordings, SQLite metadata, and linked asset files.

## Files

- `index.html`: main explorer page
- `styles.css`: site styling
- `app.js`: interactive client-side explorer logic
- `build_data.py`: exports `data/explorer-data.json` from `Assets/database_working_copy.db`

## Refresh the data

Run:

```bash
python3 Data_Explorer/build_data.py
```

The explorer expects to be hosted from the repository so that relative links like `../Assets/...` resolve correctly.

## GitHub Pages

To publish this on GitHub Pages:

1. Push `Assets/Benchmark`, `Assets/database_working_copy.db`, and `Data_Explorer` to the repository.
2. Keep the repository root `index.html` and `.nojekyll` files so the site redirects to `Data_Explorer/` and GitHub Pages serves the static files without Jekyll processing.
3. In the GitHub repository settings, enable Pages from the main branch root.

After that, the explorer will be reachable at:

- `https://<user>.github.io/<repo>/`
- `https://<user>.github.io/<repo>/Data_Explorer/`

The explorer is designed to work from the repository root because benchmark media and script links resolve relative to `../Assets/...`.
