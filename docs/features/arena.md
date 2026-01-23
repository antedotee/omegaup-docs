---
title: Arena
description: Contest interface and problem-solving environment
icon: bootstrap/play-circle
---

# Arena

Arena is the contest interface where participants solve problems during competitions. It provides a real-time problem-solving environment with live scoreboard updates.

## Features

- **Problem Display**: View problem statements, constraints, and examples
- **Code Editor**: Monaco editor with syntax highlighting
- **Submission**: Submit solutions and view results
- **Scoreboard**: Real-time contest rankings
- **Clarifications**: Ask and view contest clarifications
- **Timer**: Contest countdown timer

## User Flow

```mermaid
flowchart TD
    A[Enter Contest] --> B[View Problems]
    B --> C[Read Problem Statement]
    C --> D[Write Solution]
    D --> E[Submit Code]
    E --> F{Result?}
    F -->|AC| G[Problem Solved]
    F -->|WA/TLE/etc| D
    G --> H[Scoreboard Updated]
    H --> I[Continue to Next Problem]
```

## Related Documentation

- **[Contests](contests/index.md)** - Contest management
- **[Problems](problems/index.md)** - Problem creation
- **[API Reference](../api/index.md)** - Arena API endpoints
