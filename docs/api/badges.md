---
title: Badges API
description: API endpoints for the achievement badge system
icon: bootstrap/award
---

# Badges API

Badges are achievements that users earn for various accomplishments on the platform. This API allows you to query badges and user badge ownership.

## Overview

The badge system in omegaUp rewards users for:

- Solving problems
- Participating in contests
- Community contributions
- Special achievements

Badges are automatically assigned by background processes when users meet the criteria.

## Endpoints

### List All Badges

Returns a list of all available badge aliases.

**`GET /api/badge/list/`**

**Response:**

```json
[
  "problemSetter",
  "contestParticipant",
  "100Problems",
  "firstAC"
]
```

**Privileges:** Public (no authentication required)

---

### Get User's Badges

Returns all badges owned by the current authenticated user.

**`GET /api/badge/myList/`**

**Response:**

```json
{
  "badges": [
    {
      "badge_alias": "firstAC",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 50000,
      "total_users": 100000
    }
  ]
}
```

**Privileges:** Authenticated user

---

### Get Badges by Username

Returns all badges owned by a specific user.

**`GET /api/badge/userList/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target_username` | string | Yes | Username to query |

**Response:**

```json
{
  "badges": [
    {
      "badge_alias": "problemSetter",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 1500,
      "total_users": 100000
    }
  ]
}
```

**Privileges:** Public

---

### Get Badge Details

Returns detailed information about a specific badge.

**`GET /api/badge/badgeDetails/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `badge_alias` | string | Yes | Badge alias |

**Response:**

```json
{
  "badge_alias": "100Problems",
  "assignation_time": null,
  "first_assignation": { "time": 1546300800 },
  "owners_count": 2500,
  "total_users": 100000
}
```

**Fields:**

| Field | Description |
|-------|-------------|
| `badge_alias` | Unique badge identifier |
| `assignation_time` | When current user earned it (null if not owned) |
| `first_assignation` | When badge was first ever awarded |
| `owners_count` | Number of users who have this badge |
| `total_users` | Total registered users (for percentage calculation) |

**Privileges:** Public

---

### Get Badge Assignment Time

Returns when the current user earned a specific badge.

**`GET /api/badge/myBadgeAssignationTime/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `badge_alias` | string | Yes | Badge alias |

**Response:**

```json
{
  "assignation_time": { "time": 1609459200 }
}
```

Returns `null` for `assignation_time` if the user doesn't have the badge.

**Privileges:** Authenticated user

---

## Available Badges

Badges are defined in the `frontend/badges/` directory. Each badge has:

- A unique alias (folder name)
- An icon (`icon.svg`)
- Localized descriptions
- Assignment criteria (SQL or code-based)

Common badge categories:

### Problem Solving
- `firstAC` - First accepted submission
- `100Problems` - Solved 100 problems
- `legacyUser` - Early platform user

### Contest Participation
- `contestParticipant` - Participated in a contest
- `virtualContestParticipant` - Participated in a virtual contest

### Content Creation
- `problemSetter` - Created a public problem
- `problemSetterAdvanced` - Created multiple quality problems

### Community
- `coderOfTheMonth` - Selected as coder of the month

---

## Badge Assignment

Badges are automatically assigned by:

1. **Cron jobs** - Periodic checks for criteria
2. **Event triggers** - Immediate assignment on qualifying actions

Users cannot manually claim badges.

---

## Use Cases

### Display User Achievements

```javascript
// Fetch user's badges for profile display
const response = await fetch('/api/badge/userList/?target_username=omegaup');
const { badges } = await response.json();

badges.forEach(badge => {
  console.log(`${badge.badge_alias}: ${badge.owners_count} owners`);
});
```

### Check Badge Rarity

```javascript
// Calculate badge rarity percentage
const details = await fetch('/api/badge/badgeDetails/?badge_alias=100Problems');
const badge = await details.json();

const rarity = (badge.owners_count / badge.total_users * 100).toFixed(2);
console.log(`${rarity}% of users have this badge`);
```

---

## Related Documentation

- **[Users API](users.md)** - User profile information
- **[Problems API](problems.md)** - Problem-related achievements
- **[Contests API](contests.md)** - Contest-related achievements

## Full Reference

For complete badge definitions and assignment logic, see the [Badge Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Badge.php) and [badges directory](https://github.com/omegaup/omegaup/tree/main/frontend/badges).
