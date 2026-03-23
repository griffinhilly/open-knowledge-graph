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
status: validated
---

# Demand Paging and Page Faults

## Core Idea
Demand paging loads pages into memory only when accessed, reducing memory pressure and enabling programs larger than physical RAM. A page fault occurs when accessing a page not in memory; the kernel fetches it from disk and resumes execution. Frequent page faults (thrashing) severely degrade performance and indicate excessive memory overcommitment or poor working set behavior.

## Questions

```yaml
- question: "A process accesses a valid virtual address, but that page is not currently in physical memory. Which sequence correctly describes what happens next?"
  type: multiple-choice
  options:
    - "The process immediately crashes with a segmentation fault because the address is not in RAM"
    - "The hardware raises a page fault exception; the kernel allocates a physical frame, loads the page from disk, updates the page table, and restarts the faulting instruction"
    - "The OS terminates the process for attempting to access unmapped memory"
    - "The hardware automatically fetches the page from disk and continues execution without kernel involvement"
  answer: 1
  explanation: "A page fault on a valid virtual address (one that exists in the process's address space but isn't loaded) is a normal, handled event — not a crash. The hardware detects the missing page-table entry and traps to the kernel's page fault handler. The kernel does the work (allocate frame, load page, update table), then returns to user mode and restarts the instruction. The process never 'sees' the fault. A segfault occurs only when the address is genuinely invalid (not mapped to anything in the process's virtual address space)."

- question: "A system is experiencing thrashing. Which explanation best describes the underlying cause?"
  type: multiple-choice
  options:
    - "The CPU is too slow to service page faults efficiently, causing a fault backlog"
    - "The combined working sets of the running processes exceed physical memory, so pages evicted to make room for faults are immediately needed again, causing near-continuous faulting"
    - "The page replacement algorithm is poorly tuned and consistently evicts recently-used pages"
    - "Disk fragmentation has increased page fault service time, creating a performance bottleneck"
  answer: 1
  explanation: "Thrashing is a systemic resource exhaustion problem, not an algorithmic one. When total demand for physical frames exceeds supply, the OS pages something out to satisfy a fault, but the evicted page is needed almost immediately — triggering another fault. The system spirals: it spends more time on page fault handling than on useful work. The fix is structural: reduce the number of active processes, add RAM, or improve application locality. Replacing the replacement algorithm addresses the wrong level."

- question: "A page fault does not necessarily indicate a program error — it is the normal mechanism by which valid pages are loaded into memory on their first access under demand paging."
  type: true-false
  answer: true
  explanation: "Demand paging deliberately defers loading pages until they are needed. The first access to any page that hasn't been loaded yet will fault, and this is expected and correct behavior. Operating systems routinely handle millions of such 'minor' or 'cold-start' page faults during normal operation. Only a page fault on an address outside the process's valid virtual memory region (an invalid access) results in an error signal to the process."

- question: "Demand paging requires that each process's entire virtual address space fit within physical memory, since any page not currently present in RAM will cause the process to crash."
  type: true-false
  answer: false
  explanation: "The entire purpose of demand paging is to allow programs larger than physical RAM. The OS maintains pages on disk (in a swap partition or the executable file itself) and brings them into physical memory only when needed, evicting others if RAM is full. A process may have a 4 GB virtual address space on a machine with 1 GB of RAM — demand paging makes this work as long as the process's active working set (currently needed pages) fits in memory."

- question: "Why does even a small page fault rate — say, 1 fault per 1,000 memory accesses — have such a disproportionately large impact on overall performance?"
  type: short-answer
  answer: "Because the latency gap between a normal memory access (~100 ns) and a page fault requiring disk I/O (~100 μs for SSD, ~10 ms for HDD) is 1,000× to 100,000×. With 1 fault per 1,000 accesses, the average access time becomes (999 × 100 ns + 1 × 100,000 ns) / 1000 ≈ 200 ns — roughly double. Even this small fault rate cuts effective memory performance in half."
  explanation: "Performance analysis: effective access time = (1 − p) × t_mem + p × t_fault, where p is the fault rate. With p = 0.001, t_mem = 100 ns, and t_fault = 100,000 ns (SSD): EAT = 0.999 × 100 + 0.001 × 100,000 = 99.9 + 100 ≈ 200 ns. The fault term (100 ns contribution) equals the entire no-fault memory time. This is why thrashing — where fault rates spike to near 1 — causes throughput to collapse almost entirely."
```

## Explainer

From your study of virtual memory, you know that each process sees a large, private address space mapped through page tables to physical frames. But here is a practical question: when a process starts, does the OS load its entire address space — code, data, stack, heap, shared libraries — into physical memory? For a large application this could be hundreds of megabytes or more, and most of it may never be accessed during a given run. **Demand paging** takes the lazy approach: pages are loaded into physical memory only when the process actually tries to access them, not before.

When a process accesses an address whose page is not currently in physical memory, the hardware triggers a **page fault** — a special exception that transfers control to the kernel's page fault handler. The handler looks up the faulting address in the process's page table to determine what should be there. If the page belongs to the process's valid address space (mapped in its virtual memory layout but not yet loaded), the kernel allocates a free physical frame, reads the page's contents from disk (from the executable file, a swap partition, or a memory-mapped file), updates the page table entry to point to the new frame, and then restarts the instruction that faulted. From the process's perspective, nothing unusual happened — the memory access simply took longer than usual.

The performance implications are dramatic. A typical memory access takes on the order of 100 nanoseconds. A page fault that requires reading from an SSD takes roughly 100 microseconds — a thousand times slower. On a spinning hard drive, a page fault can take 10 milliseconds — a hundred thousand times slower than a memory access. This means that even a small page fault rate has an outsized effect on performance. If 1 in 1,000 memory accesses faults, performance drops by roughly a factor of 100. The system can tolerate occasional faults (cold start faults when a program first runs, for example), but sustained high fault rates indicate a problem.

**Thrashing** occurs when the system's combined working sets — the pages actively being used by all running processes — exceed physical memory. The OS pages out frames to make room for faulting pages, but those evicted frames are needed again almost immediately, triggering more faults. The system spends most of its time servicing page faults rather than doing useful work, and throughput collapses. The solution is to reduce the number of active processes, add physical memory, or improve locality of reference in the application. Understanding the page fault mechanism connects virtual memory (the abstraction) to real performance (the cost of that abstraction when it breaks down).
