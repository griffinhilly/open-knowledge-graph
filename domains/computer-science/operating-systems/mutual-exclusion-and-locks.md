---
id: mutual-exclusion-and-locks
title: Mutual Exclusion and Locks
domain: computer-science
course: operating-systems
prerequisites:
- id: synchronization-problem
  type: hard
builds-toward:
- semaphores
- counting-semaphores-resource-pools
- monitors-and-condition-variables
tags:
- synchronization
- locks
- critical-sections
stage: formal-systems
status: validated
---

# Mutual Exclusion and Locks

## Core Idea
Mutual exclusion ensures only one thread executes in a critical section (shared resource access) at a time. Simple locks (mutexes) achieve this via atomic operations. Spinlocks busy-wait; blocking locks suspend threads and use context switching. Fairness, deadlock freedom, and starvation resistance depend on lock implementation.

## How It's Best Learned
Implement a spinlock and a blocking lock; measure contention, overhead, and performance under various contention levels.

## Questions

```yaml
- question: "Thread A and Thread B both execute the sequence: (1) read lock variable — see it is free, (2) set lock variable to 'taken'. What concurrency problem does this expose?"
  type: multiple-choice
  options:
    - "Both threads will enter the critical section simultaneously, violating mutual exclusion"
    - "Thread B will be permanently blocked waiting for Thread A to release the lock"
    - "The lock variable will overflow from concurrent writes"
    - "This is not a problem — only one thread can read memory at a time"
  answer: 0
  explanation: "If read and write are separate operations, both threads can observe the lock as free before either marks it as taken. Both then mark it as taken and proceed into the critical section together — mutual exclusion is violated. This is precisely why hardware provides atomic instructions like test-and-set and compare-and-swap: they make the check and the claim a single indivisible step so no thread can be interrupted between them."

- question: "A system uses a blocking lock for a critical section that consistently completes in 3 nanoseconds on a modern CPU. A performance engineer proposes switching to a spinlock. What is the likely performance outcome?"
  type: multiple-choice
  options:
    - "Worse — spinlocks waste CPU cycles that could serve other threads during longer critical sections"
    - "Better — for a very short critical section, avoiding two context switches (sleep + wake) outweighs the cost of briefly spinning"
    - "Identical — spinlocks and blocking locks have the same overhead by design"
    - "Worse — spinlocks cannot guarantee mutual exclusion for nanosecond-scale operations"
  answer: 1
  explanation: "The spinlock vs. blocking lock tradeoff hinges on how long the wait is. A context switch takes thousands to tens of thousands of nanoseconds. For a 3 ns critical section, the cost of putting a thread to sleep and waking it back up vastly exceeds the cost of spinning briefly. Spinlocks are efficient for very short critical sections with low contention; blocking locks are better when critical sections are long enough that the CPU can do useful work during the wait."

- question: "A correctly implemented spinlock guarantees that nearly every thread waiting for the lock will eventually acquire it."
  type: true-false
  answer: false
  explanation: "A naive spinlock does not guarantee starvation freedom. On some hardware, memory access patterns can favor one core over others, causing a thread to spin indefinitely while another repeatedly re-acquires the lock. Ticket locks address this by assigning each waiting thread a number and serving them in order, guaranteeing that every thread eventually gets its turn. Starvation freedom is a design property that must be explicitly built in — it does not come for free from mutual exclusion alone."

- question: "The fundamental hardware requirement for any correct lock implementation is an operation that atomically reads and writes a shared variable in a single indivisible step."
  type: true-false
  answer: true
  explanation: "Without atomicity, any implementation of acquire() that checks 'is the lock free?' and then 'marks it as taken' is vulnerable to interleaving: two threads can both pass the check before either marks it. Hardware atomic instructions — test-and-set, compare-and-swap, fetch-and-add — make the read-modify-write sequence indivisible. This hardware primitive is the foundation that all higher-level synchronization mechanisms are built on."

- question: "Why must the 'check if free' and 'mark as taken' steps of a lock's acquire() operation be atomic, and what goes wrong if they are not?"
  type: short-answer
  answer: "If the two steps are separate, a thread can be interrupted or preempted between them. Thread A reads the lock as free; before it marks it taken, Thread B also reads the lock as free; both then mark it taken and both enter the critical section simultaneously — violating mutual exclusion and potentially corrupting shared state. Atomic instructions prevent this by making the check-and-claim a single step that cannot be interrupted."
  explanation: "This is the core correctness requirement for locking. Any implementation that separates the read from the write — even by a single instruction — opens a race condition window. The entire value of a lock is that exactly one thread can be in the critical section at a time; non-atomic acquire() destroys this guarantee."
```

## Explainer

From concurrency and race conditions, you know that when multiple threads access shared data simultaneously and at least one is writing, the result depends on the unpredictable interleaving of their operations. A **critical section** is a region of code that accesses such shared data and must not be executed by more than one thread at a time. **Mutual exclusion** is the property that guarantees this: at most one thread is in the critical section at any moment.

A **lock** (or **mutex**) is the simplest mechanism to enforce mutual exclusion. The interface is minimal: `acquire()` before entering the critical section and `release()` after leaving. If thread A has acquired the lock, thread B's call to `acquire()` will not return until A calls `release()`. The critical implementation detail is how `acquire()` is made **atomic** — the check "is the lock free?" and the action "mark it as taken" must happen as a single indivisible step. If they were separate, two threads could both see the lock as free and both claim it, defeating the entire purpose. Hardware provides atomic instructions like **test-and-set**, **compare-and-swap** (CAS), or **fetch-and-add** that make this possible.

The two fundamental lock designs differ in what a thread does while waiting. A **spinlock** loops continuously, checking the lock in a tight loop (`while (test_and_set(&lock));`). This wastes CPU cycles but avoids the overhead of a context switch, making spinlocks efficient when the critical section is very short and the wait is brief. A **blocking lock** (or sleeping lock) puts the waiting thread to sleep — removing it from the CPU's run queue — and wakes it when the lock becomes available. This is better when critical sections are long, because the CPU can do useful work running other threads instead of spinning. The tradeoff is the cost of two context switches (sleep and wake) versus the cost of wasted CPU cycles from spinning.

Beyond the basic design, lock implementations must consider **fairness** and **livelock**. A naive spinlock can starve some threads if the hardware consistently favors one core's memory access over another. **Ticket locks** solve this by assigning each waiting thread a number and serving them in order, like a bakery queue. A correct lock must also guarantee **deadlock freedom** — if the lock is released, some waiting thread must eventually acquire it — and ideally **starvation freedom** — every thread that requests the lock eventually gets it. These properties are not automatic; they depend on the lock algorithm and the underlying hardware's memory ordering guarantees.
