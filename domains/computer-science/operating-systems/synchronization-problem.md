---
id: synchronization-problem
title: The Critical Section Problem and Race Conditions
domain: computer-science
course: operating-systems
prerequisites:
- id: threads-and-concurrency
  type: hard
- id: inter-process-communication
  type: soft
builds-toward:
- mutex-and-locks
- semaphores
tags:
- race-condition
- critical-section
- mutual-exclusion
- atomicity
stage: formal-systems
status: validated
---

# The Critical Section Problem and Race Conditions

## Core Idea
A race condition occurs when two or more concurrent threads access shared data and the final result depends on the unpredictable interleaving of their operations. The critical section is the code segment where shared data is accessed; correct concurrent programs must ensure that only one thread executes its critical section at a time (mutual exclusion), that waiting threads eventually enter their critical section (progress and bounded waiting), and that no assumptions are made about CPU speed or scheduling. These three requirements — mutual exclusion, progress, bounded waiting — define the Critical Section Problem.

## How It's Best Learned
Reproduce a race condition: have two threads increment a shared counter 1,000,000 times without synchronization and observe the incorrect final value. Then explain why the assembly-level read-modify-write sequence is not atomic.

## Common Misconceptions
- Race conditions are not always obvious; they may appear intermittently depending on timing.
- Declaring a variable 'volatile' in C/C++ does not fix race conditions; it only prevents compiler optimization of reads.
