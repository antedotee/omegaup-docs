---
title: API de equipes
description: Endpoints de API para gerenciar grupos de equipes e competições de equipes
icon: bootstrap/account-group
---
# API de equipes

A API Teams permite criar e gerenciar grupos de equipes para competições baseadas em equipes. Equipes são grupos de usuários que competem juntos como uma única unidade.

## Visão geral

Os grupos de equipe no omegaUp permitem:

- **Competições em equipe**: vários usuários resolvendo problemas juntos
- **Tamanho da equipe configurável**: 1 a 10 competidores por equipe
- **Gerenciamento de identidade da equipe**: cada equipe tem sua própria identidade

## Pontos finais do grupo de equipe

### Criar grupo de equipe

Cria um novo grupo de equipe. O usuário autenticado se torna o administrador.

**`POST /api/teamsGroup/create/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Alias ​​exclusivas do grupo de equipe |
| `name` | corda | Sim | Nome de exibição |
| `description` | corda | Sim | Descrição |
| `numberOfContestants` | interno | Não | Tamanho da equipe (padrão: 3, máximo: 10) |

**Resposta:**

```json
{
  "status": "ok"
}
```
**Privilégios:** Usuário autenticado (13+)

---

### Atualizar grupo de equipe

Atualiza um grupo de equipe existente.

**`POST /api/teamsGroup/update/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Apelido do grupo de equipe |
| `name` | corda | Sim | Novo nome de exibição |
| `description` | corda | Sim | Nova descrição |
| `numberOfContestants` | interno | Sim | Tamanho da equipe (1-10) |

**Privilégios:** Administrador do grupo da equipe

---

### Obtenha detalhes do grupo da equipe

Retorna informações detalhadas sobre um grupo de equipe.

**`GET /api/teamsGroup/details/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | Apelido do grupo de equipe |

**Resposta:**

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
**Privilégios:** Administrador do grupo da equipe

---

### Listar grupos de equipes

Retorna grupos de equipes que correspondem a uma consulta de pesquisa.

**`GET /api/teamsGroup/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `query` | corda | Sim | Termo de pesquisa |

**Resposta:**

```json
[
  {
    "key": "icpc-team-2024",
    "value": "ICPC Team 2024"
  }
]
```
**Privilégios:** Usuário autenticado

---

### Listar equipes no grupo

Retorna todas as equipes (identidades) em um grupo de equipes.

**`GET /api/teamsGroup/teams/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | Apelido do grupo de equipe |

**Resposta:**

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
**Privilégios:** Administrador do grupo da equipe

---

### Remover equipe

Remove uma equipe de um grupo de equipes.

**`POST /api/teamsGroup/removeTeam/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | Apelido do grupo de equipe |
| `usernameOrEmail` | corda | Sim | Nome de usuário da equipe a ser removido |

**Privilégios:** Administrador do grupo da equipe

---

## Pontos finais dos membros da equipe

### Adicionar membros à equipe

Adiciona um ou mais usuários a uma equipe específica.

**`POST /api/teamsGroup/addMembers/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | O nome de usuário da equipe (por exemplo, `team:group:teamname`) |
| `usernames` | corda | Sim | Lista de nomes de usuário separados por vírgula |

**Resposta:**

```json
{
  "status": "ok"
}
```
**Privilégios:** Administrador do grupo da equipe

**Erros:**

- `teamMemberUsernameInUse`: O membro já está em uma equipe

---

### Remover membro da equipe

Remove um membro de uma equipe.

**`POST /api/teamsGroup/removeMember/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | O nome de usuário da equipe |
| `username` | corda | Sim | Nome de usuário do membro a ser removido |

**Privilégios:** Administrador do grupo da equipe

---

### Listar membros da equipe

Retorna todos os membros de todas as equipes de um grupo de equipes.

**`GET /api/teamsGroup/teamsMembers/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `team_group_alias` | corda | Sim | Apelido do grupo de equipe |
| `page` | interno | Não | Número da página (padrão: 1) |
| `page_size` | interno | Não | Resultados por página (padrão: 100) |

**Resposta:**

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
**Privilégios:** Administrador do grupo da equipe

---

## Formato de nome de usuário da equipe

As equipes têm um formato de nome de usuário especial:

```
team:{team_group_alias}:{team_name}
```
Por exemplo: `team:icpc-2024:alpha`

Este nome de usuário é usado para:
- Faça login como equipe
- Referência da equipe em chamadas de API
- Exibição em placares

---

## Configuração

### Limites de tamanho da equipe

- **Tamanho padrão da equipe**: 3 competidores
- **Tamanho máximo da equipe**: 10 competidores
- O tamanho da equipe é configurado por grupo de equipe

---

## Casos de uso

### Configurando uma competição estilo ICPC

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

## Documentação Relacionada

- **[API de grupos](groups.md)** - Para grupos de usuários regulares
- **[API de concursos](contests.md)** - Criação de concursos de equipe
- **[Autenticação](authentication.md)** - Fluxo de login da equipe

## Referência completa

Para obter detalhes completos do endpoint, consulte o código-fonte do [TeamsGroup Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/TeamsGroup.php).
