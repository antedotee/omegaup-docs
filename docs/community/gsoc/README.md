# GSoC Dynamic Content System

This directory uses a data-driven approach to generate GSoC pages, eliminating the need to copy and paste content between years.

## How It Works

1. **Data File**: All year-specific content is stored in `_data/gsoc-data.json`
2. **Generator Script**: `scripts/generate-gsoc-pages.py` reads the data and generates markdown files
3. **Generated Pages**: The script creates `YYYY.md` files for each year

## Adding a New Year

### For Current Year (with project ideas):

1. Open `_data/gsoc-data.json`
2. Add a new entry under `years` with the year as the key:
   ```json
   "2026": {
     "type": "current",
     "title": "GSoC 2026",
     "description": "Google Summer of Code 2026 program at omegaUp",
     "intro": "Your introduction text here...",
     "project_ideas": [...],
     "application_process": {...},
     "communications": [...],
     "faq": [...],
     "related_docs": [...]
   }
   ```
3. Update the previous year's `type` to `"past"` and add `projects` array instead of `project_ideas`
4. Run the generator:
   ```bash
   python3 scripts/generate-gsoc-pages.py
   ```
5. Review the generated files and commit them

### For Past Year (completed projects):

1. Open `_data/gsoc-data.json`
2. Add a new entry under `years`:
   ```json
   "2025": {
     "type": "past",
     "title": "GSoC 2025",
     "description": "Google Summer of Code 2025 projects",
     "intro": "Projects completed during GSoC 2025.",
     "projects": [
       {
         "name": "Project Name",
         "description": "Project description",
         "result": "Project result/outcome"
       }
     ],
     "related_docs": [...]
   }
   ```
3. Run the generator script
4. Review and commit

## Updating Existing Content

Simply edit `_data/gsoc-data.json` and run the generator script. All pages will be regenerated with the updated content.

## Benefits

- **No Copy-Paste Errors**: Single source of truth for shared content
- **Consistency**: All pages follow the same structure
- **Easy Updates**: Update data file once, regenerate all pages
- **Version Control**: Data file shows exactly what changed between years

## File Structure

```
gsoc/
├── _data/
│   └── gsoc-data.json      # Single source of truth
├── _templates/             # (Legacy - not used anymore)
├── 2023.md                 # Generated file
├── 2024.md                 # Generated file
├── 2025.md                 # Generated file
├── index.md                # Manual file (not generated)
└── README.md               # This file
```

## Notes

- The generator script uses only Python standard library (no external dependencies)
- Generated files should be committed to git
- The data file (`gsoc-data.json`) is the source of truth - edit this, not the generated markdown files
- Always run the generator after updating the data file
