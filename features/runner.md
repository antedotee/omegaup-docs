---
title: Runner
description: Code compilation and execution system
---

# Runner

Runners are distributed services responsible for compiling and executing user-submitted code in a secure sandbox environment.

## Overview

Runners are deployed on cloud virtual machines and communicate with the Grader via HTTPS using mutual certificate authentication.

## Key Features

- **Secure Execution**: Uses Minijail sandbox
- **Distributed**: Multiple Runners for scalability
- **Language Support**: C, C++, Java, Python, Ruby, Perl, Pascal, Karel, and more
- **Caching**: Input files cached for efficiency

## API Endpoints

### `/compile/`

Compiles a submission synchronously.

**Input:**
```json
{
  "lang": "cpp",
  "code": ["main.cpp", "helper.cpp"]
}
```

**Output (Success):**
```json
{
  "token": "ABJdfoeKFPer9183409dsfDFPOfkaR834JFDJF="
}
```

**Output (Error):**
```json
{
  "error": "Compilation error message"
}
```

### `/run/`

Executes a compiled program against test cases.

**Input:**
```json
{
  "token": "ABJdfoeKFPer9183409dsfDFPOfkaR834JFDJF=",
  "input": "d41d8cd98f00b204e9800998ecf8427e"
}
```

**Output:**
```json
{
  "results": [
    {
      "name": "05",
      "status": "OK",
      "time": 103,
      "memory": 1235,
      "output": "BlaBlaBla"
    },
    {
      "name": "06",
      "status": "TLE",
      "time": 3000,
      "memory": 1235
    }
  ]
}
```

### `/input/`

Uploads input test cases to Runner cache.

**Input:**
```json
{
  "input": "d41d8cd98f00b204e9800998ecf8427e",
  "cases": [
    {"name": "05", "data": "input data"},
    {"name": "06", "data": "input data"}
  ]
}
```

## Security

- **Minijail**: Linux sandbox for secure execution
- **HTTPS**: Encrypted communication
- **Mutual Authentication**: Certificate-based authentication
- **Isolation**: Each submission runs in isolated environment

## Related Documentation

- **[Grader](grader.md)** - Queue management system
- **[Sandbox](sandbox.md)** - Security and isolation
- **[System Internals](../architecture/internals.md)** - Detailed flow
