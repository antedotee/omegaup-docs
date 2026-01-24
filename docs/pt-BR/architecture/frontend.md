---
title: Arquitetura de front-end
description: Estrutura de front-end, componentes Vue.js e organização TypeScript
icon: bootstrap/web
---
# Arquitetura de front-end

O frontend do omegaUp é construído com tecnologias web modernas: Vue.js, TypeScript e Bootstrap 4.

## Pilha de tecnologia

| Tecnologia | Finalidade | Versão |
|------------|---------|---------|
| Vue.js | Estrutura de IU | 2.5.22 |
| Datilografado | JavaScript com segurança de tipo | 4.4.4 |
| Inicialização | Estrutura CSS | 4.6.0 |
| Webpack | Ferramenta de construção | 5,94 |

## Estrutura de diretório

```
frontend/www/
├── js/                    # TypeScript source files
│   └── omegaup/
│       ├── components/     # Vue components
│       ├── api/           # API client code
│       └── *.ts           # TypeScript modules
├── css/                   # Stylesheets
├── sass/                  # Sass source files
└── [PHP files]            # Entry points
```
## Arquitetura de Componentes

Os componentes Vue são organizados por recurso:

- **Componentes**: componentes de UI reutilizáveis
- **Clientes de API**: classes TypeScript para chamadas de API
- **Tipos**: definições de tipo TypeScript
- **Utilitários**: Funções utilitárias

## Processo de construção

Webpack agrupa arquivos TypeScript e Vue:

1. **TypeScript** → Compilado em JavaScript
2. **Componentes Vue** → Compilado e empacotado
3. **Sass** → Compilado em CSS
4. **Ativos** → Copiado para o diretório de saída

## Documentação Relacionada

- **[Guia de componentes](../development/components.md)** - Desenvolvimento de componentes
- **[Diretrizes de codificação](../development/coding-guidelines.md)** - Padrões de front-end
- **[Guia de migração](../development/migration-guide.md)** - Migrando do Smarty para Vue
