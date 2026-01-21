---
title: Problems API
description: API endpoints for problem creation and management
---

# Problems API

Endpoints for creating, updating, and managing programming problems.

## Create Problem

**`POST problem/create/`**

Creates a new problem.

**Privileges**: Logged-in user

**Parameters:**
- `title` (string, required): Problem title
- `alias` (string, required): Problem alias
- `source` (string, optional): Problem source (e.g., "OMI 2020")
- `public` (int, required): 0 for private, 1 for public
- `validator` (string, required): Validator type (see below)
- `time_limit` (int, required): Time limit in milliseconds
- `memory_limit` (int, required): Memory limit in KB
- `problem_contents` (FILE, required): ZIP file with problem contents

**Validator Types:**
- `literal`: Exact match
- `token`: Token-by-token comparison
- `token-caseless`: Case-insensitive token comparison
- `token-numeric`: Numeric comparison with tolerance
- `custom`: User-defined validator

**Response:**
```json
{
  "status": "ok",
  "uploaded_files": ["file1.in", "file1.out", ...]
}
```

## Get Problem Details

**`GET problems/:problem_alias/details/`**

Returns problem details within a contest context.

**Privileges**: Logged-in user; private contests require invitation

**Parameters:**
- `contest_alias` (string, required): Contest alias
- `lang` (string, optional): Language (default: "es")

**Response:**
```json
{
  "title": "Problem Title",
  "author_id": 123,
  "validator": "token-numeric",
  "time_limit": 3000,
  "memory_limit": 65536,
  "visits": 1000,
  "submissions": 500,
  "accepted": 200,
  "difficulty": 5.5,
  "creation_date": "2020-01-01T00:00:00Z",
  "source": "OMI 2020",
  "runs": [...]
}
```

## Related Documentation

- **[Creating Problems](../../features/problems/creating-problems.md)** - Problem creation guide
- **[Problem Format](../../features/problems/problem-format.md)** - ZIP file structure
- **[REST API Overview](rest-api.md)** - General API information
