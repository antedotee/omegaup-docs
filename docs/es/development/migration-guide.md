---
title: Guía de migración
description: Migración de plantillas Smarty a Vue.js y TypeScript
icon: bootstrap/arrow-right
---
# Guía de migración: Smarty a Vue.js/TypeScript

omegaUp está migrando de plantillas Smarty a componentes modernos de Vue.js con TypeScript.

## Estrategia de migración

### Estado actual
- **Antiguo**: Plantillas Smarty (archivos `.tpl`)
- **Nuevo**: componentes Vue.js (archivos `.vue`) + TypeScript

### Proceso de migración

1. **Identificar plantilla**: busque la plantilla de Smarty para migrar
2. **Crear componente Vue**: Cree un componente Vue equivalente
3. **Actualizar controladores**: modifique PHP para devolver JSON en lugar de representar la plantilla
4. **Actualizar rutas**: cambiar rutas para servir el componente Vue
5. **Prueba**: asegúrese de que la funcionalidad coincida con la original
6. **Eliminar plantilla antigua**: elimine la plantilla Smarty después de la verificación

## Directrices

### Estructura de plantilla

**Plantilla inteligente:**
```smarty
{include file='header.tpl'}
<div class="problem">
    <h1>{$problem.title}</h1>
    <p>{$problem.description}</p>
</div>
{include file='footer.tpl'}
```
**Componente Vue:**
```vue
<template>
  <div class="problem">
    <h1>{% raw %}{{ problem.title }}{% endraw %}</h1>
    <p>{% raw %}{{ problem.description }}{% endraw %}</p>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component
export default class ProblemView extends Vue {
  @Prop({ required: true })
  problem!: Problem;
}
</script>
```
### Cambios en la API

Los controladores deberían devolver JSON en lugar de representar plantillas:

```php
// ❌ Old: Render template
return [
    'smarty' => true,
    'template' => 'problem.tpl',
    'problem' => $problem,
];

// ✅ New: Return JSON
return [
    'status' => 'ok',
    'problem' => $problem,
];
```
## Documentación relacionada

- **[Pautas de codificación](coding-guidelines.md)** - Estándares Vue.js
- **[Guía de componentes](components.md)** - Desarrollo de componentes
- **[Arquitectura Frontend](../architecture/frontend.md)** - Estructura Frontend
