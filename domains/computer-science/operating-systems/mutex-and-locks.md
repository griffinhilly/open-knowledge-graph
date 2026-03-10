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
status: draft
---

# Mutexes and Locking Primitives

## Core Idea
A mutex (mutual exclusion lock) is the fundamental synchronization primitive that allows at most one thread to hold it at a time; any other thread attempting to acquire a held mutex blocks until it is released. Hardware support is essential: atomic instructions like test-and-set or compare-and-swap allow a thread to atomically read and conditionally modify a memory location, enabling correct mutex implementation without race conditions in the lock acquisition code itself. Spinlocks busy-wait (spin) in a loop testing the lock, suitable for short critical sections on multiprocessors; blocking mutexes deschedule the waiting thread, suitable for longer waits.

## How It's Best Learned
Implement a spinlock using a compare-and-swap loop. Measure the performance difference between a spinlock and a pthread_mutex on a long versus short critical section.

## Common Misconceptions
- A mutex held by one thread cannot be released by a different thread (unlike some semaphores).
- Spinlocks waste CPU cycles; they should never be used when the lock holder might be descheduled.
