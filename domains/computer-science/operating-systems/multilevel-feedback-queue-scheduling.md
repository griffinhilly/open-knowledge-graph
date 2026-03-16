---
id: multilevel-feedback-queue-scheduling
title: Multilevel Feedback Queue (MLFQ) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: shortest-job-first-sjf-cpu-scheduling
  type: hard
- id: priority-scheduling-algorithms
  type: soft
builds-toward:
- real-time-scheduling-algorithms
tags:
- scheduling
- algorithms
- cpu
- feedback
stage: formal-systems
status: draft
---

# Multilevel Feedback Queue (MLFQ) Scheduling

## Core Idea
MLFQ uses multiple queues with different priorities and time quanta, allowing processes to move between queues based on behavior. Processes that consume their full time slice move to lower-priority queues, while I/O-bound processes stay in higher-priority queues. This design approximates SJF without requiring prior knowledge of burst times.

## How It's Best Learned
Trace through MLFQ scheduling with varying process behaviors. Experiment with different queue structures and time quantum combinations. Compare against SJF and round-robin to understand trade-offs.

## Common Misconceptions
- Thinking MLFQ requires knowing job length in advance (it adapts dynamically).
- Assuming all processes converge to the lowest queue (depends on behavior).
- Ignoring the risk of starvation in lower-priority queues.

## Explainer

From your study of Shortest Job First scheduling, you know that SJF produces optimal average waiting times — but it has a fatal practical flaw: it requires knowing how long each job will run *before* it runs. In real operating systems, the kernel has no idea whether the process that just became ready will use the CPU for 2 milliseconds or 2 seconds. **Multilevel Feedback Queue (MLFQ)** scheduling solves this by *observing* process behavior and adjusting priority dynamically, effectively learning which processes are short and interactive versus long and CPU-bound.

The structure is a set of queues arranged by priority level. A new process enters the **highest-priority queue** with a small time quantum (say 8ms). If it finishes its CPU burst before the quantum expires — perhaps because it issued an I/O request — it stays at the same high priority. The system infers that this process is interactive or I/O-bound, and interactive processes need fast response times. But if the process uses its entire quantum without voluntarily yielding, the scheduler demotes it to the **next lower queue**, which has a larger time quantum (say 16ms). If it burns through that quantum too, it drops again. Eventually, long-running CPU-bound processes sink to the lowest-priority queue with the largest time quantum, where they run less frequently but get larger chunks of CPU time when they do run.

This design elegantly approximates SJF without requiring advance knowledge. Short jobs finish quickly in the high-priority queue and never get demoted. Long jobs gradually sink to lower queues where they don't interfere with interactive responsiveness. I/O-bound processes (like a text editor waiting for keystrokes) naturally stay at high priority because they frequently yield the CPU before their quantum expires. The scheduler gives preferential treatment to exactly the processes that need it: those with short, bursty CPU usage patterns that would suffer most from delayed scheduling.

The main pitfall is **starvation**: if enough high-priority processes keep arriving, the low-priority queues never get to run. The standard solution is a **priority boost** — periodically (say every second), the scheduler moves all processes back to the highest-priority queue. This gives long-running processes a fresh chance to run and also handles processes whose behavior changes over time (a computation phase might end and the process might become interactive). Another concern is **gaming**: a clever process could issue a trivial I/O request just before its quantum expires, tricking the scheduler into keeping it at high priority while monopolizing the CPU. Modern MLFQ implementations track total CPU time per priority level rather than just per-quantum behavior to prevent this. Nearly every general-purpose OS uses some variant of MLFQ — Linux's CFS and Windows' priority scheduling both incorporate feedback-based priority adjustment, because the principle of "observe and adapt" is fundamentally more robust than requiring predictions about future behavior.
