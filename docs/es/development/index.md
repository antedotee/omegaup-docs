---
title: Guías de desarrollo
description: Guías para desarrolladores, estándares de codificación y mejores prácticas
icon: bootstrap/code-tags
---
# Guías de desarrollo

Esta sección contiene guías completas para desarrolladores que trabajan en omegaUp.

## Enlaces rápidos

<div class="grid cards" markdown>

- :material-code-tags:{ .lg .middle } __[Pautas de codificación](coding-guidelines.md)__

    ---

    Estándares de codificación, guías de estilo y mejores prácticas para PHP, TypeScript y Python.

    [Pautas de lectura :octicons-arrow-right-24:](coding-guidelines.md)

- :material-flask:{ .lg .middle } __[Guía de pruebas](testing.md)__

    ---

    Cómo escribir y ejecutar pruebas para PHP, TypeScript y Cypress E2E.

    [Prueba de aprendizaje :octicons-arrow-right-24:](testing.md)

- :material-database:{ .lg .middle } __[Patrones de base de datos](database-patterns.md)__

    ---

    Comprender los patrones DAO/VO y las mejores prácticas de interacción con bases de datos.

    [:octicons-arrow-right-24: Aprender patrones](database-patterns.md)

- :material-puzzle:{ .lg .middle } __[Componentes](components.md)__

    ---

    Desarrollo de componentes Vue.js e integración de Storybook.

    [Componentes de aprendizaje :octicons-arrow-right-24:](components.md)

- :material-tools:{ .lg .middle } __[Comandos útiles](useful-commands.md)__

    ---

    Comandos y atajos de desarrollo comunes.

    [Comandos de visualización :octicons-arrow-right-24:](useful-commands.md)

</div>

## Flujo de trabajo de desarrollo

1. **[Configure su entorno](../../getting-started/development-setup.md)** - Ejecute Docker
2. **[Lea las pautas de codificación](coding-guidelines.md)** - Comprenda nuestros estándares
3. **[Escribir pruebas](testing.md)** - Asegúrese de que su código funcione
4. **[Enviar un PR](../../getting-started/contributing.md)** - Contribuya con sus cambios

## Principios clave

### Tipo Seguridad
- Todo el código debe declarar tipos de datos.
- TypeScript para interfaz
- Salmo para PHP
- mypy para Python

### Pruebas
- Todos los cambios de funcionalidad deben incluir pruebas.
- Las pruebas deben pasar el 100% antes de comprometerse.
- Escribe pruebas primero cuando sea posible.

### Calidad del código
- Siga las reglas de linting automatizadas
- Utilice cláusulas de protección en lugar de condicionales anidados
- Minimizar el uso nulo/indefinido
- Eliminar el código no utilizado (no comentarlo)

## Documentación relacionada

- **[Descripción general de la arquitectura](../architecture/index.md)** - Diseño del sistema
- **[Referencia de API](../api/index.md)** - Documentación de API
- **[Comenzando](../../getting-started/index.md)** - Guía de configuración y contribución

---

**¿Listo para codificar?** ¡Comience con las [Pautas de codificación](coding-guidelines.md)!
