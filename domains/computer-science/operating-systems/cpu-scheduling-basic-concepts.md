---
id: cpu-scheduling-basic-concepts
title: 'CPU Scheduling: Basic Concepts'
domain: computer-science
course: operating-systems
prerequisites:
- id: context-switching-and-cpu-dispatch
  type: hard
builds-toward:
- fcfs-scheduling-algorithm
- round-robin-scheduling
- priority-scheduling-algorithms
tags:
- scheduling
- resource-allocation
- fairness
stage: formal-systems
status: draft
---

# CPU Scheduling: Basic Concepts

## Core Idea
Scheduling is the process of selecting which ready process runs next on the CPU. Scheduling goals include maximizing CPU utilization, minimizing average waiting time, ensuring fairness, and meeting deadlines. Different scheduling policies serve different workload characteristics and system objectives.
