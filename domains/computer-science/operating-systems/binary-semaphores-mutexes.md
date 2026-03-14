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
