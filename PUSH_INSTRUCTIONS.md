# Push Instructions: Separate Documentation Repository

## ✅ Repository Status

Your documentation repository has been successfully initialized as a separate git repository!

**Commit:** `d678d69` - Initial commit: omegaUp documentation site  
**Files:** 68 files committed (51 markdown files + assets + config)  
**Branch:** `main`

## 🚀 Next Steps to Push to GitHub

### Step 1: Create GitHub Repository

1. Go to **https://github.com/new**
2. Fill in the form:
   - **Repository name:** `omegaup-docs` (or your preferred name)
   - **Description:** `Documentation site for omegaUp built with Zensical`
   - **Visibility:** Public (recommended for documentation)
   - **⚠️ IMPORTANT:** Do NOT check any boxes (no README, .gitignore, or license)
3. Click **Create repository**

### Step 2: Update Site URL

Before pushing, update the `site_url` in `zensical.toml`:

```bash
# Edit zensical.toml
# Update this line:
site_url = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
```

**Example:**
- If your GitHub username is `omegaup` and repo is `omegaup-docs`:
  ```toml
  site_url = "https://omegaup.github.io/omegaup-docs"
  ```

### Step 3: Commit URL Change (if updated)

```bash
cd docs
git add zensical.toml
git commit -m "Update site URL for GitHub Pages"
```

### Step 4: Add Remote and Push

```bash
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/omegaup/omegaup-docs.git
git push -u origin main
```

### Step 5: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **Source**, select **GitHub Actions**
5. The site will automatically deploy when you push

### Step 6: Verify Deployment

1. Go to the **Actions** tab in your repository
2. You should see a workflow run called "Deploy to GitHub Pages"
3. Wait for it to complete (usually 1-2 minutes)
4. Once complete, your site will be available at:
   `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## 📋 Quick Command Reference

```bash
# Navigate to docs directory
cd docs

# Check repository status
git status

# View commit history
git log --oneline

# Add remote (replace with your values)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main

# Check remote
git remote -v
```

## 🔧 Troubleshooting

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### "failed to push some refs"
Make sure you created the repository on GitHub first, and didn't initialize it with any files.

### GitHub Pages not deploying
1. Check **Actions** tab for errors
2. Verify GitHub Pages is enabled: Settings → Pages → Source: GitHub Actions
3. Ensure `.github/workflows/deploy.yml` exists (it should!)

### Need to update site URL later
```bash
# Edit zensical.toml, then:
git add zensical.toml
git commit -m "Update site URL"
git push
```

## 📦 What's Included

Your repository contains:
- ✅ 51 documentation markdown files
- ✅ 9 image assets (logos, favicons, illustrations)
- ✅ Zensical configuration (`zensical.toml`)
- ✅ GitHub Actions workflow (`.github/workflows/deploy.yml`)
- ✅ Git ignore rules (`.gitignore`)
- ✅ Setup documentation (README.md, SETUP_REPO.md, QUICK_START.md)

The `site/` directory is gitignored and will be generated during GitHub Actions build.

## 🎉 Success!

Once pushed and deployed, your documentation site will be live at:
`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

You can then:
- Make changes locally
- Commit and push to update the site
- Customize the domain (if desired) in repository Settings → Pages
