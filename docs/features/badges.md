---
title: Badges
description: Achievement system implementation
icon: bootstrap/award
---

# Badges

omegaUp includes a badge system to recognize user achievements and milestones.

## Badge Types

- **Problem Solving**: Milestones like "100 Solved Problems"
- **Streaks**: Daily solving streaks (7, 15, 30 days)
- **Expertise**: Language-specific badges (C++ Expert, Python Expert)
- **Course Completion**: Graduation badges for courses
- **Special Events**: Event-specific badges

## Implementation

Badges are implemented using:

- **SQL Queries**: Defined in `frontend/badges/[badge-name]/query.sql`
- **Localization**: Translations in `localizations.json`
- **Icons**: SVG icons for display
- **Tests**: Validation in `test.json`

## Related Documentation

- **[Badge Implementation Guide](../../development/badge-implementation.md)** - How to create new badges
- **[Badges API](../../api/badges.md)** - API endpoints
