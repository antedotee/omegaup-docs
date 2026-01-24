---
title: Arquitectura de back-end
description: Controladores PHP, patrones DAO/VO y estructura API
icon: bootstrap/server
---
# Arquitectura de back-end

El backend de omegaUp está construido con PHP siguiendo el patrón MVC, con una clara separación entre controladores, acceso a datos y lógica de negocio.

## Estructura del directorio

```
frontend/server/src/
├── Controllers/           # API controllers
├── DAO/                  # Data Access Objects
│   ├── VO/               # Value Objects
│   └── Base/             # Base DAO classes
└── libs/                 # Libraries and utilities
```
## Controladores

Los controladores manejan solicitudes HTTP e implementan lógica empresarial:

- Ubicado en `frontend/server/src/Controllers/`
- Un controlador por recurso API (por ejemplo, `RunController`, `ContestController`)
- Los métodos corresponden a puntos finales de API (por ejemplo, `apiCreate`, `apiDetails`)

## Patrón DAO/VO

### Objetos de valor (VO)
- Mapear directamente a las tablas de la base de datos.
- Generado automáticamente a partir del esquema.
- Ubicado en `frontend/server/src/DAO/VO/`

### Objetos de acceso a datos (DAO)
- Clases estáticas para operaciones de bases de datos.
- Métodos: `search()`, `getByPK()`, `save()`, `delete()`
- Ubicado en `frontend/server/src/DAO/`

### Ejemplo de uso

```php
// Create a VO
$user = new Users();
$user->setEmail('user@example.com');

// Search using DAO
$results = UsersDAO::search($user);

// Access results
if (count($results) > 0) {
    $foundUser = $results[0];
    echo $foundUser->getUserId();
}
```
## Documentación relacionada

- **[Patrones de base de datos](../development/database-patterns.md)** - Guía detallada de DAO/VO
- **[Patrón MVC](mvc-pattern.md)** - Implementación de MVC
- **[Referencia de API](../api/index.md)** - Puntos finales de API
