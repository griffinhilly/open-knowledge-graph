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
status: draft
---

# Page Replacement Algorithms: LRU and FIFO

## Core Idea
When physical memory is full, the OS must choose a page to evict. FIFO (First-In-First-Out) evicts the oldest page; LRU (Least-Recently-Used) evicts the least-recently-accessed page. Optimal (Belady's) is infeasible but serves as a benchmark. Page replacement is central to virtual memory performance and system responsiveness.

## Common Misconceptions
LRU is always optimal (Belady's algorithm is; LRU approximates it well in practice). More memory always improves performance (Belady's anomaly shows FIFO can degrade with more memory for some workloads).

## Explainer

From your study of paging, you know that the OS divides physical memory into fixed-size **frames** and virtual memory into **pages**, and that a page table maps virtual pages to physical frames. When a program accesses a page that is not currently in physical memory, a **page fault** occurs, and the OS must load that page from disk. But if all physical frames are already occupied, the OS must first choose a victim page to **evict**. The algorithm that makes this choice is the **page replacement algorithm**, and its quality directly determines how often programs stall waiting for disk I/O.

The simplest approach is **FIFO** (First-In-First-Out): evict the page that has been in memory the longest. Imagine a queue of pages — when a new page arrives and memory is full, the page at the front of the queue is kicked out. FIFO is trivial to implement (just maintain a circular pointer through the frames), but it makes a poor assumption: that the oldest page is the least useful. A page loaded early might be a frequently accessed code page or a hot data structure — FIFO will evict it anyway. Even worse, FIFO suffers from **Belady's anomaly**: there exist reference strings where giving the algorithm *more* physical frames actually *increases* the number of page faults. This counterintuitive result shows that FIFO's eviction logic is fundamentally disconnected from actual usage patterns.

**LRU** (Least Recently Used) takes a smarter approach: evict the page that has gone the longest without being accessed. The intuition comes from **temporal locality** — if a page was used recently, it is likely to be used again soon. LRU exploits this by always sacrificing the page whose last access is furthest in the past. In practice, LRU performs close to optimal for most workloads and does not suffer from Belady's anomaly. The difficulty is implementation: true LRU requires recording the time of every memory access, which would add unacceptable overhead if done in software for every instruction. Hardware support (reference bits, counters) and approximation algorithms (like the **clock algorithm**, which uses a circular buffer with reference bits) make LRU practical.

The theoretical benchmark is **Belady's optimal algorithm** (OPT): evict the page that will not be used for the longest time in the future. OPT is impossible to implement in a real system because it requires knowledge of future memory accesses, but it serves as a lower bound on page faults. When evaluating LRU or FIFO, you compare their fault rates against OPT on the same reference string. LRU typically comes within a few percent of OPT, while FIFO can be substantially worse. This is why virtually all modern operating systems use LRU approximations — the clock algorithm in Linux, for instance — as their default page replacement strategy.
