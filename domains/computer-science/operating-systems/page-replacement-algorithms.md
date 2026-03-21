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

## Questions

```yaml
- question: "A system using FIFO page replacement with 3 frames produces 10 page faults on a particular reference string. When frames are increased to 4, the same string produces 12 page faults. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The reference string was adversarially constructed — this would not happen with real workloads"
    - "Belady's Anomaly: FIFO can produce more page faults with more physical frames for certain reference strings"
    - "The system has a bug — more frames should always reduce or maintain page faults"
    - "LRU would show the same behavior since it is also affected by the number of frames"
  answer: 1
  explanation: "This is a demonstration of Belady's Anomaly, which affects FIFO and certain other replacement algorithms. Intuitively, more frames should mean fewer evictions, but FIFO's eviction criterion — 'evict the page loaded longest ago' — is not aligned with which pages are actually useful. Adding a frame can change the eviction sequence in a way that, for some reference strings, triggers more total faults. LRU does not exhibit Belady's Anomaly because it is a 'stack algorithm' — with n+1 frames, the set of pages in memory always contains the set that would be in memory with n frames, so adding a frame can only help."

- question: "Why is exact LRU not directly implemented in most real operating systems, despite being a strong approximation of the optimal algorithm?"
  type: multiple-choice
  options:
    - "LRU requires future knowledge of access patterns, just like OPT"
    - "Tracking the exact recency order of all pages requires updating a timestamp or sorted structure on every memory access, which is prohibitively expensive in hardware"
    - "LRU performs worse than FIFO on most real workloads"
    - "LRU requires pages to be sorted by access frequency, not recency"
  answer: 1
  explanation: "LRU's logic is sound — evict the page unused longest — but implementing it exactly requires knowing the precise access order of all pages at all times. This means either recording a timestamp on every memory access and finding the minimum when eviction is needed, or maintaining a stack where the accessed page moves to the top on every reference. Both approaches require hardware support on every memory access, which happens billions of times per second — the overhead is enormous. Instead, hardware provides a single reference bit per page, which the Clock (Second-Chance) algorithm exploits to approximate LRU with minimal cost."

- question: "The Optimal (OPT) page replacement algorithm cannot be implemented in a real operating system."
  type: true-false
  answer: true
  explanation: "OPT evicts the page that will not be used for the longest time in the future, which requires knowing future memory access patterns — impossible during normal execution. The OS only knows which pages have been accessed in the past, not which will be needed next. OPT is therefore used only as a theoretical benchmark: you can apply it retrospectively to a recorded trace to measure how close a practical algorithm comes to the theoretical minimum number of page faults. It is not an implementable policy."

- question: "LRU page replacement can also exhibit Belady's Anomaly — adding more frames can increase page faults — just like FIFO."
  type: true-false
  answer: false
  explanation: "Belady's Anomaly does not affect LRU. LRU is a 'stack algorithm': with n frames, the set of pages in memory is always a subset of the set in memory with n+1 frames for any reference string. This means adding a frame can only keep the same pages or more — it can never cause a useful page to be evicted. FIFO lacks this property because its eviction criterion (age of loading) is not consistently aligned with usefulness; adding a frame can alter the eviction sequence in a way that introduces new faults on some strings. OPT is also a stack algorithm and similarly immune to Belady's Anomaly."

- question: "Explain why the Clock (Second-Chance) algorithm uses a reference bit per page rather than tracking exact access times, and how it approximates LRU."
  type: short-answer
  answer: "Hardware sets the reference bit for a page automatically on every access with zero computational overhead. The Clock algorithm sweeps through pages in a circle: if a page's reference bit is 1, it clears the bit and moves on (giving a 'second chance'); if the bit is 0, the page has not been accessed since the last sweep and is evicted. This approximates LRU because a page with reference bit = 0 has gone at least one full clock cycle without being used — a proxy for 'least recently used.' Exact LRU would require a complete sorted ordering of all pages by last-access time, too expensive to maintain per-access."
  explanation: "The Clock algorithm trades precision for efficiency. Exact LRU knows the full ordering of recency; Clock only distinguishes recent vs. not-recent within each sweep cycle. In practice this approximation works well because actively used pages will have their reference bits set repeatedly, while cold pages will consistently show bit = 0 and be evicted promptly. The Clock algorithm is implemented in most Unix-derived operating systems — its simplicity (one bit per page and a circularly advancing pointer) makes it suitable for the OS kernel where per-access overhead must be minimal."
```

## Explainer

From virtual memory management, you know that a process's address space can be larger than physical memory. The OS maps virtual pages to physical frames, and when a process accesses a page that is not currently in memory, a **page fault** occurs and the OS must load that page from disk. If all physical frames are already occupied, the OS must **evict** one page to make room. The page replacement algorithm decides which page gets evicted — and this choice has a dramatic effect on performance, because a bad choice means the evicted page will be needed again soon, causing another expensive page fault.

The **Optimal algorithm** (OPT, also called Belady's algorithm) provides the theoretical best answer: evict the page that will not be used for the longest time in the future. If page A will next be accessed in 100 instructions and page B will next be accessed in 5 instructions, evict A. This minimizes total page faults, but it requires knowing the future access pattern — impossible in a real system. OPT serves as a benchmark: you can run it on a recorded trace to see how close your real algorithm comes to the theoretical minimum.

**FIFO** (First-In, First-Out) is the simplest practical algorithm: evict the page that has been in memory the longest. It requires only a queue — load a page, push it to the back; evict from the front. FIFO is easy to implement but performs poorly because "oldest" does not mean "least useful." A page loaded long ago might be accessed constantly (think: a loop's code page). FIFO's most surprising property is **Belady's Anomaly**: increasing the number of available frames can actually *increase* page faults for certain reference strings. This is counterintuitive — more memory should help — and it reveals that FIFO's eviction criterion is fundamentally misaligned with what matters (recency of use, not age of loading).

**LRU** (Least Recently Used) fixes this by evicting the page that has gone the longest *without being accessed*. The reasoning comes from **temporal locality**, a principle you know from cache replacement: if a page was used recently, it is likely to be used again soon. LRU never exhibits Belady's Anomaly and closely approximates OPT in practice. However, exact LRU is expensive — tracking the precise access order of all pages requires either a timestamp on every memory access or maintaining a stack of page numbers, both of which are prohibitively costly in hardware. This is why real systems use **approximations**. The **Clock algorithm** (Second-Chance) is the most common: each page has a **reference bit** set by hardware whenever the page is accessed. The algorithm sweeps through pages in a circle. If a page's reference bit is 1, it gets a "second chance" — the bit is cleared and the algorithm moves on. If the bit is 0, that page has not been accessed since the last sweep and is evicted. Clock approximates LRU with minimal overhead — just one bit per page and a circular pointer — making it the algorithm most widely deployed in real operating systems.
