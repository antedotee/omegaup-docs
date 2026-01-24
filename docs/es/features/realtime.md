---
title: Actualizaciones en tiempo real
description: Eventos WebSocket para marcadores en vivo y notificaciones
icon: bootstrap/cloud
---
# Actualizaciones en tiempo real

omegaUp proporciona actualizaciones en tiempo real para marcadores, estado de envío y aclaraciones a través de conexiones WebSocket al servicio Broadcaster.

## Descripción general

Las funciones en tiempo real permiten:

- **Marcadores en vivo**: Actualizaciones sin actualizar la página
- **Notificaciones de envío**: comentarios instantáneos sobre el veredicto
- **Alertas de aclaración**: actualizaciones inmediatas de preguntas y respuestas
- **Eventos del concurso**: cambios de estado del concurso en tiempo real

## Configuración de la conexión

### URL de WebSocket

```javascript
const EVENTS_URL = 'wss://omegaup.com/events/';
```
### Conexión básica

```javascript
const ws = new WebSocket(EVENTS_URL);

ws.onopen = () => {
  console.log('Connected to event stream');
  authenticate();
};

ws.onclose = (event) => {
  console.log('Disconnected:', event.code);
  scheduleReconnect();
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};
```
### Autenticación

Después de conectarse, autentíquese con su token de sesión:

```javascript
function authenticate() {
  ws.send(JSON.stringify({
    type: 'auth',
    token: getAuthToken()  // From ouat cookie
  }));
}
```
## Canales de eventos

### Tipos de canales

| Patrón de canal | Descripción | Se requiere autenticación |
|-----------------|-------------|---------------|
| `/user/{username}` | Notificaciones personales | Sí (solo propietario) |
| `/contest/{alias}` | Eventos del concurso | Participante del concurso |
| `/contest/{alias}/admin` | Eventos de administración | Administrador del concurso |
| `/problem/{alias}` | Actualizaciones de problemas | Visor de problemas |
| `/scoreboard/{token}` | Marcador público | Ficha válida |

### Suscribirse a canales

```javascript
function subscribe(channel) {
  ws.send(JSON.stringify({
    type: 'subscribe',
    channel: channel
  }));
}

// Examples
subscribe('/contest/annual-2024');
subscribe('/user/myusername');
```
### Cancelar suscripción

```javascript
function unsubscribe(channel) {
  ws.send(JSON.stringify({
    type: 'unsubscribe',
    channel: channel
  }));
}
```
## Tipos de eventos

### Actualizaciones de envío (`run_update`)

Se activa cuando cambia un veredicto de envío:

```json
{
  "type": "run_update",
  "channel": "/contest/annual-2024",
  "timestamp": 1704067200,
  "data": {
    "guid": "abc123def456",
    "run_id": 12345,
    "contest_alias": "annual-2024",
    "problem_alias": "sum-two",
    "username": "contestant1",
    "status": "ready",
    "verdict": "AC",
    "score": 1.0,
    "contest_score": 100.0,
    "runtime": 0.045,
    "memory": 2048
  }
}
```
### Actualizaciones del marcador (`scoreboard_update`)

Se activa cuando cambia el marcador:

```json
{
  "type": "scoreboard_update",
  "channel": "/contest/annual-2024",
  "timestamp": 1704067200,
  "data": {
    "contest_alias": "annual-2024",
    "scoreboard_url": "/api/contest/scoreboard/..."
  }
}
```
### Aclaraciones (`clarification`)

Activado para nuevas aclaraciones o respuestas:

```json
{
  "type": "clarification",
  "channel": "/contest/annual-2024",
  "timestamp": 1704067200,
  "data": {
    "clarification_id": 567,
    "contest_alias": "annual-2024",
    "problem_alias": "sum-two",
    "author": "admin",
    "message": "The input is guaranteed to be positive.",
    "answer": null,
    "public": true
  }
}
```
### Actualizaciones del concurso (`contest_update`)

Se activa cuando cambia la configuración del concurso:

```json
{
  "type": "contest_update",
  "channel": "/contest/annual-2024",
  "timestamp": 1704067200,
  "data": {
    "contest_alias": "annual-2024",
    "event": "extended",
    "finish_time": 1704153600
  }
}
```
## Manejo de eventos

### Patrón de controlador de eventos

```javascript
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  
  switch (message.type) {
    case 'run_update':
      handleRunUpdate(message.data);
      break;
    case 'scoreboard_update':
      handleScoreboardUpdate(message.data);
      break;
    case 'clarification':
      handleClarification(message.data);
      break;
    case 'contest_update':
      handleContestUpdate(message.data);
      break;
    case 'auth_success':
      onAuthSuccess();
      break;
    case 'subscribed':
      onSubscribed(message.channel);
      break;
    case 'error':
      handleError(message);
      break;
  }
};
```
### Actualizaciones de envío

```javascript
function handleRunUpdate(data) {
  // Update submission row in UI
  const row = document.querySelector(`[data-run="${data.guid}"]`);
  if (row) {
    row.querySelector('.verdict').textContent = data.verdict;
    row.querySelector('.score').textContent = data.score;
    row.classList.remove('pending');
    row.classList.add(getVerdictClass(data.verdict));
  }
  
  // Show notification for own submissions
  if (data.username === currentUser) {
    showNotification(`${data.problem_alias}: ${data.verdict}`);
  }
}
```
### Actualización del marcador

```javascript
function handleScoreboardUpdate(data) {
  // Fetch updated scoreboard
  fetch(`/api/contest/scoreboard/?contest_alias=${data.contest_alias}`)
    .then(response => response.json())
    .then(scoreboard => {
      updateScoreboardUI(scoreboard);
    });
}
```
### Notificaciones de aclaración

```javascript
function handleClarification(data) {
  // Add to clarification list
  addClarificationToUI(data);
  
  // Show desktop notification
  if (Notification.permission === 'granted') {
    new Notification('New Clarification', {
      body: data.message.substring(0, 100),
      icon: '/icon.png'
    });
  }
  
  // Play notification sound
  playNotificationSound();
}
```
## Gestión de conexión

### Lógica de reconexión

```javascript
class EventConnection {
  constructor() {
    this.ws = null;
    this.reconnectAttempts = 0;
    this.maxReconnectDelay = 30000;
    this.subscriptions = new Set();
  }
  
  connect() {
    this.ws = new WebSocket(EVENTS_URL);
    this.ws.onopen = () => this.onConnect();
    this.ws.onclose = () => this.onDisconnect();
    this.ws.onmessage = (e) => this.onMessage(e);
  }
  
  onConnect() {
    this.reconnectAttempts = 0;
    this.authenticate();
    // Resubscribe to channels
    for (const channel of this.subscriptions) {
      this.subscribe(channel);
    }
  }
  
  onDisconnect() {
    const delay = Math.min(
      1000 * Math.pow(2, this.reconnectAttempts),
      this.maxReconnectDelay
    );
    this.reconnectAttempts++;
    setTimeout(() => this.connect(), delay);
  }
}
```
### Latido del corazón

```javascript
// Server sends ping every 30 seconds
// Client should handle pong automatically

setInterval(() => {
  if (ws.readyState === WebSocket.OPEN) {
    // Connection is alive
  } else {
    // Reconnect if needed
    reconnect();
  }
}, 35000);
```
## Marcadores públicos

### Ficha de marcador

Los concursos pueden generar URL de marcadores públicos:

```
https://omegaup.com/arena/contest-alias/scoreboard/{token}/
```
### Suscribirse sin autenticación

```javascript
// Token-based subscription
ws.send(JSON.stringify({
  type: 'subscribe',
  channel: `/scoreboard/${scoreboardToken}`
}));
```
## Mejores prácticas

### Rendimiento

1. **Actualizaciones aceleradas**: actualizaciones rápidas por lotes
2. **Carga diferida**: no actualizar elementos fuera de la pantalla
3. **Respuestas en caché**: evite llamadas API redundantes

```javascript
// Throttle scoreboard updates
const throttledUpdate = throttle(updateScoreboard, 1000);
```
### Manejo de errores

```javascript
ws.onerror = (error) => {
  console.error('WebSocket error:', error);
  // Don't try to reconnect immediately on error
  // Wait for onclose event
};

function handleError(message) {
  if (message.error === 'unauthorized') {
    // Re-authenticate
    authenticate();
  } else if (message.error === 'not_found') {
    // Channel doesn't exist
    unsubscribe(message.channel);
  }
}
```
### Degradación elegante

```javascript
// Fallback to polling if WebSocket unavailable
if (!('WebSocket' in window)) {
  startPolling();
} else {
  connectWebSocket();
}

function startPolling() {
  setInterval(async () => {
    const scoreboard = await fetchScoreboard();
    updateScoreboardUI(scoreboard);
  }, 30000);
}
```
## Integración de Vue.js

### Servicio de eventos

```typescript
// services/events.ts
import { ref, onMounted, onUnmounted } from 'vue';

export function useEventStream(contestAlias: string) {
  const scoreboard = ref(null);
  const clarifications = ref([]);
  let ws: WebSocket | null = null;
  
  function connect() {
    ws = new WebSocket(EVENTS_URL);
    ws.onopen = () => {
      authenticate();
      subscribe(`/contest/${contestAlias}`);
    };
    ws.onmessage = handleMessage;
  }
  
  function handleMessage(event: MessageEvent) {
    const data = JSON.parse(event.data);
    if (data.type === 'scoreboard_update') {
      fetchScoreboard().then(s => scoreboard.value = s);
    }
    if (data.type === 'clarification') {
      clarifications.value.push(data.data);
    }
  }
  
  onMounted(connect);
  onUnmounted(() => ws?.close());
  
  return { scoreboard, clarifications };
}
```
### Uso en componente

```vue
<template>
  <Scoreboard :data="scoreboard" />
  <ClarificationList :items="clarifications" />
</template>

<script setup>
const { scoreboard, clarifications } = useEventStream('annual-2024');
</script>
```
## Documentación relacionada

- **[Arquitectura de emisora](../architecture/broadcaster.md)** - Detalles técnicos
- **[API de concursos](../api/contests.md)** - Puntos finales del marcador
- **[API de aclaraciones](../api/clarifications.md)** - Puntos finales de aclaración
