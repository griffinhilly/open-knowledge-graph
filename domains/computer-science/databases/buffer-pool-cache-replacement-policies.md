---
id: buffer-pool-cache-replacement-policies
title: Buffer Pool Management and Cache Replacement Policies
domain: computer-science
course: databases
prerequisites:
- id: physical-storage-pages-records
  type: hard
- id: memory-management-basics
  type: soft
builds-toward:
- crash-recovery-undo-redo
- query-execution-plan-analysis-explain
tags:
- buffer-pool
- cache
- replacement-policy
- LRU
- FIFO
stage: formal-systems
status: draft
---

# Buffer Pool Management and Cache Replacement Policies

## Core Idea
Buffer pools cache frequently accessed pages in memory to minimize disk I/O. Pages are identified by frame numbers and tracked with metadata (dirty bit, pin count, reference time). Replacement policies decide which page to evict when full: LRU (least-recently-used) works well for many workloads, FIFO is simpler, clock algorithms approximate LRU with less overhead. Pinning prevents eviction of critical pages.
