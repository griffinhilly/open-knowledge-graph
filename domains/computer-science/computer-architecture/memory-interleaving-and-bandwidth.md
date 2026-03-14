---
id: memory-interleaving-and-bandwidth
title: Memory Interleaving and Bandwidth Optimization
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-organization
  type: hard
- id: dynamic-ram-dram-design
  type: soft
builds-toward:
- memory-hierarchy-design
tags:
- memory-interleaving
- bandwidth
- memory-access
stage: formal-systems
status: draft
---

# Memory Interleaving and Bandwidth Optimization

## Core Idea
Interleaving distributes consecutive addresses across multiple memory banks so that successive accesses can proceed in parallel. N-way interleaving achieves N× bandwidth improvement if successive addresses are accessed. Low-order address bits select the bank; higher bits select the address within that bank. Interleaving is essential for maintaining throughput in pipelined systems.
