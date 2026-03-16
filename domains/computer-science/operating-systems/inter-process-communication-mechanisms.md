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

## Explainer

From your study of inter-process communication, you know that processes have isolated address spaces — one process cannot simply read another's memory. This isolation is essential for stability and security, but it creates a problem: processes often need to cooperate, sharing data or coordinating actions. **IPC mechanisms** are the OS-provided channels that allow communication across this isolation boundary, and understanding their tradeoffs is key to designing systems where multiple processes work together.

**Pipes** are the simplest IPC mechanism. A pipe is a unidirectional byte stream: one process writes bytes in, another reads them out, in order. The classic Unix pipeline `ls | grep ".txt"` creates a pipe connecting the stdout of `ls` to the stdin of `grep`. Pipes are anonymous — they exist only as long as the processes using them — and work only between related processes (typically parent and child). **Named pipes** (FIFOs) extend this by creating a pipe with a filesystem name, allowing unrelated processes to communicate. Pipes are easy to use but limited: they are unidirectional, byte-oriented (no message boundaries), and work only on the same machine.

**Shared memory** takes the opposite approach. Instead of copying data through a kernel-managed channel, two processes map the same physical memory region into their respective address spaces. One process writes directly to this region; the other reads from it — no kernel involvement per operation, no data copying. This makes shared memory the fastest IPC mechanism by far. The catch is that the processes must coordinate their access to avoid race conditions, using semaphores or mutexes to ensure one process doesn't read while another is mid-write. Shared memory trades simplicity for performance: it is powerful but requires careful synchronization.

**Message queues** provide structured communication. Unlike pipes (which carry raw bytes), message queues carry discrete messages with types and boundaries. A producer process enqueues a message; a consumer dequeues it. Messages can be prioritized, filtered by type, and persist until consumed even if the sender exits. This makes message queues well-suited for producer-consumer patterns where the sender and receiver operate at different speeds.

**Sockets** are the most versatile mechanism. While the other IPC methods work only between processes on the same machine, sockets can communicate across a network. Even for local communication, Unix domain sockets provide bidirectional, connection-oriented channels between processes. Network sockets (TCP/UDP) extend this to remote processes, making sockets the foundation of all network programming. The tradeoff is overhead — socket communication involves more kernel processing than pipes or shared memory — but the flexibility of working across machine boundaries makes sockets indispensable for distributed systems.
