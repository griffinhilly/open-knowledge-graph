---
id: fcfs-scheduling-algorithm
title: First-Come-First-Served (FCFS) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- round-robin-scheduling
- priority-scheduling-algorithms
tags:
- scheduling-algorithms
- non-preemptive
- fairness
stage: formal-systems
status: validated
---

# First-Come-First-Served (FCFS) Scheduling

## Core Idea
First-Come-First-Served is the simplest scheduling algorithm: processes run in the order they arrive until completion. It is non-preemptive, fair, and easy to implement. However, short jobs can suffer long waits if a long job arrives first, causing the convoy effect and poor average waiting time.

## Common Misconceptions
FCFS is optimal (it is not; convoy effect harms responsiveness). All non-preemptive algorithms are equally bad (FCFS often outperforms preemptive scheduling for CPU-bound workloads).

## Questions

```yaml
- question: "Three processes arrive simultaneously. Process C requires 100ms of CPU time; processes A and B each require 1ms. Under FCFS with arrival order C → A → B, what is the average waiting time?"
  type: multiple-choice
  options:
    - "0ms — since all three arrive simultaneously, FCFS distributes wait time equally"
    - "34ms — FCFS computes waiting time as total_time / number_of_processes"
    - "Approximately 67ms — C waits 0ms, A waits 100ms, B waits 101ms; average = 201/3 ≈ 67ms"
    - "1ms — short processes dominate the average because there are more of them"
  answer: 2
  explanation: "C runs first (arrives first), so A must wait the entire 100ms for C to finish, and B must wait 100ms + 1ms for both C and A. Average = (0 + 100 + 101) / 3 ≈ 67ms. If the arrival order were A → B → C, the average would be (0 + 1 + 2) / 3 ≈ 1ms. This dramatic difference illustrates the convoy effect: the average waiting time under FCFS depends heavily on arrival order, not just on job characteristics."

- question: "A student argues that FCFS scheduling is bad because it causes starvation — some processes never get the CPU. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — long processes can keep getting scheduled repeatedly, permanently delaying short ones"
    - "Yes — high-priority processes always preempt lower-priority ones, leaving some processes stuck indefinitely"
    - "No — FCFS is non-preemptive and runs each process to completion in arrival order; every process in the queue eventually reaches the front"
    - "No — FCFS uses time slicing, so all processes share the CPU fairly and none starve"
  answer: 2
  explanation: "Starvation occurs in algorithms where some processes can be indefinitely bypassed — for example, priority scheduling where a constant stream of high-priority arrivals prevents low-priority processes from ever running. FCFS has no such mechanism: it is purely order-based and non-preemptive. Once a process joins the queue, it moves steadily toward the front as processes ahead of it complete. No process can cut in line. FCFS's weakness is poor average waiting time (the convoy effect), not starvation."

- question: "In FCFS scheduling, if three short I/O-bound processes arrive just after a long CPU-bound process starts, all three must wait the entire duration of the long process before receiving any CPU time."
  type: true-false
  answer: true
  explanation: "This is the convoy effect in action. Because FCFS is non-preemptive, the running process keeps the CPU until it finishes voluntarily or blocks. The three short processes join the ready queue behind the long one and have no mechanism to preempt it — they must wait regardless of how brief their own CPU needs are. If the long process takes 500ms and each short process needs only 2ms, all three wait at least 500ms before their turn arrives."

- question: "FCFS scheduling causes starvation because processes that arrive later must always wait longer, and a process can wait indefinitely if the queue is always non-empty."
  type: true-false
  answer: false
  explanation: "Waiting longer is not the same as starvation. Starvation means a process is indefinitely blocked from running — it never completes. In FCFS, every process that enters the queue will eventually reach the front, because processes ahead of it will complete (they are never preempted back into the queue after joining). A newly arriving process always joins behind existing ones, but existing ones always move forward. As long as the queue drains, every process eventually runs. Poor waiting time ≠ starvation."

- question: "What is the convoy effect in FCFS scheduling, and why does it harm I/O device utilization?"
  type: short-answer
  answer: "The convoy effect occurs when short I/O-bound processes queue behind a long CPU-bound process. Because FCFS is non-preemptive, the short processes cannot run until the long one finishes. During this entire period, the I/O devices those short processes would use sit idle — the CPU is busy but I/O subsystems are starved of work. When the short processes finally get the CPU, they complete their small bursts quickly and issue I/O requests, but the opportunity for concurrent CPU+I/O overlap during the long process's run has been lost. The result is reduced overall system throughput even though the CPU appears busy."
  explanation: "The deeper point is that modern systems achieve throughput through parallelism: while the CPU executes one process, another should be doing I/O. FCFS destroys this overlap by forcing I/O-bound processes to idle behind a long CPU-bound one. Algorithms like Shortest Job First or Round Robin mitigate this by allowing shorter or time-sliced jobs to interleave with long ones, keeping I/O devices active."
```

## Explainer

From your study of CPU scheduling basics, you understand that the scheduler decides which ready process gets the CPU next, and that different algorithms optimize for different metrics (throughput, waiting time, response time). First-Come-First-Served is the most intuitive algorithm: processes are served in the exact order they enter the ready queue, and once a process starts running, it runs to completion without interruption. It is the scheduling equivalent of a single checkout line at a grocery store — whoever arrives first gets served first, regardless of how many items they have.

FCFS is implemented with a simple **FIFO queue**. When a process enters the ready state, it joins the back of the queue. The scheduler always picks the process at the front. Because FCFS is **non-preemptive**, a running process keeps the CPU until it either finishes or voluntarily blocks (for I/O, for example). There is no timer interrupt pulling the CPU away. This makes FCFS trivially simple to implement — no priority comparisons, no preemption logic, no time quantum to tune — and it is perfectly fair in the sense that no process can cut in line.

The critical weakness of FCFS is the **convoy effect**. Imagine a long CPU-bound process (say, a 100ms computation) arrives first, followed by ten short I/O-bound processes (each needing 1ms of CPU time). All ten short processes must wait behind the long one, even though they could each finish almost instantly. The average waiting time balloons. If the short processes arrived first, the average waiting time would be tiny. This order-dependence makes FCFS highly sensitive to arrival patterns and produces poor average waiting time compared to algorithms like Shortest Job First. The convoy effect also hurts I/O utilization: while short I/O-bound processes wait behind a long CPU-bound process, I/O devices sit idle.

Despite its weaknesses, FCFS is not useless. It serves as a **baseline** for evaluating other algorithms — if a more complex algorithm does not beat FCFS on your workload, the complexity is not justified. FCFS also works well for batch processing systems where all jobs are similar in length and fairness (no starvation) is more important than minimizing average wait. It is also commonly used as a tiebreaker within other algorithms: when two processes have the same priority or burst time, FCFS order resolves the tie. Understanding FCFS thoroughly prepares you for round-robin scheduling (which adds preemption via time slices) and priority scheduling (which replaces arrival order with priority values).
