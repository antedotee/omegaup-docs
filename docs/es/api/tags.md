---
title: Etiquetas API
description: Puntos finales API para etiquetas y categorización de problemas
icon: bootstrap/code-tags
---
# Etiquetas API

La API de etiquetas proporciona puntos finales para buscar y recuperar etiquetas problemáticas utilizadas para la categorización y el filtrado.

## Descripción general

Las etiquetas en omegaUp clasifican los problemas por:

- **Tema**: Algoritmo o estructura de datos (por ejemplo, programación dinámica, gráficos)
- **Nivel**: nivel de dificultad (por ejemplo, básico, intermedio, avanzado)
- **Fuente**: Origen o competencia (por ejemplo, IOI, ICPC, OMI)

## Puntos finales

### Etiquetas de lista

Busca etiquetas que coincidan con una consulta.

**`GET /api/tag/list/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `query` | cadena | Sí* | Término de búsqueda |
| `term` | cadena | Sí* | Parámetro de búsqueda alternativo |

*Se requiere uno de `query` o `term`.

**Respuesta:**

```json
[
  { "name": "problemTopicDynamicProgramming" },
  { "name": "problemTopicGraphTheory" },
  { "name": "problemTopicGreedy" }
]
```
**Privilegios:** Público (no se requiere autenticación)

---

### Obtener etiquetas frecuentes

Devuelve las etiquetas utilizadas con más frecuencia para un nivel de problema determinado.

**`GET /api/tag/frequentTags/`**

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|----------|-------------|
| `problemLevel` | cadena | Sí | Etiqueta de nivel (por ejemplo, `problemLevelBasicKarel`) |
| `rows` | entero | Sí | Número de etiquetas a devolver |

**Respuesta:**

```json
{
  "frequent_tags": [
    { "name": "problemTopicLoops", "problemCount": 150 },
    { "name": "problemTopicArrays", "problemCount": 120 },
    { "name": "problemTopicConditionals", "problemCount": 95 }
  ]
}
```
**Privilegios:** Público

---

## Categorías de etiquetas

### Etiquetas de tema (`problemTopic*`)

Categorías de algoritmos y estructuras de datos:

| Etiqueta | Descripción |
|-----|-------------|
| `problemTopicArrays` | Manipulación de matrices |
| `problemTopicBinarySearch` | Algoritmos de búsqueda binaria |
| `problemTopicDynamicProgramming` | Técnicas de DP |
| `problemTopicGraphTheory` | Algoritmos gráficos |
| `problemTopicGreedy` | Algoritmos codiciosos |
| `problemTopicMath` | Problemas matemáticos |
| `problemTopicStrings` | Procesamiento de cadenas |
| `problemTopicTrees` | Estructuras de árboles |
| `problemTopicSorting` | Algoritmos de clasificación |
| `problemTopicDataStructures` | Estructuras de datos avanzadas |
| `problemTopicGeometry` | Geometría computacional |
| `problemTopicNumberTheory` | Teoría de números |
| `problemTopicCombinatorics` | Combinatoria |
| `problemTopicBitmasks` | Operaciones de máscara de bits |
| `problemTopicSimulation` | Problemas de simulación |

### Etiquetas de nivel (`problemLevel*`)

Clasificación de dificultad:

| Etiqueta | Descripción |
|-----|-------------|
| `problemLevelBasicKarel` | Karel nivel principiante |
| `problemLevelBasicIntroductionToProgramming` | Conceptos básicos de programación |
| `problemLevelIntermediateDataStructuresAndAlgorithms` | DS/Algo intermedio |
| `problemLevelIntermediateMathsInProgramming` | Matemáticas en programación |
| `problemLevelIntermediateAnalysisAndDesignOfAlgorithms` | Diseño de algoritmos |
| `problemLevelAdvancedCompetitiveProgramming` | Programación competitiva |
| `problemLevelAdvancedSpecializedTopics` | Avanzado especializado |

### Etiquetas públicas (`problemTag*`)

Categorización detallada de problemas públicos:

| Etiqueta | Descripción |
|-----|-------------|
| `problemTagArithmetic` | Aritmética básica |
| `problemTagConditionals` | Declaraciones if/else |
| `problemTagLoops` | Construcciones de bucle |
| `problemTagFunctions` | Funciones y procedimientos |
| `problemTagRecursion` | Soluciones recursivas |
| `problemTagDynamicProgramming` | Problemas de PD |
| `problemTagBreadthFirstSearch` | Recorrido BFS |
| `problemTagDepthFirstSearch` | Recorrido DFS |
| `problemTagShortestPaths` | Algoritmos de ruta más corta |
| ... | (muchos más disponibles) |

### Etiquetas de competencia

Etiquetas de fuente/origen:

| Etiqueta | Descripción |
|-----|-------------|
| `problemTagIOI` | Olimpiada Internacional de Informática |
| `problemTagICPC` | Concurso Internacional de Programación Universitaria |
| `problemTagOMI` | Olimpiada Mexicana de Informática |
| `problemTagCOCI` | Competición Abierta de Croacia |
| `problemTagBOI` | Olimpiada del Báltico |

---

## Normalización de etiquetas

Las etiquetas se normalizan antes del almacenamiento:

1. Convertir a minúsculas
2. Quitar acentos
3. Reemplace los no alfanuméricos con guiones.
4. Contraer varios guiones

```php
// Example: "Árbol Binário!" → "arbol-binario"
```
---

## Casos de uso

### Buscar etiquetas (Autocompletar)

```javascript
// Search tags as user types
const response = await fetch('/api/tag/list/?query=graph');
const tags = await response.json();
// Returns: [{ name: "problemTopicGraphTheory" }, ...]
```
### Obtener etiquetas populares para un nivel

```javascript
// Get top 10 tags for basic programming
const response = await fetch(
  '/api/tag/frequentTags/?problemLevel=problemLevelBasicIntroductionToProgramming&rows=10'
);
const { frequent_tags } = await response.json();
```
### Filtrar problemas por etiqueta

Las etiquetas se utilizan con la API de Problemas para filtrar:

```bash
# Get problems with a specific tag
curl "https://omegaup.com/api/problem/list/?tag=problemTopicDynamicProgramming"
```
---

## Fuentes de etiquetas

Las etiquetas provienen de:

1. **Autores del problema**: agregado durante la creación del problema
2. **Nominaciones de calidad**: sugerencias de la comunidad
3. **Revisores de calidad**: Asignaciones de etiquetas oficiales
4. **Sistema**: Categorización automática

---

## Documentación relacionada

- **[API de problemas](problems.md)** - Listado de problemas con filtros de etiquetas
- **[API de nominaciones de calidad](quality-nominations.md)** - Sugerencias de etiquetas

## Referencia completa

Para obtener listas completas de etiquetas e implementación, consulte el [Controlador de etiquetas](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Tag.php) y el [Controlador de QualityNomination](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/QualityNomination.php) para conocer las etiquetas permitidas.
