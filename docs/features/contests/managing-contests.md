---
title: Managing Contests
description: Guide to creating and managing programming contests
icon: bootstrap/cog
---

# Managing Contests

Complete guide to creating and managing programming contests in omegaUp.

## Creating a Contest

### Basic Information

- **Title**: Contest name
- **Alias**: Short identifier (used in URLs)
- **Description**: Contest description
- **Start Time**: When the contest begins
- **End Time**: When the contest ends
- **Public/Private**: Visibility setting

### Advanced Settings

- **Window Length**: USACO-style individual timers
- **Scoreboard Visibility**: Percentage of time scoreboard is visible
- **Points Decay**: Time-based score decay factor
- **Penalty Policy**: How penalties are calculated
- **Submission Gap**: Seconds between submissions

## Contest Types

### Standard Contest
- Fixed start and end time
- Shared timer for all participants
- Traditional contest format

### Virtual Contest (USACO-style)
- Individual timer per participant
- Starts when participant enters
- Window-based duration

## Managing Problems

Add problems to your contest:

1. Create or select problems
2. Set point values
3. Order problems
4. Configure problem-specific settings

## Managing Participants

### Public Contests
- Open to all users
- No invitation needed

### Private Contests
- Invite specific users
- Manage participant list
- Control access

## Scoreboard Configuration

- **Visibility**: Control when scoreboard is visible
- **Freeze**: Freeze scoreboard before contest ends
- **Refresh**: Real-time updates via WebSocket

## Related Documentation

- **[Contests API](../../api/contests.md)** - API endpoints
- **[Arena](../arena.md)** - Contest interface
- **[Running Contests](../../../frontend/www/docs/Run-a-contest-at-your-school.md)** - User guide
