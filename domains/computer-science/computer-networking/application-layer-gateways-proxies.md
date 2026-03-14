---
id: application-layer-gateways-proxies
title: Application-Layer Gateways and Proxies
domain: computer-science
course: computer-networking
prerequisites:
- id: http-hypertext-transfer-protocol
  type: hard
- id: tcp-transmission-control-protocol
  type: hard
tags:
- proxy
- gateway
- application-layer
- filtering
stage: advanced
status: draft
---

# Application-Layer Gateways and Proxies

## Core Idea
Application-layer gateways (proxies) terminate client connections, parse application protocol messages, and make forwarding decisions based on application content rather than just network headers. Proxies can filter malicious content, cache responses, rewrite URLs, and enforce policies on application-specific protocols. They provide stronger security than network-layer firewalls but require protocol-specific logic.
