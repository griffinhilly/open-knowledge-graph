---
id: http-hypertext-transfer-protocol
title: 'HTTP: Hypertext Transfer Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: port-addressing-sockets
  type: hard
builds-toward:
- https-and-tls
tags:
- http
- web
- request-response
- stateless
- methods
stage: advanced
status: draft
---

# HTTP: Hypertext Transfer Protocol

## Core Idea
HTTP is a stateless request-response application protocol used by the World Wide Web. Clients send HTTP requests (GET, POST, etc.) to servers over TCP port 80, and servers respond with status codes (200, 404, 500, etc.) and content. HTTP is the foundation for web applications and APIs.

## How It's Best Learned
Use curl or browser developer tools to inspect HTTP headers and responses; manually construct HTTP requests to understand the protocol format.

## Common Misconceptions
- HTTP is stateless; applications build stateful sessions using cookies or tokens.
- HTTP/1.1 is the current standard; HTTP/3 is now available and uses QUIC instead of TCP.
