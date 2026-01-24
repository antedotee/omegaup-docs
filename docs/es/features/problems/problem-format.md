---
title: Formato del problema
description: Estructura de archivos ZIP para la creación manual de problemas
icon: bootstrap/file-document
---
# Formato del problema

Para la creación avanzada de problemas, puede crear manualmente un archivo `.zip` con la estructura adecuada.

## Estructura del archivo ZIP

```
problem.zip
├── statements/
│   ├── es.markdown      # Spanish statement
│   ├── en.markdown      # English statement
│   └── pt.markdown      # Portuguese statement
├── cases/
│   ├── 01.in
│   ├── 01.out
│   ├── 02.in
│   ├── 02.out
│   └── ...
├── validator.cpp         # Optional: Custom validator
├── limits.json           # Optional: Custom limits
└── testplan              # Optional: Test case weights
```
## Formato de declaración

Las declaraciones están escritas en Markdown:

```markdown
# Problem Title

## Description

Problem description here...

## Input

Input format description...

## Output

Output format description...

## Examples

### Example 1

**Input:**
```
1 2
```

**Output:**
```
3
```
```
## Casos de prueba

Los casos de prueba son pares de archivos `.in` y `.out`:

- `01.in`, `01.out`
- `02.in`, `02.out`
- `03.in`, `03.out`
-...

## Validador

Si utiliza un validador personalizado, incluya el código fuente (por ejemplo, `validator.cpp`).

## Documentación relacionada

- **[Creando problemas](creating-problems.md)** - Guía de creación de problemas
- **[Guía ZIP manual](../../../frontend/www/docs/Manual-for-Zip-File-Creation-for-Problems.md)** - Especificación de formato detallada
