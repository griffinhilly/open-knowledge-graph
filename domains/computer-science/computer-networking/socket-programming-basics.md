---
id: socket-programming-basics
title: Socket Programming and Network APIs
domain: computer-science
course: computer-networking
prerequisites:
- id: port-addressing-sockets
  type: hard
- id: system-calls
  type: hard
tags:
- socket-api
- programming
- tcp-client
- udp-client
- bind-listen-accept
stage: advanced
status: draft
---

# Socket Programming and Network APIs

## Core Idea
Sockets are the primary API for network programming. TCP servers use socket(), bind(), listen(), and accept() to receive connections; clients use socket() and connect(). UDP uses sendto() and recvfrom(). Understanding socket semantics is essential for building networked applications.
