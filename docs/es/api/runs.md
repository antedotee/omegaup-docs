---
title: Ejecuta API
description: Manejo de envíos y puntos finales de recuperación de resultados
icon: bootstrap/play-circle
---
# Ejecuta API

Puntos finales para enviar código y recuperar resultados de envío.

## Crear ejecución (enviar código)

**`POST runs/create/`**

Crea un nuevo envío para un problema en un concurso.

**Privilegios**: usuario registrado

**Parámetros:**
- `problem_alias` (cadena, requerida): alias del problema
- `contest_alias` (cadena, requerida): alias del concurso
- `language` (cadena, requerida): Lenguaje de programación
- `source` (cadena, requerida): Código fuente

**Respuesta:**
```json
{
  "status": "ok",
  "guid": "abc123def456..."
}
```
## Obtener detalles de ejecución

**`GET runs/:run_alias/details/`**

Devuelve detalles de un envío específico.

**Privilegios**: usuario registrado

**Respuesta:**
```json
{
  "guid": "abc123def456...",
  "language": "cpp",
  "status": "ready",
  "verdict": "AC",
  "runtime": 150,
  "memory": 2048,
  "score": 1.0,
  "contest_score": 100,
  "time": 1436577101,
  "submit_delay": 30
}
```
## Obtener fuente de ejecución

**`GET runs/:run_alias/source/`**

Devuelve el código fuente de un envío. Si la compilación falla, devuelve un error de compilación.

**Privilegios**: usuario registrado

**Respuesta:**
```json
{
  "source": "#include <iostream>...",
  "compilation_error": null
}
```
## Valores de estado de ejecución

- `new`: Recién creado
- `waiting`: En cola
- `compiling`: En proceso de compilación
- `running`: Ejecutando
- `ready`: Evaluación completa

## Valores de veredicto

- `AC`: Aceptado
- `PA`: Aceptado parcialmente
- `PE`: Error de presentación
- `WA`: Respuesta incorrecta
- `TLE`: Límite de tiempo excedido
- `OLE`: Límite de salida excedido
- `MLE`: Límite de memoria excedido
- `RTE`: Error de tiempo de ejecución
- `RFE`: Error de función restringida
- `CE`: Error de compilación
- `JE`: Error de juez

## Documentación relacionada

- **[Descripción general de la API REST](rest-api.md)** - Información general de la API
- **[Calificador](../../features/grader.md)** - Sistema de evaluación
- **[Runner](../../features/runner.md)** - Ejecución de código
