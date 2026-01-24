---
title: Arquitectura de emisora
description: Servidor WebSocket para actualizaciones en tiempo real
icon: bootstrap/cloud
---
# Arquitectura de emisora

Broadcaster es un servidor WebSocket que permite la comunicación en tiempo real entre el backend y los clientes web. Impulsa marcadores en vivo, actualizaciones de envíos y notificaciones de aclaraciones.

## Descripción general

```mermaid
flowchart LR
    subgraph Backend
        Grader[Grader]
        PHP[PHP API]
    end
    
    subgraph Broadcaster
        WS[WebSocket Server]
        Channels[Channel Manager]
        Auth[Auth Handler]
    end
    
    subgraph Clients
        C1[Browser 1]
        C2[Browser 2]
        C3[Browser N]
    end
    
    Grader -->|HTTPS| WS
    PHP -->|HTTPS| WS
    WS --> Channels
    Channels --> Auth
    Auth <-->|WebSocket| C1
    Auth <-->|WebSocket| C2
    Auth <-->|WebSocket| C3
```
## Eventos en tiempo real

### Tipos de eventos

| Evento | Descripción | Canal |
|-------|-------------|---------|
| `run_update` | Veredicto de presentación cambiado | Usuario, Concurso |
| `scoreboard_update` | Marcador cambiado | Concurso |
| `clarification` | Nueva aclaración | Concurso, Problema |
| `contest_update` | La configuración del concurso cambió | Concurso |

### Estructura de carga útil del evento

```json
{
  "type": "run_update",
  "timestamp": 1704067200,
  "data": {
    "run_id": 12345,
    "verdict": "AC",
    "score": 1.0,
    "contest_alias": "contest-2024",
    "problem_alias": "sum-two"
  }
}
```
## Sistema de canales

### Tipos de canales

| Patrón de canal | Descripción | Se requiere autenticación |
|-----------------|-------------|---------------|
| `/user/{username}` | Eventos específicos del usuario | Sí (propietario) |
| `/contest/{alias}` | Eventos del concurso | Acceso al concurso |
| `/contest/{alias}/admin` | Eventos de administración | Administrador del concurso |
| `/problem/{alias}` | Eventos problemáticos | Acceso problemático |
| `/scoreboard/{token}` | Marcador público | Token válido |

### Flujo de suscripción al canal

```mermaid
sequenceDiagram
    participant C as Client
    participant B as Broadcaster
    participant A as Auth Service
    
    C->>B: WebSocket Connect
    B-->>C: Connected
    
    C->>B: Subscribe /contest/abc
    B->>A: Verify access
    A-->>B: Authorized
    B-->>C: Subscribed
    
    Note over B: Event occurs
    B->>C: Push event
```
## Protocolo WebSocket

### Conexión

```javascript
const ws = new WebSocket('wss://omegaup.com/events/');

ws.onopen = () => {
  // Authenticate
  ws.send(JSON.stringify({
    type: 'auth',
    token: authToken
  }));
};
```
### Suscríbete al canal

```javascript
ws.send(JSON.stringify({
  type: 'subscribe',
  channel: '/contest/annual-2024'
}));
```
### Darse de baja

```javascript
ws.send(JSON.stringify({
  type: 'unsubscribe',
  channel: '/contest/annual-2024'
}));
```
### Recibir eventos

```javascript
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  switch (data.type) {
    case 'run_update':
      updateSubmissionStatus(data.data);
      break;
    case 'scoreboard_update':
      refreshScoreboard();
      break;
    case 'clarification':
      showClarificationNotification(data.data);
      break;
  }
};
```
## Integración de back-end

### Calificador a emisor

Cuando se califica una presentación:

```mermaid
sequenceDiagram
    participant R as Runner
    participant G as Grader
    participant B as Broadcaster
    participant C as Client
    
    R-->>G: Verdict result
    G->>G: Update database
    G->>B: POST /broadcast/
    B->>B: Route to channels
    B->>C: WebSocket push
```
### PHP a emisora

Para aclaraciones y actualizaciones del concurso:

```php
// In Clarification Controller
\OmegaUp\Grader::getInstance()->broadcast(
    contestAlias: $contest->alias,
    problemAlias: $problem->alias,
    message: json_encode([
        'type' => 'clarification',
        'data' => $clarification
    ]),
    public: false,
    username: $identity->username
);
```
## Autenticación

### Autenticación basada en tokens

Las conexiones WebSocket se autentican usando:

1. **Token de autenticación**: el mismo token que la API REST (de la cookie `ouat`)
2. **Token del marcador**: para URL públicas del marcador

### Verificación de permiso

Para cada suscripción:

```mermaid
flowchart TD
    Sub[Subscribe Request] --> CheckAuth{Authenticated?}
    CheckAuth -->|No| Public{Public Channel?}
    CheckAuth -->|Yes| CheckAccess{Has Access?}
    
    Public -->|Yes| Allow[Allow]
    Public -->|No| Deny[Deny]
    
    CheckAccess -->|Yes| Allow
    CheckAccess -->|No| Deny
```
## Escalabilidad

### Manejo de conexión

- Cada instancia de Broadcaster maneja miles de conexiones.
- Las conexiones no tienen estado (suscripciones almacenadas en la memoria)
- Latido cada 30 segundos para detectar conexiones muertas

### Escala horizontal

```mermaid
flowchart TB
    LB[Load Balancer]
    LB --> B1[Broadcaster 1]
    LB --> B2[Broadcaster 2]
    LB --> B3[Broadcaster N]
    
    Redis[(Redis Pub/Sub)]
    
    B1 <--> Redis
    B2 <--> Redis
    B3 <--> Redis
    
    Grader[Grader] --> Redis
```
Con múltiples instancias:
- El equilibrador de carga distribuye conexiones WebSocket
- Redis Pub/Sub distribuye eventos entre instancias
- Cualquier instancia puede publicar en cualquier canal.

## Configuración

### Configuración de emisora

```json
{
  "Broadcaster": {
    "Port": 32672,
    "TLS": {
      "CertFile": "/etc/omegaup/ssl/broadcaster.crt",
      "KeyFile": "/etc/omegaup/ssl/broadcaster.key"
    },
    "EventsPort": 39613,
    "PingInterval": 30,
    "WriteTimeout": 10
  },
  "Redis": {
    "URL": "redis://redis:6379",
    "Channel": "omegaup:events"
  }
}
```
### Componente acoplable

```yaml
broadcaster:
  image: omegaup/broadcaster
  ports:
    - "32672:32672"  # Internal API
    - "39613:39613"  # WebSocket
  depends_on:
    - redis
  environment:
    - REDIS_URL=redis://redis:6379
```
## Implementación del cliente

### Servicio de interfaz

La interfaz de Vue.js utiliza un servicio WebSocket:

```typescript
class EventService {
  private ws: WebSocket | null = null;
  private subscriptions: Map<string, Set<Function>> = new Map();
  
  connect(authToken: string): void {
    this.ws = new WebSocket(EVENTS_URL);
    this.ws.onopen = () => this.authenticate(authToken);
    this.ws.onmessage = (e) => this.handleMessage(e);
  }
  
  subscribe(channel: string, callback: Function): void {
    if (!this.subscriptions.has(channel)) {
      this.subscriptions.set(channel, new Set());
      this.ws?.send(JSON.stringify({
        type: 'subscribe',
        channel
      }));
    }
    this.subscriptions.get(channel)!.add(callback);
  }
  
  private handleMessage(event: MessageEvent): void {
    const data = JSON.parse(event.data);
    const callbacks = this.subscriptions.get(data.channel);
    callbacks?.forEach(cb => cb(data));
  }
}
```
## Monitoreo

### Control de salud

```bash
curl https://broadcaster:32672/health
```
### Métricas

Disponible en `/metrics`:

| Métrica | Descripción |
|--------|-------------|
| `connections_active` | Conexiones WebSocket actuales |
| `subscriptions_total` | Total de suscripciones activas |
| `messages_sent_total` | Mensajes enviados a clientes |
| `messages_received_total` | Mensajes de backends |

## Solución de problemas

### Problemas de conexión

| Problema | Causa | Solución |
|-------|-------|----------|
| Conexión rechazada | Locutor caído | Consultar estado del servicio |
| Error de autenticación | Token no válido | Volver a autenticar |
| Sin eventos | No suscrito | Verificar suscripción |
| Eventos retrasados ​​| Latencia de red | Comprobar conexión |

### Modo de depuración

Habilite el registro detallado:

```json
{
  "Logging": {
    "Level": "debug",
    "IncludeMessages": true
  }
}
```
## Código fuente

El Broadcaster es parte del repositorio [`quark`](https://github.com/omegaup/quark):

- `cmd/omegaup-broadcaster/` - Punto de entrada principal
- `broadcaster/` - Lógica principal de WebSocket

## Documentación relacionada

- **[Funciones en tiempo real](../features/realtime.md)** - Descripción general de las funciones
- **[Grader Internals](grader-internals.md)** - Origen del evento
- **[Infraestructura](infrastructure.md)** - Integración de Redis
