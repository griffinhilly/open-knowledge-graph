---
id: condition-variable-patterns
title: 'Condition Variables: Usage Patterns and Pitfalls'
domain: computer-science
course: operating-systems
prerequisites:
- id: monitors-and-condition-variables
  type: hard
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- monitors-and-condition-variables
tags:
- condition-variables
- patterns
- synchronization
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A thread wakes from a condition variable wait() call and finds the condition it was waiting for is still false. In a correctly written program, what should happen next?"
  type: multiple-choice
  options:
    - "The thread should proceed anyway — if it was signaled, the condition must be true"
    - "The thread should release the lock and terminate, since the wakeup was erroneous"
    - "The thread should re-check the condition in its while loop and call wait() again"
    - "This cannot happen if the signaling thread holds the lock when it calls signal()"
  answer: 2
  explanation: "Spurious wakeups and barging can cause a thread to wake even when the condition is false. The OS may wake a thread for implementation reasons unrelated to any signal(), or a third 'barging' thread can acquire the lock between the signal and the waiter reacquiring it, changing the condition back to false. The while-loop pattern handles all of these: the thread re-checks and calls wait() again if still false. Using `if` instead of `while` is a classic concurrency bug because it assumes wakeup implies the condition holds."

- question: "A bounded buffer uses a single condition variable shared by both producers (waiting when full) and consumers (waiting when empty). A producer adds an item and calls signal(). What could go wrong?"
  type: multiple-choice
  options:
    - "Nothing — signal() correctly wakes one waiting thread, which will then check its condition"
    - "Another producer could be woken instead of a consumer, find the buffer still full, and go back to sleep without notifying any consumer"
    - "The signaled thread will always be a consumer because signal() uses FIFO ordering"
    - "signal() is invalid unless called with the lock held, causing undefined behavior"
  answer: 1
  explanation: "When producers and consumers share one condition variable, signal() wakes one thread — but it might wake another producer. That producer checks whether the buffer is not-full (it still is, since an item was just added), goes back to sleep, and no consumer is ever woken. The item sits in the buffer forever. The fix is either separate condition variables (one per condition) or broadcast() so all waiters recheck. This illustrates why signal() requires careful reasoning about which waiter gets woken."

- question: "Using `if (!condition) wait(cv, lock)` instead of `while (!condition) wait(cv, lock)` is safe as long as the signaling thread always holds the lock when it calls signal()."
  type: true-false
  answer: false
  explanation: "Holding the lock during signal() is necessary but not sufficient to make `if` safe. The problem is barging: after the signaling thread calls signal() and releases the lock, a third thread can acquire the lock before the waiting thread does, and change the condition back to false. The waiting thread then wakes with the condition false — a bug. Additionally, POSIX explicitly permits spurious wakeups (wakeups with no corresponding signal()) for implementation reasons, making `while` necessary regardless of lock discipline."

- question: "Using broadcast() in place of signal() is always correct, even if it causes unnecessary wakeups."
  type: true-false
  answer: true
  explanation: "broadcast() wakes all waiting threads; each then re-checks its condition in the while loop and goes back to sleep if the condition is not satisfied. This is always correct — it may waste CPU cycles on unnecessary wakeups, but it never leaves a thread blocked when it could make progress. signal() is an optimization that requires careful reasoning about which waiter will be woken; broadcast() is the safe default when in doubt."

- question: "Explain what 'barging' is in the context of condition variables, and why it requires waits to be in a while loop rather than an if statement."
  type: short-answer
  answer: "Barging occurs when a third thread acquires the mutex in the window between a signal being sent and the waiting thread reacquiring the lock. The waiting thread was legitimately woken, but before it could proceed, the barging thread grabbed the lock first — potentially consuming the resource or changing the condition back to false. When the original waiting thread finally gets the lock, the condition may no longer hold. A while loop handles this: the woken thread re-checks the condition and waits again if it's false, regardless of whether barging, spurious wakeups, or a legitimate signal caused the wakeup."
  explanation: "Barging is not a bug in the signaling code — it's an inherent property of lock acquisition in most threading implementations. Correctness requires the waiting thread to always re-check rather than trust that a wakeup implies the condition is true."
```

## Explainer

You already know what condition variables and mutexes are — a condition variable lets a thread sleep until some condition becomes true, and a mutex protects shared data from concurrent access. The challenge is using them together correctly. The patterns here are not complex in concept, but the pitfalls are subtle enough that even experienced programmers introduce bugs. Learning the canonical patterns now saves you from debugging race conditions that only manifest under heavy load.

The most important pattern is the **wait loop**. Never write `if (condition) wait(cv, lock)` — always write `while (!condition) wait(cv, lock)`. The reason is **spurious wakeups**: a thread can be woken from `wait()` even though no other thread called `signal()` or `broadcast()`. This happens because of implementation details in how the OS manages thread scheduling and because of a race called **barging** — between the moment a signaling thread releases the lock and the waiting thread reacquires it, a third thread can swoop in, acquire the lock, and change the condition back. The `while` loop handles all of these cases: if the thread wakes up and the condition is not actually true, it simply goes back to sleep.

The second critical pattern is the **bounded buffer** (producer-consumer queue), which uses two condition variables: one for "buffer not full" and one for "buffer not empty." A producer acquires the lock, checks if the buffer is full in a `while` loop (waiting on `not_full` if it is), inserts an item, then signals `not_empty`. A consumer does the mirror image. This pattern generalizes to any situation where threads must wait for different conditions on the same shared state. Using a single condition variable for both conditions technically works with `broadcast()`, but it is wasteful — every wakeup forces all waiting threads to recheck their condition, even when only one type of condition changed.

The choice between **signal** and **broadcast** matters for correctness and performance. `signal()` wakes one waiting thread; `broadcast()` wakes all of them. Use `signal()` when any single waiter can make progress (e.g., one item was added to a buffer, so one consumer can proceed). Use `broadcast()` when the state change might allow multiple waiters to proceed, or when different waiters are waiting for different conditions on the same condition variable. A common mistake is calling `signal()` when `broadcast()` is needed — this can cause threads to remain blocked indefinitely because the one thread that was woken cannot actually use the new state, while a thread that could use it stays asleep. When in doubt, `broadcast()` is always safe (it just wastes CPU cycles on unnecessary wakeups), while `signal()` requires you to reason carefully about which waiter will be woken.
