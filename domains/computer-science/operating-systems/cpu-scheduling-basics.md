---
id: cpu-scheduling-basics
title: CPU Scheduling Fundamentals
domain: computer-science
course: operating-systems
prerequisites:
- id: process-states-lifecycle
  type: hard
builds-toward:
- scheduling-algorithms
tags:
- scheduling
- dispatcher
- turnaround-time
- waiting-time
- cpu-burst
stage: formal-systems
status: validated
---

# CPU Scheduling Fundamentals

## Core Idea
CPU scheduling is the task of deciding which ready process runs next on the CPU, with the goal of maximizing utilization and meeting fairness or latency objectives. The scheduler operates at multiple levels: long-term (admission), medium-term (swapping), and short-term (dispatch). Key metrics for evaluating schedulers include CPU utilization, throughput, turnaround time (total time from submission to completion), waiting time, and response time. Processes alternate between CPU bursts (active computation) and I/O bursts (waiting on devices), and this burst pattern heavily influences which scheduling algorithm performs best.

## How It's Best Learned
Simulate scheduling decisions on paper with a Gantt chart using five or six example processes with different burst times. Calculate waiting and turnaround times for each algorithm.

## Common Misconceptions
- A scheduler that maximizes CPU utilization may not minimize user-perceived latency.
- Preemptive and non-preemptive are not algorithm-specific traits; most algorithms have both variants.

## Questions

```yaml
- question: "An operating system uses a scheduling algorithm that achieves 99% CPU utilization — the CPU is almost never idle. Can we conclude that interactive users will experience fast response times?"
  type: multiple-choice
  options:
    - "Yes — high CPU utilization means work is being done efficiently, which directly benefits all users"
    - "No — a compute-bound job could monopolize the CPU, leaving interactive processes waiting even though utilization is high"
    - "Yes — CPU utilization and response time always improve together under any scheduling algorithm"
    - "No — CPU utilization above 95% causes thermal throttling, which degrades response time"
  answer: 1
  explanation: "CPU utilization measures how often the CPU is busy — it says nothing about which processes are getting that CPU time. A single long-running batch job could keep the CPU at 99% utilization while short interactive jobs wait in the ready queue. From the interactive user's perspective, response time (time from request to first output) could be terrible. This is the key insight: different metrics measure different things, and optimizing one can leave others unchanged or worsened. Non-preemptive scheduling in particular can produce high utilization with terrible interactive response time."

- question: "Shortest-Job-First (SJF) scheduling is described as 'optimal.' What exactly is it optimal for, and what is its main practical limitation?"
  type: multiple-choice
  options:
    - "It minimizes average CPU utilization; the limitation is that it requires preemption hardware support"
    - "It minimizes average waiting time; the limitation is that it requires knowing each job's burst time in advance, which is rarely available"
    - "It maximizes throughput for I/O-bound processes; the limitation is that it starves CPU-bound processes indefinitely"
    - "It minimizes response time for all processes; the limitation is that it cannot handle processes that arrive after scheduling begins"
  answer: 1
  explanation: "SJF is provably optimal for minimizing average waiting time — by seeing the shortest jobs first, you reduce the total time other jobs spend waiting behind them. But this requires knowing each process's CPU burst time before it runs, which is not available in practice (the OS doesn't know in advance how long a process will compute before blocking on I/O). Practical implementations estimate burst times from historical behavior. SJF can also cause starvation: if short jobs keep arriving, long jobs may never get scheduled."

- question: "A scheduler that maximizes CPU utilization will necessarily minimize the waiting time experienced by processes in the ready queue."
  type: true-false
  answer: false
  explanation: "CPU utilization and waiting time measure entirely different things and can move in opposite directions. High CPU utilization means the processor is rarely idle — but if a single long job is running, every other process waits in the ready queue the entire time. Waiting time (time spent ready but not running) can be very high while utilization is also high. To minimize waiting time, you need to consider scheduling order and fairness, not just keep the CPU busy. This is why real operating systems balance multiple metrics simultaneously, accepting imperfect utilization in exchange for acceptable waiting and response times."

- question: "In preemptive scheduling, the operating system can interrupt a currently-running process and move it back to the ready queue before it voluntarily yields the CPU."
  type: true-false
  answer: true
  explanation: "This is the defining feature of preemptive scheduling. The OS retains the ability to interrupt a process — typically when a higher-priority process becomes ready or when a time quantum expires — and reassign the CPU to another process. This is essential for interactive systems: without preemption, a compute-bound process could run indefinitely while a user's keypress waits unprocessed. Preemption requires saving the interrupted process's state (context switch) so it can resume correctly later. Non-preemptive scheduling, by contrast, requires a process to voluntarily release the CPU."

- question: "Explain the difference between turnaround time and response time. Why does this distinction matter for different types of computing workloads?"
  type: short-answer
  answer: "Turnaround time is the total elapsed time from when a process is submitted to when it completes. Response time is the time from submission to the first output or first CPU allocation. For batch workloads (e.g., scientific simulations), turnaround time matters — users want the job done fast. For interactive workloads (e.g., a text editor), response time matters — users need immediate feedback to keystrokes even if the overall session takes a long time. A scheduler could achieve good turnaround time while having terrible response time (run each job to completion in order) or vice versa."
  explanation: "This distinction drives real scheduler design decisions. Interactive operating systems (like desktop OSes) prioritize response time by preempting long jobs and giving I/O-bound processes quick CPU access — users notice a 100ms keyboard lag but not a 10% increase in total session time. Batch schedulers on HPC clusters prioritize turnaround time and throughput, sometimes accepting poor response time in exchange for completing more work per unit time. Multi-level feedback queues try to achieve both by dynamically classifying processes based on their observed behavior."
```

## Explainer

From your study of process states and lifecycles, you know that a process cycles through states — new, ready, running, waiting, terminated — and that multiple processes can be in the ready state simultaneously. **CPU scheduling** is the policy that decides which of those ready processes gets the CPU next, and it is one of the most consequential decisions an operating system makes, because the CPU is typically the most contended resource in the system.

Think of scheduling like a doctor's office with one examination room. Patients (processes) arrive, wait in the lobby (ready queue), and eventually get seen. The key question is: in what order? **First-Come-First-Served** (FCFS) is simplest — patients are seen in arrival order — but a patient needing a quick blood pressure check waits behind a patient getting a full physical. **Shortest-Job-First** (SJF) is provably optimal for minimizing average waiting time — see the quick patients first — but it requires knowing how long each appointment will take, which is rarely known in advance. These tradeoffs between simplicity, optimality, and information requirements define the scheduling problem.

The distinction between **preemptive** and **non-preemptive** scheduling is fundamental. In non-preemptive scheduling, once a process gets the CPU, it runs until it voluntarily yields (by completing or blocking on I/O). In preemptive scheduling, the OS can interrupt a running process and move it back to the ready queue — for example, when a higher-priority process becomes ready or when a time quantum expires. Preemption is essential for interactive systems where responsiveness matters: without it, a single compute-bound process could monopolize the CPU while users wait for their keystrokes to be processed.

The metrics for evaluating schedulers reflect different stakeholders. **CPU utilization** (percentage of time the CPU is busy) matters for system throughput. **Turnaround time** (total time from process submission to completion) matters for batch workloads. **Waiting time** (time spent in the ready queue) and **response time** (time from submission to first output) matter for interactive users. No single algorithm optimizes all metrics simultaneously, which is why real operating systems use sophisticated multi-level feedback queues that adapt their behavior based on observed process characteristics — promoting I/O-bound processes for quick turnaround while ensuring CPU-bound processes still make progress.
