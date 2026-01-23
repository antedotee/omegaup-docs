---
title: Problem Format
description: ZIP file structure for manual problem creation
icon: bootstrap/file-document
---

# Problem Format

For advanced problem creation, you can manually create a `.zip` file with the proper structure.

## ZIP File Structure

```
problem.zip
├── statements/
│   ├── es.markdown      # Spanish statement
│   ├── en.markdown      # English statement
│   └── pt.markdown      # Portuguese statement
├── cases/
│   ├── 01.in
│   ├── 01.out
│   ├── 02.in
│   ├── 02.out
│   └── ...
├── validator.cpp         # Optional: Custom validator
├── limits.json           # Optional: Custom limits
└── testplan              # Optional: Test case weights
```

## Statement Format

Statements are written in Markdown:

```markdown
# Problem Title

## Description

Problem description here...

## Input

Input format description...

## Output

Output format description...

## Examples

### Example 1

**Input:**
```
1 2
```

**Output:**
```
3
```
```

## Test Cases

Test cases are pairs of `.in` and `.out` files:

- `01.in`, `01.out`
- `02.in`, `02.out`
- `03.in`, `03.out`
- ...

## Validator

If using a custom validator, include the source code (e.g., `validator.cpp`).

## Related Documentation

- **[Creating Problems](creating-problems.md)** - Problem creation guide
- **[Manual ZIP Guide](../../../frontend/www/docs/Manual-for-Zip-File-Creation-for-Problems.md)** - Detailed format specification
