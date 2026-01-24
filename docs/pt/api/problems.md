---
title: API de problemas
description: Endpoints de API para criação e gerenciamento de problemas
icon: bootstrap/puzzle
---
# API de problemas

Endpoints para criar, atualizar e gerenciar problemas de programação.

## Criar problema

**`POST problem/create/`**

Cria um novo problema.

**Privilégios**: Usuário logado

**Parâmetros:**
- `title` (string, obrigatório): Título do problema
- `alias` (string, obrigatório): Alias do problema
- `source` (string, opcional): Fonte do problema (por exemplo, "OMI 2020")
- `public` (int, obrigatório): 0 para privado, 1 para público
- `validator` (string, obrigatório): Tipo de validador (veja abaixo)
- `time_limit` (int, obrigatório): Limite de tempo em milissegundos
- `memory_limit` (int, obrigatório): Limite de memória em KB
- `problem_contents` (FILE, obrigatório): arquivo ZIP com conteúdo do problema

**Tipos de validador:**
- `literal`: correspondência exata
- `token`: comparação token por token
- `token-caseless`: comparação de token sem distinção entre maiúsculas e minúsculas
- `token-numeric`: Comparação numérica com tolerância
- `custom`: validador definido pelo usuário

**Resposta:**
```json
{
  "status": "ok",
  "uploaded_files": ["file1.in", "file1.out", ...]
}
```
## Obtenha detalhes do problema

**`GET problems/:problem_alias/details/`**

Retorna detalhes do problema dentro de um contexto de concurso.

**Privilégios**: Usuário logado; concursos privados exigem convite

**Parâmetros:**
- `contest_alias` (string, obrigatório): alias do concurso
- `lang` (string, opcional): Idioma (padrão: "es")

**Resposta:**
```json
{
  "title": "Problem Title",
  "author_id": 123,
  "validator": "token-numeric",
  "time_limit": 3000,
  "memory_limit": 65536,
  "visits": 1000,
  "submissions": 500,
  "accepted": 200,
  "difficulty": 5.5,
  "creation_date": "2020-01-01T00:00:00Z",
  "source": "OMI 2020",
  "runs": [...]
}
```
## Documentação Relacionada

- **[Criando Problemas](../../features/problems/creating-problems.md)** - Guia de criação de problemas
- **[Formato do problema](../../features/problems/problem-format.md)** - Estrutura do arquivo ZIP
- **[Visão geral da API REST](rest-api.md)** - Informações gerais da API
