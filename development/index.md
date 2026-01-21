---
title: Development Guides
description: Developer guides, coding standards, and best practices
---

# Development Guides

This section contains comprehensive guides for developers working on omegaUp.

## Quick Links

<div class="grid cards" markdown>

-   :material-code-tags:{ .lg .middle } __[Coding Guidelines](coding-guidelines.md)__

    ---

    Coding standards, style guides, and best practices for PHP, TypeScript, and Python.

    [:octicons-arrow-right-24: Read Guidelines](coding-guidelines.md)

-   :material-flask:{ .lg .middle } __[Testing Guide](testing.md)__

    ---

    How to write and run tests for PHP, TypeScript, and Cypress E2E tests.

    [:octicons-arrow-right-24: Learn Testing](testing.md)

-   :material-database:{ .lg .middle } __[Database Patterns](database-patterns.md)__

    ---

    Understanding DAO/VO patterns and database interaction best practices.

    [:octicons-arrow-right-24: Learn Patterns](database-patterns.md)

-   :material-puzzle:{ .lg .middle } __[Components](components.md)__

    ---

    Vue.js component development and Storybook integration.

    [:octicons-arrow-right-24: Learn Components](components.md)

-   :material-tools:{ .lg .middle } __[Useful Commands](useful-commands.md)__

    ---

    Common development commands and shortcuts.

    [:octicons-arrow-right-24: View Commands](useful-commands.md)

</div>

## Development Workflow

1. **[Set up your environment](../../getting-started/development-setup.md)** - Get Docker running
2. **[Read coding guidelines](coding-guidelines.md)** - Understand our standards
3. **[Write tests](testing.md)** - Ensure your code works
4. **[Submit a PR](../../getting-started/contributing.md)** - Contribute your changes

## Key Principles

### Type Safety
- All code must declare data types
- TypeScript for frontend
- Psalm for PHP
- mypy for Python

### Testing
- All functionality changes must include tests
- Tests must pass 100% before committing
- Write tests first when possible

### Code Quality
- Follow automated linting rules
- Use guard clauses instead of nested conditionals
- Minimize null/undefined usage
- Remove unused code (don't comment it out)

## Related Documentation

- **[Architecture Overview](../architecture/index.md)** - System design
- **[API Reference](../api/index.md)** - API documentation
- **[Getting Started](../../getting-started/index.md)** - Setup and contribution guide

---

**Ready to code?** Start with [Coding Guidelines](coding-guidelines.md)!
