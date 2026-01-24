---
title: API Escolas
description: Endpoints de API para gerenciamento e classificações escolares
icon: bootstrap/school
---
# API de escolas

A API Schools fornece endpoints para gerenciar escolas, visualizar classificações escolares e o programa Escola do Mês.

## Visão geral

Escolas em omegaUp:

- Rastreie afiliações de usuários
- Contribuir para classificações escolares com base na atividade dos membros
- Participe do programa Escola do Mês

## Pontos finais

### Listar escolas

Pesquisa escolas que correspondem a uma consulta. Usado para digitação antecipada/preenchimento automático.

**`GET /api/school/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `query` | corda | Sim* | Termo de pesquisa |
| `term` | corda | Sim* | Parâmetro de pesquisa alternativo |

*É necessário um dos `query` ou `term`.

**Resposta:**

```json
{
  "results": [
    {
      "key": 123,
      "value": "Massachusetts Institute of Technology"
    },
    {
      "key": 456,
      "value": "Stanford University"
    }
  ]
}
```
**Privilégios:** Usuário autenticado

---

### Criar escola

Cria uma nova entrada escolar.

**`POST /api/school/create/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `name` | corda | Sim | Nome da escola |
| `country_id` | corda | Não | Código do país (por exemplo, "MX", "US") |
| `state_id` | corda | Não | Código do estado/província |

**Resposta:**

```json
{
  "school_id": 789
}
```
**Notas:**

- Se existir uma escola com o mesmo nome, retorna o ID escolar existente
- O estado exige que o país seja especificado

**Privilégios:** Usuário autenticado

---

### Selecione a escola do mês

Seleciona uma escola como a Escola do Mês (somente mentor).

**`POST /api/school/selectSchoolOfTheMonth/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `school_id` | interno | Sim | ID escolar para selecionar |

**Resposta:**

```json
{
  "status": "ok"
}
```
**Privilégios:** Função de mentor

**Requisitos:**

- Deve estar dentro do período de seleção
- A escola deve estar na lista de candidatos
- Não é possível selecionar se já estiver selecionado para o mês

---

## Dados do perfil da escola

Os perfis escolares incluem:

### Informações Básicas

- Nome da escola
- Localização (país, estado)
- Classificação global

### Estatísticas

- Contagem mensal de problemas resolvidos
- Codificadores do Mês da escola
- Usuários ativos e suas conquistas

---

## Classificações escolares

As escolas são classificadas com base em:

1. **Pontuação**: Agregado de atividades dos membros
2. **Problemas Resolvidos**: Total de problemas resolvidos pelos membros
3. **Usuários Ativos**: Número de membros contribuintes

As classificações são armazenadas em cache e atualizadas periodicamente.

---

## Escola do Mês

### Visão geral do programa

A cada mês, uma escola é selecionada como "Escola do Mês" com base em:

- Atividade dos membros e resolução de problemas
- Participação no concurso
- Contribuições de qualidade

### Processo Seletivo

1. Sistema gera candidatos com base na atividade
2. Os mentores podem selecionar candidatos durante o período de seleção
3. O candidato ao primeiro lugar é selecionado por padrão se não houver seleção de mentor

### Dados do Candidato

```json
{
  "candidatesToSchoolOfTheMonth": [
    {
      "school_id": 123,
      "name": "Top University",
      "country_id": "MX",
      "ranking": 1,
      "score": 1500.5,
      "school_of_the_month_id": 456
    }
  ]
}
```
---

## Campos de perfil da escola

| Campo | Tipo | Descrição |
|-------|------|-------------|
| `school_id` | interno | Identificador único |
| `name` | corda | Nome da escola |
| `country_id` | corda | Código do país |
| `ranking` | interno | Posição no ranking global |
| `score` | flutuar | Pontuação de atividade calculada |

---

## Casos de uso

### Registro de usuário na escola

```javascript
// Search for school
const schools = await fetch('/api/school/list/?query=MIT');
const results = await schools.json();

// Use school_id (key) in user profile
const schoolId = results.results[0].key;
```
### Criar nova escola

```bash
curl -X POST https://omegaup.com/api/school/create/ \
  -d "name=New Tech University&country_id=US&state_id=CA"
```
---

## Dados relacionados

### Problemas resolvidos mensalmente

Acompanhe a atividade escolar ao longo do tempo:

```json
{
  "monthly_solved_problems": [
    { "year": 2024, "month": 1, "problems_solved": 150 },
    { "year": 2024, "month": 2, "problems_solved": 175 }
  ]
}
```
### Usuários escolares

Principais colaboradores de uma escola:

```json
{
  "school_users": [
    {
      "username": "top_coder",
      "classname": "user-rank-master",
      "created_problems": 10,
      "solved_problems": 500,
      "organized_contests": 5
    }
  ]
}
```
---

## Documentação Relacionada

- **[API de usuários](users.md)** - Perfil do usuário e associação escolar
- **[API de problemas](problems.md)** - Estatísticas de resolução de problemas

## Referência completa

Para obter detalhes completos de implementação, consulte o código-fonte do [School Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/School.php).
