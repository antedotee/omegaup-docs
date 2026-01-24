---
title: API de emblemas
description: Endpoints de API para o sistema de emblemas de conquistas
icon: bootstrap/award
---
# API de emblemas

Os emblemas são conquistas que os usuários ganham por diversas conquistas na plataforma. Esta API permite consultar crachás e propriedade de crachás do usuário.

## Visão geral

O sistema de emblemas no omegaUp recompensa os usuários por:

- Resolvendo problemas
- Participação em concursos
- Contribuições comunitárias
- Conquistas especiais

Os selos são atribuídos automaticamente por processos em segundo plano quando os usuários atendem aos critérios.

## Pontos finais

### Listar todos os emblemas

Retorna uma lista de todos os aliases de crachás disponíveis.

**`GET /api/badge/list/`**

**Resposta:**

```json
[
  "problemSetter",
  "contestParticipant",
  "100Problems",
  "firstAC"
]
```
**Privilégios:** Público (sem necessidade de autenticação)

---

### Obtenha os emblemas do usuário

Retorna todos os crachás pertencentes ao usuário autenticado atual.

**`GET /api/badge/myList/`**

**Resposta:**

```json
{
  "badges": [
    {
      "badge_alias": "firstAC",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 50000,
      "total_users": 100000
    }
  ]
}
```
**Privilégios:** Usuário autenticado

---

### Obtenha emblemas por nome de usuário

Retorna todos os emblemas pertencentes a um usuário específico.

**`GET /api/badge/userList/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `target_username` | corda | Sim | Nome de usuário a consultar |

**Resposta:**

```json
{
  "badges": [
    {
      "badge_alias": "problemSetter",
      "assignation_time": { "time": 1609459200 },
      "first_assignation": { "time": 1546300800 },
      "owners_count": 1500,
      "total_users": 100000
    }
  ]
}
```
**Privilégios:** Público

---

### Obtenha detalhes do selo

Retorna informações detalhadas sobre um selo específico.

**`GET /api/badge/badgeDetails/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `badge_alias` | corda | Sim | Alias ​​do emblema |

**Resposta:**

```json
{
  "badge_alias": "100Problems",
  "assignation_time": null,
  "first_assignation": { "time": 1546300800 },
  "owners_count": 2500,
  "total_users": 100000
}
```
**Campos:**

| Campo | Descrição |
|-------|------------|
| `badge_alias` | Identificador exclusivo do crachá |
| `assignation_time` | Quando o usuário atual o ganhou (nulo se não for de propriedade) |
| `first_assignation` | Quando o distintivo foi concedido pela primeira vez |
| `owners_count` | Número de usuários que possuem este selo |
| `total_users` | Total de utilizadores registados (para cálculo percentual) |

**Privilégios:** Público

---

### Obtenha o tempo de atribuição do crachá

Retorna quando o usuário atual ganhou um selo específico.

**`GET /api/badge/myBadgeAssignationTime/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `badge_alias` | corda | Sim | Alias ​​do emblema |

**Resposta:**

```json
{
  "assignation_time": { "time": 1609459200 }
}
```
Retorna `null` para `assignation_time` se o usuário não tiver o crachá.

**Privilégios:** Usuário autenticado

---

## Emblemas disponíveis

Os emblemas são definidos no diretório `frontend/badges/`. Cada emblema possui:

- Um alias exclusivo (nome da pasta)
- Um ícone (`icon.svg`)
- Descrições localizadas
- Critérios de atribuição (SQL ou baseados em código)

Categorias de emblemas comuns:

### Resolução de problemas
- `firstAC` - Primeiro envio aceito
- `100Problems` - Resolvido 100 problemas
- `legacyUser` - Usuário inicial da plataforma

### Participação no Concurso
- `contestParticipant` - Participou de um concurso
- `virtualContestParticipant` - Participou de um concurso virtual

### Criação de conteúdo
- `problemSetter` - Criou um problema público
- `problemSetterAdvanced` - Criou vários problemas de qualidade

### Comunidade
- `coderOfTheMonth` - Selecionado como codificador do mês

---

## Atribuição de emblema

Os emblemas são atribuídos automaticamente por:

1. **Cron jobs** – Verificações periódicas de critérios
2. **Acionadores de eventos** - Atribuição imediata de ações qualificadas

Os usuários não podem reivindicar emblemas manualmente.

---

## Casos de uso

### Exibir conquistas do usuário

```javascript
// Fetch user's badges for profile display
const response = await fetch('/api/badge/userList/?target_username=omegaup');
const { badges } = await response.json();

badges.forEach(badge => {
  console.log(`${badge.badge_alias}: ${badge.owners_count} owners`);
});
```
### Verifique a raridade do emblema

```javascript
// Calculate badge rarity percentage
const details = await fetch('/api/badge/badgeDetails/?badge_alias=100Problems');
const badge = await details.json();

const rarity = (badge.owners_count / badge.total_users * 100).toFixed(2);
console.log(`${rarity}% of users have this badge`);
```
---

## Documentação Relacionada

- **[API de usuários](users.md)** - Informações do perfil do usuário
- **[API de problemas](problems.md)** - Conquistas relacionadas a problemas
- **[API de concursos](contests.md)** - Conquistas relacionadas ao concurso

## Referência completa

Para definições completas de crachás e lógica de atribuição, consulte [Controlador de crachás](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Badge.php) e [diretório de crachás](https://github.com/omegaup/omegaup/tree/main/frontend/badges).
