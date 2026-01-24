---
title: Guia de teste
description: Guia de teste abrangente para omegaUp
icon: bootstrap/flask
---
# Guia de teste

omegaUp usa várias estruturas de teste para garantir a qualidade do código em diferentes camadas.

## Pilha de testes

| Camada | Estrutura | Localização |
|-------|-----------|----------|
| Testes de Unidade PHP | Unidade PHP | `frontend/tests/controllers/` |
| Testes TypeScript/Vue | Brincadeira | `frontend/www/js/` |
| Testes E2E | Cipreste | `cypress/e2e/` |
| Testes Python | pytest | `stuff/` |

## Testes de Unidade PHP

### Executando todos os testes PHP

```bash
./stuff/runtests.sh
```
Executa testes PHPUnit, validação de tipo MySQL e Psalm.

**Localização**: Dentro do contêiner Docker

### Executando arquivo de teste específico

```bash
./stuff/run-php-tests.sh frontend/tests/controllers/MyControllerTest.php
```
Omita o nome do arquivo para executar todos os testes.

### Requisitos de teste

- Todos os testes devem passar 100% antes de serem confirmados
- Nova funcionalidade requer testes novos/modificados
- Testes localizados em `frontend/tests/controllers/`

## Testes TypeScript/Vue

### Executando testes Vue (modo Watch)

```bash
yarn run test:watch
```
Executa novamente testes automaticamente quando o código é alterado.

**Localização**: Dentro do contêiner Docker

### Executando arquivo de teste específico

```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/MyComponent.test.ts
```
### Estrutura de teste

Verificação de testes de componentes Vue:
- Visibilidade dos componentes
- Emissão de eventos
- Comportamento esperado
- Adereços e estado

## Testes Cypress E2E

### Abrindo o Cypress Test Runner

```bash
npx cypress open
```
Abre a interface gráfica para testes interativos.

**Pré-requisitos**:
- Node.js instalado
- npm instalado
-libasound2 (Linux)

**Localização**: Fora do contêiner Docker

### Executando testes Cypress

```bash
yarn test:e2e
```
Executa todos os testes Cypress sem cabeça.

### Arquivos de teste

Testes E2E localizados em `cypress/e2e/`:
-`login.spec.ts`
-`problem-creation.spec.ts`
-`contest-management.spec.ts`
- E mais...

## Testes Python

Os testes Python usam pytest e estão localizados no diretório `stuff/`.

## Cobertura de teste

Usamos **Codecov** para medir a cobertura:

- **PHP**: Cobertura medida ✅
- **TypeScript**: Cobertura medida ✅
- **Cypress**: Cobertura ainda não medida ⚠️

## Melhores práticas

### Escreva os testes primeiro
Quando possível, escreva testes antes da implementação (TDD).

### Testar caminhos críticos
Concentre-se em:
- Fluxos de autenticação de usuários
- Envio e avaliação de problemas
- Gestão de concursos
- Terminais de API

### Mantenha os testes rápidos
- Os testes unitários devem ser rápidos (<1 segundo)
- Os testes E2E podem ser mais lentos, mas devem ser concluídos em um tempo razoável

### Teste de isolamento
- Cada teste deve ser independente
- Limpe os dados de teste após os testes
- Use acessórios de teste para dados consistentes

## Documentação Relacionada

- **[Diretrizes de codificação](coding-guidelines.md)** - Padrões de código
- **[Comandos úteis](useful-commands.md)** - Comandos de teste
- **[Guia Cypress](../../../frontend/www/docs/How-to-use-Cypress-in-omegaUp.md)** - Guia Cypress detalhado
