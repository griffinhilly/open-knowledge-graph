---
id: page-replacement-algorithms
title: Page Replacement Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-management
  type: hard
- id: cache-replacement-policies
  type: soft
builds-toward:
- thrashing-and-working-set
tags:
- page-replacement
- FIFO
- LRU
- optimal
- clock-algorithm
- Belady-anomaly
stage: formal-systems
status: validated
---

# Page Replacement Algorithms

## Core Idea
When a page fault occurs and no free frames exist, the OS must evict a page — the page replacement algorithm chooses which one. The Optimal algorithm (OPT) evicts the page that will be used furthest in the future, minimizing page faults, but requires future knowledge so it serves only as a theoretical benchmark. FIFO evicts the oldest page but exhibits Belady's Anomaly (more frames can cause more faults). LRU (Least Recently Used) approximates OPT by evicting the page unused longest and is well-supported by the principle of temporal locality. The Clock (Second-Chance) algorithm approximates LRU efficiently using a reference bit and a circular scan, and is widely used in practice.

## How It's Best Learned
Apply each algorithm to the same reference string (e.g., 1,2,3,4,1,2,5,1,2,3,4,5) with 3 frames, counting page faults. Then verify Belady's anomaly by running FIFO with 4 frames on the same string.

## Common Misconceptions
- LRU cannot be implemented exactly in hardware because tracking the exact access order for all pages is too expensive; approximations are used.
- More physical frames always reduce page faults for LRU and OPT, but not necessarily for FIFO (Belady's Anomaly).

## Explainer

From virtual memory management, you know that a process's address space can be larger than physical memory. The OS maps virtual pages to physical frames, and when a process accesses a page that is not currently in memory, a **page fault** occurs and the OS must load that page from disk. If all physical frames are already occupied, the OS must **evict** one page to make room. The page replacement algorithm decides which page gets evicted — and this choice has a dramatic effect on performance, because a bad choice means the evicted page will be needed again soon, causing another expensive page fault.

The **Optimal algorithm** (OPT, also called Belady's algorithm) provides the theoretical best answer: evict the page that will not be used for the longest time in the future. If page A will next be accessed in 100 instructions and page B will next be accessed in 5 instructions, evict A. This minimizes total page faults, but it requires knowing the future access pattern — impossible in a real system. OPT serves as a benchmark: you can run it on a recorded trace to see how close your real algorithm comes to the theoretical minimum.

**FIFO** (First-In, First-Out) is the simplest practical algorithm: evict the page that has been in memory the longest. It requires only a queue — load a page, push it to the back; evict from the front. FIFO is easy to implement but performs poorly because "oldest" does not mean "least useful." A page loaded long ago might be accessed constantly (think: a loop's code page). FIFO's most surprising property is **Belady's Anomaly**: increasing the number of available frames can actually *increase* page faults for certain reference strings. This is counterintuitive — more memory should help — and it reveals that FIFO's eviction criterion is fundamentally misaligned with what matters (recency of use, not age of loading).

**LRU** (Least Recently Used) fixes this by evicting the page that has gone the longest *without being accessed*. The reasoning comes from **temporal locality**, a principle you know from cache replacement: if a page was used recently, it is likely to be used again soon. LRU never exhibits Belady's Anomaly and closely approximates OPT in practice. However, exact LRU is expensive — tracking the precise access order of all pages requires either a timestamp on every memory access or maintaining a stack of page numbers, both of which are prohibitively costly in hardware. This is why real systems use **approximations**. The **Clock algorithm** (Second-Chance) is the most common: each page has a **reference bit** set by hardware whenever the page is accessed. The algorithm sweeps through pages in a circle. If a page's reference bit is 1, it gets a "second chance" — the bit is cleared and the algorithm moves on. If the bit is 0, that page has not been accessed since the last sweep and is evicted. Clock approximates LRU with minimal overhead — just one bit per page and a circular pointer — making it the algorithm most widely deployed in real operating systems.
