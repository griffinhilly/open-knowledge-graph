---
id: buffer-pool-cache-replacement-policies
title: Buffer Pool Management and Cache Replacement Policies
domain: computer-science
course: databases
prerequisites:
- id: physical-storage-pages-records
  type: hard
- id: memory-management-basics
  type: soft
builds-toward:
- crash-recovery-undo-redo-logs
- query-execution-plan-analysis-explain
tags:
- buffer-pool
- cache
- replacement-policy
- LRU
- FIFO
stage: formal-systems
status: validated
---

# Buffer Pool Management and Cache Replacement Policies

## Core Idea
Buffer pools cache frequently accessed pages in memory to minimize disk I/O. Pages are identified by frame numbers and tracked with metadata (dirty bit, pin count, reference time). Replacement policies decide which page to evict when full: LRU (least-recently-used) works well for many workloads, FIFO is simpler, clock algorithms approximate LRU with less overhead. Pinning prevents eviction of critical pages.

## Questions

```yaml
- question: "The buffer pool is full and the replacement policy selects a page to evict. The chosen page's dirty bit is set to 1. What must happen before the frame can be reused?"
  type: multiple-choice
  options:
    - "Nothing extra — the dirty bit just indicates the page was recently accessed, not that it was modified"
    - "The page must be written back to disk before the frame can be reused, incurring a write I/O"
    - "The page is discarded immediately since dirty pages are invalid and the disk copy is authoritative"
    - "The pin count must be decremented to zero before the dirty page can be written"
  answer: 1
  explanation: "The dirty bit tracks whether a page has been modified since it was read from disk. A dirty page has changes that exist only in memory — the disk copy is stale. Before the frame can be reused for a new page, the dirty page must be flushed to disk, incurring a write I/O. A clean page (dirty bit = 0) can be evicted instantly because the disk copy is still valid. This asymmetry is why the buffer manager tries to evict clean pages first and why background writer processes proactively flush dirty pages."

- question: "A database buffer pool is running the clock algorithm. A frame's reference bit is currently 1 when the clock hand reaches it during eviction. What happens?"
  type: multiple-choice
  options:
    - "The frame is immediately evicted because it was recently accessed and should be refreshed"
    - "The reference bit is reset to 0, the clock hand moves on, and the frame gets a 'second chance'"
    - "The frame's pin count is incremented to protect it from future eviction"
    - "The frame is promoted to a special 'hot' list that the clock algorithm skips permanently"
  answer: 1
  explanation: "The clock algorithm approximates LRU with less bookkeeping. When the clock hand encounters a frame with reference bit = 1, it gives it a second chance: reset the bit to 0 and move on. Only when the hand returns to a frame and finds the bit still 0 (meaning no access occurred in the interim) does it evict that frame. This avoids LRU's expensive per-access list updates while still approximating recency — recently accessed pages have their bit reset to 1 before the hand can revisit them."

- question: "LRU is the most commonly implemented replacement policy in real database buffer pools because it provides the best performance in most workloads."
  type: true-false
  answer: false
  explanation: "Despite LRU's theoretical appeal, most real database systems use the clock algorithm (or variants like Clock-Pro or 2Q) rather than true LRU. The reason is overhead: LRU requires updating a precise access ordering on every page access — typically maintaining a doubly-linked list — which adds synchronization cost in concurrent systems. The clock algorithm approximates LRU's behavior with a single reference bit and no per-access list manipulation. Additionally, LRU performs poorly on sequential scans (where every page is accessed exactly once and then not again), and real systems often use special-purpose policies for scan patterns."

- question: "A page with a pin count greater than zero cannot be evicted by any replacement policy, regardless of how long it has been in the buffer pool."
  type: true-false
  answer: true
  explanation: "The pin count tracks how many active operations are currently using a page. If a transaction or query is in the middle of reading or writing a page, it pins the page to prevent the buffer manager from evicting it mid-operation. Any eviction algorithm — LRU, FIFO, clock — must skip pinned pages entirely. The pin count is decremented when the operation completes, at which point the page becomes eligible for eviction. This mechanism is essential for correctness: evicting a page an active operation depends on would cause data corruption or invalid memory references."

- question: "Why does evicting a dirty page cost more than evicting a clean page, and how do database systems reduce this overhead?"
  type: short-answer
  answer: "A dirty page has been modified in memory but not yet written to disk, so evicting it requires a write I/O to persist the changes — doubling the I/O cost compared to simply reading a new page in. A clean page's disk copy is still valid, so no write is needed. Database systems reduce this overhead through background writer processes that proactively flush dirty pages to disk during idle periods, so that when eviction is needed, more frames are already clean and can be evicted immediately."
  explanation: "The dirty bit is central to both correctness and performance. Without flushing dirty pages before eviction, updates would be permanently lost. But if every eviction required a write (flush) followed by a read (new page), the effective throughput would be halved. Background flushing decouples these two operations: dirty pages are written to disk asynchronously before they are urgently needed for eviction, so the eviction path is usually just a read, not a read-after-write."
```

## Explainer

From your study of physical storage, you know that database data lives on disk in fixed-size units called **pages** (typically 4KB or 8KB). Disk access is orders of magnitude slower than memory access — roughly 10 milliseconds for a random disk read versus 100 nanoseconds for a memory access, a factor of 100,000. The **buffer pool** exists to bridge this gap. It is a region of main memory divided into **frames**, each sized to hold exactly one page. When the database engine needs a page, it first checks the buffer pool; if the page is already there (a **hit**), it avoids the disk entirely. If not (a **miss**), it reads the page from disk into a free frame.

The interesting problem arises when the buffer pool is full and a new page must be brought in. Some existing page must be **evicted** to make room, and the choice of which page to evict has enormous performance implications. The **LRU** (least-recently-used) policy evicts the page that has gone the longest without being accessed, based on the intuition that recently used pages are likely to be used again soon. LRU works well for many database workloads but requires maintaining a precise access ordering — typically a doubly-linked list that gets updated on every page access, which adds overhead.

**FIFO** (first-in, first-out) is the simplest alternative: evict whichever page has been in the buffer pool the longest, regardless of how recently it was accessed. It is cheap to implement but performs poorly when old pages are frequently re-accessed. The **clock algorithm** offers a practical middle ground. It arranges frames in a circular buffer with a "clock hand" pointer. Each frame has a **reference bit** set to 1 whenever the page is accessed. When eviction is needed, the clock hand sweeps around: if a frame's reference bit is 1, it gets reset to 0 and the hand moves on; if it is 0, that frame is evicted. This approximates LRU — recently accessed pages get a second chance — with far less bookkeeping overhead, making it the policy most real database systems actually use.

Two additional pieces of metadata are critical. The **dirty bit** tracks whether a page has been modified since it was read from disk. A clean page can be evicted instantly (the disk copy is still valid), but a dirty page must be written back to disk before eviction, doubling the I/O cost. The **pin count** tracks how many operations are currently using a page — a pinned page cannot be evicted under any policy, because an active transaction or operation depends on it being in memory. Understanding these mechanics explains why database tuning often focuses on buffer pool sizing: a larger buffer pool means more pages fit in memory, more accesses are hits, and fewer expensive disk I/Os occur.
