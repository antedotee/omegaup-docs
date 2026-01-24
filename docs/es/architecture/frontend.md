---
title: Arquitectura frontal
description: Estructura frontend, componentes Vue.js y organización TypeScript
icon: bootstrap/web
---
# Arquitectura frontal

La interfaz de omegaUp está construida con tecnologías web modernas: Vue.js, TypeScript y Bootstrap 4.

## Pila de tecnología

| Tecnología | Propósito | Versión |
|------------|---------|---------|
| Vue.js | Marco de interfaz de usuario | 2.5.22 |
| Mecanografiado | JavaScript con seguridad de tipos | 4.4.4 |
| Arranque | Marco CSS | 4.6.0 |
| Paquete web | Herramienta de construcción | 5,94 |

## Estructura del directorio

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
## Arquitectura de componentes

Los componentes de Vue están organizados por característica:

- **Componentes**: componentes de interfaz de usuario reutilizables
- **Clientes API**: clases de TypeScript para llamadas API
- **Tipos**: definiciones de tipos de TypeScript
- **Utils**: funciones de utilidad

## Proceso de construcción

Webpack incluye archivos TypeScript y Vue:

1. **TypeScript** → Compilado en JavaScript
2. **Componentes de Vue** → Compilado y empaquetado
3. **Sass** → Compilado en CSS
4. **Activos** → Copiado al directorio de salida

## Documentación relacionada

- **[Guía de componentes](../development/components.md)** - Desarrollo de componentes
- **[Pautas de codificación](../development/coding-guidelines.md)** - Estándares de interfaz
- **[Guía de migración](../development/migration-guide.md)** - Migración de Smarty a Vue
