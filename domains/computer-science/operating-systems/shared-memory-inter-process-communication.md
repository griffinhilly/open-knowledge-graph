---
id: shared-memory-inter-process-communication
title: Shared Memory Inter-Process Communication
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication-mechanisms
  type: hard
- id: virtual-memory-management
  type: soft
builds-toward:
- memory-mapped-files-io
tags:
- ipc
- shared-memory
- high-performance
stage: formal-systems
status: draft
---

# Shared Memory Inter-Process Communication

## Core Idea
Shared memory allows multiple processes to map the same memory region into their address spaces for high-speed data exchange without kernel overhead. Multiple processes can read and write simultaneously, requiring explicit synchronization to prevent data races and corruption. Shared memory is the fastest IPC mechanism but demands careful coordination and is vulnerable to one process corrupting another's data.

## Explainer

From your study of IPC mechanisms, you know that processes are isolated by default — each has its own address space, and the kernel mediates all communication. Pipes and message queues work by copying data from one process into the kernel and then out to another. This double-copy is safe but expensive for large or frequent transfers. **Shared memory** eliminates the copies entirely by letting two or more processes map the same physical memory region into their respective virtual address spaces. Once the region is set up, reads and writes go directly to RAM with no kernel involvement, making it the fastest IPC mechanism available.

Setting up shared memory involves a few steps. One process creates a named shared memory segment (using system calls like `shmget` on Unix or `CreateFileMapping` on Windows), specifying its size. Other processes attach to that segment by name, receiving a pointer they can use like any other memory address. The operating system's virtual memory system — which you may have encountered as a prerequisite — handles the mapping so that the same physical frames back the virtual pages in each process. Once attached, processes read and write through ordinary pointer operations. When done, each process detaches, and the segment is destroyed when the last user releases it.

The speed advantage comes with a critical responsibility: **synchronization is entirely your problem**. Unlike pipes or message queues, where the kernel serializes access, shared memory provides no built-in ordering or mutual exclusion. If one process writes a data structure while another reads it, the reader may see a half-written, inconsistent state — a classic **data race**. You must layer your own synchronization on top, typically using semaphores, mutexes in shared memory, or other coordination primitives. A common pattern is a **producer-consumer ring buffer** in shared memory, where one process writes to the next available slot and another reads from the oldest unread slot, with semaphores tracking how many slots are full and empty.

Shared memory is most valuable when processes exchange large volumes of data at high frequency — video frames, audio buffers, database page caches, or scientific simulation grids. For small, infrequent messages, the complexity of manual synchronization usually outweighs the performance gain, and simpler IPC like pipes or sockets is preferable. The tradeoff is direct: maximum speed in exchange for maximum programmer responsibility. A bug in one process can corrupt the shared region and crash or silently corrupt every other process attached to it, so defensive programming — checksums, version fields, careful lock discipline — is essential in production shared-memory systems.
