---
id: deadlock-conditions-and-graphs
title: 'Deadlock: Conditions and Resource Allocation Graphs'
domain: computer-science
course: operating-systems
prerequisites:
- id: binary-semaphores-mutexes
  type: hard
builds-toward:
- deadlock-prevention-and-avoidance
- deadlock-detection-and-resource-recovery
tags:
- deadlock
- resource-allocation
- necessary-conditions
stage: formal-systems
status: draft
---

# Deadlock: Conditions and Resource Allocation Graphs

## Core Idea
Deadlock occurs when processes cannot proceed because they hold resources others need. Necessary conditions are mutual exclusion, hold-and-wait, no preemption, and circular wait. Resource allocation graphs visualize resource requests and assignments; cycles indicate potential deadlocks. Understanding these conditions guides prevention and detection strategies.
