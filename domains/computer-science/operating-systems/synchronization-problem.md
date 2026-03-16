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

## Explainer

From your study of threads and concurrency, you know that multiple threads can execute simultaneously and share the same memory space. This sharing is what makes threads powerful — but it also introduces a fundamental problem. When two threads read and write the same variable without coordination, the result depends on the exact timing of their operations. This unpredictable dependence on timing is called a **race condition**, and it is the central problem that all synchronization mechanisms exist to solve.

Consider a simple example: two threads each incrementing a shared counter by 1. The operation `counter = counter + 1` looks atomic in source code, but at the hardware level it is three steps — load the value from memory into a register, add 1, store the result back. If Thread A loads the value 5, then Thread B also loads 5 before A stores its result, both threads compute 6 and store 6. The counter should be 7 but ends up as 6. Run this millions of times and the final value will be wrong by an unpredictable amount, different on every run. This is why race conditions are so dangerous: programs that appear correct can fail intermittently and unreproducibly.

The code segment where a thread accesses shared data is called its **critical section**. The **Critical Section Problem** asks: how do we ensure correctness when multiple threads have critical sections that access the same data? The solution must satisfy three properties. **Mutual exclusion** requires that when one thread is in its critical section, no other thread can be in its critical section for the same data. **Progress** requires that if no thread is in the critical section and some threads want to enter, the selection of which thread enters next cannot be postponed indefinitely — the system must not deadlock. **Bounded waiting** requires that after a thread requests entry, there is a limit on how many times other threads can enter before it — no thread should starve.

These three requirements are precise and non-negotiable. A solution that provides mutual exclusion but allows starvation is incorrect. A solution that prevents deadlock but occasionally lets two threads into the critical section simultaneously is incorrect. Simple software-only approaches like Peterson's algorithm satisfy all three requirements but rely on assumptions about memory ordering that modern processors violate. This is why practical systems use hardware-supported atomic instructions (test-and-set, compare-and-swap) as building blocks for higher-level synchronization primitives like mutexes and semaphores, which you will study next.
