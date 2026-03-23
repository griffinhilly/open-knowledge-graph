---
id: page-replacement-algorithms-lru-fifo
title: 'Page Replacement Algorithms: LRU and FIFO'
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-paging
  type: hard
builds-toward:
- virtual-memory-and-demand-paging
tags:
- page-replacement
- memory-management
- cache-simulation
stage: formal-systems
status: validated
---

# Page Replacement Algorithms: LRU and FIFO

## Core Idea
When physical memory is full, the OS must choose a page to evict. FIFO (First-In-First-Out) evicts the oldest page; LRU (Least-Recently-Used) evicts the least-recently-accessed page. Optimal (Belady's) is infeasible but serves as a benchmark. Page replacement is central to virtual memory performance and system responsiveness.

## Common Misconceptions
LRU is always optimal (Belady's algorithm is; LRU approximates it well in practice). More memory always improves performance (Belady's anomaly shows FIFO can degrade with more memory for some workloads).

## Questions

```yaml
- question: "A process repeatedly accesses a hot code page that was loaded at program startup, 10 minutes ago, while 500 other pages have been loaded and evicted since. Which replacement algorithm is most likely to evict this hot page when memory is tight?"
  type: multiple-choice
  options:
    - "LRU, because the page has not been recently accessed relative to current working set"
    - "FIFO, because the page has been in memory the longest and is first in the eviction queue"
    - "OPT, because it will predict the page is needed soon and protect it"
    - "Both FIFO and LRU equally, since both track page age"
  answer: 1
  explanation: "FIFO evicts based on load order, not recency of use. A page loaded at startup will be at the front of the FIFO queue regardless of how frequently it is accessed. LRU, by contrast, tracks when a page was last *used* — a hot page that was accessed recently would be protected. This is the core failure of FIFO: it conflates 'old' with 'unneeded.'"

- question: "You are given the same reference string run against FIFO with 3 frames and then with 4 frames. Which statement correctly describes what Belady's anomaly demonstrates?"
  type: multiple-choice
  options:
    - "LRU also suffers from Belady's anomaly, making it unreliable with varying frame counts"
    - "More physical frames always reduce page faults under any replacement algorithm"
    - "For FIFO, some reference strings produce more page faults with 4 frames than with 3 — showing that FIFO's eviction logic is disconnected from actual usage patterns"
    - "Belady's anomaly only occurs when the reference string has no temporal locality"
  answer: 2
  explanation: "Belady's anomaly is unique to FIFO (and some other non-stack algorithms). With more frames, FIFO may keep different pages in memory, and for certain reference strings, this set performs worse. LRU does not suffer from this anomaly because it has the 'stack property': the set of pages in memory with k+1 frames always contains the set kept with k frames. The anomaly reveals that FIFO's eviction criterion (age) is fundamentally at odds with usefulness."

- question: "LRU is the theoretically optimal page replacement algorithm for minimizing page faults."
  type: true-false
  answer: false
  explanation: "The theoretically optimal algorithm is Belady's OPT: evict the page that will not be used for the longest time in the future. OPT achieves the minimum possible page faults but requires knowledge of future accesses, making it impossible to implement in a real system. LRU is a practical approximation that performs close to optimal for most real workloads because temporal locality makes recent history a good proxy for future access — but it is not optimal."

- question: "More physical memory (more frames) can sometimes increase the number of page faults when using FIFO page replacement."
  type: true-false
  answer: true
  explanation: "This is Belady's anomaly. For certain reference strings, FIFO with n+1 frames produces more faults than FIFO with n frames. The anomaly arises because FIFO lacks the stack property: adding a frame changes *which* pages are retained, and for some workloads the new selection performs worse. LRU does not suffer from this — adding frames always reduces or maintains the page fault rate under LRU."

- question: "Why does LRU typically outperform FIFO in practice? What property of real program behavior does LRU exploit that FIFO ignores?"
  type: short-answer
  answer: "LRU exploits temporal locality — the observation that pages accessed recently are very likely to be accessed again soon. By always evicting the least-recently-used page, LRU keeps the active working set in memory. FIFO ignores recency entirely, evicting based on load order, which means it can evict heavily-used pages simply because they were loaded early. For programs with stable working sets (typical of loops, frequently-called functions, and hot data), LRU's recency heuristic closely approximates the optimal strategy, while FIFO's age-based heuristic does not."
  explanation: "The gap between FIFO and LRU is most dramatic when the working set fits in memory but exceeds the frame count by a small margin. In that regime, LRU retains the active working set while FIFO churns through old-but-useful pages, producing many unnecessary faults."
```

## Explainer

From your study of paging, you know that the OS divides physical memory into fixed-size **frames** and virtual memory into **pages**, and that a page table maps virtual pages to physical frames. When a program accesses a page that is not currently in physical memory, a **page fault** occurs, and the OS must load that page from disk. But if all physical frames are already occupied, the OS must first choose a victim page to **evict**. The algorithm that makes this choice is the **page replacement algorithm**, and its quality directly determines how often programs stall waiting for disk I/O.

The simplest approach is **FIFO** (First-In-First-Out): evict the page that has been in memory the longest. Imagine a queue of pages — when a new page arrives and memory is full, the page at the front of the queue is kicked out. FIFO is trivial to implement (just maintain a circular pointer through the frames), but it makes a poor assumption: that the oldest page is the least useful. A page loaded early might be a frequently accessed code page or a hot data structure — FIFO will evict it anyway. Even worse, FIFO suffers from **Belady's anomaly**: there exist reference strings where giving the algorithm *more* physical frames actually *increases* the number of page faults. This counterintuitive result shows that FIFO's eviction logic is fundamentally disconnected from actual usage patterns.

**LRU** (Least Recently Used) takes a smarter approach: evict the page that has gone the longest without being accessed. The intuition comes from **temporal locality** — if a page was used recently, it is likely to be used again soon. LRU exploits this by always sacrificing the page whose last access is furthest in the past. In practice, LRU performs close to optimal for most workloads and does not suffer from Belady's anomaly. The difficulty is implementation: true LRU requires recording the time of every memory access, which would add unacceptable overhead if done in software for every instruction. Hardware support (reference bits, counters) and approximation algorithms (like the **clock algorithm**, which uses a circular buffer with reference bits) make LRU practical.

The theoretical benchmark is **Belady's optimal algorithm** (OPT): evict the page that will not be used for the longest time in the future. OPT is impossible to implement in a real system because it requires knowledge of future memory accesses, but it serves as a lower bound on page faults. When evaluating LRU or FIFO, you compare their fault rates against OPT on the same reference string. LRU typically comes within a few percent of OPT, while FIFO can be substantially worse. This is why virtually all modern operating systems use LRU approximations — the clock algorithm in Linux, for instance — as their default page replacement strategy.
