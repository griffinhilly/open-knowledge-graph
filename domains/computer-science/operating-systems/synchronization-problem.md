---
id: synchronization-problem
title: The Critical Section Problem and Race Conditions
domain: computer-science
course: operating-systems
prerequisites:
- id: threads-and-concurrency
  type: hard
- id: inter-process-communication
  type: soft
builds-toward:
- mutex-and-locks
- semaphores
tags:
- race-condition
- critical-section
- mutual-exclusion
- atomicity
stage: formal-systems
status: validated
---

# The Critical Section Problem and Race Conditions

## Core Idea
A race condition occurs when two or more concurrent threads access shared data and the final result depends on the unpredictable interleaving of their operations. The critical section is the code segment where shared data is accessed; correct concurrent programs must ensure that only one thread executes its critical section at a time (mutual exclusion), that waiting threads eventually enter their critical section (progress and bounded waiting), and that no assumptions are made about CPU speed or scheduling. These three requirements — mutual exclusion, progress, bounded waiting — define the Critical Section Problem.

## How It's Best Learned
Reproduce a race condition: have two threads increment a shared counter 1,000,000 times without synchronization and observe the incorrect final value. Then explain why the assembly-level read-modify-write sequence is not atomic.

## Common Misconceptions
- Race conditions are not always obvious; they may appear intermittently depending on timing.
- Declaring a variable 'volatile' in C/C++ does not fix race conditions; it only prevents compiler optimization of reads.

## Questions

```yaml
- question: "Two threads each increment a shared counter 1,000,000 times starting from 0. After both threads finish, the final value is 1,756,432 instead of 2,000,000. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The CPU made arithmetic errors on some additions"
    - "A race condition occurred: the load-modify-store sequence is not atomic, so some increments from one thread overwrote increments from the other"
    - "The threads ran sequentially, so only one completed its full million iterations"
    - "Integer overflow caused some counts to wrap around"
  answer: 1
  explanation: "The operation `counter++` compiles to three hardware steps: load the current value, add 1, store the result. If Thread A loads 5, then Thread B also loads 5 before A stores its result, both store 6 — losing one increment. With millions of iterations, these lost updates accumulate to an unpredictable deficit. This is the classic race condition: a result that depends on the interleaving of non-atomic operations."

- question: "A C++ programmer declares a shared counter as volatile to fix a race condition between two threads incrementing it. Will this solve the problem?"
  type: multiple-choice
  options:
    - "Yes — volatile forces all reads and writes to go directly to memory, preventing stale values"
    - "Yes — volatile makes operations on the variable atomic"
    - "No — volatile only prevents the compiler from caching the variable in a register; it does not make the load-modify-store sequence atomic"
    - "No — volatile makes the problem worse by disabling all compiler optimizations"
  answer: 2
  explanation: "volatile tells the compiler not to cache the variable in a register and to re-read it from memory on every access. It does NOT make compound operations like `counter++` atomic — the three-step load/modify/store sequence remains interruptible. A thread switch can still occur between the load and the store, allowing another thread to overwrite the value. Proper fixes use atomic types, mutexes, or hardware-supported atomic instructions."

- question: "A correct solution to the Critical Section Problem must guarantee mutual exclusion, progress, and bounded waiting — satisfying just two of the three is insufficient."
  type: true-false
  answer: true
  explanation: "All three requirements are necessary. Mutual exclusion prevents two threads from being in the critical section simultaneously. Progress ensures the system doesn't deadlock when threads want to enter. Bounded waiting ensures no thread starves indefinitely. A solution providing mutual exclusion but allowing starvation (violating bounded waiting) is incorrect; so is one preventing deadlock but occasionally allowing simultaneous access (violating mutual exclusion)."

- question: "Race conditions are easy to detect in testing because they always produce a clearly wrong result or cause the program to crash."
  type: true-false
  answer: false
  explanation: "Race conditions are notoriously difficult to detect precisely because they manifest intermittently. The outcome depends on the timing of thread interleaving, which varies with CPU load, scheduling decisions, and other environmental factors. A program with a race condition may run correctly thousands of times before the interleaving that exposes the bug occurs — and may never reproduce the bug in a controlled testing environment, even though it fails in production under load."

- question: "Why does declaring a variable as volatile in C/C++ not fix a race condition on a shared counter?"
  type: short-answer
  answer: "volatile prevents the compiler from caching a variable in a register, but it does not make operations on the variable atomic. The increment `counter++` still compiles to three separate hardware steps (load, add, store), and a thread switch between any two steps allows another thread to overwrite the result."
  explanation: "The root cause of the race condition is that counter++ is not a single indivisible operation at the hardware level — it is read-modify-write. volatile only controls compiler behavior (preventing register caching), not the hardware's ability to interleave these steps across threads. Fixing a race condition requires atomicity, which comes from hardware atomic instructions (like compare-and-swap), mutex locks, or std::atomic in C++."
```

## Explainer

From your study of threads and concurrency, you know that multiple threads can execute simultaneously and share the same memory space. This sharing is what makes threads powerful — but it also introduces a fundamental problem. When two threads read and write the same variable without coordination, the result depends on the exact timing of their operations. This unpredictable dependence on timing is called a **race condition**, and it is the central problem that all synchronization mechanisms exist to solve.

Consider a simple example: two threads each incrementing a shared counter by 1. The operation `counter = counter + 1` looks atomic in source code, but at the hardware level it is three steps — load the value from memory into a register, add 1, store the result back. If Thread A loads the value 5, then Thread B also loads 5 before A stores its result, both threads compute 6 and store 6. The counter should be 7 but ends up as 6. Run this millions of times and the final value will be wrong by an unpredictable amount, different on every run. This is why race conditions are so dangerous: programs that appear correct can fail intermittently and unreproducibly.

The code segment where a thread accesses shared data is called its **critical section**. The **Critical Section Problem** asks: how do we ensure correctness when multiple threads have critical sections that access the same data? The solution must satisfy three properties. **Mutual exclusion** requires that when one thread is in its critical section, no other thread can be in its critical section for the same data. **Progress** requires that if no thread is in the critical section and some threads want to enter, the selection of which thread enters next cannot be postponed indefinitely — the system must not deadlock. **Bounded waiting** requires that after a thread requests entry, there is a limit on how many times other threads can enter before it — no thread should starve.

These three requirements are precise and non-negotiable. A solution that provides mutual exclusion but allows starvation is incorrect. A solution that prevents deadlock but occasionally lets two threads into the critical section simultaneously is incorrect. Simple software-only approaches like Peterson's algorithm satisfy all three requirements but rely on assumptions about memory ordering that modern processors violate. This is why practical systems use hardware-supported atomic instructions (test-and-set, compare-and-swap) as building blocks for higher-level synchronization primitives like mutexes and semaphores, which you will study next.
