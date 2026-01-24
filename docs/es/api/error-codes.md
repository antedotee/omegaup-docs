---
title: Referencia de códigos de error
description: Referencia completa de códigos de error API y sus significados
icon: bootstrap/help-circle
---
# Referencia de códigos de error

Esta página documenta todos los códigos de error devueltos por la API omegaUp, sus códigos de estado HTTP y las causas comunes.

## Formato de respuesta de error

Todos los errores de API siguen este formato:

```json
{
  "status": "error",
  "error": "Human-readable error message",
  "errorname": "errorKeyName",
  "errorcode": 400,
  "header": "HTTP/1.1 400 BAD REQUEST",
  "parameter": "field_name"
}
```
| Campo | Descripción |
|-------|-------------|
| `status` | Siempre `"error"` para respuestas de error |
| `error` | Mensaje localizado legible por humanos |
| `errorname` | Clave de error legible por máquina |
| `errorcode` | Código de estado HTTP |
| `header` | Encabezado de respuesta HTTP completo |
| `parameter` | (Opcional) Parámetro que provocó el error |

---

## Códigos de estado HTTP

### 400 Solicitud incorrecta

Errores de parámetros o entradas no válidas.

| Nombre del error | Descripción |
|------------|-------------|
| `parameterEmpty` | El parámetro requerido está vacío |
| `parameterInvalid` | El valor del parámetro no es válido |
| `parameterNotFound` | Entidad referenciada no encontrada |
| `parameterStringTooLong` | La cadena supera la longitud máxima |
| `parameterStringTooShort` | Cadena por debajo de la longitud mínima |
| `parameterNumberTooSmall` | Número por debajo del valor mínimo |
| `parameterNumberTooLarge` | El número supera el valor máximo |
| `invalidAlias` | Formato de alias no válido |
| `aliasInUse` | El alias ya existe |

**Ejemplo:**

```json
{
  "status": "error",
  "error": "problem_alias: Parameter is invalid",
  "errorname": "parameterInvalid",
  "errorcode": 400,
  "parameter": "problem_alias"
}
```
---

### 401 No autorizado

Autenticación requerida o no válida.

| Nombre del error | Descripción |
|------------|-------------|
| `loginRequired` | El usuario debe iniciar sesión |
| `invalidCredentialsException` | Nombre de usuario/contraseña incorrectos |
| `emailNotVerified` | Verificación de correo electrónico pendiente |

**Ejemplo:**

```json
{
  "status": "error",
  "error": "Login required",
  "errorname": "loginRequired",
  "errorcode": 401
}
```
---

### 403 Prohibido

Autenticado pero no autorizado.

| Nombre del error | Descripción |
|------------|-------------|
| `userNotAllowed` | El usuario carece de permiso |
| `forbiddenInLockdown` | Sistema en modo bloqueo |
| `contestNotStarted` | El concurso no ha comenzado |
| `contestEnded` | El concurso ha finalizado |
| `cannotSubmit` | El usuario no puede enviar |

**Ejemplo:**

```json
{
  "status": "error",
  "error": "User is not allowed to perform this action",
  "errorname": "userNotAllowed",
  "errorcode": 403
}
```
---

### 404 no encontrado

El recurso solicitado no existe.

| Nombre del error | Descripción |
|------------|-------------|
| `contestNotFound` | El concurso no existe |
| `problemNotFound` | El problema no existe |
| `userNotExist` | El usuario no existe |
| `courseNotFound` | El curso no existe |
| `groupNotFound` | El grupo no existe |
| `schoolNotFound` | La escuela no existe |
| `qualityNominationNotFound` | La nominación no existe |

**Ejemplo:**

```json
{
  "status": "error",
  "error": "Problem not found",
  "errorname": "problemNotFound",
  "errorcode": 404
}
```
---

### 409 Conflicto

Conflicto de estado de recursos.

| Nombre del error | Descripción |
|------------|-------------|
| `duplicatedEntryInDatabase` | El registro ya existe |
| `identityInGroup` | Usuario ya en el grupo |
| `teamMemberUsernameInUse` | Miembro del equipo ya asignado |

**Ejemplo:**

```json
{
  "status": "error",
  "error": "User is already a member of this group",
  "errorname": "identityInGroup",
  "errorcode": 409
}
```
---

### 412 Condición previa fallida

No se cumple la restricción de lógica empresarial.

| Nombre del error | Descripción |
|------------|-------------|
| `qualityNominationMustHaveSolvedProblem` | Debe resolver antes de nominar |
| `qualityNominationMustNotHaveSolvedProblem` | No debe haberse resuelto (para before_ac) |
| `qualityNominationMustHaveTriedToSolveProblem` | Debe haber intentado problema |
| `contestCertificatesError` | Error de generación de certificado |
| `contestCertificatesCurrentContestError` | El concurso no ha terminado |

---

### 429 Demasiadas solicitudes

Se superó el límite de tarifa.

| Nombre del error | Descripción |
|------------|-------------|
| `rateLimitExceeded` | Demasiadas solicitudes de API |
| `submissionWaitGap` | Límite de tasa de envío |

**Encabezados incluidos:**

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1704070800
Retry-After: 3600
```
---

### 500 Error interno del servidor

Errores del lado del servidor.

| Nombre del error | Descripción |
|------------|-------------|
| `generalError` | Error inesperado del servidor |
| `databaseOperationError` | Error en la consulta de la base de datos |

---

### Servicio 503 no disponible

Servicio no disponible temporalmente.

| Nombre del error | Descripción |
|------------|-------------|
| `serviceUnavailable` | Servicio temporalmente caído |

---

## Escenarios de errores comunes

### Errores de autenticación

```json
// Wrong password
{
  "errorname": "invalidCredentialsException",
  "errorcode": 401
}

// Not logged in
{
  "errorname": "loginRequired", 
  "errorcode": 401
}

// Email not verified
{
  "errorname": "emailNotVerified",
  "errorcode": 401
}
```
### Errores de validación

```json
// Missing required field
{
  "errorname": "parameterEmpty",
  "parameter": "name",
  "errorcode": 400
}

// Invalid format
{
  "errorname": "parameterInvalid",
  "parameter": "email",
  "errorcode": 400
}

// Alias taken
{
  "errorname": "aliasInUse",
  "errorcode": 400
}
```
### Errores de permiso

```json
// Not contest admin
{
  "errorname": "userNotAllowed",
  "errorcode": 403
}

// Contest not open yet
{
  "errorname": "contestNotStarted",
  "errorcode": 403
}
```
---

## Prácticas recomendadas para el manejo de errores

### Manejo del lado del cliente

```javascript
async function makeAPICall(endpoint, data) {
  const response = await fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  
  if (result.status === 'error') {
    switch (result.errorcode) {
      case 401:
        // Redirect to login
        window.location.href = '/login/';
        break;
      case 403:
        // Show permission error
        alert(result.error);
        break;
      case 404:
        // Resource not found
        showNotFoundMessage(result.error);
        break;
      case 429:
        // Rate limited - retry after delay
        const retryAfter = response.headers.get('Retry-After');
        setTimeout(() => makeAPICall(endpoint, data), retryAfter * 1000);
        break;
      default:
        // Generic error handling
        console.error(result.error);
    }
    return null;
  }
  
  return result;
}
```
### Comprobación de errores específicos

```javascript
if (result.errorname === 'aliasInUse') {
  // Suggest alternative alias
  suggestAlternative(data.alias);
}
```
---

## Localización

Los mensajes de error se localizan según la preferencia de idioma del usuario. El campo `errorname` permanece constante en todos los lenguajes para el manejo programático.

| Idioma | Ejemplo de valor `error` |
|----------|----------------------|
| Inglés | "Es necesario iniciar sesión" |
| Español | "Inicio de sesión requerida" |
| portugués | "Iniciar sesión necesaria" |

---

## Documentación relacionada

- **[Referencia de API](index.md)** - Descripción general de API
- **[Autenticación](authentication.md)** - Flujo de autenticación y errores

## Referencia completa

Para obtener la lista completa de clases de excepción, consulte el [directorio de excepciones](https://github.com/omegaup/omegaup/tree/main/frontend/server/src/Exceptions) en el código fuente.
