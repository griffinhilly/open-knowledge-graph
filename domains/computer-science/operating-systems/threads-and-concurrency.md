---
id: threads-and-concurrency
title: Threads and Concurrency
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
- id: process-states-lifecycle
  type: soft
builds-toward:
- synchronization-problem
- scheduling-algorithms
tags:
- threads
- concurrency
- user-threads
- kernel-threads
- multithreading
stage: formal-systems
status: validated
---

# Threads and Concurrency

## Core Idea
A thread is the unit of CPU utilization within a process — a lightweight execution stream that shares the process's address space, open files, and resources while having its own program counter, register set, and stack. Multiple threads within one process can run concurrently, enabling parallelism on multi-core systems without the overhead of separate address spaces. Threads can be implemented in user space (user-level threads, managed by a library) or kernel space (kernel threads, scheduled by the OS directly), with different tradeoffs in scheduling flexibility and blocking behavior.

## How It's Best Learned
Write a multithreaded program using pthreads or Java threads. Observe how threads share heap data, then introduce a race condition intentionally to see non-deterministic output.

## Common Misconceptions
- Threads are not automatically faster; synchronization overhead and contention can make a multithreaded program slower than a single-threaded one.
- User-level threads cannot take advantage of multiple cores unless the OS sees them.

## Explainer

From the process concept, you know that a process is a running program with its own address space, open file descriptors, and OS-managed state. Creating a new process is expensive: the OS must allocate a separate address space, copy or share page tables, and set up independent resource tracking. A **thread** is a lighter-weight alternative — it is an independent sequence of execution *within* a process that shares the process's address space, heap, global variables, and open files, but has its own program counter, register set, and stack. Think of a process as an apartment and threads as roommates: they share the kitchen and living room (heap, global data, files) but each has their own bedroom (stack, registers, program counter).

This sharing is both the power and the danger of threads. The power: threads within the same process can communicate by simply reading and writing shared variables — no pipes, sockets, or shared memory setup required. Creating a thread is fast because there is no address space to duplicate. Context switching between threads in the same process is cheaper than switching between processes because the memory mapping (page tables, TLB entries) stays the same. On a multi-core system, threads of the same process can run truly in parallel on different cores, enabling a single program to fully utilize modern hardware.

The danger: because threads share memory, two threads can read and write the same variable simultaneously, producing **race conditions** — bugs where the program's output depends on the unpredictable timing of thread execution. If thread A reads a counter, increments it, and writes it back, but thread B reads the same counter between A's read and write, the increment is lost. These bugs are notoriously difficult to reproduce and debug because they depend on scheduling timing that varies between runs. This is why threads and concurrency lead directly to synchronization — locks, semaphores, and other mechanisms for coordinating access to shared data.

Threads can be implemented at two levels. **Kernel threads** are managed directly by the operating system scheduler, which means the OS can schedule different threads of the same process on different cores and can block one thread without blocking the others. **User-level threads** are managed by a library in user space — the OS sees only one process and schedules it as a unit. User-level threads are faster to create and switch between (no system call needed), but if one user thread makes a blocking system call, the entire process blocks because the kernel does not know about the other threads. The mapping between user threads and kernel threads — many-to-one, one-to-one, or many-to-many — determines the tradeoff between performance and true parallelism. Most modern systems (Linux, Windows, macOS) use one-to-one mapping, where each user thread corresponds to a kernel thread, giving full multi-core parallelism at the cost of slightly heavier thread creation.
