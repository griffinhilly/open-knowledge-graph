---
id: semaphores
title: Semaphores
domain: computer-science
course: operating-systems
prerequisites:
- id: mutex-and-locks
  type: hard
builds-toward:
- monitors-and-condition-variables
- deadlock-conditions
tags:
- semaphore
- binary-semaphore
- counting-semaphore
- P-V-operations
- Dijkstra
stage: formal-systems
status: validated
---

# Semaphores

## Core Idea
A semaphore, introduced by Dijkstra, is an integer synchronization variable with two atomic operations: wait (P) decrements the value and blocks if it becomes negative, and signal (V) increments the value and wakes a blocked thread if any. A binary semaphore (values 0 and 1) implements mutual exclusion and behaves like a mutex. A counting semaphore (any non-negative integer) tracks the count of available resources, enabling the classic producer-consumer and bounded-buffer patterns. Unlike mutexes, a semaphore can be signaled by a thread different from the one that waited, making them suitable for signaling between threads.

## How It's Best Learned
Implement the bounded-buffer (producer-consumer) problem using two counting semaphores (empty slots, full slots) plus a mutex. Trace through an execution by hand, showing how the semaphore values change.

## Common Misconceptions
- Semaphores are not queues; the standard definition doesn't specify which blocked thread is woken.
- Using semaphores correctly requires disciplined P before critical section and V after, or bugs are subtle.

## Explainer

You already understand that mutexes provide mutual exclusion — only one thread enters the critical section at a time. A **semaphore** generalizes this idea by replacing the binary locked/unlocked state with an integer counter, enabling a much wider range of synchronization patterns. Dijkstra introduced semaphores in 1965, naming the two operations **P** (from the Dutch *proberen*, to test) and **V** (*verhogen*, to increment). In modern terminology these are called **wait** and **signal**, but the semantics are identical: wait decrements the counter and blocks if it goes negative; signal increments the counter and wakes a blocked thread if any are waiting.

A **binary semaphore** has values restricted to 0 and 1 and behaves like a mutex — wait locks it, signal unlocks it. The key difference is ownership: a mutex must be released by the same thread that acquired it, but a semaphore can be signaled by any thread. This makes semaphores ideal for **signaling** between threads. For example, a parent thread can wait on a semaphore initialized to 0; when the child thread finishes its setup, it signals the semaphore, and the parent unblocks. No mutex can express this pattern cleanly because no single thread "owns" both sides of the interaction.

A **counting semaphore** starts at some value N representing the number of available resources. Each wait decrements the count, and each signal increments it. When the count reaches zero, the next thread to wait blocks until another thread signals. This is the foundation of the bounded-buffer (producer-consumer) pattern: one counting semaphore tracks empty slots, another tracks full slots, and together they coordinate producers and consumers without busy-waiting.

The discipline required with semaphores is strict: every wait must have a matching signal, and the order matters. If you wait on two semaphores in different orders in different threads, you risk deadlock. If you forget a signal, a thread blocks forever. If you add an extra signal, a thread enters a critical section when it should not. Unlike higher-level constructs like monitors, semaphores give you no compile-time safety net — correctness depends entirely on the programmer placing P and V in the right places. This is both their power and their danger, which is why understanding them thoroughly is essential before moving on to monitors and condition variables.
