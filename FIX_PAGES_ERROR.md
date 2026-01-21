# Fix: GitHub Pages "Not Found" Error

## 🔴 Error Message

If you see this error in GitHub Actions:

```
Error: Get Pages site failed. Please verify that the repository has Pages enabled 
and configured to build using GitHub Actions, or consider exploring the `enablement` 
parameter for this action.
Error: HttpError: Not Found
```

## ✅ Solution

The workflow has been updated to automatically enable GitHub Pages. However, you still need to manually enable it the first time:

### Option 1: Enable via GitHub UI (Recommended for First Time)

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar, under "Code and automation")
4. Under **Build and deployment** → **Source**, select **GitHub Actions**
5. Click **Save** (if there's a save button)
6. Re-run the failed workflow (or push a new commit)

### Option 2: The Workflow Will Auto-Enable (After First Manual Enable)

The workflow has been updated with `enablement: true` which will automatically enable Pages if it's not already enabled. However, GitHub may still require the first manual enablement.

## 🔧 Updated Workflow

The workflow file (`.github/workflows/deploy.yml`) has been updated to include:

```yaml
- name: Setup Pages
  uses: actions/configure-pages@v4
  with:
    enablement: true
```

This tells GitHub Actions to automatically enable Pages if it's not already enabled.

## 📋 Step-by-Step Fix

1. **Enable Pages manually (first time only):**
   - Repository → Settings → Pages
   - Source: **GitHub Actions**
   - Save

2. **Re-run the workflow:**
   - Go to **Actions** tab
   - Click on the failed workflow run
   - Click **Re-run all jobs** (or **Re-run failed jobs**)

3. **Or push a new commit:**
   ```bash
   cd docs
   git commit --allow-empty -m "Trigger Pages deployment"
   git push
   ```

## ✅ Verification

After enabling Pages and re-running the workflow:

1. Check **Actions** tab - workflow should complete successfully
2. Go to **Settings → Pages** - you should see "Your site is live at..."
3. Visit the URL shown in Settings → Pages

## 🚨 Common Issues

### "Pages not available for private repositories"
- **Solution:** Make the repository public, or upgrade to GitHub Pro/Team/Enterprise

### "Permission denied"
- **Solution:** Ensure the workflow has these permissions:
  ```yaml
  permissions:
    contents: read
    pages: write
    id-token: write
  ```

### "Workflow still fails after enabling Pages"
- **Solution:** 
  1. Wait 1-2 minutes after enabling Pages
  2. Re-run the workflow
  3. Check that the workflow file has `enablement: true` in the configure-pages step

## 📝 Notes

- The first time you enable Pages, GitHub may require manual activation
- After the first successful deployment, subsequent deployments should work automatically
- The `enablement: true` parameter helps but may not work on the very first run
- Always check repository Settings → Pages to verify Pages is enabled
