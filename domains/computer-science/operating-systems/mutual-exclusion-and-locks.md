---
id: mutual-exclusion-and-locks
title: Mutual Exclusion and Locks
domain: computer-science
course: operating-systems
prerequisites:
- id: concurrency-and-race-conditions
  type: hard
builds-toward:
- binary-semaphores-mutexes
- counting-semaphores-resource-pools
- condition-variables-and-monitors
tags:
- synchronization
- locks
- critical-sections
stage: formal-systems
status: draft
---

# Mutual Exclusion and Locks

## Core Idea
Mutual exclusion ensures only one thread executes in a critical section (shared resource access) at a time. Simple locks (mutexes) achieve this via atomic operations. Spinlocks busy-wait; blocking locks suspend threads and use context switching. Fairness, deadlock freedom, and starvation resistance depend on lock implementation.

## How It's Best Learned
Implement a spinlock and a blocking lock; measure contention, overhead, and performance under various contention levels.
