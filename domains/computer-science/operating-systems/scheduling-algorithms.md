---
id: scheduling-algorithms
title: CPU Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
- id: threads-and-concurrency
  type: soft
tags:
- FCFS
- SJF
- round-robin
- priority-scheduling
- multilevel-queue
stage: formal-systems
status: validated
---

# CPU Scheduling Algorithms

## Core Idea
Classic scheduling algorithms each optimize different objectives: First-Come First-Served (FCFS) is simple but causes the convoy effect; Shortest Job First (SJF) minimizes average waiting time but requires knowing future burst lengths; Round Robin (RR) gives each process a fixed time quantum and is fair for interactive systems; Priority Scheduling assigns numeric priorities but risks starvation of low-priority processes, mitigated by aging. Multilevel Feedback Queues combine multiple algorithms into a hierarchy, promoting or demoting processes based on their observed behavior, and represent the approach used by most real operating systems.

## How It's Best Learned
Calculate average waiting time and turnaround time for the same workload under each algorithm. Then argue: for which workload would Round Robin beat SJF?

## Common Misconceptions
- SJF is theoretically optimal for minimizing average waiting time, but it is not practical because burst times must be predicted.
- A small Round Robin quantum isn't always better; too small causes excessive context switching overhead.

## Explainer

From CPU scheduling basics, you know that the scheduler decides which ready process gets the CPU next, and that metrics like waiting time, turnaround time, and response time measure how well it does its job. Scheduling algorithms are the specific strategies for making that decision, and each one represents a different tradeoff between fairness, efficiency, and practicality. No single algorithm is best for all workloads — understanding why requires walking through each one.

**First-Come, First-Served (FCFS)** is the simplest: processes run in arrival order, and each runs to completion (or until it blocks). It's easy to implement — just a FIFO queue — but it suffers from the **convoy effect**. If a long CPU-bound process arrives first, every short process behind it waits. Imagine a grocery store with one cashier and no express lane: one customer with 200 items holds up everyone behind them. Average waiting time can be terrible. **Shortest Job First (SJF)** fixes this by always running the process with the shortest expected CPU burst next. It provably minimizes average waiting time — it's the mathematical optimum. The catch is that you need to know burst lengths in advance, which you don't. Real implementations estimate them using exponential averaging of past bursts, making SJF more of an ideal benchmark than a practical algorithm.

**Round Robin (RR)** takes a fundamentally different approach: every process gets a fixed **time quantum** (say, 10–100 milliseconds), and if it doesn't finish in that window, it's preempted and sent to the back of the ready queue. This guarantees that no process waits more than (n−1) × quantum time before getting a turn, making it excellent for interactive systems where responsiveness matters. The tradeoff is the quantum size. Too large, and RR degenerates into FCFS. Too small, and you spend more time context-switching than computing. A good rule of thumb is that the quantum should be large enough that 80% of CPU bursts complete within a single quantum.

**Priority Scheduling** assigns each process a numeric priority, and the highest-priority process runs first. This is powerful but introduces the risk of **starvation** — low-priority processes may never run if high-priority processes keep arriving. The solution is **aging**: gradually increasing the priority of waiting processes so that even the lowest-priority process eventually runs. Most real operating systems use **Multilevel Feedback Queues (MLFQ)**, which combine several of these ideas. MLFQ maintains multiple queues at different priority levels, each with its own scheduling policy (often RR with different quantum sizes). New processes start in the highest-priority queue. If a process uses its full quantum (suggesting it's CPU-bound), it gets demoted to a lower queue. If it blocks quickly for I/O (suggesting it's interactive), it stays at high priority. This adaptive behavior means the system automatically learns the nature of each process and schedules accordingly — no advance knowledge of burst times required.
