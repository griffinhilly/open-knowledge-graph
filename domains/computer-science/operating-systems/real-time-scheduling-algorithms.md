---
id: real-time-scheduling-algorithms
title: Real-Time Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: priority-scheduling-algorithms
  type: hard
- id: multilevel-feedback-queue-scheduling
  type: soft
tags:
- scheduling
- real-time
- deterministic
stage: formal-systems
status: draft
---

# Real-Time Scheduling Algorithms

## Core Idea
Real-time systems require deterministic scheduling guarantees to meet task deadlines. Rate-Monotonic Scheduling (RMS) assigns priorities inversely to task period length, while Earliest Deadline First (EDF) dynamically selects the task nearest its deadline. Both algorithms have precise schedulability conditions and are used in safety-critical applications.
