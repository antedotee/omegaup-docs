---
title: Solución de problemas
description: Problemas comunes y soluciones
icon: bootstrap/tools
---
# Solución de problemas

Problemas comunes y sus soluciones al trabajar con omegaUp, que cubren el entorno de desarrollo, problemas de compilación y problemas de producción.

## Entorno de desarrollo

### Problemas con Docker

#### Los contenedores no se inician

**Síntomas**: `docker-compose up` falla o los contenedores salen inmediatamente.

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
**Soluciones**:

1. **Reiniciar el servicio Docker**:
   ```bash
   # macOS
   killall Docker && open /Applications/Docker.app
   
   # Linux
   sudo systemctl restart docker
   ```
2. **Verificar conflictos de puertos**:
   ```bash
   # Find what's using port 8001
   lsof -i :8001
   
   # Kill conflicting process
   kill -9 <PID>
   ```
3. **Limpiar recursos de Docker**:
   ```bash
   # Remove stopped containers
   docker-compose down
   
   # Remove all resources (careful!)
   docker-compose down -v --rmi all
   ```
4. **Compruebe el espacio en disco**:
   ```bash
   docker system df
   docker system prune
   ```
#### Errores de conexión MySQL

**Síntomas**: Errores "No se puede conectar al servidor MySQL".

**Diagnóstico**:
```bash
# Check MySQL container is running
docker-compose ps mysql

# Check MySQL logs
docker-compose logs mysql | tail -50

# Test connection
docker-compose exec mysql mysql -u omegaup -p
```
**Soluciones**:

1. **Espere a que MySQL se inicialice**:
   ```bash
   # MySQL takes time on first run
   docker-compose logs mysql | grep "ready for connections"
   ```
2. **Verifique las variables de entorno**:
   ```bash
   docker-compose exec frontend printenv | grep MYSQL
   ```
3. **Restablecer datos de MySQL**:
   ```bash
   docker-compose down -v
   docker volume rm omegaup_mysql_data
   docker-compose up -d
   ```
#### La interfaz no se actualiza

**Síntomas**: los cambios de código no se reflejan en el navegador.

**Diagnóstico**:
```bash
# Check if webpack is running
docker-compose logs frontend | grep webpack

# Check file timestamps
ls -la frontend/www/js/dist/
```
**Soluciones**:

1. **Reiniciar el paquete web**:
   ```bash
   docker-compose exec frontend yarn run dev
   ```
2. **Borrar caché del navegador**:
   - Actualización completa: `Ctrl+Shift+R` (Windows/Linux) o `Cmd+Shift+R` (Mac)
   - Borrar todo: DevTools → Red → Desactivar caché

3. **Reconstruir interfaz**:
   ```bash
   docker-compose exec frontend yarn build
   ```
4. **Verificar permisos de archivos**:
   ```bash
   ls -la frontend/www/
   ```
### Problemas con el submódulo de Git

**Síntomas**: Faltan archivos o "fatal: no se encontró ninguna asignación de submódulo".

**Soluciones**:
```bash
# Initialize submodules
git submodule update --init --recursive

# Reset submodules
git submodule foreach git checkout .
git submodule update --init --recursive
```
---

## Problemas de compilación

### Fallos de pelusa

**Síntomas**: `./stuff/lint.sh` falla con errores de estilo.

**Diagnóstico**:
```bash
# Run linter with verbose output
./stuff/lint.sh

# Run specific linter
./stuff/lint.sh php
./stuff/lint.sh js
```
**Soluciones**:

1. **Problemas de solución automática**:
   ```bash
   # Fix PHP
   ./vendor/bin/php-cs-fixer fix
   
   # Fix JS/TS
   yarn run lint:fix
   ```
2. **Correcciones comunes de PHP**:
   ```php
   // Add missing type declarations
   public function myMethod(string $param): int
   
   // Use strict types
   declare(strict_types=1);
   ```
3. **Correcciones comunes de JS/TS**:
   ```typescript
   // Use const/let instead of var
   const x = 1;
   
   // Add explicit types
   function fn(x: number): string { }
   ```
### Fallos de prueba

**Síntomas**: Las pruebas de PHPUnit, Jest o Cypress fallan.

**Diagnóstico**:
```bash
# Run specific test
docker-compose exec frontend ./vendor/bin/phpunit tests/controllers/UserTest.php

# Run with verbose output
docker-compose exec frontend ./vendor/bin/phpunit -v
```
**Soluciones**:

1. **Restablecer base de datos de prueba**:
   ```bash
   docker-compose exec frontend php stuff/bootstrap-environment.php
   ```
2. **Revise los accesorios de prueba**:
   ```bash
   # Verify test data exists
   docker-compose exec mysql mysql -u omegaup -p omegaup -e "SELECT * FROM Users LIMIT 5"
   ```
3. **Ejecutar pruebas individualmente**:
   ```bash
   # Isolate failing test
   docker-compose exec frontend ./vendor/bin/phpunit --filter testSpecificMethod
   ```
### Errores de tipo de salmo

**Síntomas**: Errores de análisis estático del Salmo.

**Soluciones**:

1. **Actualizar anotaciones de tipo**:
   ```php
   /**
    * @param array<string, mixed> $params
    * @return array{success: bool, data: mixed}
    */
   ```
2. **Verifique la línea de base**:
   ```bash
   # Update psalm baseline
   ./vendor/bin/psalm --update-baseline
   ```
---

## Problemas de producción

### Trabajo pendiente en la cola de calificadores

**Síntomas**: Envíos atascados en la cola, tiempos de espera prolongados.

**Diagnóstico**:
```bash
# Check queue length
curl http://grader:36663/grader/status/

# Check runner availability
curl http://grader:36663/grader/runners/
```
**Soluciones**:

1. **Corredores de escala**:
   ```bash
   docker-compose up -d --scale runner=4
   ```
2. **Comprueba la salud del corredor**:
   ```bash
   docker-compose logs runner | grep -i error
   ```
3. **Eliminar envíos atascados**:
   ```sql
   UPDATE Runs SET status = 'new' WHERE status = 'running' AND time < NOW() - INTERVAL 1 HOUR;
   ```
### Rendimiento de la base de datos

**Síntomas**: cargas de página lentas, errores de tiempo de espera.

**Diagnóstico**:
```bash
# Check slow queries
docker-compose exec mysql mysql -u root -p -e "SHOW PROCESSLIST"

# Check query performance
docker-compose exec mysql mysql -u root -p -e "SHOW STATUS LIKE 'Slow_queries'"
```
**Soluciones**:

1. **Identificar consultas lentas**:
   ```sql
   SET GLOBAL slow_query_log = 'ON';
   SET GLOBAL long_query_time = 1;
   ```
2. **Agregar índices faltantes**:
   ```sql
   EXPLAIN SELECT ... -- Check query plan
   CREATE INDEX idx_name ON Table(column);
   ```
3. **Optimizar tablas**:
   ```sql
   OPTIMIZE TABLE Runs;
   OPTIMIZE TABLE Submissions;
   ```
### Problemas de memoria

**Síntomas**: El OOM del contenedor se interrumpe, "Tamaño de memoria permitido agotado".

**Diagnóstico**:
```bash
# Check memory usage
docker stats

# Check PHP memory limit
docker-compose exec frontend php -i | grep memory_limit
```
**Soluciones**:

1. **Aumentar la memoria PHP**:
   ```php
   // php.ini
   memory_limit = 512M
   ```
2. **Aumentar los límites de contenedores**:
   ```yaml
   # docker-compose.yml
   services:
     frontend:
       deploy:
         resources:
           limits:
             memory: 2G
   ```
### Problemas de conexión de WebSocket

**Síntomas**: Las actualizaciones en tiempo real no funcionan, el marcador no se actualiza.

**Diagnóstico**:
```bash
# Check broadcaster logs
docker-compose logs broadcaster

# Test WebSocket connection
wscat -c ws://localhost:39613/events/
```
**Soluciones**:

1. **Comprueba que la emisora esté funcionando**:
   ```bash
   docker-compose ps broadcaster
   ```
2. **Verifique la configuración del proxy nginx**:
   ```nginx
   location ^~ /events/ {
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
   }
   ```
---

## Referencia de errores

### Mensajes de error comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `SQLSTATE[HY000] [2002]` | MySQL no se ejecuta | Iniciar contenedor MySQL |
| `CSRF token mismatch` | Sesión caducada | Borrar cookies, volver a iniciar sesión |
| `Permission denied` | Permisos de archivos | `chmod` o comprobar propiedad |
| `504 Gateway Timeout` | Tiempo de espera de PHP-FPM | Aumentar los tiempos de espera |
| `ENOMEM` | Sin memoria | Aumentar límites |

### Códigos de estado HTTP

| Código | Significado | Causa común |
|------|---------|--------------|
| 400 | Solicitud incorrecta | Parámetros no válidos |
| 401 | No autorizado | No iniciado sesión |
| 403 | Prohibido | Permisos insuficientes |
| 404 | No encontrado | URL incorrecta o recurso eliminado |
| 429 | Demasiadas solicitudes | Tarifa limitada |
| 500 | Error del servidor | Verifique los registros de la aplicación |
| 502 | Mala puerta de enlace | PHP-FPM no responde |
| 504 | Tiempo de espera de puerta de enlace | La solicitud tardó demasiado |

---

## Obtener más ayuda

Si estas soluciones no resuelven su problema:

1. **Buscar problemas existentes**: [Problemas de GitHub](https://github.com/omegaup/omegaup/issues)
2. **Preguntar en Discord**: [Únete a nuestro servidor](https://discord.gg/gMEMX7Mrwe)
3. **Verificar registros**: incluya siempre resultados de registro relevantes cuando solicite ayuda
4. **Crear un problema**: [Informar un error](https://github.com/omegaup/omegaup/issues/new)

## Documentación relacionada

- **[Configuración de desarrollo](../getting-started/development-setup.md)** - Configuración del entorno
- **[Obtener ayuda](../getting-started/getting-help.md)** - Dónde hacer preguntas
- **[Monitoreo](monitoring.md)** - Monitoreo del sistema
- **[Configuración de Docker](docker-setup.md)** - Configuración del contenedor
