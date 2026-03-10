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
status: draft
---

# CPU Scheduling Algorithms

## Core Idea
Classic scheduling algorithms each optimize different objectives: First-Come First-Served (FCFS) is simple but causes the convoy effect; Shortest Job First (SJF) minimizes average waiting time but requires knowing future burst lengths; Round Robin (RR) gives each process a fixed time quantum and is fair for interactive systems; Priority Scheduling assigns numeric priorities but risks starvation of low-priority processes, mitigated by aging. Multilevel Feedback Queues combine multiple algorithms into a hierarchy, promoting or demoting processes based on their observed behavior, and represent the approach used by most real operating systems.

## How It's Best Learned
Calculate average waiting time and turnaround time for the same workload under each algorithm. Then argue: for which workload would Round Robin beat SJF?

## Common Misconceptions
- SJF is theoretically optimal for minimizing average waiting time, but it is not practical because burst times must be predicted.
- A small Round Robin quantum isn't always better; too small causes excessive context switching overhead.
