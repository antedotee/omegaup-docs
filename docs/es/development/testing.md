---
title: Guía de prueba
description: Guía de pruebas completa para omegaUp
icon: bootstrap/flask
---
# Guía de prueba

omegaUp utiliza múltiples marcos de prueba para garantizar la calidad del código en diferentes capas.

## Pila de pruebas

| Capa | Marco | Ubicación |
|-------|-----------|----------|
| Pruebas unitarias de PHP | Unidad PHP | `frontend/tests/controllers/` |
| Pruebas de TypeScript/Vue | Broma | `frontend/www/js/` |
| Pruebas E2E | Ciprés | `cypress/e2e/` |
| Pruebas de Python | pytest | `stuff/` |

## Pruebas unitarias de PHP

### Ejecutando todas las pruebas de PHP

```bash
./stuff/runtests.sh
```
Ejecuta pruebas PHPUnit, validación de tipo MySQL y Psalm.

**Ubicación**: Dentro del contenedor Docker

### Ejecutando un archivo de prueba específico

```bash
./stuff/run-php-tests.sh frontend/tests/controllers/MyControllerTest.php
```
Omita el nombre del archivo para ejecutar todas las pruebas.

### Requisitos de prueba

- Todas las pruebas deben pasar el 100% antes de comprometerse.
- La nueva funcionalidad requiere pruebas nuevas/modificadas
- Pruebas ubicadas en `frontend/tests/controllers/`

## Pruebas de TypeScript/Vue

### Ejecución de pruebas de Vue (modo de vigilancia)

```bash
yarn run test:watch
```
Vuelve a ejecutar pruebas automáticamente cuando cambia el código.

**Ubicación**: Dentro del contenedor Docker

### Ejecutando un archivo de prueba específico

```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/MyComponent.test.ts
```
### Estructura de prueba

Verificación de pruebas de componentes de Vue:
- Visibilidad de los componentes
- Emisión de eventos
- Comportamiento esperado
- Props y estado

## Pruebas de ciprés E2E

### Apertura del corredor de prueba de Cypress

```bash
npx cypress open
```
Abre una interfaz gráfica para pruebas interactivas.

**Requisitos previos**:
- Node.js instalado
- NPM instalado
-libasound2 (Linux)

**Ubicación**: contenedor Docker exterior

### Ejecución de pruebas de Cypress

```bash
yarn test:e2e
```
Ejecuta todas las pruebas de Cypress sin cabeza.

### Archivos de prueba

Pruebas E2E ubicadas en `cypress/e2e/`:
- `login.spec.ts`
-`problem-creation.spec.ts`
-`contest-management.spec.ts`
- Y más...

## Pruebas de Python

Las pruebas de Python utilizan pytest y se encuentran en el directorio `stuff/`.

## Cobertura de prueba

Usamos **Codecov** para medir la cobertura:

- **PHP**: Cobertura medida ✅
- **TypeScript**: Cobertura medida ✅
- **Cypress**: Cobertura aún no medida ⚠️

## Mejores prácticas

### Escriba las pruebas primero
Cuando sea posible, escriba pruebas antes de la implementación (TDD).

### Probar rutas críticas
Centrarse en:
- Flujos de autenticación de usuarios.
- Presentación y evaluación de problemas.
- Gestión del concurso
- Puntos finales API

### Mantenga las pruebas rápidas
- Las pruebas unitarias deben ser rápidas (< 1 segundo)
- Las pruebas E2E pueden ser más lentas pero deben completarse en un tiempo razonable

### Prueba de aislamiento
- Cada prueba debe ser independiente.
- Limpiar datos de prueba después de las pruebas.
- Utilice dispositivos de prueba para obtener datos consistentes

## Documentación relacionada

- **[Pautas de codificación](coding-guidelines.md)** - Estándares de código
- **[Comandos útiles](useful-commands.md)** - Comandos de prueba
- **[Guía de Cypress](../../../frontend/www/docs/How-to-use-Cypress-in-omegaUp.md)** - Guía detallada de Cypress
