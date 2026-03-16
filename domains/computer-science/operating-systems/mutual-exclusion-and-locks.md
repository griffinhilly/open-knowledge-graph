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

## Explainer

From concurrency and race conditions, you know that when multiple threads access shared data simultaneously and at least one is writing, the result depends on the unpredictable interleaving of their operations. A **critical section** is a region of code that accesses such shared data and must not be executed by more than one thread at a time. **Mutual exclusion** is the property that guarantees this: at most one thread is in the critical section at any moment.

A **lock** (or **mutex**) is the simplest mechanism to enforce mutual exclusion. The interface is minimal: `acquire()` before entering the critical section and `release()` after leaving. If thread A has acquired the lock, thread B's call to `acquire()` will not return until A calls `release()`. The critical implementation detail is how `acquire()` is made **atomic** — the check "is the lock free?" and the action "mark it as taken" must happen as a single indivisible step. If they were separate, two threads could both see the lock as free and both claim it, defeating the entire purpose. Hardware provides atomic instructions like **test-and-set**, **compare-and-swap** (CAS), or **fetch-and-add** that make this possible.

The two fundamental lock designs differ in what a thread does while waiting. A **spinlock** loops continuously, checking the lock in a tight loop (`while (test_and_set(&lock));`). This wastes CPU cycles but avoids the overhead of a context switch, making spinlocks efficient when the critical section is very short and the wait is brief. A **blocking lock** (or sleeping lock) puts the waiting thread to sleep — removing it from the CPU's run queue — and wakes it when the lock becomes available. This is better when critical sections are long, because the CPU can do useful work running other threads instead of spinning. The tradeoff is the cost of two context switches (sleep and wake) versus the cost of wasted CPU cycles from spinning.

Beyond the basic design, lock implementations must consider **fairness** and **livelock**. A naive spinlock can starve some threads if the hardware consistently favors one core's memory access over another. **Ticket locks** solve this by assigning each waiting thread a number and serving them in order, like a bakery queue. A correct lock must also guarantee **deadlock freedom** — if the lock is released, some waiting thread must eventually acquire it — and ideally **starvation freedom** — every thread that requests the lock eventually gets it. These properties are not automatic; they depend on the lock algorithm and the underlying hardware's memory ordering guarantees.
