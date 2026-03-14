---
id: fcfs-scheduling-algorithm
title: First-Come-First-Served (FCFS) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
builds-toward:
- round-robin-scheduling
- priority-scheduling-algorithms
tags:
- scheduling-algorithms
- non-preemptive
- fairness
stage: formal-systems
status: draft
---

# First-Come-First-Served (FCFS) Scheduling

## Core Idea
First-Come-First-Served is the simplest scheduling algorithm: processes run in the order they arrive until completion. It is non-preemptive, fair, and easy to implement. However, short jobs can suffer long waits if a long job arrives first, causing the convoy effect and poor average waiting time.

## Common Misconceptions
FCFS is optimal (it is not; convoy effect harms responsiveness). All non-preemptive algorithms are equally bad (FCFS often outperforms preemptive scheduling for CPU-bound workloads).
