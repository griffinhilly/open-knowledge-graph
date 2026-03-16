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

## Explainer

From your study of processes and system calls, you know that each process runs in its own isolated address space — one process cannot simply read another's variables. This isolation is essential for stability and security, but it creates a problem: useful work often requires processes to cooperate. A web server might fork worker processes to handle requests; a shell pipeline like `grep pattern file | sort | uniq` requires three processes to stream data through each other. **Inter-process communication** (IPC) is the set of OS-provided mechanisms that bridge these isolated address spaces.

The two fundamental IPC models represent a classic tradeoff. **Message passing** routes data through the kernel: process A writes data into a kernel-managed channel, and process B reads from it. The data gets copied twice — from A's address space into a kernel buffer, then from the kernel buffer into B's address space. This is simple and safe (the kernel mediates all access), but the copying overhead can matter for large or frequent transfers. **Shared memory** takes the opposite approach: the OS maps the same physical memory pages into both processes' address spaces, so they can read and write the same bytes directly with no kernel involvement after setup. This eliminates copying overhead, but now both processes are accessing the same memory — just like threads sharing an address space — so they need explicit synchronization (locks, semaphores) to avoid race conditions.

**Pipes** are the most common message-passing mechanism in Unix. A pipe is a unidirectional byte stream backed by a small kernel buffer (typically 64 KB on Linux). One process writes to the pipe's write end, and another reads from the read end. When the buffer fills, the writer blocks until the reader consumes some data; when the buffer empties, the reader blocks until the writer produces more. This automatic flow control makes pipes elegant for producer-consumer patterns — the shell's `|` operator creates a pipe connecting stdout of one process to stdin of the next. Named pipes (FIFOs) extend this to unrelated processes by giving the pipe a name in the file system.

Beyond pipes, the OS provides richer mechanisms for different needs. **Message queues** allow sending discrete, typed messages rather than raw byte streams. **Sockets** enable IPC across machine boundaries using network protocols. **Signals** provide asynchronous notification (like SIGTERM to request graceful shutdown). Each mechanism makes a different tradeoff between simplicity, performance, and flexibility. The right choice depends on whether the communicating processes are related or independent, on the same machine or different machines, exchanging streaming data or discrete requests, and how much latency and throughput matter.
