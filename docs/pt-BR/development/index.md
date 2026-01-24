---
title: Guias de desenvolvimento
description: Guias do desenvolvedor, padrões de codificação e práticas recomendadas
icon: bootstrap/code-tags
---
# Guias de desenvolvimento

Esta seção contém guias completos para desenvolvedores que trabalham no omegaUp.

## Links rápidos

<div class="grid cards" markdown>

- :material-code-tags:{ .lg .middle } __[Diretrizes de codificação](coding-guidelines.md)__

    ---

    Padrões de codificação, guias de estilo e práticas recomendadas para PHP, TypeScript e Python.

    [Diretrizes de leitura do :octicons-arrow-right-24:](coding-guidelines.md)

- :material-flask:{ .lg .middle } __[Guia de teste](testing.md)__

    ---

    Como escrever e executar testes para testes PHP, TypeScript e Cypress E2E.

    [Teste de aprendizagem do :octicons-arrow-right-24:](testing.md)

- :material-database:{ .lg .middle } __[Padrões de banco de dados](database-patterns.md)__

    ---

    Compreender os padrões DAO/VO e as melhores práticas de interação com o banco de dados.

    [Padrões de aprendizagem :octicons-arrow-right-24:](database-patterns.md)

- :material-puzzle:{ .lg .middle } __[Componentes](components.md)__

    ---

    Desenvolvimento de componentes Vue.js e integração com Storybook.

    [Componentes de aprendizagem do :octicons-arrow-right-24:](components.md)

- :material-tools:{ .lg .middle } __[Comandos úteis](useful-commands.md)__

    ---

    Comandos e atalhos comuns de desenvolvimento.

    [Comandos de visualização do :octicons-arrow-right-24:](useful-commands.md)

</div>

## Fluxo de trabalho de desenvolvimento

1. **[Configure seu ambiente](../../getting-started/development-setup.md)** - Coloque o Docker em execução
2. **[Leia as diretrizes de codificação](coding-guidelines.md)** - Entenda nossos padrões
3. **[Escrever testes](testing.md)** - Certifique-se de que seu código funcione
4. **[Envie um PR](../../getting-started/contributing.md)** - Contribua com suas alterações

## Princípios Chave

### Digite Segurança
- Todo código deve declarar tipos de dados
- TypeScript para front-end
- Salmo para PHP
- mypy para Python

### Teste
- Todas as alterações de funcionalidade devem incluir testes
- Os testes devem passar 100% antes de serem confirmados
- Escreva os testes primeiro, quando possível

### Qualidade do código
- Siga regras automatizadas de linting
- Use cláusulas de guarda em vez de condicionais aninhadas
- Minimize o uso nulo/indefinido
- Remova o código não utilizado (não comente)

## Documentação Relacionada

- **[Visão geral da arquitetura](../architecture/index.md)** - Design do sistema
- **[Referência da API](../api/index.md)** - Documentação da API
- **[Primeiros passos](../../getting-started/index.md)** - Guia de configuração e contribuição

---

**Pronto para codificar?** Comece com [Diretrizes de codificação](coding-guidelines.md)!
