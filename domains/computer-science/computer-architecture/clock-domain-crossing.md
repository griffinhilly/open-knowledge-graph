---
id: clock-domain-crossing
title: Clock Domain Crossing and Synchronization
domain: computer-science
course: computer-architecture
prerequisites:
- id: synchronous-logic-and-clocks
  type: hard
- id: flip-flops-and-latches
  type: soft
builds-toward:
- multi-core-system-design
tags:
- asynchronous
- synchronization
- metastability
stage: formal-systems
status: draft
---

# Clock Domain Crossing and Synchronization

## Core Idea
When signals cross between clock domains running at different speeds, metastability—where a flip-flop output is neither 0 nor 1—can occur. Synchronizers using cascaded flip-flops (or special synchronization circuits) reduce metastability probability to acceptable levels. This is critical in multi-core and peripheral integration.
