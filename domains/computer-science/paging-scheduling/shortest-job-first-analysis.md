---
id: shortest-job-first-analysis
title: 'Shortest Job First: Optimality and Practicality'
domain: computer-science
course: paging-scheduling
prerequisites:
- id: scheduling-algorithm-analysis
  type: hard
builds-toward:
- priority-scheduling-inversion
tags:
- scheduling
- sjf
- optimal
stage: formal-systems
status: draft
---

# Shortest Job First: Optimality and Practicality

## Core Idea
Non-preemptive SJF minimizes average waiting time (proven optimal) but requires knowing job lengths in advance. Preemptive SJF (SRTF) uses estimates (aging, machine learning) but starvation remains a risk for long jobs.

## How It's Best Learned
Prove SJF optimality by exchange argument; implement with estimated job lengths and observe starvation on realistic workloads.

## Common Misconceptions
- Thinking SJF is practical without length prediction.
- Confusing with priority scheduling.
- Overlooking starvation from bad length estimates.
