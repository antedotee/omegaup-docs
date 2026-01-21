---
title: Useful Development Commands
description: Common commands and shortcuts for omegaUp development
---

# Useful Development Commands

Quick reference for common development commands in omegaUp.

## Linting and Validation

### Run All Linters
```bash
./stuff/lint.sh
```
Runs all code validations. Automatically runs on `git push`.

**Location:** Outside Docker container, project root

### Validate Style Only
```bash
./stuff/lint.sh validate
```
Validates code style without fixing issues.

### Generate i18n Files
```bash
./stuff/lint.sh --linters=i18n fix --all
```
Generates `*.lang` files based on `es.lang`, `en.lang`, and `pt.lang`.

## Testing

### Run All PHP Tests
```bash
./stuff/runtests.sh
```
Runs PHPUnit tests, MySQL type validation, and Psalm.

**Location:** Inside Docker container

### Run Specific PHP Test File
```bash
./stuff/run-php-tests.sh frontend/tests/controllers/$MY_FILE.php
```
Runs unit tests for a single PHP file. Omit filename to run all tests.

### Run Cypress Tests
```bash
npx cypress open
```
Opens Cypress Test Runner GUI for interactive testing.

**Prerequisites:**
- Node.js installed
- npm installed
- libasound2 (Linux)

**Location:** Outside Docker container

### Run Vue Unit Tests (Watch Mode)
```bash
yarn run test:watch
```
Runs Vue tests in watch mode, auto-rerunning on code changes.

### Run Specific Vue Test File
```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/$MY_FILE.test.ts
```
Runs a single Vue test file.

## Database

### Reset Database to Initial State
```bash
./stuff/bootstrap-environment.py --purge
```
Restores database to initial state and populates with test data.

**Location:** Inside Docker container

### Apply Database Migrations
```bash
./stuff/db-migrate.py migrate --databases=omegaup,omegaup-test
```
Applies schema changes from new migration files.

**Location:** Inside Docker container

### Update schema.sql from Migrations
```bash
./stuff/update-dao.sh
```
Applies changes to `schema.sql` when adding new migration files.

**Location:** Inside Docker container

## PHP Type Validation

### Run Psalm on All PHP Files
```bash
find frontend/ \
    -name *.php \
    -and -not -wholename 'frontend/server/libs/third_party/*' \
    -and -not -wholename 'frontend/tests/badges/*' \
    -and -not -wholename 'frontend/tests/controllers/*' \
    -and -not -wholename 'frontend/tests/runfiles/*' \
    -and -not -wholename 'frontend/www/preguntas/*' \
  | xargs ./vendor/bin/psalm \
    --long-progress \
    --show-info=false
```
Runs type validation on PHP files using Psalm.

**Location:** Inside Docker container

## Docker

### Restart Docker Service
```bash
systemctl restart docker.service
```
Restarts Docker service. Useful for fixing container access errors.

**Location:** Outside Docker container (Linux)

### Access Container Console
```bash
docker exec -it omegaup-frontend-1 /bin/bash
```
Opens a bash shell inside the frontend container.

## Quick Reference

| Task | Command | Location |
|------|---------|----------|
| Lint code | `./stuff/lint.sh` | Outside container |
| Run PHP tests | `./stuff/runtests.sh` | Inside container |
| Run Cypress | `npx cypress open` | Outside container |
| Reset DB | `./stuff/bootstrap-environment.py --purge` | Inside container |
| Migrate DB | `./stuff/db-migrate.py migrate` | Inside container |
| Vue tests | `yarn run test:watch` | Inside container |

## Related Documentation

- **[Testing Guide](testing.md)** - Comprehensive testing documentation
- **[Coding Guidelines](coding-guidelines.md)** - Code standards
- **[Development Setup](../../getting-started/development-setup.md)** - Environment setup
