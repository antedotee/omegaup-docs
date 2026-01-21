---
title: Getting Started
description: Start your journey contributing to omegaUp
---

![omegaUp Logo](assets/images/omegaup.svg){ width="200" }

# Getting Started with omegaUp Development

Welcome! This guide will help you get started with contributing to omegaUp, a free educational platform that helps improve programming skills.

## What is omegaUp?

omegaUp is an educational programming platform used by tens of thousands of students and teachers in Latin America. It provides:

- **Problem Solving**: Thousands of programming problems with automatic evaluation
- **Contests**: Organize programming competitions
- **Courses**: Structured learning paths
- **Training**: Practice problems organized by topic and difficulty

## Before You Begin

If you're new to omegaUp, we recommend:

1. **Experience the Platform**: Visit [omegaUp.com](https://omegaup.com/), create an account, and solve a few problems
2. **Learn About Us**: Explore [omegaup.org](https://omegaup.org/) to learn more about our organization
3. **Understand the Codebase**: Review the [Architecture Overview](../architecture/index.md) to understand how omegaUp works

## Quick Start Path

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } __[Development Setup](development-setup.md)__

    ---

    Set up your local development environment using Docker. This is the first step to start contributing.

    [:octicons-arrow-right-24: Setup Guide](development-setup.md)

-   :material-source-branch:{ .lg .middle } __[Contributing Guide](contributing.md)__

    ---

    Learn how to fork the repository, create branches, and submit pull requests.

    [:octicons-arrow-right-24: Contribute](contributing.md)

-   :material-help-circle:{ .lg .middle } __[Getting Help](getting-help.md)__

    ---

    Stuck? Learn how to ask questions effectively and get help from the community.

    [:octicons-arrow-right-24: Get Help](getting-help.md)

</div>

## Development Environment Overview

omegaUp uses Docker for local development. The main components include:

- **Frontend**: PHP + MySQL (MVC architecture)
- **Backend**: Go-based grader and runner system
- **Frontend UI**: Vue.js + TypeScript + Bootstrap 4
- **Database**: MySQL 8.0.39

## Development Accounts

When you set up your local environment, you'll have access to two pre-configured accounts:

| Username | Password | Role |
|----------|----------|------|
| `omegaup` | `omegaup` | Administrator |
| `user` | `user` | Regular user |

## Next Steps

1. **[Set up your development environment](development-setup.md)** - Get Docker running and clone the repository
2. **[Read the contributing guide](contributing.md)** - Learn the workflow for submitting changes
3. **[Explore the architecture](../architecture/index.md)** - Understand how omegaUp is structured
4. **[Review coding guidelines](../development/coding-guidelines.md)** - Learn our coding standards

## Resources

- **Website**: [omegaup.com](https://omegaup.com)
- **GitHub**: [github.com/omegaup/omegaup](https://github.com/omegaup/omegaup)
- **Discord**: [Join our Discord server](https://discord.com/invite/K3JFd9d3wk) for community support
- **Issues**: [Report bugs or request features](https://github.com/omegaup/omegaup/issues)

---

Ready to start? Head to [Development Setup](development-setup.md) to begin!
