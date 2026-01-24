---
title: API de insignias
description: Puntos finales API para el sistema de insignias de logros
icon: bootstrap/award
---
# API de insignias

Las insignias son logros que los usuarios obtienen por diversos logros en la plataforma. Esta API le permite consultar las insignias y la propiedad de las insignias de los usuarios.

## Descripción general

El sistema de insignias de omegaUp recompensa a los usuarios por:

- Resolver problemas
- Participar en concursos.
- Aportes comunitarios
- Logros especiales

Las insignias se asignan automáticamente mediante procesos en segundo plano cuando los usuarios cumplen con los criterios.

## Puntos finales

### Listar todas las insignias

Devuelve una lista de todos los alias de insignias disponibles.

**`GET /api/badge/list/`**

**Respuesta:**

```json
[
  "problemSetter",
  "contestParticipant",
  "100Problems",
  "firstAC"
]
```
**Privilegios:** Público (no se requiere autenticación)

---

### Obtener insignias de usuario

Devuelve todas las insignias propiedad del usuario autenticado actual.

**`GET /api/badge/myList/`**

**Respuesta:**

```json
{
  "badges": [
    {
      "badge_alias": "firstAC",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 50000,
      "total_users": 100000
    }
  ]
}
```
**Privilegios:** Usuario autenticado

---

### Obtener insignias por nombre de usuario

Devuelve todas las insignias propiedad de un usuario específico.

**`GET /api/badge/userList/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `target_username` | cadena | Sí | Nombre de usuario para consultar |

**Respuesta:**

```json
{
  "badges": [
    {
      "badge_alias": "problemSetter",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 1500,
      "total_users": 100000
    }
  ]
}
```
**Privilegios:** Público

---

### Obtener detalles de la insignia

Devuelve información detallada sobre una insignia específica.

**`GET /api/badge/badgeDetails/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `badge_alias` | cadena | Sí | Alias ​​de insignia |

**Respuesta:**

```json
{
  "badge_alias": "100Problems",
  "assignation_time": null,
  "first_assignation": { "time": 1546300800 },
  "owners_count": 2500,
  "total_users": 100000
}
```
**Campos:**

| Campo | Descripción |
|-------|-------------|
| `badge_alias` | Identificador de insignia único |
| `assignation_time` | Cuándo lo obtuvo el usuario actual (nulo si no es propietario) |
| `first_assignation` | Cuando se otorgó la insignia por primera vez |
| `owners_count` | Número de usuarios que tienen esta insignia |
| `total_users` | Total de usuarios registrados (para cálculo porcentual) |

**Privilegios:** Público

---

### Obtener hora de asignación de insignias

Devuelve cuando el usuario actual obtuvo una insignia específica.

**`GET /api/badge/myBadgeAssignationTime/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `badge_alias` | cadena | Sí | Alias ​​de insignia |

**Respuesta:**

```json
{
  "assignation_time": { "time": 1609459200 }
}
```
Devuelve `null` para `assignation_time` si el usuario no tiene la insignia.

**Privilegios:** Usuario autenticado

---

## Insignias disponibles

Las insignias se definen en el directorio `frontend/badges/`. Cada insignia tiene:

- Un alias único (nombre de carpeta)
- Un icono (`icon.svg`)
- Descripciones localizadas
- Criterios de asignación (SQL o basados en código)

Categorías de insignias comunes:

### Resolución de problemas
- `firstAC` - Primera presentación aceptada
- `100Problems` - Resuelto 100 problemas
- `legacyUser` - Usuario inicial de la plataforma

### Participación en el concurso
- `contestParticipant` - Participó en un concurso.
- `virtualContestParticipant` - Participó en un concurso virtual

### Creación de contenido
- `problemSetter` - Creó un problema público
- `problemSetterAdvanced` - Creó múltiples problemas de calidad

### Comunidad
- `coderOfTheMonth` - Seleccionado como codificador del mes

---

## Asignación de insignia

Las insignias son asignadas automáticamente por:

1. **Trabajos cron**: comprobaciones periódicas de los criterios
2. **Activadores de eventos**: asignación inmediata de acciones calificadas

Los usuarios no pueden reclamar insignias manualmente.

---

## Casos de uso

### Mostrar logros del usuario

```javascript
// Fetch user's badges for profile display
const response = await fetch('/api/badge/userList/?target_username=omegaup');
const { badges } = await response.json();

badges.forEach(badge => {
  console.log(`${badge.badge_alias}: ${badge.owners_count} owners`);
});
```
### Verificar la rareza de la insignia

```javascript
// Calculate badge rarity percentage
const details = await fetch('/api/badge/badgeDetails/?badge_alias=100Problems');
const badge = await details.json();

const rarity = (badge.owners_count / badge.total_users * 100).toFixed(2);
console.log(`${rarity}% of users have this badge`);
```
---

## Documentación relacionada

- **[API de usuarios](users.md)** - Información del perfil del usuario
- **[API de problemas](problems.md)** - Logros relacionados con problemas
- **[API de concursos](contests.md)** - Logros relacionados con el concurso

## Referencia completa

Para obtener definiciones completas de insignias y lógica de asignación, consulte el [Controlador de insignias](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Badge.php) y el [directorio de insignias](https://github.com/omegaup/omegaup/tree/main/frontend/badges).
