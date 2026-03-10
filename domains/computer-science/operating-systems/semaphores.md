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
status: draft
---

# Semaphores

## Core Idea
A semaphore, introduced by Dijkstra, is an integer synchronization variable with two atomic operations: wait (P) decrements the value and blocks if it becomes negative, and signal (V) increments the value and wakes a blocked thread if any. A binary semaphore (values 0 and 1) implements mutual exclusion and behaves like a mutex. A counting semaphore (any non-negative integer) tracks the count of available resources, enabling the classic producer-consumer and bounded-buffer patterns. Unlike mutexes, a semaphore can be signaled by a thread different from the one that waited, making them suitable for signaling between threads.

## How It's Best Learned
Implement the bounded-buffer (producer-consumer) problem using two counting semaphores (empty slots, full slots) plus a mutex. Trace through an execution by hand, showing how the semaphore values change.

## Common Misconceptions
- Semaphores are not queues; the standard definition doesn't specify which blocked thread is woken.
- Using semaphores correctly requires disciplined P before critical section and V after, or bugs are subtle.
