---
title: Solução de problemas
description: Problemas e soluções comuns
icon: bootstrap/tools
---
# Solução de problemas

Problemas comuns e suas soluções ao trabalhar com omegaUp, abrangendo ambiente de desenvolvimento, problemas de construção e problemas de produção.

## Ambiente de Desenvolvimento

### Problemas do Docker

#### Os contêineres não iniciam

**Sintomas**: `docker-compose up` falha ou os contêineres são encerrados imediatamente.

**Diagnóstico**:
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
**Soluções**:

1. **Reinicie o serviço Docker**:
   ```bash
   # macOS
   killall Docker && open /Applications/Docker.app
   
   # Linux
   sudo systemctl restart docker
   ```
2. **Verifique conflitos de porta**:
   ```bash
   # Find what's using port 8001
   lsof -i :8001
   
   # Kill conflicting process
   kill -9 <PID>
   ```
3. **Limpar recursos do Docker**:
   ```bash
   # Remove stopped containers
   docker-compose down
   
   # Remove all resources (careful!)
   docker-compose down -v --rmi all
   ```
4. **Verifique o espaço em disco**:
   ```bash
   docker system df
   docker system prune
   ```
#### Erros de conexão do MySQL

**Sintomas**: Erros "Não é possível conectar ao servidor MySQL".

**Diagnóstico**:
```bash
# Check MySQL container is running
docker-compose ps mysql

# Check MySQL logs
docker-compose logs mysql | tail -50

# Test connection
docker-compose exec mysql mysql -u omegaup -p
```
**Soluções**:

1. **Aguarde a inicialização do MySQL**:
   ```bash
   # MySQL takes time on first run
   docker-compose logs mysql | grep "ready for connections"
   ```
2. **Verifique as variáveis ​​de ambiente**:
   ```bash
   docker-compose exec frontend printenv | grep MYSQL
   ```
3. **Redefinir dados MySQL**:
   ```bash
   docker-compose down -v
   docker volume rm omegaup_mysql_data
   docker-compose up -d
   ```
#### Frontend não atualiza

**Sintomas**: alterações de código não refletidas no navegador.

**Diagnóstico**:
```bash
# Check if webpack is running
docker-compose logs frontend | grep webpack

# Check file timestamps
ls -la frontend/www/js/dist/
```
**Soluções**:

1. **Reinicie o webpack**:
   ```bash
   docker-compose exec frontend yarn run dev
   ```
2. **Limpar cache do navegador**:
   - Atualização total: `Ctrl+Shift+R` (Windows/Linux) ou `Cmd+Shift+R` (Mac)
   - Limpar tudo: DevTools → Rede → Desativar cache

3. **Reconstruir interface**:
   ```bash
   docker-compose exec frontend yarn build
   ```
4. **Verifique as permissões do arquivo**:
   ```bash
   ls -la frontend/www/
   ```
### Problemas do submódulo Git

**Sintomas**: Arquivos ausentes ou "fatal: nenhum mapeamento de submódulo encontrado".

**Soluções**:
```bash
# Initialize submodules
git submodule update --init --recursive

# Reset submodules
git submodule foreach git checkout .
git submodule update --init --recursive
```
---

## Problemas de compilação

### Falhas de linting

**Sintomas**: `./stuff/lint.sh` falha com erros de estilo.

**Diagnóstico**:
```bash
# Run linter with verbose output
./stuff/lint.sh

# Run specific linter
./stuff/lint.sh php
./stuff/lint.sh js
```
**Soluções**:

1. **Problemas de correção automática**:
   ```bash
   # Fix PHP
   ./vendor/bin/php-cs-fixer fix
   
   # Fix JS/TS
   yarn run lint:fix
   ```
2. **Correções comuns de PHP**:
   ```php
   // Add missing type declarations
   public function myMethod(string $param): int
   
   // Use strict types
   declare(strict_types=1);
   ```
3. **Correções comuns de JS/TS**:
   ```typescript
   // Use const/let instead of var
   const x = 1;
   
   // Add explicit types
   function fn(x: number): string { }
   ```
### Falhas no teste

**Sintomas**: Os testes PHPUnit, Jest ou Cypress falham.

**Diagnóstico**:
```bash
# Run specific test
docker-compose exec frontend ./vendor/bin/phpunit tests/controllers/UserTest.php

# Run with verbose output
docker-compose exec frontend ./vendor/bin/phpunit -v
```
**Soluções**:

1. **Redefinir banco de dados de teste**:
   ```bash
   docker-compose exec frontend php stuff/bootstrap-environment.php
   ```
2. **Verifique os acessórios de teste**:
   ```bash
   # Verify test data exists
   docker-compose exec mysql mysql -u omegaup -p omegaup -e "SELECT * FROM Users LIMIT 5"
   ```
3. **Execute testes individualmente**:
   ```bash
   # Isolate failing test
   docker-compose exec frontend ./vendor/bin/phpunit --filter testSpecificMethod
   ```
### Erros de tipo de salmo

**Sintomas**: Erros de análise estática do Salmo.

**Soluções**:

1. **Anotações de tipo de atualização**:
   ```php
   /**
    * @param array<string, mixed> $params
    * @return array{success: bool, data: mixed}
    */
   ```
2. **Verifique a linha de base**:
   ```bash
   # Update psalm baseline
   ./vendor/bin/psalm --update-baseline
   ```
---

## Problemas de produção

### Pendências da fila do avaliador

**Sintomas**: Envios presos na fila, longos tempos de espera.

**Diagnóstico**:
```bash
# Check queue length
curl http://grader:36663/grader/status/

# Check runner availability
curl http://grader:36663/grader/runners/
```
**Soluções**:

1. **Corredores de escala**:
   ```bash
   docker-compose up -d --scale runner=4
   ```
2. **Verifique a saúde do corredor**:
   ```bash
   docker-compose logs runner | grep -i error
   ```
3. **Limpar envios travados**:
   ```sql
   UPDATE Runs SET status = 'new' WHERE status = 'running' AND time < NOW() - INTERVAL 1 HOUR;
   ```
### Desempenho do banco de dados

**Sintomas**: carregamento lento da página, erros de tempo limite.

**Diagnóstico**:
```bash
# Check slow queries
docker-compose exec mysql mysql -u root -p -e "SHOW PROCESSLIST"

# Check query performance
docker-compose exec mysql mysql -u root -p -e "SHOW STATUS LIKE 'Slow_queries'"
```
**Soluções**:

1. **Identifique consultas lentas**:
   ```sql
   SET GLOBAL slow_query_log = 'ON';
   SET GLOBAL long_query_time = 1;
   ```
2. **Adicione índices ausentes**:
   ```sql
   EXPLAIN SELECT ... -- Check query plan
   CREATE INDEX idx_name ON Table(column);
   ```
3. **Otimizar tabelas**:
   ```sql
   OPTIMIZE TABLE Runs;
   OPTIMIZE TABLE Submissions;
   ```
### Problemas de memória

**Sintomas**: O contêiner OOM é eliminado, "Tamanho de memória permitido esgotado".

**Diagnóstico**:
```bash
# Check memory usage
docker stats

# Check PHP memory limit
docker-compose exec frontend php -i | grep memory_limit
```
**Soluções**:

1. **Aumente a memória do PHP**:
   ```php
   // php.ini
   memory_limit = 512M
   ```
2. **Aumentar os limites dos contêineres**:
   ```yaml
   # docker-compose.yml
   services:
     frontend:
       deploy:
         resources:
           limits:
             memory: 2G
   ```
### Problemas de conexão WebSocket

**Sintomas**: Atualizações em tempo real não funcionam, placar não atualiza.

**Diagnóstico**:
```bash
# Check broadcaster logs
docker-compose logs broadcaster

# Test WebSocket connection
wscat -c ws://localhost:39613/events/
```
**Soluções**:

1. **Verifique se a emissora está funcionando**:
   ```bash
   docker-compose ps broadcaster
   ```
2. **Verifique a configuração do proxy nginx**:
   ```nginx
   location ^~ /events/ {
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
   }
   ```
---

## Referência de erro

### Mensagens de erro comuns

| Erro | Causa | Solução |
|-------|-------|----------|
| `SQLSTATE[HY000] [2002]` | MySQL não está funcionando | Inicie o contêiner MySQL |
| `CSRF token mismatch` | Sessão expirada | Limpar cookies, fazer login novamente |
| `Permission denied` | Permissões de arquivo | `chmod` ou verifique a propriedade |
| `504 Gateway Timeout` | Tempo limite do PHP-FPM | Aumentar os tempos limite |
| `ENOMEM` | Sem memória | Aumentar limites |

### Códigos de status HTTP

| Código | Significado | Causa Comum |
|------|---------|-------------|
| 400 | Solicitação incorreta | Parâmetros inválidos |
| 401 | Não autorizado | Não logado |
| 403 | Proibido | Permissões insuficientes |
| 404 | Não encontrado | URL errado ou recurso excluído |
| 429 | Muitas solicitações | Taxa limitada |
| 500 | Erro no servidor | Verifique os logs do aplicativo |
| 502 | Gateway ruim | PHP-FPM não responde |
| 504 | Tempo limite do gateway | A solicitação demorou muito |

---

## Obtendo mais ajuda

Se essas soluções não resolverem seu problema:

1. **Pesquisar problemas existentes**: [Problemas do GitHub](https://github.com/omegaup/omegaup/issues)
2. **Pergunte no Discord**: [Entre em nosso servidor](https://discord.gg/gMEMX7Mrwe)
3. **Verifique os registros**: sempre inclua saídas de registro relevantes ao pedir ajuda
4. **Crie um problema**: [Informar um bug](https://github.com/omegaup/omegaup/issues/new)

## Documentação Relacionada

- **[Configuração de desenvolvimento](../getting-started/development-setup.md)** - Configuração do ambiente
- **[Como obter ajuda](../getting-started/getting-help.md)** - Onde fazer perguntas
- **[Monitoramento](monitoring.md)** - Monitoramento do sistema
- **[Configuração do Docker](docker-setup.md)** - Configuração do contêiner
