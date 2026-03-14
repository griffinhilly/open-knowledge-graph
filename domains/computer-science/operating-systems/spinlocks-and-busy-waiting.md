---
id: spinlocks-and-busy-waiting
title: Spinlocks and Busy-Waiting Synchronization
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
- id: context-switching-and-cpu-dispatch
  type: soft
builds-toward:
- atomic-operations-and-compare-swap
tags:
- synchronization
- locks
- multiprocessor
stage: formal-systems
status: draft
---

# Spinlocks and Busy-Waiting Synchronization

## Core Idea
Spinlocks are synchronization primitives where a process repeatedly checks a lock in a loop without yielding the CPU. They are efficient for very short critical sections on multiprocessor systems but waste CPU cycles on single-processor systems or under high lock contention. The choice between spinlocks and blocking locks depends on expected contention and critical section duration.
