#!/bin/bash

# Setup script for creating a separate documentation repository
# This script initializes a new git repository in the docs folder
# and prepares it for pushing to GitHub

set -e

echo "🚀 Setting up separate documentation repository..."
echo ""

# Check if we're in the docs directory
if [ ! -f "zensical.toml" ]; then
    echo "❌ Error: This script must be run from the docs/ directory"
    echo "   Current directory: $(pwd)"
    exit 1
fi

# Check if git is already initialized
if [ -d ".git" ]; then
    echo "⚠️  Warning: Git repository already initialized"
    read -p "Do you want to reinitialize? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    echo "Removing existing .git directory..."
    rm -rf .git
fi

# Initialize git repository
echo "📦 Initializing git repository..."
git init
git branch -M main

# Add all files
echo "📝 Adding files..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: omegaUp documentation site

- 51 documentation files organized across 7 sections
- Zensical configuration with Material theme
- GitHub Actions workflow for automatic deployment
- Complete documentation covering architecture, API, development, features, operations, and community"

echo ""
echo "✅ Repository initialized successfully!"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Name: omegaup-docs (or your preferred name)"
echo "   - Do NOT initialize with README, .gitignore, or license"
echo "   - Click 'Create repository'"
echo ""
echo "2. Update site URL in zensical.toml:"
echo "   - Edit zensical.toml"
echo "   - Update site_url to: https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
echo ""
echo "3. Add remote and push:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git push -u origin main"
echo ""
echo "4. Enable GitHub Pages:"
echo "   - Go to repository Settings → Pages"
echo "   - Source: GitHub Actions"
echo ""
echo "📖 For detailed instructions, see SETUP_REPO.md"
