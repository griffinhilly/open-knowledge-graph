---
id: cpu-scheduling-basic-concepts
title: 'CPU Scheduling: Basic Concepts'
domain: computer-science
course: operating-systems
prerequisites:
- id: context-switching-and-cpu-dispatch
  type: hard
- id: optimization-problems
  type: soft
builds-toward:
- fcfs-scheduling-algorithm
- round-robin-scheduling
- priority-scheduling-algorithms
tags:
- scheduling
- resource-allocation
- fairness
stage: formal-systems
status: draft
---

# CPU Scheduling: Basic Concepts

## Core Idea
Scheduling is the process of selecting which ready process runs next on the CPU. Scheduling goals include maximizing CPU utilization, minimizing average waiting time, ensuring fairness, and meeting deadlines. Different scheduling policies serve different workload characteristics and system objectives.

## Explainer

From your understanding of context switching and CPU dispatch, you know that the operating system can stop a running process, save its state, and load a different process onto the CPU. Context switching is the *mechanism* — scheduling is the *policy* that decides which process gets the CPU next. This distinction between mechanism and policy is fundamental in OS design: the dispatcher performs the switch, but the **scheduler** makes the choice.

The need for scheduling arises because there are typically more ready processes than CPUs. At any moment, several processes may be waiting in the **ready queue**, each wanting CPU time. The scheduler examines this queue and selects one process to run, based on whatever policy is in effect. This decision happens at specific moments: when a running process blocks (on I/O, for example), when a process terminates, when a new process arrives, or — in preemptive systems — when a timer interrupt fires. Each of these events is a **scheduling point** where the scheduler must decide whether to continue running the current process or switch to another.

Scheduling policies are evaluated against several metrics that often conflict with each other. **CPU utilization** measures what fraction of time the CPU is doing useful work (not idle). **Throughput** counts how many processes complete per unit time. **Turnaround time** measures the total time from process submission to completion. **Waiting time** measures how long a process sits in the ready queue. **Response time** measures how quickly a process first gets the CPU after becoming ready — critical for interactive systems. No scheduling algorithm can optimize all of these simultaneously, which is why different algorithms exist for different workloads.

The most important design choice is whether the scheduler is **preemptive** or **non-preemptive** (cooperative). A non-preemptive scheduler lets a process run until it voluntarily yields the CPU — by blocking on I/O, finishing, or explicitly calling a yield function. This is simpler but risks one process monopolizing the CPU. A preemptive scheduler can forcibly take the CPU away from a running process (via a timer interrupt), guaranteeing that every process gets regular time slices. Nearly all modern general-purpose operating systems use preemptive scheduling, because interactive responsiveness requires it. But preemption introduces complexity: the interrupted process might be in the middle of updating a shared data structure, so the kernel must handle synchronization carefully.

Understanding these tradeoffs — utilization vs. responsiveness, fairness vs. throughput, simplicity vs. flexibility — is the foundation for studying specific scheduling algorithms like FCFS, Round Robin, and priority scheduling. Each algorithm makes a different bet about which metric matters most, and each reveals different pathologies when its assumptions about the workload are violated.
