#!/usr/bin/env python3
"""
Generate GSoC markdown pages from data file.

This script reads the GSoC data from _data/gsoc-data.json and generates
markdown files for each year.

Usage:
    python3 scripts/generate-gsoc-pages.py

After updating gsoc-data.json, run this script to regenerate all GSoC pages.
"""

import json
import sys
from pathlib import Path

# Get the project root directory (parent of scripts/)
PROJECT_ROOT = Path(__file__).parent.parent
DATA_FILE = PROJECT_ROOT / "docs" / "community" / "gsoc" / "_data" / "gsoc-data.json"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "community" / "gsoc"


def load_data():
    """Load GSoC data from JSON file."""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_current_year_page(year, year_data):
    """Generate markdown for current year (with project ideas and application process)."""
    lines = [
        "---",
        f"title: {year_data['title']}",
        f"description: {year_data['description']}",
        "icon: material/school",
        "---",
        "",
        f"# {year_data['title']}",
        "",
        year_data['intro'],
        "",
        "## Project Ideas",
        ""
    ]
    
    # Add project ideas
    for idea in year_data.get('project_ideas', []):
        lines.extend([
            f"### {idea['name']}",
            idea['description'],
            "",
            f"**Skills**: {idea['skills']}",
            f"**Size**: {idea['size']}",
            f"**Level**: {idea['level']}",
            ""
        ])
    
    # Add application process
    lines.append("## Application Process")
    lines.append("")
    
    for phase_key in ['phase1', 'phase2', 'phase3', 'phase4']:
        if phase_key in year_data.get('application_process', {}):
            phase = year_data['application_process'][phase_key]
            lines.append(f"### {phase['title']}")
            if 'steps' in phase:
                for i, step in enumerate(phase['steps'], 1):
                    lines.append(f"{i}. {step}")
            if 'description' in phase:
                lines.append(phase['description'])
            lines.append("")
    
    # Add communications
    if 'communications' in year_data:
        lines.append("## Communications")
        lines.append("")
        for comm in year_data['communications']:
            lines.append(f"- {comm}")
        lines.append("")
    
    # Add FAQ
    if 'faq' in year_data:
        lines.append("## FAQ")
        lines.append("")
        for item in year_data['faq']:
            lines.append(f"**{item['question']}**")
            lines.append(item['answer'])
            lines.append("")
    
    # Add related docs
    if 'related_docs' in year_data:
        lines.append("## Related Documentation")
        lines.append("")
        for doc in year_data['related_docs']:
            lines.append(f"- **{doc}**")
    
    return "\n".join(lines)


def generate_past_year_page(year, year_data):
    """Generate markdown for past year (with completed projects)."""
    lines = [
        "---",
        f"title: {year_data['title']}",
        f"description: {year_data['description']}",
        "icon: material/school",
        "---",
        "",
        f"# {year_data['title']}",
        "",
        year_data['intro'],
        "",
        "## Projects",
        ""
    ]
    
    # Add projects
    for project in year_data.get('projects', []):
        lines.extend([
            f"### {project['name']}",
            project['description'],
            "",
            f"**Result**: {project['result']}",
            ""
        ])
    
    # Add related docs
    if 'related_docs' in year_data:
        lines.append("## Related Documentation")
        lines.append("")
        for doc in year_data['related_docs']:
            lines.append(f"- **{doc}**")
    
    return "\n".join(lines)


def generate_page(year, data):
    """Generate a markdown page for a specific year."""
    year_data = data['years'][year]
    
    if year_data['type'] == 'current':
        content = generate_current_year_page(year, year_data)
    else:
        content = generate_past_year_page(year, year_data)
    
    # Write to file
    output_file = OUTPUT_DIR / f"{year}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Generated {output_file}")


def main():
    """Main function."""
    # Check if data file exists
    if not DATA_FILE.exists():
        print(f"Error: Data file not found: {DATA_FILE}")
        print("Please create the data file first.")
        sys.exit(1)
    
    # Load data
    print("Loading GSoC data...")
    try:
        data = load_data()
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in data file: {e}")
        sys.exit(1)
    
    # Generate pages for each year
    print("\nGenerating GSoC pages...")
    for year in sorted(data['years'].keys(), reverse=True):
        generate_page(year, data)
    
    print("\n✓ All GSoC pages generated successfully!")
    print("\nNote: Review the generated files and commit them to git.")


if __name__ == "__main__":
    main()
