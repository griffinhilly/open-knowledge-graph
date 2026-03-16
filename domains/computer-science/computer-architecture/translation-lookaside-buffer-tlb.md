---
id: translation-lookaside-buffer-tlb
title: Translation Lookaside Buffer (TLB) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-translation
  type: hard
- id: cache-associativity-and-mapping
  type: soft
builds-toward:
- exception-handling-architecture
tags:
- tlb
- address-translation
- cache
stage: formal-systems
status: draft
---

# Translation Lookaside Buffer (TLB) Design

## Core Idea
The TLB is a small associative cache that stores recent virtual-to-physical address translations. A TLB hit provides the physical page number in one cycle; a miss requires a page table walk (several memory accesses). TLB entries include the virtual page number, physical page number, and protection bits. TLB size is a trade-off between speed and area; typical sizes are 32–512 entries.

## Explainer

From your study of virtual memory translation, you know that every memory access requires converting a virtual address to a physical address by looking up the page table. The problem is that the page table itself lives in main memory, so a naive implementation would double the cost of every memory access — one access to translate the address, then another to fetch the actual data. The **translation lookaside buffer (TLB)** eliminates this penalty for the vast majority of accesses by caching recent translations in a small, fast, on-chip structure.

The TLB works on the same principle as the caches you have studied — **locality of reference**. Programs tend to access the same pages repeatedly (temporal locality) and access addresses near each other (spatial locality). Since a single page translation covers an entire 4 KB page (or larger), even a small TLB with 64 entries can cover 256 KB of actively used memory. When the processor issues a memory access, it extracts the virtual page number and simultaneously searches the TLB for a matching entry. If found (a **TLB hit**), the physical page number is returned in a single cycle and the memory access proceeds with no delay. If not found (a **TLB miss**), the processor must perform a **page table walk** — traversing the multi-level page table in memory to find the correct translation — which may cost tens to hundreds of cycles.

The TLB is typically organized as a **fully associative** or **set-associative** cache, drawing on the associativity concepts from your cache design studies. Fully associative means any translation can go in any TLB entry, which maximizes hit rates but requires comparing the virtual page number against every entry simultaneously using parallel comparators. Each TLB entry stores not just the virtual-to-physical mapping but also **protection bits** (read, write, execute permissions), a **valid bit**, and often an **address space identifier (ASID)** that tags which process owns the entry, avoiding the need to flush the entire TLB on every context switch.

TLB misses are handled in one of two ways depending on the architecture. In a **hardware-managed TLB** (as in x86), the processor itself walks the page table and fills the TLB entry automatically — software never sees the miss. In a **software-managed TLB** (as in MIPS), a TLB miss triggers an exception, and the operating system's trap handler looks up the translation and loads the TLB entry manually. Hardware management is faster for individual misses; software management gives the OS more flexibility in page table format. Either way, the TLB is the single most performance-critical structure in the memory hierarchy — a typical program experiences TLB hit rates above 99%, and even a small drop in hit rate can devastate performance because every memory access depends on translation.
