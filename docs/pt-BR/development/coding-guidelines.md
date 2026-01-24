---
title: Diretrizes de codificação
description: Padrões de codificação e práticas recomendadas para desenvolvimento do omegaUp
icon: bootstrap/code
---
# Diretrizes de codificação

Este documento descreve os padrões de codificação e as melhores práticas para contribuir com o omegaUp. Essas diretrizes são aplicadas por linters automatizados e testes de integração.

## Princípios Gerais

### Digite Segurança

Todo código deve declarar tipos de dados em parâmetros de função e tipos de retorno:

- **TypeScript** para front-end (`frontend/www/`)
- **Salmo** para PHP (`frontend/server/`)
- **mypy** para Python (`stuff/`)

!!! dica "Anotações de tipo"
    Prefira anotações de tipo para arrays/mapas dentro de funções para tornar o código mais fácil de entender.

### Idioma

- Todos os códigos e comentários são escritos em **Inglês**

### Teste

- Mudanças de funcionalidade deverão ser acompanhadas de testes
- Todos os testes devem passar 100% antes de serem confirmados
- Sem exceções

### Qualidade do código

- Evite `null` e `undefined` sempre que possível
- Use [Padrão de cláusula de proteção](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html)
- Remova o código não utilizado (não comente - use o histórico do git)
- Minimize a distância entre a declaração da variável e o primeiro uso

### Convenções de nomenclatura

- **camelCase** para funções, variáveis e classes
- **snake_case** exceções:
  - Nomes de colunas MySQL
  - Variáveis ​​e parâmetros Python
  - Parâmetros API

!!! aviso "Abreviaturas"
    Evite abreviações no código e nos comentários. Eles não são óbvios para todos.

## Formatação de código

Delegamos a formatação para ferramentas automatizadas:

- **[yapf](https://github.com/google/yapf)** para Python
- **[prettier.io](https://prettier.io/)** para TypeScript/Vue
- **[phpcbf](https://github.com/squizlabs/PHP_CodeSniffer)** para PHP

Valide o estilo com:

```bash
./stuff/lint.sh validate
```
### Diretrizes de estilo

- Use espaços 2/4 (depende do tipo de arquivo), não tabulações
- Terminações de linha no estilo Unix (`\n`), não Windows (`\r\n`)
- Abrindo colchetes na mesma linha da instrução
- Espaço entre palavras-chave e parênteses: `if`, `else`, `while`, `switch`, `catch`, `function`
- Sem espaço antes dos parênteses de chamada de função
- Sem espaços entre parênteses
- Espaço depois da vírgula, não antes
- Operadores binários: espaço antes e depois
- Máximo de uma linha em branco seguida
- Sem comentários vazios
- Somente comentários de linha `//`, sem comentários de bloco `/* */`

## Diretrizes PHP

### Teste

```php
// Tests must pass 100% before committing
// All functionality changes need tests
```
### Consultas de banco de dados

Evite consultas O(n). Crie consultas manuais para viagens únicas de ida e volta:

```php
// ❌ Bad: Multiple queries
foreach ($users as $user) {
    $runs = RunsDAO::searchByUserId($user->userId);
}

// ✅ Good: Single query
$runs = RunsDAO::searchByUserIds(array_map(fn($u) => $u->userId, $users));
```
### Parâmetros de Função

As funções API são as únicas que podem receber `\OmegaUp\Request`. Todas as outras funções devem:

1. Valide os parâmetros
2. Extraia para variáveis digitadas
3. Chame funções com essas variáveis

### Documentação de função

Todas as funções devem ser documentadas:

```php
/**
 * set
 *
 * If cache is on, save value in key with given timeout
 *
 * @param string $value
 * @param int $timeout
 * @return boolean
 */
public function set($value, $timeout) { ... }
```
### Exceções

Use exceções para relatar erros. Funções que retornam verdadeiro/falso são permitidas quando representam valores esperados.

### Respostas da API

Todas as APIs devem retornar matrizes associativas.

## Diretrizes Vue.js

### Comportamento do Componente

Evite componentes que alteram significativamente o comportamento com base em sinalizadores. Use `slot`s em vez disso:

```vue
<!-- ✅ Good: Using slots for customization -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```
### Internacionalização

Nunca codifique o texto. Sempre use strings de tradução:

```typescript
// ❌ Bad: Hardcoded text
<div>Contest ranking: {% raw %}{{ user.rank }}{% endraw %}</div>

// ✅ Good: Translation string
<div>{% raw %}{{ T.contestRanking }}{% endraw %}</div>
```
!!! dica "Formatação de String"
    Evite concatenar strings de tradução. Use `ui.formatString()` com parâmetros.

### Cores

Evite cores hexadecimais ou `rgb()`. Use variáveis ​​CSS para suporte ao modo escuro.

### Ganchos de ciclo de vida

Evite ganchos de ciclo de vida, a menos que interaja diretamente com o DOM. A interação direta do DOM também deve ser evitada.

### Propriedades computadas

Prefira propriedades computadas e observadores à manipulação de variáveis programáticas.

### Livro de histórias

Adicione histórias do Storybook para novos componentes. Atualize histórias ao modificar componentes existentes.

## Diretrizes do TypeScript

### Parâmetros de Função

Quando uma função tiver mais de 2 a 3 parâmetros, especialmente do mesmo tipo, use um objeto:

```typescript
// ❌ Bad: Too many parameters
function updateProblem(
  problem: Problem,
  previousVersion: string,
  currentVersion: string,
  points?: int
): void { ... }

// ✅ Good: Object parameter
function updateProblem({
  problem,
  previousVersion,
  currentVersion,
  points,
}: {
  problem: Problem;
  previousVersion: string;
  currentVersion: string;
  points?: int;
}): void { ... }
```
### Asserções de tipo

Evite asserções de tipo, exceto para:
- Interações DOM (`document.querySelector`)
- Declarações vazias de tipo literal: `null as null | string`
- Teste: declarando `params` no construtor Vue

### descontinuação do jQuery

`jQuery` foi descontinuado e não pode ser usado.

## Diretrizes Python

### Parâmetros de Função

Para funções com muitos parâmetros, especialmente os opcionais, use parâmetros somente com palavras-chave:

```python
# ❌ Bad: Positional parameters
def updateProblem(
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None
) -> None: ...

# ✅ Good: Keyword-only parameters
def updateProblem(
    *,
    problem: Problem,
    previous_version: str,
    current_version: str,
    points: Optional[int] = None,
) -> None: ...
```
### Nomenclatura

- **snake_case** para funções e variáveis
- **CamelCase** para aulas

### Importações

Evite `from module import function`. Importe módulos e use notação de ponto:

```python
# ❌ Bad
from module import function
function()

# ✅ Good
import module
module.function()
```
Exceção: o módulo `typing` pode usar `from typing import ...`

## Comentários

Os comentários devem explicar **por que**, não **o que**:

```php
// ❌ Bad: Explains what
// Increment counter
$counter++;

// ✅ Good: Explains why
// Increment counter to track retry attempts for rate limiting
$counter++;
```
## Documentação Relacionada

- **[Guia de testes](testing.md)** - Como escrever testes
- **[Comandos Úteis](useful-commands.md)** - Comandos de desenvolvimento
- **[Guia de Componentes](components.md)** - Desenvolvimento de componentes Vue

---

**Lembre-se:** essas diretrizes são aplicadas por ferramentas automatizadas. Execute `./stuff/lint.sh` antes de confirmar!
