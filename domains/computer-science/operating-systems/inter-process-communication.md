---
id: inter-process-communication
title: Inter-Process Communication (IPC)
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
- id: system-calls
  type: hard
builds-toward:
- synchronization-problem
tags:
- IPC
- pipes
- message-passing
- shared-memory
- sockets
stage: formal-systems
status: validated
---

# Inter-Process Communication (IPC)

## Core Idea
Because processes have separate address spaces, the OS must provide mechanisms for them to exchange data and coordinate. The two fundamental IPC models are message passing (processes exchange messages through kernel-managed channels like pipes, message queues, or sockets — simpler but involves copying data through the kernel) and shared memory (processes map the same physical memory region into their address spaces for direct, low-latency communication — faster but requires explicit synchronization). Pipes are the canonical Unix IPC primitive: unidirectional byte streams connecting a producer to a consumer through a kernel buffer.

## How It's Best Learned
Implement a producer-consumer pipeline using Unix pipes in C. Then reimplement using POSIX shared memory and compare the data path each takes through the kernel.

## Common Misconceptions
- Shared memory is not automatically synchronized; concurrent access requires locks or semaphores.
- Pipes are not bidirectional; full-duplex communication requires two pipes or a different mechanism.
