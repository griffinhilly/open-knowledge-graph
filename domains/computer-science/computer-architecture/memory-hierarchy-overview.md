---
id: memory-hierarchy-overview
title: Memory Hierarchy
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-organization
  type: hard
- id: registers-and-register-files
  type: soft
builds-toward:
- cache-memory-design
- virtual-memory-basics
tags:
- memory-hierarchy
- cache
- DRAM
- storage
- locality
stage: formal-systems
status: validated
---

# Memory Hierarchy

## Core Idea
The memory hierarchy organizes storage into levels with increasing capacity and decreasing speed moving away from the CPU: registers → L1/L2/L3 cache → main memory (DRAM) → secondary storage (SSD/HDD). The hierarchy exploits temporal locality (recently accessed data will likely be accessed again) and spatial locality (data near recently accessed data will likely be accessed soon). The goal is to provide the illusion of a large, fast, cheap memory by keeping frequently used data at the top of the hierarchy.

## How It's Best Learned
Look up actual latency and capacity numbers for each hierarchy level in a modern processor. Trace what happens when a CPU reads a value: which levels are checked in order and how data is brought up through the hierarchy on a miss. Relate to time-space-complexity trade-offs in algorithms.

## Common Misconceptions
- Cache memory is not explicitly addressed by programs; it is managed automatically by hardware.
- A cache miss does not mean data is lost — it is simply not in the cache and must be fetched from a lower level, which takes more time.
