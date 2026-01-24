---
title: Glossary
description: Terminology and definitions used in omegaUp
icon: bootstrap/book
---

# Glossary

Comprehensive reference of terms and definitions used throughout omegaUp documentation and the platform.

---

## General Terms

### omegaUp
The educational programming platform that helps students improve their programming skills through practice problems, contests, and courses.

### Problem
A programming challenge consisting of a problem statement, input/output specifications, constraints, and test cases. Problems are the core unit of content on omegaUp.

### Contest
A timed programming competition where participants solve a set of problems. Contests have defined start/end times, scoring rules, and may include features like virtual participation.

### Course
A structured learning path containing assignments with problems, organized by topics. Courses include progress tracking and deadlines.

### Submission (Run)
Code submitted by a user to solve a problem. Each submission is compiled, executed against test cases, and assigned a verdict.

### Arena
The contest interface where participants solve problems during competitions. Provides real-time scoreboard, code editor, and submission system.

---

## User Roles

### Contestant / Participant
A user participating in a contest or practicing problems.

### Problem Setter
A user who creates problems for omegaUp. Problem setters define statements, test cases, and validators.

### Contest Organizer
A user who creates and manages contests. Can add problems, manage participants, and configure contest settings.

### Course Administrator
A user who manages courses, assigns problems, tracks student progress, and reviews submissions.

### Teaching Assistant (TA)
A course helper who can provide code reviews and answer student clarifications.

### System Administrator (Sysadmin)
A user with full administrative access to the omegaUp platform.

---

## Technical Terms

### Grader
The Go microservice that manages the submission queue and coordinates evaluation. The Grader receives submissions from the frontend, assigns them to Runners, and stores results.

### Runner
A service instance that compiles and executes user-submitted code in a secure sandbox. Multiple Runners can operate in parallel to handle submission load.

### Minijail
The Linux sandbox used for secure code execution, forked from Chrome OS. Provides process isolation, syscall filtering, and resource limits.

### GitServer
The service that manages problem repositories using Git. Provides version control, branch management, and content serving for problems.

### Broadcaster
The WebSocket server that delivers real-time updates to clients, including scoreboard changes, verdict notifications, and clarifications.

### DAO (Data Access Object)
PHP classes that handle database interactions. DAOs provide methods for CRUD operations on database tables.

### VO (Value Object)
PHP classes that map to database tables. VOs represent individual database records with typed properties.

### MVC (Model-View-Controller)
The architectural pattern used in omegaUp's PHP application. Controllers handle business logic, DAOs/VOs handle data, and templates handle presentation.

### Controller
PHP classes that implement API endpoints and business logic. Located in `frontend/server/src/Controllers/`.

---

## Verdicts

### AC (Accepted)
The solution produces correct output for all test cases and passes within resource limits.

### PA (Partially Accepted)
The solution passes some but not all test cases. Used with partial scoring problems.

### WA (Wrong Answer)
The solution produces incorrect output for one or more test cases.

### TLE (Time Limit Exceeded)
The solution exceeded the time limit on one or more test cases.

### MLE (Memory Limit Exceeded)
The solution exceeded the memory limit during execution.

### RTE (Runtime Error)
The solution crashed during execution (e.g., segmentation fault, division by zero, stack overflow).

### CE (Compilation Error)
The code failed to compile. Common causes: syntax errors, missing includes, type mismatches.

### JE (Judge Error)
An internal error occurred during evaluation. Typically indicates a problem with the test data or validator.

### OLE (Output Limit Exceeded)
The solution produced too much output, exceeding the allowed limit.

---

## Contest Scoring

### IOI Style
Scoring model where each test case awards partial points. Final score is the sum of points from all test cases.

### ICPC Style
Scoring model where problems are worth equal points (typically 1). Penalty time is added for wrong submissions.

### Penalty
Time-based or submission-based deduction in ICPC-style contests. Typically 20 minutes per wrong submission.

### Scoreboard Freeze
Period before contest end when the scoreboard stops updating publicly, creating suspense for final results.

### Virtual Contest
Simulating a past contest under original time conditions. Allows practice with historical contests.

---

## Problem Components

### Statement
The problem description including the task, input/output format, constraints, and examples.

### Test Case
A pair of input data and expected output used to evaluate submissions.

### Test Group
A collection of related test cases, often with shared points. Used for subtask scoring.

### Validator
A program that checks solution output, especially for problems with multiple valid answers.

### Interactive Problem
A problem where the solution must interact with a judge program through standard I/O.

### Generator
A program that creates test cases, typically for large or randomized inputs.

### Subtask
A subset of test cases with specific constraints, allowing partial credit for simpler solutions.

---

## Problem Settings

### Time Limit
Maximum execution time allowed per test case, in seconds (e.g., 1.0s, 2.0s).

### Memory Limit
Maximum memory the solution can use, in bytes or megabytes (e.g., 256 MB).

### Output Limit
Maximum size of solution output, prevents infinite printing.

### Validator Type
How output is compared: `token-caseless`, `token-numeric`, `literal`, or `custom`.

### Problem Visibility
Access level: `private` (owner only), `public` (anyone), or contest-specific.

---

## API Terms

### Endpoint
A specific API URL that handles a particular operation (e.g., `/api/Problem/create/`).

### Request Parameter
Data sent to an API endpoint, either in the URL query string or request body.

### Response
JSON data returned by an API endpoint, including status and requested data.

### Authentication Token
The `ouat` cookie that identifies and authenticates users for API requests.

### Rate Limiting
Restriction on API call frequency to prevent abuse. Limits vary by endpoint.

---

## Infrastructure Terms

### Redis
In-memory data store used for session storage, caching, and real-time messaging.

### RabbitMQ
Message queue used for asynchronous task processing, such as certificate generation.

### PHP-FPM
PHP FastCGI Process Manager that handles PHP request processing.

### Nginx
Web server and reverse proxy that routes requests to appropriate backend services.

### Docker
Containerization platform used for development and deployment environments.

---

## Development Terms

### PR (Pull Request)
A proposed code change submitted for review before merging into the main codebase.

### CI (Continuous Integration)
Automated testing that runs on every code change to ensure quality.

### Linter
Tool that checks code for style and potential errors (e.g., ESLint, Psalm).

### Migration
Database schema change script that updates the database structure.

### Fixture
Test data used to set up a known state for testing.

---

## Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| API | Application Programming Interface |
| CRUD | Create, Read, Update, Delete |
| CSRF | Cross-Site Request Forgery |
| DAO | Data Access Object |
| GSoC | Google Summer of Code |
| ICPC | International Collegiate Programming Contest |
| IOI | International Olympiad in Informatics |
| JSON | JavaScript Object Notation |
| JWT | JSON Web Token |
| MVC | Model-View-Controller |
| REST | Representational State Transfer |
| SQL | Structured Query Language |
| TLS | Transport Layer Security |
| VO | Value Object |
| WS | WebSocket |
| XSS | Cross-Site Scripting |

---

## Related Documentation

- **[Architecture Overview](../architecture/index.md)** - System architecture
- **[API Reference](../api/index.md)** - API documentation
- **[Verdicts](../features/verdicts.md)** - Detailed verdict information
- **[Development Guides](../development/index.md)** - Developer resources
