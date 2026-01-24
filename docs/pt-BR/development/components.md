---
title: Componentes Vue
description: Desenvolvimento de componentes Vue.js e integração com Storybook
icon: bootstrap/view-grid
---
# Componentes Vue

O frontend do omegaUp usa Vue.js 2.5.22 com TypeScript para desenvolvimento de componentes.

## Estrutura do Componente

Os componentes estão localizados em `frontend/www/js/omegaup/components/`.

### Componente Básico

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
## Diretrizes de componentes

### Evite sinalizadores de comportamento
Não crie componentes que alterem significativamente o comportamento com base em sinalizadores. Use `slot`s em vez disso:

```vue
<!-- ✅ Good: Using slots -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```
### Internacionalização
Nunca codifique o texto. Sempre use strings de tradução:

```typescript
// ❌ Bad
<div>Hello World</div>

// ✅ Good
<div>{% raw %}{{ T.helloWorld }}{% endraw %}</div>
```
### Evite concatenação de strings
Use `ui.formatString()` para strings parametrizadas:

```typescript
// ❌ Bad
{% raw %}{{ T.greeting }}{% endraw %} {% raw %}{{ userName }}{% endraw %}

// ✅ Good
{% raw %}{{ ui.formatString(T.greeting, { name: userName }) }}{% endraw %}
```
### Cores
Use variáveis CSS, não cores codificadas:

```css
/* ❌ Bad */
color: #ff0000;

/* ✅ Good */
color: var(--color-primary);
```
## Integração com livro de histórias

Usamos o Storybook para documentação e teste de componentes.

### Adicionando histórias

Crie histórias para cada componente:

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
### Livro de histórias em execução

```bash
yarn storybook
```
Abre o livro de histórias em `http://localhost:6006`

## Teste de componentes

Cada componente Vue deve ter testes unitários:

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
## Documentação Relacionada

- **[Diretrizes de codificação](coding-guidelines.md)** - Diretrizes Vue.js
- **[Guia de teste](testing.md)** - Teste de componentes
- **[Arquitetura de front-end](../architecture/frontend.md)** - Estrutura de front-end
