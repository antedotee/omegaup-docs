---
title: Troubleshooting
description: Common issues and solutions
icon: bootstrap/tools
---

# Troubleshooting

Common issues and their solutions when working with omegaUp, covering development environment, build issues, and production problems.

## Development Environment

### Docker Issues

#### Containers Won't Start

**Symptoms**: `docker-compose up` fails or containers exit immediately.

**Diagnostics**:
```bash
# Check Docker is running
docker ps

# Check container status
docker-compose ps

# View container logs
docker-compose logs

# Check specific container
docker-compose logs frontend
```

**Solutions**:

1. **Restart Docker service**:
   ```bash
   # macOS
   killall Docker && open /Applications/Docker.app
   
   # Linux
   sudo systemctl restart docker
   ```

2. **Check port conflicts**:
   ```bash
   # Find what's using port 8001
   lsof -i :8001
   
   # Kill conflicting process
   kill -9 <PID>
   ```

3. **Clean Docker resources**:
   ```bash
   # Remove stopped containers
   docker-compose down
   
   # Remove all resources (careful!)
   docker-compose down -v --rmi all
   ```

4. **Check disk space**:
   ```bash
   docker system df
   docker system prune
   ```

#### MySQL Connection Errors

**Symptoms**: "Can't connect to MySQL server" errors.

**Diagnostics**:
```bash
# Check MySQL container is running
docker-compose ps mysql

# Check MySQL logs
docker-compose logs mysql | tail -50

# Test connection
docker-compose exec mysql mysql -u omegaup -p
```

**Solutions**:

1. **Wait for MySQL to initialize**:
   ```bash
   # MySQL takes time on first run
   docker-compose logs mysql | grep "ready for connections"
   ```

2. **Check environment variables**:
   ```bash
   docker-compose exec frontend printenv | grep MYSQL
   ```

3. **Reset MySQL data**:
   ```bash
   docker-compose down -v
   docker volume rm omegaup_mysql_data
   docker-compose up -d
   ```

#### Frontend Not Updating

**Symptoms**: Code changes not reflected in browser.

**Diagnostics**:
```bash
# Check if webpack is running
docker-compose logs frontend | grep webpack

# Check file timestamps
ls -la frontend/www/js/dist/
```

**Solutions**:

1. **Restart webpack**:
   ```bash
   docker-compose exec frontend yarn run dev
   ```

2. **Clear browser cache**:
   - Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
   - Clear all: DevTools → Network → Disable cache

3. **Rebuild frontend**:
   ```bash
   docker-compose exec frontend yarn build
   ```

4. **Check file permissions**:
   ```bash
   ls -la frontend/www/
   ```

### Git Submodule Issues

**Symptoms**: Missing files or "fatal: no submodule mapping found".

**Solutions**:
```bash
# Initialize submodules
git submodule update --init --recursive

# Reset submodules
git submodule foreach git checkout .
git submodule update --init --recursive
```

---

## Build Issues

### Linting Failures

**Symptoms**: `./stuff/lint.sh` fails with style errors.

**Diagnostics**:
```bash
# Run linter with verbose output
./stuff/lint.sh

# Run specific linter
./stuff/lint.sh php
./stuff/lint.sh js
```

**Solutions**:

1. **Auto-fix issues**:
   ```bash
   # Fix PHP
   ./vendor/bin/php-cs-fixer fix
   
   # Fix JS/TS
   yarn run lint:fix
   ```

2. **Common PHP fixes**:
   ```php
   // Add missing type declarations
   public function myMethod(string $param): int
   
   // Use strict types
   declare(strict_types=1);
   ```

3. **Common JS/TS fixes**:
   ```typescript
   // Use const/let instead of var
   const x = 1;
   
   // Add explicit types
   function fn(x: number): string { }
   ```

### Test Failures

**Symptoms**: PHPUnit, Jest, or Cypress tests fail.

**Diagnostics**:
```bash
# Run specific test
docker-compose exec frontend ./vendor/bin/phpunit tests/controllers/UserTest.php

# Run with verbose output
docker-compose exec frontend ./vendor/bin/phpunit -v
```

**Solutions**:

1. **Reset test database**:
   ```bash
   docker-compose exec frontend php stuff/bootstrap-environment.php
   ```

2. **Check test fixtures**:
   ```bash
   # Verify test data exists
   docker-compose exec mysql mysql -u omegaup -p omegaup -e "SELECT * FROM Users LIMIT 5"
   ```

3. **Run tests individually**:
   ```bash
   # Isolate failing test
   docker-compose exec frontend ./vendor/bin/phpunit --filter testSpecificMethod
   ```

### Psalm Type Errors

**Symptoms**: Static analysis errors from Psalm.

**Solutions**:

1. **Update type annotations**:
   ```php
   /**
    * @param array<string, mixed> $params
    * @return array{success: bool, data: mixed}
    */
   ```

2. **Check baseline**:
   ```bash
   # Update psalm baseline
   ./vendor/bin/psalm --update-baseline
   ```

---

## Production Issues

### Grader Queue Backlog

**Symptoms**: Submissions stuck in queue, long wait times.

**Diagnostics**:
```bash
# Check queue length
curl http://grader:36663/grader/status/

# Check runner availability
curl http://grader:36663/grader/runners/
```

**Solutions**:

1. **Scale runners**:
   ```bash
   docker-compose up -d --scale runner=4
   ```

2. **Check runner health**:
   ```bash
   docker-compose logs runner | grep -i error
   ```

3. **Clear stuck submissions**:
   ```sql
   UPDATE Runs SET status = 'new' WHERE status = 'running' AND time < NOW() - INTERVAL 1 HOUR;
   ```

### Database Performance

**Symptoms**: Slow page loads, timeout errors.

**Diagnostics**:
```bash
# Check slow queries
docker-compose exec mysql mysql -u root -p -e "SHOW PROCESSLIST"

# Check query performance
docker-compose exec mysql mysql -u root -p -e "SHOW STATUS LIKE 'Slow_queries'"
```

**Solutions**:

1. **Identify slow queries**:
   ```sql
   SET GLOBAL slow_query_log = 'ON';
   SET GLOBAL long_query_time = 1;
   ```

2. **Add missing indexes**:
   ```sql
   EXPLAIN SELECT ... -- Check query plan
   CREATE INDEX idx_name ON Table(column);
   ```

3. **Optimize tables**:
   ```sql
   OPTIMIZE TABLE Runs;
   OPTIMIZE TABLE Submissions;
   ```

### Memory Issues

**Symptoms**: Container OOM kills, "Allowed memory size exhausted".

**Diagnostics**:
```bash
# Check memory usage
docker stats

# Check PHP memory limit
docker-compose exec frontend php -i | grep memory_limit
```

**Solutions**:

1. **Increase PHP memory**:
   ```php
   // php.ini
   memory_limit = 512M
   ```

2. **Increase container limits**:
   ```yaml
   # docker-compose.yml
   services:
     frontend:
       deploy:
         resources:
           limits:
             memory: 2G
   ```

### WebSocket Connection Issues

**Symptoms**: Real-time updates not working, scoreboard not updating.

**Diagnostics**:
```bash
# Check broadcaster logs
docker-compose logs broadcaster

# Test WebSocket connection
wscat -c ws://localhost:39613/events/
```

**Solutions**:

1. **Check broadcaster is running**:
   ```bash
   docker-compose ps broadcaster
   ```

2. **Verify nginx proxy config**:
   ```nginx
   location ^~ /events/ {
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
   }
   ```

---

## Error Reference

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `SQLSTATE[HY000] [2002]` | MySQL not running | Start MySQL container |
| `CSRF token mismatch` | Session expired | Clear cookies, re-login |
| `Permission denied` | File permissions | `chmod` or check ownership |
| `504 Gateway Timeout` | PHP-FPM timeout | Increase timeouts |
| `ENOMEM` | Out of memory | Increase limits |

### HTTP Status Codes

| Code | Meaning | Common Cause |
|------|---------|--------------|
| 400 | Bad Request | Invalid parameters |
| 401 | Unauthorized | Not logged in |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Wrong URL or deleted resource |
| 429 | Too Many Requests | Rate limited |
| 500 | Server Error | Check application logs |
| 502 | Bad Gateway | PHP-FPM not responding |
| 504 | Gateway Timeout | Request took too long |

---

## Getting More Help

If these solutions don't resolve your issue:

1. **Search existing issues**: [GitHub Issues](https://github.com/omegaup/omegaup/issues)
2. **Ask on Discord**: [Join our server](https://discord.gg/gMEMX7Mrwe)
3. **Check logs**: Always include relevant log output when asking for help
4. **Create an issue**: [Report a bug](https://github.com/omegaup/omegaup/issues/new)

## Related Documentation

- **[Development Setup](../getting-started/development-setup.md)** - Environment setup
- **[Getting Help](../getting-started/getting-help.md)** - Where to ask questions
- **[Monitoring](monitoring.md)** - System monitoring
- **[Docker Setup](docker-setup.md)** - Container configuration
