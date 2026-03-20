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
builds-toward: []
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

## Explainer

From your study of mutual exclusion and locks, you know that when a thread finds a lock already held, it must wait. The question is *how* it waits. A **blocking lock** (like a mutex) puts the waiting thread to sleep and asks the OS scheduler to run something else — the thread gives up the CPU until the lock holder signals that the lock is free. A **spinlock** takes the opposite approach: the waiting thread stays on the CPU and continuously checks the lock in a tight loop, "spinning" until it becomes available. Think of it as the difference between taking a number at a deli counter and sitting down (blocking) versus standing at the counter watching the clerk and asking "is it my turn yet?" over and over (spinning).

Spinning sounds wasteful, and on a **single-processor** system it genuinely is. If only one CPU exists, the thread holding the lock cannot make progress while the spinner occupies the processor — spinning just burns cycles until the OS preempts the spinner and schedules the lock holder. But on a **multiprocessor** system, the lock holder is running on a different CPU and actively making progress. If the critical section is very short — say, updating a single counter or pointer — the lock will be released in a few dozen nanoseconds. In that scenario, the cost of spinning is far less than the cost of a context switch, which you know involves saving registers, switching page tables, and potentially flushing caches. The breakeven point is roughly: if the expected wait time is less than the cost of two context switches (one to sleep, one to wake up), spinning wins.

This is why spinlocks are the synchronization primitive of choice inside operating system kernels for protecting short critical sections, especially on multiprocessor machines. Interrupt handlers, scheduler code, and memory allocators all use spinlocks because they cannot afford to sleep — sleeping inside the scheduler would be circular. A common pattern is **spin-then-block**: try spinning for a brief period, and if the lock is still held, fall back to blocking. This hybrid approach, sometimes called an **adaptive lock**, captures the best of both worlds: fast acquisition when contention is low, and CPU-efficient waiting when contention is high.

The implementation of a spinlock relies on the atomic hardware instructions you studied, such as test-and-set or compare-and-swap. A minimal spinlock is just a loop: `while (test_and_set(&lock) == 1) { /* spin */ }`. When the lock variable is 0, test-and-set atomically sets it to 1 and returns 0, and the thread enters the critical section. When the lock is already 1, test-and-set returns 1, and the thread keeps looping. The danger is **priority inversion**: if a low-priority thread holds a spinlock and a high-priority thread spins on it, the high-priority thread wastes its entire time slice spinning while the low-priority thread cannot run to release the lock. Real spinlock implementations address this with techniques like disabling preemption while holding the lock, ensuring the holder runs to completion quickly.
