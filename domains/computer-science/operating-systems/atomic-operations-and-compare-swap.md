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
status: validated
---

# Atomic Operations and Compare-and-Swap

## Core Idea
Atomic operations execute indivisibly without interruption, enabling lock-free synchronization primitives. Compare-and-swap (CAS) atomically compares a memory location's value and conditionally updates it in a single operation. Lock-free algorithms using CAS can improve concurrency and reduce context switch overhead but are notoriously difficult to implement and reason about correctly.

## Questions

```yaml
- question: "Thread T1 reads a shared pointer P = A, then gets descheduled. Thread T2 changes P: A → B → A. T1 resumes and executes CAS(P, A, new_value). What happens and why is it a problem?"
  type: multiple-choice
  options:
    - "The CAS fails because P was modified while T1 was descheduled"
    - "The CAS succeeds, but the underlying state may have changed in ways T1 did not account for"
    - "The CAS succeeds and is safe because P currently equals T1's expected value"
    - "The CAS fails because T2 performed two modifications rather than one"
  answer: 1
  explanation: "This is the ABA problem. CAS only checks whether the current value equals the expected value — it has no memory of intermediate states. Even though T1's CAS succeeds (P is currently A, matching the expected value), the underlying data structure may have been reorganized or a memory node freed and reallocated at the same address. T1 proceeds as if nothing changed, potentially corrupting the structure. Solutions include tagged pointers (appending a version counter so A-at-version-1 and A-at-version-2 are distinguishable)."

- question: "A high-frequency trading system uses a shared reference counter incremented and decremented by many threads. Which synchronization approach is most appropriate?"
  type: multiple-choice
  options:
    - "A mutex protecting all increment/decrement operations"
    - "An atomic CAS-based counter, since the critical section is tiny and mutex overhead would dominate"
    - "No synchronization, since increments on separate threads are independent"
    - "A read-write lock, since increments and decrements are symmetric operations"
  answer: 1
  explanation: "For a simple integer counter, the critical section is just a few instructions. Using a mutex causes threads to sleep, wake, and context-switch — overhead that dwarfs the actual work. A CAS loop retries inline: read, compute new value, CAS. If the CAS fails due to concurrent modification, the thread retries immediately without sleeping. For short critical sections with moderate contention, this lock-free approach eliminates scheduling overhead. For longer critical sections or complex multi-step operations, mutexes remain simpler and safer."

- question: "Unlike mutex acquisition, compare-and-swap instructions can be executed from user space without requiring a transition to kernel mode."
  type: true-false
  answer: true
  explanation: "CAS is implemented as a single hardware instruction (e.g., CMPXCHG on x86, LDREX/STREX on ARM) available in user mode. Mutex lock acquisition, by contrast, often requires a system call (futex on Linux) when there is contention, which involves a kernel trap and context-switch overhead. CAS-based lock-free operations run entirely in user space, avoiding this overhead for short operations. This is one reason lock-free data structures can outperform mutex-based ones in high-throughput scenarios."

- question: "Lock-free algorithms using CAS never cause threads to wait, so they are always faster than mutex-based algorithms for the same operation."
  type: true-false
  answer: false
  explanation: "Lock-free means no thread ever blocks indefinitely (a liveness guarantee), but it does not mean threads never waste time. Under high contention, many threads may repeatedly fail their CAS and retry in tight loops — a form of livelock that burns CPU cycles without making progress. A mutex allows contending threads to sleep and yield the CPU, which can be more efficient when contention is sustained. Lock-free code excels for short critical sections with low-to-moderate contention; mutexes can be better when contention is high or critical sections are long."

- question: "Explain why ordinary loads and stores cannot be composed into a correct compare-and-swap, even with careful ordering."
  type: short-answer
  answer: "Between any load (read) and the subsequent store (write), another thread on a different core can modify the same location — and modern CPUs execute threads truly in parallel with no 'between instruction' gap that software can lock out. No software ordering scheme can prevent this race because the hardware executes multiple threads simultaneously. Only a single hardware instruction that atomically tests and conditionally writes — using bus locking or hardware-level exclusive reservation — can prevent any interleaving between the check and the update."
  explanation: "This is why hardware support is essential. x86 provides CMPXCHG with a LOCK prefix that asserts exclusive access to the memory location during the operation. ARM uses load-linked/store-conditional pairs with a hardware reservation mechanism. These are not software tricks — they require explicit hardware mechanisms that signal to other cores to invalidate their cached copies and stall. No software-only protocol operating above the hardware abstraction layer can match this guarantee."
```

## Explainer

From the synchronization problem, you know that concurrent threads sharing memory can produce incorrect results when their operations interleave. The root cause is that ordinary operations like "read a variable, add one, write it back" are not indivisible — another thread can sneak in between the read and the write. **Atomic operations** solve this by making certain operations execute as a single, uninterruptible step from the perspective of all other threads. No thread can ever observe an atomic operation "half-done."

The most important atomic operation is **compare-and-swap (CAS)**. It takes three arguments: a memory address, an expected value, and a new value. In a single atomic step, it checks whether the memory location currently holds the expected value. If it does, CAS replaces it with the new value and reports success. If it does not (because another thread changed it), CAS does nothing and reports failure. The calling thread can then re-read the current value, recompute its desired update, and try again. This "read-compute-CAS-retry" loop is the fundamental pattern of lock-free programming. For example, to atomically increment a counter, a thread reads the current value (say, 5), computes 6, then executes CAS(address, 5, 6). If another thread incremented it to 6 in the meantime, the CAS fails, the thread re-reads 6, computes 7, and retries.

CAS is implemented in hardware — the CPU provides instructions like `CMPXCHG` on x86 or `LDREX/STREX` on ARM that execute atomically with respect to all cores. This hardware support is essential: you cannot build correct atomic operations out of ordinary loads and stores alone because the CPU and memory system can reorder or interleave them in ways that break any software-only protocol. The kernel-mode privilege you studied earlier is relevant here because these hardware instructions are available in user space — unlike many OS features, threads do not need to trap into the kernel to use CAS, which is one reason lock-free code can be faster than mutex-based code for short critical sections.

The appeal of CAS-based lock-free algorithms is that no thread ever blocks: if a CAS fails, the thread simply retries rather than sleeping. This eliminates problems like priority inversion (a high-priority thread waiting for a low-priority lock holder) and reduces context-switch overhead. However, lock-free programming is notoriously difficult. The **ABA problem** is a classic pitfall: a value changes from A to B and back to A between a thread's read and its CAS, so CAS succeeds even though the underlying state changed in ways the thread did not account for. Solutions include tagged pointers (appending a version counter to the value) and hazard pointers for memory reclamation. For most application code, mutexes remain the right choice — CAS-based lock-free structures are reserved for performance-critical infrastructure like concurrent queues, memory allocators, and reference counters where the complexity is justified.
