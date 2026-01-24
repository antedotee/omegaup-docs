---
title: API de usuários
description: Endpoints de gerenciamento e autenticação de usuários
icon: bootstrap/account-group
---
# API de usuários

Endpoints para gerenciamento de usuários, autenticação e operações de perfil.

## Login

**`POST user/login/`**

Autentica um usuário e retorna um token de autenticação.

**Privilégios**: Nenhum (endpoint público)

**Parâmetros:**
- `usernameOrEmail` (string, obrigatório): Nome de usuário ou e-mail
- `password` (string, obrigatório): Senha do usuário

**Resposta:**
```json
{
  "status": "ok",
  "auth_token": "abc123def456..."
}
```
!!! importante "Uso de token"
    Inclua `auth_token` em um cookie chamado `ouat` para solicitações autenticadas subsequentes.

## Criar usuário

**`POST user/create/`**

Cria uma nova conta de usuário.

**Privilégios**: Nenhum (endpoint público)

**Parâmetros:**
- `username` (string, obrigatório): Nome de usuário
- `password` (string, obrigatório): Senha
- `email` (string, obrigatório): Endereço de e-mail

**Resposta:**
```json
{
  "status": "ok"
}
```
## Obtenha o perfil do usuário

**`GET user/profile/`**

Retorna informações de perfil do usuário.

**Privilégios**: Usuário logado (perfil próprio) ou perfil público

**Resposta:**
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
## Documentação Relacionada

- **[Guia de autenticação](authentication.md)** - Fluxo de autenticação
- **[Visão geral da API REST](rest-api.md)** - Informações gerais da API
