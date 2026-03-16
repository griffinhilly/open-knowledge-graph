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

## Explainer

From studying software mutual exclusion solutions like Peterson's algorithm, you know the fundamental problem: two threads both want to enter a critical section, and we need a protocol that guarantees only one gets in at a time. Software solutions work, but they rely on careful sequences of reads and writes to shared variables — and on modern processors with out-of-order execution and caching, these sequences can break in subtle ways. The hardware solution is to give the processor a single instruction that does two things at once, indivisibly.

**Test-and-set** is the simplest such instruction. It reads the current value of a memory location, sets it to 1 (or true), and returns the old value — all in one atomic step. No other processor or thread can intervene between the read and the write. To build a lock, you initialize a shared variable `lock` to 0 (unlocked). A thread that wants to enter the critical section executes test-and-set on `lock`. If the old value was 0, the thread knows it just changed the lock from unlocked to locked — it now holds the lock and can proceed. If the old value was 1, someone else already holds the lock, and the thread must try again (spinning in a loop until test-and-set returns 0).

**Compare-and-swap** (CAS) is a more flexible variant. It takes three arguments: a memory location, an expected old value, and a new value. It atomically checks whether the location holds the expected value; if so, it replaces it with the new value and reports success; if not, it does nothing and reports failure. CAS can implement not just locks but also lock-free data structures — for example, you can atomically update a linked list's head pointer only if no other thread changed it since you last read it. This "optimistic" approach avoids locking entirely in the uncontended case, which can dramatically improve performance on multi-core systems.

The key insight is that these operations derive their power from hardware guarantees. The processor's memory bus or cache coherence protocol ensures that when one core executes test-and-set, no other core can access that memory location until the operation completes. This atomicity cannot be achieved by software alone on modern hardware — it requires dedicated instructions like x86's `XCHG`, `LOCK CMPXCHG`, or ARM's `LDREX`/`STREX` pairs. These primitives are the foundation on which all higher-level synchronization — semaphores, mutexes, condition variables — is ultimately built.
