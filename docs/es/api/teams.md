---
title: API de equipos
description: Puntos finales API para gestionar grupos de equipos y competiciones de equipos
icon: bootstrap/account-group
---
# API de equipos

La API de Teams le permite crear y administrar grupos de equipos para competiciones por equipos. Los equipos son grupos de usuarios que compiten juntos como una sola unidad.

## Descripción general

Los grupos de equipos en omegaUp permiten:

- **Competiciones en equipo**: varios usuarios resuelven problemas juntos
- **Tamaño de equipo configurable**: 1-10 concursantes por equipo
- **Gestión de identidad del equipo**: cada equipo tiene su propia identidad

## Puntos finales del grupo de equipo

### Crear grupo de equipo

Crea un nuevo grupo de equipo. El usuario autenticado se convierte en administrador.

**`POST /api/teamsGroup/create/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​único del grupo de equipo |
| `name` | cadena | Sí | Nombre para mostrar |
| `description` | cadena | Sí | Descripción |
| `numberOfContestants` | entero | No | Tamaño del equipo (predeterminado: 3, máximo: 10) |

**Respuesta:**

```json
{
  "status": "ok"
}
```
**Privilegios:** Usuario autenticado (13+)

---

### Actualizar grupo de equipo

Actualiza un grupo de equipo existente.

**`POST /api/teamsGroup/update/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​del grupo de equipo |
| `name` | cadena | Sí | Nuevo nombre para mostrar |
| `description` | cadena | Sí | Nueva descripción |
| `numberOfContestants` | entero | Sí | Tamaño del equipo (1-10) |

**Privilegios:** Administrador del grupo de equipo

---

### Obtener detalles del grupo de equipo

Devuelve información detallada sobre un grupo de equipo.

**`GET /api/teamsGroup/details/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | Alias ​​del grupo de equipo |

**Respuesta:**

```json
{
  "team_group": {
    "create_time": 1609459200,
    "alias": "icpc-team-2024",
    "name": "ICPC Team 2024",
    "description": "Our ICPC competitive team"
  }
}
```
**Privilegios:** Administrador del grupo de equipo

---

### Listar grupos de equipos

Devuelve grupos de equipos que coinciden con una consulta de búsqueda.

**`GET /api/teamsGroup/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `query` | cadena | Sí | Término de búsqueda |

**Respuesta:**

```json
[
  {
    "key": "icpc-team-2024",
    "value": "ICPC Team 2024"
  }
]
```
**Privilegios:** Usuario autenticado

---

### Listar equipos en grupo

Devuelve todos los equipos (identidades) de un grupo de equipos.

**`GET /api/teamsGroup/teams/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | Alias ​​del grupo de equipo |

**Respuesta:**

```json
{
  "identities": [
    {
      "username": "team:icpc-team-2024:alpha",
      "name": "Team Alpha",
      "country": "MX",
      "school": "University"
    }
  ]
}
```
**Privilegios:** Administrador del grupo de equipo

---

### Eliminar equipo

Elimina un equipo de un grupo de equipos.

**`POST /api/teamsGroup/removeTeam/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | Alias ​​del grupo de equipo |
| `usernameOrEmail` | cadena | Sí | Nombre de usuario del equipo para eliminar |

**Privilegios:** Administrador del grupo de equipo

---

## Puntos finales de miembros del equipo

### Agregar miembros al equipo

Agrega uno o más usuarios a un equipo específico.

**`POST /api/teamsGroup/addMembers/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | El nombre de usuario del equipo (por ejemplo, `team:group:teamname`) |
| `usernames` | cadena | Sí | Lista de nombres de usuario separados por comas |

**Respuesta:**

```json
{
  "status": "ok"
}
```
**Privilegios:** Administrador del grupo de equipo

**Errores:**

- `teamMemberUsernameInUse`: El miembro ya está en un equipo.

---

### Eliminar miembro del equipo

Elimina a un miembro de un equipo.

**`POST /api/teamsGroup/removeMember/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | El nombre de usuario del equipo |
| `username` | cadena | Sí | Nombre de usuario del miembro a eliminar |

**Privilegios:** Administrador del grupo de equipo

---

### Listar miembros del equipo

Devuelve todos los miembros de todos los equipos de un grupo de equipo.

**`GET /api/teamsGroup/teamsMembers/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `team_group_alias` | cadena | Sí | Alias ​​del grupo de equipo |
| `page` | entero | No | Número de página (predeterminado: 1) |
| `page_size` | entero | No | Resultados por página (predeterminado: 100) |

**Respuesta:**

```json
{
  "pageNumber": 1,
  "totalRows": 15,
  "teamsUsers": [
    {
      "username": "user1",
      "name": "User One",
      "team_alias": "alpha",
      "team_name": "Team Alpha",
      "classname": "user-rank-expert",
      "isMainUserIdentity": true
    }
  ]
}
```
**Privilegios:** Administrador del grupo de equipo

---

## Formato de nombre de usuario del equipo

Los equipos tienen un formato de nombre de usuario especial:

```
team:{team_group_alias}:{team_name}
```
Por ejemplo: `team:icpc-2024:alpha`

Este nombre de usuario se utiliza para:
- Inicia sesión como equipo
- Referenciar al equipo en llamadas API.
- Visualización en marcadores.

---

## Configuración

### Límites de tamaño del equipo

- **Tamaño de equipo predeterminado**: 3 concursantes
- **Tamaño máximo del equipo**: 10 concursantes
- El tamaño del equipo se configura por grupo de equipo.

---

## Casos de uso

### Creación de una competición estilo ICPC

```bash
# 1. Create team group with 3-person teams
curl -X POST https://omegaup.com/api/teamsGroup/create/ \
  -d "alias=icpc-regionals-2024&name=ICPC Regionals 2024&description=Regional contest&numberOfContestants=3"

# 2. Teams are created via bulk upload or identity management

# 3. Add members to a team
curl -X POST https://omegaup.com/api/teamsGroup/addMembers/ \
  -d "team_group_alias=team:icpc-regionals-2024:mit-alpha&usernames=alice,bob,charlie"

# 4. Use contest API to create contest and add team group
```
---

## Documentación relacionada

- **[API de grupos](groups.md)** - Para grupos de usuarios habituales
- **[API de concursos](contests.md)** - Creación de concursos en equipo
- **[Autenticación](authentication.md)** - Flujo de inicio de sesión del equipo

## Referencia completa

Para obtener detalles completos sobre los terminales, consulte el código fuente de [TeamsGroup Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/TeamsGroup.php).
