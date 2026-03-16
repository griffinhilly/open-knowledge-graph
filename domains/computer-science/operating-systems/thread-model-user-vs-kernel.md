---
id: thread-model-user-vs-kernel
title: 'Thread Models: User-Level and Kernel Threads'
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
builds-toward:
- thread-creation-and-lifecycle
- concurrency-and-race-conditions
tags:
- threading
- lightweight-concurrency
- kernel-vs-user
stage: formal-systems
status: draft
---

# Thread Models: User-Level and Kernel Threads

## Core Idea
Threads are lightweight execution units sharing an address space within a process. User-level threads are scheduled by user-space libraries, reducing kernel overhead but limiting parallelism to one thread per process. Kernel threads are scheduled by the OS, enabling true parallelism. Hybrid models (M:N) attempt to balance overhead and parallelism.

## Explainer

You already know that a process has its own address space, registers, and resources. A **thread** is a way to have multiple streams of execution within a single process, all sharing the same memory and open files but each with its own program counter, register set, and stack. If a process is like a house, threads are the people living in it — they share the kitchen and living room (memory, file handles) but each has their own to-do list (instruction pointer) and personal workspace (stack). The critical question is: who manages these threads?

**User-level threads** are managed entirely by a library in user space — the operating system doesn't even know they exist. The thread library handles creation, scheduling, and switching between threads, all without making system calls. This makes thread operations extremely fast: creating a user-level thread or switching between them might take microseconds rather than the tens of microseconds a kernel call would cost. The tradeoff is severe, though. Because the OS sees only one process, it schedules that process onto one CPU core. If you have four user-level threads, they take turns running on that one core — you get concurrency (interleaved execution) but not parallelism (simultaneous execution). Even worse, if one user-level thread makes a blocking system call (like a disk read), the entire process blocks, freezing all threads, because the kernel doesn't know there are other threads that could keep running.

**Kernel-level threads** solve these problems by making the OS aware of each thread. The kernel schedules threads individually, so different threads in the same process can run on different CPU cores simultaneously — true parallelism. If one thread blocks on I/O, the kernel simply schedules another thread from the same process. The cost is overhead: every thread creation, destruction, and context switch requires a system call and kernel data structures. On modern systems, this overhead is small enough that kernel threads are the dominant model. Linux, for example, implements threads as lightweight processes (via `clone()`) that share address space, making kernel thread operations fast enough for most applications.

The **hybrid M:N model** maps M user-level threads onto N kernel threads, trying to get the best of both worlds: fast user-space switching for threads that don't need parallelism, and kernel threads to provide actual parallel execution across cores. The user-space scheduler multiplexes many user threads onto fewer kernel threads. When a user thread blocks, the scheduler can swap in another user thread on the same kernel thread. In theory, this is ideal. In practice, M:N threading is complex to implement correctly — the user scheduler and kernel scheduler can make conflicting decisions, leading to priority inversion and subtle bugs. Most modern systems have abandoned M:N models in favor of 1:1 (one user thread per kernel thread), accepting the modest kernel overhead in exchange for simplicity and predictability. Go's goroutine scheduler is a notable modern exception that successfully implements an M:N-like approach.
