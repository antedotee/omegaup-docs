---
title: Testing Guide
description: Comprehensive testing guide for omegaUp
---

# Testing Guide

omegaUp uses multiple testing frameworks to ensure code quality across different layers.

## Testing Stack

| Layer | Framework | Location |
|-------|-----------|----------|
| PHP Unit Tests | PHPUnit | `frontend/tests/controllers/` |
| TypeScript/Vue Tests | Jest | `frontend/www/js/` |
| E2E Tests | Cypress | `cypress/e2e/` |
| Python Tests | pytest | `stuff/` |

## PHP Unit Tests

### Running All PHP Tests

```bash
./stuff/runtests.sh
```

Runs PHPUnit tests, MySQL type validation, and Psalm.

**Location**: Inside Docker container

### Running Specific Test File

```bash
./stuff/run-php-tests.sh frontend/tests/controllers/MyControllerTest.php
```

Omit filename to run all tests.

### Test Requirements

- All tests must pass 100% before committing
- New functionality requires new/modified tests
- Tests located in `frontend/tests/controllers/`

## TypeScript/Vue Tests

### Running Vue Tests (Watch Mode)

```bash
yarn run test:watch
```

Automatically reruns tests when code changes.

**Location**: Inside Docker container

### Running Specific Test File

```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/MyComponent.test.ts
```

### Test Structure

Vue component tests check:
- Component visibility
- Event emission
- Expected behavior
- Props and state

## Cypress E2E Tests

### Opening Cypress Test Runner

```bash
npx cypress open
```

Opens graphical interface for interactive testing.

**Prerequisites**:
- Node.js installed
- npm installed
- libasound2 (Linux)

**Location**: Outside Docker container

### Running Cypress Tests

```bash
yarn test:e2e
```

Runs all Cypress tests headlessly.

### Test Files

E2E tests located in `cypress/e2e/`:
- `login.spec.ts`
- `problem-creation.spec.ts`
- `contest-management.spec.ts`
- And more...

## Python Tests

Python tests use pytest and are located in `stuff/` directory.

## Test Coverage

We use **Codecov** to measure coverage:

- **PHP**: Coverage measured ✅
- **TypeScript**: Coverage measured ✅
- **Cypress**: Coverage not yet measured ⚠️

## Best Practices

### Write Tests First
When possible, write tests before implementation (TDD).

### Test Critical Paths
Focus on:
- User authentication flows
- Problem submission and evaluation
- Contest management
- API endpoints

### Keep Tests Fast
- Unit tests should be fast (< 1 second)
- E2E tests can be slower but should complete in reasonable time

### Test Isolation
- Each test should be independent
- Clean up test data after tests
- Use test fixtures for consistent data

## Related Documentation

- **[Coding Guidelines](coding-guidelines.md)** - Code standards
- **[Useful Commands](useful-commands.md)** - Testing commands
- **[Cypress Guide](../../../frontend/www/docs/How-to-use-Cypress-in-omegaUp.md)** - Detailed Cypress guide
