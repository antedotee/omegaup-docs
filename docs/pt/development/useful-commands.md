---
title: Comandos úteis de desenvolvimento
description: Comandos e atalhos comuns para desenvolvimento omegaUp
icon: bootstrap/terminal
---
# Comandos úteis de desenvolvimento

Referência rápida para comandos de desenvolvimento comuns no omegaUp.

## Linting e validação

### Execute todos os linters
```bash
./stuff/lint.sh
```
Executa todas as validações de código. É executado automaticamente em `git push`.

**Local:** Fora do contêiner Docker, raiz do projeto

### Validar apenas estilo
```bash
./stuff/lint.sh validate
```
Valida o estilo do código sem corrigir problemas.

### Gerar arquivos i18n
```bash
./stuff/lint.sh --linters=i18n fix --all
```
Gera arquivos `*.lang` baseados em `es.lang`, `en.lang` e `pt.lang`.

## Teste

### Execute todos os testes PHP
```bash
./stuff/runtests.sh
```
Executa testes PHPUnit, validação de tipo MySQL e Psalm.

**Localização:** Dentro do contêiner Docker

### Executar arquivo de teste PHP específico
```bash
./stuff/run-php-tests.sh frontend/tests/controllers/$MY_FILE.php
```
Executa testes de unidade para um único arquivo PHP. Omita o nome do arquivo para executar todos os testes.

### Executar testes Cypress
```bash
npx cypress open
```
Abre a GUI do Cypress Test Runner para testes interativos.

**Pré-requisitos:**
- Node.js instalado
- npm instalado
-libasound2 (Linux)

**Local:** Fora do contêiner Docker

### Execute testes de unidade Vue (modo Watch)
```bash
yarn run test:watch
```
Executa testes Vue no modo de observação, reexecutando automaticamente nas alterações de código.

### Executar arquivo de teste específico do Vue
```bash
./node_modules/.bin/jest frontend/www/js/omegaup/components/$MY_FILE.test.ts
```
Executa um único arquivo de teste Vue.

## Banco de dados

### Redefinir o banco de dados para o estado inicial
```bash
./stuff/bootstrap-environment.py --purge
```
Restaura o banco de dados ao estado inicial e preenche com dados de teste.

**Localização:** Dentro do contêiner Docker

### Aplicar migrações de banco de dados
```bash
./stuff/db-migrate.py migrate --databases=omegaup,omegaup-test
```
Aplica alterações de esquema de novos arquivos de migração.

**Localização:** Dentro do contêiner Docker

### Atualizar schema.sql de Migrações
```bash
./stuff/update-dao.sh
```
Aplica alterações em `schema.sql` ao adicionar novos arquivos de migração.

**Localização:** Dentro do contêiner Docker

## Validação de tipo PHP

### Execute o Salmo em todos os arquivos PHP
```bash
find frontend/ \
    -name *.php \
    -and -not -wholename 'frontend/server/libs/third_party/*' \
    -and -not -wholename 'frontend/tests/badges/*' \
    -and -not -wholename 'frontend/tests/controllers/*' \
    -and -not -wholename 'frontend/tests/runfiles/*' \
    -and -not -wholename 'frontend/www/preguntas/*' \
  | xargs ./vendor/bin/psalm \
    --long-progress \
    --show-info=false
```
Executa validação de tipo em arquivos PHP usando Psalm.

**Localização:** Dentro do contêiner Docker

## Docker

### Reinicie o serviço Docker
```bash
systemctl restart docker.service
```
Reinicia o serviço Docker. Útil para corrigir erros de acesso a contêineres.

**Local:** Fora do contêiner Docker (Linux)

### Acessar o console do contêiner
```bash
docker exec -it omegaup-frontend-1 /bin/bash
```
Abre um shell bash dentro do contêiner frontend.

## Referência rápida

| Tarefa | Comando | Localização |
|------|---------|----------|
| Código Lint | `./stuff/lint.sh` | Contentor exterior |
| Execute testes PHP | `./stuff/runtests.sh` | Dentro do recipiente |
| Execute Cipreste | `npx cypress open` | Contentor exterior |
| Redefinir banco de dados | `./stuff/bootstrap-environment.py --purge` | Dentro do recipiente |
| Migrar banco de dados | `./stuff/db-migrate.py migrate` | Dentro do recipiente |
| Testes Vue | `yarn run test:watch` | Dentro do recipiente |

## Documentação Relacionada

- **[Guia de teste](testing.md)** - Documentação de teste abrangente
- **[Diretrizes de codificação](coding-guidelines.md)** - Padrões de código
- **[Configuração de desenvolvimento](../../getting-started/development-setup.md)** - Configuração do ambiente
