# Sistema de contenido dinámico GSoC

Este directorio utiliza un enfoque basado en datos para generar páginas GSoC, eliminando la necesidad de copiar y pegar contenido entre años.

## Cómo funciona

1. **Archivo de datos**: todo el contenido específico del año se almacena en `_data/gsoc-data.json`
2. **Secuencia de comandos del generador**: `scripts/generate-gsoc-pages.py` lee los datos y genera archivos de rebajas
3. **Páginas generadas**: el script crea archivos `YYYY.md` para cada año.

## Agregar un año nuevo

### Para el año actual (con ideas de proyectos):

1. Abra `_data/gsoc-data.json`
2. Agregue una nueva entrada en `years` con el año como clave:
   ```json
   "2026": {
     "type": "current",
     "title": "GSoC 2026",
     "description": "Google Summer of Code 2026 program at omegaUp",
     "intro": "Your introduction text here...",
     "project_ideas": [...],
     "application_process": {...},
     "communications": [...],
     "faq": [...],
     "related_docs": [...]
   }
   ```
3. Actualice el `type` del año anterior a `"past"` y agregue la matriz `projects` en lugar de `project_ideas`.
4. Ejecute el generador:
   ```bash
   python3 scripts/generate-gsoc-pages.py
   ```
5. Revise los archivos generados y confírmelos.

### Para el año pasado (proyectos completados):

1. Abra `_data/gsoc-data.json`
2. Agregue una nueva entrada en `years`:
   ```json
   "2025": {
     "type": "past",
     "title": "GSoC 2025",
     "description": "Google Summer of Code 2025 projects",
     "intro": "Projects completed during GSoC 2025.",
     "projects": [
       {
         "name": "Project Name",
         "description": "Project description",
         "result": "Project result/outcome"
       }
     ],
     "related_docs": [...]
   }
   ```
3. Ejecute el script del generador.
4. Revisar y comprometerse

## Actualización del contenido existente

Simplemente edite `_data/gsoc-data.json` y ejecute el script del generador. Todas las páginas se regenerarán con el contenido actualizado.

## Beneficios

- **Sin errores de copiar y pegar**: fuente única de verdad para el contenido compartido
- **Consistencia**: todas las páginas siguen la misma estructura
- **Actualizaciones fáciles**: actualiza el archivo de datos una vez, regenera todas las páginas
- **Control de versiones**: el archivo de datos muestra exactamente qué cambió entre años

## Estructura de archivos

```
gsoc/
├── _data/
│   └── gsoc-data.json      # Single source of truth
├── _templates/             # (Legacy - not used anymore)
├── 2023.md                 # Generated file
├── 2024.md                 # Generated file
├── 2025.md                 # Generated file
├── index.md                # Manual file (not generated)
└── README.md               # This file
```
## Notas

- El script del generador utiliza sólo la biblioteca estándar de Python (sin dependencias externas)
- Los archivos generados deben enviarse a git.
- El archivo de datos (`gsoc-data.json`) es la fuente de la verdad; edítelo, no los archivos de rebajas generados.
- Ejecute siempre el generador después de actualizar el archivo de datos.
