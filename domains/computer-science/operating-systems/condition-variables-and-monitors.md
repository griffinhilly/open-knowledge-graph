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
status: validated
---

# Condition Variables and Monitors

## Core Idea
Condition variables allow threads to wait until a specific condition is true. Used with locks, wait() releases the lock and blocks; notify()/notifyAll() wakes waiting threads. Monitors combine locks and condition variables to simplify synchronization. Condition variables are more expressive than semaphores for complex coordination patterns.

## Questions

```yaml
- question: "A consumer thread checks that a buffer is empty, then tries to sleep. Why must wait() atomically release the lock and block the thread — rather than releasing first, then blocking?"
  type: multiple-choice
  options:
    - "Releasing before blocking would allow the consumer to starve the producer by holding the lock too long"
    - "A producer could add an item and call notify() between the release and the block, causing the consumer to sleep indefinitely despite data being available"
    - "Non-atomic release would cause the consumer to wake up immediately and re-check the condition unnecessarily"
    - "The lock must be held during blocking to prevent other threads from entering the critical section"
  answer: 1
  explanation: "This is the classic missed-signal race: if the consumer releases the lock and hasn't yet gone to sleep, a producer thread can acquire the lock, add an item, call notify(), and then the consumer finally sleeps — having missed the only notification. It would wait forever for a signal that already fired. Making wait() atomic — releasing the lock and blocking in one indivisible step — eliminates the window where this race can occur."

- question: "A thread is woken by notify() and re-acquires the lock. It should check its condition using:"
  type: multiple-choice
  options:
    - "An if statement — the signal guarantees the condition is true"
    - "A while loop — another thread may have consumed the resource between the signal and re-acquisition"
    - "No check — the monitor guarantees the condition holds when the thread resumes"
    - "A try-catch block — to handle the case where the condition is spuriously false"
  answer: 1
  explanation: "Under Mesa semantics (used by pthreads, Java, and most real systems), notify() is a hint, not a guarantee. Another thread may have run between the signal and the notified thread re-acquiring the lock, consuming the resource and making the condition false again. A while loop re-checks the condition after every wake-up, handling both spurious wakeups and the case where another thread consumed the resource first. The if-statement pattern is a common bug that leads to subtle crashes under concurrent load."

- question: "The wait() operation on a condition variable atomically releases the associated lock and suspends the calling thread."
  type: true-false
  answer: true
  explanation: "Atomicity here is critical for correctness. If releasing the lock and sleeping were two separate operations, a producer could signal between them — after the lock release but before sleep — causing the consumer to miss the signal and wait indefinitely. The atomic design of wait() closes this race window. This is a fundamental property of condition variables, not an implementation detail."

- question: "A thread woken by notify() can safely assume the condition it was waiting for is still true and proceed without re-checking."
  type: true-false
  answer: false
  explanation: "Under Mesa semantics — the model used by virtually all real systems — a signal only says 'something may have changed, check again.' It does not guarantee the condition is still true when the woken thread re-acquires the lock. Another thread may have consumed the resource in the interval. The correct pattern always re-checks the condition in a while loop after wait() returns, treating the wake-up as a prompt to re-evaluate rather than a confirmation."

- question: "Why must the condition check after a wait() call be placed in a while loop rather than an if statement?"
  type: short-answer
  answer: "Because under Mesa semantics, a thread can be woken up when the condition it was waiting for is no longer true. Two scenarios cause this: (1) spurious wakeups, where the OS wakes a thread for implementation reasons unrelated to a signal; (2) another thread acquires the lock and consumes the resource between the notify() call and the woken thread re-acquiring the lock. The while loop re-evaluates the condition every time the thread wakes, and only proceeds when the condition is genuinely satisfied."
  explanation: "The if-statement version is a common and dangerous bug. It works most of the time, since spurious wakeups are rare and contention is often low — but under load or on certain OSes, it will occasionally proceed with a false condition, leading to crashes or corrupt state. The while-loop pattern is always correct and adds negligible overhead, so it is the universal standard."
```

## Explainer

You already know that locks (mutexes) provide mutual exclusion — only one thread can hold the lock at a time, preventing data races on shared state. But locks alone cannot express waiting for a condition. Suppose a consumer thread wants to remove an item from a shared buffer, but the buffer is empty. With only a lock, the consumer would have to release the lock, busy-wait (repeatedly acquire the lock, check if the buffer is non-empty, release), wasting CPU cycles. **Condition variables** solve this by letting a thread say "wake me up when something changes" instead of spinning.

A condition variable is always used in conjunction with a lock. The pattern has three parts. First, the waiting thread acquires the lock and checks a condition (e.g., `buffer.size() > 0`). If the condition is false, it calls `wait()` on the condition variable, which atomically releases the lock and puts the thread to sleep — these two steps must be atomic to avoid a race where another thread signals between the release and the sleep. Second, when another thread changes the shared state (e.g., a producer adds an item to the buffer), it calls `notify()` (wake one waiter) or `notifyAll()` (wake all waiters) on the condition variable. Third, the woken thread re-acquires the lock and re-checks the condition in a **while loop**, not an if statement. The loop is essential because under Mesa-style semantics (used by pthreads, Java, and most real systems), another thread might have consumed the item between the signal and the re-acquisition of the lock.

A **monitor** packages this pattern into a clean abstraction. It is an object (or module) that encapsulates shared data along with the procedures that access it, and the language or runtime automatically enforces that only one thread can be executing inside the monitor at any time. You do not manually acquire and release locks — the monitor handles it. Condition variables live inside the monitor, providing the wait/signal mechanism for coordination. Java's `synchronized` keyword with `wait()`/`notifyAll()` is the most widely encountered monitor implementation. The bounded buffer becomes straightforward: `put()` waits on a "not full" condition and signals "not empty"; `get()` waits on "not empty" and signals "not full." All locking is implicit.

The key advantage over raw semaphores is clarity and safety. With semaphores, forgetting a `signal()` or placing it in the wrong order causes subtle deadlocks or race conditions that are hard to debug. Monitors make the critical section boundaries explicit through language constructs, and condition variables give you named, semantic wait points — you wait on "buffer not empty," not on an anonymous counter. This makes concurrent code easier to write correctly and easier to reason about during code review.
