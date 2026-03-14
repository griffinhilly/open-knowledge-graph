---
id: round-robin-scheduling
title: Round-Robin (RR) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
builds-toward:
- priority-scheduling-algorithms
tags:
- scheduling-algorithms
- preemptive
- time-sharing
stage: formal-systems
status: draft
---

# Round-Robin (RR) Scheduling

## Core Idea
Round-Robin scheduling allocates each process a fixed time quantum, then moves it to the back of the ready queue. It is preemptive, providing better responsiveness and interactivity than FCFS. Performance depends heavily on quantum size: too small causes excessive context switching; too large approaches FCFS behavior.

## How It's Best Learned
Trace through RR scheduling with different time quanta to observe context switches and measure turnaround time and response time changes.
