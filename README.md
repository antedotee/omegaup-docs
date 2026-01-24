# omegaUp Documentation Site

This is the documentation site for omegaUp, built with Zensical (Material for MkDocs).

## Setup Instructions

### 1. Create a new GitHub repository

Create a new repository on GitHub (e.g., `omegaup-docs` or `docs`). Do NOT initialize it with a README, .gitignore, or license.

### 2. Add the remote and push

```bash
cd docs
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

### 3. Update site URL in zensical.toml

Update the `site_url` in `zensical.toml` to match your GitHub Pages URL:

```toml
site_url = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
```

Or if using a custom domain:
```toml
site_url = "https://docs.omegaup.com"
```

### 4. Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. The site will automatically deploy when you push to the `main` branch

## Local Development

This documentation site supports multiple languages (English, Spanish, Portuguese, and Brazilian Portuguese). Follow these steps to set up and run the site locally.

### 1. Initial Setup

#### Create and activate a virtual environment (recommended)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

#### Install dependencies

```bash
pip install zensical
```

### 2. Building the Documentation

#### Quick Build - All Languages

To build all language versions at once, use the provided build script:

```bash
python3 build_all.py
```

This will:
- Clean the existing `site/` directory
- Build English (`/en/`), Spanish (`/es/`), Portuguese (`/pt/`), and Brazilian Portuguese (`/pt-BR/`) versions
- Create a root redirect from `/` to `/en/`

#### Manual Build - Single Language

To build only one language version:

```bash
# English (default)
zensical build --clean --config-file zensical.toml

# Spanish
zensical build --clean --config-file zensical.es.toml

# Portuguese
zensical build --clean --config-file zensical.pt.toml

# Brazilian Portuguese
zensical build --clean --config-file zensical.pt-BR.toml
```

### 3. Serving Locally

#### Multi-Language Server (Recommended)

To test language switching and view all language versions:

```bash
python3 serve_multilang.py
```

Then open your browser to:
- **Root (redirects to English):** http://localhost:8000/
- **English:** http://localhost:8000/en/
- **Español:** http://localhost:8000/es/
- **Português:** http://localhost:8000/pt/
- **Português (Brasil):** http://localhost:8000/pt-BR/

> **Note:** The `serve_multilang.py` script properly serves all language directories and allows language switching to work correctly.

#### Alternative - Simple HTTP Server

```bash
cd site
python3 -m http.server 8000
```

#### Single Language Only (Not Recommended for Multi-Language Testing)

```bash
# This only serves English and won't allow language switching
zensical serve --config-file zensical.toml
```

### 4. Making Changes

#### Editing Content

1. Edit the Markdown files in `docs/en/` for English content
2. Rebuild the site: `python3 build_all.py`
3. Refresh your browser to see changes

#### Translating Content

To translate English content to other languages:

```bash
# Translate all files
python3 scripts/translate_docs.py

# Translate specific language only
python3 scripts/translate_docs.py --langs pt

# Translate only specific files (for testing)
python3 scripts/translate_docs.py --only "getting-started"
```

### 5. Troubleshooting

#### Issue: 404 errors when clicking language links

**Cause:** Using `zensical serve` which only serves one language directory.

**Solution:** Use the multi-language server instead:
```bash
python3 serve_multilang.py
```

#### Issue: Changes not showing up

**Cause:** Browser cache or stale build.

**Solution:** 
```bash
# Clean rebuild
python3 build_all.py

# Or manually clear cache
rm -rf .cache site
```

#### Issue: Missing dependencies

**Cause:** Zensical not installed or virtual environment not activated.

**Solution:**
```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux

# Install/upgrade Zensical
pip install --upgrade zensical
```

## Project Structure

```
docs/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment workflow
├── .venv/                      # Virtual environment (gitignored)
├── .cache/                     # Build cache (gitignored)
├── site/                       # Built site (gitignored)
│   ├── en/                     # English version
│   ├── es/                     # Spanish version
│   ├── pt/                     # Portuguese version
│   ├── pt-BR/                  # Brazilian Portuguese version
│   └── index.html              # Root redirect to /en/
├── docs/                       # Source documentation files
│   ├── en/                     # English source (primary)
│   ├── es/                     # Spanish translations
│   ├── pt/                     # Portuguese translations
│   └── pt-BR/                  # Brazilian Portuguese translations
├── scripts/
│   ├── translate_docs.py       # Auto-translate from English to other languages
│   └── generate-gsoc-pages.py  # GSoC pages generator
├── overrides/                  # Theme customizations
├── .gitignore                  # Git ignore rules
├── zensical.toml               # English config
├── zensical.es.toml            # Spanish config
├── zensical.pt.toml            # Portuguese config
├── zensical.pt-BR.toml         # Brazilian Portuguese config
├── build_all.py                # Build all language versions
├── serve_multilang.py          # Multi-language development server
└── README.md                   # This file
```

### Language-Specific Configuration

Each language has its own `zensical.*.toml` configuration file that specifies:
- `site_dir`: Where to output the built files (e.g., `site/en/`, `site/pt/`)
- `docs_dir`: Source directory for that language (e.g., `docs/en/`, `docs/pt/`)
- `language`: The language code for theme localization
- `alternate`: Links to other language versions for the language switcher

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when you push to the `main` branch. The workflow:

1. Builds the site using Zensical
2. Deploys to GitHub Pages
3. Makes the site available at your configured URL

## Notes

- The `site/` directory is gitignored as it's generated during build
- The `.cache/` directory is gitignored as it contains build cache
- The `.nojekyll` file will be automatically generated in the `site/` directory during build for GitHub Pages
