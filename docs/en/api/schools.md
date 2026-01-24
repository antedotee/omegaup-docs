---
title: Schools API
description: API endpoints for school management and rankings
icon: bootstrap/school
---

# Schools API

The Schools API provides endpoints for managing schools, viewing school rankings, and the School of the Month program.

## Overview

Schools in omegaUp:

- Track user affiliations
- Contribute to school rankings based on member activity
- Participate in the School of the Month program

## Endpoints

### List Schools

Searches for schools matching a query. Used for typeahead/autocomplete.

**`GET /api/school/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes* | Search term |
| `term` | string | Yes* | Alternative search parameter |

*One of `query` or `term` is required.

**Response:**

```json
{
  "results": [
    {
      "key": 123,
      "value": "Massachusetts Institute of Technology"
    },
    {
      "key": 456,
      "value": "Stanford University"
    }
  ]
}
```

**Privileges:** Authenticated user

---

### Create School

Creates a new school entry.

**`POST /api/school/create/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | School name |
| `country_id` | string | No | Country code (e.g., "MX", "US") |
| `state_id` | string | No | State/province code |

**Response:**

```json
{
  "school_id": 789
}
```

**Notes:**

- If a school with the same name exists, returns the existing school ID
- State requires country to be specified

**Privileges:** Authenticated user

---

### Select School of the Month

Selects a school as the School of the Month (mentor only).

**`POST /api/school/selectSchoolOfTheMonth/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `school_id` | int | Yes | School ID to select |

**Response:**

```json
{
  "status": "ok"
}
```

**Privileges:** Mentor role

**Requirements:**

- Must be within the selection period
- School must be in the candidates list
- Cannot select if already selected for the month

---

## School Profile Data

School profiles include:

### Basic Information

- School name
- Location (country, state)
- Global ranking

### Statistics

- Monthly solved problems count
- Coders of the Month from the school
- Active users and their achievements

---

## School Rankings

Schools are ranked based on:

1. **Score**: Aggregate of member activity
2. **Problems Solved**: Total problems solved by members
3. **Active Users**: Number of contributing members

Rankings are cached and updated periodically.

---

## School of the Month

### Program Overview

Each month, a school is selected as "School of the Month" based on:

- Member activity and problem-solving
- Contest participation
- Quality contributions

### Selection Process

1. System generates candidates based on activity
2. Mentors can select from candidates during selection window
3. First-place candidate is selected by default if no mentor selection

### Candidate Data

```json
{
  "candidatesToSchoolOfTheMonth": [
    {
      "school_id": 123,
      "name": "Top University",
      "country_id": "MX",
      "ranking": 1,
      "score": 1500.5,
      "school_of_the_month_id": 456
    }
  ]
}
```

---

## School Profile Fields

| Field | Type | Description |
|-------|------|-------------|
| `school_id` | int | Unique identifier |
| `name` | string | School name |
| `country_id` | string | Country code |
| `ranking` | int | Global ranking position |
| `score` | float | Calculated activity score |

---

## Use Cases

### User Registration with School

```javascript
// Search for school
const schools = await fetch('/api/school/list/?query=MIT');
const results = await schools.json();

// Use school_id (key) in user profile
const schoolId = results.results[0].key;
```

### Create New School

```bash
curl -X POST https://omegaup.com/api/school/create/ \
  -d "name=New Tech University&country_id=US&state_id=CA"
```

---

## Related Data

### Monthly Solved Problems

Track school activity over time:

```json
{
  "monthly_solved_problems": [
    { "year": 2024, "month": 1, "problems_solved": 150 },
    { "year": 2024, "month": 2, "problems_solved": 175 }
  ]
}
```

### School Users

Top contributors from a school:

```json
{
  "school_users": [
    {
      "username": "top_coder",
      "classname": "user-rank-master",
      "created_problems": 10,
      "solved_problems": 500,
      "organized_contests": 5
    }
  ]
}
```

---

## Related Documentation

- **[Users API](users.md)** - User profile and school association
- **[Problems API](problems.md)** - Problem solving statistics

## Full Reference

For complete implementation details, see the [School Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/School.php) source code.
