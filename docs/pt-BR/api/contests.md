---
title: API de concursos
description: Endpoints de API para gerenciamento e participação em concursos
icon: bootstrap/trophy
---
# API de concursos

A API Contests fornece endpoints abrangentes para criar, gerenciar e participar de concursos de programação.

## Visão geral

Suporte para concursos omegaUp:

- **Vários formatos**: IOI, ICPC e pontuação personalizada
- **Tempo flexível**: duração fixa ou janelas estilo USACO
- **Controle de acesso**: público, privado ou baseado em registro
- **Concursos virtuais**: Pratique com condições de concursos anteriores

## Gerenciamento de concurso

### Criar concurso

Cria um novo concurso. O usuário autenticado torna-se o diretor do concurso.

**`POST /api/contest/create/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Alias ​​exclusivo do concurso (usado em URLs) |
| `title` | corda | Sim | Título do concurso |
| `description` | corda | Sim | Descrição do concurso |
| `start_time` | interno | Sim | Carimbo de data e hora de início (Unix) |
| `finish_time` | interno | Sim | Carimbo de data/hora final (Unix) |
| `admission_mode` | corda | Não | `public`, `private` ou `registration` |
| `score_mode` | corda | Não | `all_or_nothing`, `partial`, `max_per_group` |
| `scoreboard` | interno | Não | Visibilidade do placar (0-100%) |
| `window_length` | interno | Não | Janela estilo USACO em minutos |
| `submissions_gap` | interno | Não | Segundos mínimos entre envios |
| `penalty` | corda | Não | `none`, `runtime`, `submission_count` |
| `penalty_calc_policy` | corda | Não | `sum`, `max` |
| `feedback` | corda | Não | `detailed`, `summary`, `none` |
| `languages` | corda | Não | Lista de idiomas separados por vírgula |
| `show_scoreboard_after` | bool | Não | Mostrar placar após concurso |

**Resposta:**

```json
{
  "status": "ok"
}
```
---

### Concurso de atualização

Atualiza as configurações de um concurso existente.

**`POST /api/contest/update/`**

**Parâmetros:** O mesmo que criar, mais:

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Concurso para atualizar |

**Privilégios:** Administrador do concurso

---

### Concurso de Clones

Cria uma cópia de um concurso existente.

**`POST /api/contest/clone/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Concurso para clonar |
| `title` | corda | Sim | Novo título do concurso |
| `alias` | corda | Sim | Novo apelido do concurso |
| `description` | corda | Sim | Nova descrição |
| `start_time` | interno | Sim | Novo carimbo de data e hora de início |

---

### Concurso de Arquivo

Arquiva um concurso (oculta das listas ativas).

**`POST /api/contest/archive/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `archive` | bool | Sim | verdadeiro para arquivar, falso para desarquivar |

---

## Informações do Concurso

### Listar concursos

Retorna uma lista paginada de concursos.

**`GET /api/contest/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `page` | interno | Não | Número da página |
| `page_size` | interno | Não | Resultados por página |
| `query` | corda | Não | Termo de pesquisa |
| `tab_name` | corda | Não | `current`, `future`, `past` |
| `admission_mode` | corda | Não | Filtrar por modo de admissão |

**Resposta:**

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

### Meus concursos

Retorna concursos onde o usuário é administrador.

**`GET /api/contest/myList/`**

---

### Listar concursos participantes

Retorna concursos dos quais o usuário está participando.

**`GET /api/contest/listParticipating/`**

---

### Obtenha detalhes do concurso

Retorna informações completas do concurso.

**`GET /api/contest/details/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |

**Resposta:**

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

### Obtenha detalhes do administrador

Retorna informações específicas do administrador do concurso.

**`GET /api/contest/adminDetails/`**

**Privilégios:** Administrador do concurso

---

### Obtenha detalhes públicos

Retorna informações do concurso visíveis publicamente.

**`GET /api/contest/publicDetails/`**

---

## Gerenciamento de Problemas

### Adicionar problema

Adiciona um problema a um concurso.

**`POST /api/contest/addProblem/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `problem_alias` | corda | Sim | Problema para adicionar |
| `points` | flutuar | Sim | Valor em pontos |
| `order_in_contest` | interno | Não | Ordem de exibição |
| `commit` | corda | Não | Versão específica do problema |

**Privilégios:** Administrador do concurso

---

### Remover problema

Remove um problema de um concurso.

**`POST /api/contest/removeProblem/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `problem_alias` | corda | Sim | Problema para remover |

**Privilégios:** Administrador do concurso

---

### Listar problemas

Retorna todos os problemas de um concurso.

**`GET /api/contest/problems/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |

---

## Gerenciamento de usuários e acesso

### Adicionar usuário

Adiciona um usuário a um concurso privado.

**`POST /api/contest/addUser/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `usernameOrEmail` | corda | Sim | Usuário a ser adicionado |

**Privilégios:** Administrador do concurso

---

### Remover usuário

Remove um usuário de um concurso.

**`POST /api/contest/removeUser/`**

---

### Adicionar grupo

Concede acesso ao concurso a um grupo inteiro.

**`POST /api/contest/addGroup/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `group` | corda | Sim | Alias ​​do grupo |

---

### Remover grupo

**`POST /api/contest/removeGroup/`**

---

### Listar usuários

Retorna todos os usuários com acesso ao concurso.

**`GET /api/contest/users/`**

---

### Listar concorrentes

Retorna os participantes reais do concurso.

**`GET /api/contest/contestants/`**

---

### Pesquisar usuários

Pesquisa usuários para adicionar ao concurso.

**`GET /api/contest/searchUsers/`**

---

## Gerenciamento administrativo

### Adicionar administrador

Concede privilégios de administrador a um usuário.

**`POST /api/contest/addAdmin/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `usernameOrEmail` | corda | Sim | Novo administrador |

---

### Remover administrador

**`POST /api/contest/removeAdmin/`**

---

### Adicionar administrador do grupo

Concede administração a todos os membros do grupo.

**`POST /api/contest/addGroupAdmin/`**

---

### Remover administrador do grupo

**`POST /api/contest/removeGroupAdmin/`**

---

### Listar administradores

Retorna todos os administradores do concurso.

**`GET /api/contest/admins/`**

---

## Participação

### Concurso Aberto

Abre um concurso para o usuário (inicia seu cronômetro no modo USACO).

**`POST /api/contest/open/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |

---

### Inscreva-se no concurso

Registra-se em um concurso baseado em registro.

**`POST /api/contest/registerForContest/`**

---

### Obtenha a função do usuário

Retorna a função do usuário em um concurso.

**`GET /api/contest/role/`**

**Resposta:**

```json
{
  "admin": false,
  "contestant": true,
  "reviewer": false
}
```
---

### Criar concurso virtual

Cria um concurso virtual (prático) a partir de um concurso anterior.

**`POST /api/contest/createVirtual/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `alias` | corda | Sim | Apelido original do concurso |
| `start_time` | interno | Sim | Hora de início virtual |

---

## Placar

### Obter placar

Retorna o placar atual.

**`GET /api/contest/scoreboard/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `token` | corda | Não | Token do placar (para URLs compartilhados) |

**Resposta:**

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

### Obtenha eventos do placar

Retorna eventos de alteração do placar (para animações).

**`GET /api/contest/scoreboardEvents/`**

---

### Mesclar placares

Mescla placares de vários concursos.

**`GET /api/contest/scoreboardMerge/`**

---

## Execuções e envios

### Listar execuções

Retorna envios para um concurso.

**`GET /api/contest/runs/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `problem_alias` | corda | Não | Filtrar por problema |
| `username` | corda | Não | Filtrar por usuário |
| `status` | corda | Não | Filtrar por status |
| `verdict` | corda | Não | Filtrar por veredicto |
| `language` | corda | Não | Filtrar por idioma |
| `offset` | interno | Não | Deslocamento de paginação |
| `rowcount` | interno | Não | Resultados por página |

---

### Executa diferença

Retorna diferenças entre execuções.

**`GET /api/contest/runsDiff/`**

---

## Esclarecimentos

### Obtenha esclarecimentos

Retorna esclarecimentos do concurso.

**`GET /api/contest/clarifications/`**

---

### Obtenha esclarecimentos sobre problemas

Retorna esclarecimentos sobre um problema específico.

**`GET /api/contest/problemClarifications/`**

---

## Relatórios e estatísticas

### Relatório de atividades

Retorna a atividade do usuário durante o concurso.

**`GET /api/contest/activityReport/`**

**Privilégios:** Administrador do concurso

---

### Relatório do Concurso

Retorna relatório detalhado do concurso.

**`GET /api/contest/report/`**

**Privilégios:** Administrador do concurso

---

### Estatísticas do Concurso

Retorna estatísticas do concurso.

**`GET /api/contest/stats/`**

---

### Obtenha o número de concorrentes

**`GET /api/contest/getNumberOfContestants/`**

---

## Solicitações (baseadas em registro)

### Listar solicitações

Retorna solicitações de registro.

**`GET /api/contest/requests/`**

**Privilégios:** Administrador do concurso

---

### Solicitação de Arbitragem

Aprova ou nega uma solicitação de registro.

**`POST /api/contest/arbitrateRequest/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `username` | corda | Sim | Usuário solicitante |
| `resolution` | bool | Sim | verdadeiro=aprovar, falso=negar |
| `note` | corda | Não | Nota opcional |

---

## Integração de equipes

### Substituir grupo de equipes

Substitui o grupo de equipes por uma competição por equipes.

**`POST /api/contest/replaceTeamsGroup/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `teams_group_alias` | corda | Sim | Novo grupo de equipes |

---

## Outras operações

### Definir recomendado

Marca um concurso como recomendado (apenas para funcionários).

**`POST /api/contest/setRecommended/`**

---

### Atualizar horário de término da identidade

Prolonga o tempo para um usuário específico (acomodações).

**`POST /api/contest/updateEndTimeForIdentity/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `contest_alias` | corda | Sim | Apelido do concurso |
| `username` | corda | Sim | Usuário a estender |
| `end_time` | interno | Sim | Novo carimbo de data/hora final |

---

## Modos de concurso

### Modos de Admissão

| Modo | Descrição |
|------|-------------|
| `public` | Qualquer pessoa pode participar |
| `private` | Somente convite |
| `registration` | Os usuários devem solicitar acesso |

### Modos de pontuação

| Modo | Descrição |
|------|-------------|
| `all_or_nothing` | Pontos completos apenas para AC |
| `partial` | Pontos parciais por caso de teste |
| `max_per_group` | Máximo por grupo de teste |

### Modos de Penalidade

| Modo | Descrição |
|------|-------------|
| `none` | Sem penalidade |
| `runtime` | Penalidade total de tempo de execução |
| `submission_count` | Penalidade por envio errado |

---

## Documentação Relacionada

- **[Executa API](runs.md)** - Gerenciamento de envios
- **[API de problemas](problems.md)** - Gerenciamento de problemas
- **[API de esclarecimentos](clarifications.md)** - Perguntas e respostas do concurso
- **[API de grupos](groups.md)** - Gerenciamento de grupos

## Referência completa

Para obter detalhes completos de implementação, consulte o código-fonte do [Contest Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Contest.php).
