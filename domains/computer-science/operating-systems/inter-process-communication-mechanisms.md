---
id: inter-process-communication-mechanisms
title: Inter-Process Communication Mechanisms
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication
  type: hard
- id: process-concept-in-os
  type: soft
builds-toward:
- pipes-and-named-pipes-ipc
- sockets-and-network-ipc
- shared-memory-inter-process-communication
- message-queues-ipc-systems
tags:
- ipc
- communication
- processes
stage: formal-systems
status: draft
---

# Inter-Process Communication Mechanisms

## Core Idea
IPC mechanisms enable independent processes to exchange data and synchronize actions. Major categories include pipes/FIFOs, sockets, shared memory, and message queues, each with different trade-offs in performance, coupling, and use cases. Choosing the right IPC mechanism depends on whether processes are local/remote, synchronous/asynchronous, and whether unidirectional or bidirectional communication is needed.
