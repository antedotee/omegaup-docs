---
title: Troubleshooting
description: Common issues and solutions
---

# Troubleshooting

Common issues and their solutions when working with omegaUp.

## Development Environment

### Docker Issues

**Problem**: Containers won't start

**Solutions**:
- Check Docker is running: `docker ps`
- Restart Docker service
- Check port conflicts: `lsof -i :8001`
- Review Docker logs: `docker-compose logs`

### Database Connection Errors

**Problem**: MySQL connection failures

**Solutions**:
- Verify MySQL is running in container
- Check connection configuration
- Review database migration status

### Frontend Not Updating

**Problem**: Changes not visible in browser

**Solutions**:
- Restart Docker containers
- Clear browser cache
- Check webpack build output
- Verify file changes are saved

## Build Issues

### Linting Failures

**Problem**: `./stuff/lint.sh` fails

**Solutions**:
- Run `./stuff/lint.sh` to auto-fix issues
- Check specific linter output
- Review coding guidelines

### Test Failures

**Problem**: Tests failing locally

**Solutions**:
- Ensure database is properly set up
- Check test data fixtures
- Review test output for specific errors
- Run tests individually to isolate issues

## Related Documentation

- **[Development Setup](../../getting-started/development-setup.md)** - Environment setup
- **[Getting Help](../../getting-started/getting-help.md)** - Where to ask questions
