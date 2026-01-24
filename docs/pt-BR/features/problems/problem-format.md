---
title: Formato do problema
description: Estrutura de arquivo ZIP para criação manual de problemas
icon: bootstrap/file-document
---
# Formato do problema

Para criação avançada de problemas, você pode criar manualmente um arquivo `.zip` com a estrutura adequada.

## Estrutura do arquivo ZIP

```
problem.zip
├── statements/
│   ├── es.markdown      # Spanish statement
│   ├── en.markdown      # English statement
│   └── pt.markdown      # Portuguese statement
├── cases/
│   ├── 01.in
│   ├── 01.out
│   ├── 02.in
│   ├── 02.out
│   └── ...
├── validator.cpp         # Optional: Custom validator
├── limits.json           # Optional: Custom limits
└── testplan              # Optional: Test case weights
```
## Formato da declaração

As declarações são escritas em Markdown:

```markdown
# Problem Title

## Description

Problem description here...

## Input

Input format description...

## Output

Output format description...

## Examples

### Example 1

**Input:**
```
1 2
```

**Output:**
```
3
```
```
## Casos de teste

Os casos de teste são pares de arquivos `.in` e `.out`:

-`01.in`, `01.out`
-`02.in`, `02.out`
-`03.in`, `03.out`
- ...

## Validador

Se estiver usando um validador personalizado, inclua o código-fonte (por exemplo, `validator.cpp`).

## Documentação Relacionada

- **[Criando Problemas](creating-problems.md)** - Guia de criação de problemas
- **[Guia ZIP manual](../../../frontend/www/docs/Manual-for-Zip-File-Creation-for-Problems.md)** - Especificação detalhada do formato
