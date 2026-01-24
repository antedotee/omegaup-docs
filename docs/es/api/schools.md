---
title: API de escuelas
description: Puntos finales API para gestión y clasificación de escuelas
icon: bootstrap/school
---
# API de escuelas

La API de escuelas proporciona puntos finales para administrar escuelas, ver clasificaciones de escuelas y el programa Escuela del mes.

## Descripción general

Escuelas en omegaUp:

- Seguimiento de afiliaciones de usuarios
- Contribuir a las clasificaciones escolares basadas en la actividad de los miembros.
- Participar en el programa Escuela del Mes

## Puntos finales

### Listar escuelas

Busca escuelas que coincidan con una consulta. Se utiliza para escritura anticipada/autocompletar.

**`GET /api/school/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `query` | cadena | Sí* | Término de búsqueda |
| `term` | cadena | Sí* | Parámetro de búsqueda alternativo |

*Se requiere uno de `query` o `term`.

**Respuesta:**

```json
{
  "results": [
    {
      "key": 123,
      "value": "Massachusetts Institute of Technology"
    },
    {
      "key": 456,
      "value": "Stanford University"
    }
  ]
}
```
**Privilegios:** Usuario autenticado

---

### Crear escuela

Crea una nueva entrada de escuela.

**`POST /api/school/create/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `name` | cadena | Sí | Nombre de la escuela |
| `country_id` | cadena | No | Código de país (por ejemplo, "MX", "US") |
| `state_id` | cadena | No | Código de estado/provincia |

**Respuesta:**

```json
{
  "school_id": 789
}
```
**Notas:**

- Si existe una escuela con el mismo nombre, devuelve el ID de la escuela existente.
- El estado requiere que se especifique el país

**Privilegios:** Usuario autenticado

---

### Seleccione la escuela del mes

Selecciona una escuela como Escuela del Mes (solo mentor).

**`POST /api/school/selectSchoolOfTheMonth/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `school_id` | entero | Sí | ID de escuela para seleccionar |

**Respuesta:**

```json
{
  "status": "ok"
}
```
**Privilegios:** Rol de mentor

**Requisitos:**

- Debe estar dentro del periodo de selección.
- La escuela debe estar en la lista de candidatos.
- No se puede seleccionar si ya está seleccionado para el mes

---

## Datos del perfil escolar

Los perfiles escolares incluyen:

### Información básica

- Nombre de la escuela
- Ubicación (país, estado)
- Clasificación mundial

### Estadísticas

- Recuento mensual de problemas resueltos.
- Codificadores del mes de la escuela.
- Usuarios activos y sus logros.

---

## Clasificaciones escolares

Las escuelas se clasifican según:

1. **Puntuación**: Actividad total de los miembros
2. **Problemas resueltos**: Total de problemas resueltos por los miembros
3. **Usuarios activos**: Número de miembros contribuyentes

Las clasificaciones se almacenan en caché y se actualizan periódicamente.

---

## Escuela del mes

### Descripción general del programa

Cada mes, se selecciona una escuela como "Escuela del mes" según:

- Actividad de los miembros y resolución de problemas.
- Participación en el concurso
- Aportes de calidad

### Proceso de selección

1. El sistema genera candidatos según la actividad.
2. Los mentores pueden seleccionar candidatos durante la ventana de selección.
3. El candidato que ocupa el primer lugar se selecciona de forma predeterminada si no se selecciona un mentor.

### Datos del candidato

```json
{
  "candidatesToSchoolOfTheMonth": [
    {
      "school_id": 123,
      "name": "Top University",
      "country_id": "MX",
      "ranking": 1,
      "score": 1500.5,
      "school_of_the_month_id": 456
    }
  ]
}
```
---

## Campos del perfil de la escuela

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `school_id` | entero | Identificador único |
| `name` | cadena | Nombre de la escuela |
| `country_id` | cadena | Código de país |
| `ranking` | entero | Posición en el ranking mundial |
| `score` | flotador | Puntuación de actividad calculada |

---

## Casos de uso

### Registro de usuario en la escuela

```javascript
// Search for school
const schools = await fetch('/api/school/list/?query=MIT');
const results = await schools.json();

// Use school_id (key) in user profile
const schoolId = results.results[0].key;
```
### Crear nueva escuela

```bash
curl -X POST https://omegaup.com/api/school/create/ \
  -d "name=New Tech University&country_id=US&state_id=CA"
```
---

## Datos relacionados

### Problemas resueltos mensuales

Seguimiento de la actividad escolar a lo largo del tiempo:

```json
{
  "monthly_solved_problems": [
    { "year": 2024, "month": 1, "problems_solved": 150 },
    { "year": 2024, "month": 2, "problems_solved": 175 }
  ]
}
```
### Usuarios de la escuela

Principales colaboradores de una escuela:

```json
{
  "school_users": [
    {
      "username": "top_coder",
      "classname": "user-rank-master",
      "created_problems": 10,
      "solved_problems": 500,
      "organized_contests": 5
    }
  ]
}
```
---

## Documentación relacionada

- **[API de usuarios](users.md)** - Perfil de usuario y asociación escolar
- **[API de problemas](problems.md)** - Estadísticas de resolución de problemas

## Referencia completa

Para obtener detalles completos de la implementación, consulte el código fuente del [Controlador escolar](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/School.php).
