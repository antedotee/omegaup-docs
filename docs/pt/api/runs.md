---
title: Executa API
description: Endpoints de tratamento de envio e recuperação de resultados
icon: bootstrap/play-circle
---
# Executa API

Endpoints para envio de código e recuperação de resultados de envio.

## Criar execução (enviar código)

**`POST runs/create/`**

Cria um novo envio para um problema em um concurso.

**Privilégios**: Usuário logado

**Parâmetros:**
- `problem_alias` (string, obrigatório): Alias do problema
- `contest_alias` (string, obrigatório): alias do concurso
- `language` (string, obrigatório): Linguagem de programação
- `source` (string, obrigatório): Código fonte

**Resposta:**
```json
{
  "status": "ok",
  "guid": "abc123def456..."
}
```
## Obtenha detalhes da execução

**`GET runs/:run_alias/details/`**

Retorna detalhes de um envio específico.

**Privilégios**: Usuário logado

**Resposta:**
```json
{
  "guid": "abc123def456...",
  "language": "cpp",
  "status": "ready",
  "verdict": "AC",
  "runtime": 150,
  "memory": 2048,
  "score": 1.0,
  "contest_score": 100,
  "time": 1436577101,
  "submit_delay": 30
}
```
## Obtenha a fonte da execução

**`GET runs/:run_alias/source/`**

Retorna o código-fonte de um envio. Se a compilação falhar, retornará um erro de compilação.

**Privilégios**: Usuário logado

**Resposta:**
```json
{
  "source": "#include <iostream>...",
  "compilation_error": null
}
```
## Executar valores de status

- `new`: recém criado
- `waiting`: Na fila
- `compiling`: Em fase de compilação
- `running`: Executando
- `ready`: Avaliação concluída

## Valores do veredicto

- `AC`: Aceito
- `PA`: parcialmente aceito
- `PE`: Erro de apresentação
- `WA`: Resposta errada
- `TLE`: Limite de tempo excedido
- `OLE`: Limite de saída excedido
- `MLE`: Limite de memória excedido
- `RTE`: Erro de tempo de execução
- `RFE`: Erro de função restrita
- `CE`: Erro de compilação
- `JE`: Erro do juiz

## Documentação Relacionada

- **[Visão geral da API REST](rest-api.md)** - Informações gerais da API
- **[Avaliador](../../features/grader.md)** - Sistema de avaliação
- **[Runner](../../features/runner.md)** - Execução de código
