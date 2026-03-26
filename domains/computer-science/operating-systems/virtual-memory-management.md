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

## Questions

```yaml
- question: "A process is allocated 8 GB of virtual memory on a machine with only 4 GB of physical RAM. The program runs successfully. How is this possible?"
  type: multiple-choice
  options:
    - "The OS compresses pages in RAM to fit twice as much data"
    - "Virtual memory allows pages not currently in use to reside on disk; the OS loads them on demand via page faults, keeping only the active working set in RAM"
    - "The CPU silently discards memory accesses that fall outside physical RAM"
    - "The program is allocated 4 GB of real memory and 4 GB of empty address space that cannot actually be used"
  answer: 1
  explanation: "Demand paging makes this possible: not all pages need to be in RAM simultaneously. Pages currently unused reside on disk (swap space). When the process accesses a page on disk, a page fault occurs — the OS loads that page into a free frame, possibly evicting another page, then resumes the process. As long as the program's working set (actively used pages) fits in RAM, it runs fine. Only if it tries to use all 8 GB simultaneously would performance degrade severely (thrashing)."

- question: "When a CPU instruction triggers a page fault, what is the correct sequence of events?"
  type: multiple-choice
  options:
    - "The process is terminated; the OS logs the error and notifies the user"
    - "The CPU retries the instruction automatically up to three times before invoking the OS"
    - "The hardware signals the OS; the OS finds the page on disk, loads it into a free frame, updates the page table, and restarts the faulting instruction"
    - "The OS immediately swaps the entire process out to disk and loads a different process"
  answer: 2
  explanation: "A page fault is a hardware exception that transfers control to the OS page-fault handler. The handler locates the needed page on disk (in swap space), finds or frees a physical frame (evicting another page if necessary), reads the page from disk into that frame, marks the page table entry valid, and restarts the instruction that originally triggered the fault. From the process's perspective, the access simply took longer. The process is not terminated — page faults are the normal mechanism for demand paging."

- question: "A page fault usually signals a programming error, and the operating system is expected to terminate the faulting process."
  type: true-false
  answer: false
  explanation: "Page faults are a normal, expected part of demand paging — not errors. Every time a process first accesses a page that hasn't been loaded yet, a page fault occurs and the OS loads it from disk. This is the designed mechanism that enables virtual address spaces larger than physical RAM. Only a specific type of page fault — accessing an invalid address (a segmentation fault) — results in process termination. The valid/invalid bit distinguishes between 'this page is on disk' (load it) and 'this address is not mapped' (terminate)."

- question: "The maximum size of a process's virtual address space is determined by the amount of physical RAM installed in the system."
  type: true-false
  answer: false
  explanation: "Virtual address space size is bounded by the address width of the CPU, not by physical RAM. On a 64-bit system with 48-bit virtual addresses (typical x86-64), each process can have up to 2^48 = 256 TB of virtual address space — far exceeding any practical amount of RAM. Physical RAM limits how many pages can reside in memory simultaneously, which affects performance (page fault frequency), but the virtual address space itself is constrained by the hardware's addressing capability."

- question: "Why does a program that causes many page faults run dramatically slower, and what is the extreme form of this condition called?"
  type: short-answer
  answer: "Each page fault requires reading a page from disk into RAM — a disk access takes roughly 10 milliseconds, while reading from RAM takes about 100 nanoseconds, making disk roughly 100,000× slower. A program that repeatedly accesses pages not in physical memory spends most of its time waiting for disk I/O rather than executing instructions. The extreme case — where the OS spends more time swapping pages than executing code — is called thrashing, and it can reduce effective throughput to near zero."
  explanation: "The performance gap between RAM and disk is the fundamental constraint behind demand paging's cost. Occasional page faults are acceptable; frequent ones indicate the working set (actively used pages) no longer fits in RAM. The OS attempts to minimize this through page replacement algorithms (LRU, CLOCK, etc.) that predict which pages to keep resident. Understanding this tension — unlimited virtual address space vs. the cost of every page fault — explains why memory access patterns and working set size matter enormously for real program performance."
```

## Explainer

From your study of paging and virtual memory basics, you know that a process's address space is divided into fixed-size pages, and a page table maps each virtual page to a physical frame in RAM. Virtual memory management extends this idea with a powerful insight: **not every page needs to be in physical memory at the same time**. Pages that aren't currently being used can live on disk in a region called **swap space**, and the OS loads them into RAM only when the process actually tries to access them. This is called **demand paging** — pages are loaded on demand, not in advance.

Here's how it works in practice. Each entry in the page table has a **valid/invalid bit**. Valid means the page is currently in a physical frame; invalid means it's somewhere on disk (or hasn't been allocated at all). When the CPU translates a virtual address and finds an invalid bit, it triggers a **page fault** — a hardware exception that transfers control to the operating system's page fault handler. The handler determines where the needed page lives on disk, finds a free physical frame (or evicts an existing page to make room), reads the page from disk into that frame, updates the page table entry to mark it valid, and restarts the instruction that faulted. From the process's perspective, the memory access simply took longer than usual.

The practical consequence is remarkable: a process can have a virtual address space far larger than physical RAM. A program that allocates 8 GB of memory on a machine with 4 GB of RAM works fine — as long as it doesn't actively use all 8 GB simultaneously. The OS juggles pages between RAM and disk, keeping the **working set** (the pages actively in use) in physical memory while less-used pages wait on disk. This also enables efficient memory sharing: if two processes load the same shared library, the OS can map the library's pages into both address spaces using the same physical frames, storing only one copy in RAM.

The cost of this illusion is the page fault itself. Accessing RAM takes roughly 100 nanoseconds; reading a page from disk takes milliseconds — about 10,000 times slower. A program that frequently accesses pages not in memory (causing many page faults) will slow to a crawl, a condition called **thrashing**. The OS uses page replacement algorithms to decide which pages to evict, trying to keep the most-needed pages resident. Understanding this tension — the flexibility of a huge virtual address space versus the performance penalty of page faults — is central to reasoning about how real programs use memory and why memory-access patterns matter so much for performance.
