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

## Explainer

From your study of paging and virtual memory basics, you know that a process's address space is divided into fixed-size pages, and a page table maps each virtual page to a physical frame in RAM. Virtual memory management extends this idea with a powerful insight: **not every page needs to be in physical memory at the same time**. Pages that aren't currently being used can live on disk in a region called **swap space**, and the OS loads them into RAM only when the process actually tries to access them. This is called **demand paging** — pages are loaded on demand, not in advance.

Here's how it works in practice. Each entry in the page table has a **valid/invalid bit**. Valid means the page is currently in a physical frame; invalid means it's somewhere on disk (or hasn't been allocated at all). When the CPU translates a virtual address and finds an invalid bit, it triggers a **page fault** — a hardware exception that transfers control to the operating system's page fault handler. The handler determines where the needed page lives on disk, finds a free physical frame (or evicts an existing page to make room), reads the page from disk into that frame, updates the page table entry to mark it valid, and restarts the instruction that faulted. From the process's perspective, the memory access simply took longer than usual.

The practical consequence is remarkable: a process can have a virtual address space far larger than physical RAM. A program that allocates 8 GB of memory on a machine with 4 GB of RAM works fine — as long as it doesn't actively use all 8 GB simultaneously. The OS juggles pages between RAM and disk, keeping the **working set** (the pages actively in use) in physical memory while less-used pages wait on disk. This also enables efficient memory sharing: if two processes load the same shared library, the OS can map the library's pages into both address spaces using the same physical frames, storing only one copy in RAM.

The cost of this illusion is the page fault itself. Accessing RAM takes roughly 100 nanoseconds; reading a page from disk takes milliseconds — about 10,000 times slower. A program that frequently accesses pages not in memory (causing many page faults) will slow to a crawl, a condition called **thrashing**. The OS uses page replacement algorithms to decide which pages to evict, trying to keep the most-needed pages resident. Understanding this tension — the flexibility of a huge virtual address space versus the performance penalty of page faults — is central to reasoning about how real programs use memory and why memory-access patterns matter so much for performance.
