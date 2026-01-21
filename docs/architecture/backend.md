---
title: Backend Architecture
description: PHP controllers, DAO/VO patterns, and API structure
---

# Backend Architecture

omegaUp's backend is built with PHP following the MVC pattern, with a clear separation between controllers, data access, and business logic.

## Directory Structure

```
frontend/server/src/
├── Controllers/           # API controllers
├── DAO/                  # Data Access Objects
│   ├── VO/               # Value Objects
│   └── Base/             # Base DAO classes
└── libs/                 # Libraries and utilities
```

## Controllers

Controllers handle HTTP requests and implement business logic:

- Located in `frontend/server/src/Controllers/`
- One controller per API resource (e.g., `RunController`, `ContestController`)
- Methods correspond to API endpoints (e.g., `apiCreate`, `apiDetails`)

## DAO/VO Pattern

### Value Objects (VO)
- Map directly to database tables
- Auto-generated from schema
- Located in `frontend/server/src/DAO/VO/`

### Data Access Objects (DAO)
- Static classes for database operations
- Methods: `search()`, `getByPK()`, `save()`, `delete()`
- Located in `frontend/server/src/DAO/`

### Example Usage

```php
// Create a VO
$user = new Users();
$user->setEmail('user@example.com');

// Search using DAO
$results = UsersDAO::search($user);

// Access results
if (count($results) > 0) {
    $foundUser = $results[0];
    echo $foundUser->getUserId();
}
```

## Related Documentation

- **[Database Patterns](../development/database-patterns.md)** - Detailed DAO/VO guide
- **[MVC Pattern](mvc-pattern.md)** - MVC implementation
- **[API Reference](../api/index.md)** - API endpoints
