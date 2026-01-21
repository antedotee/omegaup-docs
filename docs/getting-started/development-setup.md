---
title: Development Environment Setup
description: Complete guide to setting up your local omegaUp development environment
---

# Development Environment Setup

This guide will walk you through setting up a local development environment for omegaUp using Docker.

!!! tip "Video Tutorial"
    We have a [video tutorial](http://www.youtube.com/watch?v=H1PG4Dvje88) that demonstrates the setup process visually.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker Engine**: [Install Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- **Docker Compose 2**: [Install Docker Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
- **Git**: For cloning the repository

!!! note "WSL Users"
    If you're using WSL (Windows Subsystem for Linux), follow the [official Docker Desktop WSL integration guide](https://docs.docker.com/desktop/features/wsl).

### Linux-Specific Setup

If you're running Linux, after installing Docker, add your user to the docker group:

```bash
sudo usermod -a -G docker $USER
```

Log out and log back in for the changes to take effect.

!!! warning "Git Knowledge"
    If you're not confident using Git, we recommend reading [this Git tutorial](https://github.com/shekhargulati/git-the-missing-tutorial) first.

## Step 1: Fork and Clone the Repository

1. **Fork the repository**: Visit [github.com/omegaup/omegaup](https://github.com/omegaup/omegaup) and click the "Fork" button

2. **Clone your fork**:
   ```bash
   git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
   cd omegaup
   ```

3. **Initialize submodules** (if needed):
   ```bash
   git submodule update --init --recursive
   ```

## Step 2: Start Docker Containers

### First Time Setup

On your first run, pull the Docker images and start the containers:

```bash
docker-compose pull
docker-compose up --no-build
```

This will take 2-10 minutes. You'll know it's ready when you see output similar to:

```
frontend_1     | Child frontend:
frontend_1     |        1550 modules
frontend_1     |     Child HtmlWebpackCompiler:
frontend_1     |            1 module
...
```

### Subsequent Runs

After the first run, you can start containers faster with:

```bash
docker compose up --no-build
```

The `--no-build` flag avoids rebuilding everything, significantly speeding up startup.

## Step 3: Access Your Local Instance

Once the containers are running, access your local omegaUp instance at:

**http://localhost:8001**

## Step 4: Access Container Console

To run commands inside the container:

```bash
docker exec -it omegaup-frontend-1 /bin/bash
```

The codebase is located at `/opt/omegaup` inside the container.

## Development Accounts

Your local installation includes pre-configured accounts:

### Admin Account
- **Username**: `omegaup`
- **Password**: `omegaup`
- **Role**: Administrator (sysadmin privileges)

### Regular User Account
- **Username**: `user`
- **Password**: `user`
- **Role**: Regular user

### Test Accounts

For testing purposes, you can use these test accounts:

| Username | Password |
|----------|----------|
| `test_user_0` | `test_user_0` |
| `test_user_1` | `test_user_1` |
| ... | ... |
| `course_test_user_0` | `course_test_user_0` |

!!! info "Email Verification"
    In development mode, email verification is disabled. You can use dummy email addresses when creating new accounts.

## Running Tests Locally

If you want to run JavaScript/TypeScript tests outside of Docker:

### Prerequisites

1. **Node.js**: Version 16 or higher
2. **Yarn**: Package manager

### Setup Steps

1. **Initialize Git Submodules**:
   ```bash
   git submodule update --init --recursive
   ```
   
   This downloads required dependencies:
   - `pagedown` - Markdown editor
   - `iso-3166-2.js` - Country/region codes
   - `csv.js` - CSV parsing
   - `mathjax` - Math rendering

2. **Install Dependencies**:
   ```bash
   yarn install
   ```

3. **Run Tests**:
   ```bash
   yarn test
   ```

### Quick Start (Fresh Clone)

For a fresh clone, use this single command:

```bash
git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
cd omegaup
yarn install
yarn test
```

## Codebase Structure

The omegaUp codebase is organized as follows:

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

For more details, see the [Architecture Overview](../architecture/index.md).

## Common Issues

### The Web App Is Not Showing My Changes

Make sure Docker is running:

```bash
docker compose up --no-build
```

If the problem persists, ask for help in omegaUp's communication channels.

### Browser Redirects HTTP to HTTPS

If your browser keeps changing `http` to `https` for localhost, you can disable security policies for `localhost`. [See this guide](https://hmheng.medium.com/exclude-localhost-from-chrome-chromium-browsers-forced-https-redirection-642c8befa9b).

### MySQL Not Found Error

If you encounter this error when pushing to GitHub:

```
FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/mysql'
```

Install MySQL client outside the container:

```bash
sudo apt-get install mysql-client mysql-server
```

Then configure MySQL connection:

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

### MySQL Connection Error

If MySQL is installed but you get connection errors, ensure the configuration file above is set up correctly.

## Next Steps

- **[Learn how to contribute](contributing.md)** - Create branches and submit pull requests
- **[Review coding guidelines](../development/coding-guidelines.md)** - Understand our coding standards
- **[Explore the architecture](../architecture/index.md)** - Understand how omegaUp works

## Getting Help

If you encounter issues not covered here:

1. Check the [Getting Help guide](getting-help.md)
2. Search existing [GitHub issues](https://github.com/omegaup/deploy/issues)
3. Ask in our [Discord server](https://discord.com/invite/K3JFd9d3wk)

---

**Ready to start coding?** Head to the [Contributing Guide](contributing.md) to learn how to submit your first pull request!
