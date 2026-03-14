---
id: https-and-tls
title: HTTPS and TLS (Transport Layer Security)
domain: computer-science
course: computer-networking
prerequisites:
- id: http-hypertext-transfer-protocol
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- https
- tls
- ssl
- encryption
- certificate
- public-key
stage: advanced
status: draft
---

# HTTPS and TLS (Transport Layer Security)

## Core Idea
HTTPS wraps HTTP with TLS (formerly SSL), adding encryption and authentication. TLS uses public-key cryptography to establish a secure session, then switches to symmetric encryption for efficiency. X.509 certificates prove server identity, protecting against man-in-the-middle attacks.
