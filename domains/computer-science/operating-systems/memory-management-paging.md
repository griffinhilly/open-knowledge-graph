---
id: memory-management-paging
title: 'Memory Management: Paging and Page Tables'
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
builds-toward:
- page-replacement-algorithms-lru-fifo
- virtual-memory-and-demand-paging
tags:
- memory-management
- virtual-memory
- address-translation
stage: formal-systems
status: draft
---

# Memory Management: Paging and Page Tables

## Core Idea
Paging divides physical and virtual memory into fixed-size pages. The page table maps virtual page numbers to physical page frames. The MMU (memory management unit) translates virtual addresses using the page table on every access. Multi-level page tables reduce memory overhead; TLBs cache translations for performance.

## Explainer

From your introduction to operating systems, you know that the OS must manage memory so multiple programs can run simultaneously without interfering with each other. **Paging** is the mechanism that makes this possible. The core idea is to break both virtual memory and physical memory into fixed-size chunks — typically 4KB — called **pages** (virtual) and **frames** (physical). Any virtual page can map to any physical frame, so a process's memory does not need to be contiguous in physical RAM.

Every process gets its own **page table**, a data structure that maps virtual page numbers to physical frame numbers. When your program accesses memory address 0x00401234, the CPU's **memory management unit** (MMU) splits this into a virtual page number (0x00401) and an offset within the page (0x234). It looks up page 0x00401 in the current process's page table, finds that it maps to physical frame 0x7A3, and accesses physical address 0x7A3234. This translation happens on every single memory access — every instruction fetch, every variable read, every stack push. The process never sees physical addresses; it operates entirely in its own virtual address space.

The problem with a flat page table is size. A 32-bit address space with 4KB pages has over one million page entries. A 64-bit address space would require an astronomically large table. **Multi-level page tables** solve this by splitting the page number into multiple indices, each indexing into a smaller table. A two-level scheme uses the upper bits to index a page directory, which points to a second-level page table, which contains the actual frame mapping. Pages of virtual memory that a process has never used need no second-level table at all — the directory entry is simply marked "not present." This means a process using only a few megabytes of a vast address space needs only a handful of small tables rather than one enormous one.

Since the page table lives in memory, every memory access would normally require two memory accesses — one to read the page table entry, one to access the actual data. This would halve performance. The **Translation Lookaside Buffer** (TLB) eliminates this overhead for the common case. The TLB is a small, fast hardware cache inside the MMU that stores recently used page-to-frame translations. On a TLB hit, translation adds zero extra memory accesses. TLB miss rates are typically below 1% because programs exhibit strong locality — they tend to access the same pages repeatedly. When the OS switches between processes, it must flush or tag the TLB entries, since each process has its own page table and the same virtual address maps to different physical frames in different processes.
