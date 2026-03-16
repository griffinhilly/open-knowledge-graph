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

## Explainer

From your study of process states and lifecycles, you know that a process cycles through states — new, ready, running, waiting, terminated — and that multiple processes can be in the ready state simultaneously. **CPU scheduling** is the policy that decides which of those ready processes gets the CPU next, and it is one of the most consequential decisions an operating system makes, because the CPU is typically the most contended resource in the system.

Think of scheduling like a doctor's office with one examination room. Patients (processes) arrive, wait in the lobby (ready queue), and eventually get seen. The key question is: in what order? **First-Come-First-Served** (FCFS) is simplest — patients are seen in arrival order — but a patient needing a quick blood pressure check waits behind a patient getting a full physical. **Shortest-Job-First** (SJF) is provably optimal for minimizing average waiting time — see the quick patients first — but it requires knowing how long each appointment will take, which is rarely known in advance. These tradeoffs between simplicity, optimality, and information requirements define the scheduling problem.

The distinction between **preemptive** and **non-preemptive** scheduling is fundamental. In non-preemptive scheduling, once a process gets the CPU, it runs until it voluntarily yields (by completing or blocking on I/O). In preemptive scheduling, the OS can interrupt a running process and move it back to the ready queue — for example, when a higher-priority process becomes ready or when a time quantum expires. Preemption is essential for interactive systems where responsiveness matters: without it, a single compute-bound process could monopolize the CPU while users wait for their keystrokes to be processed.

The metrics for evaluating schedulers reflect different stakeholders. **CPU utilization** (percentage of time the CPU is busy) matters for system throughput. **Turnaround time** (total time from process submission to completion) matters for batch workloads. **Waiting time** (time spent in the ready queue) and **response time** (time from submission to first output) matter for interactive users. No single algorithm optimizes all metrics simultaneously, which is why real operating systems use sophisticated multi-level feedback queues that adapt their behavior based on observed process characteristics — promoting I/O-bound processes for quick turnaround while ensuring CPU-bound processes still make progress.
