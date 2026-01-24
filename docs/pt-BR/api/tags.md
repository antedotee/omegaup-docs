---
title: API de tags
description: Endpoints de API para tags de problema e categorização
icon: bootstrap/code-tags
---
# API de tags

A API Tags fornece endpoints para pesquisar e recuperar tags problemáticas usadas para categorização e filtragem.

## Visão geral

As tags no omegaUp categorizam os problemas por:

- **Tópico**: Algoritmo ou estrutura de dados (por exemplo, Programação Dinâmica, Gráficos)
- **Nível**: Nível de dificuldade (por exemplo, Básico, Intermediário, Avançado)
- **Fonte**: Origem ou concorrência (por exemplo, IOI, ICPC, OMI)

## Pontos finais

### Listar tags

Pesquisa tags que correspondem a uma consulta.

**`GET /api/tag/list/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `query` | corda | Sim* | Termo de pesquisa |
| `term` | corda | Sim* | Parâmetro de pesquisa alternativo |

*É necessário um dos `query` ou `term`.

**Resposta:**

```json
[
  { "name": "problemTopicDynamicProgramming" },
  { "name": "problemTopicGraphTheory" },
  { "name": "problemTopicGreedy" }
]
```
**Privilégios:** Público (sem necessidade de autenticação)

---

### Obtenha tags frequentes

Retorna as tags usadas com mais frequência para um determinado nível de problema.

**`GET /api/tag/frequentTags/`**

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|------------|
| `problemLevel` | corda | Sim | Tag de nível (por exemplo, `problemLevelBasicKarel`) |
| `rows` | interno | Sim | Número de tags a serem retornadas |

**Resposta:**

```json
{
  "frequent_tags": [
    { "name": "problemTopicLoops", "problemCount": 150 },
    { "name": "problemTopicArrays", "problemCount": 120 },
    { "name": "problemTopicConditionals", "problemCount": 95 }
  ]
}
```
**Privilégios:** Público

---

## Categorias de tags

### Tags de tópico (`problemTopic*`)

Categorias de algoritmo e estrutura de dados:

| Etiqueta | Descrição |
|-----|-------------|
| `problemTopicArrays` | Manipulação de matriz |
| `problemTopicBinarySearch` | Algoritmos de pesquisa binária |
| `problemTopicDynamicProgramming` | Técnicas de PD |
| `problemTopicGraphTheory` | Algoritmos gráficos |
| `problemTopicGreedy` | Algoritmos gananciosos |
| `problemTopicMath` | Problemas matemáticos |
| `problemTopicStrings` | Processamento de strings |
| `problemTopicTrees` | Estruturas de árvores |
| `problemTopicSorting` | Algoritmos de classificação |
| `problemTopicDataStructures` | Estruturas de dados avançadas |
| `problemTopicGeometry` | Geometria computacional |
| `problemTopicNumberTheory` | Teoria dos números |
| `problemTopicCombinatorics` | Combinatória |
| `problemTopicBitmasks` | Operações de máscara de bits |
| `problemTopicSimulation` | Problemas de simulação |

### Tags de nível (`problemLevel*`)

Classificação de dificuldade:

| Etiqueta | Descrição |
|-----|-------------|
| `problemLevelBasicKarel` | Karel nível iniciante |
| `problemLevelBasicIntroductionToProgramming` | Noções básicas de programação |
| `problemLevelIntermediateDataStructuresAndAlgorithms` | DS/Algo intermediário |
| `problemLevelIntermediateMathsInProgramming` | Matemática em programação |
| `problemLevelIntermediateAnalysisAndDesignOfAlgorithms` | Projeto de algoritmo |
| `problemLevelAdvancedCompetitiveProgramming` | Programação competitiva |
| `problemLevelAdvancedSpecializedTopics` | Avançado especializado |

### Tags públicas (`problemTag*`)

Categorização refinada para problemas públicos:

| Etiqueta | Descrição |
|-----|-------------|
| `problemTagArithmetic` | Aritmética básica |
| `problemTagConditionals` | Declarações if/else |
| `problemTagLoops` | Construções de loop |
| `problemTagFunctions` | Funções e procedimentos |
| `problemTagRecursion` | Soluções recursivas |
| `problemTagDynamicProgramming` | Problemas de DP |
| `problemTagBreadthFirstSearch` | Travessia BFS |
| `problemTagDepthFirstSearch` | Travessia DFS |
| `problemTagShortestPaths` | Algoritmos de caminho mais curto |
| ... | (muitos mais disponíveis) |

### Tags de competição

Tags de origem/origem:

| Etiqueta | Descrição |
|-----|-------------|
| `problemTagIOI` | Olimpíada Internacional de Informática |
| `problemTagICPC` | Concurso Internacional de Programação Universitária |
| `problemTagOMI` | Olimpíada Mexicana de Informática |
| `problemTagCOCI` | Competição Aberta da Croácia |
| `problemTagBOI` | Olimpíada do Báltico |

---

## Normalização de tags

As tags são normalizadas antes do armazenamento:

1. Converta para minúsculas
2. Remova acentos
3. Substitua não alfanumérico por hífens
4. Recolher vários hífens

```php
// Example: "Árbol Binário!" → "arbol-binario"
```
---

## Casos de uso

### Pesquisa por tags (preenchimento automático)

```javascript
// Search tags as user types
const response = await fetch('/api/tag/list/?query=graph');
const tags = await response.json();
// Returns: [{ name: "problemTopicGraphTheory" }, ...]
```
### Obtenha tags populares para um nível

```javascript
// Get top 10 tags for basic programming
const response = await fetch(
  '/api/tag/frequentTags/?problemLevel=problemLevelBasicIntroductionToProgramming&rows=10'
);
const { frequent_tags } = await response.json();
```
### Filtrar problemas por tag

As tags são usadas com a API Problems para filtrar:

```bash
# Get problems with a specific tag
curl "https://omegaup.com/api/problem/list/?tag=problemTopicDynamicProgramming"
```
---

## Fontes de tags

As tags vêm de:

1. **Autores do problema**: Adicionado durante a criação do problema
2. **Nomeações de qualidade**: sugestões da comunidade
3. **Revisores de qualidade**: atribuições de tags oficiais
4. **Sistema**: Categorização automática

---

## Documentação Relacionada

- **[API de problemas](problems.md)** - Listagem de problemas com filtros de tags
- **[API de nomeações de qualidade](quality-nominations.md)** - Sugestões de tags

## Referência completa

Para listas completas de tags e implementação, consulte [Tag Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/Tag.php) e [QualityNomination Controller](https://github.com/omegaup/omegaup/blob/main/frontend/server/src/Controllers/QualityNomination.php) para tags permitidas.
