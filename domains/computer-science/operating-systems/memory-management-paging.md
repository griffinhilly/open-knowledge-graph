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

## Questions

```yaml
- question: "A program requests 16 MB of virtual memory, but physical RAM is fragmented — the largest contiguous free block is only 4 MB. What does paging allow the OS to do?"
  type: multiple-choice
  options:
    - "Refuse the allocation, since no contiguous physical block of 16 MB exists"
    - "Temporarily swap the program to disk and wait for RAM to consolidate"
    - "Map each 4 KB virtual page to any available physical frame, regardless of physical contiguity"
    - "Double-map physical frames so the program shares memory with other processes"
  answer: 2
  explanation: "Paging's key benefit is eliminating the requirement for contiguous physical memory. The page table maps each virtual page independently to any available physical frame — the physical frames can be scattered across RAM. The program sees a large, contiguous virtual address space, but the physical backing can be spread across many non-adjacent frames. This is precisely what paging was designed to solve: the memory fragmentation problem that afflicted earlier segmentation schemes."

- question: "Why do multi-level page tables consume far less memory than a flat single-level page table for a typical process?"
  type: multiple-choice
  options:
    - "They compress page table entries using run-length encoding"
    - "Second-level tables are only allocated for regions of virtual memory the process actually uses, so large unused address ranges need no second-level entries"
    - "They store physical frame numbers instead of virtual page numbers, which are smaller"
    - "The TLB caches their entries, reducing the memory needed to store them"
  answer: 1
  explanation: "A flat page table must allocate an entry for every possible virtual page, even ones the process never uses. A 64-bit address space with 4 KB pages would require trillions of entries. A two-level scheme uses a top-level directory whose entries point to second-level tables, but only creates those second-level tables for virtual address regions the process actually accesses. A process using only a few megabytes of virtual address space needs only a handful of small tables, not one astronomical flat table."

- question: "Under paging, a process can directly access physical memory addresses if it needs to bypass the overhead of the page table lookup."
  type: true-false
  answer: false
  explanation: "Processes never see physical addresses. The MMU intercepts every single memory access — every instruction fetch, variable read, and stack operation — and translates the virtual address to a physical one using the page table. This translation is hardware-enforced and cannot be bypassed by the process. This is precisely what provides memory isolation: two processes can use the same virtual address and be directed to completely different physical locations."

- question: "Without the TLB, paging would require two memory accesses for every one that a program makes: one to look up the page table, and one to access the actual data."
  type: true-false
  answer: true
  explanation: "The page table itself lives in physical memory. Without any caching, translating a virtual address requires reading the page table entry from memory (access 1), then accessing the actual memory location (access 2). The TLB eliminates this overhead for the common case by caching recent virtual-to-physical translations in fast hardware inside the MMU. A TLB hit adds no extra memory accesses; miss rates are typically below 1% due to the strong locality of most programs."

- question: "Why does the TLB achieve high hit rates for most programs, even though it can only cache a small number of page translations?"
  type: short-answer
  answer: "Most programs exhibit strong spatial and temporal locality — they tend to access the same memory regions (the same pages) repeatedly over short time windows. A running loop touches the same code page on every iteration; local variables on the stack occupy the same frame for the duration of a function. Because the TLB caches the most recently used translations, and most accesses cluster within a small working set of pages, the cached entries cover the vast majority of accesses."
  explanation: "The TLB is effective not because it's large, but because programs are predictable. A typical TLB holds 64–1024 entries, yet hit rates exceed 99% because the working set of actively used pages is usually small. This is the same locality principle that makes CPU caches effective — programs revisit the same memory far more often than they explore new regions."
```

## Explainer

From your introduction to operating systems, you know that the OS must manage memory so multiple programs can run simultaneously without interfering with each other. **Paging** is the mechanism that makes this possible. The core idea is to break both virtual memory and physical memory into fixed-size chunks — typically 4KB — called **pages** (virtual) and **frames** (physical). Any virtual page can map to any physical frame, so a process's memory does not need to be contiguous in physical RAM.

Every process gets its own **page table**, a data structure that maps virtual page numbers to physical frame numbers. When your program accesses memory address 0x00401234, the CPU's **memory management unit** (MMU) splits this into a virtual page number (0x00401) and an offset within the page (0x234). It looks up page 0x00401 in the current process's page table, finds that it maps to physical frame 0x7A3, and accesses physical address 0x7A3234. This translation happens on every single memory access — every instruction fetch, every variable read, every stack push. The process never sees physical addresses; it operates entirely in its own virtual address space.

The problem with a flat page table is size. A 32-bit address space with 4KB pages has over one million page entries. A 64-bit address space would require an astronomically large table. **Multi-level page tables** solve this by splitting the page number into multiple indices, each indexing into a smaller table. A two-level scheme uses the upper bits to index a page directory, which points to a second-level page table, which contains the actual frame mapping. Pages of virtual memory that a process has never used need no second-level table at all — the directory entry is simply marked "not present." This means a process using only a few megabytes of a vast address space needs only a handful of small tables rather than one enormous one.

Since the page table lives in memory, every memory access would normally require two memory accesses — one to read the page table entry, one to access the actual data. This would halve performance. The **Translation Lookaside Buffer** (TLB) eliminates this overhead for the common case. The TLB is a small, fast hardware cache inside the MMU that stores recently used page-to-frame translations. On a TLB hit, translation adds zero extra memory accesses. TLB miss rates are typically below 1% because programs exhibit strong locality — they tend to access the same pages repeatedly. When the OS switches between processes, it must flush or tag the TLB entries, since each process has its own page table and the same virtual address maps to different physical frames in different processes.
