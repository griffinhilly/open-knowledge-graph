---
id: sockets-and-network-ipc
title: Sockets and Network Inter-Process Communication
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication-mechanisms
  type: hard
tags:
- ipc
- sockets
- networking
stage: formal-systems
status: draft
---

# Sockets and Network Inter-Process Communication

## Core Idea
Sockets are the primary mechanism for network communication and can also be used for local IPC via Unix domain sockets. TCP sockets provide reliable, connection-oriented communication; UDP sockets provide connectionless, datagram-based communication. Unix domain sockets enable efficient local inter-process communication without network stack overhead.
