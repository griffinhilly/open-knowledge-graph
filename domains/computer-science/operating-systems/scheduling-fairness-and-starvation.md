---
id: scheduling-fairness-and-starvation
title: Scheduling Fairness and Starvation Prevention
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- multilevel-feedback-queue-scheduling
tags:
- scheduling
- fairness
- concurrency
stage: formal-systems
status: draft
---

# Scheduling Fairness and Starvation Prevention

## Core Idea
Fair scheduling ensures all processes receive a reasonable share of CPU time and prevents indefinite delay (starvation). Starvation can occur when high-priority processes continuously arrive or when low-priority lock holders block high-priority processes. Modern systems use aging, priority inheritance, and proportional-share scheduling to mitigate these problems.
