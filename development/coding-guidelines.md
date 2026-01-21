---
title: Coding Guidelines
description: Coding standards and best practices for omegaUp development
---

# Coding Guidelines

This document outlines the coding standards and best practices for contributing to omegaUp. These guidelines are enforced by automated linters and integration tests.

## General Principles

### Type Safety

All code must declare data types in function parameters and return types:

- **TypeScript** for frontend (`frontend/www/`)
- **Psalm** for PHP (`frontend/server/`)
- **mypy** for Python (`stuff/`)

!!! tip "Type Annotations"
    Prefer type annotations for arrays/maps inside functions to make code easier to understand.

### Language

- All code and comments are written in **English**

### Testing

- Changes in functionality must be accompanied by tests
- All tests must pass 100% before committing
- No exceptions

### Code Quality

- Avoid `null` and `undefined` wherever possible
- Use [Guard Clause Pattern](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html)
- Remove unused code (don't comment it out - use git history)
- Minimize distance between variable declaration and first use

### Naming Conventions

- **camelCase** for functions, variables, and classes
- **snake_case** exceptions:
  - MySQL column names
  - Python variables and parameters
  - API parameters

!!! warning "Abbreviations"
    Avoid abbreviations in code and comments. They're not obvious to everyone.

## Code Formatting

We delegate formatting to automated tools:

- **[yapf](https://github.com/google/yapf)** for Python
- **[prettier.io](https://prettier.io/)** for TypeScript/Vue
- **[phpcbf](https://github.com/squizlabs/PHP_CodeSniffer)** for PHP

Validate style with:

```bash
./stuff/lint.sh validate
```

### Style Guidelines

- Use 2/4 spaces (depends on file type), not tabs
- Unix-style line endings (`\n`), not Windows (`\r\n`)
- Opening brackets on same line as statement
- Space between keywords and parentheses: `if`, `else`, `while`, `switch`, `catch`, `function`
- No space before function call parentheses
- No spaces inside parentheses
- Space after comma, not before
- Binary operators: space before and after
- Maximum one blank line in a row
- No empty comments
- Only `//` line comments, no `/* */` block comments

## PHP Guidelines

### Testing

```php
// Tests must pass 100% before committing
// All functionality changes need tests
```

### Database Queries

Avoid O(n) queries. Create manual queries for single round trips:

```php
// ❌ Bad: Multiple queries
foreach ($users as $user) {
    $runs = RunsDAO::searchByUserId($user->userId);
}

// ✅ Good: Single query
$runs = RunsDAO::searchByUserIds(array_map(fn($u) => $u->userId, $users));
```

### Function Parameters

API functions are the only ones that can receive `\OmegaUp\Request`. All other functions must:

1. Validate parameters
2. Extract to typed variables
3. Call functions with these variables

### Function Documentation

All functions must be documented:

```php
/**
 * set
 *
 * If cache is on, save value in key with given timeout
 *
 * @param string $value
 * @param int $timeout
 * @return boolean
 */
public function set($value, $timeout) { ... }
```

### Exceptions

Use exceptions to report errors. Functions returning true/false are allowed when they represent expected values.

### API Responses

All APIs must return associative arrays.

## Vue.js Guidelines

### Component Behavior

Avoid components that change behavior significantly based on flags. Use `slot`s instead:

```vue
<!-- ✅ Good: Using slots for customization -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```

### Internationalization

Never hardcode text. Always use translation strings:

```typescript
// ❌ Bad: Hardcoded text
<div>Contest ranking: {{ user.rank }}</div>

// ✅ Good: Translation string
<div>{{ T.contestRanking }}</div>
```

!!! tip "String Formatting"
    Avoid concatenating translation strings. Use `ui.formatString()` with parameters instead.

### Colors

Avoid hexadecimal or `rgb()` colors. Use CSS variables for dark mode support.

### Lifecycle Hooks

Avoid lifecycle hooks unless directly interacting with DOM. Direct DOM interaction should also be avoided.

### Computed Properties

Prefer computed properties and watchers over programmatic variable manipulation.

### Storybook

Add Storybook stories for new components. Update stories when modifying existing components.

## TypeScript Guidelines

### Function Parameters

When a function has more than 2-3 parameters, especially of the same type, use an object:

```typescript
// ❌ Bad: Too many parameters
function updateProblem(
  problem: Problem,
  previousVersion: string,
  currentVersion: string,
  points?: int
): void { ... }

// ✅ Good: Object parameter
function updateProblem({
  problem,
  previousVersion,
  currentVersion,
  points,
}: {
  problem: Problem;
  previousVersion: string;
  currentVersion: string;
  points?: int;
}): void { ... }
```

### Type Assertions

Avoid type assertions except for:
- DOM interactions (`document.querySelector`)
- Empty literal type declarations: `null as null | string`
- Testing: declaring `params` in Vue constructor

### jQuery Deprecation

`jQuery` has been deprecated and cannot be used.

## Python Guidelines

### Function Parameters

For functions with many parameters, especially optional ones, use keyword-only parameters:

```python
# ❌ Bad: Positional parameters
def updateProblem(
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None
) -> None: ...

# ✅ Good: Keyword-only parameters
def updateProblem(
    *,
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None,
) -> None: ...
```

### Naming

- **snake_case** for functions and variables
- **CamelCase** for classes

### Imports

Avoid `from module import function`. Import modules and use dot notation:

```python
# ❌ Bad
from module import function
function()

# ✅ Good
import module
module.function()
```

Exception: `typing` module can use `from typing import ...`

## Comments

Comments should explain **why**, not **what**:

```php
// ❌ Bad: Explains what
// Increment counter
$counter++;

// ✅ Good: Explains why
// Increment counter to track retry attempts for rate limiting
$counter++;
```

## Related Documentation

- **[Testing Guide](testing.md)** - How to write tests
- **[Useful Commands](useful-commands.md)** - Development commands
- **[Components Guide](components.md)** - Vue component development

---

**Remember:** These guidelines are enforced by automated tools. Run `./stuff/lint.sh` before committing!
