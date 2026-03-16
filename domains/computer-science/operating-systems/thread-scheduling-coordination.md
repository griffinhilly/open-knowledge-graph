---
id: thread-scheduling-coordination
title: Thread Scheduling and Coordination
domain: computer-science
course: operating-systems
prerequisites:
- id: threads-and-concurrency
  type: hard
- id: process-model-formalization
  type: hard
builds-toward:
- critical-section-problem-formalization
- semaphore-formal-definition
tags:
- threads
- scheduling
- coordination
stage: formal-systems
status: draft
---

# Thread Scheduling and Coordination

## Core Idea
Threads share a process's address space but maintain independent execution stacks and program counters. Independent scheduling of threads requires explicit synchronization mechanisms to coordinate shared data access and prevent race conditions.

## How It's Best Learned
Implement simple concurrent programs with race conditions, observe the failures, then add locks to fix them.

## Common Misconceptions
- Assuming shared memory automatically means data is consistent.
- Thinking compiler optimizations are thread-safe.
- Missing that memory visibility requires explicit synchronization.

## Explainer

You know from studying threads that multiple threads within a process share the same address space — the same heap, the same global variables, the same code. And from the process model, you know that each execution context has its own program counter and stack. When the OS scheduler decides to run a different thread, it performs a **context switch** that saves one thread's registers and restores another's. The critical insight is that these switches can happen at any point — between any two machine instructions — and this unpredictability is what makes concurrent programming fundamentally different from sequential programming.

Consider a simple example: two threads both increment a shared counter. The operation `counter += 1` looks atomic in source code, but at the machine level it decomposes into three steps: load the value from memory into a register, add one, and store the result back. If thread A loads the value (say, 5), then gets preempted before storing, thread B loads the same value 5, increments to 6, and stores it. When thread A resumes, it stores its result — also 6. Two increments happened, but the counter only went up by one. This is a **race condition**: the result depends on the unpredictable timing of thread scheduling.

Race conditions are not bugs in the scheduler — they are bugs in the program. The scheduler is doing exactly what it should: sharing the CPU among threads. The problem is that the program accesses shared data without **synchronization**. The simplest synchronization primitive is a **lock** (or mutex): a thread acquires the lock before accessing shared data and releases it afterward. While the lock is held, any other thread that tries to acquire it will block until the first thread releases it. This guarantees that the load-increment-store sequence completes without interruption, making the operation effectively atomic from the perspective of other threads.

But synchronization introduces its own challenges. Locks create **contention** — threads waiting for locks are doing no useful work, reducing parallelism. Using too few locks risks race conditions; using too many risks **deadlock**, where two threads each hold a lock the other needs. Beyond locks, threads need ways to coordinate their execution order — for example, a producer thread must signal a consumer thread that data is ready. These coordination patterns lead to higher-level primitives like **condition variables** and **semaphores**, which you will study next. The fundamental lesson here is that shared memory is not free communication — it is a shared resource that requires disciplined access protocols, just like any other shared resource in an operating system.
