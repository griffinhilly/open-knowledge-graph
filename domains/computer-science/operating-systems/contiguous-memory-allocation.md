---
id: contiguous-memory-allocation
title: Contiguous Memory Allocation and Fragmentation
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
builds-toward:
- paging
- segmentation
tags:
- fragmentation
- fixed-partition
- variable-partition
- first-fit
- best-fit
- worst-fit
stage: formal-systems
status: validated
---

# Contiguous Memory Allocation and Fragmentation

## Core Idea
The simplest memory allocation scheme places each process in a single contiguous region of physical memory. Fixed-partition schemes divide RAM into fixed-size regions (suffering internal fragmentation when a process is smaller than its partition), while variable-partition schemes allocate exactly what is needed (suffering external fragmentation — enough total free memory exists, but it is scattered in small non-contiguous holes). Allocation policies — First-Fit (allocate first hole large enough), Best-Fit (smallest hole that works), and Worst-Fit (largest hole) — trade off allocation speed against fragmentation. Compaction, relocating all processes to consolidate free space, is expensive and requires execution-time address binding.

## Common Misconceptions
- Best-Fit does not always result in least fragmentation in practice; First-Fit is often competitive and faster.
- External fragmentation is not fixable by compaction alone; paging eliminates it structurally.

## Questions

```yaml
- question: "A system uses variable-partition memory allocation. Currently, free memory consists of three holes: 60 KB, 50 KB, and 40 KB — 150 KB total. A new process requiring 120 KB arrives. What happens?"
  type: multiple-choice
  options:
    - "The process is allocated across the 60 KB and 50 KB holes using non-contiguous allocation"
    - "The process cannot be allocated because no single contiguous hole is large enough — this is external fragmentation"
    - "The OS performs compaction automatically and then allocates the process"
    - "The process is allocated to the 60 KB hole with 60 KB of internal fragmentation"
  answer: 1
  explanation: "This is the classic external fragmentation scenario: enough total free memory (150 KB > 120 KB needed) exists, but no single contiguous region is large enough. Under contiguous allocation, a process must reside in one unbroken block — so the 120 KB process cannot be placed. Automatic compaction (option C) is not assumed — it is expensive and must be explicitly invoked. Option D confuses the problem type: internal fragmentation occurs within an allocated block, not when a process is refused due to hole-size mismatch."

- question: "Why is First-Fit often preferred over Best-Fit in practice, despite Best-Fit selecting the smallest hole that fits a process?"
  type: multiple-choice
  options:
    - "First-Fit is faster to implement and requires less memory for bookkeeping"
    - "Best-Fit creates many tiny residual holes that are too small to be useful, producing more total unusable fragmentation"
    - "First-Fit always leaves larger free holes available for future large processes"
    - "Best-Fit is incompatible with variable-partition allocation schemes"
  answer: 1
  explanation: "Best-Fit sounds optimal — taking the smallest sufficient hole minimizes waste per allocation. But in practice, it creates many tiny leftover fragments (the unused remainder after a best-fit allocation) that are too small for any practical future request. These tiny holes accumulate and are effectively unusable. First-Fit, despite selecting holes less 'efficiently,' often leaves larger residual spaces that can accommodate future requests. In practice, First-Fit is faster (doesn't require scanning all holes) and produces comparable or better actual utilization. The locally optimal choice produces globally worse outcomes — a counterintuitive but important result."

- question: "Fixed-partition memory allocation suffers from internal fragmentation but is immune to external fragmentation."
  type: true-false
  answer: true
  explanation: "This is correct. In fixed-partition allocation, memory is divided into predetermined regions at boot time, and each process gets exactly one partition. Internal fragmentation occurs when a process is smaller than its partition — the unused space inside is wasted. But because partition boundaries are fixed and each partition is either fully allocated or fully free, there are no 'holes' between allocations — which is what external fragmentation requires. External fragmentation is specifically a variable-partition problem, where allocated and freed regions of different sizes create a patchwork of unusable gaps."

- question: "Best-Fit allocation consistently produces less total memory fragmentation than First-Fit in practice."
  type: true-false
  answer: false
  explanation: "Despite the intuitive appeal, empirical studies and simulations consistently show that Best-Fit does not reliably outperform First-Fit in practice. Best-Fit's selection of the smallest sufficient hole leaves many tiny residual fragments that are practically unusable, eventually filling memory with slivers no process can use. First-Fit tends to leave larger residual regions. Neither strategy eliminates external fragmentation, and neither consistently dominates the other across all workloads. The intuitively 'best' local strategy is not empirically the best global strategy."

- question: "Explain why compaction addresses external fragmentation but is not a complete solution, and what structural change paging makes to eliminate external fragmentation entirely."
  type: short-answer
  answer: "Compaction physically relocates all processes to consolidate free space into one contiguous region. It works but has three limitations: (1) it is expensive — every byte of occupied memory may need to be copied; (2) all processes must pause during compaction; (3) it requires addresses to be rebound at runtime, which not all systems support. Most importantly, it is reactive — fragmentation recurs after more allocations. Paging eliminates external fragmentation structurally by removing the contiguity requirement: a process's logical address space is divided into fixed-size pages that map to any available physical frames regardless of location. Because any page can go anywhere, no space is ever 'too small' due to non-contiguity."
  explanation: "This is the 'why paging exists' insight. Paging isn't just a different allocation strategy — it's a structural escape from the contiguity constraint that makes fragmentation inevitable. Understanding the fragmentation problems of contiguous allocation is precisely what makes the motivation for paging clear rather than arbitrary."
```

## Explainer

From your study of memory management basics, you know the OS must decide where in physical memory to place each process. The simplest approach is **contiguous allocation**: give each process a single unbroken block of memory. This is easy to implement — the OS just needs to track the start address and size of each allocation — and it makes address translation trivial (add the base address to every logical address). But contiguous allocation creates a fundamental tension between simplicity and efficient use of memory.

**Fixed partitioning** divides physical memory into slots of predetermined size at boot time. Process A gets partition 1, process B gets partition 2, and so on. The problem is obvious: if a process needs 60 KB but the smallest available partition is 256 KB, the remaining 196 KB is wasted. This waste inside an allocated region is called **internal fragmentation**. You cannot give that leftover space to another process because the partition boundaries are fixed. It is like assigning each family a standardized apartment — a single occupant gets the same space as a family of four.

**Variable partitioning** eliminates internal fragmentation by allocating exactly the amount of memory each process needs. But it introduces a different problem. As processes start and finish in unpredictable order, memory becomes a patchwork of allocated blocks and free holes. Eventually you might have 100 KB free total, but split across three non-adjacent holes of 40 KB, 35 KB, and 25 KB — none large enough for a new 80 KB process. This is **external fragmentation**: enough total free memory exists, but no single contiguous block is large enough. The allocation policy determines how severe this gets. **First-Fit** scans from the beginning and takes the first hole that is large enough — fast, but can clutter the front of memory. **Best-Fit** finds the smallest sufficient hole — minimizes leftover scraps per allocation but creates many tiny unusable fragments. **Worst-Fit** takes the largest hole, hoping the remainder is still useful — but in practice performs poorly because it rapidly consumes the few large blocks.

The OS can fight external fragmentation through **compaction**: pausing all processes, sliding their memory blocks together to consolidate free space, and updating all their base addresses. This works but is expensive — every byte of occupied memory might need to move, and all processes must be paused during the shuffle. Compaction also requires that addresses can be rebound at runtime (dynamic address binding), which not all systems support. These limitations are precisely why operating systems moved beyond contiguous allocation to **paging**, which you will study next. Paging solves external fragmentation entirely by breaking memory into small fixed-size frames and allowing a process's logical address space to map to non-contiguous physical frames — but understanding why paging exists requires first understanding the fragmentation problems that contiguous allocation cannot escape.
