---
id: condition-variables-and-monitors
title: Condition Variables and Monitors
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- producer-consumer-classic-sync
- readers-writers-problem-synchronization
tags:
- synchronization
- condition-variables
- monitors
stage: formal-systems
status: draft
---

# Condition Variables and Monitors

## Core Idea
Condition variables allow threads to wait until a specific condition is true. Used with locks, wait() releases the lock and blocks; notify()/notifyAll() wakes waiting threads. Monitors combine locks and condition variables to simplify synchronization. Condition variables are more expressive than semaphores for complex coordination patterns.

## Explainer

You already know that locks (mutexes) provide mutual exclusion — only one thread can hold the lock at a time, preventing data races on shared state. But locks alone cannot express waiting for a condition. Suppose a consumer thread wants to remove an item from a shared buffer, but the buffer is empty. With only a lock, the consumer would have to release the lock, busy-wait (repeatedly acquire the lock, check if the buffer is non-empty, release), wasting CPU cycles. **Condition variables** solve this by letting a thread say "wake me up when something changes" instead of spinning.

A condition variable is always used in conjunction with a lock. The pattern has three parts. First, the waiting thread acquires the lock and checks a condition (e.g., `buffer.size() > 0`). If the condition is false, it calls `wait()` on the condition variable, which atomically releases the lock and puts the thread to sleep — these two steps must be atomic to avoid a race where another thread signals between the release and the sleep. Second, when another thread changes the shared state (e.g., a producer adds an item to the buffer), it calls `notify()` (wake one waiter) or `notifyAll()` (wake all waiters) on the condition variable. Third, the woken thread re-acquires the lock and re-checks the condition in a **while loop**, not an if statement. The loop is essential because under Mesa-style semantics (used by pthreads, Java, and most real systems), another thread might have consumed the item between the signal and the re-acquisition of the lock.

A **monitor** packages this pattern into a clean abstraction. It is an object (or module) that encapsulates shared data along with the procedures that access it, and the language or runtime automatically enforces that only one thread can be executing inside the monitor at any time. You do not manually acquire and release locks — the monitor handles it. Condition variables live inside the monitor, providing the wait/signal mechanism for coordination. Java's `synchronized` keyword with `wait()`/`notifyAll()` is the most widely encountered monitor implementation. The bounded buffer becomes straightforward: `put()` waits on a "not full" condition and signals "not empty"; `get()` waits on "not empty" and signals "not full." All locking is implicit.

The key advantage over raw semaphores is clarity and safety. With semaphores, forgetting a `signal()` or placing it in the wrong order causes subtle deadlocks or race conditions that are hard to debug. Monitors make the critical section boundaries explicit through language constructs, and condition variables give you named, semantic wait points — you wait on "buffer not empty," not on an anonymous counter. This makes concurrent code easier to write correctly and easier to reason about during code review.
