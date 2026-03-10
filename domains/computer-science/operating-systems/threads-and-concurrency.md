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
status: draft
---

# Threads and Concurrency

## Core Idea
A thread is the unit of CPU utilization within a process — a lightweight execution stream that shares the process's address space, open files, and resources while having its own program counter, register set, and stack. Multiple threads within one process can run concurrently, enabling parallelism on multi-core systems without the overhead of separate address spaces. Threads can be implemented in user space (user-level threads, managed by a library) or kernel space (kernel threads, scheduled by the OS directly), with different tradeoffs in scheduling flexibility and blocking behavior.

## How It's Best Learned
Write a multithreaded program using pthreads or Java threads. Observe how threads share heap data, then introduce a race condition intentionally to see non-deterministic output.

## Common Misconceptions
- Threads are not automatically faster; synchronization overhead and contention can make a multithreaded program slower than a single-threaded one.
- User-level threads cannot take advantage of multiple cores unless the OS sees them.
