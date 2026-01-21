# Setting Up Separate Documentation Repository

This guide will help you create a separate GitHub repository for the omegaUp documentation site.

## Step 1: Initialize Git Repository

The `docs/` folder is currently part of the parent omegaUp repository. We need to initialize it as a separate repository.

```bash
cd docs
git init
git branch -M main
```

## Step 2: Add All Files

Add all documentation files to the new repository:

```bash
git add .
git commit -m "Initial commit: omegaUp documentation site"
```

## Step 3: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right → **New repository**
3. Repository name: `omegaup-docs` (or your preferred name)
4. Description: "Documentation site for omegaUp built with Zensical"
5. **Important:** Do NOT initialize with README, .gitignore, or license (we already have these)
6. Choose visibility (Public recommended for documentation)
7. Click **Create repository**

## Step 4: Update Site URL

Before pushing, update the `site_url` in `zensical.toml`:

```bash
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values
# For example: https://omegaup.github.io/omegaup-docs
```

Edit `zensical.toml` and update:
```toml
site_url = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
```

## Step 5: Add Remote and Push

```bash
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## Step 6: Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. The site will automatically deploy when you push to the `main` branch

## Step 7: Verify Deployment

After pushing, GitHub Actions will automatically:
1. Build the site using Zensical
2. Deploy to GitHub Pages
3. Make it available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

You can check the deployment status in the **Actions** tab of your repository.

## Troubleshooting

### If you get "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### If you need to update the site URL later
1. Edit `zensical.toml`
2. Update `site_url`
3. Commit and push:
   ```bash
   git add zensical.toml
   git commit -m "Update site URL"
   git push
   ```

### If GitHub Pages doesn't deploy
1. Check the **Actions** tab for any errors
2. Ensure GitHub Pages is enabled in Settings → Pages
3. Verify the workflow file `.github/workflows/deploy.yml` exists

## Next Steps

Once deployed, you can:
- Access your documentation at the GitHub Pages URL
- Make changes locally and push to update the site
- Customize the domain (if desired) in repository Settings → Pages
