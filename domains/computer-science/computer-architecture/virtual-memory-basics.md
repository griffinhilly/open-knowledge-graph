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

## Questions

```yaml
- question: "A program accesses virtual address 0x5000. The TLB has no entry for this page, but the page table shows the page IS present in physical memory. What happens?"
  type: multiple-choice
  options:
    - "A page fault occurs and the OS loads the page from disk"
    - "The hardware walks the page table, finds the frame number, loads the mapping into the TLB, and the access succeeds — no page fault"
    - "The program crashes because a TLB miss means the page is inaccessible"
    - "The OS suspends the program until the TLB has an available slot"
  answer: 1
  explanation: "A TLB miss means the mapping is not cached in the TLB — not that the page isn't in physical memory. The hardware performs a page table walk, finds the physical frame number, loads the entry into the TLB, and the memory access completes without OS involvement. A PAGE FAULT only occurs when the page is actually absent from physical memory (stored on disk or never loaded). TLB miss ≠ page fault."

- question: "Process A writes data to its virtual address 0x1000. Process B also uses virtual address 0x1000. What does virtual memory guarantee about these accesses?"
  type: multiple-choice
  options:
    - "They access the same physical location, which is protected by a lock the OS manages"
    - "The OS prevents any two processes from using overlapping virtual addresses"
    - "Each process has its own page table mapping its virtual addresses to separate physical frames, so they are fully isolated"
    - "The TLB arbitrates which process gets priority when virtual addresses collide"
  answer: 2
  explanation: "Memory isolation is a core purpose of virtual memory. Each process has its own page table, mapping its private virtual address space to different physical frames. Two processes can use the same virtual address without conflict or even awareness of each other. This abstraction is foundational to modern OS security and stability."

- question: "The primary purpose of virtual memory is to allow programs to use more total memory than physically fits in RAM by storing excess pages on disk."
  type: true-false
  answer: false
  explanation: "While virtual memory does enable programs to address more memory than physical RAM, this understates its purpose. Virtual memory also provides memory isolation between processes (each process has a private address space), enables memory-mapped files, and supports memory protection — all independently valuable even on systems with abundant RAM. Reducing virtual memory to 'disk as RAM' misses its most foundational contribution."

- question: "The Translation Lookaside Buffer (TLB) is a hardware cache for page table entries, and a TLB hit allows address translation without accessing the page table in main memory."
  type: true-false
  answer: true
  explanation: "The TLB stores recently used virtual-to-physical page mappings. On a TLB hit, the hardware retrieves the frame number in a single fast lookup — typically sub-nanosecond — without doing the full page table walk (which requires multiple memory accesses). This is the same caching principle as the rest of the memory hierarchy, now applied to address translation itself."

- question: "Why is a TLB miss not the same as a page fault, and what happens in each case?"
  type: short-answer
  answer: "A TLB miss means the virtual-to-physical mapping is not cached in the TLB, but the page may still be in physical memory. The hardware walks the page table in RAM, finds the frame number, loads it into the TLB, and the access completes — no OS involvement, relatively cheap. A page fault occurs when the page is not in physical memory at all (it is on disk or has never been loaded). The hardware traps to the OS, which locates the page on disk, loads it into a free frame, updates the page table, and restarts the instruction. Page faults are expensive (disk I/O); TLB misses are not."
  explanation: "Confusing TLB misses with page faults is a common error. The distinction matters because they involve very different mechanisms and costs: a TLB miss is handled entirely in hardware or through a fast table walk, while a page fault requires full OS intervention and disk I/O that is millions of times slower."
```

## Explainer

From your study of the memory hierarchy, you understand that faster memory is smaller and more expensive, while slower memory is larger and cheaper. Virtual memory extends this principle one level further: it uses main memory (DRAM) as a "cache" for an even larger and slower storage level — the disk. But virtual memory does far more than just expand capacity. It gives each running process the illusion that it has the entire address space to itself, completely isolated from every other process. This abstraction is so foundational that virtually every modern operating system depends on it.

The mechanism works by dividing the virtual address space into fixed-size chunks called **pages** (typically 4 KB) and physical memory into same-sized chunks called **frames**. A data structure called the **page table**, maintained by the operating system, maps each virtual page number to a physical frame number. When a program accesses memory address 0x7FFF0042, the hardware splits this into a virtual page number and an offset within that page. It looks up the page number in the page table to find which physical frame holds that page, then combines the frame number with the offset to form the actual physical address. The program never knows or cares where its data physically resides — it works entirely in virtual addresses.

Because the page table can be enormous (a 48-bit virtual address space with 4 KB pages has billions of entries), walking through it on every memory access would be devastatingly slow. The **Translation Lookaside Buffer (TLB)** solves this by caching recently used page table entries in a small, fast hardware structure — typically 64 to 1024 entries with sub-nanosecond access time. Thanks to locality, most accesses hit the TLB, and the full page table walk is only needed on a TLB miss. This is the same caching principle you learned in the memory hierarchy, now applied to address translation itself.

When a program accesses a page that is not currently in physical memory — perhaps it was swapped to disk to make room for another process — a **page fault** occurs. The hardware traps to the operating system, which finds the page on disk, loads it into a free frame (evicting another page if necessary, using replacement policies similar to those you studied for caches), updates the page table, and restarts the instruction. This is expensive — disk access is millions of times slower than DRAM — but it happens rarely in well-behaved programs because locality keeps the **working set** of actively used pages small enough to fit in physical memory. The genius of virtual memory is that it makes the common case fast (TLB hit, page in memory) while gracefully handling the uncommon case (page fault) through a transparent software mechanism that the program never sees.
