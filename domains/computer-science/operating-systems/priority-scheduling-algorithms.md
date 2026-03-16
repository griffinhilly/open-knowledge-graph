---
id: priority-scheduling-algorithms
title: Priority Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
tags:
- scheduling-algorithms
- priority-based
- starvation-risk
stage: formal-systems
status: draft
---

# Priority Scheduling Algorithms

## Core Idea
Priority scheduling associates a priority with each process and runs the highest-priority process. Preemptive variants interrupt lower-priority processes when higher-priority ones arrive. However, priority scheduling can starve low-priority processes and requires careful priority assignment and aging techniques to prevent pathological behavior.

## Common Misconceptions
Higher priority always means faster execution (depends on competing processes and workload). Static priorities are always better (dynamic/adaptive priorities often prevent starvation).

## Explainer

From CPU scheduling basics, you understand that the scheduler chooses which ready process runs next and that different algorithms optimize for different goals. Priority scheduling assigns each process a numerical **priority value** and always runs the highest-priority ready process. Unlike FCFS, which uses arrival order, or Shortest Job First, which uses burst time, priority scheduling uses an externally assigned importance ranking — the OS or the user decides which processes matter most. This makes it the natural choice for systems where some tasks are genuinely more urgent than others: a real-time audio driver should preempt a background file indexer, not wait behind it.

Priority scheduling comes in two flavors. In the **non-preemptive** variant, once a process starts running, it keeps the CPU until it finishes or blocks, even if a higher-priority process arrives in the meantime. In the **preemptive** variant, a newly arrived or newly unblocked process with higher priority immediately interrupts the currently running process. Preemptive priority scheduling is more responsive — a high-priority task gets the CPU as soon as it needs it — but requires more context switches. Most real operating systems use preemptive priority scheduling because responsiveness matters: when you move your mouse, the interrupt handler and input processing should preempt your background compilation, not wait for it to finish.

The critical problem with priority scheduling is **starvation**: a low-priority process may never run if higher-priority processes keep arriving. Imagine a system where interactive tasks (high priority) constantly arrive — a batch job sitting at low priority could wait hours or even indefinitely. The standard solution is **aging**: the OS gradually increases the priority of processes that have been waiting a long time. After enough time in the ready queue, even the lowest-priority process eventually reaches a priority high enough to run. Aging ensures that priority scheduling has a bounded worst-case waiting time rather than an unbounded one.

In practice, priorities can be **static** (assigned once, fixed for the process lifetime) or **dynamic** (adjusted by the OS based on behavior). Many systems use dynamic priorities to balance responsiveness and throughput: a process that has been I/O-bound (frequently blocking on I/O) gets a priority boost because it is likely to use only a small burst of CPU time before blocking again, keeping I/O devices busy. A process that has been CPU-bound gets its priority reduced to prevent it from monopolizing the CPU. Linux's Completely Fair Scheduler (CFS) and Windows' multilevel feedback queue both incorporate priority with dynamic adjustment. Understanding pure priority scheduling gives you the building block for these more sophisticated multilevel schemes, where processes move between priority bands based on their observed behavior.
