---
id: atomic-operations-and-compare-swap
title: Atomic Operations and Compare-and-Swap
domain: computer-science
course: operating-systems
prerequisites:
- id: synchronization-problem
  type: hard
- id: kernel-mode-and-privilege-levels
  type: soft
builds-toward:
- spinlocks-and-busy-waiting
tags:
- synchronization
- atomic
- lock-free
stage: formal-systems
status: draft
---

# Atomic Operations and Compare-and-Swap

## Core Idea
Atomic operations execute indivisibly without interruption, enabling lock-free synchronization primitives. Compare-and-swap (CAS) atomically compares a memory location's value and conditionally updates it in a single operation. Lock-free algorithms using CAS can improve concurrency and reduce context switch overhead but are notoriously difficult to implement and reason about correctly.

## Explainer

From the synchronization problem, you know that concurrent threads sharing memory can produce incorrect results when their operations interleave. The root cause is that ordinary operations like "read a variable, add one, write it back" are not indivisible — another thread can sneak in between the read and the write. **Atomic operations** solve this by making certain operations execute as a single, uninterruptible step from the perspective of all other threads. No thread can ever observe an atomic operation "half-done."

The most important atomic operation is **compare-and-swap (CAS)**. It takes three arguments: a memory address, an expected value, and a new value. In a single atomic step, it checks whether the memory location currently holds the expected value. If it does, CAS replaces it with the new value and reports success. If it does not (because another thread changed it), CAS does nothing and reports failure. The calling thread can then re-read the current value, recompute its desired update, and try again. This "read-compute-CAS-retry" loop is the fundamental pattern of lock-free programming. For example, to atomically increment a counter, a thread reads the current value (say, 5), computes 6, then executes CAS(address, 5, 6). If another thread incremented it to 6 in the meantime, the CAS fails, the thread re-reads 6, computes 7, and retries.

CAS is implemented in hardware — the CPU provides instructions like `CMPXCHG` on x86 or `LDREX/STREX` on ARM that execute atomically with respect to all cores. This hardware support is essential: you cannot build correct atomic operations out of ordinary loads and stores alone because the CPU and memory system can reorder or interleave them in ways that break any software-only protocol. The kernel-mode privilege you studied earlier is relevant here because these hardware instructions are available in user space — unlike many OS features, threads do not need to trap into the kernel to use CAS, which is one reason lock-free code can be faster than mutex-based code for short critical sections.

The appeal of CAS-based lock-free algorithms is that no thread ever blocks: if a CAS fails, the thread simply retries rather than sleeping. This eliminates problems like priority inversion (a high-priority thread waiting for a low-priority lock holder) and reduces context-switch overhead. However, lock-free programming is notoriously difficult. The **ABA problem** is a classic pitfall: a value changes from A to B and back to A between a thread's read and its CAS, so CAS succeeds even though the underlying state changed in ways the thread did not account for. Solutions include tagged pointers (appending a version counter to the value) and hazard pointers for memory reclamation. For most application code, mutexes remain the right choice — CAS-based lock-free structures are reserved for performance-critical infrastructure like concurrent queues, memory allocators, and reference counters where the complexity is justified.
