---
title: Directrices de codificación
description: Estándares de codificación y mejores prácticas para el desarrollo de omegaUp
icon: bootstrap/code
---
# Pautas de codificación

Este documento describe los estándares de codificación y las mejores prácticas para contribuir a omegaUp. Estas pautas se aplican mediante linters automatizados y pruebas de integración.

## Principios generales

### Tipo Seguridad

Todo el código debe declarar tipos de datos en parámetros de función y tipos de retorno:

- **TypeScript** para interfaz (`frontend/www/`)
- **Salmo** para PHP (`frontend/server/`)
- **mypy** para Python (`stuff/`)

!!! consejo "Escribir anotaciones"
    Prefiera anotaciones de tipo para matrices/mapas dentro de funciones para que el código sea más fácil de entender.

### Idioma

- Todo el código y los comentarios están escritos en **inglés**

### Pruebas

- Los cambios en la funcionalidad deben ir acompañados de pruebas.
- Todas las pruebas deben pasar el 100% antes de comprometerse.
- Sin excepciones

### Calidad del código

- Evite `null` y `undefined` siempre que sea posible
- Utilice [Patrón de cláusula de protección](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html)
- Elimina el código no utilizado (no lo comentes, usa el historial de git)
- Minimizar la distancia entre la declaración de variables y el primer uso.

### Convenciones de nomenclatura

- **camelCase** para funciones, variables y clases
- **snake_case** excepciones:
  - Nombres de columnas de MySQL
  - Variables y parámetros de Python.
  - Parámetros API

!!! advertencia "Abreviaturas"
    Evite abreviaturas en el código y los comentarios. No son obvios para todos.

## Formato de código

Delegamos el formato a herramientas automatizadas:

- **[yapf](https://github.com/google/yapf)** para Python
- **[prettier.io](https://prettier.io/)** para TypeScript/Vue
- **[phpcbf](https://github.com/squizlabs/PHP_CodeSniffer)** para PHP

Validar estilo con:

```bash
./stuff/lint.sh validate
```
### Pautas de estilo

- Utilice 2/4 espacios (depende del tipo de archivo), no tabulaciones
- Finales de línea estilo Unix (`\n`), no Windows (`\r\n`)
- Corchetes de apertura en la misma línea que la declaración
- Espacio entre palabras clave y paréntesis: `if`, `else`, `while`, `switch`, `catch`, `function`
- No hay espacio antes de los paréntesis de llamada a función.
- Sin espacios entre paréntesis
- Espacio después de la coma, no antes.
- Operadores binarios: espacio antes y después.
- Máximo una línea en blanco seguida
- No hay comentarios vacíos
- Sólo comentarios de línea `//`, no comentarios de bloque `/* */`

## Pautas de PHP

### Pruebas

```php
// Tests must pass 100% before committing
// All functionality changes need tests
```
### Consultas de bases de datos

Evite consultas O(n). Cree consultas manuales para viajes sencillos de ida y vuelta:

```php
// ❌ Bad: Multiple queries
foreach ($users as $user) {
    $runs = RunsDAO::searchByUserId($user->userId);
}

// ✅ Good: Single query
$runs = RunsDAO::searchByUserIds(array_map(fn($u) => $u->userId, $users));
```
### Parámetros de función

Las funciones API son las únicas que pueden recibir `\OmegaUp\Request`. Todas las demás funciones deben:

1. Validar parámetros
2. Extraer a variables escritas
3. Llamar funciones con estas variables.

### Documentación de funciones

Todas las funciones deben estar documentadas:

```php
/**
 * set
 *
 * If cache is on, save value in key with given timeout
 *
 * @param string $value
 * @param int $timeout
 * @return boolean
 */
public function set($value, $timeout) { ... }
```
### Excepciones

Utilice excepciones para informar errores. Se permiten funciones que devuelven verdadero/falso cuando representan valores esperados.

### Respuestas API

Todas las API deben devolver matrices asociativas.

## Directrices de Vue.js

### Comportamiento del componente

Evite componentes que cambien significativamente el comportamiento según las banderas. Utilice `slot` en su lugar:

```vue
<!-- ✅ Good: Using slots for customization -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```
### Internacionalización

Nunca codifique texto. Utilice siempre cadenas de traducción:

```typescript
// ❌ Bad: Hardcoded text
<div>Contest ranking: {% raw %}{{ user.rank }}{% endraw %}</div>

// ✅ Good: Translation string
<div>{% raw %}{{ T.contestRanking }}{% endraw %}</div>
```
!!! consejo "Formato de cadenas"
    Evite concatenar cadenas de traducción. Utilice `ui.formatString()` con parámetros en su lugar.

### Colores

Evite los colores hexadecimales o `rgb()`. Utilice variables CSS para admitir el modo oscuro.

### Ganchos de ciclo de vida

Evite los ganchos del ciclo de vida a menos que interactúe directamente con DOM. También se debe evitar la interacción directa con DOM.

### Propiedades calculadas

Prefiera las propiedades calculadas y los observadores a la manipulación programática de variables.

### Libro de cuentos

Agregue historias de Storybook para nuevos componentes. Actualizar historias al modificar componentes existentes.

## Directrices de TypeScript

### Parámetros de función

Cuando una función tiene más de 2-3 parámetros, especialmente del mismo tipo, use un objeto:

```typescript
// ❌ Bad: Too many parameters
function updateProblem(
  problem: Problem,
  previousVersion: string,
  currentVersion: string,
  points?: int
): void { ... }

// ✅ Good: Object parameter
function updateProblem({
  problem,
  previousVersion,
  currentVersion,
  points,
}: {
  problem: Problem;
  previousVersion: string;
  currentVersion: string;
  points?: int;
}): void { ... }
```
### Escriba afirmaciones

Evite las afirmaciones de tipo excepto:
- Interacciones DOM (`document.querySelector`)
- Declaraciones de tipo literal vacías: `null as null | string`
- Pruebas: declarando `params` en el constructor Vue

### jQuery en desuso

`jQuery` ha quedado obsoleto y no se puede utilizar.

## Directrices de Python

### Parámetros de función

Para funciones con muchos parámetros, especialmente los opcionales, utilice parámetros de solo palabras clave:

```python
# ❌ Bad: Positional parameters
def updateProblem(
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None
) -> None: ...

# ✅ Good: Keyword-only parameters
def updateProblem(
    *,
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None,
) -> None: ...
```
### Nombrar

- **snake_case** para funciones y variables
- **CamelCase** para clases

### Importaciones

Evite `from module import function`. Importe módulos y use notación de puntos:

```python
# ❌ Bad
from module import function
function()

# ✅ Good
import module
module.function()
```
Excepción: el módulo `typing` puede usar `from typing import ...`

## Comentarios

Los comentarios deben explicar **por qué**, no **qué**:

```php
// ❌ Bad: Explains what
// Increment counter
$counter++;

// ✅ Good: Explains why
// Increment counter to track retry attempts for rate limiting
$counter++;
```
## Documentación relacionada

- **[Guía de pruebas](testing.md)** - Cómo escribir pruebas
- **[Comandos útiles](useful-commands.md)** - Comandos de desarrollo
- **[Guía de componentes](components.md)** - Desarrollo de componentes de Vue

---

**Recuerde:** Estas pautas se aplican mediante herramientas automatizadas. ¡Ejecute `./stuff/lint.sh` antes de comprometerse!
