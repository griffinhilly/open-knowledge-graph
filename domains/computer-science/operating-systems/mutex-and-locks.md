---
id: mutex-and-locks
title: Mutexes and Locking Primitives
domain: computer-science
course: operating-systems
prerequisites:
- id: synchronization-problem
  type: hard
builds-toward:
- semaphores
- deadlock-conditions
tags:
- mutex
- spinlock
- test-and-set
- compare-and-swap
- locking
stage: formal-systems
status: validated
---

# Mutexes and Locking Primitives

## Core Idea
A mutex (mutual exclusion lock) is the fundamental synchronization primitive that allows at most one thread to hold it at a time; any other thread attempting to acquire a held mutex blocks until it is released. Hardware support is essential: atomic instructions like test-and-set or compare-and-swap allow a thread to atomically read and conditionally modify a memory location, enabling correct mutex implementation without race conditions in the lock acquisition code itself. Spinlocks busy-wait (spin) in a loop testing the lock, suitable for short critical sections on multiprocessors; blocking mutexes deschedule the waiting thread, suitable for longer waits.

## How It's Best Learned
Implement a spinlock using a compare-and-swap loop. Measure the performance difference between a spinlock and a pthread_mutex on a long versus short critical section.

## Common Misconceptions
- A mutex held by one thread cannot be released by a different thread (unlike some semaphores).
- Spinlocks waste CPU cycles; they should never be used when the lock holder might be descheduled.

## Explainer

From the synchronization problem, you know that concurrent threads accessing shared data can produce incorrect results due to race conditions — one thread reads a value, another modifies it, and the first thread proceeds with stale data. A **mutex** (short for mutual exclusion) is the most fundamental solution: it is a lock that only one thread can hold at a time. Before entering a **critical section** (code that accesses shared data), a thread acquires the mutex. If another thread already holds it, the requesting thread waits. When the holding thread leaves the critical section, it releases the mutex, allowing a waiting thread to proceed. This serializes access to shared data, eliminating race conditions.

The tricky part is implementing the mutex itself. Consider a naive attempt: use a shared variable `locked` that threads check before entering. Thread A reads `locked == false`, decides to enter, and sets `locked = true`. But thread B might read `locked == false` at the exact same instant, before A writes `true` — now both threads think they hold the lock. The acquisition code itself has a race condition. This is where hardware atomic instructions become essential. **Test-and-set** atomically reads a memory location and sets it to 1 in a single indivisible operation, returning the old value. If the old value was 0, you got the lock; if it was 1, someone else has it. **Compare-and-swap** is more flexible: it atomically checks if a location holds an expected value and, only if so, replaces it with a new value. Both instructions are provided by the CPU hardware and cannot be interrupted, so no interleaving can corrupt the lock acquisition.

The simplest mutex built on these primitives is a **spinlock**: a thread executes test-and-set (or CAS) in a tight loop, spinning until the lock becomes available. Spinlocks are efficient when the expected wait is very short — a few microseconds — because spinning avoids the overhead of putting a thread to sleep and waking it up later. On a multiprocessor, while thread A holds a spinlock and executes its short critical section on one core, thread B spins on another core and grabs the lock almost instantly when A releases it. However, if the lock holder might run for a long time or might be descheduled by the OS, spinning wastes CPU cycles doing nothing useful. In that case, a **blocking mutex** (like `pthread_mutex`) is better: it puts the waiting thread to sleep and the OS wakes it when the lock is released, freeing the CPU for other work.

An important ownership rule distinguishes mutexes from other synchronization primitives you will encounter next (like semaphores): **a mutex must be released by the same thread that acquired it**. This ownership property enables useful features like priority inheritance (temporarily boosting a lock holder's priority to prevent priority inversion) and recursive locking (allowing the same thread to re-acquire a lock it already holds). It also makes reasoning about correctness simpler — you always know which thread is responsible for releasing a lock. Getting locking discipline right — acquiring locks in a consistent order, holding them for the minimum necessary time, and always releasing them (even on error paths) — is one of the most important practical skills in concurrent programming and directly sets up the deadlock analysis you will study next.
