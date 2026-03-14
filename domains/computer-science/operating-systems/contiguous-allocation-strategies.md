---
id: contiguous-allocation-strategies
title: Contiguous Memory Allocation Strategies
domain: computer-science
course: operating-systems
prerequisites:
- id: contiguous-memory-allocation
  type: hard
- id: memory-layout-and-address-binding
  type: hard
builds-toward:
- virtual-address-translation-scheme
tags:
- memory-management
- allocation
- contiguous
stage: formal-systems
status: draft
---

# Contiguous Memory Allocation Strategies

## Core Idea
Contiguous allocation assigns each process a single contiguous RAM region. Allocation algorithms (first-fit, best-fit, worst-fit) balance speed and fragmentation. External fragmentation accumulates; compaction (expensive) or non-contiguous schemes (paging) address this.
