---
title: Users API
description: User management and authentication endpoints
icon: bootstrap/account-group
---

# Users API

Endpoints for user management, authentication, and profile operations.

## Login

**`POST user/login/`**

Authenticates a user and returns an authentication token.

**Privileges**: None (public endpoint)

**Parameters:**
- `usernameOrEmail` (string, required): Username or email
- `password` (string, required): User password

**Response:**
```json
{
  "status": "ok",
  "auth_token": "abc123def456..."
}
```

!!! important "Token Usage"
    Include the `auth_token` in a cookie named `ouat` for subsequent authenticated requests.

## Create User

**`POST user/create/`**

Creates a new user account.

**Privileges**: None (public endpoint)

**Parameters:**
- `username` (string, required): Username
- `password` (string, required): Password
- `email` (string, required): Email address

**Response:**
```json
{
  "status": "ok"
}
```

## Get User Profile

**`GET user/profile/`**

Returns user profile information.

**Privileges**: Logged-in user (own profile) or public profile

**Response:**
```json
{
  "username": "user123",
  "name": "User Name",
  "email": "user@example.com",
  "solved": 50,
  "submissions": 200,
  ...
}
```

## Related Documentation

- **[Authentication Guide](authentication.md)** - Authentication flow
- **[REST API Overview](rest-api.md)** - General API information
