---
id: binary-semaphores-mutexes
title: Binary Semaphores and Mutexes
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- counting-semaphores-resource-pools
- condition-variables-and-monitors
- producer-consumer-classic-sync
tags:
- semaphores
- synchronization
- classic-primitives
stage: formal-systems
status: draft
---

# Binary Semaphores and Mutexes

## Core Idea
A binary semaphore is a synchronization primitive with a counter of 0 or 1, acting as a lock. wait() (P) decrements; if already 0, the thread blocks. signal() (V) increments and wakes a waiting thread. Binary semaphores are conceptually simple but can be error-prone; locked semaphores ensure unlock occurs in the same thread.

## Common Misconceptions
Semaphore value never goes negative (it does if threads block; negative values represent blocked threads). Semaphores are easier than locks (implementation and usage can be subtle and error-prone).

## Explainer

You already understand mutual exclusion and the basic idea of a lock: only one thread can hold it at a time, and any other thread that tries to acquire it must wait. A **binary semaphore** formalizes this idea using a counter that is always 0 or 1. When the counter is 1, the resource is available; when it is 0, the resource is held. The two fundamental operations — traditionally called **P** (from the Dutch *proberen*, "to try") and **V** (*verhogen*, "to increment") — are also known as **wait()** and **signal()**. Wait decrements the counter: if the result is 0, the thread proceeds; if the counter was already 0, the thread blocks and joins a queue. Signal increments the counter and wakes one blocked thread if any are waiting. Both operations are **atomic** — they cannot be interrupted halfway through — which is what makes the whole mechanism safe.

A **mutex** (short for "mutual exclusion") looks almost identical to a binary semaphore, but it carries an additional constraint: **ownership**. Only the thread that locked the mutex can unlock it. With a plain binary semaphore, any thread can call signal(), which means thread A could accidentally (or intentionally) release a lock held by thread B. A mutex prevents this by tracking which thread holds it and rejecting unlock attempts from other threads. This ownership property also enables **priority inheritance** — if a high-priority thread is waiting for a mutex held by a low-priority thread, the OS can temporarily boost the low-priority thread's priority to avoid **priority inversion**, a situation where a medium-priority thread preempts the lock holder and indirectly blocks the high-priority thread.

The classic usage pattern is straightforward: surround a critical section with wait() before and signal() after. But the simplicity is deceptive. If a thread acquires semaphore A then tries to acquire semaphore B, while another thread acquires B then tries A, you have a deadlock. If a thread takes an early return or throws an exception between wait() and signal(), the semaphore is never released and every subsequent thread blocks forever. These failure modes are why higher-level abstractions like monitors and condition variables were invented — they bundle the lock with the condition-checking logic and ensure cleanup even when things go wrong. Understanding binary semaphores is essential because those higher-level tools are built on top of them, and when debugging concurrency bugs, you often need to reason at this level.

Consider a concrete analogy: a single-occupancy bathroom with a lock. The binary semaphore is the lock mechanism itself — flip it to "occupied" when you enter, flip it to "vacant" when you leave. A mutex adds a rule: only the person inside can unlock the door. Without that rule, someone outside could flip the lock while you are still using the bathroom — technically "correct" in the semaphore model, but clearly wrong in practice. Most OS synchronization scenarios require the mutex's ownership guarantee, which is why mutexes are the default choice for protecting critical sections in modern systems programming.
