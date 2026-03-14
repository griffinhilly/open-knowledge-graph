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
