---
id: monitors-and-condition-variables
title: Monitors and Condition Variables
domain: computer-science
course: operating-systems
prerequisites:
- id: semaphores
  type: hard
tags:
- monitor
- condition-variable
- wait
- signal
- broadcast
- Hoare
- Mesa
stage: formal-systems
status: draft
---

# Monitors and Condition Variables

## Core Idea
A monitor is a high-level synchronization abstraction that encapsulates shared data and the procedures that operate on it, automatically enforcing mutual exclusion — only one thread executes inside the monitor at a time. Condition variables are synchronization objects used inside monitors: a thread calls wait() to release the lock and sleep until some condition holds, and another thread calls signal() (or broadcast()) to wake waiting threads. The Mesa-style semantics (used by Java, pthreads) require waiting threads to re-check their condition in a loop after waking because the condition may no longer hold. Monitors eliminate many subtle synchronization errors inherent in raw semaphore use.

## How It's Best Learned
Re-implement the bounded-buffer using Java synchronized methods and wait()/notifyAll(). Compare the code structure and potential for bugs against the semaphore solution.

## Common Misconceptions
- signal() does not immediately transfer control to the woken thread (Mesa semantics); the woken thread must compete for the lock.
- Always use while() not if() when waiting on a condition variable to guard against spurious wakeups.
