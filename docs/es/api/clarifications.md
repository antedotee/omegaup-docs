---
title: API de aclaraciones
description: Puntos finales de aclaración del concurso
icon: bootstrap/help-circle
---
# API de aclaraciones

Puntos finales para hacer y responder preguntas durante los concursos.

## Crear aclaración

**`POST clarification/create/`**

Crea una nueva aclaración para un problema en un concurso. Las aclaraciones son privadas por defecto.

**Privilegios**: usuario registrado

**Parámetros:**
- `contest_alias` (cadena, requerida): alias del concurso
- `problem_alias` (cadena, requerida): alias del problema
- `message` (cadena, requerida): Mensaje de aclaración

**Respuesta:**
```json
{
  "status": "ok",
  "clarification_id": 123
}
```
## Obtener detalles aclaratorios

**`GET clarification/:clarification_id/details/`**

Devuelve detalles de una aclaración específica.

**Privilegios**: Usuario registrado con acceso al concurso

**Respuesta:**
```json
{
  "message": "Question text",
  "answer": "Answer text",
  "time": "2020-01-01T12:00:00Z",
  "problem_id": 456,
  "contest_id": 789
}
```
## Actualizar aclaración

**`POST clarification/:clarification_id/update/`**

Actualiza una aclaración (normalmente para agregar una respuesta o hacerla pública).

**Privilegios**: Administrador del concurso o superior

**Parámetros:**
- `contest_alias` (cadena, opcional): alias del concurso
- `problem_alias` (cadena, opcional): alias del problema
- `message` (cadena, opcional): mensaje actualizado
- `answer` (cadena, opcional): Respuesta a la aclaración
- `public` (int, opcional): Hacer pública la aclaración (0 o 1)

**Respuesta:**
```json
{
  "status": "ok"
}
```
## Documentación relacionada

- **[Descripción general de la API REST](rest-api.md)** - Información general de la API
- **[API de concursos](contests.md)** - Gestión de concursos
- **[Arena](../../features/arena.md)** - Interfaz del concurso
