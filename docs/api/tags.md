---
title: Tags API
description: API endpoints for problem tags and categorization
icon: bootstrap/code-tags
---

# Tags API

The Tags API provides endpoints for searching and retrieving problem tags used for categorization and filtering.

## Overview

Tags in omegaUp categorize problems by:

- **Topic**: Algorithm or data structure (e.g., Dynamic Programming, Graphs)
- **Level**: Difficulty tier (e.g., Basic, Intermediate, Advanced)
- **Source**: Origin or competition (e.g., IOI, ICPC, OMI)

## Endpoints

### List Tags

Searches for tags matching a query.

**`GET /api/tag/list/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes* | Search term |
| `term` | string | Yes* | Alternative search parameter |

*One of `query` or `term` is required.

**Response:**

```json
[
  { "name": "problemTopicDynamicProgramming" },
  { "name": "problemTopicGraphTheory" },
  { "name": "problemTopicGreedy" }
]
```

**Privileges:** Public (no authentication required)

---

### Get Frequent Tags

Returns the most frequently used tags for a given problem level.

**`GET /api/tag/frequentTags/`**

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `problemLevel` | string | Yes | Level tag (e.g., `problemLevelBasicKarel`) |
| `rows` | int | Yes | Number of tags to return |

**Response:**

```json
{
  "frequent_tags": [
    { "name": "problemTopicLoops", "problemCount": 150 },
    { "name": "problemTopicArrays", "problemCount": 120 },
    { "name": "problemTopicConditionals", "problemCount": 95 }
  ]
}
```

**Privileges:** Public

---

## Tag Categories

### Topic Tags (`problemTopic*`)

Algorithm and data structure categories:

| Tag | Description |
|-----|-------------|
| `problemTopicArrays` | Array manipulation |
| `problemTopicBinarySearch` | Binary search algorithms |
| `problemTopicDynamicProgramming` | DP techniques |
| `problemTopicGraphTheory` | Graph algorithms |
| `problemTopicGreedy` | Greedy algorithms |
| `problemTopicMath` | Mathematical problems |
| `problemTopicStrings` | String processing |
| `problemTopicTrees` | Tree structures |
| `problemTopicSorting` | Sorting algorithms |
| `problemTopicDataStructures` | Advanced data structures |
| `problemTopicGeometry` | Computational geometry |
| `problemTopicNumberTheory` | Number theory |
| `problemTopicCombinatorics` | Combinatorics |
| `problemTopicBitmasks` | Bitmask operations |
| `problemTopicSimulation` | Simulation problems |

### Level Tags (`problemLevel*`)

Difficulty classification:

| Tag | Description |
|-----|-------------|
| `problemLevelBasicKarel` | Karel beginner level |
| `problemLevelBasicIntroductionToProgramming` | Programming basics |
| `problemLevelIntermediateDataStructuresAndAlgorithms` | Intermediate DS/Algo |
| `problemLevelIntermediateMathsInProgramming` | Math in programming |
| `problemLevelIntermediateAnalysisAndDesignOfAlgorithms` | Algorithm design |
| `problemLevelAdvancedCompetitiveProgramming` | Competitive programming |
| `problemLevelAdvancedSpecializedTopics` | Specialized advanced |

### Public Tags (`problemTag*`)

Fine-grained categorization for public problems:

| Tag | Description |
|-----|-------------|
| `problemTagArithmetic` | Basic arithmetic |
| `problemTagConditionals` | If/else statements |
| `problemTagLoops` | Loop constructs |
| `problemTagFunctions` | Functions and procedures |
| `problemTagRecursion` | Recursive solutions |
| `problemTagDynamicProgramming` | DP problems |
| `problemTagBreadthFirstSearch` | BFS traversal |
| `problemTagDepthFirstSearch` | DFS traversal |
| `problemTagShortestPaths` | Shortest path algorithms |
| ... | (many more available) |

### Competition Tags

Source/origin tags:

| Tag | Description |
|-----|-------------|
| `problemTagIOI` | International Olympiad in Informatics |
| `problemTagICPC` | International Collegiate Programming Contest |
| `problemTagOMI` | Mexican Olympiad in Informatics |
| `problemTagCOCI` | Croatian Open Competition |
| `problemTagBOI` | Baltic Olympiad |

---

## Tag Normalization

Tags are normalized before storage:

1. Convert to lowercase
2. Remove accents
3. Replace non-alphanumeric with hyphens
4. Collapse multiple hyphens

```php
// Example: "Árbol Binário!" → "arbol-binario"
```

---

## Use Cases

### Search for Tags (Autocomplete)

```javascript
// Search tags as user types
const response = await fetch('/api/tag/list/?query=graph');
const tags = await response.json();
// Returns: [{ name: "problemTopicGraphTheory" }, ...]
```

### Get Popular Tags for a Level

```javascript
// Get top 10 tags for basic programming
const response = await fetch(
  '/api/tag/frequentTags/?problemLevel=problemLevelBasicIntroductionToProgramming&rows=10'
);
const { frequent_tags } = await response.json();
```

### Filter Problems by Tag

Tags are used with the Problems API to filter:

```bash
# Get problems with a specific tag
curl "https://omegaup.com/api/problem/list/?tag=problemTopicDynamicProgramming"
```

---

## Tag Sources

Tags come from:

1. **Problem authors**: Added during problem creation
2. **Quality nominations**: Community suggestions
3. **Quality reviewers**: Official tag assignments
4. **System**: Automatic categorization

---

## Related Documentation

- **[Problems API](problems.md)** - Problem listing with tag filters
- **[Quality Nominations API](quality-nominations.md)** - Tag suggestions

## Full Reference

For complete tag lists and implementation, see the [Tag Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Tag.php) and [QualityNomination Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/QualityNomination.php) for allowed tags.
