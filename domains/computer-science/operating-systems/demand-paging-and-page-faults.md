---
id: demand-paging-and-page-faults
title: Demand Paging and Page Faults
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-and-demand-paging
  type: hard
- id: page-replacement-algorithms
  type: soft
builds-toward:
- copy-on-write-optimization
- thrashing-and-working-set
tags:
- paging
- memory
- virtual-memory
stage: formal-systems
status: draft
---

# Demand Paging and Page Faults

## Core Idea
Demand paging loads pages into memory only when accessed, reducing memory pressure and enabling programs larger than physical RAM. A page fault occurs when accessing a page not in memory; the kernel fetches it from disk and resumes execution. Frequent page faults (thrashing) severely degrade performance and indicate excessive memory overcommitment or poor working set behavior.

## Explainer

From your study of virtual memory, you know that each process sees a large, private address space mapped through page tables to physical frames. But here is a practical question: when a process starts, does the OS load its entire address space — code, data, stack, heap, shared libraries — into physical memory? For a large application this could be hundreds of megabytes or more, and most of it may never be accessed during a given run. **Demand paging** takes the lazy approach: pages are loaded into physical memory only when the process actually tries to access them, not before.

When a process accesses an address whose page is not currently in physical memory, the hardware triggers a **page fault** — a special exception that transfers control to the kernel's page fault handler. The handler looks up the faulting address in the process's page table to determine what should be there. If the page belongs to the process's valid address space (mapped in its virtual memory layout but not yet loaded), the kernel allocates a free physical frame, reads the page's contents from disk (from the executable file, a swap partition, or a memory-mapped file), updates the page table entry to point to the new frame, and then restarts the instruction that faulted. From the process's perspective, nothing unusual happened — the memory access simply took longer than usual.

The performance implications are dramatic. A typical memory access takes on the order of 100 nanoseconds. A page fault that requires reading from an SSD takes roughly 100 microseconds — a thousand times slower. On a spinning hard drive, a page fault can take 10 milliseconds — a hundred thousand times slower than a memory access. This means that even a small page fault rate has an outsized effect on performance. If 1 in 1,000 memory accesses faults, performance drops by roughly a factor of 100. The system can tolerate occasional faults (cold start faults when a program first runs, for example), but sustained high fault rates indicate a problem.

**Thrashing** occurs when the system's combined working sets — the pages actively being used by all running processes — exceed physical memory. The OS pages out frames to make room for faulting pages, but those evicted frames are needed again almost immediately, triggering more faults. The system spends most of its time servicing page faults rather than doing useful work, and throughput collapses. The solution is to reduce the number of active processes, add physical memory, or improve locality of reference in the application. Understanding the page fault mechanism connects virtual memory (the abstraction) to real performance (the cost of that abstraction when it breaks down).
