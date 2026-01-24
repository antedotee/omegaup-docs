---
title: API de grupos
description: Puntos finales API para gestionar grupos y marcadores de grupos
icon: bootstrap/account-group
---
# API de grupos

Los grupos le permiten organizar a los usuarios para marcadores y concursos colectivos. Esta API proporciona puntos finales para crear grupos, administrar miembros y manejar marcadores de grupos.

## Descripción general

Los grupos en omegaUp tienen dos propósitos principales:

1. **Organización de usuarios**: agrupa a los usuarios para su seguimiento y administración.
2. **Marcadores**: cree marcadores personalizados que agreguen resultados de múltiples concursos.

## Puntos finales de grupo

### Crear grupo

Crea un nuevo grupo. El usuario autenticado se convierte en el administrador del grupo.

**`POST /api/group/create/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​de grupo único (utilizado en URL) |
| `name` | cadena | Sí | Nombre para mostrar del grupo |
| `description` | cadena | Sí | Descripción del grupo |

**Respuesta:**

```json
{
  "status": "ok"
}
```
**Privilegios:** Usuario autenticado (se convierte en administrador)

---

### Grupo de actualización

Actualiza la información de un grupo existente.

**`POST /api/group/update/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​de grupo |
| `name` | cadena | Sí | Nuevo nombre para mostrar |
| `description` | cadena | Sí | Nueva descripción |

**Privilegios:** Administrador de grupo

---

### Obtener detalles del grupo

Devuelve información detallada sobre un grupo, incluidos sus marcadores.

**`GET /api/group/details/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |

**Respuesta:**

```json
{
  "group": {
    "create_time": 1609459200,
    "alias": "my-group",
    "name": "My Group",
    "description": "A sample group"
  },
  "scoreboards": [
    {
      "alias": "scoreboard-1",
      "create_time": "2021-01-01T00:00:00Z",
      "description": "Main scoreboard",
      "name": "Main Scoreboard"
    }
  ]
}
```
**Privilegios:** Administrador de grupo

---

### Listar grupos de usuarios

Devuelve todos los grupos administrados por el usuario actual.

**`GET /api/group/myList/`**

**Respuesta:**

```json
{
  "groups": [
    {
      "alias": "group-1",
      "create_time": { "time": 1609459200 },
      "description": "Description",
      "name": "Group Name"
    }
  ]
}
```
**Privilegios:** Usuario autenticado

---

### Buscar grupos

Devuelve grupos que coinciden con una consulta de búsqueda. Se utiliza para escribir con anticipación.

**`GET /api/group/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `query` | cadena | Sí | Término de búsqueda |

**Respuesta:**

```json
[
  {
    "label": "Group Name",
    "value": "group-alias"
  }
]
```
**Privilegios:** Usuario autenticado

---

### Obtener miembros del grupo

Devuelve todos los miembros de un grupo.

**`GET /api/group/members/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |

**Respuesta:**

```json
{
  "identities": [
    {
      "username": "user1",
      "name": "User One",
      "country": "MX",
      "country_id": "MX",
      "school": "School Name",
      "school_id": 123
    }
  ]
}
```
**Privilegios:** Administrador de grupo

---

### Agregar usuario al grupo

Agrega un usuario a un grupo.

**`POST /api/group/addUser/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `usernameOrEmail` | cadena | Sí | Nombre de usuario o correo electrónico del usuario a agregar |

**Respuesta:**

```json
{
  "status": "ok"
}
```
**Privilegios:** Administrador de grupo

**Errores:**

- `identityInGroup`: El usuario ya es miembro del grupo.

---

### Eliminar usuario del grupo

Elimina un usuario de un grupo.

**`POST /api/group/removeUser/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `usernameOrEmail` | cadena | Sí | Nombre de usuario o correo electrónico del usuario a eliminar |

**Privilegios:** Administrador de grupo

---

### Crear marcador

Crea un nuevo marcador para un grupo.

**`POST /api/group/createScoreboard/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `alias` | cadena | Sí | Alias ​​del marcador |
| `name` | cadena | Sí | Nombre para mostrar del marcador |
| `description` | cadena | No | Descripción del marcador |

**Privilegios:** Administrador de grupo

---

## Puntos finales del marcador de grupo

Los marcadores grupales agregan resultados de múltiples concursos.

### Agregar concurso al marcador

Agrega un concurso a un marcador de grupo.

**`POST /api/groupScoreboard/addContest/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `scoreboard_alias` | cadena | Sí | Alias ​​del marcador |
| `contest_alias` | cadena | Sí | Concurso para sumar |
| `weight` | flotador | Sí | Peso para marcar |
| `only_ac` | booleano | No | Solo cuente las presentaciones de AC |

**Privilegios:** Administrador de grupo + acceso al concurso

---

### Eliminar concurso del marcador

Elimina un concurso de un marcador de grupo.

**`POST /api/groupScoreboard/removeContest/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `scoreboard_alias` | cadena | Sí | Alias ​​del marcador |
| `contest_alias` | cadena | Sí | Concurso para eliminar |

**Privilegios:** Administrador de grupo

---

### Obtener detalles del marcador

Devuelve detalles del marcador, incluida la clasificación y los concursos.

**`GET /api/groupScoreboard/details/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |
| `scoreboard_alias` | cadena | Sí | Alias ​​del marcador |

**Respuesta:**

```json
{
  "ranking": [
    {
      "username": "user1",
      "name": "User One",
      "contests": {
        "contest-1": { "points": 100, "penalty": 50 }
      },
      "total": { "points": 100, "penalty": 50 }
    }
  ],
  "scoreboard": {
    "alias": "scoreboard-1",
    "name": "Main Scoreboard",
    "description": "Description"
  },
  "contests": [...]
}
```
**Privilegios:** Administrador de grupo

---

### Listar marcadores de grupos

Devuelve todos los marcadores de un grupo.

**`GET /api/groupScoreboard/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `group_alias` | cadena | Sí | Alias ​​de grupo |

**Privilegios:** Administrador de grupo

---

## Casos de uso

### Creando un grupo de clase

```bash
# 1. Create the group
curl -X POST https://omegaup.com/api/group/create/ \
  -d "alias=algorithms-2024&name=Algorithms 2024&description=Spring semester class"

# 2. Add students
curl -X POST https://omegaup.com/api/group/addUser/ \
  -d "group_alias=algorithms-2024&usernameOrEmail=student1@example.com"

# 3. Create a scoreboard
curl -X POST https://omegaup.com/api/group/createScoreboard/ \
  -d "group_alias=algorithms-2024&alias=homework&name=Homework Scores"

# 4. Add contests to scoreboard
curl -X POST https://omegaup.com/api/groupScoreboard/addContest/ \
  -d "group_alias=algorithms-2024&scoreboard_alias=homework&contest_alias=hw1&weight=1.0"
```
## Documentación relacionada

- **[API de Teams](teams.md)** - Para administrar grupos de equipos
- **[API de concursos](contests.md)** - Creación de concursos para grupos
- **[API de usuarios](users.md)** - Gestión de usuarios

## Referencia completa

Para obtener detalles completos sobre los terminales, consulte el código fuente de [Group Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Group.php) y [GroupScoreboard Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/GroupScoreboard.php).
