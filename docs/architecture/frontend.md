---
title: Frontend Architecture
description: Frontend structure, Vue.js components, and TypeScript organization
---

# Frontend Architecture

omegaUp's frontend is built with modern web technologies: Vue.js, TypeScript, and Bootstrap 4.

## Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| Vue.js | UI Framework | 2.5.22 |
| TypeScript | Type-safe JavaScript | 4.4.4 |
| Bootstrap | CSS Framework | 4.6.0 |
| Webpack | Build Tool | 5.94 |

## Directory Structure

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

## Component Architecture

Vue components are organized by feature:

- **Components**: Reusable UI components
- **API Clients**: TypeScript classes for API calls
- **Types**: TypeScript type definitions
- **Utils**: Utility functions

## Build Process

Webpack bundles TypeScript and Vue files:

1. **TypeScript** → Compiled to JavaScript
2. **Vue Components** → Compiled and bundled
3. **Sass** → Compiled to CSS
4. **Assets** → Copied to output directory

## Related Documentation

- **[Components Guide](../development/components.md)** - Component development
- **[Coding Guidelines](../development/coding-guidelines.md)** - Frontend standards
- **[Migration Guide](../development/migration-guide.md)** - Migrating from Smarty to Vue
