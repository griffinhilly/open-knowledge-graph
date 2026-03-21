---
id: test-and-set-primitive
title: Test-and-Set and Atomic Primitives
domain: computer-science
course: operating-systems
prerequisites:
- id: software-mutual-exclusion-solutions
  type: hard
- id: atomic-operations-compare-and-swap
  type: soft
builds-toward:
- semaphore-formal-definition
tags:
- synchronization
- atomic
- hardware
stage: formal-systems
status: draft
---

# Test-and-Set and Atomic Primitives

## Core Idea
Test-and-set, compare-and-swap, and similar atomic operations read and modify memory in a single indivisible instruction. These enable efficient lock implementation without polling or context switches, providing the hardware foundation for high-level synchronization primitives.

## Questions

```yaml
- question: "A thread executes test-and-set on a shared lock variable and the instruction returns 1. What should the thread do next?"
  type: multiple-choice
  options:
    - "Enter the critical section — returning 1 means the lock is now acquired"
    - "Release the lock by writing 0 — returning 1 means the thread previously held it"
    - "Spin and retry — returning 1 means the lock was already held by another thread"
    - "Block until the OS wakes it — test-and-set automatically suspends the thread when the lock is taken"
  answer: 2
  explanation: "Test-and-set atomically reads the current value and sets it to 1, returning the old value. If the old value was 0 (unlocked), the thread changed it from 0→1 and now holds the lock — proceed. If the old value was 1 (already locked), the thread changed it from 1→1 (no net change) and the lock was already held. A return of 1 means 'it was locked when I looked' — the thread must retry. Option A reverses the logic. Option D confuses test-and-set (a busy-waiting primitive) with blocking OS synchronization."

- question: "Why can't Peterson's algorithm reliably guarantee mutual exclusion on modern multicore processors without additional hardware support?"
  type: multiple-choice
  options:
    - "It uses too many shared variables for the hardware cache to track efficiently"
    - "Modern processors may reorder memory operations, breaking the assumptions Peterson's algorithm relies on"
    - "Peterson's algorithm requires atomic increment operations that are not available on all hardware"
    - "It only works for two threads, so systems with more threads require a different approach"
  answer: 1
  explanation: "Peterson's algorithm assumes that writes to shared memory are immediately visible to other processors in the order they were issued — sequential consistency. Modern out-of-order processors and cache coherence protocols can reorder memory operations for performance, so the careful read-write sequence that Peterson's algorithm relies on can arrive at other cores in a different order than intended, breaking the mutual exclusion guarantee. Hardware atomic primitives bypass this problem by making the read-modify-write sequence truly indivisible at the hardware level."

- question: "The test-and-set instruction is atomic: no other processor can access the targeted memory location between the read and the write."
  type: true-false
  answer: true
  explanation: "This is precisely what makes test-and-set useful. The processor's cache coherence protocol ensures exclusive access to the memory location for the duration of the operation — no other core can observe an intermediate state. The location transitions from old-value to 1 instantaneously from the perspective of all other processors. This hardware guarantee is what software-only solutions cannot provide on modern out-of-order hardware, and it is the foundation for all higher-level synchronization primitives."

- question: "Compare-and-swap (CAS) and test-and-set solve exactly the same problem in exactly the same way; CAS is simply a more recent version of the same idea."
  type: true-false
  answer: false
  explanation: "While both are atomic read-modify-write primitives, CAS is strictly more flexible. CAS takes three arguments (a location, an expected old value, and a new value) and only performs the write if the current value matches the expected value — reporting whether the swap succeeded. This conditionality enables lock-free data structures that test-and-set cannot implement. With CAS, a thread can optimistically read a value, compute an update, and atomically commit it only if no other thread changed the value in the meantime — without holding any lock."

- question: "Why is hardware-provided atomicity necessary for synchronization on modern systems? Why isn't a careful sequence of software operations sufficient?"
  type: short-answer
  answer: "Modern processors execute instructions out of order and use private caches that may not immediately propagate writes to other cores. A software sequence like 'read a variable, check its value, write a new value' is not atomic — another thread can interleave between the read and the write, creating a race condition. Hardware atomic instructions use the processor's cache coherence protocol to ensure no other core can access the target location while the operation is in progress, making the entire read-modify-write appear instantaneous to the rest of the system. This guarantee cannot be replicated purely in software on modern architectures."
  explanation: "The root cause is that software mutual exclusion assumes sequential consistency — that all processors see memory operations in the same order they were issued. Modern CPUs trade this for performance by reordering operations and using private caches. Hardware primitives restore a strong guarantee for specific operations: the cache coherence protocol forces all cores to serialize access to the target address for the duration of the atomic instruction. This is exactly what Peterson's algorithm assumes but cannot enforce, and what test-and-set and CAS provide directly."
```

## Explainer

From studying software mutual exclusion solutions like Peterson's algorithm, you know the fundamental problem: two threads both want to enter a critical section, and we need a protocol that guarantees only one gets in at a time. Software solutions work, but they rely on careful sequences of reads and writes to shared variables — and on modern processors with out-of-order execution and caching, these sequences can break in subtle ways. The hardware solution is to give the processor a single instruction that does two things at once, indivisibly.

**Test-and-set** is the simplest such instruction. It reads the current value of a memory location, sets it to 1 (or true), and returns the old value — all in one atomic step. No other processor or thread can intervene between the read and the write. To build a lock, you initialize a shared variable `lock` to 0 (unlocked). A thread that wants to enter the critical section executes test-and-set on `lock`. If the old value was 0, the thread knows it just changed the lock from unlocked to locked — it now holds the lock and can proceed. If the old value was 1, someone else already holds the lock, and the thread must try again (spinning in a loop until test-and-set returns 0).

**Compare-and-swap** (CAS) is a more flexible variant. It takes three arguments: a memory location, an expected old value, and a new value. It atomically checks whether the location holds the expected value; if so, it replaces it with the new value and reports success; if not, it does nothing and reports failure. CAS can implement not just locks but also lock-free data structures — for example, you can atomically update a linked list's head pointer only if no other thread changed it since you last read it. This "optimistic" approach avoids locking entirely in the uncontended case, which can dramatically improve performance on multi-core systems.

The key insight is that these operations derive their power from hardware guarantees. The processor's memory bus or cache coherence protocol ensures that when one core executes test-and-set, no other core can access that memory location until the operation completes. This atomicity cannot be achieved by software alone on modern hardware — it requires dedicated instructions like x86's `XCHG`, `LOCK CMPXCHG`, or ARM's `LDREX`/`STREX` pairs. These primitives are the foundation on which all higher-level synchronization — semaphores, mutexes, condition variables — is ultimately built.
