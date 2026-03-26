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

## Questions

```yaml
- question: "A developer uses POSIX shared memory to share a large data structure between two processes but implements no locks or semaphores. This design will most likely result in:"
  type: multiple-choice
  options:
    - "Correct behavior — shared memory handles access coordination automatically through the OS"
    - "A compilation error — the POSIX API requires synchronization primitives to be declared at allocation time"
    - "Race conditions — both processes access the same memory concurrently without coordination, risking corrupted or inconsistent data"
    - "A kernel panic — the OS detects unsynchronized access to shared memory and terminates the processes"
  answer: 2
  explanation: "Shared memory gives multiple processes direct access to the same physical memory pages with no kernel mediation after setup. This is precisely analogous to two threads sharing a variable without a mutex. Without explicit synchronization (locks, semaphores, memory barriers), one process may read while another is mid-write, producing corrupted data. The OS provides no automatic protection — synchronization is entirely the programmer's responsibility. This is the most common misconception about shared memory IPC."

- question: "Why does a Unix pipe block the writer process when the pipe buffer is full?"
  type: multiple-choice
  options:
    - "To prevent the kernel from allocating memory beyond the system's physical capacity"
    - "To implement automatic flow control, preventing a fast producer from outrunning a slow consumer"
    - "Because the read end of the pipe has closed, signaling the consumer has finished"
    - "Because pipes hold only a single message at a time and must be emptied before the next write"
  answer: 1
  explanation: "Pipe blocking implements automatic back-pressure. The pipe has a fixed kernel buffer (typically 64 KB on Linux). When it fills, the writer blocks until the reader consumes enough data to free space; when it empties, the reader blocks until the writer produces more. This flow control is what makes the Unix shell pipeline model elegant — `grep | sort | uniq` doesn't require the programmer to manually coordinate timing between the three processes. The blocking is a feature, not a limitation."

- question: "Message passing through pipes is generally faster than shared memory for exchanging large amounts of data, because the kernel manages most data movement."
  type: true-false
  answer: false
  explanation: "The opposite is true. Message passing requires two data copies: from the sender's address space into the kernel buffer, then from the kernel buffer into the receiver's address space. For large or frequent transfers, this copying overhead is significant. Shared memory eliminates both copies after initial setup — processes access the same physical memory directly with no kernel involvement. The performance advantage of shared memory over message passing for large transfers is precisely the reason shared memory exists as a separate IPC mechanism, despite its more complex synchronization requirements."

- question: "Standard Unix pipes are bidirectional — a process can both write to and read from the same pipe for two-way communication with another process."
  type: true-false
  answer: false
  explanation: "Standard Unix pipes are unidirectional byte streams: one end is the write end, the other is the read end. A single pipe only moves data in one direction. Full-duplex communication between two processes requires either two pipes (one for each direction) or a different mechanism such as sockets, which support bidirectional data flow. This is why shell pipelines use a separate pipe for each connection between processes."

- question: "Explain the fundamental tradeoff between message passing and shared memory as IPC mechanisms, and describe when you would choose each."
  type: short-answer
  answer: "Message passing routes data through the kernel — data is copied from sender's address space into a kernel buffer, then into the receiver's. This is simple and safe (the kernel mediates all access, preventing simultaneous access issues), but the two-copy overhead adds latency and CPU cost for large or frequent transfers. Shared memory maps the same physical pages into multiple address spaces for zero-copy direct access — much faster, but requires explicit programmer-managed synchronization (locks, semaphores) to prevent race conditions. Choose message passing when simplicity and safety matter more than throughput, or when data volumes are modest; choose shared memory when transfer performance is critical and you can manage synchronization complexity."
  explanation: "This tradeoff mirrors the core tension in concurrent systems design between safety and performance. Kernel mediation provides safety guarantees at the cost of overhead; bypassing the kernel gives performance but transfers the safety responsibility to the programmer. The right choice depends on whether the performance benefit of eliminating kernel copying justifies the added synchronization complexity — and on whether the communicating processes are on the same machine (shared memory possible) or across machines (message passing via sockets required)."
```

## Explainer

From your study of processes and system calls, you know that each process runs in its own isolated address space — one process cannot simply read another's variables. This isolation is essential for stability and security, but it creates a problem: useful work often requires processes to cooperate. A web server might fork worker processes to handle requests; a shell pipeline like `grep pattern file | sort | uniq` requires three processes to stream data through each other. **Inter-process communication** (IPC) is the set of OS-provided mechanisms that bridge these isolated address spaces.

The two fundamental IPC models represent a classic tradeoff. **Message passing** routes data through the kernel: process A writes data into a kernel-managed channel, and process B reads from it. The data gets copied twice — from A's address space into a kernel buffer, then from the kernel buffer into B's address space. This is simple and safe (the kernel mediates all access), but the copying overhead can matter for large or frequent transfers. **Shared memory** takes the opposite approach: the OS maps the same physical memory pages into both processes' address spaces, so they can read and write the same bytes directly with no kernel involvement after setup. This eliminates copying overhead, but now both processes are accessing the same memory — just like threads sharing an address space — so they need explicit synchronization (locks, semaphores) to avoid race conditions.

**Pipes** are the most common message-passing mechanism in Unix. A pipe is a unidirectional byte stream backed by a small kernel buffer (typically 64 KB on Linux). One process writes to the pipe's write end, and another reads from the read end. When the buffer fills, the writer blocks until the reader consumes some data; when the buffer empties, the reader blocks until the writer produces more. This automatic flow control makes pipes elegant for producer-consumer patterns — the shell's `|` operator creates a pipe connecting stdout of one process to stdin of the next. Named pipes (FIFOs) extend this to unrelated processes by giving the pipe a name in the file system.

Beyond pipes, the OS provides richer mechanisms for different needs. **Message queues** allow sending discrete, typed messages rather than raw byte streams. **Sockets** enable IPC across machine boundaries using network protocols. **Signals** provide asynchronous notification (like SIGTERM to request graceful shutdown). Each mechanism makes a different tradeoff between simplicity, performance, and flexibility. The right choice depends on whether the communicating processes are related or independent, on the same machine or different machines, exchanging streaming data or discrete requests, and how much latency and throughput matter.
