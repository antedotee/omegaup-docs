---
title: Configuración del entorno de desarrollo
description: Guía completa para configurar su entorno de desarrollo omegaUp local
icon: bootstrap/tools
---
# Configuración del entorno de desarrollo

Esta guía lo guiará en la configuración de un entorno de desarrollo local para omegaUp usando Docker.

!!! consejo "Videotutorial"
    Tenemos un [video tutorial](http://www.youtube.com/watch?v=H1PG4Dvje88) que demuestra visualmente el proceso de configuración.

## Requisitos previos

Antes de comenzar, asegúrese de tener instalado lo siguiente:

- **Docker Engine**: [Instalar Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- **Docker Compose 2**: [Instalar Docker Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
- **Git**: Para clonar el repositorio

!!! nota "Usuarios de WSL"
    Si está utilizando WSL (Subsistema de Windows para Linux), siga la [guía oficial de integración de WSL de Docker Desktop] (https://docs.docker.com/desktop/features/wsl).

### Configuración específica de Linux

Si está ejecutando Linux, después de instalar Docker, agregue su usuario al grupo de Docker:

```bash
sudo usermod -a -G docker $USER
```
Cierra sesión y vuelve a iniciarla para que los cambios surtan efecto.

!!! advertencia "Git Knowledge"
    Si no está seguro de usar Git, le recomendamos leer [este tutorial de Git](https://github.com/shekhargulati/git-the-missing-tutorial) primero.

## Paso 1: bifurcar y clonar el repositorio

1. **Bifurcar el repositorio**: visita [github.com/omegaup/omegaup](https://github.com/omegaup/omegaup) y haz clic en el botón "Bifurcar"

2. **Clona tu tenedor**:
   ```bash
   git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
   cd omegaup
   ```
3. **Inicializar submódulos** (si es necesario):
   ```bash
   git submodule update --init --recursive
   ```
## Paso 2: Iniciar contenedores Docker

### Configuración por primera vez

En su primera ejecución, extraiga las imágenes de Docker e inicie los contenedores:

```bash
docker-compose pull
docker-compose up --no-build
```
Esto tardará entre 2 y 10 minutos. Sabrá que está listo cuando vea un resultado similar a:

```
frontend_1     | Child frontend:
frontend_1     |        1550 modules
frontend_1     |     Child HtmlWebpackCompiler:
frontend_1     |            1 module
...
```
### Ejecuciones posteriores

Después de la primera ejecución, puedes iniciar contenedores más rápido con:

```bash
docker compose up --no-build
```
La bandera `--no-build` evita reconstruir todo, acelerando significativamente el inicio.

## Paso 3: acceda a su instancia local

Una vez que los contenedores se estén ejecutando, acceda a su instancia local de omegaUp en:

**http://localhost:8001**

## Paso 4: Acceder a la consola del contenedor

Para ejecutar comandos dentro del contenedor:

```bash
docker exec -it omegaup-frontend-1 /bin/bash
```
El código base se encuentra en `/opt/omegaup` dentro del contenedor.

## Cuentas de Desarrollo

Su instalación local incluye cuentas preconfiguradas:

### Cuenta de administrador
- **Nombre de usuario**: `omegaup`
- **Contraseña**: `omegaup`
- **Rol**: Administrador (privilegios de administrador de sistemas)

### Cuenta de usuario habitual
- **Nombre de usuario**: `user`
- **Contraseña**: `user`
- **Rol**: Usuario habitual

### Cuentas de prueba

Para fines de prueba, puede utilizar estas cuentas de prueba:

| Nombre de usuario | Contraseña |
|----------|----------|
| `test_user_0` | `test_user_0` |
| `test_user_1` | `test_user_1` |
| ... | ... |
| `course_test_user_0` | `course_test_user_0` |

!!! información "Verificación por correo electrónico"
    En el modo de desarrollo, la verificación de correo electrónico está deshabilitada. Puede utilizar direcciones de correo electrónico ficticias al crear cuentas nuevas.

## Ejecución de pruebas localmente

Si desea ejecutar pruebas de JavaScript/TypeScript fuera de Docker:

### Requisitos previos

1. **Node.js**: Versión 16 o superior
2. **Yarn**: Administrador de paquetes

### Pasos de configuración

1. **Inicializar submódulos de Git**:
   ```bash
   git submodule update --init --recursive
   ```
Esta descarga requiere dependencias:
   - `pagedown` - Editor de rebajas
   - `iso-3166-2.js` - Códigos de país/región
   - `csv.js` - Análisis CSV
   - `mathjax` - Representación matemática

2. **Instalar dependencias**:
   ```bash
   yarn install
   ```
3. **Ejecutar pruebas**:
   ```bash
   yarn test
   ```
### Inicio rápido (clon nuevo)

Para un clon nuevo, use este único comando:

```bash
git clone --recurse-submodules https://github.com/YOURUSERNAME/omegaup
cd omegaup
yarn install
yarn test
```
## Estructura de la base de código

El código base de omegaUp está organizado de la siguiente manera:

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
Para obtener más detalles, consulte la [Descripción general de la arquitectura](../architecture/index.md).

## Problemas comunes

### La aplicación web no muestra mis cambios

Asegúrese de que Docker se esté ejecutando:

```bash
docker compose up --no-build
```
Si el problema persiste pide ayuda en los canales de comunicación de omegaUp.

### El navegador redirige HTTP a HTTPS

Si su navegador sigue cambiando `http` a `https` para localhost, puede desactivar las políticas de seguridad para `localhost`. [Consulte esta guía](https://hmheng.medium.com/exclude-localhost-from-chrome-chromium-browsers-forced-https-redirection-642c8befa9b).

### Error de MySQL no encontrado

Si encuentra este error al ingresar a GitHub:

```
FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/mysql'
```
Instale el cliente MySQL fuera del contenedor:

```bash
sudo apt-get install mysql-client mysql-server
```
Luego configure la conexión MySQL:

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
### Error de conexión MySQL

Si MySQL está instalado pero obtiene errores de conexión, asegúrese de que el archivo de configuración anterior esté configurado correctamente.

## Próximos pasos

- **[Aprenda cómo contribuir](contributing.md)** - Cree sucursales y envíe solicitudes de extracción
- **[Revisar las pautas de codificación](../development/coding-guidelines.md)** - Comprenda nuestros estándares de codificación
- **[Explora la arquitectura](../architecture/index.md)** - Entiende cómo funciona omegaUp

## Obtener ayuda

Si encuentra problemas que no se tratan aquí:

1. Consulte la [Guía para obtener ayuda](getting-help.md)
2. Busque [problemas de GitHub] existentes (https://github.com/omegaup/deploy/issues)
3. Pregunta en nuestro [servidor de Discord](https://discord.com/invite/K3JFd9d3wk)

---

**¿Listo para comenzar a codificar?** Dirígete a la [Guía de contribución](contributing.md) para saber cómo enviar tu primera solicitud de extracción.
