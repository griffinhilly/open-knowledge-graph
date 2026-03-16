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
status: validated
---

# Paging and Page Tables

## Core Idea
Paging eliminates external fragmentation by dividing the logical address space into fixed-size pages and physical memory into equal-size frames. The OS maintains a page table per process that maps each logical page number to its physical frame number; the MMU performs translation on every access by splitting the logical address into a page number and an offset. The Translation Lookaside Buffer (TLB) is a fast hardware cache for recent page table entries, critical for performance since every memory access would otherwise require two memory accesses (one for the page table, one for the data). Modern systems use multi-level (hierarchical) page tables to avoid allocating large contiguous page table space for sparse address spaces.

## How It's Best Learned
Work through a manual TLB lookup: given a logical address, extract page number and offset, check TLB for hit or miss, look up page table on miss, combine frame number with offset to get physical address.

## Common Misconceptions
- Paging eliminates external fragmentation but introduces internal fragmentation within the last page.
- Page size is not configurable by the programmer; it is set by the hardware and OS (typically 4KB).

## Explainer

From memory management basics, you know that the OS must allocate physical memory to multiple processes while providing each one with the illusion of a private, contiguous address space. You also know the problem with contiguous allocation: as processes are loaded and terminated, physical memory becomes fragmented into small, scattered free blocks (**external fragmentation**), eventually preventing even small processes from fitting despite sufficient total free memory. **Paging** solves this by abandoning the requirement that a process occupy contiguous physical memory.

The idea is to divide both logical memory and physical memory into fixed-size chunks. On the logical side, these chunks are called **pages**; on the physical side, they are called **frames**. A typical page/frame size is 4 KB. A process's logical address space might consist of 256 pages (1 MB total), but those pages can be scattered across any 256 available frames in physical memory — they need not be adjacent. The OS maintains a **page table** for each process that records the mapping: page 0 is in frame 47, page 1 is in frame 312, page 2 is in frame 5, and so on. External fragmentation is eliminated because any free frame can hold any page. The only waste is **internal fragmentation** — the last page of a process may not be completely full (on average, half a page is wasted per process).

Every memory access by the CPU triggers address translation. The hardware splits the logical address into two parts: the high-order bits form the **page number**, which indexes into the page table to find the corresponding frame number; the low-order bits form the **offset** within the page, which is unchanged. The frame number replaces the page number, and the result is the physical address. For example, with a 4 KB page size (12-bit offset), the logical address 0x00003A7F has page number 3 and offset 0xA7F. If the page table says page 3 maps to frame 100 (0x64), the physical address is 0x00064A7F. This translation happens on every single memory access, so it must be fast.

The problem is that the page table itself lives in memory, so a naive implementation doubles every memory access: one access to read the page table entry, then another to read the actual data. The **Translation Lookaside Buffer (TLB)** solves this. The TLB is a small, fast hardware cache (typically 64-1024 entries) that stores recently used page-to-frame mappings. On a TLB hit, translation adds zero extra memory accesses. On a TLB miss, the hardware walks the page table, caches the result in the TLB, and future accesses to that page are fast. Because programs exhibit spatial and temporal locality — they tend to access the same pages repeatedly — TLB hit rates above 99% are common, making the performance overhead of paging negligible in practice. For large address spaces (64-bit systems), a flat page table would itself consume gigabytes of memory, so modern systems use **multi-level page tables** that only allocate table entries for portions of the address space actually in use, trading a few extra memory accesses on TLB misses for dramatic space savings.
