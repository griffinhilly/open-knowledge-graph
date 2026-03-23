---
id: thread-scheduling-coordination
title: Thread Scheduling and Coordination
domain: computer-science
course: operating-systems
prerequisites:
- id: threads-and-concurrency
  type: hard
- id: process-model-formalization
  type: hard
builds-toward:
- critical-section-problem-formalization
- semaphore-formal-definition
tags:
- threads
- scheduling
- coordination
stage: formal-systems
status: validated
---

# Thread Scheduling and Coordination

## Core Idea
Threads share a process's address space but maintain independent execution stacks and program counters. Independent scheduling of threads requires explicit synchronization mechanisms to coordinate shared data access and prevent race conditions.

## How It's Best Learned
Implement simple concurrent programs with race conditions, observe the failures, then add locks to fix them.

## Common Misconceptions
- Assuming shared memory automatically means data is consistent.
- Thinking compiler optimizations are thread-safe.
- Missing that memory visibility requires explicit synchronization.

## Questions

```yaml
- question: "Two threads both execute `counter += 1`. Thread A loads counter=5 and is preempted. Thread B loads 5, increments to 6, and stores. Thread A resumes and stores 6. The final value is 6, not 7. This is best described as:"
  type: multiple-choice
  options:
    - "A scheduler bug — the OS should never preempt a thread mid-operation"
    - "A hardware bug — CPUs should make read-modify-write atomic by default"
    - "A race condition — the program accesses shared data without synchronization"
    - "A memory allocation bug — both threads should have their own copy of counter"
  answer: 2
  explanation: "The scheduler is behaving correctly — sharing the CPU is exactly its job, and preemption can happen between any two machine instructions. The bug is in the program: `counter += 1` compiles to three steps (load, add, store), and the program provides no guarantee that these steps run atomically. Race conditions are always program bugs, fixed by synchronization (locks, atomic operations), not by demanding different scheduler behavior."

- question: "After adding a mutex lock around `counter += 1`, a team notices that 8 threads incrementing the counter runs far slower than expected. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The mutex is broken — threads are still racing despite the lock"
    - "Mutexes have O(n) acquisition cost where n is the number of waiting threads"
    - "Lock contention — threads spend significant time blocked waiting for the lock rather than doing useful work"
    - "The compiler has eliminated the mutex as dead code during optimization"
  answer: 2
  explanation: "When many threads compete for a single lock protecting a short critical section, most threads spend most of their time blocked, waiting. This is lock contention: the serialization imposed by the lock prevents parallel execution, reducing throughput below even single-threaded performance in extreme cases. The solution is to reduce contention — finer-grained locks, lock-free algorithms, or redesigning to reduce shared state. This is the core tension of concurrent programming: locks prevent races but limit parallelism."

- question: "A race condition can only occur when two threads run simultaneously on multiple CPU cores; single-core systems are immune."
  type: true-false
  answer: false
  explanation: "Even on a single core, the OS scheduler can preempt a thread between any two machine instructions and switch to another thread. Thread A can be halfway through a read-modify-write when thread B runs and modifies the same data. When A resumes, it operates on a stale value. Preemptive scheduling produces race conditions regardless of the number of cores. Multi-core systems do enable truly simultaneous access, but single-core systems are not safe — they just require a context switch to trigger the race."

- question: "Two threads that access shared memory but never write to it simultaneously can safely do so without any synchronization."
  type: true-false
  answer: true
  explanation: "Concurrent reads from shared memory are safe — multiple readers do not interfere with each other because reads do not modify the data. Race conditions require at least one writer. If both threads only read a shared variable, no synchronization is needed. Problems arise when at least one thread writes: a write concurrent with any other access (read or write) creates a data race. The readers-writers problem formalizes this distinction."

- question: "Explain why `counter += 1` is not an atomic operation even though it appears as a single statement in source code. What must a programmer do to ensure this operation is safe when shared between threads?"
  type: short-answer
  answer: "Source-level statements compile to multiple machine instructions. `counter += 1` typically compiles to: (1) load the value of counter into a register, (2) add 1 to the register, (3) store the result back to memory. The scheduler can preempt the thread between any of these steps. To make it safe, the programmer must either use a hardware atomic instruction (like compare-and-swap or atomic increment), or protect the three-step sequence with a mutex so only one thread can execute it at a time."
  explanation: "The gap between source code and machine code is the root of the confusion. High-level languages let programmers reason at a higher abstraction, but the hardware executes sequences of primitive operations with no inherent atomicity guarantee. Synchronization primitives — locks, atomic operations — bridge this gap by providing atomicity guarantees that the source code and hardware do not provide on their own. Understanding this gap is foundational to concurrent programming."
```

## Explainer

You know from studying threads that multiple threads within a process share the same address space — the same heap, the same global variables, the same code. And from the process model, you know that each execution context has its own program counter and stack. When the OS scheduler decides to run a different thread, it performs a **context switch** that saves one thread's registers and restores another's. The critical insight is that these switches can happen at any point — between any two machine instructions — and this unpredictability is what makes concurrent programming fundamentally different from sequential programming.

Consider a simple example: two threads both increment a shared counter. The operation `counter += 1` looks atomic in source code, but at the machine level it decomposes into three steps: load the value from memory into a register, add one, and store the result back. If thread A loads the value (say, 5), then gets preempted before storing, thread B loads the same value 5, increments to 6, and stores it. When thread A resumes, it stores its result — also 6. Two increments happened, but the counter only went up by one. This is a **race condition**: the result depends on the unpredictable timing of thread scheduling.

Race conditions are not bugs in the scheduler — they are bugs in the program. The scheduler is doing exactly what it should: sharing the CPU among threads. The problem is that the program accesses shared data without **synchronization**. The simplest synchronization primitive is a **lock** (or mutex): a thread acquires the lock before accessing shared data and releases it afterward. While the lock is held, any other thread that tries to acquire it will block until the first thread releases it. This guarantees that the load-increment-store sequence completes without interruption, making the operation effectively atomic from the perspective of other threads.

But synchronization introduces its own challenges. Locks create **contention** — threads waiting for locks are doing no useful work, reducing parallelism. Using too few locks risks race conditions; using too many risks **deadlock**, where two threads each hold a lock the other needs. Beyond locks, threads need ways to coordinate their execution order — for example, a producer thread must signal a consumer thread that data is ready. These coordination patterns lead to higher-level primitives like **condition variables** and **semaphores**, which you will study next. The fundamental lesson here is that shared memory is not free communication — it is a shared resource that requires disciplined access protocols, just like any other shared resource in an operating system.
