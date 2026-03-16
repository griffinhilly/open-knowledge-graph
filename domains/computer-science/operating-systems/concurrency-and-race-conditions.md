---
id: concurrency-and-race-conditions
title: Concurrency and Race Conditions
domain: computer-science
course: operating-systems
prerequisites:
- id: thread-creation-and-lifecycle
  type: hard
builds-toward:
- mutual-exclusion-and-locks
- binary-semaphores-mutexes
tags:
- concurrency
- synchronization
- testing-challenges
stage: formal-systems
status: draft
---

# Concurrency and Race Conditions

## Core Idea
Concurrent execution of multiple threads enables responsiveness and parallelism but introduces subtle bugs. A race condition occurs when multiple threads access shared data concurrently and at least one modifies it, producing non-deterministic results. Race conditions are difficult to detect and reproduce because they depend on scheduling order and timing.

## Common Misconceptions
Race conditions are easily caught by testing (they are timing-dependent and often manifest only under specific workloads or hardware). Modern hardware prevents race conditions (atomic instructions prevent some but not all race conditions).

## Explainer

From your study of threads, you know that multiple threads within a process share the same address space — they can all read and write the same variables and data structures. This sharing is what makes threads efficient (no need to copy data between address spaces), but it is also the source of one of the most insidious classes of bugs in computing: the **race condition**.

A race condition occurs whenever the correctness of a program depends on the relative timing or interleaving of operations from multiple threads. Consider a simple example: two threads both execute `counter = counter + 1` on a shared variable that starts at zero. You might expect the final value to be 2, but this single line of code is actually three operations at the machine level — load the value from memory, add one, store the result back. If both threads load the value (0) before either stores, both compute 1, and both store 1. The final value is 1 instead of 2. One increment was silently lost. This is a **data race** — the specific case where two threads access the same memory location concurrently with at least one write and no synchronization.

What makes race conditions so dangerous is their **non-determinism**. The exact interleaving of thread operations depends on the OS scheduler, CPU load, cache behavior, and even the temperature of the processor affecting clock speeds. A program with a race condition might pass thousands of tests and run correctly for months, then fail catastrophically under slightly different load conditions in production. You cannot reliably test for race conditions by running the program many times — the bug hides in interleavings that your test environment might never produce. This is why formal reasoning about shared state, rather than empirical testing alone, is essential for concurrent programming.

The solution space falls into two categories. The first is **mutual exclusion**: using locks, semaphores, or monitors to ensure that only one thread executes a **critical section** (the code that accesses shared data) at a time. The second is **avoiding shared mutable state** entirely — using message passing, immutable data structures, or thread-local storage so threads never contend on the same memory. Both approaches have tradeoffs in complexity and performance, and you will explore them in depth as you study synchronization primitives. The key insight for now is that any time two threads can access the same data and at least one can modify it, you must either synchronize access or restructure the code to eliminate the sharing.
