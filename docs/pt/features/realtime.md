---
title: Atualizações em tempo real
description: Eventos WebSocket para placares e notificações ao vivo
icon: bootstrap/cloud
---
# Atualizações em tempo real

omegaUp fornece atualizações em tempo real para placares, status de envio e esclarecimentos por meio de conexões WebSocket com o serviço Broadcaster.

## Visão geral

Os recursos em tempo real permitem:

- **Placares ao vivo**: Atualizações sem atualização de página
- **Notificações de envio**: feedback instantâneo do veredicto
- **Alertas de esclarecimento**: Atualizações imediatas de perguntas e respostas
- **Eventos do concurso**: mudanças no estado do concurso em tempo real

## Configuração de conexão

###URL do WebSocket

```javascript
const EVENTS_URL = 'wss://omegaup.com/events/';
```
### Conexão Básica

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
### Autenticação

Após conectar, autentique-se com seu token de sessão:

```javascript
function authenticate() {
  ws.send(JSON.stringify({
    type: 'auth',
    token: getAuthToken()  // From ouat cookie
  }));
}
```
## Canais de eventos

### Tipos de canais

| Padrão de canal | Descrição | Autenticação necessária |
|-----------------|-------------|---------------|
| `/user/{username}` | Notificações pessoais | Sim (apenas proprietário) |
| `/contest/{alias}` | Eventos de concurso | Participante do concurso |
| `/contest/{alias}/admin` | Eventos administrativos | Administrador do concurso |
| `/problem/{alias}` | Atualizações de problemas | Visualizador de problemas |
| `/scoreboard/{token}` | Placar público | Token válido |

### Inscrevendo-se em canais

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
### Cancelando inscrição

```javascript
function unsubscribe(channel) {
  ws.send(JSON.stringify({
    type: 'unsubscribe',
    channel: channel
  }));
}
```
## Tipos de eventos

### Atualizações de envio (`run_update`)

Acionado quando um veredicto de envio é alterado:

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
### Atualizações do placar (`scoreboard_update`)

Acionado quando o placar muda:

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
### Esclarecimentos (`clarification`)

Acionado para novos esclarecimentos ou respostas:

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
### Atualizações do concurso (`contest_update`)

Acionado quando as configurações do concurso mudam:

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
## Tratamento de eventos

### Padrão de manipulador de eventos

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
### Atualizações de envio

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
### Atualização do placar

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
### Notificações de esclarecimento

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
## Gerenciamento de conexão

### Lógica de reconexão

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
### Batimento cardíaco

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
## Painéis públicos

### Símbolo do placar

Os concursos podem gerar URLs de placar público:

```
https://omegaup.com/arena/contest-alias/scoreboard/{token}/
```
### Assinando sem autenticação

```javascript
// Token-based subscription
ws.send(JSON.stringify({
  type: 'subscribe',
  channel: `/scoreboard/${scoreboardToken}`
}));
```
## Melhores práticas

### Desempenho

1. **Atualizações de aceleração**: atualizações rápidas em lote
2. **Carregamento lento**: não atualize elementos fora da tela
3. **Respostas de cache**: evite chamadas de API redundantes

```javascript
// Throttle scoreboard updates
const throttledUpdate = throttle(updateScoreboard, 1000);
```
### Tratamento de erros

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
### Degradação Graciosa

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
## Integração Vue.js

### Serviço de Eventos

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
### Uso no componente

```vue
<template>
  <Scoreboard :data="scoreboard" />
  <ClarificationList :items="clarifications" />
</template>

<script setup>
const { scoreboard, clarifications } = useEventStream('annual-2024');
</script>
```
## Documentação Relacionada

- **[Arquitetura da emissora](../architecture/broadcaster.md)** - Detalhes técnicos
- **[API de concursos](../api/contests.md)** - Pontos de extremidade do placar
- **[API de esclarecimentos](../api/clarifications.md)** - Pontos de extremidade de esclarecimento
