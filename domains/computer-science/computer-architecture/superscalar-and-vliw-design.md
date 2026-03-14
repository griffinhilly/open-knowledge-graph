---
id: superscalar-and-vliw-design
title: Superscalar and VLIW Processors
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-pipeline-organization
  type: hard
builds-toward:
- out-of-order-execution-design
- power-thermal-performance-metrics
tags:
- superscalar
- vliw
- parallelism
- performance
stage: formal-systems
status: draft
---

# Superscalar and VLIW Processors

## Core Idea
Superscalar processors issue multiple instructions per clock cycle by using multiple pipelines and dynamic dispatch; VLIW (Very Long Instruction Word) processors issue multiple operations per instruction, with scheduling done at compile time. Both exploit instruction-level parallelism.

## How It's Best Learned
Compare superscalar (dynamic, hardware scheduling) with VLIW (static, compile-time scheduling) using a data dependency graph.

## Common Misconceptions
Superscalar and VLIW are not the same—superscalar schedules dynamically; VLIW schedules statically. Both require careful hazard management.
