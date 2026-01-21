---
title: Getting Help
description: Learn how to effectively ask questions and get help from the omegaUp community
---

# Getting Help

We know you'll have questions about how things work at omegaUp—technical questions, process questions, and more. This guide will help you get better answers faster.

## Before Asking

### 1. Search Existing Resources

Before posting a question, search these resources:

#### Documentation
- **This documentation site** - Search for your topic
- **[Development Setup Guide](development-setup.md)** - Installation and setup issues
- **[Architecture Documentation](../architecture/index.md)** - System design questions

#### Community Resources
- **Discord Search** - Search message history in our [#dev_training channel](https://discord.com/invite/K3JFd9d3wk)
  - Discord has a powerful search feature—many questions have been asked before
  - Search by keywords related to your question

#### External Resources
- **Google** - For general questions about Git, Docker, PHP, JavaScript, etc.
  - If your question isn't omegaUp-specific, Google likely has the answer

!!! tip "Search Tips"
    Try different keyword combinations. Often, someone has asked a similar question before.

## Asking Questions Effectively

### Where to Ask

Post your question in the **#dev_training channel** of our [Discord server](https://discord.com/invite/K3JFd9d3wk).

!!! important "Public Channels Only"
    - ✅ Post in public channels (not DMs)
    - ✅ Tag the appropriate channel
    - ❌ Don't send direct messages
    - ❌ Don't tag specific people unnecessarily

### How to Ask

Follow these guidelines to get better answers:

#### 1. Provide Context

Explain what you're trying to do:

```markdown
I'm trying to set up my development environment on macOS, and I'm getting
an error when running `docker compose up`.
```

#### 2. Describe the Problem

Include:
- **What you expected to happen**
- **What actually happened**
- **Steps you followed**
- **Error messages** (copy-paste the full error)
- **Relevant code snippets** (if applicable)
- **Logs** (if applicable)

#### 3. Show What You've Tried

Mention what you've already attempted:

```markdown
I've already tried:
- Reinstalling Docker
- Checking the documentation
- Searching Discord history for similar issues
```

#### 4. Include System Information

If relevant, include:
- Operating system and version
- Docker version
- Node.js version (if applicable)
- Any other relevant environment details

### Example Good Question

```markdown
Hi! I'm setting up the development environment on Ubuntu 22.04 and getting
an error when running `docker compose up`.

**Expected:** Containers should start successfully
**Actual:** Getting "port already in use" error

**Steps I followed:**
1. Installed Docker and Docker Compose
2. Cloned the repository
3. Ran `docker compose up`

**Error message:**
```
ERROR: for frontend  Cannot start service frontend: 
driver failed programming external connectivity on endpoint 
omegaup-frontend-1: Bind for 0.0.0.0:8001 failed: port is already allocated
```

**What I've tried:**
- Checked if port 8001 is in use: `lsof -i :8001`
- Found process using the port and killed it
- Still getting the same error

Any help would be appreciated!
```

### Example Bad Question

```markdown
docker not working help pls
```

!!! failure "Why This Is Bad"
    - No context about what "not working" means
    - No error message
    - No system information
    - No indication of what was tried

## Following Up

### If Your Question Gets Answered

1. **Thank the person** who helped you
2. **Confirm the solution worked**
3. **Update the thread** with what fixed it (if different from the suggested solution)

This helps future people with the same problem!

### If You Solve It Yourself

If you figure out the solution:

1. **Update the thread** explaining how you solved it
2. **Mark it as resolved** (if the platform supports it)

This prevents others from wasting time trying to help after you've already solved it.

### If Your Question Was Asked Before

If you find an existing thread with your question:

- **Reply to that thread** instead of creating a new one
- **Add new information** if your situation differs
- **Ask follow-up questions** in the same thread

This keeps related information together and makes it easier to find.

## Helping Others

We encourage you to **help your peers** with their questions!

### Why Help Others?

- **Learning**: Explaining concepts helps you understand them better
- **Community**: Building a helpful, inclusive community
- **Recognition**: We take helpfulness into account when selecting GSoC candidates

### How to Help

- **Read questions** posted by others regularly
- **Answer questions** you're familiar with
- **Share resources** that might help
- **Be patient and kind** - everyone is learning

## What to Avoid

### ❌ Don't Do These Things

1. **Don't send DMs** - Post in public channels so others can benefit
2. **Don't tag specific people** - Post publicly so anyone can help
3. **Don't repost questions** - Search first, reply to existing threads
4. **Don't ask the same question multiple times** - Be patient for responses

### ✅ Do These Things

1. **Search first** - Check documentation and Discord history
2. **Post publicly** - Use appropriate channels
3. **Be specific** - Provide context, errors, and what you've tried
4. **Follow up** - Update threads when issues are resolved
5. **Help others** - Answer questions you know the answer to

## Additional Resources

### Learning to Ask Better Questions

We recommend reading:
- **[How to Ask Questions the Smart Way](https://www.mikeash.com/getting_answers.html)** - Excellent guide on asking effective questions

### omegaUp-Specific Resources

- **[Development Setup](development-setup.md)** - Environment setup issues
- **[Contributing Guide](contributing.md)** - PR and workflow questions
- **[Architecture Documentation](../architecture/index.md)** - System design questions
- **[API Documentation](../api/index.md)** - API-related questions

### Community Channels

- **Discord**: [#dev_training channel](https://discord.com/invite/K3JFd9d3wk) - Main support channel
- **GitHub Issues**: [Report bugs](https://github.com/omegaup/omegaup/issues) - For confirmed bugs
- **GitHub Discussions**: [General discussions](https://github.com/omegaup/omegaup/discussions) - For feature ideas and discussions

## Summary

1. ✅ **Search first** - Documentation, Discord history, Google
2. ✅ **Ask publicly** - Use appropriate channels, not DMs
3. ✅ **Be specific** - Provide context, errors, steps, system info
4. ✅ **Follow up** - Update threads when resolved
5. ✅ **Help others** - Answer questions you can help with

---

**Still need help?** Join our [Discord server](https://discord.com/invite/K3JFd9d3wk) and ask in the #dev_training channel!
