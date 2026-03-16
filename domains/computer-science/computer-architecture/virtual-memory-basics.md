---
id: virtual-memory-basics
title: Virtual Memory and Paging
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-hierarchy-overview
  type: hard
- id: memory-organization
  type: hard
- id: cache-replacement-policies
  type: soft
tags:
- virtual-memory
- paging
- page-table
- TLB
- address-translation
stage: formal-systems
status: validated
---

# Virtual Memory and Paging

## Core Idea
Virtual memory gives each process the illusion of a private, contiguous address space larger than physical RAM. The virtual address space is divided into fixed-size pages; corresponding physical memory units are called frames. A page table maintained by the OS and hardware maps virtual page numbers to physical frame numbers. The Translation Lookaside Buffer (TLB) caches recent page table entries to speed up address translation. Pages not in physical memory are stored on disk and fetched on a page fault.

## How It's Best Learned
Trace the full address translation path: virtual address → TLB lookup or page table walk → physical address → cache lookup → memory. Simulate page replacement policies on a small address sequence. Understand the page fault handler's role in the OS.

## Common Misconceptions
- Virtual memory is not just using disk as RAM; it also provides memory isolation between processes and enables memory-mapped files.
- A TLB miss does not always cause a page fault; the page may already be in physical memory and the TLB simply needs to be refilled from the page table.

## Explainer

From your study of the memory hierarchy, you understand that faster memory is smaller and more expensive, while slower memory is larger and cheaper. Virtual memory extends this principle one level further: it uses main memory (DRAM) as a "cache" for an even larger and slower storage level — the disk. But virtual memory does far more than just expand capacity. It gives each running process the illusion that it has the entire address space to itself, completely isolated from every other process. This abstraction is so foundational that virtually every modern operating system depends on it.

The mechanism works by dividing the virtual address space into fixed-size chunks called **pages** (typically 4 KB) and physical memory into same-sized chunks called **frames**. A data structure called the **page table**, maintained by the operating system, maps each virtual page number to a physical frame number. When a program accesses memory address 0x7FFF0042, the hardware splits this into a virtual page number and an offset within that page. It looks up the page number in the page table to find which physical frame holds that page, then combines the frame number with the offset to form the actual physical address. The program never knows or cares where its data physically resides — it works entirely in virtual addresses.

Because the page table can be enormous (a 48-bit virtual address space with 4 KB pages has billions of entries), walking through it on every memory access would be devastatingly slow. The **Translation Lookaside Buffer (TLB)** solves this by caching recently used page table entries in a small, fast hardware structure — typically 64 to 1024 entries with sub-nanosecond access time. Thanks to locality, most accesses hit the TLB, and the full page table walk is only needed on a TLB miss. This is the same caching principle you learned in the memory hierarchy, now applied to address translation itself.

When a program accesses a page that is not currently in physical memory — perhaps it was swapped to disk to make room for another process — a **page fault** occurs. The hardware traps to the operating system, which finds the page on disk, loads it into a free frame (evicting another page if necessary, using replacement policies similar to those you studied for caches), updates the page table, and restarts the instruction. This is expensive — disk access is millions of times slower than DRAM — but it happens rarely in well-behaved programs because locality keeps the **working set** of actively used pages small enough to fit in physical memory. The genius of virtual memory is that it makes the common case fast (TLB hit, page in memory) while gracefully handling the uncommon case (page fault) through a transparent software mechanism that the program never sees.
