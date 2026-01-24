---
title: API de problemas
description: Puntos finales API para la creación y gestión de problemas
icon: bootstrap/puzzle
---
# API de problemas

Puntos finales para crear, actualizar y gestionar problemas de programación.

## Crear problema

**`POST problem/create/`**

Crea un nuevo problema.

**Privilegios**: usuario registrado

**Parámetros:**
- `title` (cadena, requerida): Título del problema
- `alias` (cadena, requerida): alias del problema
- `source` (cadena, opcional): origen del problema (p. ej., "OMI 2020")
- `public` (int, requerido): 0 para privado, 1 para público
- `validator` (cadena, requerida): Tipo de validador (ver más abajo)
- `time_limit` (int, requerido): Límite de tiempo en milisegundos
- `memory_limit` (int, requerido): Límite de memoria en KB
- `problem_contents` (ARCHIVO, requerido): archivo ZIP con el contenido del problema

**Tipos de validador:**
- `literal`: coincidencia exacta
- `token`: Comparación token por token
- `token-caseless`: Comparación de tokens que no distingue entre mayúsculas y minúsculas
- `token-numeric`: Comparación numérica con tolerancia
- `custom`: validador definido por el usuario

**Respuesta:**
```json
{
  "status": "ok",
  "uploaded_files": ["file1.in", "file1.out", ...]
}
```
## Obtener detalles del problema

**`GET problems/:problem_alias/details/`**

Devuelve detalles del problema dentro de un contexto de concurso.

**Privilegios**: usuario registrado; los concursos privados requieren invitación

**Parámetros:**
- `contest_alias` (cadena, requerida): alias del concurso
- `lang` (cadena, opcional): Idioma (por defecto: "es")

**Respuesta:**
```json
{
  "title": "Problem Title",
  "author_id": 123,
  "validator": "token-numeric",
  "time_limit": 3000,
  "memory_limit": 65536,
  "visits": 1000,
  "submissions": 500,
  "accepted": 200,
  "difficulty": 5.5,
  "creation_date": "2020-01-01T00:00:00Z",
  "source": "OMI 2020",
  "runs": [...]
}
```
## Documentación relacionada

- **[Creando problemas](../../features/problems/creating-problems.md)** - Guía de creación de problemas
- **[Formato del problema](../../features/problems/problem-format.md)** - Estructura del archivo ZIP
- **[Descripción general de la API REST](rest-api.md)** - Información general de la API
