---
id: page-replacement-algorithms-lru-fifo
title: 'Page Replacement Algorithms: LRU and FIFO'
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-paging
  type: hard
builds-toward:
- virtual-memory-and-demand-paging
tags:
- page-replacement
- memory-management
- cache-simulation
stage: formal-systems
status: draft
---

# Page Replacement Algorithms: LRU and FIFO

## Core Idea
When physical memory is full, the OS must choose a page to evict. FIFO (First-In-First-Out) evicts the oldest page; LRU (Least-Recently-Used) evicts the least-recently-accessed page. Optimal (Belady's) is infeasible but serves as a benchmark. Page replacement is central to virtual memory performance and system responsiveness.

## Common Misconceptions
LRU is always optimal (Belady's algorithm is; LRU approximates it well in practice). More memory always improves performance (Belady's anomaly shows FIFO can degrade with more memory for some workloads).
