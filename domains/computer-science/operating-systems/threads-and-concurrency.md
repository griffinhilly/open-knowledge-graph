---
id: threads-and-concurrency
title: Threads and Concurrency
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
- id: process-states-lifecycle
  type: soft
builds-toward:
- synchronization-problem
- scheduling-algorithms
tags:
- threads
- concurrency
- user-threads
- kernel-threads
- multithreading
stage: formal-systems
status: validated
---

# Threads and Concurrency

## Core Idea
A thread is the unit of CPU utilization within a process — a lightweight execution stream that shares the process's address space, open files, and resources while having its own program counter, register set, and stack. Multiple threads within one process can run concurrently, enabling parallelism on multi-core systems without the overhead of separate address spaces. Threads can be implemented in user space (user-level threads, managed by a library) or kernel space (kernel threads, scheduled by the OS directly), with different tradeoffs in scheduling flexibility and blocking behavior.

## How It's Best Learned
Write a multithreaded program using pthreads or Java threads. Observe how threads share heap data, then introduce a race condition intentionally to see non-deterministic output.

## Common Misconceptions
- Threads are not automatically faster; synchronization overhead and contention can make a multithreaded program slower than a single-threaded one.
- User-level threads cannot take advantage of multiple cores unless the OS sees them.

## Questions

```yaml
- question: "A developer rewrites a single-threaded program to use 4 threads on a 4-core machine, expecting a 4x speedup. Instead, the program runs slower than before. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Threads are inherently slower than single-threaded execution on all modern hardware"
    - "Synchronization overhead and lock contention between threads eliminate the expected speedup"
    - "User-level threads cannot run on multiple cores, so only one core executes at a time"
    - "The OS scheduler can only assign one thread per process regardless of core count"
  answer: 1
  explanation: "Threads are not automatically faster — synchronization overhead is real and significant. If threads must frequently acquire and release locks to access shared data, they spend time waiting for each other rather than running in parallel. Lock contention can serialize execution almost as badly as a single-threaded program, while adding the overhead of thread management. Threads provide speedup only when work can be genuinely parallelized with minimal synchronization — identifying those workloads requires careful design."

- question: "Thread A and Thread B both read a shared counter (value: 10), each increment it by 1, and write the result back. After both threads complete, what values are possible for the counter?"
  type: multiple-choice
  options:
    - "Always 12 — the OS ensures threads execute their operations atomically"
    - "Either 11 or 12 — a race condition means one thread's write may overwrite the other's"
    - "Always 11 — the OS merges concurrent writes by taking the last value written"
    - "The program will always crash — concurrent writes to the same variable are undefined behavior"
  answer: 1
  explanation: "This is the classic race condition. If Thread A reads 10, Thread B also reads 10 (before A writes), then A writes 11 and B also writes 11, the counter ends at 11 despite two increments. If the threads happen to interleave perfectly (A reads, increments, writes, then B reads), the result is 12. The actual result depends on scheduling timing, which varies between runs — this is what makes race conditions notoriously difficult to debug. The fix is synchronization (a lock around the read-increment-write sequence)."

- question: "Threads within the same process can communicate by reading and writing shared variables directly, without any OS-mediated mechanism like pipes or sockets."
  type: true-false
  answer: true
  explanation: "This is one of threads' key advantages over processes. Because threads share the process's address space — the same heap, global variables, and data segments — one thread can simply write to a variable and another can read it. No system call, no pipe setup, no serialization required. This makes thread communication extremely fast. The tradeoff is that this same sharing creates race conditions: any shared variable can be read and written simultaneously by multiple threads unless access is synchronized."

- question: "User-level threads can fully utilize multiple CPU cores because the thread library manages their scheduling independently of the OS."
  type: true-false
  answer: false
  explanation: "User-level threads are invisible to the OS kernel — the kernel sees only one process. Because the kernel schedules processes (not user threads) onto cores, it assigns at most one core to the process at any time. Worse, if any user thread makes a blocking system call (like reading from a file), the kernel blocks the entire process, suspending all user threads even though other threads could be running. Kernel threads, by contrast, are scheduled directly by the OS and can run on separate cores simultaneously, enabling true multi-core parallelism."

- question: "Why is creating a new thread much cheaper than creating a new process, and what is the fundamental tradeoff of this efficiency?"
  type: short-answer
  answer: "A new process requires the OS to allocate an entirely separate address space: new page tables, memory maps for code/heap/stack, and independent resource tracking. A new thread requires only its own stack and register set — everything else (address space, open files, heap) is inherited from the parent process with no copying. The tradeoff is that the shared address space removes isolation: all threads can accidentally or maliciously access each other's data, and a bug in one thread can corrupt state used by others. Processes pay a higher creation and context-switch cost in exchange for strong safety boundaries; threads pay a lower cost but require careful synchronization to avoid race conditions and data corruption."
  explanation: "The efficiency gain comes directly from what is not duplicated. The safety cost comes from what is shared. This tradeoff is the central design tension in concurrent programming."
```

## Explainer

From the process concept, you know that a process is a running program with its own address space, open file descriptors, and OS-managed state. Creating a new process is expensive: the OS must allocate a separate address space, copy or share page tables, and set up independent resource tracking. A **thread** is a lighter-weight alternative — it is an independent sequence of execution *within* a process that shares the process's address space, heap, global variables, and open files, but has its own program counter, register set, and stack. Think of a process as an apartment and threads as roommates: they share the kitchen and living room (heap, global data, files) but each has their own bedroom (stack, registers, program counter).

This sharing is both the power and the danger of threads. The power: threads within the same process can communicate by simply reading and writing shared variables — no pipes, sockets, or shared memory setup required. Creating a thread is fast because there is no address space to duplicate. Context switching between threads in the same process is cheaper than switching between processes because the memory mapping (page tables, TLB entries) stays the same. On a multi-core system, threads of the same process can run truly in parallel on different cores, enabling a single program to fully utilize modern hardware.

The danger: because threads share memory, two threads can read and write the same variable simultaneously, producing **race conditions** — bugs where the program's output depends on the unpredictable timing of thread execution. If thread A reads a counter, increments it, and writes it back, but thread B reads the same counter between A's read and write, the increment is lost. These bugs are notoriously difficult to reproduce and debug because they depend on scheduling timing that varies between runs. This is why threads and concurrency lead directly to synchronization — locks, semaphores, and other mechanisms for coordinating access to shared data.

Threads can be implemented at two levels. **Kernel threads** are managed directly by the operating system scheduler, which means the OS can schedule different threads of the same process on different cores and can block one thread without blocking the others. **User-level threads** are managed by a library in user space — the OS sees only one process and schedules it as a unit. User-level threads are faster to create and switch between (no system call needed), but if one user thread makes a blocking system call, the entire process blocks because the kernel does not know about the other threads. The mapping between user threads and kernel threads — many-to-one, one-to-one, or many-to-many — determines the tradeoff between performance and true parallelism. Most modern systems (Linux, Windows, macOS) use one-to-one mapping, where each user thread corresponds to a kernel thread, giving full multi-core parallelism at the cost of slightly heavier thread creation.
