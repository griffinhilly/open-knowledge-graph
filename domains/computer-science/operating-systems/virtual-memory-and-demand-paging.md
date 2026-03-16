---
id: virtual-memory-and-demand-paging
title: Virtual Memory and Demand Paging
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-paging
  type: hard
- id: page-replacement-algorithms-lru-fifo
  type: soft
tags:
- virtual-memory
- memory-management
- demand-paging
stage: formal-systems
status: draft
---

# Virtual Memory and Demand Paging

## Core Idea
Virtual memory abstracts hardware memory, giving processes the illusion of a large, contiguous address space. Demand paging loads pages on-demand from disk when accessed, not preemptively. This enables oversubscription (total virtual memory > physical memory) and strong process isolation. Page faults trigger I/O; performance depends on locality and page replacement policy.

## Explainer

From your study of paging, you know that physical memory is divided into fixed-size frames and that a page table translates virtual addresses to physical frame numbers. **Virtual memory** extends this idea to its logical conclusion: every process gets its own complete virtual address space — typically 2^48 bytes or more on a 64-bit system — regardless of how much physical RAM is installed. The operating system and hardware collaborate to maintain the illusion that all of this space is available, even though only a fraction is backed by physical memory at any moment. The rest lives on disk, ready to be brought in when needed.

**Demand paging** is the strategy that makes this practical. Rather than loading an entire program into memory at startup, the OS marks most pages as "not present" in the page table. When the CPU tries to access a not-present page, the hardware raises a **page fault** — a trap to the operating system. The OS then locates the page's contents on disk (in a swap area or the original executable file), finds a free physical frame, reads the page data from disk into that frame, updates the page table to point to the new frame, and resumes the faulting instruction. From the process's perspective, nothing unusual happened — the memory access simply took a bit longer. This lazy loading means programs start faster (no waiting for everything to load) and memory-efficient programs never load pages they do not actually touch.

The critical tradeoff is performance. A normal memory access takes nanoseconds; a page fault that requires reading from disk takes milliseconds — roughly a million times slower. This is why **locality of reference** matters so much. Programs that access memory in predictable patterns (sequential array traversal, repeatedly using the same working set of data) fault rarely because their active pages stay in memory. Programs with scattered, unpredictable access patterns generate frequent faults and grind to a halt — a condition called **thrashing**, where the system spends more time swapping pages than doing useful work. You may recall page replacement algorithms like LRU and FIFO from your prerequisites; these algorithms decide which page to evict when all physical frames are occupied. A good replacement policy keeps the working set in memory and evicts pages that will not be needed soon.

Virtual memory also provides **process isolation** as an architectural guarantee, not just a convention. Because each process has its own page table, process A literally cannot name a physical address belonging to process B — the address "0x4000" in process A maps to a completely different frame than "0x4000" in process B. A buggy or malicious process can corrupt its own memory but cannot reach another process's data. This same mechanism enables features like copy-on-write (sharing pages between processes until one writes, at which point the OS transparently duplicates the page), memory-mapped files (mapping a file's contents directly into the address space), and overcommit (allocating more virtual memory than physical RAM plus swap, betting that not all of it will be used simultaneously).
