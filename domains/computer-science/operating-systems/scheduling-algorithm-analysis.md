---
id: scheduling-algorithm-analysis
title: Scheduling Algorithm Classification and Analysis
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- shortest-job-first-analysis
- priority-scheduling-inversion
tags:
- scheduling
- algorithms
- analysis
stage: formal-systems
status: draft
---

# Scheduling Algorithm Classification and Analysis

## Core Idea
CPU scheduling algorithms are classified as preemptive vs. non-preemptive, priority-based vs. fair, and work-conserving vs. non-work-conserving. Each classification reflects assumptions about workload and optimization goals (latency, throughput, fairness).

## How It's Best Learned
Simulate schedulers on diverse workloads (batch jobs, interactive tasks, I/O-intensive); measure metrics like average wait time, response time, and fairness.

## Common Misconceptions
- Assuming one scheduler is optimal for all workloads.
- Confusing process priority with scheduling priority.
- Missing that preemption incurs context-switch overhead.

## Explainer

From your study of CPU scheduling basics, you know that the scheduler decides which ready process gets the CPU next. But there are many ways to make that decision, and the point of scheduling algorithm analysis is to understand *how* those strategies differ and *when* each one excels or fails. The key is that every scheduling algorithm embodies a tradeoff between competing goals — minimizing wait time, maximizing throughput, ensuring fairness, or keeping response time low — and no single algorithm wins on every metric simultaneously.

The first major classification is **preemptive versus non-preemptive**. A non-preemptive scheduler lets a process run until it voluntarily yields the CPU (by blocking on I/O or terminating). A preemptive scheduler can interrupt a running process — typically when a timer fires or a higher-priority process becomes ready — and force a context switch. Non-preemptive scheduling is simpler and avoids context-switch overhead, but it cannot guarantee responsiveness: a long-running computation monopolizes the CPU while interactive processes starve. Preemptive scheduling is essential for interactive and real-time systems, but each preemption costs time for saving and restoring process state.

The second classification is **priority-based versus fair**. Priority schedulers assign a numeric priority to each process and always run the highest-priority ready process. This is powerful for distinguishing urgent work from background tasks, but it creates the risk of **starvation**: low-priority processes may never run if high-priority ones keep arriving. Aging — gradually boosting the priority of waiting processes — is the standard countermeasure. Fair schedulers like round-robin or proportional-share algorithms aim to give every process an equitable fraction of CPU time. Round-robin rotates through the ready queue with a fixed time quantum; if the quantum is too short, context-switch overhead dominates, and if it is too long, the scheduler degenerates into non-preemptive first-come-first-served.

A third, less obvious classification is **work-conserving versus non-work-conserving**. A work-conserving scheduler never leaves the CPU idle when there is a ready process — it always dispatches something. Most real schedulers are work-conserving, but some real-time or energy-aware schedulers deliberately idle the CPU to batch future work or save power. When analyzing any scheduling algorithm, the procedure is the same: define a workload (a set of processes with arrival times, burst lengths, and priorities), simulate the algorithm's decisions step by step, and compute metrics like **average waiting time**, **average turnaround time**, **throughput** (processes completed per unit time), and **response time** (time from arrival to first execution). Comparing these metrics across algorithms on the same workload reveals each strategy's strengths — and there is always a workload that makes any given algorithm look bad, which is why real operating systems combine multiple strategies into multilevel feedback queues rather than committing to a single approach.
