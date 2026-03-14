---
id: priority-scheduling-algorithms
title: Priority Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
tags:
- scheduling-algorithms
- priority-based
- starvation-risk
stage: formal-systems
status: draft
---

# Priority Scheduling Algorithms

## Core Idea
Priority scheduling associates a priority with each process and runs the highest-priority process. Preemptive variants interrupt lower-priority processes when higher-priority ones arrive. However, priority scheduling can starve low-priority processes and requires careful priority assignment and aging techniques to prevent pathological behavior.

## Common Misconceptions
Higher priority always means faster execution (depends on competing processes and workload). Static priorities are always better (dynamic/adaptive priorities often prevent starvation).
