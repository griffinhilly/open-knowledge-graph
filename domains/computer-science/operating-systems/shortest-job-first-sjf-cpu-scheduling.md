---
id: shortest-job-first-sjf-cpu-scheduling
title: Shortest Job First (SJF) CPU Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- multilevel-feedback-queue-scheduling
- scheduling-fairness-and-starvation
tags:
- scheduling
- algorithms
- cpu
stage: formal-systems
status: draft
---

# Shortest Job First (SJF) CPU Scheduling

## Core Idea
SJF scheduling selects the process with the shortest expected burst time to minimize average waiting time. This algorithm is provably optimal for non-preemptive scheduling but requires accurate knowledge of future burst times, which is impractical in real systems. Preemptive SJF (Shortest Remaining Time First) can outperform non-preemptive SJF but adds complexity.

## How It's Best Learned
Study the algorithm with concrete examples showing scheduling timelines. Compare average waiting times against FCFS and round-robin. Implement a simple SJF simulator to see how different burst time predictions affect scheduling.

## Common Misconceptions
- Assuming SJF is always optimal in practice (it requires future knowledge).
- Confusing preemptive and non-preemptive SJF behavior.
- Believing SJF is fair to all processes (short jobs get priority).

## Explainer

From CPU scheduling basics, you know the OS must choose which ready process gets the CPU next, and that different policies produce different average wait times. **Shortest Job First (SJF)** takes a greedy approach: always run the process with the shortest expected CPU burst next. The intuition is the same as choosing the fastest checkout line at a grocery store — letting the person with one item go first minimizes total waiting for everyone behind them.

To see why SJF is optimal for minimizing average waiting time, consider a simple example. Three processes arrive simultaneously with burst times of 6, 8, and 2 milliseconds. Under FCFS (in arrival order), waiting times are 0, 6, and 14 — average 6.67ms. Under SJF, the order is 2, 6, 8, giving waiting times of 0, 2, and 8 — average 3.33ms. SJF always wins because short jobs finish quickly and stop contributing to everyone else's wait. This can be proven formally: any schedule that does not run the shortest remaining job can be improved by swapping it earlier, which always reduces or maintains total waiting time.

The catch is that SJF requires knowing how long each process will run before it runs — and the OS cannot predict the future. In practice, systems **estimate** burst times using historical data: if a process's last three CPU bursts were 5ms, 6ms, and 4ms, the next is likely around 5ms. Exponential averaging is the classic technique, where recent bursts count more than older ones. These estimates are imperfect, but they make SJF approximately usable.

**Preemptive SJF**, also called **Shortest Remaining Time First (SRTF)**, goes further: if a new process arrives with a shorter burst than the time remaining on the currently running process, the OS preempts the running process immediately. This achieves even lower average waiting time but adds context-switch overhead and introduces a serious fairness problem — **starvation**. A long-running process can be perpetually pushed aside as short jobs keep arriving. This is the fundamental tradeoff: SJF is optimal for throughput and wait times but fundamentally unfair to long jobs, which is why real schedulers rarely use pure SJF and instead incorporate aging mechanisms or multi-level feedback queues to balance efficiency with fairness.
