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
status: draft
---

# CPU Scheduling Fundamentals

## Core Idea
CPU scheduling is the task of deciding which ready process runs next on the CPU, with the goal of maximizing utilization and meeting fairness or latency objectives. The scheduler operates at multiple levels: long-term (admission), medium-term (swapping), and short-term (dispatch). Key metrics for evaluating schedulers include CPU utilization, throughput, turnaround time (total time from submission to completion), waiting time, and response time. Processes alternate between CPU bursts (active computation) and I/O bursts (waiting on devices), and this burst pattern heavily influences which scheduling algorithm performs best.

## How It's Best Learned
Simulate scheduling decisions on paper with a Gantt chart using five or six example processes with different burst times. Calculate waiting and turnaround times for each algorithm.

## Common Misconceptions
- A scheduler that maximizes CPU utilization may not minimize user-perceived latency.
- Preemptive and non-preemptive are not algorithm-specific traits; most algorithms have both variants.
