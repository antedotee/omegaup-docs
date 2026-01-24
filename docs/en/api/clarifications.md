---
title: Clarifications API
description: Contest clarification endpoints
icon: bootstrap/help-circle
---

# Clarifications API

Endpoints for asking and answering questions during contests.

## Create Clarification

**`POST clarification/create/`**

Creates a new clarification for a problem in a contest. Clarifications are private by default.

**Privileges**: Logged-in user

**Parameters:**
- `contest_alias` (string, required): Contest alias
- `problem_alias` (string, required): Problem alias
- `message` (string, required): Clarification message

**Response:**
```json
{
  "status": "ok",
  "clarification_id": 123
}
```

## Get Clarification Details

**`GET clarification/:clarification_id/details/`**

Returns details of a specific clarification.

**Privileges**: Logged-in user with contest access

**Response:**
```json
{
  "message": "Question text",
  "answer": "Answer text",
  "time": "2020-01-01T12:00:00Z",
  "problem_id": 456,
  "contest_id": 789
}
```

## Update Clarification

**`POST clarification/:clarification_id/update/`**

Updates a clarification (typically to add an answer or make it public).

**Privileges**: Contest administrator or higher

**Parameters:**
- `contest_alias` (string, optional): Contest alias
- `problem_alias` (string, optional): Problem alias
- `message` (string, optional): Updated message
- `answer` (string, optional): Answer to the clarification
- `public` (int, optional): Make clarification public (0 or 1)

**Response:**
```json
{
  "status": "ok"
}
```

## Related Documentation

- **[REST API Overview](rest-api.md)** - General API information
- **[Contests API](contests.md)** - Contest management
- **[Arena](../../features/arena.md)** - Contest interface
