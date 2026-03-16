---
id: page-fault-processing
title: Page Fault Handling and Recovery
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-address-translation-scheme
  type: hard
- id: exception-handling-os-internals
  type: hard
builds-toward:
- working-set-model
tags:
- page-faults
- virtual-memory
- handling
stage: formal-systems
status: draft
---

# Page Fault Handling and Recovery

## Core Idea
A page fault occurs when a process accesses a non-resident page. The handler finds or allocates the page, evicts a victim if needed, performs disk I/O, updates page tables, and resumes. Replacement policy (LRU, FIFO) significantly affects performance.

## Explainer

From your study of virtual address translation, you know that each virtual address is mapped to a physical frame through a page table, and that the page table entry contains a **valid bit** indicating whether the page is currently in physical memory. From your understanding of exception handling in the OS, you know that hardware can trap into the kernel when something goes wrong during instruction execution. A **page fault** connects these two concepts: when the CPU tries to translate a virtual address and finds the valid bit is clear, it raises a page fault exception, transferring control to the kernel's page fault handler.

The page fault handler must determine why the page is not resident and respond appropriately. Not all page faults are equal. An **illegal access** — the process is trying to read memory it never allocated — results in a segmentation fault and process termination. But the common case is a **valid page fault**: the page belongs to the process but has been swapped out to disk or has never been loaded (for example, a page of a memory-mapped file being accessed for the first time). In this case, the handler must bring the page into physical memory so the process can continue.

The handler follows a specific sequence. First, it identifies which virtual page caused the fault and locates the page's data on disk (in the swap area or in a file). Next, it finds a free physical frame. If no free frame is available, the handler must choose a **victim page** to evict — this is where the **page replacement policy** comes in. Policies like **LRU** (Least Recently Used) evict the page that has gone longest without being accessed, betting that past access patterns predict future ones. **FIFO** evicts the oldest page, which is simpler to implement but can evict frequently used pages. If the victim page has been modified (its **dirty bit** is set), it must be written back to disk before its frame can be reused; if it is clean, the frame can be reclaimed immediately.

Once a frame is available, the handler initiates a disk read to load the faulted page into the frame. This I/O operation takes milliseconds — an eternity compared to nanosecond memory accesses — so the handler blocks the faulting process and switches to another ready process while the I/O completes. When the disk transfer finishes, the handler updates the page table to point the virtual page at the new frame, sets the valid bit, and marks the faulting process as ready to run. The next time that process is scheduled, the CPU retries the instruction that caused the fault, this time finding a valid mapping and proceeding normally.

The performance of virtual memory depends critically on keeping page faults rare. Each fault costs disk I/O — roughly 10 milliseconds — while a normal memory access takes roughly 100 nanoseconds. A page fault is therefore about 100,000 times slower than a memory hit. Even a fault rate of one in a thousand memory accesses would slow a program dramatically. This is why the choice of replacement policy matters so much: a good policy keeps the process's **working set** — the pages it is actively using — resident in memory, making faults rare. A poor policy evicts pages that will be needed again soon, causing a cascade of faults known as **thrashing** that can bring a system to its knees.
