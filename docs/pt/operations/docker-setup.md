---
title: Configuração do Docker
description: Configuração detalhada do Docker Compose para desenvolvimento local
icon: bootstrap/tools
---
#Configuração do Docker

Este guia aborda a configuração do Docker Compose para executar omegaUp localmente, incluindo todos os serviços, rede e solução de problemas comuns.

## Pré-requisitos

- Motor Docker 20.10+
- Docker Compor 2.0+
- 8 GB + RAM recomendado
- 20 GB + espaço em disco

## Início rápido

```bash
# Clone the repository
git clone https://github.com/omegaup/omegaup.git
cd omegaup

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Access at http://localhost:8001
```
## Visão geral da arquitetura

```mermaid
flowchart TB
    subgraph "Docker Network: omegaup"
        Nginx[nginx:80,443] --> PHP[php:9000]
        PHP --> MySQL[(mysql:3306)]
        PHP --> Redis[(redis:6379)]
        PHP --> RabbitMQ[rabbitmq:5672]
        PHP -->|HTTPS| Grader[grader:21680]
        
        Grader --> MySQL
        Grader --> GitServer[gitserver:33861]
        Grader --> Broadcaster[broadcaster:32672]
        Grader --> Runner1[runner:1]
        Grader --> Runner2[runner:2]
        
        Broadcaster --> Redis
    end
    
    Browser[Browser] --> Nginx
```
## Configuração de serviço

### Front-end (Nginx + PHP-FPM)

```yaml
services:
  frontend:
    image: omegaup/frontend
    ports:
      - "8001:80"
      - "8443:443"
    volumes:
      - ./frontend:/opt/omegaup
      - ./stuff/docker/etc/omegaup:/etc/omegaup:ro
    depends_on:
      mysql:
        condition: service_healthy
      redis:
        condition: service_started
    environment:
      - OMEGAUP_DB_HOST=mysql
      - OMEGAUP_DB_NAME=omegaup
      - OMEGAUP_DB_USER=omegaup
      - OMEGAUP_DB_PASS=omegaup
```
### Banco de dados MySQL

```yaml
services:
  mysql:
    image: mysql:8.0
    ports:
      - "13306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./stuff/docker/mysql/init:/docker-entrypoint-initdb.d:ro
    environment:
      - MYSQL_ROOT_PASSWORD=omegaup
      - MYSQL_DATABASE=omegaup
      - MYSQL_USER=omegaup
      - MYSQL_PASSWORD=omegaup
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
    command: >
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_unicode_ci
```
### Cache Redis

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
```
### CoelhoMQ

```yaml
services:
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"    # AMQP
      - "15672:15672"  # Management UI
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
    environment:
      - RABBITMQ_DEFAULT_USER=omegaup
      - RABBITMQ_DEFAULT_PASS=omegaup
```
### Graduador

```yaml
services:
  grader:
    image: omegaup/backend
    ports:
      - "21680:21680"  # HTTPS API
      - "6060:6060"    # Metrics
    volumes:
      - ./stuff/docker/etc/omegaup/grader:/etc/omegaup/grader:ro
      - grader_data:/var/lib/omegaup
    depends_on:
      - mysql
      - gitserver
    entrypoint: >
      wait-for-it mysql:3306 -- 
      /usr/bin/omegaup-grader
```
###GitServer

```yaml
services:
  gitserver:
    image: omegaup/gitserver
    ports:
      - "33861:33861"  # HTTP API
      - "33862:33862"  # Git protocol
    volumes:
      - problems_data:/var/lib/omegaup/problems
      - ./stuff/docker/etc/omegaup/gitserver:/etc/omegaup/gitserver:ro
```
### Emissora

```yaml
services:
  broadcaster:
    image: omegaup/backend
    ports:
      - "32672:32672"  # Internal API
      - "39613:39613"  # WebSocket
    depends_on:
      - redis
    entrypoint: /usr/bin/omegaup-broadcaster
```
### Corredores

```yaml
services:
  runner:
    image: omegaup/runner
    deploy:
      replicas: 2
    volumes:
      - runner_data:/var/lib/omegaup/runner
    cap_add:
      - SYS_PTRACE
    security_opt:
      - seccomp:unconfined
    depends_on:
      - grader
```
## Volumes

```yaml
volumes:
  mysql_data:
    driver: local
  redis_data:
    driver: local
  rabbitmq_data:
    driver: local
  grader_data:
    driver: local
  problems_data:
    driver: local
  runner_data:
    driver: local
```
## Redes

```yaml
networks:
  default:
    name: omegaup
    driver: bridge
```
## Variáveis de ambiente

### Variáveis de front-end

| Variável | Padrão | Descrição |
|----------|------------|-------------|
| `OMEGAUP_DB_HOST` | `mysql` | Nome de host MySQL |
| `OMEGAUP_DB_NAME` | `omegaup` | Nome do banco de dados |
| `OMEGAUP_DB_USER` | `omegaup` | Usuário do banco de dados |
| `OMEGAUP_DB_PASS` | `omegaup` | Senha do banco de dados |
| `OMEGAUP_GRADER_URL` | `https://grader:21680` | URL do avaliador |
| `OMEGAUP_GITSERVER_URL` | `http://gitserver:33861` | URL do servidor Git |

### Variáveis da niveladora

| Variável | Padrão | Descrição |
|----------|------------|-------------|
| `OMEGAUP_DB_HOST` | `mysql` | Nome de host MySQL |
| `OMEGAUP_BROADCASTER_URL` | `https://broadcaster:32672` | URL da emissora |
| `OMEGAUP_GITSERVER_URL` | `http://gitserver:33861` | URL do servidor Git |

## Comandos Comuns

### Iniciar serviços

```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d frontend

# Rebuild and start
docker-compose up -d --build
```
### Ver registros

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f grader

# Last 100 lines
docker-compose logs --tail 100 frontend
```
### Gerenciamento de serviços

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Restart specific service
docker-compose restart frontend

# Scale runners
docker-compose up -d --scale runner=4
```
### Operações de banco de dados

```bash
# Connect to MySQL
docker-compose exec mysql mysql -u omegaup -p omegaup

# Import database
docker-compose exec -T mysql mysql -u omegaup -p omegaup < backup.sql

# Run migrations
docker-compose exec frontend php /opt/omegaup/stuff/database/migrate.php
```
### Depuração

```bash
# Shell into container
docker-compose exec frontend bash

# Check container status
docker-compose ps

# Inspect container
docker inspect omegaup_frontend_1
```
## Arquivos de configuração

### Estrutura de diretório

```
stuff/docker/
├── etc/
│   └── omegaup/
│       ├── frontend/
│       │   └── config.php
│       ├── grader/
│       │   └── config.json
│       ├── gitserver/
│       │   └── config.json
│       └── ssl/
│           ├── ca.crt
│           ├── frontend.crt
│           └── frontend.key
├── mysql/
│   └── init/
│       └── 00-init.sql
└── nginx/
    └── default.conf
```
### Configuração de front-end

```php
// stuff/docker/etc/omegaup/frontend/config.php
<?php
define('OMEGAUP_DB_HOST', 'mysql');
define('OMEGAUP_DB_NAME', 'omegaup');
define('OMEGAUP_DB_USER', 'omegaup');
define('OMEGAUP_DB_PASS', 'omegaup');

define('OMEGAUP_GRADER_URL', 'https://grader:21680/');
define('OMEGAUP_GITSERVER_URL', 'http://gitserver:33861/');

define('REDIS_HOST', 'redis');
define('REDIS_PORT', 6379);
```
## Verificações de integridade

### Verifique todos os serviços

```bash
#!/bin/bash

# Frontend
curl -sf http://localhost:8001/health/ && echo "Frontend: OK" || echo "Frontend: FAIL"

# MySQL
docker-compose exec mysql mysqladmin ping -h localhost && echo "MySQL: OK" || echo "MySQL: FAIL"

# Redis
docker-compose exec redis redis-cli ping && echo "Redis: OK" || echo "Redis: FAIL"

# Grader (internal)
docker-compose exec frontend curl -sf https://grader:21680/health && echo "Grader: OK" || echo "Grader: FAIL"
```
## Solução de problemas

### Problemas comuns

#### Conexão MySQL recusada

```bash
# Check if MySQL is ready
docker-compose logs mysql | grep "ready for connections"

# Restart MySQL
docker-compose restart mysql
```
#### O aluno não está respondendo

```bash
# Check grader logs
docker-compose logs grader

# Verify certificates
docker-compose exec grader ls -la /etc/omegaup/ssl/
```
#### Erros de sandbox do corredor

```bash
# Check seccomp is disabled
docker-compose exec runner cat /proc/sys/kernel/seccomp/actions_logged

# Verify capabilities
docker-compose exec runner capsh --print
```
#### Desempenho lento

```bash
# Increase Docker resources (Docker Desktop)
# Memory: 8GB+, CPUs: 4+

# Check resource usage
docker stats
```
### Redefinir ambiente

```bash
# Stop everything
docker-compose down -v

# Remove all containers
docker-compose rm -f

# Remove images
docker-compose down --rmi all

# Fresh start
docker-compose up -d --build
```
## Considerações sobre produção

Para implantação de produção, consulte:

- **[Guia de implantação](deployment.md)** - Instruções completas de implantação
- **[Segurança](../architecture/security.md)** - Configuração de segurança
- **[Monitoramento](monitoring.md)** - Configuração de monitoramento

## Documentação Relacionada

- **[Infraestrutura](../architecture/infrastructure.md)** - Arquitetura de serviço
- **[Configuração de desenvolvimento](../getting-started/development-setup.md)** - Ambiente de desenvolvimento
- **[Comandos úteis](../development/useful-commands.md)** - Mais comandos
