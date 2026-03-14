---
id: io-architecture-system-integration
title: I/O Architecture and System Integration
domain: computer-science
course: computer-architecture
prerequisites:
- id: io-systems-overview
  type: hard
- id: interrupt-exception-handling
  type: soft
builds-toward:
- power-thermal-performance-metrics
tags:
- io
- architecture
- system
- integration
stage: formal-systems
status: draft
---

# I/O Architecture and System Integration

## Core Idea
I/O architecture bridges CPU, memory, and external devices via buses and controllers. DMA transfers data without CPU intervention; memory-mapped I/O treats devices as memory addresses; programmed I/O uses load/store instructions.
