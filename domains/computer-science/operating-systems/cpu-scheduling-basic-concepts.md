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

## Questions

```yaml
- question: "A batch server runs long scientific simulations that rarely need user interaction. An interactive desktop OS runs many short tasks like text editors and browsers that users expect to feel responsive. Which scheduling design is more appropriate for each?"
  type: multiple-choice
  options:
    - "Both should use preemptive scheduling — modern hardware makes preemption essentially free"
    - "The batch server benefits from non-preemptive scheduling (fewer context switches, better throughput for long jobs); the desktop OS requires preemptive scheduling (no single task can monopolize the CPU)"
    - "The desktop OS benefits from non-preemptive scheduling because users don't want their tasks interrupted mid-execution"
    - "Both should use the same algorithm — fairness requires treating all processes identically regardless of workload"
  answer: 1
  explanation: "Non-preemptive scheduling minimizes context-switch overhead and lets long CPU-bound jobs run to completion, maximizing throughput in batch workloads. Preemptive scheduling is essential for interactive responsiveness: if any single process could run indefinitely without interruption, the desktop would freeze whenever a CPU-bound job ran. The appropriate policy depends entirely on what the system needs to optimize. This illustrates the core insight that no single scheduling algorithm is best — the right choice depends on workload characteristics and which metric matters most."

- question: "In a preemptive scheduling system, a timer interrupt fires every 10 milliseconds. What does this guarantee that a non-preemptive (cooperative) scheduler cannot guarantee?"
  type: multiple-choice
  options:
    - "It guarantees that every process completes within a bounded total time"
    - "It guarantees that no single process can monopolize the CPU for more than 10 milliseconds, ensuring every ready process gets regular access"
    - "It guarantees optimal CPU utilization by eliminating idle time between processes"
    - "It guarantees that every process receives an equal share of CPU time over any given window"
  answer: 1
  explanation: "The timer interrupt is the mechanism that makes preemption work: regardless of what a running process is doing, the OS reclaims the CPU after the quantum expires. A cooperative scheduler has no such guarantee — a misbehaving or CPU-bound process that never voluntarily yields can starve all other processes indefinitely. Preemption doesn't guarantee bounded completion time (A), optimal utilization (C), or strict equal shares (D — that depends on the specific algorithm). But it does guarantee that no process permanently monopolizes the CPU, which is the minimum required for responsive multiprogramming."

- question: "The scheduler is the OS component that decides which process runs next; the dispatcher is the OS component that actually performs the context switch."
  type: true-false
  answer: true
  explanation: "This is the mechanism vs. policy distinction fundamental to OS design. The scheduler implements the policy — examining the ready queue and selecting the next process according to some algorithm (FCFS, round-robin, priority, etc.). The dispatcher implements the mechanism — saving the current process's registers and state, loading the selected process's state, and transferring control to it. These are separate concerns: the same dispatcher can work with many different scheduling policies, and changing the scheduling algorithm doesn't require changing how context switches are performed."

- question: "A scheduling algorithm that maximizes CPU utilization will also minimize average waiting time for processes in the ready queue."
  type: true-false
  answer: false
  explanation: "These metrics can directly conflict. A long CPU-bound job might keep the CPU busy (high utilization) while all shorter processes queue behind it — dramatically increasing average waiting time. This is the 'convoy effect' in FCFS scheduling: one long job monopolizes the CPU and many short jobs wait. Minimizing average waiting time often requires prioritizing short jobs (as in Shortest Job First) at the cost of potentially starving long ones. No scheduling algorithm simultaneously optimizes all metrics, which is why the choice of algorithm depends on what the workload requires."

- question: "Why is no single CPU scheduling algorithm optimal for all workloads, and what does this imply about how real operating systems handle scheduling?"
  type: short-answer
  answer: "Different workloads require optimizing different, often conflicting metrics. Batch systems care most about throughput and CPU utilization. Interactive systems care most about response time. Real-time systems require meeting deadlines. Maximizing throughput may starve short interactive tasks; minimizing response time wastes CPU on context-switch overhead; guaranteeing deadlines requires reserving CPU for specific tasks at the expense of others. Because no algorithm is universally optimal, real operating systems typically provide configurable or adaptive schedulers — often combining multiple policies, such as interactive-class processes on round-robin and batch-class on priority queues, to serve mixed workloads."
  explanation: "The deeper insight is that 'best scheduling' is meaningless without specifying what you're optimizing for. Every algorithm makes a bet about the workload. When those assumptions are violated — when FCFS gets a long job, when round-robin handles real-time tasks — the algorithm's pathologies emerge. Understanding these tradeoffs is the foundation for evaluating specific algorithms and for knowing when to question the scheduler's default behavior."
```

## Explainer

From your understanding of context switching and CPU dispatch, you know that the operating system can stop a running process, save its state, and load a different process onto the CPU. Context switching is the *mechanism* — scheduling is the *policy* that decides which process gets the CPU next. This distinction between mechanism and policy is fundamental in OS design: the dispatcher performs the switch, but the **scheduler** makes the choice.

The need for scheduling arises because there are typically more ready processes than CPUs. At any moment, several processes may be waiting in the **ready queue**, each wanting CPU time. The scheduler examines this queue and selects one process to run, based on whatever policy is in effect. This decision happens at specific moments: when a running process blocks (on I/O, for example), when a process terminates, when a new process arrives, or — in preemptive systems — when a timer interrupt fires. Each of these events is a **scheduling point** where the scheduler must decide whether to continue running the current process or switch to another.

Scheduling policies are evaluated against several metrics that often conflict with each other. **CPU utilization** measures what fraction of time the CPU is doing useful work (not idle). **Throughput** counts how many processes complete per unit time. **Turnaround time** measures the total time from process submission to completion. **Waiting time** measures how long a process sits in the ready queue. **Response time** measures how quickly a process first gets the CPU after becoming ready — critical for interactive systems. No scheduling algorithm can optimize all of these simultaneously, which is why different algorithms exist for different workloads.

The most important design choice is whether the scheduler is **preemptive** or **non-preemptive** (cooperative). A non-preemptive scheduler lets a process run until it voluntarily yields the CPU — by blocking on I/O, finishing, or explicitly calling a yield function. This is simpler but risks one process monopolizing the CPU. A preemptive scheduler can forcibly take the CPU away from a running process (via a timer interrupt), guaranteeing that every process gets regular time slices. Nearly all modern general-purpose operating systems use preemptive scheduling, because interactive responsiveness requires it. But preemption introduces complexity: the interrupted process might be in the middle of updating a shared data structure, so the kernel must handle synchronization carefully.

Understanding these tradeoffs — utilization vs. responsiveness, fairness vs. throughput, simplicity vs. flexibility — is the foundation for studying specific scheduling algorithms like FCFS, Round Robin, and priority scheduling. Each algorithm makes a different bet about which metric matters most, and each reveals different pathologies when its assumptions about the workload are violated.
