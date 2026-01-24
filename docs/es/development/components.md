---
title: Componentes de Vue
description: Desarrollo de componentes Vue.js e integración de Storybook
icon: bootstrap/view-grid
---
# Componentes de Vue

La interfaz de omegaUp utiliza Vue.js 2.5.22 con TypeScript para el desarrollo de componentes.

## Estructura de componentes

Los componentes están ubicados en `frontend/www/js/omegaup/components/`.

### Componente básico

```vue
<template>
  <div class="my-component">
    <h1>{% raw %}{{ title }}{% endraw %}</h1>
    <button @click="handleClick">Click me</button>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component
export default class MyComponent extends Vue {
  @Prop({ required: true })
  title!: string;

  handleClick(): void {
    this.$emit('clicked');
  }
}
</script>
```
## Directrices de componentes

### Evite las señales de comportamiento
No cree componentes que cambien significativamente el comportamiento en función de las banderas. Utilice `slot` en su lugar:

```vue
<!-- ✅ Good: Using slots -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```
### Internacionalización
Nunca codifique texto. Utilice siempre cadenas de traducción:

```typescript
// ❌ Bad
<div>Hello World</div>

// ✅ Good
<div>{% raw %}{{ T.helloWorld }}{% endraw %}</div>
```
### Evite la concatenación de cadenas
Utilice `ui.formatString()` para cadenas parametrizadas:

```typescript
// ❌ Bad
{% raw %}{{ T.greeting }}{% endraw %} {% raw %}{{ userName }}{% endraw %}

// ✅ Good
{% raw %}{{ ui.formatString(T.greeting, { name: userName }) }}{% endraw %}
```
### Colores
Utilice variables CSS, no colores codificados:

```css
/* ❌ Bad */
color: #ff0000;

/* ✅ Good */
color: var(--color-primary);
```
## Integración de libros de cuentos

Usamos Storybook para la documentación y pruebas de componentes.

### Agregar historias

Crea historias para cada componente:

```typescript
import MyComponent from './MyComponent.vue';

export default {
  title: 'Components/MyComponent',
  component: MyComponent,
};

export const Default = () => ({
  components: { MyComponent },
  template: '<MyComponent title="Hello" />',
});
```
### Libro de cuentos en ejecución

```bash
yarn storybook
```
Abre el libro de cuentos en `http://localhost:6006`

## Pruebas de componentes

Cada componente de Vue debe tener pruebas unitarias:

```typescript
import { mount } from '@vue/test-utils';
import MyComponent from './MyComponent.vue';

describe('MyComponent', () => {
  it('renders title', () => {
    const wrapper = mount(MyComponent, {
      propsData: { title: 'Test' }
    });
    expect(wrapper.text()).toContain('Test');
  });
});
```
## Documentación relacionada

- **[Pautas de codificación](coding-guidelines.md)** - Directrices de Vue.js
- **[Guía de pruebas](testing.md)** - Pruebas de componentes
- **[Arquitectura Frontend](../architecture/frontend.md)** - Estructura Frontend
