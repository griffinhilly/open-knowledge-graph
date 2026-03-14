---
id: contiguous-memory-allocation
title: Contiguous Memory Allocation and Fragmentation
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
builds-toward:
- paging
- segmentation
tags:
- fragmentation
- fixed-partition
- variable-partition
- first-fit
- best-fit
- worst-fit
stage: formal-systems
status: validated
---

# Contiguous Memory Allocation and Fragmentation

## Core Idea
The simplest memory allocation scheme places each process in a single contiguous region of physical memory. Fixed-partition schemes divide RAM into fixed-size regions (suffering internal fragmentation when a process is smaller than its partition), while variable-partition schemes allocate exactly what is needed (suffering external fragmentation — enough total free memory exists, but it is scattered in small non-contiguous holes). Allocation policies — First-Fit (allocate first hole large enough), Best-Fit (smallest hole that works), and Worst-Fit (largest hole) — trade off allocation speed against fragmentation. Compaction, relocating all processes to consolidate free space, is expensive and requires execution-time address binding.

## Common Misconceptions
- Best-Fit does not always result in least fragmentation in practice; First-Fit is often competitive and faster.
- External fragmentation is not fixable by compaction alone; paging eliminates it structurally.
