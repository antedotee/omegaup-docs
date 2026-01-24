---
title: Infrastructure Components
description: Redis, RabbitMQ, and service communication architecture
icon: bootstrap/server
---

# Infrastructure Components

This page documents the supporting infrastructure components that enable omegaUp's distributed architecture: Redis for caching and sessions, RabbitMQ for message queuing, and inter-service communication patterns.

## System Overview

```mermaid
flowchart TB
    subgraph Frontend
        Nginx[Nginx]
        PHP[PHP-FPM]
    end
    
    subgraph Backend Services
        Grader[Grader]
        Runner[Runners]
        GitServer[GitServer]
        Broadcaster[Broadcaster]
    end
    
    subgraph Infrastructure
        MySQL[(MySQL)]
        Redis[(Redis)]
        RabbitMQ[RabbitMQ]
    end
    
    Nginx --> PHP
    PHP --> MySQL
    PHP --> Redis
    PHP --> RabbitMQ
    PHP -->|HTTPS| Grader
    
    Grader --> MySQL
    Grader --> GitServer
    Grader --> Runner
    Grader --> Broadcaster
    
    Broadcaster --> Redis
```

## Redis

Redis serves as the caching layer and session store for omegaUp.

### Use Cases

| Use Case | Key Pattern | TTL |
|----------|-------------|-----|
| Session data | `session:{token}` | 24h |
| Problem statements | `problem:{alias}:statement:{lang}` | 1h |
| Scoreboard cache | `scoreboard:{contest}` | 30s |
| Rate limiting | `ratelimit:{ip}:{endpoint}` | 1min |
| School rankings | `school_rank:{page}` | 1h |
| Tags cache | `tags:{prefix}` | 1h |

### Session Storage

```php
// Session key format
$key = "session:{$authToken}";

// Session data structure
{
  "identity_id": 12345,
  "user_id": 67890,
  "login_time": 1704067200,
  "ip_address": "192.168.1.1"
}
```

### Caching Pattern

```php
// Get from cache or compute
$result = \OmegaUp\Cache::getFromCacheOrSet(
    \OmegaUp\Cache::SCHOOL_RANK,
    "{$page}-{$length}",
    fn () => \OmegaUp\DAO\Schools::getRank($page, $length),
    3600 // TTL in seconds
);
```

### Cache Invalidation

```php
// Delete specific key
\OmegaUp\Cache::deleteFromCache(
    \OmegaUp\Cache::SESSION_PREFIX,
    $authToken
);

// Pattern-based invalidation
\OmegaUp\Cache::invalidateAllKeys(
    \OmegaUp\Cache::PROBLEM_STATEMENT,
    $problemAlias
);
```

### Configuration

```yaml
# docker-compose.yml
redis:
  image: redis:7-alpine
  ports:
    - "6379:6379"
  volumes:
    - redis_data:/data
  command: redis-server --appendonly yes
```

```php
// PHP configuration
define('REDIS_HOST', 'redis');
define('REDIS_PORT', 6379);
define('REDIS_PASS', '');
```

## RabbitMQ

RabbitMQ handles asynchronous task processing and inter-service messaging.

### Queues

| Queue | Purpose | Consumer |
|-------|---------|----------|
| `ContestQueue` | Certificate generation | Certificate Worker |
| `SubmissionQueue` | Async submission processing | Grader |
| `NotificationQueue` | Email notifications | Notification Worker |
| `AnalyticsQueue` | Usage analytics | Analytics Worker |

### Certificate Generation Flow

```mermaid
sequenceDiagram
    participant A as Admin
    participant P as PHP
    participant R as RabbitMQ
    participant W as Worker
    participant D as Database
    
    A->>P: Generate certificates
    P->>R: Publish to ContestQueue
    P-->>A: Queued
    
    R->>W: Consume message
    W->>W: Generate PDFs
    W->>D: Store certificates
    W->>R: Acknowledge
```

### Message Format

```json
{
  "type": "generate_certificates",
  "contest_id": 123,
  "certificate_cutoff": 10,
  "ranking": [
    {"username": "user1", "place": 1},
    {"username": "user2", "place": 2}
  ],
  "timestamp": 1704067200
}
```

### Publishing Messages

```php
// Get RabbitMQ channel
$channel = \OmegaUp\RabbitMQConnection::getInstance()->channel();

// Prepare message
$message = new \PhpAmqpLib\Message\AMQPMessage(
    json_encode($data),
    ['delivery_mode' => 2] // Persistent
);

// Publish to exchange
$channel->basic_publish(
    $message,
    'certificates',  // Exchange
    'ContestQueue'   // Routing key
);
```

### Configuration

```yaml
# docker-compose.yml
rabbitmq:
  image: rabbitmq:3-management
  ports:
    - "5672:5672"   # AMQP
    - "15672:15672" # Management UI
  environment:
    RABBITMQ_DEFAULT_USER: omegaup
    RABBITMQ_DEFAULT_PASS: omegaup
  volumes:
    - rabbitmq_data:/var/lib/rabbitmq
```

### Management UI

Access at `http://localhost:15672`:

- Monitor queue lengths
- View message rates
- Manage exchanges and bindings
- Purge queues for debugging

## Service Communication

### Internal HTTPS

Services communicate via HTTPS with client certificates:

```mermaid
flowchart LR
    PHP[PHP] -->|Client Cert| Grader
    Grader -->|Client Cert| GitServer
    Grader -->|Client Cert| Broadcaster
```

### Certificate Setup

```bash
# Generate CA
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 365 -key ca.key -out ca.crt

# Generate service certificates
openssl genrsa -out grader.key 2048
openssl req -new -key grader.key -out grader.csr
openssl x509 -req -in grader.csr -CA ca.crt -CAkey ca.key -out grader.crt
```

### PHP to Grader Communication

```php
class Grader {
    private function call(string $endpoint, array $data): array {
        $curl = curl_init();
        curl_setopt_array($curl, [
            CURLOPT_URL => "https://grader:21680{$endpoint}",
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode($data),
            CURLOPT_SSLCERT => '/etc/omegaup/ssl/frontend.crt',
            CURLOPT_SSLKEY => '/etc/omegaup/ssl/frontend.key',
            CURLOPT_CAINFO => '/etc/omegaup/ssl/ca.crt',
        ]);
        
        $response = curl_exec($curl);
        return json_decode($response, true);
    }
}
```

### Service Discovery

In Docker Compose, services use DNS-based discovery:

```yaml
services:
  frontend:
    environment:
      - GRADER_URL=https://grader:21680
      - GITSERVER_URL=http://gitserver:33861
      - BROADCASTER_URL=https://broadcaster:32672
```

## Health Checks

### Service Health Endpoints

| Service | Endpoint | Port |
|---------|----------|------|
| Frontend | `/health/` | 80 |
| Grader | `/health` | 21680 |
| GitServer | `/health` | 33861 |
| Broadcaster | `/health` | 32672 |
| MySQL | TCP check | 3306 |
| Redis | `PING` | 6379 |
| RabbitMQ | HTTP API | 15672 |

### Docker Compose Health Checks

```yaml
services:
  mysql:
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 3
      
  redis:
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
      
  rabbitmq:
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "check_running"]
      interval: 30s
      timeout: 10s
      retries: 3
```

## Monitoring

### Prometheus Metrics

Each service exposes metrics:

```
# Grader metrics
grader_queue_length{queue="contest"} 5
grader_submissions_total 150000
grader_runners_available 3

# Redis metrics
redis_connected_clients 15
redis_used_memory_bytes 104857600

# RabbitMQ metrics
rabbitmq_queue_messages{queue="ContestQueue"} 10
```

### Grafana Dashboards

Key dashboards:

1. **System Overview**: Request rates, error rates, latencies
2. **Grader Dashboard**: Queue lengths, runner utilization
3. **Cache Dashboard**: Hit rates, memory usage
4. **Queue Dashboard**: Message rates, consumer lag

## Failover & Recovery

### Redis Failover

For production, use Redis Sentinel:

```yaml
redis-sentinel:
  image: redis:7-alpine
  command: redis-sentinel /etc/redis/sentinel.conf
  volumes:
    - ./sentinel.conf:/etc/redis/sentinel.conf
```

### RabbitMQ Clustering

For high availability:

```yaml
rabbitmq1:
  environment:
    - RABBITMQ_ERLANG_COOKIE=secret
    
rabbitmq2:
  environment:
    - RABBITMQ_ERLANG_COOKIE=secret
  command: rabbitmqctl join_cluster rabbit@rabbitmq1
```

### Database Replication

MySQL replication for read scaling:

```yaml
mysql-primary:
  environment:
    - MYSQL_REPLICATION_MODE=master
    
mysql-replica:
  environment:
    - MYSQL_REPLICATION_MODE=slave
    - MYSQL_MASTER_HOST=mysql-primary
```

## Performance Tuning

### Redis Optimization

```conf
# redis.conf
maxmemory 2gb
maxmemory-policy allkeys-lru
tcp-keepalive 300
```

### RabbitMQ Optimization

```conf
# rabbitmq.conf
vm_memory_high_watermark.relative = 0.6
disk_free_limit.absolute = 2GB
channel_max = 2000
```

### Connection Pooling

PHP uses persistent connections:

```php
// Redis connection pool
$redis = new \Redis();
$redis->pconnect(REDIS_HOST, REDIS_PORT);

// RabbitMQ connection reuse
$connection = \OmegaUp\RabbitMQConnection::getInstance();
```

## Related Documentation

- **[Docker Setup](../operations/docker-setup.md)** - Complete Docker configuration
- **[Deployment](../operations/deployment.md)** - Production deployment
- **[Monitoring](../operations/monitoring.md)** - Monitoring setup
- **[Security](security.md)** - Security architecture
