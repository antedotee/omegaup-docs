---
title: Teams API
description: API endpoints for managing team groups and team competitions
icon: bootstrap/account-group
---

# Teams API

The Teams API allows you to create and manage team groups for team-based competitions. Teams are groups of users who compete together as a single unit.

## Overview

Team groups in omegaUp enable:

- **Team Competitions**: Multiple users solving problems together
- **Configurable Team Size**: 1-10 contestants per team
- **Team Identity Management**: Each team has its own identity

## Team Group Endpoints

### Create Team Group

Creates a new team group. The authenticated user becomes the admin.

**`POST /api/teamsGroup/create/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Unique team group alias |
| `name` | string | Yes | Display name |
| `description` | string | Yes | Description |
| `numberOfContestants` | int | No | Team size (default: 3, max: 10) |

**Response:**

```json
{
  "status": "ok"
}
```

**Privileges:** Authenticated user (13+)

---

### Update Team Group

Updates an existing team group.

**`POST /api/teamsGroup/update/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Team group alias |
| `name` | string | Yes | New display name |
| `description` | string | Yes | New description |
| `numberOfContestants` | int | Yes | Team size (1-10) |

**Privileges:** Team group admin

---

### Get Team Group Details

Returns detailed information about a team group.

**`GET /api/teamsGroup/details/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | Team group alias |

**Response:**

```json
{
  "team_group": {
    "create_time": 1609459200,
    "alias": "icpc-team-2024",
    "name": "ICPC Team 2024",
    "description": "Our ICPC competitive team"
  }
}
```

**Privileges:** Team group admin

---

### List Team Groups

Returns team groups matching a search query.

**`GET /api/teamsGroup/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search term |

**Response:**

```json
[
  {
    "key": "icpc-team-2024",
    "value": "ICPC Team 2024"
  }
]
```

**Privileges:** Authenticated user

---

### List Teams in Group

Returns all teams (identities) in a team group.

**`GET /api/teamsGroup/teams/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | Team group alias |

**Response:**

```json
{
  "identities": [
    {
      "username": "team:icpc-team-2024:alpha",
      "name": "Team Alpha",
      "country": "MX",
      "school": "University"
    }
  ]
}
```

**Privileges:** Team group admin

---

### Remove Team

Removes a team from a team group.

**`POST /api/teamsGroup/removeTeam/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | Team group alias |
| `usernameOrEmail` | string | Yes | Team username to remove |

**Privileges:** Team group admin

---

## Team Member Endpoints

### Add Members to Team

Adds one or more users to a specific team.

**`POST /api/teamsGroup/addMembers/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | The team's username (e.g., `team:group:teamname`) |
| `usernames` | string | Yes | Comma-separated list of usernames |

**Response:**

```json
{
  "status": "ok"
}
```

**Privileges:** Team group admin

**Errors:**

- `teamMemberUsernameInUse`: Member is already in a team

---

### Remove Team Member

Removes a member from a team.

**`POST /api/teamsGroup/removeMember/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | The team's username |
| `username` | string | Yes | Username of member to remove |

**Privileges:** Team group admin

---

### List Team Members

Returns all members across all teams in a team group.

**`GET /api/teamsGroup/teamsMembers/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_alias` | string | Yes | Team group alias |
| `page` | int | No | Page number (default: 1) |
| `page_size` | int | No | Results per page (default: 100) |

**Response:**

```json
{
  "pageNumber": 1,
  "totalRows": 15,
  "teamsUsers": [
    {
      "username": "user1",
      "name": "User One",
      "team_alias": "alpha",
      "team_name": "Team Alpha",
      "classname": "user-rank-expert",
      "isMainUserIdentity": true
    }
  ]
}
```

**Privileges:** Team group admin

---

## Team Username Format

Teams have a special username format:

```
team:{team_group_alias}:{team_name}
```

For example: `team:icpc-2024:alpha`

This username is used to:
- Log in as the team
- Reference the team in API calls
- Display on scoreboards

---

## Configuration

### Team Size Limits

- **Default team size**: 3 contestants
- **Maximum team size**: 10 contestants
- Team size is configured per team group

---

## Use Cases

### Setting Up an ICPC-Style Competition

```bash
# 1. Create team group with 3-person teams
curl -X POST https://omegaup.com/api/teamsGroup/create/ \
  -d "alias=icpc-regionals-2024&name=ICPC Regionals 2024&description=Regional contest&numberOfContestants=3"

# 2. Teams are created via bulk upload or identity management

# 3. Add members to a team
curl -X POST https://omegaup.com/api/teamsGroup/addMembers/ \
  -d "team_group_alias=team:icpc-regionals-2024:mit-alpha&usernames=alice,bob,charlie"

# 4. Use contest API to create contest and add team group
```

---

## Related Documentation

- **[Groups API](groups.md)** - For regular user groups
- **[Contests API](contests.md)** - Creating team contests
- **[Authentication](authentication.md)** - Team login flow

## Full Reference

For complete endpoint details, see the [TeamsGroup Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/TeamsGroup.php) source code.
