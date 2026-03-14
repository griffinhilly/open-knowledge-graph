---
id: deadlock-detection-and-resource-recovery
title: Deadlock Detection and Recovery
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-conditions-and-graphs
  type: hard
tags:
- deadlock
- detection
- recovery
- resource-allocation
stage: formal-systems
status: draft
---

# Deadlock Detection and Recovery

## Core Idea
Deadlock detection uses resource allocation graphs to identify cycles, indicating deadlock. The OS periodically checks for cycles. Recovery involves terminating processes (simple but destructive) or preempting resources (complex but less disruptive). Detection-and-recovery trades off prevention overhead for acceptance of occasional deadlocks.
