---
title: Componentes de infraestructura
description: Redis, RabbitMQ y arquitectura de comunicación de servicios
icon: bootstrap/server
---
# Componentes de infraestructura

Esta página documenta los componentes de infraestructura de soporte que habilitan la arquitectura distribuida de omegaUp: Redis para almacenamiento en caché y sesiones, RabbitMQ para colas de mensajes y patrones de comunicación entre servicios.

## Descripción general del sistema

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
##Redis

Redis sirve como capa de almacenamiento en caché y almacén de sesiones para omegaUp.

### Casos de uso

| Caso de uso | Patrón clave | TTL |
|----------|-------------|-----|
| Datos de la sesión | `session:{token}` | 24h |
| Declaraciones de problemas | `problem:{alias}:statement:{lang}` | 1 hora |
| Caché del marcador | `scoreboard:{contest}` | 30 años |
| Limitación de velocidad | `ratelimit:{ip}:{endpoint}` | 1min |
| Clasificaciones escolares | `school_rank:{page}` | 1 hora |
| Caché de etiquetas | `tags:{prefix}` | 1 hora |

### Almacenamiento de sesiones

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
### Patrón de almacenamiento en caché

```php
// Get from cache or compute
$result = \OmegaUp\Cache::getFromCacheOrSet(
    \OmegaUp\Cache::SCHOOL_RANK,
    "{$page}-{$length}",
    fn () => \OmegaUp\DAO\Schools::getRank($page, $length),
    3600 // TTL in seconds
);
```
### Invalidación de caché

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
### Configuración

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
## ConejoMQ

RabbitMQ maneja el procesamiento de tareas asíncrono y la mensajería entre servicios.

### Colas

| Cola | Propósito | Consumidor |
|-------|---------|----------|
| `ContestQueue` | Generación de certificados | Trabajador certificado |
| `SubmissionQueue` | Procesamiento de envío asíncrono | Calificador |
| `NotificationQueue` | Notificaciones por correo electrónico | Trabajador de notificaciones |
| `AnalyticsQueue` | Análisis de uso | Trabajador de análisis |

### Flujo de generación de certificados

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
### Formato del mensaje

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
### Publicación de mensajes

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
### Configuración

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
### Interfaz de usuario de administración

Acceso en `http://localhost:15672`:

- Supervisar la longitud de las colas
- Ver tarifas de mensajes
- Gestionar intercambios y vinculaciones.
- Purgar colas para depurar

## Comunicación de servicio

### HTTPS interno

Los servicios se comunican vía HTTPS con certificados de cliente:

```mermaid
flowchart LR
    PHP[PHP] -->|Client Cert| Grader
    Grader -->|Client Cert| GitServer
    Grader -->|Client Cert| Broadcaster
```
### Configuración del certificado

```bash
# Generate CA
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 365 -key ca.key -out ca.crt

# Generate service certificates
openssl genrsa -out grader.key 2048
openssl req -new -key grader.key -out grader.csr
openssl x509 -req -in grader.csr -CA ca.crt -CAkey ca.key -out grader.crt
```
### Comunicación de PHP a Grader

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
### Descubrimiento de servicios

En Docker Compose, los servicios utilizan descubrimiento basado en DNS:

```yaml
services:
  frontend:
    environment:
      - GRADER_URL=https://grader:21680
      - GITSERVER_URL=http://gitserver:33861
      - BROADCASTER_URL=https://broadcaster:32672
```
## Controles de salud

### Puntos finales de estado del servicio

| Servicio | Punto final | Puerto |
|---------|----------|------|
| Interfaz | `/health/` | 80 |
| Calificador | `/health` | 21680 |
| Servidor Git | `/health` | 33861 |
| Locutor | `/health` | 32672 |
| MySQL | Comprobación TCP | 3306 |
| Redis | `PING` | 6379 |
| ConejoMQ | API HTTP | 15672 |

### Comprobaciones de estado de Docker Compose

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
## Monitoreo

### Métricas de Prometeo

Cada servicio expone métricas:

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
### Paneles de control de Grafana

Paneles de control clave:

1. **Descripción general del sistema**: tasas de solicitudes, tasas de error, latencias
2. **Panel de calificación**: longitud de las colas, utilización de los corredores
3. **Panel de caché**: tasas de aciertos, uso de memoria
4. **Panel de cola**: tasas de mensajes, retraso del consumidor

## Conmutación por error y recuperación

### Conmutación por error de Redis

Para producción, utilice Redis Sentinel:

```yaml
redis-sentinel:
  image: redis:7-alpine
  command: redis-sentinel /etc/redis/sentinel.conf
  volumes:
    - ./sentinel.conf:/etc/redis/sentinel.conf
```
### Agrupación en clústeres de RabbitMQ

Para alta disponibilidad:

```yaml
rabbitmq1:
  environment:
    - RABBITMQ_ERLANG_COOKIE=secret
    
rabbitmq2:
  environment:
    - RABBITMQ_ERLANG_COOKIE=secret
  command: rabbitmqctl join_cluster rabbit@rabbitmq1
```
### Replicación de bases de datos

Replicación de MySQL para escalado de lectura:

```yaml
mysql-primary:
  environment:
    - MYSQL_REPLICATION_MODE=master
    
mysql-replica:
  environment:
    - MYSQL_REPLICATION_MODE=slave
    - MYSQL_MASTER_HOST=mysql-primary
```
## Ajuste de rendimiento

### Optimización de Redis

```conf
# redis.conf
maxmemory 2gb
maxmemory-policy allkeys-lru
tcp-keepalive 300
```
### Optimización de RabbitMQ

```conf
# rabbitmq.conf
vm_memory_high_watermark.relative = 0.6
disk_free_limit.absolute = 2GB
channel_max = 2000
```
### Agrupación de conexiones

PHP usa conexiones persistentes:

```php
// Redis connection pool
$redis = new \Redis();
$redis->pconnect(REDIS_HOST, REDIS_PORT);

// RabbitMQ connection reuse
$connection = \OmegaUp\RabbitMQConnection::getInstance();
```
## Documentación relacionada

- **[Configuración de Docker](../operations/docker-setup.md)** - Configuración completa de Docker
- **[Implementación](../operations/deployment.md)** - Implementación de producción
- **[Monitoreo](../operations/monitoring.md)** - Configuración de monitoreo
- **[Seguridad](security.md)** - Arquitectura de seguridad
