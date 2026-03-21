---
id: concurrency-and-race-conditions
title: Concurrency and Race Conditions
domain: computer-science
course: operating-systems
prerequisites:
- id: thread-creation-and-lifecycle
  type: hard
builds-toward:
- mutual-exclusion-and-locks
- binary-semaphores-mutexes
tags:
- concurrency
- synchronization
- testing-challenges
stage: formal-systems
status: draft
---

# Concurrency and Race Conditions

## Core Idea
Concurrent execution of multiple threads enables responsiveness and parallelism but introduces subtle bugs. A race condition occurs when multiple threads access shared data concurrently and at least one modifies it, producing non-deterministic results. Race conditions are difficult to detect and reproduce because they depend on scheduling order and timing.

## Common Misconceptions
Race conditions are easily caught by testing (they are timing-dependent and often manifest only under specific workloads or hardware). Modern hardware prevents race conditions (atomic instructions prevent some but not all race conditions).

## Questions

```yaml
- question: "Two threads both execute `counter = counter + 1` on a shared variable initialized to 0. This compiles to three machine instructions: LOAD, ADD, STORE. If both threads execute LOAD before either executes STORE, what is the final value of counter?"
  type: multiple-choice
  options:
    - "2 — because two increment operations were performed"
    - "1 — both threads loaded 0, computed 1, and stored 1, so one increment was silently lost"
    - "0 — concurrent access corrupts the variable and returns it to its initial state"
    - "Undefined — the hardware detects the conflict and throws an exception"
  answer: 1
  explanation: "Both threads read the initial value 0 before either writes back. Each computes 0 + 1 = 1 and stores 1. The second store overwrites the first, and the final result is 1 instead of the expected 2 — one increment was silently lost. Hardware doesn't detect or prevent this; it executes each instruction in isolation. This is the classic data race: two threads accessing shared mutable state with no synchronization, producing a result that depends on scheduling order."

- question: "A developer runs a concurrent program 1,000 times during testing and observes no failures. Which conclusion is best supported?"
  type: multiple-choice
  options:
    - "The program is race-condition-free, since it passed 1,000 independent trials"
    - "The program may have races that appear only under different scheduling, load, or hardware conditions not reproduced by the test environment"
    - "The program may have races, but since they never appeared in testing, they pose no practical risk"
    - "Testing concurrent programs 1,000 times is the standard method for certifying them race-free"
  answer: 1
  explanation: "Race conditions are timing-dependent and may only manifest under specific scheduling interleavings, CPU loads, or hardware configurations that the test environment never produced. Passing 1,000 tests provides evidence that the bug doesn't appear easily, but zero evidence that the race doesn't exist. Production environments differ from test environments in ways that can expose races — different hardware, higher concurrency, different OS scheduler behavior. Formal reasoning about shared-state access patterns, not empirical testing alone, is required to certify race freedom."

- question: "A race condition can only occur when two threads execute exactly the same code simultaneously."
  type: true-false
  answer: false
  explanation: "A race condition requires that two threads access the same shared memory location with at least one write — they don't need to execute the same code. For example, one thread could read a shared variable while another thread writes it; the code paths are entirely different, but the access to shared state causes a race. What matters is the memory location accessed and whether writes are involved, not whether the threads are running identical code."

- question: "Running a concurrent program many times and observing consistent correct results is sufficient evidence to conclude it is free of race conditions."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception about race conditions. Because races depend on precise timing of thread scheduling — which varies with CPU load, OS decisions, and hardware — a race may almost never trigger in a test environment but consistently appear in production. A program can run correctly 99.999% of the time and still have a catastrophic race that surfaces under specific conditions. Testing can reveal the presence of a race but cannot prove its absence. Only reasoning about all possible interleavings of shared-state access can establish correctness."

- question: "Why is it insufficient to protect shared data by checking whether another thread is 'currently using it' before accessing it — why doesn't a simple flag variable solve the race condition problem?"
  type: short-answer
  answer: "Checking and then acting on a shared flag is itself a read-modify-write operation subject to races. If thread A reads the flag (sees 'not in use'), and thread B also reads the flag before A sets it to 'in use,' both threads believe the resource is free and both proceed. The check-then-act sequence is not atomic — there is a window between the check and the subsequent action where another thread can intervene. Mutual exclusion requires atomic operations that cannot be interrupted between the check and the acquisition."
  explanation: "This is the 'TOCTOU' (time-of-check to time-of-use) problem. Any solution that uses a non-atomic read-check-write sequence as its guard is itself a race condition. Proper synchronization primitives like mutexes use atomic hardware instructions (compare-and-swap, test-and-set) that guarantee the entire check-and-acquire happens as a single indivisible operation, closing the window that allows races."
```

## Explainer

From your study of threads, you know that multiple threads within a process share the same address space — they can all read and write the same variables and data structures. This sharing is what makes threads efficient (no need to copy data between address spaces), but it is also the source of one of the most insidious classes of bugs in computing: the **race condition**.

A race condition occurs whenever the correctness of a program depends on the relative timing or interleaving of operations from multiple threads. Consider a simple example: two threads both execute `counter = counter + 1` on a shared variable that starts at zero. You might expect the final value to be 2, but this single line of code is actually three operations at the machine level — load the value from memory, add one, store the result back. If both threads load the value (0) before either stores, both compute 1, and both store 1. The final value is 1 instead of 2. One increment was silently lost. This is a **data race** — the specific case where two threads access the same memory location concurrently with at least one write and no synchronization.

What makes race conditions so dangerous is their **non-determinism**. The exact interleaving of thread operations depends on the OS scheduler, CPU load, cache behavior, and even the temperature of the processor affecting clock speeds. A program with a race condition might pass thousands of tests and run correctly for months, then fail catastrophically under slightly different load conditions in production. You cannot reliably test for race conditions by running the program many times — the bug hides in interleavings that your test environment might never produce. This is why formal reasoning about shared state, rather than empirical testing alone, is essential for concurrent programming.

The solution space falls into two categories. The first is **mutual exclusion**: using locks, semaphores, or monitors to ensure that only one thread executes a **critical section** (the code that accesses shared data) at a time. The second is **avoiding shared mutable state** entirely — using message passing, immutable data structures, or thread-local storage so threads never contend on the same memory. Both approaches have tradeoffs in complexity and performance, and you will explore them in depth as you study synchronization primitives. The key insight for now is that any time two threads can access the same data and at least one can modify it, you must either synchronize access or restructure the code to eliminate the sharing.
