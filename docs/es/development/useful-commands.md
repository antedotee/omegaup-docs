---
title: Comandos de desarrollo útiles
description: Comandos y atajos comunes para el desarrollo de omegaUp
icon: bootstrap/terminal
---
# Comandos de desarrollo útiles

Referencia rápida para comandos de desarrollo comunes en omegaUp.

## Linting y validación

### Ejecutar todos los Linters
```bash
./stuff/lint.sh
```
Ejecuta todas las validaciones de código. Se ejecuta automáticamente en `git push`.

**Ubicación:** Fuera del contenedor Docker, raíz del proyecto

### Validar solo estilo
```bash
./stuff/lint.sh validate
```
Valida el estilo del código sin solucionar problemas.

### Generar archivos i18n
```bash
./stuff/lint.sh --linters=i18n fix --all
```
Genera archivos `*.lang` basados ​​en `es.lang`, `en.lang` y `pt.lang`.

## Pruebas

### Ejecute todas las pruebas de PHP
```bash
./stuff/runtests.sh
```
Ejecuta pruebas PHPUnit, validación de tipo MySQL y Psalm.

**Ubicación:** Dentro del contenedor Docker

### Ejecutar archivo de prueba PHP específico
```bash
./stuff/run-php-tests.sh frontend/tests/controllers/$MY_FILE.php
```
Ejecuta pruebas unitarias para un único archivo PHP. Omita el nombre del archivo para ejecutar todas las pruebas.

### Ejecutar pruebas de Cypress
```bash
npx cypress open
```
Abre la GUI de Cypress Test Runner para realizar pruebas interactivas.

**Requisitos previos:**
- Node.js instalado
- NPM instalado
-libasound2 (Linux)

**Ubicación:** Contenedor Docker exterior

### Ejecutar pruebas unitarias de Vue (modo de vigilancia)
```bash
yarn run test:watch
```
Ejecuta pruebas de Vue en modo de vigilancia y se vuelve a ejecutar automáticamente cuando se realizan cambios de código.

### Ejecutar archivo de prueba de Vue específico
```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/$MY_FILE.test.ts
```
Ejecuta un único archivo de prueba de Vue.

## Base de datos

### Restablecer la base de datos al estado inicial
```bash
./stuff/bootstrap-environment.py --purge
```
Restaura la base de datos al estado inicial y la completa con datos de prueba.

**Ubicación:** Dentro del contenedor Docker

### Aplicar migraciones de bases de datos
```bash
./stuff/db-migrate.py migrate --databases=omegaup,omegaup-test
```
Aplica cambios de esquema de nuevos archivos de migración.

**Ubicación:** Dentro del contenedor Docker

### Actualizar esquema.sql desde Migraciones
```bash
./stuff/update-dao.sh
```
Aplica cambios a `schema.sql` al agregar nuevos archivos de migración.

**Ubicación:** Dentro del contenedor Docker

## Validación de tipo PHP

### Ejecute Psalm en todos los archivos PHP
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
Ejecuta validación de tipos en archivos PHP usando Psalm.

**Ubicación:** Dentro del contenedor Docker

## acoplador

### Reiniciar el servicio Docker
```bash
systemctl restart docker.service
```
Reinicia el servicio Docker. Útil para corregir errores de acceso a contenedores.

**Ubicación:** Contenedor Docker externo (Linux)

### Acceder a la consola del contenedor
```bash
docker exec -it omegaup-frontend-1 /bin/bash
```
Abre un shell bash dentro del contenedor frontend.

## Referencia rápida

| Tarea | Comando | Ubicación |
|------|---------|----------|
| Código de pelusa | `./stuff/lint.sh` | Contenedor exterior |
| Ejecutar pruebas de PHP | `./stuff/runtests.sh` | Contenedor interior |
| Ejecutar ciprés | `npx cypress open` | Contenedor exterior |
| Restablecer base de datos | `./stuff/bootstrap-environment.py --purge` | Contenedor interior |
| Migrar base de datos | `./stuff/db-migrate.py migrate` | Contenedor interior |
| Pruebas de vista | `yarn run test:watch` | Contenedor interior |

## Documentación relacionada

- **[Guía de pruebas](testing.md)** - Documentación de pruebas completa
- **[Pautas de codificación](coding-guidelines.md)** - Estándares de código
- **[Configuración de desarrollo](../../getting-started/development-setup.md)** - Configuración del entorno
