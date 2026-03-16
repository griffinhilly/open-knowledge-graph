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

## Explainer

From your study of memory management basics, you know the OS must decide where in physical memory to place each process. The simplest approach is **contiguous allocation**: give each process a single unbroken block of memory. This is easy to implement — the OS just needs to track the start address and size of each allocation — and it makes address translation trivial (add the base address to every logical address). But contiguous allocation creates a fundamental tension between simplicity and efficient use of memory.

**Fixed partitioning** divides physical memory into slots of predetermined size at boot time. Process A gets partition 1, process B gets partition 2, and so on. The problem is obvious: if a process needs 60 KB but the smallest available partition is 256 KB, the remaining 196 KB is wasted. This waste inside an allocated region is called **internal fragmentation**. You cannot give that leftover space to another process because the partition boundaries are fixed. It is like assigning each family a standardized apartment — a single occupant gets the same space as a family of four.

**Variable partitioning** eliminates internal fragmentation by allocating exactly the amount of memory each process needs. But it introduces a different problem. As processes start and finish in unpredictable order, memory becomes a patchwork of allocated blocks and free holes. Eventually you might have 100 KB free total, but split across three non-adjacent holes of 40 KB, 35 KB, and 25 KB — none large enough for a new 80 KB process. This is **external fragmentation**: enough total free memory exists, but no single contiguous block is large enough. The allocation policy determines how severe this gets. **First-Fit** scans from the beginning and takes the first hole that is large enough — fast, but can clutter the front of memory. **Best-Fit** finds the smallest sufficient hole — minimizes leftover scraps per allocation but creates many tiny unusable fragments. **Worst-Fit** takes the largest hole, hoping the remainder is still useful — but in practice performs poorly because it rapidly consumes the few large blocks.

The OS can fight external fragmentation through **compaction**: pausing all processes, sliding their memory blocks together to consolidate free space, and updating all their base addresses. This works but is expensive — every byte of occupied memory might need to move, and all processes must be paused during the shuffle. Compaction also requires that addresses can be rebound at runtime (dynamic address binding), which not all systems support. These limitations are precisely why operating systems moved beyond contiguous allocation to **paging**, which you will study next. Paging solves external fragmentation entirely by breaking memory into small fixed-size frames and allowing a process's logical address space to map to non-contiguous physical frames — but understanding why paging exists requires first understanding the fragmentation problems that contiguous allocation cannot escape.
