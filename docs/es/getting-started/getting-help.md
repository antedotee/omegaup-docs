---
title: Obtener ayuda
description: Aprenda cómo hacer preguntas de manera efectiva y obtener ayuda de la comunidad omegaUp
icon: bootstrap/help-circle
---
# Obtener ayuda

Sabemos que tendrá preguntas sobre cómo funcionan las cosas en omegaUp: preguntas técnicas, preguntas sobre procesos y más. Esta guía le ayudará a obtener mejores respuestas más rápido.

## Antes de preguntar

### 1. Buscar recursos existentes

Antes de publicar una pregunta, busque estos recursos:

#### Documentación
- **Este sitio de documentación** - Busque su tema
- **[Guía de configuración de desarrollo](development-setup.md)** - Problemas de instalación y configuración
- **[Documentación de arquitectura](../architecture/index.md)** - Preguntas de diseño del sistema

#### Recursos comunitarios
- **Búsqueda de Discord** - Buscar el historial de mensajes en nuestro [canal #dev_training](https://discord.com/invite/K3JFd9d3wk)
  - Discord tiene una poderosa función de búsqueda: ya se han hecho muchas preguntas antes
  - Busque por palabras clave relacionadas con su pregunta

#### Recursos externos
- **Google** - Para preguntas generales sobre Git, Docker, PHP, JavaScript, etc.
  - Si su pregunta no es específica de omegaUp, es probable que Google tenga la respuesta.

!!! consejo "Consejos de búsqueda"
    Pruebe diferentes combinaciones de palabras clave. A menudo, alguien ya ha hecho una pregunta similar antes.

## Hacer preguntas de forma eficaz

### Dónde preguntar

Publique su pregunta en el canal **#dev_training** de nuestro [servidor de Discord](https://discord.com/invite/K3JFd9d3wk).

!!! importante "Solo canales públicos"
    - ✅ Publicar en canales públicos (no DM)
    - ✅ Etiquetar el canal apropiado
    - ❌ No envíes mensajes directos
    - ❌ No etiquetes a personas específicas innecesariamente

### Cómo preguntar

Siga estas pautas para obtener mejores respuestas:

#### 1. Proporcionar contexto

Explica lo que estás intentando hacer:

```markdown
I'm trying to set up my development environment on macOS, and I'm getting
an error when running `docker compose up`.
```
#### 2. Describe el problema

Incluye:
- **Lo que esperabas que sucediera**
- **Lo que realmente pasó**
- **Pasos que seguiste**
- **Mensajes de error** (copia y pega el error completo)
- **Fragmentos de código relevantes** (si corresponde)
- **Registros** (si corresponde)

#### 3. Muestra lo que has probado

Menciona lo que ya has intentado:

```markdown
I've already tried:
- Reinstalling Docker
- Checking the documentation
- Searching Discord history for similar issues
```
#### 4. Incluir información del sistema

Si es relevante, incluya:
- Sistema operativo y versión.
- Versión acoplable
- Versión de Node.js (si corresponde)
- Cualquier otro detalle ambiental relevante.

### Ejemplo de buena pregunta

```markdown
Hi! I'm setting up the development environment on Ubuntu 22.04 and getting
an error when running `docker compose up`.

**Expected:** Containers should start successfully
**Actual:** Getting "port already in use" error

**Steps I followed:**
1. Installed Docker and Docker Compose
2. Cloned the repository
3. Ran `docker compose up`

**Error message:**
```
ERROR: para la interfaz No se puede iniciar la interfaz del servicio: 
El controlador falló al programar la conectividad externa en el terminal 
omegaup-frontend-1: Falló el enlace para 0.0.0.0:8001: el puerto ya está asignado
```

**What I've tried:**
- Checked if port 8001 is in use: `lsof -i :8001`
- Found process using the port and killed it
- Still getting the same error

Any help would be appreciated!
```
### Ejemplo de mala pregunta

```markdown
docker not working help pls
```
!!! fracaso "Por qué esto es malo"
    - No hay contexto sobre lo que significa "no funciona"
    - Ningún mensaje de error
    - No hay información del sistema
    - No hay indicación de lo que se intentó.

## Seguimiento

### Si tu pregunta obtiene respuesta

1. **Agradece a la persona** que te ayudó
2. **Confirma que la solución funcionó**
3. **Actualice el hilo** con lo que lo solucionó (si es diferente de la solución sugerida)

¡Esto ayuda a futuras personas con el mismo problema!

### Si lo resuelves tú mismo

Si descubres la solución:

1. **Actualiza el hilo** explicando cómo lo resolviste
2. **Márcalo como resuelto** (si la plataforma lo admite)

Esto evita que otros pierdan el tiempo intentando ayudar después de que ya lo hayas resuelto.

### Si su pregunta fue formulada antes

Si encuentra un hilo existente con su pregunta:

- **Responder a ese hilo** en lugar de crear uno nuevo
- **Agregue nueva información** si su situación es diferente
- **Hacer preguntas de seguimiento** en el mismo hilo

Esto mantiene unida la información relacionada y hace que sea más fácil de encontrar.

## Ayudar a los demás

¡Te animamos a **ayudar a tus compañeros** con sus preguntas!

### ¿Por qué ayudar a los demás?

- **Aprendizaje**: Explicar conceptos te ayuda a comprenderlos mejor.
- **Comunidad**: construir una comunidad útil e inclusiva
- **Reconocimiento**: tenemos en cuenta la utilidad al seleccionar candidatos de GSoC

### Cómo ayudar

- **Leer las preguntas** publicadas por otros con regularidad
- **Responda preguntas** con las que esté familiarizado
- **Comparte recursos** que podrían ayudar
- **Sea paciente y amable** - todos están aprendiendo

## Qué evitar

### ❌ No hagas estas cosas

1. **No envíe mensajes directos**: publique en canales públicos para que otros puedan beneficiarse
2. **No etiquetes a personas específicas** - Publica públicamente para que cualquiera pueda ayudar
3. **No volver a publicar preguntas**: busque primero, responda a los hilos existentes
4. **No hagas la misma pregunta varias veces** - Ten paciencia para recibir las respuestas

### ✅ Haz Estas Cosas

1. **Buscar primero** - Consulta la documentación y el historial de Discord
2. **Publicar públicamente**: utilice los canales adecuados
3. **Sea específico**: proporcione contexto, errores y lo que ha probado
4. **Seguimiento**: actualice los hilos cuando se resuelvan los problemas.
5. **Ayuda a otros** - Responde preguntas cuyas respuestas conoces

## Recursos adicionales

### Aprender a hacer mejores preguntas

Recomendamos leer:
- **[Cómo hacer preguntas de manera inteligente](https://www.mikeash.com/getting_answers.html)** - Excelente guía para hacer preguntas efectivas

### Recursos específicos de omegaUp

- **[Configuración de desarrollo](development-setup.md)** - Problemas de configuración del entorno
- **[Guía de contribución](contributing.md)** - Preguntas de relaciones públicas y flujo de trabajo
- **[Documentación de arquitectura](../architecture/index.md)** - Preguntas de diseño del sistema
- **[Documentación de API](../api/index.md)** - Preguntas relacionadas con API

### Canales comunitarios

- **Discord**: [canal #dev_training](https://discord.com/invite/K3JFd9d3wk) - Canal de soporte principal
- **Problemas de GitHub**: [Informar errores](https://github.com/omegaup/omegaup/issues) - Para errores confirmados
- **Discusiones de GitHub**: [Discusiones generales](https://github.com/omegaup/omegaup/discussions) - Para ideas sobre funciones y debates

## Resumen

1. ✅ **Buscar primero** - Documentación, Historial de Discord, Google
2. ✅ **Pregunta públicamente** - Utiliza los canales adecuados, no mensajes directos
3. ✅ **Sea específico**: proporcione contexto, errores, pasos e información del sistema
4. ✅ **Seguimiento** - Actualizar los hilos cuando se resuelvan
5. ✅ **Ayuda a otros** - Responde preguntas con las que puedas ayudar

---

**¿Aún necesitas ayuda?** Únete a nuestro [servidor de Discord](https://discord.com/invite/K3JFd9d3wk) y pregunta en el canal #dev_training.
