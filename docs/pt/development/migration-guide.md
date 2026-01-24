---
title: Guia de migração
description: Migrando de modelos Smarty para Vue.js e TypeScript
icon: bootstrap/arrow-right
---
# Guia de migração: Smarty para Vue.js/TypeScript

omegaUp está migrando de modelos Smarty para componentes Vue.js modernos com TypeScript.

## Estratégia de Migração

### Estado Atual
- **Antigo**: modelos Smarty (arquivos `.tpl`)
- **Novo**: componentes Vue.js (arquivos `.vue`) + TypeScript

### Processo de migração

1. **Identificar modelo**: Encontre o modelo Smarty para migrar
2. **Criar componente Vue**: Construir componente Vue equivalente
3. **Atualizar controladores**: modifique o PHP para retornar JSON em vez de renderizar o modelo
4. **Atualizar Rotas**: Alterar rotas para servir o componente Vue
5. **Teste**: certifique-se de que a funcionalidade corresponda ao original
6. **Remover modelo antigo**: Exclua o modelo Smarty após verificação

## Diretrizes

### Estrutura do modelo

**Modelo inteligente:**
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
### Mudanças na API

Os controladores devem retornar JSON em vez de renderizar modelos:

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
## Documentação Relacionada

- **[Diretrizes de codificação](coding-guidelines.md)** - Padrões Vue.js
- **[Guia de Componentes](components.md)** - Desenvolvimento de componentes
- **[Arquitetura de front-end](../architecture/frontend.md)** - Estrutura de front-end
