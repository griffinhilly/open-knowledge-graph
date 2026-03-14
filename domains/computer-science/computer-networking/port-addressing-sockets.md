---
id: port-addressing-sockets
title: Port Addressing and Sockets
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: udp-user-datagram-protocol
  type: hard
builds-toward:
- socket-programming-basics
- dns-domain-name-system
- http-hypertext-transfer-protocol
tags:
- port
- socket
- demultiplexing
- well-known-ports
- ephemeral-ports
stage: advanced
status: draft
---

# Port Addressing and Sockets

## Core Idea
Ports are 16-bit identifiers that allow multiple applications to use the same transport protocol on a single host. A socket is an endpoint of a network connection, identified by a tuple (IP, protocol, port). Well-known ports (0–1023) are assigned to standard services; ephemeral ports (49152–65535) are assigned dynamically to clients.
