---
title: API de esclarecimentos
description: Pontos finais de esclarecimento do concurso
icon: bootstrap/help-circle
---
# API de esclarecimentos

Pontos finais para fazer e responder perguntas durante concursos.

## Criar Esclarecimento

**`POST clarification/create/`**

Cria um novo esclarecimento para um problema em um concurso. Os esclarecimentos são privados por padrão.

**Privilégios**: Usuário logado

**Parâmetros:**
- `contest_alias` (string, obrigatório): alias do concurso
- `problem_alias` (string, obrigatório): Alias do problema
- `message` (string, obrigatório): Mensagem de esclarecimento

**Resposta:**
```json
{
  "status": "ok",
  "clarification_id": 123
}
```
## Obtenha detalhes de esclarecimento

**`GET clarification/:clarification_id/details/`**

Retorna detalhes de um esclarecimento específico.

**Privilégios**: Usuário logado com acesso ao concurso

**Resposta:**
```json
{
  "message": "Question text",
  "answer": "Answer text",
  "time": "2020-01-01T12:00:00Z",
  "problem_id": 456,
  "contest_id": 789
}
```
## Atualização de esclarecimento

**`POST clarification/:clarification_id/update/`**

Atualiza um esclarecimento (normalmente para adicionar uma resposta ou torná-la pública).

**Privilégios**: Administrador do concurso ou superior

**Parâmetros:**
- `contest_alias` (string, opcional): alias do concurso
- `problem_alias` (string, opcional): Alias do problema
- `message` (string, opcional): Mensagem atualizada
- `answer` (string, opcional): Resposta ao esclarecimento
- `public` (int, opcional): Tornar o esclarecimento público (0 ou 1)

**Resposta:**
```json
{
  "status": "ok"
}
```
## Documentação Relacionada

- **[Visão geral da API REST](rest-api.md)** - Informações gerais da API
- **[API de concursos](contests.md)** - Gerenciamento de concursos
- **[Arena](../../features/arena.md)** - Interface do concurso
