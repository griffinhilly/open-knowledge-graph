---
id: fcfs-scheduling-algorithm
title: First-Come-First-Served (FCFS) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
builds-toward:
- round-robin-scheduling
- priority-scheduling-algorithms
tags:
- scheduling-algorithms
- non-preemptive
- fairness
stage: formal-systems
status: draft
---

# First-Come-First-Served (FCFS) Scheduling

## Core Idea
First-Come-First-Served is the simplest scheduling algorithm: processes run in the order they arrive until completion. It is non-preemptive, fair, and easy to implement. However, short jobs can suffer long waits if a long job arrives first, causing the convoy effect and poor average waiting time.

## Common Misconceptions
FCFS is optimal (it is not; convoy effect harms responsiveness). All non-preemptive algorithms are equally bad (FCFS often outperforms preemptive scheduling for CPU-bound workloads).

## Explainer

From your study of CPU scheduling basics, you understand that the scheduler decides which ready process gets the CPU next, and that different algorithms optimize for different metrics (throughput, waiting time, response time). First-Come-First-Served is the most intuitive algorithm: processes are served in the exact order they enter the ready queue, and once a process starts running, it runs to completion without interruption. It is the scheduling equivalent of a single checkout line at a grocery store — whoever arrives first gets served first, regardless of how many items they have.

FCFS is implemented with a simple **FIFO queue**. When a process enters the ready state, it joins the back of the queue. The scheduler always picks the process at the front. Because FCFS is **non-preemptive**, a running process keeps the CPU until it either finishes or voluntarily blocks (for I/O, for example). There is no timer interrupt pulling the CPU away. This makes FCFS trivially simple to implement — no priority comparisons, no preemption logic, no time quantum to tune — and it is perfectly fair in the sense that no process can cut in line.

The critical weakness of FCFS is the **convoy effect**. Imagine a long CPU-bound process (say, a 100ms computation) arrives first, followed by ten short I/O-bound processes (each needing 1ms of CPU time). All ten short processes must wait behind the long one, even though they could each finish almost instantly. The average waiting time balloons. If the short processes arrived first, the average waiting time would be tiny. This order-dependence makes FCFS highly sensitive to arrival patterns and produces poor average waiting time compared to algorithms like Shortest Job First. The convoy effect also hurts I/O utilization: while short I/O-bound processes wait behind a long CPU-bound process, I/O devices sit idle.

Despite its weaknesses, FCFS is not useless. It serves as a **baseline** for evaluating other algorithms — if a more complex algorithm does not beat FCFS on your workload, the complexity is not justified. FCFS also works well for batch processing systems where all jobs are similar in length and fairness (no starvation) is more important than minimizing average wait. It is also commonly used as a tiebreaker within other algorithms: when two processes have the same priority or burst time, FCFS order resolves the tie. Understanding FCFS thoroughly prepares you for round-robin scheduling (which adds preemption via time slices) and priority scheduling (which replaces arrival order with priority values).
