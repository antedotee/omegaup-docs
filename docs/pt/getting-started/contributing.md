---
title: Contribuindo para omegaUp
description: Aprenda como contribuir com código para omegaUp por meio de pull requests
icon: bootstrap/code-tags
---
# Contribuindo para omegaUp

Obrigado pelo seu interesse em contribuir com o omegaUp! Este guia orientará você no processo de envio de sua primeira contribuição.

## Visão geral do processo de desenvolvimento

A ramificação `main` em seu fork deve sempre ser mantida atualizada com a ramificação `main` do repositório omegaUp. **Nunca se comprometa diretamente com `main`**. Em vez disso, crie um branch separado para cada alteração que você planeja enviar por meio de uma solicitação pull.

## Pré-requisitos

Antes de começar:

1. ✅ [Configure seu ambiente de desenvolvimento](development-setup.md)
2. ✅ Leia as [Diretrizes de codificação](../development/coding-guidelines.md)
3. ✅ Entenda [como obter ajuda](getting-help.md) se tiver dúvidas

## Requisito de atribuição de problemas

!!! importante "Obrigatório antes de abrir PR"
    Cada solicitação pull **deve** estar vinculada a um problema existente do GitHub que é **atribuído a você**.

### Etapas para atribuir o problema

1. **Encontre ou crie um problema**:
   - Procure [problemas existentes](https://github.com/omegaup/omegaup/issues)
   - Ou [crie um novo problema](https://github.com/omegaup/omegaup/issues/new) descrevendo sua correção de bug ou recurso

2. **Expressar interesse**:
   - Comente o assunto manifestando seu interesse em trabalhar nele
   - Espere que um mantenedor o atribua a você

3. **Comece a trabalhar**:
   - Uma vez atribuído, você pode criar sua filial e começar a codificar
   - Faça referência ao problema na descrição do seu PR usando: `Fixes #1234` ou `Closes #1234`

!!! falha "PR falhará sem atribuição de problemas"
    Se o seu PR não estiver vinculado a um problema atribuído, as verificações automatizadas falharão e o seu PR não poderá ser mesclado.

## Configurando seu fork e controles remotos

Você só precisa fazer isso uma vez:

### 1. Bifurque o repositório

Visite [github.com/omegaup/omegaup](https://github.com/omegaup/omegaup) e clique no botão "Fork".

### 2. Clone seu garfo

```bash
git clone https://github.com/YOURUSERNAME/omegaup.git
cd omegaup
```
### 3. Configurar controles remotos

Verifique seus controles remotos atuais:

```bash
git remote -v
```
Você deverá ver algo como:

```
origin        https://github.com/YOURUSERNAME/omegaup.git (fetch)
origin        https://github.com/YOURUSERNAME/omegaup.git (push)
```
Caso contrário, adicione o repositório omegaUp como `origin`:

```bash
git remote add origin https://github.com/omegaup/omegaup.git
```
Em seguida, adicione seu fork como `upstream`:

```bash
git remote add upstream https://github.com/YOURUSERNAME/omegaup.git
```
Sua configuração final deverá ficar assim:

```
origin	https://github.com/omegaup/omegaup.git (fetch)
origin	https://github.com/omegaup/omegaup.git (push)
upstream	https://github.com/YOURUSERNAME/omegaup.git (fetch)
upstream	https://github.com/YOURUSERNAME/omegaup.git (push)
```
## Atualizando sua filial principal

Mantenha seu branch `main` sincronizado com o `main` do omegaUp:

```bash
git checkout main              # Switch to main branch
git fetch origin               # Fetch latest changes
git pull --rebase origin main  # Sync with omegaUp/main
git push upstream              # Update your fork
```
!!! aviso "Aviso de envio forçado"
    Se `git push upstream` falhar, significa que você fez alterações diretamente em `main`. Use `git push upstream -f` para forçar o envio, mas evite fazer alterações em `main` no futuro.

## Iniciando uma nova mudança

### 1. Crie uma ramificação de recursos

Crie uma nova ramificação de `origin/main`:

```bash
git checkout -b feature-name origin/main
git push upstream feature-name
```
!!! dica "Nomeação de filiais"
    Use nomes de ramificação descritivos como `fix-login-bug` ou `add-dark-mode-toggle`.

### 2. Faça suas alterações

- Escreva seu código seguindo as [diretrizes de codificação](../development/coding-guidelines.md)
- Escreva testes para suas alterações
- Garantir que todos os testes sejam aprovados

### 3. Confirme suas alterações

```bash
git add .
git commit -m "Write a clear description of your changes"
```
!!! dica "Confirmar mensagens"
    Escreva mensagens de commit claras e descritivas. Consulte [Commits convencionais](https://www.conventionalcommits.org/) para conhecer as práticas recomendadas.

### 4. Execute validadores

Antes de enviar, execute o script linting:

```bash
./stuff/lint.sh
```
Este comando:
- Alinha elementos de código
- Remove linhas desnecessárias
- Realiza validações para todas as linguagens utilizadas no omegaUp

!!! observe "Ganchos pré-empurrados"
    Esse script também é executado automaticamente por meio de ganchos pré-push, mas executá-lo manualmente garante que suas alterações atendam aos padrões.

### 5. Configurar usuário Git (somente na primeira vez)

Se você não configurou as informações do usuário do Git:

```bash
git config --global user.email "your-email@domain.com"
git config --global user.name "Your Name"
```
## Criando uma solicitação pull

### 1. Envie suas alterações

```bash
git push -u upstream feature-name
```
O sinalizador `-u` configura o rastreamento entre sua filial local e a filial remota.

### 2. Solicitação pull aberta no GitHub

1. Acesse [github.com/SEU NOME DE USUÁRIO/omegaup](https://github.com/YOURUSERNAME/omegaup)
2. Clique em "Filial" e selecione sua filial
3. Clique em "Solicitação pull"
4. Preencha a descrição do PR

### 3. Modelo de descrição de relações públicas

Sua descrição de RP deve incluir:

```markdown
## Description
Brief description of what this PR does.

## Related Issue
Fixes #1234  <!-- Replace with your issue number -->

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
Describe how you tested your changes.

## Screenshots (if applicable)
Add screenshots if your changes affect the UI.
```
!!! importante "Referência do problema necessária"
    Sempre inclua `Fixes #1234` ou `Closes #1234` na descrição do seu PR. Isso fecha automaticamente o problema quando o PR é mesclado.

## Atualizando sua solicitação pull

Se você precisar fazer alterações após criar o PR:

```bash
git add .
git commit -m "Description of additional changes"
git push  # No -u flag needed after first push
```
O PR será atualizado automaticamente com seus novos commits.

## O que acontece após o envio

1. **Verificações automatizadas**: GitHub Actions executará testes e validações
2. **Revisão de código**: um mantenedor revisará seu código
3. **Feedback sobre endereço**: faça as alterações solicitadas e envie atualizações
4. **Mesclar**: Depois de aprovado, seu PR será mesclado
5. **Implantação**: as alterações são implantadas nos finais de semana

!!! info "Implantações de fim de semana"
    Os PRs mesclados são implantados na produção durante as implantações de fim de semana. Você verá suas alterações ao vivo após a próxima implantação.

## Excluindo filiais

Depois que seu PR for mesclado:

### Excluir filial local

```bash
git branch -D feature-name
```
### Excluir filial remota

1. Acesse GitHub e clique em "Ramos"
2. Encontre sua filial e clique no ícone excluir

Ou use Git:

```bash
git push upstream --delete feature-name
```
### Limpar referências remotas

Remova referências de ramificação remota obsoletas:

```bash
git remote prune upstream --dry-run  # Preview what will be removed
git remote prune upstream             # Actually remove them
```
## Configurações adicionais

### Configuração de localidade

A máquina virtual pode não ter `en_US.UTF-8` como localidade padrão. Para corrigir isso, siga [este guia](https://askubuntu.com/questions/881742/locale-cannot-set-lc-ctype-to-default-locale-no-such-file-or-directory-locale/893586#893586).

### Dependências do compositor

Na primeira configuração, instale as dependências do PHP:

```bash
composer install
```
### Configuração MySQL

Se você encontrar erros do MySQL ao enviar, instale e configure o MySQL:

```bash
sudo apt install mysql-client mysql-server

cat > ~/.mysql.docker.cnf <<EOF
[client]
port=13306
host=127.0.0.1
protocol=tcp
user=root
password=omegaup
EOF
ln -sf ~/.mysql.docker.cnf .my.cnf
```
## Recursos

- **[Diretrizes de codificação](../development/coding-guidelines.md)** - Nossos padrões de codificação
- **[Comandos úteis](../development/useful-commands.md)** - Referência de comandos de desenvolvimento
- **[Guia de testes](../development/testing.md)** - Como escrever e executar testes
- **[Como obter ajuda](getting-help.md)** - Onde fazer perguntas

## Próximas etapas

- Revise a [Visão geral da arquitetura](../architecture/index.md) para entender a base de código
- Confira [Guias de desenvolvimento](../development/index.md) para guias detalhados
- Junte-se ao nosso [servidor Discord](https://discord.com/invite/K3JFd9d3wk) para se conectar com a comunidade

---

**Pronto para fazer sua primeira contribuição?** Escolha um problema, crie um ramo e envie seu PR!
