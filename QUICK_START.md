# Quick Start: Push Documentation to Separate Repository

Follow these steps to create a separate GitHub repository for the omegaUp documentation site.

## Option 1: Automated Setup (Recommended)

Run the setup script:

```bash
cd docs
./create-separate-repo.sh
```

Then follow the prompts and next steps shown by the script.

## Option 2: Manual Setup

### Step 1: Initialize Separate Repository

```bash
cd docs

# Remove connection to parent repository
rm -rf .git

# Initialize new repository
git init
git branch -M main
```

### Step 2: Add and Commit Files

```bash
# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: omegaUp documentation site"
```

### Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `omegaup-docs` (or your preferred name)
3. Description: "Documentation site for omegaUp built with Zensical"
4. **Important:** Do NOT initialize with README, .gitignore, or license
5. Choose visibility (Public recommended)
6. Click **Create repository**

### Step 4: Update Site URL

Edit `zensical.toml` and update the `site_url`:

```toml
site_url = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
```

For example:
```toml
site_url = "https://omegaup.github.io/omegaup-docs"
```

### Step 5: Add Remote and Push

```bash
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 6: Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. The site will automatically deploy via the workflow in `.github/workflows/deploy.yml`

### Step 7: Verify Deployment

- Check the **Actions** tab for deployment status
- Once complete, your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## Troubleshooting

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### GitHub Pages not deploying
1. Check **Actions** tab for errors
2. Verify GitHub Pages is enabled: Settings → Pages → Source: GitHub Actions
3. Ensure `.github/workflows/deploy.yml` exists

### Need to update site URL later
1. Edit `zensical.toml`
2. Update `site_url`
3. Commit and push:
   ```bash
   git add zensical.toml
   git commit -m "Update site URL"
   git push
   ```

## What Gets Deployed

The GitHub Actions workflow will:
1. Install Zensical
2. Build the site (`zensical build`)
3. Deploy to GitHub Pages
4. Make it available at your configured URL

The `site/` directory is gitignored and generated during build.
