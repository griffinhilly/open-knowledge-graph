---
id: condition-variable-patterns
title: 'Condition Variables: Usage Patterns and Pitfalls'
domain: computer-science
course: operating-systems
prerequisites:
- id: condition-variables-and-monitors
  type: hard
- id: mutex-and-locks
  type: hard
builds-toward:
- monitor-pattern-definition
tags:
- condition-variables
- patterns
- synchronization
stage: formal-systems
status: draft
---

# Condition Variables: Usage Patterns and Pitfalls

## Core Idea
Condition variables allow threads to wait for a condition while releasing a mutex. Correct usage requires: holding the lock during wait/signal, re-checking conditions after waking (spurious wakeups occur), and understanding broadcast vs. signal semantics.

## How It's Best Learned
Implement bounded buffers and reader-writer locks using condition variables; test for spurious wakeup resilience.

## Common Misconceptions
- Calling notify without holding the lock.
- Forgetting to re-check condition after waking.
- Assuming signal always wakes exactly one waiter (barging can occur).

## Explainer

You already know what condition variables and mutexes are — a condition variable lets a thread sleep until some condition becomes true, and a mutex protects shared data from concurrent access. The challenge is using them together correctly. The patterns here are not complex in concept, but the pitfalls are subtle enough that even experienced programmers introduce bugs. Learning the canonical patterns now saves you from debugging race conditions that only manifest under heavy load.

The most important pattern is the **wait loop**. Never write `if (condition) wait(cv, lock)` — always write `while (!condition) wait(cv, lock)`. The reason is **spurious wakeups**: a thread can be woken from `wait()` even though no other thread called `signal()` or `broadcast()`. This happens because of implementation details in how the OS manages thread scheduling and because of a race called **barging** — between the moment a signaling thread releases the lock and the waiting thread reacquires it, a third thread can swoop in, acquire the lock, and change the condition back. The `while` loop handles all of these cases: if the thread wakes up and the condition is not actually true, it simply goes back to sleep.

The second critical pattern is the **bounded buffer** (producer-consumer queue), which uses two condition variables: one for "buffer not full" and one for "buffer not empty." A producer acquires the lock, checks if the buffer is full in a `while` loop (waiting on `not_full` if it is), inserts an item, then signals `not_empty`. A consumer does the mirror image. This pattern generalizes to any situation where threads must wait for different conditions on the same shared state. Using a single condition variable for both conditions technically works with `broadcast()`, but it is wasteful — every wakeup forces all waiting threads to recheck their condition, even when only one type of condition changed.

The choice between **signal** and **broadcast** matters for correctness and performance. `signal()` wakes one waiting thread; `broadcast()` wakes all of them. Use `signal()` when any single waiter can make progress (e.g., one item was added to a buffer, so one consumer can proceed). Use `broadcast()` when the state change might allow multiple waiters to proceed, or when different waiters are waiting for different conditions on the same condition variable. A common mistake is calling `signal()` when `broadcast()` is needed — this can cause threads to remain blocked indefinitely because the one thread that was woken cannot actually use the new state, while a thread that could use it stays asleep. When in doubt, `broadcast()` is always safe (it just wastes CPU cycles on unnecessary wakeups), while `signal()` requires you to reason carefully about which waiter will be woken.
