---
id: paging
title: Paging and Page Tables
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: contiguous-memory-allocation
  type: soft
builds-toward:
- virtual-memory-management
- file-system-implementation
tags:
- paging
- page-table
- frame
- TLB
- page-number
- offset
stage: formal-systems
status: draft
---

# Paging and Page Tables

## Core Idea
Paging eliminates external fragmentation by dividing the logical address space into fixed-size pages and physical memory into equal-size frames. The OS maintains a page table per process that maps each logical page number to its physical frame number; the MMU performs translation on every access by splitting the logical address into a page number and an offset. The Translation Lookaside Buffer (TLB) is a fast hardware cache for recent page table entries, critical for performance since every memory access would otherwise require two memory accesses (one for the page table, one for the data). Modern systems use multi-level (hierarchical) page tables to avoid allocating large contiguous page table space for sparse address spaces.

## How It's Best Learned
Work through a manual TLB lookup: given a logical address, extract page number and offset, check TLB for hit or miss, look up page table on miss, combine frame number with offset to get physical address.

## Common Misconceptions
- Paging eliminates external fragmentation but introduces internal fragmentation within the last page.
- Page size is not configurable by the programmer; it is set by the hardware and OS (typically 4KB).
