---
id: cache-write-policies
title: Cache Write-Through and Write-Back Policies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-design-principles
  type: hard
- id: cache-memory-design
  type: soft
builds-toward:
- cache-coherence-protocols
tags:
- cache
- write-policy
- memory-consistency
stage: formal-systems
status: draft
---

# Cache Write-Through and Write-Back Policies

## Core Idea
Write-through writes to both cache and main memory immediately; it guarantees memory consistency but is slow. Write-back writes only to the cache, marking the block dirty; the block is written back when evicted. Write-back is faster but requires careful coherence protocols in multi-core systems. Most modern systems use write-back with a write-combine buffer.

## Explainer

From your study of cache design, you know that caches exploit temporal and spatial locality to keep frequently accessed data close to the processor. But reads are only half the story — the cache must also handle writes, and the policy it uses has significant implications for performance, complexity, and correctness. The two fundamental approaches are **write-through** and **write-back**, and understanding their tradeoffs is essential to reasoning about memory system behavior.

In a **write-through** cache, every write updates both the cache line and main memory simultaneously. The advantage is simplicity: main memory always contains the most recent data, so there is never a question of staleness. If the cache line is evicted, nothing special needs to happen because memory already has the current value. The disadvantage is bandwidth: every store instruction generates a write to main memory, which is slow (hundreds of cycles). To mitigate this, write-through caches typically use a **write buffer** — a small queue that absorbs writes so the processor does not stall waiting for each one to reach memory. As long as writes arrive slower than the buffer can drain, the processor runs at full speed.

In a **write-back** cache, writes update only the cache line. The line is marked with a **dirty bit** indicating that it has been modified and differs from main memory. The modified data is written to memory only when the line is evicted (replaced by a new line). This dramatically reduces memory traffic — if a program writes to the same variable 100 times, only one write reaches memory, on eviction. The cost is complexity: the cache controller must track dirty bits, and eviction of a dirty line stalls the incoming load until the writeback completes. Many designs add a **write-back buffer** to overlap this writeback with the new line's fetch.

The choice between policies becomes critical in **multiprocessor systems**. With write-through, other cores can snoop the memory bus to see writes as they happen, keeping their caches consistent relatively easily. With write-back, a modified value may exist only in one core's cache, invisible to others. This is why write-back caches require **cache coherence protocols** (like MESI) to ensure that when one core modifies a line, other cores that hold copies are notified. Modern systems overwhelmingly use write-back for its bandwidth advantages, accepting the coherence complexity as a necessary cost. A related decision is **write-allocate** versus **no-write-allocate**: on a write miss, does the cache fetch the line first (write-allocate, paired with write-back) or write directly to memory without caching (no-write-allocate, often paired with write-through)?
