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
