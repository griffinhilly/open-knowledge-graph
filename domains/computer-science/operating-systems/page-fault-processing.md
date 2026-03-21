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
stage: advanced
status: draft
---

# Page Fault Handling and Recovery

## Core Idea
A page fault occurs when a process accesses a non-resident page. The handler finds or allocates the page, evicts a victim if needed, performs disk I/O, updates page tables, and resumes. Replacement policy (LRU, FIFO) significantly affects performance.

## Questions

```yaml
- question: "A process reads a virtual address whose page table entry has the valid bit clear, but the page was legitimately allocated and simply swapped to disk. After the OS handles this, what happens next?"
  type: multiple-choice
  options:
    - "The process receives a SIGSEGV signal and terminates"
    - "The OS loads the page into memory, updates the page table, and the faulting instruction is retried transparently"
    - "The OS loads the page but restarts the entire process from scratch"
    - "The process must explicitly re-issue the memory access after the OS notifies it"
  answer: 1
  explanation: "A valid page fault (the page exists but is not resident) is handled entirely by the OS without the process's knowledge. The handler loads the page, updates the page table entry (setting the valid bit and physical frame address), marks the process as runnable, and when the process is next scheduled, the CPU retries the exact instruction that caused the fault — which now succeeds. SIGSEGV only results from an illegal access (a virtual address the process never allocated)."

- question: "A system is thrashing. Which best explains why thrashing is so catastrophic for performance?"
  type: multiple-choice
  options:
    - "Thrashing causes the CPU to overheat because it is running too many processes simultaneously"
    - "Pages are written to disk faster than the disk can handle, causing data corruption"
    - "The CPU spends most of its time waiting for disk I/O to service page faults, doing almost no useful computation"
    - "Thrashing forces the OS to restart processes, losing their in-memory state"
  answer: 2
  explanation: "A page fault costs roughly 10 milliseconds of disk I/O, while a memory access takes ~100 nanoseconds — a 100,000× difference. When thrashing, a process's working set does not fit in physical memory, so nearly every memory access faults. The CPU blocks waiting for disk, spends almost no time executing user instructions, and throughput collapses. No data corruption or process restart occurs — thrashing is a pure performance disaster."

- question: "After the OS handles a valid page fault, the instruction that triggered the fault must be re-executed by the processor."
  type: true-false
  answer: true
  explanation: "The page fault handler brings the missing page into memory and updates the page table, but the original instruction was aborted when the fault occurred and cannot be simply resumed. The hardware retries the faulting instruction from the beginning once the handler returns. This 'restartable instruction' property is essential to virtual memory: the process is unaware a fault occurred, and the instruction proceeds as if the page had been in memory all along."

- question: "Every page fault, regardless of type, results in a disk read to load the missing page."
  type: true-false
  answer: false
  explanation: "Not all page faults involve a disk read. Demand-zero pages — freshly allocated anonymous memory pages never previously written — have no content on disk; the OS simply allocates a free frame and zeroes it. Additionally, if a victim page chosen for eviction has a clean dirty bit (never modified since being loaded), no write-back is needed. The common valid page fault does require a disk read, but 'every page fault' always does is false."

- question: "Why does the OS block the faulting process and switch to a different process while waiting for the disk I/O that services a page fault?"
  type: short-answer
  answer: "Disk I/O takes roughly 10 milliseconds — about 100,000 times longer than a memory access. Keeping the CPU idle while waiting would waste enormous processing time. By blocking the faulting process and scheduling another ready process, the OS keeps the CPU productive throughout the I/O wait. When the disk transfer completes (via interrupt), the handler marks the faulting process as ready, and it resumes the next time it is scheduled."
  explanation: "This is the OS's fundamental strategy for tolerating I/O latency: overlap computation and I/O. The page fault handler initiates the disk read and immediately yields the CPU to the scheduler rather than busy-waiting. Under moderate load, this means other processes make progress during every page fault. Under heavy load where many processes are faulting simultaneously (thrashing), every process is blocked waiting for disk and throughput collapses — illustrating how the strategy fails under pathological conditions."
```

## Explainer

From your study of virtual address translation, you know that each virtual address is mapped to a physical frame through a page table, and that the page table entry contains a **valid bit** indicating whether the page is currently in physical memory. From your understanding of exception handling in the OS, you know that hardware can trap into the kernel when something goes wrong during instruction execution. A **page fault** connects these two concepts: when the CPU tries to translate a virtual address and finds the valid bit is clear, it raises a page fault exception, transferring control to the kernel's page fault handler.

The page fault handler must determine why the page is not resident and respond appropriately. Not all page faults are equal. An **illegal access** — the process is trying to read memory it never allocated — results in a segmentation fault and process termination. But the common case is a **valid page fault**: the page belongs to the process but has been swapped out to disk or has never been loaded (for example, a page of a memory-mapped file being accessed for the first time). In this case, the handler must bring the page into physical memory so the process can continue.

The handler follows a specific sequence. First, it identifies which virtual page caused the fault and locates the page's data on disk (in the swap area or in a file). Next, it finds a free physical frame. If no free frame is available, the handler must choose a **victim page** to evict — this is where the **page replacement policy** comes in. Policies like **LRU** (Least Recently Used) evict the page that has gone longest without being accessed, betting that past access patterns predict future ones. **FIFO** evicts the oldest page, which is simpler to implement but can evict frequently used pages. If the victim page has been modified (its **dirty bit** is set), it must be written back to disk before its frame can be reused; if it is clean, the frame can be reclaimed immediately.

Once a frame is available, the handler initiates a disk read to load the faulted page into the frame. This I/O operation takes milliseconds — an eternity compared to nanosecond memory accesses — so the handler blocks the faulting process and switches to another ready process while the I/O completes. When the disk transfer finishes, the handler updates the page table to point the virtual page at the new frame, sets the valid bit, and marks the faulting process as ready to run. The next time that process is scheduled, the CPU retries the instruction that caused the fault, this time finding a valid mapping and proceeding normally.

The performance of virtual memory depends critically on keeping page faults rare. Each fault costs disk I/O — roughly 10 milliseconds — while a normal memory access takes roughly 100 nanoseconds. A page fault is therefore about 100,000 times slower than a memory hit. Even a fault rate of one in a thousand memory accesses would slow a program dramatically. This is why the choice of replacement policy matters so much: a good policy keeps the process's **working set** — the pages it is actively using — resident in memory, making faults rare. A poor policy evicts pages that will be needed again soon, causing a cascade of faults known as **thrashing** that can bring a system to its knees.
