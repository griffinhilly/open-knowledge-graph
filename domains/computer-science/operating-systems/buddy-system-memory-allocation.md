---
id: buddy-system-memory-allocation
title: Buddy System Memory Allocation
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: contiguous-memory-allocation
  type: soft
builds-toward:
- slab-allocator-kernel-memory
tags:
- allocation
- memory
- fragmentation
stage: formal-systems
status: draft
---

# Buddy System Memory Allocation

## Core Idea
The buddy system allocates memory in power-of-two sizes, recursively subdividing large blocks and merging free blocks of equal size. It reduces external fragmentation compared to simple contiguous allocation and enables efficient coalescing of freed memory. The algorithm is practical for kernel memory allocation but has internal fragmentation overhead due to power-of-two constraints.
