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

## Questions

```yaml
- question: "Thread A holds a lock while updating a single pointer — an operation that takes about 20 nanoseconds. Thread B wants the same lock. A context switch costs approximately 1–5 microseconds. Which synchronization choice is most efficient for Thread B?"
  type: multiple-choice
  options:
    - "A blocking mutex, because it avoids wasting CPU cycles while waiting"
    - "A spinlock, because the expected wait (20ns) is far less than the context switch cost (1000–5000ns)"
    - "A spinlock, because spinlocks are always more efficient than blocking locks"
    - "A blocking mutex, because spinlocks can only be used in kernel code"
  answer: 1
  explanation: "The decision between spinning and blocking is a cost comparison: how long will we wait versus how much does a context switch cost? If the critical section is 20ns and a context switch costs 1–5 microseconds, blocking would waste far more time than spinning. The breakeven is roughly: if expected wait < cost of two context switches (sleep + wake), spin. If expected wait > that cost, block. This is the exact logic kernels use — spinlocks protect very short critical sections; mutexes protect longer ones."

- question: "On a single-processor system, thread A holds a spinlock and thread B is spinning on it. What happens?"
  type: multiple-choice
  options:
    - "Thread B acquires the lock quickly because thread A will finish its critical section before the scheduler intervenes"
    - "Thread B burns its entire time slice while thread A cannot run to release the lock — the spin is pure waste until the OS preempts thread B"
    - "The OS detects the spin pattern and automatically converts it to a blocking wait"
    - "Thread A is immediately preempted by the scheduler when thread B starts spinning"
  answer: 1
  explanation: "On a single CPU, the thread holding the lock cannot run while the spinner occupies the processor. Thread B loops uselessly until the OS timer interrupt fires and preempts it, finally scheduling thread A to run and release the lock. Then thread B can be scheduled back and acquire the lock. This wastes thread B's entire time slice accomplishing nothing. Spinlocks are fundamentally designed for multiprocessor systems where the lock holder is running on a *different* CPU and making progress toward releasing the lock."

- question: "Spinlocks rely on atomic hardware instructions like test-and-set or compare-and-swap to ensure that only one thread enters the critical section at a time."
  type: true-false
  answer: true
  explanation: "A spinlock loop like `while (test_and_set(&lock) == 1) {}` works because test-and-set is an atomic read-modify-write operation: it reads the current value and writes 1 in a single uninterruptible step. Without atomicity, two threads could both read 0, both decide the lock is free, and both enter the critical section — a race condition. The atomic instruction ensures mutual exclusion without OS intervention, which is what makes spinlocks viable in interrupt handlers and kernel code where calling into the scheduler is impossible."

- question: "Spinlocks are always more efficient than blocking locks because they avoid the overhead of context switches."
  type: true-false
  answer: false
  explanation: "Spinlocks are only more efficient when the critical section is short enough that the wait time is less than the cost of a context switch, AND only on multiprocessor systems where the lock holder can make progress on another CPU. On a single-processor system, spinning wastes the entire time slice. Under high contention or for long critical sections, spinning burns CPU cycles that could do useful work elsewhere. A blocking lock that yields the CPU is more efficient whenever the expected wait exceeds the context switch cost."

- question: "Why are spinlocks used inside OS kernels for protecting short critical sections, and what would go wrong if kernel code tried to use a blocking mutex instead?"
  type: short-answer
  answer: "Kernel code often cannot sleep: interrupt handlers run with interrupts disabled, and scheduler code cannot block because the scheduler itself is not yet runnable. A blocking mutex requires calling into the scheduler to sleep — which is circular or impossible in these contexts. Spinlocks work because they never call the scheduler; they just loop in the hardware."
  explanation: "Spinlocks are the synchronization primitive of last resort for code that cannot call into the scheduler. Interrupt handlers are the clearest example: an interrupt fires, preempting whatever was running, and the handler may need to access a shared data structure. If that structure is locked, the handler must spin — it cannot block because there is no return path through the scheduler. Similarly, the scheduler's own data structures (run queues, etc.) must be protected with spinlocks because protecting them with blocking locks would require the scheduler to be running — a chicken-and-egg problem. The cost is CPU waste if the spin is long, which is why kernel spinlocks are reserved exclusively for genuinely short critical sections."
```

## Explainer

From your study of mutual exclusion and locks, you know that when a thread finds a lock already held, it must wait. The question is *how* it waits. A **blocking lock** (like a mutex) puts the waiting thread to sleep and asks the OS scheduler to run something else — the thread gives up the CPU until the lock holder signals that the lock is free. A **spinlock** takes the opposite approach: the waiting thread stays on the CPU and continuously checks the lock in a tight loop, "spinning" until it becomes available. Think of it as the difference between taking a number at a deli counter and sitting down (blocking) versus standing at the counter watching the clerk and asking "is it my turn yet?" over and over (spinning).

Spinning sounds wasteful, and on a **single-processor** system it genuinely is. If only one CPU exists, the thread holding the lock cannot make progress while the spinner occupies the processor — spinning just burns cycles until the OS preempts the spinner and schedules the lock holder. But on a **multiprocessor** system, the lock holder is running on a different CPU and actively making progress. If the critical section is very short — say, updating a single counter or pointer — the lock will be released in a few dozen nanoseconds. In that scenario, the cost of spinning is far less than the cost of a context switch, which you know involves saving registers, switching page tables, and potentially flushing caches. The breakeven point is roughly: if the expected wait time is less than the cost of two context switches (one to sleep, one to wake up), spinning wins.

This is why spinlocks are the synchronization primitive of choice inside operating system kernels for protecting short critical sections, especially on multiprocessor machines. Interrupt handlers, scheduler code, and memory allocators all use spinlocks because they cannot afford to sleep — sleeping inside the scheduler would be circular. A common pattern is **spin-then-block**: try spinning for a brief period, and if the lock is still held, fall back to blocking. This hybrid approach, sometimes called an **adaptive lock**, captures the best of both worlds: fast acquisition when contention is low, and CPU-efficient waiting when contention is high.

The implementation of a spinlock relies on the atomic hardware instructions you studied, such as test-and-set or compare-and-swap. A minimal spinlock is just a loop: `while (test_and_set(&lock) == 1) { /* spin */ }`. When the lock variable is 0, test-and-set atomically sets it to 1 and returns 0, and the thread enters the critical section. When the lock is already 1, test-and-set returns 1, and the thread keeps looping. The danger is **priority inversion**: if a low-priority thread holds a spinlock and a high-priority thread spins on it, the high-priority thread wastes its entire time slice spinning while the low-priority thread cannot run to release the lock. Real spinlock implementations address this with techniques like disabling preemption while holding the lock, ensuring the holder runs to completion quickly.
