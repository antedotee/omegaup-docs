---
title: Referência de códigos de erro
description: Referência completa de códigos de erro de API e seus significados
icon: bootstrap/help-circle
---
# Referência de códigos de erro

Esta página documenta todos os códigos de erro retornados pela API omegaUp, seus códigos de status HTTP e causas comuns.

## Formato de resposta de erro

Todos os erros da API seguem este formato:

```json
{
  "status": "error",
  "error": "Human-readable error message",
  "errorname": "errorKeyName",
  "errorcode": 400,
  "header": "HTTP/1.1 400 BAD REQUEST",
  "parameter": "field_name"
}
```
| Campo | Descrição |
|-------|------------|
| `status` | Sempre `"error"` para respostas de erro |
| `error` | Mensagem localizada e legível por humanos |
| `errorname` | Chave de erro legível por máquina |
| `errorcode` | Código de status HTTP |
| `header` | Cabeçalho de resposta HTTP completo |
| `parameter` | (Opcional) Parâmetro que causou o erro |

---

## Códigos de status HTTP

### 400 Solicitação incorreta

Entrada inválida ou erros de parâmetro.

| Nome do erro | Descrição |
|------------|-------------|
| `parameterEmpty` | O parâmetro obrigatório está vazio |
| `parameterInvalid` | O valor do parâmetro é inválido |
| `parameterNotFound` | Entidade referenciada não encontrada |
| `parameterStringTooLong` | String excede o comprimento máximo |
| `parameterStringTooShort` | String abaixo do comprimento mínimo |
| `parameterNumberTooSmall` | Número abaixo do valor mínimo |
| `parameterNumberTooLarge` | Número excede valor máximo |
| `invalidAlias` | Formato de alias inválido |
| `aliasInUse` | O alias já existe |

**Exemplo:**

```json
{
  "status": "error",
  "error": "problem_alias: Parameter is invalid",
  "errorname": "parameterInvalid",
  "errorcode": 400,
  "parameter": "problem_alias"
}
```
---

### 401 Não autorizado

Autenticação necessária ou inválida.

| Nome do erro | Descrição |
|------------|-------------|
| `loginRequired` | O usuário deve estar logado |
| `invalidCredentialsException` | Nome de usuário/senha errados |
| `emailNotVerified` | Verificação de e-mail pendente |

**Exemplo:**

```json
{
  "status": "error",
  "error": "Login required",
  "errorname": "loginRequired",
  "errorcode": 401
}
```
---

### 403 Proibido

Autenticado, mas não autorizado.

| Nome do erro | Descrição |
|------------|-------------|
| `userNotAllowed` | O usuário não tem permissão |
| `forbiddenInLockdown` | Sistema em modo de bloqueio |
| `contestNotStarted` | O concurso ainda não começou |
| `contestEnded` | O concurso terminou |
| `cannotSubmit` | O usuário não pode enviar |

**Exemplo:**

```json
{
  "status": "error",
  "error": "User is not allowed to perform this action",
  "errorname": "userNotAllowed",
  "errorcode": 403
}
```
---

### 404 não encontrado

O recurso solicitado não existe.

| Nome do erro | Descrição |
|------------|-------------|
| `contestNotFound` | O concurso não existe |
| `problemNotFound` | O problema não existe |
| `userNotExist` | O usuário não existe |
| `courseNotFound` | O curso não existe |
| `groupNotFound` | O grupo não existe |
| `schoolNotFound` | A escola não existe |
| `qualityNominationNotFound` | Nomeação não existe |

**Exemplo:**

```json
{
  "status": "error",
  "error": "Problem not found",
  "errorname": "problemNotFound",
  "errorcode": 404
}
```
---

### 409 Conflito

Conflito de estado de recurso.

| Nome do erro | Descrição |
|------------|-------------|
| `duplicatedEntryInDatabase` | O registro já existe |
| `identityInGroup` | Usuário já no grupo |
| `teamMemberUsernameInUse` | Membro da equipe já atribuído |

**Exemplo:**

```json
{
  "status": "error",
  "error": "User is already a member of this group",
  "errorname": "identityInGroup",
  "errorcode": 409
}
```
---

### 412 Falha na pré-condição

Restrição de lógica de negócios não atendida.

| Nome do erro | Descrição |
|------------|-------------|
| `qualityNominationMustHaveSolvedProblem` | Deve resolver antes de nomear |
| `qualityNominationMustNotHaveSolvedProblem` | Não deve ter resolvido (para before_ac) |
| `qualityNominationMustHaveTriedToSolveProblem` | Deve ter tentado problema |
| `contestCertificatesError` | Erro de geração de certificado |
| `contestCertificatesCurrentContestError` | O concurso não terminou |

---

### 429 Muitas solicitações

Limite de taxa excedido.

| Nome do erro | Descrição |
|------------|-------------|
| `rateLimitExceeded` | Muitas solicitações de API |
| `submissionWaitGap` | Limite de taxa de envio |

**Cabeçalhos incluídos:**

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1704070800
Retry-After: 3600
```
---

### 500 Erro interno do servidor

Erros do lado do servidor.

| Nome do erro | Descrição |
|------------|-------------|
| `generalError` | Erro inesperado do servidor |
| `databaseOperationError` | Falha na consulta ao banco de dados |

---

### 503 Serviço indisponível

Serviço temporariamente indisponível.

| Nome do erro | Descrição |
|------------|-------------|
| `serviceUnavailable` | Serviço temporariamente indisponível |

---

## Cenários de erros comuns

### Erros de autenticação

```json
// Wrong password
{
  "errorname": "invalidCredentialsException",
  "errorcode": 401
}

// Not logged in
{
  "errorname": "loginRequired", 
  "errorcode": 401
}

// Email not verified
{
  "errorname": "emailNotVerified",
  "errorcode": 401
}
```
### Erros de validação

```json
// Missing required field
{
  "errorname": "parameterEmpty",
  "parameter": "name",
  "errorcode": 400
}

// Invalid format
{
  "errorname": "parameterInvalid",
  "parameter": "email",
  "errorcode": 400
}

// Alias taken
{
  "errorname": "aliasInUse",
  "errorcode": 400
}
```
### Erros de permissão

```json
// Not contest admin
{
  "errorname": "userNotAllowed",
  "errorcode": 403
}

// Contest not open yet
{
  "errorname": "contestNotStarted",
  "errorcode": 403
}
```
---

## Práticas recomendadas para tratamento de erros

### Tratamento do lado do cliente

```javascript
async function makeAPICall(endpoint, data) {
  const response = await fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  
  if (result.status === 'error') {
    switch (result.errorcode) {
      case 401:
        // Redirect to login
        window.location.href = '/login/';
        break;
      case 403:
        // Show permission error
        alert(result.error);
        break;
      case 404:
        // Resource not found
        showNotFoundMessage(result.error);
        break;
      case 429:
        // Rate limited - retry after delay
        const retryAfter = response.headers.get('Retry-After');
        setTimeout(() => makeAPICall(endpoint, data), retryAfter * 1000);
        break;
      default:
        // Generic error handling
        console.error(result.error);
    }
    return null;
  }
  
  return result;
}
```
### Verificando erros específicos

```javascript
if (result.errorname === 'aliasInUse') {
  // Suggest alternative alias
  suggestAlternative(data.alias);
}
```
---

## Localização

As mensagens de erro são localizadas com base na preferência de idioma do usuário. O campo `errorname` permanece constante em todas as linguagens para manipulação programática.

| Idioma | Exemplo de valor `error` |
|----------|----------------------|
| Inglês | "Login necessário" |
| Espanhol | "Início de sessão necessário" |
| Português | "Login necessário" |

---

## Documentação Relacionada

- **[Referência da API](index.md)** - Visão geral da API
- **[Autenticação](authentication.md)** - Fluxo de autenticação e erros

## Referência completa

Para obter a lista completa de classes de exceção, consulte o [diretório de exceções](https://github.com/omegaup/omegaup/tree/main/frontend/server/src/Exceptions) no código-fonte.
