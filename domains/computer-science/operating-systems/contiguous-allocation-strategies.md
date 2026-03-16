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

## Explainer

From your study of contiguous memory allocation and address binding, you know that each process needs a region of physical memory to hold its code, data, and stack, and that the OS must decide where in memory each process goes. When the scheme requires each process to occupy a single unbroken block of addresses, the OS faces a classic placement problem: given a set of free memory holes of various sizes and a new process requesting a specific amount, which hole should it choose?

Three strategies dominate this decision. **First-fit** scans the list of free holes from the beginning and picks the first one large enough to hold the process. It is fast because it stops searching as soon as it finds a match, but it tends to leave small leftover fragments near the beginning of memory. **Best-fit** scans the entire list and picks the smallest hole that is large enough. This minimizes the leftover fragment from each allocation but is slower (it must examine every hole) and tends to create many tiny unusable fragments scattered throughout memory. **Worst-fit** picks the largest available hole, reasoning that the remaining fragment will be large enough to be useful. In practice, worst-fit performs poorly because it rapidly eliminates the large holes that could have served bigger requests later.

The fundamental problem all three strategies share is **external fragmentation**: after a sequence of allocations and deallocations, free memory becomes scattered across many small non-contiguous holes. The total free memory may be large enough for a new process, but no single contiguous block is. For example, imagine 100 MB of free memory split into twenty 5 MB holes — a process needing 20 MB cannot be loaded even though 100 MB is available. Empirical studies and the **50-percent rule** suggest that with first-fit allocation, roughly one-third of memory is lost to fragmentation on average.

**Compaction** can solve external fragmentation by relocating processes to pack them together, creating one large free block. But compaction requires relocatable addresses (base-and-limit registers or relocation hardware), and it is expensive — every byte of every relocated process must be copied and its base address updated. This is why contiguous allocation has been largely superseded by **paging**, which breaks processes into fixed-size pages that can be placed in any available frame of physical memory, eliminating external fragmentation entirely. Understanding contiguous allocation strategies matters because they illustrate the tradeoffs that motivated the move to paging and because the same first-fit/best-fit/worst-fit logic reappears in heap allocators (malloc), disk block allocation, and any resource placement problem.
