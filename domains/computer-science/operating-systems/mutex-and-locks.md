---
id: mutex-and-locks
title: Mutexes and Locking Primitives
domain: computer-science
course: operating-systems
prerequisites:
- id: synchronization-problem
  type: hard
builds-toward:
- semaphores
- deadlock-conditions
tags:
- mutex
- spinlock
- test-and-set
- compare-and-swap
- locking
stage: formal-systems
status: validated
---

# Mutexes and Locking Primitives

## Core Idea
A mutex (mutual exclusion lock) is the fundamental synchronization primitive that allows at most one thread to hold it at a time; any other thread attempting to acquire a held mutex blocks until it is released. Hardware support is essential: atomic instructions like test-and-set or compare-and-swap allow a thread to atomically read and conditionally modify a memory location, enabling correct mutex implementation without race conditions in the lock acquisition code itself. Spinlocks busy-wait (spin) in a loop testing the lock, suitable for short critical sections on multiprocessors; blocking mutexes deschedule the waiting thread, suitable for longer waits.

## How It's Best Learned
Implement a spinlock using a compare-and-swap loop. Measure the performance difference between a spinlock and a pthread_mutex on a long versus short critical section.

## Common Misconceptions
- A mutex held by one thread cannot be released by a different thread (unlike some semaphores).
- Spinlocks waste CPU cycles; they should never be used when the lock holder might be descheduled.

## Questions

```yaml
- question: "A developer implements a mutex using a shared boolean variable: threads check if `locked == false`, then set `locked = true`. Why does this fail to provide mutual exclusion?"
  type: multiple-choice
  options:
    - "Boolean variables cannot store lock state reliably across all CPU architectures"
    - "Two threads can both read `locked == false` before either writes `true`, allowing both to enter the critical section simultaneously"
    - "This approach works on single-core processors but fails only on multiprocessor systems with shared cache"
    - "This is a valid implementation; it is the standard way to build a software mutex"
  answer: 1
  explanation: "This is the fundamental race condition in lock implementation. Between the time Thread A reads `locked == false` and when it writes `locked = true`, Thread B may also read `locked == false`. Both threads believe they have acquired the lock and enter the critical section simultaneously — defeating mutual exclusion. This is not a Boolean limitation or a multiprocessor-only problem; it can happen on any system because the check-then-set is not atomic. This is exactly why hardware atomic instructions (test-and-set, compare-and-swap) are necessary: they make read-and-modify indivisible."

- question: "A lock protects a critical section that typically executes in 150 nanoseconds on a multiprocessor system. Which lock type is most appropriate?"
  type: multiple-choice
  options:
    - "A blocking mutex, because it always uses CPU cycles more efficiently than spinning"
    - "A spinlock, because the expected wait is short enough that spin overhead is less than sleep/wake overhead"
    - "A spinlock, but only if the critical section contains no function calls or branches"
    - "A blocking mutex, because spinlocks are always slower due to their busy-wait loop"
  answer: 1
  explanation: "Spinlocks are efficient when the expected wait time is very short because putting a thread to sleep and waking it up involves OS scheduling overhead that can exceed the wait itself. If Thread A holds a spinlock and executes its 150-nanosecond critical section, Thread B spinning on another core grabs the lock almost instantly when A releases it — no context-switch overhead. The conditions favoring spinlocks are: multiple cores (so Thread B's spinning doesn't block Thread A from running) and short critical sections (so total spin time is bounded and small)."

- question: "A mutex must be released by the same thread that acquired it."
  type: true-false
  answer: true
  explanation: "This ownership property is what distinguishes mutexes from semaphores. A mutex is owned by the thread that acquired it; only the owner can release it. This enables features like priority inheritance (temporarily raising the lock holder's priority to prevent preemption while holding the lock) and recursive locking (allowing the same thread to re-acquire a lock it already holds). It also simplifies correctness reasoning — you always know which thread is responsible for releasing the lock. Releasing a mutex from a different thread is a programming error that typically produces undefined behavior."

- question: "Spinlocks are generally more CPU-efficient than blocking mutexes because they avoid the overhead of context switches."
  type: true-false
  answer: false
  explanation: "Spinlocks are more efficient only when the expected wait is very short. When the lock holder may take a long time or may be descheduled by the OS, a spinning thread wastes CPU cycles doing nothing useful — and on a single-core system, spinning can even prevent the lock holder from being scheduled, creating a livelock. Blocking mutexes trade the cost of one context switch for the guarantee that the CPU does useful work while the thread waits. The correct principle: spinlocks for short critical sections on multiprocessors; blocking mutexes when wait time is uncertain or potentially long."

- question: "Why is hardware support — such as test-and-set or compare-and-swap — essential for correct mutex implementation, rather than software logic alone?"
  type: short-answer
  answer: "Software logic uses separate read and write operations, and two threads can interleave between them: Thread A reads the lock as free, then Thread B reads it as free before either writes 'locked.' Both believe they hold the lock. Hardware atomic instructions perform a read-and-conditional-write as a single indivisible operation that cannot be interrupted or interleaved. Test-and-set atomically reads a memory location and sets it to 1, returning the old value — if the old value was 0, you got the lock; if 1, someone else has it. This indivisibility is a hardware guarantee that software logic alone cannot provide."
  explanation: "The key insight is that the race condition lives in the acquisition code itself, not only in the critical section the mutex protects. You need mutual exclusion to implement mutual exclusion — which would be circular if hardware didn't break the circularity by providing atomicity at the instruction level. Test-and-set and compare-and-swap are the CPU's primitives for 'this operation is atomic; no other CPU operation can observe it mid-execution.' Every correct mutex implementation ultimately rests on one of these primitives."
```

## Explainer

From the synchronization problem, you know that concurrent threads accessing shared data can produce incorrect results due to race conditions — one thread reads a value, another modifies it, and the first thread proceeds with stale data. A **mutex** (short for mutual exclusion) is the most fundamental solution: it is a lock that only one thread can hold at a time. Before entering a **critical section** (code that accesses shared data), a thread acquires the mutex. If another thread already holds it, the requesting thread waits. When the holding thread leaves the critical section, it releases the mutex, allowing a waiting thread to proceed. This serializes access to shared data, eliminating race conditions.

The tricky part is implementing the mutex itself. Consider a naive attempt: use a shared variable `locked` that threads check before entering. Thread A reads `locked == false`, decides to enter, and sets `locked = true`. But thread B might read `locked == false` at the exact same instant, before A writes `true` — now both threads think they hold the lock. The acquisition code itself has a race condition. This is where hardware atomic instructions become essential. **Test-and-set** atomically reads a memory location and sets it to 1 in a single indivisible operation, returning the old value. If the old value was 0, you got the lock; if it was 1, someone else has it. **Compare-and-swap** is more flexible: it atomically checks if a location holds an expected value and, only if so, replaces it with a new value. Both instructions are provided by the CPU hardware and cannot be interrupted, so no interleaving can corrupt the lock acquisition.

The simplest mutex built on these primitives is a **spinlock**: a thread executes test-and-set (or CAS) in a tight loop, spinning until the lock becomes available. Spinlocks are efficient when the expected wait is very short — a few microseconds — because spinning avoids the overhead of putting a thread to sleep and waking it up later. On a multiprocessor, while thread A holds a spinlock and executes its short critical section on one core, thread B spins on another core and grabs the lock almost instantly when A releases it. However, if the lock holder might run for a long time or might be descheduled by the OS, spinning wastes CPU cycles doing nothing useful. In that case, a **blocking mutex** (like `pthread_mutex`) is better: it puts the waiting thread to sleep and the OS wakes it when the lock is released, freeing the CPU for other work.

An important ownership rule distinguishes mutexes from other synchronization primitives you will encounter next (like semaphores): **a mutex must be released by the same thread that acquired it**. This ownership property enables useful features like priority inheritance (temporarily boosting a lock holder's priority to prevent priority inversion) and recursive locking (allowing the same thread to re-acquire a lock it already holds). It also makes reasoning about correctness simpler — you always know which thread is responsible for releasing a lock. Getting locking discipline right — acquiring locks in a consistent order, holding them for the minimum necessary time, and always releasing them (even on error paths) — is one of the most important practical skills in concurrent programming and directly sets up the deadlock analysis you will study next.
