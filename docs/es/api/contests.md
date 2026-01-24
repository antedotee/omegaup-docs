---
title: API de concursos
description: Puntos finales API para la gestión y participación de concursos
icon: bootstrap/trophy
---
# API de concursos

La API de Concursos proporciona puntos finales integrales para crear, administrar y participar en concursos de programación.

## Descripción general

Soporte para concursos omegaUp:

- **Múltiples formatos**: IOI, ICPC y puntuación personalizada
- **Tiempos flexibles**: duración fija o ventanas estilo USACO
- **Control de acceso**: público, privado o basado en registro
- **Concursos virtuales**: Practica con condiciones de concursos anteriores

## Gestión del concurso

### Crear concurso

Crea un nuevo concurso. El usuario autenticado se convierte en el director del concurso.

**`POST /api/contest/create/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​único del concurso (utilizado en las URL) |
| `title` | cadena | Sí | Título del concurso |
| `description` | cadena | Sí | Descripción del concurso |
| `start_time` | entero | Sí | Marca de tiempo de inicio (Unix) |
| `finish_time` | entero | Sí | Marca de tiempo de finalización (Unix) |
| `admission_mode` | cadena | No | `public`, `private` o `registration` |
| `score_mode` | cadena | No | `all_or_nothing`, `partial`, `max_per_group` |
| `scoreboard` | entero | No | Visibilidad del marcador (0-100%) |
| `window_length` | entero | No | Ventana estilo USACO en minutos |
| `submissions_gap` | entero | No | Segundos mínimos entre envíos |
| `penalty` | cadena | No | `none`, `runtime`, `submission_count` |
| `penalty_calc_policy` | cadena | No | `sum`, `max` |
| `feedback` | cadena | No | `detailed`, `summary`, `none` |
| `languages` | cadena | No | Lista de idiomas separados por comas |
| `show_scoreboard_after` | booleano | No | Mostrar marcador después del concurso |

**Respuesta:**

```json
{
  "status": "ok"
}
```
---

### Concurso de actualización

Actualiza la configuración de un concurso existente.

**`POST /api/contest/update/`**

**Parámetros:** Igual que crear, más:

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Concurso para actualizar |

**Privilegios:** Administrador del concurso

---

### Concurso de clones

Crea una copia de un concurso existente.

**`POST /api/contest/clone/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Concurso para clonar |
| `title` | cadena | Sí | Nuevo título del concurso |
| `alias` | cadena | Sí | Nuevo alias del concurso |
| `description` | cadena | Sí | Nueva descripción |
| `start_time` | entero | Sí | Nueva marca de tiempo de inicio |

---

### Concurso de Archivo

Archiva un concurso (se oculta de las listas activas).

**`POST /api/contest/archive/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `archive` | booleano | Sí | verdadero para archivar, falso para desarchivar |

---

## Información del concurso

### Lista de concursos

Devuelve una lista paginada de concursos.

**`GET /api/contest/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `page` | entero | No | Número de página |
| `page_size` | entero | No | Resultados por página |
| `query` | cadena | No | Término de búsqueda |
| `tab_name` | cadena | No | `current`, `future`, `past` |
| `admission_mode` | cadena | No | Filtrar por modalidad de admisión |

**Respuesta:**

```json
{
  "results": [
    {
      "alias": "contest-2024",
      "contest_id": 123,
      "title": "Annual Contest 2024",
      "description": "...",
      "start_time": { "time": 1704067200 },
      "finish_time": { "time": 1704153600 },
      "admission_mode": "public",
      "contestants": 150
    }
  ]
}
```
---

### Mis concursos

Devuelve concursos donde el usuario es administrador.

**`GET /api/contest/myList/`**

---

### Lista de concursos participantes

Devuelve concursos donde el usuario está participando.

**`GET /api/contest/listParticipating/`**

---

### Obtener detalles del concurso

Devuelve información completa del concurso.

**`GET /api/contest/details/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |

**Respuesta:**

```json
{
  "alias": "contest-2024",
  "title": "Annual Contest 2024",
  "description": "Contest description",
  "start_time": { "time": 1704067200 },
  "finish_time": { "time": 1704153600 },
  "admission_mode": "public",
  "score_mode": "partial",
  "scoreboard": 80,
  "problems": [...],
  "director": "admin_user",
  "languages": "cpp17-gcc,java,python3"
}
```
---

### Obtener detalles del administrador

Devuelve información del concurso específica del administrador.

**`GET /api/contest/adminDetails/`**

**Privilegios:** Administrador del concurso

---

### Obtener detalles públicos

Devuelve información del concurso públicamente visible.

**`GET /api/contest/publicDetails/`**

---

## Gestión de problemas

### Agregar problema

Agrega un problema a un concurso.

**`POST /api/contest/addProblem/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `problem_alias` | cadena | Sí | Problema para agregar |
| `points` | flotador | Sí | Valor del punto |
| `order_in_contest` | entero | No | Orden de visualización |
| `commit` | cadena | No | Versión del problema específico |

**Privilegios:** Administrador del concurso

---

### Eliminar problema

Elimina un problema de un concurso.

**`POST /api/contest/removeProblem/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `problem_alias` | cadena | Sí | Problema a eliminar |

**Privilegios:** Administrador del concurso

---

### Lista de problemas

Devuelve todos los problemas en un concurso.

**`GET /api/contest/problems/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |

---

## Gestión de usuarios y accesos

### Agregar usuario

Agrega un usuario a un concurso privado.

**`POST /api/contest/addUser/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `usernameOrEmail` | cadena | Sí | Usuario para agregar |

**Privilegios:** Administrador del concurso

---

### Eliminar usuario

Elimina a un usuario de un concurso.

**`POST /api/contest/removeUser/`**

---

### Agregar grupo

Otorga acceso al concurso a todo un grupo.

**`POST /api/contest/addGroup/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `group` | cadena | Sí | Alias ​​de grupo |

---

### Eliminar grupo

**`POST /api/contest/removeGroup/`**

---

### Listar usuarios

Devuelve todos los usuarios con acceso al concurso.

**`GET /api/contest/users/`**

---

### Listar concursantes

Devuelve participantes reales del concurso.

**`GET /api/contest/contestants/`**

---

### Buscar usuarios

Busca usuarios para agregarlos al concurso.

**`GET /api/contest/searchUsers/`**

---

## Gestión administrativa

### Agregar administrador

Otorga privilegios de administrador a un usuario.

**`POST /api/contest/addAdmin/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `usernameOrEmail` | cadena | Sí | Nuevo administrador |

---

### Eliminar administrador

**`POST /api/contest/removeAdmin/`**

---

### Agregar administrador de grupo

Otorga administración a todos los miembros del grupo.

**`POST /api/contest/addGroupAdmin/`**

---

### Eliminar administrador de grupo

**`POST /api/contest/removeGroupAdmin/`**

---

### Lista de administradores

Devuelve todos los administradores del concurso.

**`GET /api/contest/admins/`**

---

## Participación

### Concurso abierto

Abre un concurso para el usuario (inicia su cronómetro en modo USACO).

**`POST /api/contest/open/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |

---

### Regístrate para el concurso

Se registra para un concurso basado en registro.

**`POST /api/contest/registerForContest/`**

---

### Obtener rol de usuario

Devuelve el rol del usuario en un concurso.

**`GET /api/contest/role/`**

**Respuesta:**

```json
{
  "admin": false,
  "contestant": true,
  "reviewer": false
}
```
---

### Crear concurso virtual

Crea un concurso virtual (de práctica) a partir de un concurso anterior.

**`POST /api/contest/createVirtual/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `alias` | cadena | Sí | Alias ​​original del concurso |
| `start_time` | entero | Sí | Hora de inicio virtual |

---

## Marcador

### Obtener marcador

Devuelve el marcador actual.

**`GET /api/contest/scoreboard/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `token` | cadena | No | Token de marcador (para URL compartidas) |

**Respuesta:**

```json
{
  "finish_time": { "time": 1704153600 },
  "problems": [...],
  "ranking": [
    {
      "username": "user1",
      "name": "User One",
      "country": "MX",
      "place": 1,
      "total": { "points": 300, "penalty": 120 },
      "problems": [
        { "alias": "prob-a", "points": 100, "penalty": 30, "runs": 1 }
      ]
    }
  ],
  "start_time": { "time": 1704067200 },
  "time": { "time": 1704100000 },
  "title": "Annual Contest 2024"
}
```
---

### Obtener eventos del marcador

Devuelve eventos de cambio del marcador (para animaciones).

**`GET /api/contest/scoreboardEvents/`**

---

### Fusionar marcadores

Fusiona marcadores de múltiples concursos.

**`GET /api/contest/scoreboardMerge/`**

---

## Ejecuciones y envíos

### Ejecuciones de lista

Devuelve envíos para un concurso.

**`GET /api/contest/runs/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `problem_alias` | cadena | No | Filtrar por problema |
| `username` | cadena | No | Filtrar por usuario |
| `status` | cadena | No | Filtrar por estado |
| `verdict` | cadena | No | Filtrar por veredicto |
| `language` | cadena | No | Filtrar por idioma |
| `offset` | entero | No | Desplazamiento de paginación |
| `rowcount` | entero | No | Resultados por página |

---

### Ejecuta diferencias

Devuelve diferencias entre ejecuciones.

**`GET /api/contest/runsDiff/`**

---

## Aclaraciones

### Obtener aclaraciones

Devuelve aclaraciones del concurso.

**`GET /api/contest/clarifications/`**

---

### Obtener aclaraciones de problemas

Devuelve aclaraciones para un problema específico.

**`GET /api/contest/problemClarifications/`**

---

## Informes y estadísticas

### Informe de actividad

Devuelve la actividad del usuario durante el concurso.

**`GET /api/contest/activityReport/`**

**Privilegios:** Administrador del concurso

---

### Informe del concurso

Devuelve un informe detallado del concurso.

**`GET /api/contest/report/`**

**Privilegios:** Administrador del concurso

---

### Estadísticas del concurso

Devuelve estadísticas del concurso.

**`GET /api/contest/stats/`**

---

### Obtener número de concursantes

**`GET /api/contest/getNumberOfContestants/`**

---

## Solicitudes (basadas en registro)

### Solicitudes de lista

Devuelve solicitudes de registro.

**`GET /api/contest/requests/`**

**Privilegios:** Administrador del concurso

---

### Solicitud de arbitraje

Aprueba o rechaza una solicitud de registro.

**`POST /api/contest/arbitrateRequest/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `username` | cadena | Sí | Usuario solicitante |
| `resolution` | booleano | Sí | verdadero=aprobar, falso=rechazar |
| `note` | cadena | No | Nota opcional |

---

## Integración de equipos

### Reemplazar grupo de equipos

Reemplaza el grupo de equipos para una competencia por equipos.

**`POST /api/contest/replaceTeamsGroup/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `teams_group_alias` | cadena | Sí | Nuevo grupo de equipos |

---

## Otras operaciones

### Establecer recomendado

Marca un concurso como recomendado (solo personal).

**`POST /api/contest/setRecommended/`**

---

### Actualizar hora de finalización de la identidad

Amplia el tiempo para un usuario específico (alojamientos).

**`POST /api/contest/updateEndTimeForIdentity/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `contest_alias` | cadena | Sí | Alias ​​del concurso |
| `username` | cadena | Sí | Usuario para ampliar |
| `end_time` | entero | Sí | Nueva marca de tiempo de finalización |

---

## Modos de concurso

### Modos de admisión

| Modo | Descripción |
|------|-------------|
| `public` | Cualquiera puede participar |
| `private` | Sólo invitación |
| `registration` | Los usuarios deben solicitar acceso |

### Modos de puntuación

| Modo | Descripción |
|------|-------------|
| `all_or_nothing` | Puntos completos sólo para AC |
| `partial` | Puntos parciales por caso de prueba |
| `max_per_group` | Máximo por grupo de prueba |

### Modos de penalización

| Modo | Descripción |
|------|-------------|
| `none` | Sin penalización |
| `runtime` | Penalización total de tiempo de ejecución |
| `submission_count` | Penalización por envío incorrecto |

---

## Documentación relacionada

- **[Ejecuta API](runs.md)** - Gestión de envíos
- **[API de problemas](problems.md)** - Gestión de problemas
- **[API de aclaraciones](clarifications.md)** - Preguntas y respuestas del concurso
- **[API de grupos](groups.md)** - Gestión de grupos

## Referencia completa

Para obtener detalles completos de la implementación, consulte el código fuente del [Controlador del concurso](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Contest.php).
