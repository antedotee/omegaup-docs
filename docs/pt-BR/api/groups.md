---
title: API de grupos
description: Endpoints de API para gerenciamento de grupos e painéis de avaliação de grupos
icon: bootstrap/account-group
---
# API de grupos

Os grupos permitem que você organize os usuários em conjunto para placares e concursos coletivos. Esta API fornece terminais para criação de grupos, gerenciamento de membros e manipulação de placares de grupo.

## Visão geral

Os grupos no omegaUp têm dois propósitos principais:

1. **Organização de usuários**: agrupe usuários para rastreamento e gerenciamento
2. **Painéis de avaliação**: crie placares personalizados que agregam resultados de vários concursos

## Pontos de extremidade do grupo

### Criar grupo

Cria um novo grupo. O usuário autenticado se torna o administrador do grupo.

**`POST /api/group/create/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Alias ​​de grupo exclusivo (usado em URLs) |
| `name` | corda | Sim | Nome de exibição do grupo |
| `description` | corda | Sim | Descrição do grupo |

**Resposta:**

```json
{
  "status": "ok"
}
```
**Privilégios:** Usuário autenticado (torna-se administrador)

---

### Atualizar grupo

Atualiza as informações de um grupo existente.

**`POST /api/group/update/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Alias ​​do grupo |
| `name` | corda | Sim | Novo nome de exibição |
| `description` | corda | Sim | Nova descrição |

**Privilégios:** Administrador do grupo

---

### Obtenha detalhes do grupo

Retorna informações detalhadas sobre um grupo, incluindo seus placares.

**`GET /api/group/details/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |

**Resposta:**

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
**Privilégios:** Administrador do grupo

---

### Listar grupos de usuários

Retorna todos os grupos administrados pelo usuário atual.

**`GET /api/group/myList/`**

**Resposta:**

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
**Privilégios:** Usuário autenticado

---

### Pesquisar grupos

Retorna grupos que correspondem a uma consulta de pesquisa. Usado para digitação antecipada.

**`GET /api/group/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `query` | corda | Sim | Termo de pesquisa |

**Resposta:**

```json
[
  {
    "label": "Group Name",
    "value": "group-alias"
  }
]
```
**Privilégios:** Usuário autenticado

---

### Obtenha membros do grupo

Retorna todos os membros de um grupo.

**`GET /api/group/members/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |

**Resposta:**

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
**Privilégios:** Administrador do grupo

---

### Adicionar usuário ao grupo

Adiciona um usuário a um grupo.

**`POST /api/group/addUser/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `usernameOrEmail` | corda | Sim | Nome de usuário ou e-mail do usuário a ser adicionado |

**Resposta:**

```json
{
  "status": "ok"
}
```
**Privilégios:** Administrador do grupo

**Erros:**

- `identityInGroup`: O usuário já é membro do grupo

---

### Remover usuário do grupo

Remove um usuário de um grupo.

**`POST /api/group/removeUser/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `usernameOrEmail` | corda | Sim | Nome de usuário ou e-mail do usuário a ser removido |

**Privilégios:** Administrador do grupo

---

### Criar placar

Cria um novo placar para um grupo.

**`POST /api/group/createScoreboard/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `alias` | corda | Sim | Alias ​​do placar |
| `name` | corda | Sim | Nome de exibição do placar |
| `description` | corda | Não | Descrição do placar |

**Privilégios:** Administrador do grupo

---

## Pontos finais do painel de avaliação do grupo

Os placares de grupo agregam resultados de vários concursos.

### Adicionar concurso ao placar

Adiciona um concurso a um placar de grupo.

**`POST /api/groupScoreboard/addContest/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `scoreboard_alias` | corda | Sim | Alias ​​do placar |
| `contest_alias` | corda | Sim | Concurso para adicionar |
| `weight` | flutuar | Sim | Peso para pontuação |
| `only_ac` | bool | Não | Contar apenas envios de AC |

**Privilégios:** Administrador do grupo + acesso ao concurso

---

### Remover concurso do placar

Remove uma competição de um placar de grupo.

**`POST /api/groupScoreboard/removeContest/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `scoreboard_alias` | corda | Sim | Alias ​​do placar |
| `contest_alias` | corda | Sim | Concurso para remover |

**Privilégios:** Administrador do grupo

---

### Obtenha detalhes do placar

Retorna detalhes do placar, incluindo classificação e concursos.

**`GET /api/groupScoreboard/details/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |
| `scoreboard_alias` | corda | Sim | Alias ​​do placar |

**Resposta:**

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
**Privilégios:** Administrador do grupo

---

### Listar placares de grupos

Retorna todos os placares de um grupo.

**`GET /api/groupScoreboard/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `group_alias` | corda | Sim | Alias ​​do grupo |

**Privilégios:** Administrador do grupo

---

## Casos de uso

### Criando um grupo de turma

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
## Documentação Relacionada

- **[API Teams](teams.md)** - Para gerenciar grupos de equipes
- **[API de concursos](contests.md)** - Criação de concursos para grupos
- **[API de usuários](users.md)** - Gerenciamento de usuários

## Referência completa

Para obter detalhes completos do endpoint, consulte o código-fonte do [Group Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Group.php) e do [GroupScoreboard Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/GroupScoreboard.php).
