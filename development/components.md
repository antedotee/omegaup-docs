---
title: Vue Components
description: Vue.js component development and Storybook integration
---

# Vue Components

omegaUp's frontend uses Vue.js 2.5.22 with TypeScript for component development.

## Component Structure

Components are located in `frontend/www/js/omegaup/components/`.

### Basic Component

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

## Component Guidelines

### Avoid Behavior Flags
Don't create components that change behavior significantly based on flags. Use `slot`s instead:

```vue
<!-- ✅ Good: Using slots -->
<template>
  <div>
    <slot name="header"></slot>
    <slot name="content"></slot>
  </div>
</template>
```

### Internationalization
Never hardcode text. Always use translation strings:

```typescript
// ❌ Bad
<div>Hello World</div>

// ✅ Good
<div>{% raw %}{{ T.helloWorld }}{% endraw %}</div>
```

### Avoid String Concatenation
Use `ui.formatString()` for parameterized strings:

```typescript
// ❌ Bad
{% raw %}{{ T.greeting }}{% endraw %} {% raw %}{{ userName }}{% endraw %}

// ✅ Good
{% raw %}{{ ui.formatString(T.greeting, { name: userName }) }}{% endraw %}
```

### Colors
Use CSS variables, not hardcoded colors:

```css
/* ❌ Bad */
color: #ff0000;

/* ✅ Good */
color: var(--color-primary);
```

## Storybook Integration

We use Storybook for component documentation and testing.

### Adding Stories

Create stories for each component:

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

### Running Storybook

```bash
yarn storybook
```

Opens Storybook at `http://localhost:6006`

## Component Testing

Each Vue component should have unit tests:

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

## Related Documentation

- **[Coding Guidelines](coding-guidelines.md)** - Vue.js guidelines
- **[Testing Guide](testing.md)** - Component testing
- **[Frontend Architecture](../architecture/frontend.md)** - Frontend structure
