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
- crash-recovery-undo-redo
- query-execution-plan-analysis-explain
tags:
- buffer-pool
- cache
- replacement-policy
- LRU
- FIFO
stage: formal-systems
status: draft
---

# Buffer Pool Management and Cache Replacement Policies

## Core Idea
Buffer pools cache frequently accessed pages in memory to minimize disk I/O. Pages are identified by frame numbers and tracked with metadata (dirty bit, pin count, reference time). Replacement policies decide which page to evict when full: LRU (least-recently-used) works well for many workloads, FIFO is simpler, clock algorithms approximate LRU with less overhead. Pinning prevents eviction of critical pages.

## Explainer

From your study of physical storage, you know that database data lives on disk in fixed-size units called **pages** (typically 4KB or 8KB). Disk access is orders of magnitude slower than memory access — roughly 10 milliseconds for a random disk read versus 100 nanoseconds for a memory access, a factor of 100,000. The **buffer pool** exists to bridge this gap. It is a region of main memory divided into **frames**, each sized to hold exactly one page. When the database engine needs a page, it first checks the buffer pool; if the page is already there (a **hit**), it avoids the disk entirely. If not (a **miss**), it reads the page from disk into a free frame.

The interesting problem arises when the buffer pool is full and a new page must be brought in. Some existing page must be **evicted** to make room, and the choice of which page to evict has enormous performance implications. The **LRU** (least-recently-used) policy evicts the page that has gone the longest without being accessed, based on the intuition that recently used pages are likely to be used again soon. LRU works well for many database workloads but requires maintaining a precise access ordering — typically a doubly-linked list that gets updated on every page access, which adds overhead.

**FIFO** (first-in, first-out) is the simplest alternative: evict whichever page has been in the buffer pool the longest, regardless of how recently it was accessed. It is cheap to implement but performs poorly when old pages are frequently re-accessed. The **clock algorithm** offers a practical middle ground. It arranges frames in a circular buffer with a "clock hand" pointer. Each frame has a **reference bit** set to 1 whenever the page is accessed. When eviction is needed, the clock hand sweeps around: if a frame's reference bit is 1, it gets reset to 0 and the hand moves on; if it is 0, that frame is evicted. This approximates LRU — recently accessed pages get a second chance — with far less bookkeeping overhead, making it the policy most real database systems actually use.

Two additional pieces of metadata are critical. The **dirty bit** tracks whether a page has been modified since it was read from disk. A clean page can be evicted instantly (the disk copy is still valid), but a dirty page must be written back to disk before eviction, doubling the I/O cost. The **pin count** tracks how many operations are currently using a page — a pinned page cannot be evicted under any policy, because an active transaction or operation depends on it being in memory. Understanding these mechanics explains why database tuning often focuses on buffer pool sizing: a larger buffer pool means more pages fit in memory, more accesses are hits, and fewer expensive disk I/Os occur.
