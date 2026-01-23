---
title: Runs API
description: Submission handling and result retrieval endpoints
icon: bootstrap/play-circle
---

# Runs API

Endpoints for submitting code and retrieving submission results.

## Create Run (Submit Code)

**`POST runs/create/`**

Creates a new submission for a problem in a contest.

**Privileges**: Logged-in user

**Parameters:**
- `problem_alias` (string, required): Problem alias
- `contest_alias` (string, required): Contest alias
- `language` (string, required): Programming language
- `source` (string, required): Source code

**Response:**
```json
{
  "status": "ok",
  "guid": "abc123def456..."
}
```

## Get Run Details

**`GET runs/:run_alias/details/`**

Returns details of a specific submission.

**Privileges**: Logged-in user

**Response:**
```json
{
  "guid": "abc123def456...",
  "language": "cpp",
  "status": "ready",
  "verdict": "AC",
  "runtime": 150,
  "memory": 2048,
  "score": 1.0,
  "contest_score": 100,
  "time": 1436577101,
  "submit_delay": 30
}
```

## Get Run Source

**`GET runs/:run_alias/source/`**

Returns the source code of a submission. If compilation failed, returns compilation error.

**Privileges**: Logged-in user

**Response:**
```json
{
  "source": "#include <iostream>...",
  "compilation_error": null
}
```

## Run Status Values

- `new`: Just created
- `waiting`: In queue
- `compiling`: Being compiled
- `running`: Executing
- `ready`: Evaluation complete

## Verdict Values

- `AC`: Accepted
- `PA`: Partially Accepted
- `PE`: Presentation Error
- `WA`: Wrong Answer
- `TLE`: Time Limit Exceeded
- `OLE`: Output Limit Exceeded
- `MLE`: Memory Limit Exceeded
- `RTE`: Runtime Error
- `RFE`: Restricted Function Error
- `CE`: Compilation Error
- `JE`: Judge Error

## Related Documentation

- **[REST API Overview](rest-api.md)** - General API information
- **[Grader](../../features/grader.md)** - Evaluation system
- **[Runner](../../features/runner.md)** - Code execution
