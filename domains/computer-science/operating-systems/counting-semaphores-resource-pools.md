---
id: counting-semaphores-resource-pools
title: Counting Semaphores and Resource Pools
domain: computer-science
course: operating-systems
prerequisites:
- id: binary-semaphores-mutexes
  type: hard
builds-toward:
- producer-consumer-classic-sync
tags:
- semaphores
- resource-management
- synchronization
stage: formal-systems
status: draft
---

# Counting Semaphores and Resource Pools

## Core Idea
Counting semaphores have integer values (≥0) representing available resources. wait() decrements (blocks if 0); signal() increments and wakes a waiting thread. Counting semaphores express resource constraints naturally and manage pools of identical resources such as buffer slots or thread pools.

## How It's Best Learned
Use counting semaphores to implement a bounded buffer, thread pool, or resource pool manager.

## Explainer

You already understand binary semaphores and mutexes — they protect critical sections by allowing exactly one thread in at a time. But many real problems involve managing a **pool of identical resources** rather than enforcing mutual exclusion. Consider a database connection pool with 10 connections: up to 10 threads can use connections simultaneously, but the 11th must wait. A mutex is too restrictive (only one thread at a time), and using 10 separate mutexes would be awkward. A **counting semaphore** solves this naturally by generalizing the binary concept: instead of toggling between 0 and 1, it maintains an integer count representing the number of available resources.

A counting semaphore supports two atomic operations. **wait()** (also called P, down, or acquire) decrements the counter. If the counter is already 0, the calling thread blocks until another thread increments it. **signal()** (also called V, up, or release) increments the counter and, if any threads are blocked on wait(), wakes one of them. Initialize the semaphore to the number of available resources — 10 for a connection pool, N for a bounded buffer with N slots — and the semaphore automatically enforces the capacity limit. Each wait() claims one resource; each signal() returns one. The semaphore never goes negative (blocked threads are queued, not counted), so the count always reflects the true number of available resources.

The classic application is the **bounded buffer** (producer-consumer) problem. You use two counting semaphores: `empty` initialized to the buffer size (number of empty slots) and `full` initialized to 0 (number of filled slots). A producer calls `wait(empty)` to claim an empty slot, writes data, then calls `signal(full)` to announce a filled slot. A consumer calls `wait(full)` to claim a filled slot, reads data, then calls `signal(empty)` to announce a newly empty slot. If the buffer is full, producers block on `wait(empty)`; if it is empty, consumers block on `wait(full)`. The two semaphores work in tandem, each counting what the other consumes. You still need a mutex to protect the actual buffer data structure from concurrent access, but the counting semaphores handle the capacity logic — a clean separation of concerns that makes the synchronization pattern both correct and readable.
