---
id: virtual-memory-management
title: Virtual Memory and Demand Paging
domain: computer-science
course: operating-systems
prerequisites:
- id: paging
  type: hard
- id: virtual-memory-basics
  type: hard
- id: segmentation
  type: soft
builds-toward:
- page-replacement-algorithms
- thrashing-and-working-set
tags:
- virtual-memory
- demand-paging
- page-fault
- swap-space
- resident-set
stage: formal-systems
status: validated
---

# Virtual Memory and Demand Paging

## Core Idea
Virtual memory decouples the logical address space from physical RAM by allowing pages to reside on disk (in swap space) when not actively needed. Demand paging loads pages only when they are accessed — on a page fault, the OS suspends the faulting process, selects a victim page to evict (possibly writing it to disk), loads the needed page from disk into a free frame, updates the page table, and resumes the process. This illusion lets a process use more memory than physically exists and enables efficient memory sharing between processes. The valid/invalid bit in each page table entry distinguishes pages currently in physical memory from those on disk.

## How It's Best Learned
Trace through a complete page fault sequence: logical address generated, TLB miss, page table lookup reveals invalid bit, OS page-fault handler invoked, disk I/O, page loaded, table updated, process restarted.

## Common Misconceptions
- Virtual address space size is limited by the address width (e.g., 48-bit on x86-64), not by physical RAM.
- Page faults are not always errors; they are normal and expected when pages must be loaded on demand.
