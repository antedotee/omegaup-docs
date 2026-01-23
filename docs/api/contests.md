---
title: Contests API
description: API endpoints for contest management and participation
icon: bootstrap/trophy
---

# Contests API

!!! note "Note"
    For the most up-to-date API documentation, see the [Controllers README](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/README.md#contest).

## Overview

The Contests API provides endpoints for creating, managing, and participating in programming contests.

## Endpoints

### List Contests

**`GET contests/list/`**

Returns recent contests the user can view.

**Response:**
```json
{
  "results": [
    {
      "alias": "contest-alias",
      "contest_id": 123,
      "title": "Contest Title",
      "description": "Contest description",
      "start_time": 1436577101,
      "finish_time": 1436584301,
      "public": 1,
      "director_id": 456
    }
  ]
}
```

### Get Contest Details

**`GET contests/:contest_alias/details/`**

Returns detailed information about a contest.

**Privileges**: Public contests accessible to all; private contests require invitation.

### Create Contest

**`POST contests/create/`**

Creates a new contest. The logged-in user becomes the contest director.

**Parameters:**
- `title` (string, required): Contest title
- `alias` (string, required): Contest alias (used in URLs)
- `description` (string, required): Contest description
- `start_time` (int, required): Start time (UNIX timestamp)
- `finish_time` (int, required): End time (UNIX timestamp)
- `public` (int, required): 0 for private, 1 for public
- `scoreboard` (int, optional): Scoreboard visibility percentage (0-100)
- `window_length` (int, optional): USACO-style individual timer (minutes)
- `problems` (array, optional): Array of problem aliases

**Response:**
```json
{
  "status": "ok"
}
```

### Add Problem to Contest

**`POST contests/:contest_alias/addProblem/`**

Adds a problem to a contest.

**Privileges**: Contest director or higher

**Parameters:**
- `problem_alias` (string, required): Problem alias
- `points` (int, required): Point value (typically 100)
- `order_in_contest` (int, optional): Problem order

### Add User to Contest

**`POST contests/:contest_alias/addUser/`**

Adds a user to a private contest.

**Privileges**: Contest director or higher

**Parameters:**
- `username` (string, required): Username to add

## Related Documentation

- **[REST API Overview](rest-api.md)** - General API information
- **[Contests Feature](../../features/contests/index.md)** - Contest management guide
