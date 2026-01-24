---
title: Configuração do ambiente de desenvolvimento
description: Guia completo para configurar seu ambiente de desenvolvimento local omegaUp
icon: bootstrap/tools
---
# Configuração do ambiente de desenvolvimento

Este guia orientará você na configuração de um ambiente de desenvolvimento local para omegaUp usando Docker.

!!! dica "Vídeo Tutorial"
    Temos um [vídeo tutorial](http://www.youtube.com/watch?v=H1PG4Dvje88) que demonstra visualmente o processo de configuração.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- **Docker Engine**: [Instalar Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- **Docker Compose 2**: [Instalar Docker Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
- **Git**: Para clonar o repositório

!!! observe "Usuários WSL"
    Se você estiver usando WSL (subsistema Windows para Linux), siga o [guia oficial de integração WSL do Docker Desktop](https://docs.docker.com/desktop/features/wsl).

### Configuração específica do Linux

Se você estiver executando o Linux, após instalar o Docker, adicione seu usuário ao grupo docker:

```bash
sudo usermod -a -G docker $USER
```
Saia e faça login novamente para que as alterações tenham efeito.

!!! aviso "Git Conhecimento"
    Se você não tiver confiança no uso do Git, recomendamos a leitura [este tutorial do Git](https://github.com/shekhargulati/git-the-missing-tutorial) primeiro.

## Etapa 1: bifurcar e clonar o repositório

1. **Fork do repositório**: Visite [github.com/omegaup/omegaup](https://github.com/omegaup/omegaup) e clique no botão "Fork"

2. **Clone seu garfo**:
   ```bash
   git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
   cd omegaup
   ```
3. **Inicializar submódulos** (se necessário):
   ```bash
   git submodule update --init --recursive
   ```
## Etapa 2: iniciar contêineres Docker

### Configuração pela primeira vez

Na primeira execução, extraia as imagens do Docker e inicie os contêineres:

```bash
docker-compose pull
docker-compose up --no-build
```
Isso levará de 2 a 10 minutos. Você saberá que está pronto quando vir uma saída semelhante a:

```
frontend_1     | Child frontend:
frontend_1     |        1550 modules
frontend_1     |     Child HtmlWebpackCompiler:
frontend_1     |            1 module
...
```
### Execuções subsequentes

Após a primeira execução, você pode iniciar contêineres mais rapidamente com:

```bash
docker compose up --no-build
```
O sinalizador `--no-build` evita reconstruir tudo, acelerando significativamente a inicialização.

## Etapa 3: acesse sua instância local

Assim que os contêineres estiverem em execução, acesse sua instância local do omegaUp em:

**http://localhost:8001**

## Etapa 4: acessar o console do contêiner

Para executar comandos dentro do contêiner:

```bash
docker exec -it omegaup-frontend-1 /bin/bash
```
A base de código está localizada em `/opt/omegaup` dentro do contêiner.

## Contas de Desenvolvimento

Sua instalação local inclui contas pré-configuradas:

### Conta de administrador
- **Nome de usuário**: `omegaup`
- **Senha**: `omegaup`
- **Função**: Administrador (privilégios de administrador de sistema)

### Conta de usuário normal
- **Nome de usuário**: `user`
- **Senha**: `user`
- **Função**: usuário regular

### Contas de teste

Para fins de teste, você pode usar estas contas de teste:

| Nome de usuário | Senha |
|----------|----------|
| `test_user_0` | `test_user_0` |
| `test_user_1` | `test_user_1` |
| ... | ... |
| `course_test_user_0` | `course_test_user_0` |

!!! informações "Verificação de e-mail"
    No modo de desenvolvimento, a verificação de e-mail está desabilitada. Você pode usar endereços de e-mail fictícios ao criar novas contas.

## Executando testes localmente

Se você deseja executar testes JavaScript/TypeScript fora do Docker:

### Pré-requisitos

1. **Node.js**: versão 16 ou superior
2. **Yarn**: Gerenciador de pacotes

### Etapas de configuração

1. **Inicializar submódulos Git**:
   ```bash
   git submodule update --init --recursive
   ```
Isso baixa as dependências necessárias:
   - `pagedown` - Editor de redução
   - `iso-3166-2.js` - Códigos de país/região
   - `csv.js` - análise CSV
   - `mathjax` - Renderização matemática

2. **Instalar dependências**:
   ```bash
   yarn install
   ```
3. **Executar testes**:
   ```bash
   yarn test
   ```
### Início rápido (novo clone)

Para um novo clone, use este único comando:

```bash
git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
cd omegaup
yarn install
yarn test
```
## Estrutura da base de código

A base de código omegaUp é organizada da seguinte forma:

```
omegaup/
├── frontend/
│   ├── server/
│   │   └── src/
│   │       ├── Controllers/    # Business logic & API endpoints
│   │       ├── DAO/            # Data Access Objects
│   │       └── libs/           # Libraries & utilities
│   ├── www/                    # Frontend assets (TypeScript, Vue.js)
│   ├── templates/              # Smarty templates & i18n files
│   ├── database/               # Database migrations
│   └── tests/                  # Test files
```
Para obter mais detalhes, consulte [Visão geral da arquitetura](../architecture/index.md).

## Problemas comuns

### O aplicativo da web não está mostrando minhas alterações

Certifique-se de que o Docker esteja em execução:

```bash
docker compose up --no-build
```
Caso o problema persista, peça ajuda nos canais de comunicação da omegaUp.

### Navegador redireciona HTTP para HTTPS

Se o seu navegador continuar mudando `http` para `https` para localhost, você poderá desabilitar as políticas de segurança para `localhost`. [Veja este guia](https://hmheng.medium.com/exclude-localhost-from-chrome-chromium-browsers-forced-https-redirection-642c8befa9b).

### Erro MySQL não encontrado

Se você encontrar esse erro ao enviar para o GitHub:

```
FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/mysql'
```
Instale o cliente MySQL fora do contêiner:

```bash
sudo apt-get install mysql-client mysql-server
```
Em seguida, configure a conexão MySQL:

```bash
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
### Erro de conexão MySQL

Se o MySQL estiver instalado, mas você receber erros de conexão, certifique-se de que o arquivo de configuração acima esteja configurado corretamente.

## Próximas etapas

- **[Aprenda como contribuir](contributing.md)** - Crie ramificações e envie solicitações pull
- **[Revise as diretrizes de codificação](../development/coding-guidelines.md)** - Entenda nossos padrões de codificação
- **[Explore a arquitetura](../architecture/index.md)** - Entenda como o omegaUp funciona

## Obtendo ajuda

Se você encontrar problemas não abordados aqui:

1. Verifique o [Guia de ajuda](getting-help.md)
2. Pesquise [problemas do GitHub] existentes (https://github.com/omegaup/deploy/issues)
3. Pergunte em nosso [servidor Discord](https://discord.com/invite/K3JFd9d3wk)

---

**Pronto para começar a codificar?** Acesse o [Guia de contribuição](contributing.md) para saber como enviar sua primeira solicitação pull!
