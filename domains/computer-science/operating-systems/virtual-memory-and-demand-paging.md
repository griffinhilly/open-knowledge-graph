---
id: virtual-memory-and-demand-paging
title: Virtual Memory and Demand Paging
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-paging
  type: hard
- id: page-replacement-algorithms-lru-fifo
  type: soft
tags:
- virtual-memory
- memory-management
- demand-paging
stage: formal-systems
status: draft
---

# Virtual Memory and Demand Paging

## Core Idea
Virtual memory abstracts hardware memory, giving processes the illusion of a large, contiguous address space. Demand paging loads pages on-demand from disk when accessed, not preemptively. This enables oversubscription (total virtual memory > physical memory) and strong process isolation. Page faults trigger I/O; performance depends on locality and page replacement policy.
