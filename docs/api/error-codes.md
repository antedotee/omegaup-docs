---
title: Error Codes Reference
description: Complete reference of API error codes and their meanings
icon: bootstrap/help-circle
---

# Error Codes Reference

This page documents all error codes returned by the omegaUp API, their HTTP status codes, and common causes.

## Error Response Format

All API errors follow this format:

```json
{
  "status": "error",
  "error": "Human-readable error message",
  "errorname": "errorKeyName",
  "errorcode": 400,
  "header": "HTTP/1.1 400 BAD REQUEST",
  "parameter": "field_name"
}
```

| Field | Description |
|-------|-------------|
| `status` | Always `"error"` for error responses |
| `error` | Localized human-readable message |
| `errorname` | Machine-readable error key |
| `errorcode` | HTTP status code |
| `header` | Full HTTP response header |
| `parameter` | (Optional) Parameter that caused the error |

---

## HTTP Status Codes

### 400 Bad Request

Invalid input or parameter errors.

| Error Name | Description |
|------------|-------------|
| `parameterEmpty` | Required parameter is empty |
| `parameterInvalid` | Parameter value is invalid |
| `parameterNotFound` | Referenced entity not found |
| `parameterStringTooLong` | String exceeds maximum length |
| `parameterStringTooShort` | String below minimum length |
| `parameterNumberTooSmall` | Number below minimum value |
| `parameterNumberTooLarge` | Number exceeds maximum value |
| `invalidAlias` | Invalid alias format |
| `aliasInUse` | Alias already exists |

**Example:**

```json
{
  "status": "error",
  "error": "problem_alias: Parameter is invalid",
  "errorname": "parameterInvalid",
  "errorcode": 400,
  "parameter": "problem_alias"
}
```

---

### 401 Unauthorized

Authentication required or invalid.

| Error Name | Description |
|------------|-------------|
| `loginRequired` | User must be logged in |
| `invalidCredentialsException` | Wrong username/password |
| `emailNotVerified` | Email verification pending |

**Example:**

```json
{
  "status": "error",
  "error": "Login required",
  "errorname": "loginRequired",
  "errorcode": 401
}
```

---

### 403 Forbidden

Authenticated but not authorized.

| Error Name | Description |
|------------|-------------|
| `userNotAllowed` | User lacks permission |
| `forbiddenInLockdown` | System in lockdown mode |
| `contestNotStarted` | Contest hasn't begun |
| `contestEnded` | Contest has finished |
| `cannotSubmit` | User cannot submit |

**Example:**

```json
{
  "status": "error",
  "error": "User is not allowed to perform this action",
  "errorname": "userNotAllowed",
  "errorcode": 403
}
```

---

### 404 Not Found

Requested resource doesn't exist.

| Error Name | Description |
|------------|-------------|
| `contestNotFound` | Contest doesn't exist |
| `problemNotFound` | Problem doesn't exist |
| `userNotExist` | User doesn't exist |
| `courseNotFound` | Course doesn't exist |
| `groupNotFound` | Group doesn't exist |
| `schoolNotFound` | School doesn't exist |
| `qualityNominationNotFound` | Nomination doesn't exist |

**Example:**

```json
{
  "status": "error",
  "error": "Problem not found",
  "errorname": "problemNotFound",
  "errorcode": 404
}
```

---

### 409 Conflict

Resource state conflict.

| Error Name | Description |
|------------|-------------|
| `duplicatedEntryInDatabase` | Record already exists |
| `identityInGroup` | User already in group |
| `teamMemberUsernameInUse` | Team member already assigned |

**Example:**

```json
{
  "status": "error",
  "error": "User is already a member of this group",
  "errorname": "identityInGroup",
  "errorcode": 409
}
```

---

### 412 Precondition Failed

Business logic constraint not met.

| Error Name | Description |
|------------|-------------|
| `qualityNominationMustHaveSolvedProblem` | Must solve before nominating |
| `qualityNominationMustNotHaveSolvedProblem` | Must not have solved (for before_ac) |
| `qualityNominationMustHaveTriedToSolveProblem` | Must have attempted problem |
| `contestCertificatesError` | Certificate generation error |
| `contestCertificatesCurrentContestError` | Contest hasn't ended |

---

### 429 Too Many Requests

Rate limit exceeded.

| Error Name | Description |
|------------|-------------|
| `rateLimitExceeded` | Too many API requests |
| `submissionWaitGap` | Submission rate limit |

**Headers included:**

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1704070800
Retry-After: 3600
```

---

### 500 Internal Server Error

Server-side errors.

| Error Name | Description |
|------------|-------------|
| `generalError` | Unexpected server error |
| `databaseOperationError` | Database query failed |

---

### 503 Service Unavailable

Service temporarily unavailable.

| Error Name | Description |
|------------|-------------|
| `serviceUnavailable` | Service temporarily down |

---

## Common Error Scenarios

### Authentication Errors

```json
// Wrong password
{
  "errorname": "invalidCredentialsException",
  "errorcode": 401
}

// Not logged in
{
  "errorname": "loginRequired", 
  "errorcode": 401
}

// Email not verified
{
  "errorname": "emailNotVerified",
  "errorcode": 401
}
```

### Validation Errors

```json
// Missing required field
{
  "errorname": "parameterEmpty",
  "parameter": "name",
  "errorcode": 400
}

// Invalid format
{
  "errorname": "parameterInvalid",
  "parameter": "email",
  "errorcode": 400
}

// Alias taken
{
  "errorname": "aliasInUse",
  "errorcode": 400
}
```

### Permission Errors

```json
// Not contest admin
{
  "errorname": "userNotAllowed",
  "errorcode": 403
}

// Contest not open yet
{
  "errorname": "contestNotStarted",
  "errorcode": 403
}
```

---

## Error Handling Best Practices

### Client-Side Handling

```javascript
async function makeAPICall(endpoint, data) {
  const response = await fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  
  if (result.status === 'error') {
    switch (result.errorcode) {
      case 401:
        // Redirect to login
        window.location.href = '/login/';
        break;
      case 403:
        // Show permission error
        alert(result.error);
        break;
      case 404:
        // Resource not found
        showNotFoundMessage(result.error);
        break;
      case 429:
        // Rate limited - retry after delay
        const retryAfter = response.headers.get('Retry-After');
        setTimeout(() => makeAPICall(endpoint, data), retryAfter * 1000);
        break;
      default:
        // Generic error handling
        console.error(result.error);
    }
    return null;
  }
  
  return result;
}
```

### Checking Specific Errors

```javascript
if (result.errorname === 'aliasInUse') {
  // Suggest alternative alias
  suggestAlternative(data.alias);
}
```

---

## Localization

Error messages are localized based on the user's language preference. The `errorname` field remains constant across languages for programmatic handling.

| Language | Example `error` value |
|----------|----------------------|
| English | "Login required" |
| Spanish | "Inicio de sesión requerido" |
| Portuguese | "Login necessário" |

---

## Related Documentation

- **[API Reference](index.md)** - API overview
- **[Authentication](authentication.md)** - Auth flow and errors

## Full Reference

For the complete list of exception classes, see the [Exceptions directory](https://github.com/omegaup/omegaup/tree/main/frontend/server/src/Exceptions) in the source code.
