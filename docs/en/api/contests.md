---
title: Contests API
description: API endpoints for contest management and participation
icon: bootstrap/trophy
---

# Contests API

The Contests API provides comprehensive endpoints for creating, managing, and participating in programming contests.

## Overview

omegaUp contests support:

- **Multiple formats**: IOI, ICPC, and custom scoring
- **Flexible timing**: Fixed duration or USACO-style windows
- **Access control**: Public, private, or registration-based
- **Virtual contests**: Practice with past contest conditions

## Contest Management

### Create Contest

Creates a new contest. The authenticated user becomes the contest director.

**`POST /api/contest/create/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Unique contest alias (used in URLs) |
| `title` | string | Yes | Contest title |
| `description` | string | Yes | Contest description |
| `start_time` | int | Yes | Start timestamp (Unix) |
| `finish_time` | int | Yes | End timestamp (Unix) |
| `admission_mode` | string | No | `public`, `private`, or `registration` |
| `score_mode` | string | No | `all_or_nothing`, `partial`, `max_per_group` |
| `scoreboard` | int | No | Scoreboard visibility (0-100%) |
| `window_length` | int | No | USACO-style window in minutes |
| `submissions_gap` | int | No | Minimum seconds between submissions |
| `penalty` | string | No | `none`, `runtime`, `submission_count` |
| `penalty_calc_policy` | string | No | `sum`, `max` |
| `feedback` | string | No | `detailed`, `summary`, `none` |
| `languages` | string | No | Comma-separated language list |
| `show_scoreboard_after` | bool | No | Show scoreboard after contest |

**Response:**

```json
{
  "status": "ok"
}
```

---

### Update Contest

Updates an existing contest's settings.

**`POST /api/contest/update/`**

**Parameters:** Same as create, plus:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest to update |

**Privileges:** Contest admin

---

### Clone Contest

Creates a copy of an existing contest.

**`POST /api/contest/clone/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest to clone |
| `title` | string | Yes | New contest title |
| `alias` | string | Yes | New contest alias |
| `description` | string | Yes | New description |
| `start_time` | int | Yes | New start timestamp |

---

### Archive Contest

Archives a contest (hides from active lists).

**`POST /api/contest/archive/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `archive` | bool | Yes | true to archive, false to unarchive |

---

## Contest Information

### List Contests

Returns paginated list of contests.

**`GET /api/contest/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | int | No | Page number |
| `page_size` | int | No | Results per page |
| `query` | string | No | Search term |
| `tab_name` | string | No | `current`, `future`, `past` |
| `admission_mode` | string | No | Filter by admission mode |

**Response:**

```json
{
  "results": [
    {
      "alias": "contest-2024",
      "contest_id": 123,
      "title": "Annual Contest 2024",
      "description": "...",
      "start_time": { "time": 1704067200 },
      "finish_time": { "time": 1704153600 },
      "admission_mode": "public",
      "contestants": 150
    }
  ]
}
```

---

### My Contests

Returns contests where the user is admin.

**`GET /api/contest/myList/`**

---

### List Participating Contests

Returns contests where the user is participating.

**`GET /api/contest/listParticipating/`**

---

### Get Contest Details

Returns full contest information.

**`GET /api/contest/details/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |

**Response:**

```json
{
  "alias": "contest-2024",
  "title": "Annual Contest 2024",
  "description": "Contest description",
  "start_time": { "time": 1704067200 },
  "finish_time": { "time": 1704153600 },
  "admission_mode": "public",
  "score_mode": "partial",
  "scoreboard": 80,
  "problems": [...],
  "director": "admin_user",
  "languages": "cpp17-gcc,java,python3"
}
```

---

### Get Admin Details

Returns admin-specific contest information.

**`GET /api/contest/adminDetails/`**

**Privileges:** Contest admin

---

### Get Public Details

Returns publicly visible contest information.

**`GET /api/contest/publicDetails/`**

---

## Problem Management

### Add Problem

Adds a problem to a contest.

**`POST /api/contest/addProblem/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `problem_alias` | string | Yes | Problem to add |
| `points` | float | Yes | Point value |
| `order_in_contest` | int | No | Display order |
| `commit` | string | No | Specific problem version |

**Privileges:** Contest admin

---

### Remove Problem

Removes a problem from a contest.

**`POST /api/contest/removeProblem/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `problem_alias` | string | Yes | Problem to remove |

**Privileges:** Contest admin

---

### List Problems

Returns all problems in a contest.

**`GET /api/contest/problems/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |

---

## User & Access Management

### Add User

Adds a user to a private contest.

**`POST /api/contest/addUser/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `usernameOrEmail` | string | Yes | User to add |

**Privileges:** Contest admin

---

### Remove User

Removes a user from a contest.

**`POST /api/contest/removeUser/`**

---

### Add Group

Grants contest access to an entire group.

**`POST /api/contest/addGroup/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `group` | string | Yes | Group alias |

---

### Remove Group

**`POST /api/contest/removeGroup/`**

---

### List Users

Returns all users with contest access.

**`GET /api/contest/users/`**

---

### List Contestants

Returns actual contest participants.

**`GET /api/contest/contestants/`**

---

### Search Users

Searches users for adding to contest.

**`GET /api/contest/searchUsers/`**

---

## Admin Management

### Add Admin

Grants admin privileges to a user.

**`POST /api/contest/addAdmin/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `usernameOrEmail` | string | Yes | New admin |

---

### Remove Admin

**`POST /api/contest/removeAdmin/`**

---

### Add Group Admin

Grants admin to all group members.

**`POST /api/contest/addGroupAdmin/`**

---

### Remove Group Admin

**`POST /api/contest/removeGroupAdmin/`**

---

### List Admins

Returns all contest admins.

**`GET /api/contest/admins/`**

---

## Participation

### Open Contest

Opens a contest for the user (starts their timer in USACO mode).

**`POST /api/contest/open/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |

---

### Register for Contest

Registers for a registration-based contest.

**`POST /api/contest/registerForContest/`**

---

### Get User Role

Returns the user's role in a contest.

**`GET /api/contest/role/`**

**Response:**

```json
{
  "admin": false,
  "contestant": true,
  "reviewer": false
}
```

---

### Create Virtual Contest

Creates a virtual (practice) contest from a past contest.

**`POST /api/contest/createVirtual/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Original contest alias |
| `start_time` | int | Yes | Virtual start time |

---

## Scoreboard

### Get Scoreboard

Returns the current scoreboard.

**`GET /api/contest/scoreboard/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `token` | string | No | Scoreboard token (for shared URLs) |

**Response:**

```json
{
  "finish_time": { "time": 1704153600 },
  "problems": [...],
  "ranking": [
    {
      "username": "user1",
      "name": "User One",
      "country": "MX",
      "place": 1,
      "total": { "points": 300, "penalty": 120 },
      "problems": [
        { "alias": "prob-a", "points": 100, "penalty": 30, "runs": 1 }
      ]
    }
  ],
  "start_time": { "time": 1704067200 },
  "time": { "time": 1704100000 },
  "title": "Annual Contest 2024"
}
```

---

### Get Scoreboard Events

Returns scoreboard change events (for animations).

**`GET /api/contest/scoreboardEvents/`**

---

### Merge Scoreboards

Merges scoreboards from multiple contests.

**`GET /api/contest/scoreboardMerge/`**

---

## Runs & Submissions

### List Runs

Returns submissions for a contest.

**`GET /api/contest/runs/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `problem_alias` | string | No | Filter by problem |
| `username` | string | No | Filter by user |
| `status` | string | No | Filter by status |
| `verdict` | string | No | Filter by verdict |
| `language` | string | No | Filter by language |
| `offset` | int | No | Pagination offset |
| `rowcount` | int | No | Results per page |

---

### Runs Diff

Returns differences between runs.

**`GET /api/contest/runsDiff/`**

---

## Clarifications

### Get Clarifications

Returns contest clarifications.

**`GET /api/contest/clarifications/`**

---

### Get Problem Clarifications

Returns clarifications for a specific problem.

**`GET /api/contest/problemClarifications/`**

---

## Reports & Statistics

### Activity Report

Returns user activity during contest.

**`GET /api/contest/activityReport/`**

**Privileges:** Contest admin

---

### Contest Report

Returns detailed contest report.

**`GET /api/contest/report/`**

**Privileges:** Contest admin

---

### Contest Statistics

Returns contest statistics.

**`GET /api/contest/stats/`**

---

### Get Number of Contestants

**`GET /api/contest/getNumberOfContestants/`**

---

## Requests (Registration-Based)

### List Requests

Returns registration requests.

**`GET /api/contest/requests/`**

**Privileges:** Contest admin

---

### Arbitrate Request

Approves or denies a registration request.

**`POST /api/contest/arbitrateRequest/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `username` | string | Yes | Requesting user |
| `resolution` | bool | Yes | true=approve, false=deny |
| `note` | string | No | Optional note |

---

## Teams Integration

### Replace Teams Group

Replaces the teams group for a team contest.

**`POST /api/contest/replaceTeamsGroup/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `teams_group_alias` | string | Yes | New teams group |

---

## Other Operations

### Set Recommended

Marks a contest as recommended (staff only).

**`POST /api/contest/setRecommended/`**

---

### Update End Time for Identity

Extends time for a specific user (accommodations).

**`POST /api/contest/updateEndTimeForIdentity/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contest_alias` | string | Yes | Contest alias |
| `username` | string | Yes | User to extend |
| `end_time` | int | Yes | New end timestamp |

---

## Contest Modes

### Admission Modes

| Mode | Description |
|------|-------------|
| `public` | Anyone can participate |
| `private` | Invitation only |
| `registration` | Users must request access |

### Score Modes

| Mode | Description |
|------|-------------|
| `all_or_nothing` | Full points only for AC |
| `partial` | Partial points per test case |
| `max_per_group` | Maximum per test group |

### Penalty Modes

| Mode | Description |
|------|-------------|
| `none` | No penalty |
| `runtime` | Total runtime penalty |
| `submission_count` | Penalty per wrong submission |

---

## Related Documentation

- **[Runs API](runs.md)** - Submission management
- **[Problems API](problems.md)** - Problem management
- **[Clarifications API](clarifications.md)** - Contest Q&A
- **[Groups API](groups.md)** - Group management

## Full Reference

For complete implementation details, see the [Contest Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Contest.php) source code.
