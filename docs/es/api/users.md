---
title: API de usuarios
description: Puntos finales de autenticación y gestión de usuarios
icon: bootstrap/account-group
---
# API de usuarios

Puntos finales para gestión de usuarios, autenticación y operaciones de perfiles.

## Iniciar sesión

**`POST user/login/`**

Autentica a un usuario y devuelve un token de autenticación.

**Privilegios**: Ninguno (punto final público)

**Parámetros:**
- `usernameOrEmail` (cadena, requerida): Nombre de usuario o correo electrónico
- `password` (cadena, requerida): Contraseña de usuario

**Respuesta:**
```json
{
  "status": "ok",
  "auth_token": "abc123def456..."
}
```
!!! importante "Uso de tokens"
    Incluya `auth_token` en una cookie denominada `ouat` para solicitudes autenticadas posteriores.

## Crear usuario

**`POST user/create/`**

Crea una nueva cuenta de usuario.

**Privilegios**: Ninguno (punto final público)

**Parámetros:**
- `username` (cadena, requerida): Nombre de usuario
- `password` (cadena, requerida): Contraseña
- `email` (cadena, obligatoria): dirección de correo electrónico

**Respuesta:**
```json
{
  "status": "ok"
}
```
## Obtener perfil de usuario

**`GET user/profile/`**

Devuelve información del perfil del usuario.

**Privilegios**: Usuario registrado (perfil propio) o perfil público

**Respuesta:**
```json
{
  "username": "user123",
  "name": "User Name",
  "email": "user@example.com",
  "solved": 50,
  "submissions": 200,
  ...
}
```
## Documentación relacionada

- **[Guía de autenticación](authentication.md)** - Flujo de autenticación
- **[Descripción general de la API REST](rest-api.md)** - Información general de la API
