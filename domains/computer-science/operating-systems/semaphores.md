---
id: semaphores
title: Semaphores
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- monitors-and-condition-variables
- deadlock-conditions
tags:
- semaphore
- binary-semaphore
- counting-semaphore
- P-V-operations
- Dijkstra
stage: formal-systems
status: validated
---

# Semaphores

## Core Idea
A semaphore, introduced by Dijkstra, is an integer synchronization variable with two atomic operations: wait (P) decrements the value and blocks if it becomes negative, and signal (V) increments the value and wakes a blocked thread if any. A binary semaphore (values 0 and 1) implements mutual exclusion and behaves like a mutex. A counting semaphore (any non-negative integer) tracks the count of available resources, enabling the classic producer-consumer and bounded-buffer patterns. Unlike mutexes, a semaphore can be signaled by a thread different from the one that waited, making them suitable for signaling between threads.

## How It's Best Learned
Implement the bounded-buffer (producer-consumer) problem using two counting semaphores (empty slots, full slots) plus a mutex. Trace through an execution by hand, showing how the semaphore values change.

## Common Misconceptions
- Semaphores are not queues; the standard definition doesn't specify which blocked thread is woken.
- Using semaphores correctly requires disciplined P before critical section and V after, or bugs are subtle.

## Questions

```yaml
- question: "A parent thread must wait until a child thread finishes initialization before proceeding. Which approach is most appropriate?"
  type: multiple-choice
  options:
    - "A mutex initialized to locked — the parent acquires the lock and the child releases it after finishing"
    - "A semaphore initialized to 0 — the parent calls wait (blocking), and the child calls signal after initialization completes"
    - "A mutex initialized to unlocked — the parent polls in a loop until it can acquire the lock"
    - "A semaphore initialized to 1 — both threads call wait, and whichever succeeds first proceeds"
  answer: 1
  explanation: "This is the signaling pattern that semaphores handle and mutexes cannot. The semaphore starts at 0 (no 'credits'), so the parent's wait immediately blocks. When the child finishes, it signals — incrementing the counter and unblocking the parent. A mutex cannot do this cleanly because mutexes require the same thread to both acquire and release; here, the child releases what the parent is waiting on, which is a different thread."

- question: "A bounded buffer holds up to 5 items. You use a counting semaphore 'empty' (initialized to 5) and 'full' (initialized to 0). A producer wants to insert an item. What is the correct sequence?"
  type: multiple-choice
  options:
    - "Signal 'empty', insert the item, then signal 'full'"
    - "Wait on 'full', insert the item, then signal 'empty'"
    - "Wait on 'empty', insert the item, then signal 'full'"
    - "Wait on both 'empty' and 'full' before inserting"
  answer: 2
  explanation: "The producer must first claim an empty slot (wait on 'empty' — decrement the count of available empty slots; block if zero), insert the item, then announce a new full slot (signal 'full' — increment the count of full slots, potentially waking a waiting consumer). Waiting on 'full' (option B) would mean waiting until the buffer is full before inserting, which is backwards."

- question: "A binary semaphore and a mutex are functionally identical because both restrict access to one thread at a time."
  type: true-false
  answer: false
  explanation: "The critical difference is ownership. A mutex must be released by the same thread that acquired it — ownership is thread-bound. A semaphore can be signaled by any thread, regardless of which thread called wait. This distinction makes semaphores suitable for inter-thread signaling (parent waits for child's completion), a pattern that requires one thread to 'unlock' what another is waiting on — which mutex semantics explicitly forbid."

- question: "Calling signal (V) on a semaphore when no threads are blocked still increments the counter, effectively saving the signal as a credit for a future wait call."
  type: true-false
  answer: true
  explanation: "Signal unconditionally increments the counter. If threads are blocked, one is woken; if none are blocked, the counter simply increments. This 'saved credit' behavior is important: if the signaling thread runs before the waiting thread, the wait call will find the counter already positive and proceed without blocking. This is one key advantage of semaphores over condition variables, which lose signals if no thread is waiting."

- question: "Why is it correct to say semaphores 'generalize' mutexes rather than simply being a different kind of lock?"
  type: short-answer
  answer: "A mutex is a binary, ownership-bound lock: only two states (locked/unlocked), and the same thread must release it. A semaphore replaces the binary state with an integer counter, enabling a superset of behaviors: a binary semaphore replicates mutual exclusion (values 0 and 1), while counting semaphores track N available resources and allow any thread to signal. Mutexes are a special case of the semaphore concept, not a parallel idea — which is why 'generalize' is the right word."
  explanation: "This framing matters practically: when a mutex isn't expressive enough (e.g., for producer-consumer coordination or thread signaling), reaching for a semaphore is the natural next step. Understanding mutexes as a degenerate case of semaphores, rather than as a separate concept, clarifies why semaphores are more powerful and more error-prone."
```

## Explainer

You already understand that mutexes provide mutual exclusion — only one thread enters the critical section at a time. A **semaphore** generalizes this idea by replacing the binary locked/unlocked state with an integer counter, enabling a much wider range of synchronization patterns. Dijkstra introduced semaphores in 1965, naming the two operations **P** (from the Dutch *proberen*, to test) and **V** (*verhogen*, to increment). In modern terminology these are called **wait** and **signal**, but the semantics are identical: wait decrements the counter and blocks if it goes negative; signal increments the counter and wakes a blocked thread if any are waiting.

A **binary semaphore** has values restricted to 0 and 1 and behaves like a mutex — wait locks it, signal unlocks it. The key difference is ownership: a mutex must be released by the same thread that acquired it, but a semaphore can be signaled by any thread. This makes semaphores ideal for **signaling** between threads. For example, a parent thread can wait on a semaphore initialized to 0; when the child thread finishes its setup, it signals the semaphore, and the parent unblocks. No mutex can express this pattern cleanly because no single thread "owns" both sides of the interaction.

A **counting semaphore** starts at some value N representing the number of available resources. Each wait decrements the count, and each signal increments it. When the count reaches zero, the next thread to wait blocks until another thread signals. This is the foundation of the bounded-buffer (producer-consumer) pattern: one counting semaphore tracks empty slots, another tracks full slots, and together they coordinate producers and consumers without busy-waiting.

The discipline required with semaphores is strict: every wait must have a matching signal, and the order matters. If you wait on two semaphores in different orders in different threads, you risk deadlock. If you forget a signal, a thread blocks forever. If you add an extra signal, a thread enters a critical section when it should not. Unlike higher-level constructs like monitors, semaphores give you no compile-time safety net — correctness depends entirely on the programmer placing P and V in the right places. This is both their power and their danger, which is why understanding them thoroughly is essential before moving on to monitors and condition variables.
