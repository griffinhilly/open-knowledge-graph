---
id: contiguous-allocation-strategies
title: Contiguous Memory Allocation Strategies
domain: computer-science
course: operating-systems
prerequisites:
- id: contiguous-memory-allocation
  type: hard
- id: memory-layout-and-address-binding
  type: hard
builds-toward:
- virtual-address-translation-scheme
tags:
- memory-management
- allocation
- contiguous
stage: formal-systems
status: validated
---

# Contiguous Memory Allocation Strategies

## Core Idea
Contiguous allocation assigns each process a single contiguous RAM region. Allocation algorithms (first-fit, best-fit, worst-fit) balance speed and fragmentation. External fragmentation accumulates; compaction (expensive) or non-contiguous schemes (paging) address this.

## Questions

```yaml
- question: "A system has 100 MB of total free memory, divided into twenty 5 MB holes scattered throughout RAM. A new process requests 10 MB of contiguous memory. What happens under any contiguous allocation strategy?"
  type: multiple-choice
  options:
    - "Best-fit will combine adjacent 5 MB holes to satisfy the 10 MB request"
    - "First-fit will find a 10 MB region by scanning from the beginning of memory"
    - "The process cannot be loaded, even though total free memory exceeds the request"
    - "Worst-fit will carve 10 MB from the largest hole available"
  answer: 2
  explanation: "This is the essence of external fragmentation: total free memory may be sufficient, but if no single contiguous hole is large enough, the request cannot be satisfied. Contiguous allocation requires a single unbroken block — it cannot combine multiple smaller holes. None of the three strategies (first-fit, best-fit, worst-fit) can merge non-adjacent holes. The process fails to load despite 100 MB being free. This is why external fragmentation is described as the fundamental weakness of contiguous allocation."

- question: "Which allocation strategy tends to produce the most numerous tiny, unusable memory fragments over time, even though it minimizes wasted space in each individual allocation?"
  type: multiple-choice
  options:
    - "First-fit — because it always grabs the first available hole, leaving large fragments at the start"
    - "Worst-fit — because it fragments the largest holes most aggressively"
    - "Best-fit — because minimizing each leftover fragment produces many small slivers that accumulate"
    - "All three strategies produce equal fragmentation over time"
  answer: 2
  explanation: "Best-fit's local optimality is its global weakness. By always choosing the smallest adequate hole, best-fit minimizes the leftover from each allocation — but those leftovers are often too small to satisfy any future request. Over many allocations and deallocations, memory fills with tiny unusable fragments. First-fit actually performs comparably to best-fit overall, and worst-fit performs poorly because it destroys the large holes that could serve big requests. Empirical studies show best-fit's precise hole selection does not reduce overall fragmentation compared to first-fit."

- question: "External fragmentation can cause a process to fail to load even when the total free memory in the system is larger than the process's memory requirement."
  type: true-false
  answer: true
  explanation: "True. This is the defining characteristic of external fragmentation. Contiguous allocation requires a single unbroken physical memory block. If free memory is scattered across many small holes — even if their total size exceeds the process's needs — no individual hole may be large enough. The 50-percent rule quantifies this: with first-fit allocation, roughly one-third of memory is lost to unusable fragments on average. This is why paging was developed: by allowing a process to occupy non-contiguous frames, paging eliminates external fragmentation entirely."

- question: "Choosing the best-fit allocation strategy eliminates external fragmentation because it always minimizes the wasted space left after each allocation."
  type: true-false
  answer: false
  explanation: "False. Best-fit minimizes the leftover fragment from each individual allocation, but this local optimization makes overall fragmentation worse, not better. The tiny leftover slivers from best-fit allocations are often too small to be useful for any future request, accumulating as waste. External fragmentation is a systemic property of contiguous allocation — it arises from the combination of varying allocation sizes and the unpredictability of deallocation order. No placement strategy (first-fit, best-fit, or worst-fit) eliminates it; only architectural changes like paging can do so."

- question: "Explain the difference between external fragmentation and internal fragmentation, and why external fragmentation is not solved simply by switching from first-fit to best-fit allocation."
  type: short-answer
  answer: "External fragmentation: free memory is divided into many small holes scattered between allocated regions; total free space may be sufficient, but no single contiguous hole is large enough for a new request. Internal fragmentation: allocated memory blocks are slightly larger than needed, wasting space inside allocated regions (common with fixed-size partitions or page-based allocation). External fragmentation cannot be solved by choosing a better placement strategy because the problem is structural — any strategy that allows variable-size allocations and deallocations in unpredictable order will eventually produce scattered holes. Best-fit reduces individual waste per allocation but produces more tiny fragments overall. The only architectural solution is compaction (expensive) or switching to non-contiguous allocation (paging)."
  explanation: "The deeper point is that the three strategies differ in performance, not in kind — they all share the external fragmentation problem. This motivated the development of paging, which trades external fragmentation for a small amount of internal fragmentation (partial last pages) while enabling efficient memory use through non-contiguous placement."
```

## Explainer

From your study of contiguous memory allocation and address binding, you know that each process needs a region of physical memory to hold its code, data, and stack, and that the OS must decide where in memory each process goes. When the scheme requires each process to occupy a single unbroken block of addresses, the OS faces a classic placement problem: given a set of free memory holes of various sizes and a new process requesting a specific amount, which hole should it choose?

Three strategies dominate this decision. **First-fit** scans the list of free holes from the beginning and picks the first one large enough to hold the process. It is fast because it stops searching as soon as it finds a match, but it tends to leave small leftover fragments near the beginning of memory. **Best-fit** scans the entire list and picks the smallest hole that is large enough. This minimizes the leftover fragment from each allocation but is slower (it must examine every hole) and tends to create many tiny unusable fragments scattered throughout memory. **Worst-fit** picks the largest available hole, reasoning that the remaining fragment will be large enough to be useful. In practice, worst-fit performs poorly because it rapidly eliminates the large holes that could have served bigger requests later.

The fundamental problem all three strategies share is **external fragmentation**: after a sequence of allocations and deallocations, free memory becomes scattered across many small non-contiguous holes. The total free memory may be large enough for a new process, but no single contiguous block is. For example, imagine 100 MB of free memory split into twenty 5 MB holes — a process needing 20 MB cannot be loaded even though 100 MB is available. Empirical studies and the **50-percent rule** suggest that with first-fit allocation, roughly one-third of memory is lost to fragmentation on average.

**Compaction** can solve external fragmentation by relocating processes to pack them together, creating one large free block. But compaction requires relocatable addresses (base-and-limit registers or relocation hardware), and it is expensive — every byte of every relocated process must be copied and its base address updated. This is why contiguous allocation has been largely superseded by **paging**, which breaks processes into fixed-size pages that can be placed in any available frame of physical memory, eliminating external fragmentation entirely. Understanding contiguous allocation strategies matters because they illustrate the tradeoffs that motivated the move to paging and because the same first-fit/best-fit/worst-fit logic reappears in heap allocators (malloc), disk block allocation, and any resource placement problem.
