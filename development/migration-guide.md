---
title: Migration Guide
description: Migrating from Smarty templates to Vue.js and TypeScript
---

# Migration Guide: Smarty to Vue.js/TypeScript

omegaUp is migrating from Smarty templates to modern Vue.js components with TypeScript.

## Migration Strategy

### Current State
- **Old**: Smarty templates (`.tpl` files)
- **New**: Vue.js components (`.vue` files) + TypeScript

### Migration Process

1. **Identify Template**: Find Smarty template to migrate
2. **Create Vue Component**: Build equivalent Vue component
3. **Update Controllers**: Modify PHP to return JSON instead of rendering template
4. **Update Routes**: Change routes to serve Vue component
5. **Test**: Ensure functionality matches original
6. **Remove Old Template**: Delete Smarty template after verification

## Guidelines

### Template Structure

**Smarty Template:**
```smarty
{include file='header.tpl'}
<div class="problem">
    <h1>{$problem.title}</h1>
    <p>{$problem.description}</p>
</div>
{include file='footer.tpl'}
```

**Vue Component:**
```vue
<template>
  <div class="problem">
    <h1>{{ problem.title }}</h1>
    <p>{{ problem.description }}</p>
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

### API Changes

Controllers should return JSON instead of rendering templates:

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

## Related Documentation

- **[Coding Guidelines](coding-guidelines.md)** - Vue.js standards
- **[Components Guide](components.md)** - Component development
- **[Frontend Architecture](../architecture/frontend.md)** - Frontend structure
