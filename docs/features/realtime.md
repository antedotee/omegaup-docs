---
title: Real-time Updates
description: WebSocket events for live scoreboards and notifications
icon: bootstrap/cloud
---

# Real-time Updates

omegaUp provides real-time updates for scoreboards, submission status, and clarifications through WebSocket connections to the Broadcaster service.

## Overview

Real-time features enable:

- **Live scoreboards**: Updates without page refresh
- **Submission notifications**: Instant verdict feedback
- **Clarification alerts**: Immediate Q&A updates
- **Contest events**: Real-time contest state changes

## Connection Setup

### WebSocket URL

```javascript
const EVENTS_URL = 'wss://omegaup.com/events/';
```

### Basic Connection

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

### Authentication

After connecting, authenticate with your session token:

```javascript
function authenticate() {
  ws.send(JSON.stringify({
    type: 'auth',
    token: getAuthToken()  // From ouat cookie
  }));
}
```

## Event Channels

### Channel Types

| Channel Pattern | Description | Auth Required |
|-----------------|-------------|---------------|
| `/user/{username}` | Personal notifications | Yes (owner only) |
| `/contest/{alias}` | Contest events | Contest participant |
| `/contest/{alias}/admin` | Admin events | Contest admin |
| `/problem/{alias}` | Problem updates | Problem viewer |
| `/scoreboard/{token}` | Public scoreboard | Valid token |

### Subscribing to Channels

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

### Unsubscribing

```javascript
function unsubscribe(channel) {
  ws.send(JSON.stringify({
    type: 'unsubscribe',
    channel: channel
  }));
}
```

## Event Types

### Submission Updates (`run_update`)

Triggered when a submission verdict changes:

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

### Scoreboard Updates (`scoreboard_update`)

Triggered when scoreboard changes:

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

### Clarifications (`clarification`)

Triggered for new clarifications or answers:

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

### Contest Updates (`contest_update`)

Triggered when contest settings change:

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

## Handling Events

### Event Handler Pattern

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

### Submission Updates

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

### Scoreboard Refresh

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

### Clarification Notifications

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

## Connection Management

### Reconnection Logic

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

### Heartbeat

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

## Public Scoreboards

### Scoreboard Token

Contests can generate public scoreboard URLs:

```
https://omegaup.com/arena/contest-alias/scoreboard/{token}/
```

### Subscribing Without Auth

```javascript
// Token-based subscription
ws.send(JSON.stringify({
  type: 'subscribe',
  channel: `/scoreboard/${scoreboardToken}`
}));
```

## Best Practices

### Performance

1. **Throttle updates**: Batch rapid updates
2. **Lazy load**: Don't update off-screen elements
3. **Cache responses**: Avoid redundant API calls

```javascript
// Throttle scoreboard updates
const throttledUpdate = throttle(updateScoreboard, 1000);
```

### Error Handling

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

### Graceful Degradation

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

## Vue.js Integration

### Event Service

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

### Usage in Component

```vue
<template>
  <Scoreboard :data="scoreboard" />
  <ClarificationList :items="clarifications" />
</template>

<script setup>
const { scoreboard, clarifications } = useEventStream('annual-2024');
</script>
```

## Related Documentation

- **[Broadcaster Architecture](../architecture/broadcaster.md)** - Technical details
- **[Contests API](../api/contests.md)** - Scoreboard endpoints
- **[Clarifications API](../api/clarifications.md)** - Clarification endpoints
