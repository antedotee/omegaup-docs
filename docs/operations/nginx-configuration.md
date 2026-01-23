---
title: Nginx Configuration
description: Web server configuration for omegaUp
icon: bootstrap/web
---

# Nginx Configuration

omegaUp uses Nginx as the web server. This guide covers configuration for development and production environments.

## Basic Configuration

Nginx handles:

- **Static Files**: CSS, JavaScript, images
- **PHP Requests**: Forwarded to PHP-FPM/HHVM
- **HTTPS**: SSL/TLS termination
- **Reverse Proxy**: For Grader and Runner services

## Development Setup

For local development, Nginx is configured via Docker Compose.

## Production Considerations

- **SSL Certificates**: Configured for HTTPS
- **Rate Limiting**: Protection against abuse
- **Caching**: Static asset caching
- **Compression**: Gzip compression enabled

## Related Documentation

- **[Development Setup](../../getting-started/development-setup.md)** - Local environment
- **[Deployment](deployment.md)** - Production deployment
