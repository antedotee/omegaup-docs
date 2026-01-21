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

### Install Zensical

```bash
pip install zensical
```

### Build the site locally

```bash
zensical build
```

The built site will be in the `site/` directory.

### Serve locally for preview

```bash
zensical serve
```

Visit `http://127.0.0.1:8000` to preview your documentation.

## Project Structure

```
docs/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions deployment workflow
├── .gitignore              # Git ignore rules
├── zensical.toml           # Zensical configuration
├── index.md                # Homepage
├── api/                    # API documentation
├── architecture/           # Architecture docs
├── community/              # Community docs
├── development/            # Development guides
├── features/               # Feature documentation
├── getting-started/        # Getting started guides
├── operations/             # Operations docs
└── reference/              # Reference materials
```

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when you push to the `main` branch. The workflow:

1. Builds the site using Zensical
2. Deploys to GitHub Pages
3. Makes the site available at your configured URL

## Notes

- The `site/` directory is gitignored as it's generated during build
- The `.cache/` directory is gitignored as it contains build cache
- The `.nojekyll` file will be automatically generated in the `site/` directory during build for GitHub Pages
