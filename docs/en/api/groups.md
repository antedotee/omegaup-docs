---
title: Groups API
description: API endpoints for managing groups and group scoreboards
icon: bootstrap/account-group
---

# Groups API

Groups allow you to organize users together for collective scoreboards and contests. This API provides endpoints for creating groups, managing members, and handling group scoreboards.

## Overview

Groups in omegaUp serve two main purposes:

1. **User Organization**: Group users together for tracking and management
2. **Scoreboards**: Create custom scoreboards that aggregate results from multiple contests

## Group Endpoints

### Create Group

Creates a new group. The authenticated user becomes the group admin.

**`POST /api/group/create/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Unique group alias (used in URLs) |
| `name` | string | Yes | Display name for the group |
| `description` | string | Yes | Group description |

**Response:**

```json
{
  "status": "ok"
}
```

**Privileges:** Authenticated user (becomes admin)

---

### Update Group

Updates an existing group's information.

**`POST /api/group/update/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `alias` | string | Yes | Group alias |
| `name` | string | Yes | New display name |
| `description` | string | Yes | New description |

**Privileges:** Group admin

---

### Get Group Details

Returns detailed information about a group including its scoreboards.

**`GET /api/group/details/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |

**Response:**

```json
{
  "group": {
    "create_time": 1609459200,
    "alias": "my-group",
    "name": "My Group",
    "description": "A sample group"
  },
  "scoreboards": [
    {
      "alias": "scoreboard-1",
      "create_time": "2021-01-01T00:00:00Z",
      "description": "Main scoreboard",
      "name": "Main Scoreboard"
    }
  ]
}
```

**Privileges:** Group admin

---

### List User's Groups

Returns all groups administered by the current user.

**`GET /api/group/myList/`**

**Response:**

```json
{
  "groups": [
    {
      "alias": "group-1",
      "create_time": { "time": 1609459200 },
      "description": "Description",
      "name": "Group Name"
    }
  ]
}
```

**Privileges:** Authenticated user

---

### Search Groups

Returns groups matching a search query. Used for typeahead.

**`GET /api/group/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search term |

**Response:**

```json
[
  {
    "label": "Group Name",
    "value": "group-alias"
  }
]
```

**Privileges:** Authenticated user

---

### Get Group Members

Returns all members of a group.

**`GET /api/group/members/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |

**Response:**

```json
{
  "identities": [
    {
      "username": "user1",
      "name": "User One",
      "country": "MX",
      "country_id": "MX",
      "school": "School Name",
      "school_id": 123
    }
  ]
}
```

**Privileges:** Group admin

---

### Add User to Group

Adds a user to a group.

**`POST /api/group/addUser/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `usernameOrEmail` | string | Yes | Username or email of user to add |

**Response:**

```json
{
  "status": "ok"
}
```

**Privileges:** Group admin

**Errors:**

- `identityInGroup`: User is already a member of the group

---

### Remove User from Group

Removes a user from a group.

**`POST /api/group/removeUser/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `usernameOrEmail` | string | Yes | Username or email of user to remove |

**Privileges:** Group admin

---

### Create Scoreboard

Creates a new scoreboard for a group.

**`POST /api/group/createScoreboard/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `alias` | string | Yes | Scoreboard alias |
| `name` | string | Yes | Scoreboard display name |
| `description` | string | No | Scoreboard description |

**Privileges:** Group admin

---

## Group Scoreboard Endpoints

Group scoreboards aggregate results from multiple contests.

### Add Contest to Scoreboard

Adds a contest to a group scoreboard.

**`POST /api/groupScoreboard/addContest/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `scoreboard_alias` | string | Yes | Scoreboard alias |
| `contest_alias` | string | Yes | Contest to add |
| `weight` | float | Yes | Weight for scoring |
| `only_ac` | bool | No | Only count AC submissions |

**Privileges:** Group admin + contest access

---

### Remove Contest from Scoreboard

Removes a contest from a group scoreboard.

**`POST /api/groupScoreboard/removeContest/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `scoreboard_alias` | string | Yes | Scoreboard alias |
| `contest_alias` | string | Yes | Contest to remove |

**Privileges:** Group admin

---

### Get Scoreboard Details

Returns scoreboard details including ranking and contests.

**`GET /api/groupScoreboard/details/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |
| `scoreboard_alias` | string | Yes | Scoreboard alias |

**Response:**

```json
{
  "ranking": [
    {
      "username": "user1",
      "name": "User One",
      "contests": {
        "contest-1": { "points": 100, "penalty": 50 }
      },
      "total": { "points": 100, "penalty": 50 }
    }
  ],
  "scoreboard": {
    "alias": "scoreboard-1",
    "name": "Main Scoreboard",
    "description": "Description"
  },
  "contests": [...]
}
```

**Privileges:** Group admin

---

### List Group Scoreboards

Returns all scoreboards for a group.

**`GET /api/groupScoreboard/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_alias` | string | Yes | Group alias |

**Privileges:** Group admin

---

## Use Cases

### Creating a Class Group

```bash
# 1. Create the group
curl -X POST https://omegaup.com/api/group/create/ \
  -d "alias=algorithms-2024&name=Algorithms 2024&description=Spring semester class"

# 2. Add students
curl -X POST https://omegaup.com/api/group/addUser/ \
  -d "group_alias=algorithms-2024&usernameOrEmail=student1@example.com"

# 3. Create a scoreboard
curl -X POST https://omegaup.com/api/group/createScoreboard/ \
  -d "group_alias=algorithms-2024&alias=homework&name=Homework Scores"

# 4. Add contests to scoreboard
curl -X POST https://omegaup.com/api/groupScoreboard/addContest/ \
  -d "group_alias=algorithms-2024&scoreboard_alias=homework&contest_alias=hw1&weight=1.0"
```

## Related Documentation

- **[Teams API](teams.md)** - For managing team groups
- **[Contests API](contests.md)** - Creating contests for groups
- **[Users API](users.md)** - User management

## Full Reference

For complete endpoint details, see the [Group Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Group.php) and [GroupScoreboard Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/GroupScoreboard.php) source code.
