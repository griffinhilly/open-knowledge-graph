---
id: binary-semaphores-mutexes
title: Binary Semaphores and Mutexes
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- counting-semaphores-resource-pools
- condition-variables-and-monitors
- producer-consumer-classic-sync
tags:
- semaphores
- synchronization
- classic-primitives
stage: formal-systems
status: validated
---

# Binary Semaphores and Mutexes

## Core Idea
A binary semaphore is a synchronization primitive with a counter of 0 or 1, acting as a lock. wait() (P) decrements; if already 0, the thread blocks. signal() (V) increments and wakes a waiting thread. Binary semaphores are conceptually simple but can be error-prone; locked semaphores ensure unlock occurs in the same thread.

## Common Misconceptions
Semaphore value never goes negative (it does if threads block; negative values represent blocked threads). Semaphores are easier than locks (implementation and usage can be subtle and error-prone).

## Questions

```yaml
- question: "Thread A acquires a binary semaphore and enters a critical section. While Thread A is still inside, Thread B (a completely different thread) calls signal() on that same semaphore. What is the consequence?"
  type: multiple-choice
  options:
    - "The OS detects the violation and terminates Thread B with an error"
    - "Thread B blocks until Thread A explicitly releases the semaphore"
    - "The semaphore is incremented and a waiting thread can now enter the critical section, allowing two threads inside simultaneously"
    - "Thread A is automatically evicted from the critical section when the counter changes"
  answer: 2
  explanation: "A binary semaphore has no ownership: any thread can call signal() at any time. Thread B's signal() increments the counter from 0 to 1, and any thread blocked on wait() can now proceed — entering the critical section while Thread A is still inside. This violates mutual exclusion. This vulnerability is precisely what mutexes solve: a mutex tracks which thread locked it and rejects unlock attempts from any other thread, preventing unauthorized releases."

- question: "What is the key advantage of a mutex over a binary semaphore for protecting a critical section?"
  type: multiple-choice
  options:
    - "A mutex can be acquired by multiple threads simultaneously, increasing concurrency"
    - "A mutex uses spin-waiting rather than blocking, reducing context-switch overhead"
    - "A mutex enforces ownership: only the thread that locked it can unlock it, preventing accidental or unauthorized release by other threads"
    - "A mutex automatically detects and resolves circular deadlocks"
  answer: 2
  explanation: "Ownership is the defining difference. The OS tracks which thread holds the mutex, and any unlock attempt from a different thread is rejected. This prevents the scenario above — where Thread B inadvertently releases Thread A's lock — and also enables priority inheritance: if a high-priority thread waits for a mutex held by a low-priority thread, the OS can temporarily boost the low-priority thread's priority to prevent priority inversion. Binary semaphores support neither of these safety properties."

- question: "A binary semaphore's internal counter can never go negative — once it reaches zero, further wait() calls simply block without changing the counter's value."
  type: true-false
  answer: false
  explanation: "This is a common misconception explicitly noted in the topic. In many implementations, the counter goes negative, where the absolute value represents the number of blocked threads. If three threads call wait() when the counter is already 0, the counter becomes -3, tracking that three threads are queued. Each subsequent signal() call unblocks one thread and increments the counter toward zero. Whether the implementation stores a negative count or a separate queue length varies, but conceptually 'negative value = number of blocked threads' accurately describes semaphore state."

- question: "The ownership property of a mutex enables the OS to temporarily raise the priority of a low-priority thread that holds the mutex when a high-priority thread is waiting for it."
  type: true-false
  answer: true
  explanation: "This optimization is called priority inheritance and depends directly on the mutex's ownership tracking. Because the OS knows exactly which thread holds the mutex, it can identify who is indirectly blocking the high-priority waiter and elevate that thread's priority to let it finish and release the lock sooner. Without ownership tracking, as in a binary semaphore, the OS cannot identify the holder and cannot apply this fix. Priority inversion — where a medium-priority thread preempts the lock holder and starves the high-priority waiter — is a real-world failure mode that mutex ownership is designed to prevent."

- question: "Explain why the ownership constraint of a mutex matters for correct concurrent programming. What failure mode does it prevent that a binary semaphore does not?"
  type: short-answer
  answer: "A mutex's ownership constraint means only the acquiring thread can release it. This prevents accidental or erroneous release by other threads — due to bugs, early returns, or exceptions — which would allow multiple threads into a critical section simultaneously, violating mutual exclusion. With a binary semaphore, any thread calling signal() increments the counter, even a thread that never called wait(). The ownership constraint also supports priority inheritance, since the OS can identify the exact thread to elevate when a higher-priority thread is blocked."
  explanation: "The classic failure scenario: Thread A acquires semaphore S and enters the critical section. Thread B, due to a bug, calls signal(S). The semaphore is now 1. Thread C, blocked on wait(S), wakes up and enters the critical section. Threads A and C are now both inside simultaneously. A mutex rejects Thread B's signal() call — it's not the owner — and the invariant holds. This is why mutexes are the default primitive for critical sections in modern systems programming, and why semaphores are reserved for signaling patterns (producer/consumer) where ownership is intentionally not required."
```

## Explainer

You already understand mutual exclusion and the basic idea of a lock: only one thread can hold it at a time, and any other thread that tries to acquire it must wait. A **binary semaphore** formalizes this idea using a counter that is always 0 or 1. When the counter is 1, the resource is available; when it is 0, the resource is held. The two fundamental operations — traditionally called **P** (from the Dutch *proberen*, "to try") and **V** (*verhogen*, "to increment") — are also known as **wait()** and **signal()**. Wait decrements the counter: if the result is 0, the thread proceeds; if the counter was already 0, the thread blocks and joins a queue. Signal increments the counter and wakes one blocked thread if any are waiting. Both operations are **atomic** — they cannot be interrupted halfway through — which is what makes the whole mechanism safe.

A **mutex** (short for "mutual exclusion") looks almost identical to a binary semaphore, but it carries an additional constraint: **ownership**. Only the thread that locked the mutex can unlock it. With a plain binary semaphore, any thread can call signal(), which means thread A could accidentally (or intentionally) release a lock held by thread B. A mutex prevents this by tracking which thread holds it and rejecting unlock attempts from other threads. This ownership property also enables **priority inheritance** — if a high-priority thread is waiting for a mutex held by a low-priority thread, the OS can temporarily boost the low-priority thread's priority to avoid **priority inversion**, a situation where a medium-priority thread preempts the lock holder and indirectly blocks the high-priority thread.

The classic usage pattern is straightforward: surround a critical section with wait() before and signal() after. But the simplicity is deceptive. If a thread acquires semaphore A then tries to acquire semaphore B, while another thread acquires B then tries A, you have a deadlock. If a thread takes an early return or throws an exception between wait() and signal(), the semaphore is never released and every subsequent thread blocks forever. These failure modes are why higher-level abstractions like monitors and condition variables were invented — they bundle the lock with the condition-checking logic and ensure cleanup even when things go wrong. Understanding binary semaphores is essential because those higher-level tools are built on top of them, and when debugging concurrency bugs, you often need to reason at this level.

Consider a concrete analogy: a single-occupancy bathroom with a lock. The binary semaphore is the lock mechanism itself — flip it to "occupied" when you enter, flip it to "vacant" when you leave. A mutex adds a rule: only the person inside can unlock the door. Without that rule, someone outside could flip the lock while you are still using the bathroom — technically "correct" in the semaphore model, but clearly wrong in practice. Most OS synchronization scenarios require the mutex's ownership guarantee, which is why mutexes are the default choice for protecting critical sections in modern systems programming.
