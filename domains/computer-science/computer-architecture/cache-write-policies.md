---
id: cache-write-policies
title: Cache Write-Through and Write-Back Policies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-memory-design
  type: hard
builds-toward:
- cache-coherence-protocols
tags:
- cache
- write-policy
- memory-consistency
stage: formal-systems
status: validated
---

# Cache Write-Through and Write-Back Policies

## Core Idea
Write-through writes to both cache and main memory immediately; it guarantees memory consistency but is slow. Write-back writes only to the cache, marking the block dirty; the block is written back when evicted. Write-back is faster but requires careful coherence protocols in multi-core systems. Most modern systems use write-back with a write-combine buffer.

## Questions

```yaml
- question: "A program writes to the same memory address 200 times in a tight loop, and the cache line containing that address is never evicted during the loop. How many writes reach main memory under write-back vs. write-through?"
  type: multiple-choice
  options:
    - "Write-back: 200 writes; Write-through: 1 write"
    - "Write-back: 1 write (on eviction); Write-through: 200 writes"
    - "Both policies generate 200 writes to main memory"
    - "Write-back: 0 writes; Write-through: 200 writes (write-back never touches main memory)"
  answer: 1
  explanation: "With write-back, each store updates only the cache line and marks it dirty. Main memory is not touched until eviction. So 200 stores to the same line produce just 1 main-memory write (when the line is eventually evicted). With write-through, every store immediately writes to main memory — 200 stores produce 200 main-memory writes. This bandwidth difference is the core reason write-back dominates in modern processors. Option D is tempting but wrong: write-back does write to main memory eventually, just only on eviction."

- question: "In a multiprocessor system, why does write-back require explicit cache coherence protocols (like MESI), while write-through is simpler to keep consistent?"
  type: multiple-choice
  options:
    - "Write-back caches are physically farther from main memory in multiprocessor layouts"
    - "With write-through, every store propagates to main memory immediately so other cores can observe writes by snooping the memory bus; with write-back, modified data may reside only in one core's cache, invisible to others"
    - "Write-through uses dirty bits that must be coordinated across all caches, while write-back does not"
    - "Write-back generates more total memory traffic, making coherence harder to track"
  answer: 1
  explanation: "The key issue is visibility. Write-through broadcasts every write to main memory, so any core monitoring the memory bus can see updates as they happen — coherence comes almost for free via bus snooping. Write-back keeps modified data silently in the local cache (the dirty line). Another core that holds a stale copy of the same line has no way of knowing it's outdated without an explicit protocol. MESI (Modified/Exclusive/Shared/Invalid) states track ownership and validity across caches, ensuring that when one core's line is Modified, other cores' copies are invalidated."

- question: "A dirty bit in a write-back cache indicates that the cache line contains data that has been modified and differs from the corresponding value in main memory."
  type: true-false
  answer: true
  explanation: "The dirty bit is the write-back cache's record-keeping mechanism. When a store updates a cache line, the hardware sets that line's dirty bit to 1. 'Dirty' means the cache holds the authoritative, up-to-date value and main memory holds a stale copy. When the line is evicted, the controller checks the dirty bit: if set, it writes the line back to memory before loading the new line; if clean, the eviction is silent. Without dirty bits, the cache would have no way to distinguish lines that need writing back from those that don't."

- question: "Write-through caches are generally faster than write-back caches because keeping main memory up to date avoids the overhead of writing back dirty lines on eviction."
  type: true-false
  answer: false
  explanation: "Write-through is generally slower, not faster. Every store instruction generates a write to main memory, which takes hundreds of cycles. Even with a write buffer to absorb some latency, high write traffic saturates the memory bus and stalls the processor. Write-back dramatically reduces memory traffic: if a cache line is written 50 times before eviction, write-back generates 1 memory write while write-through generates 50. The overhead of occasionally flushing a dirty line on eviction is far less than the constant write traffic of write-through."

- question: "Explain the role of the dirty bit in a write-back cache. What happens when a dirty cache line is evicted, and why does write-back require this mechanism while write-through does not?"
  type: short-answer
  answer: "In a write-back cache, when the CPU stores data to a cache line, only the cache is updated — main memory is not. The dirty bit (one bit per cache line) is set to signal that this line has been modified and its contents differ from main memory. When the cache controller needs to evict a line to make room for new data, it checks the dirty bit: if set, it must first write the modified data back to main memory before loading the new line; if clean, the eviction is silent. Write-through does not need dirty bits because every store immediately writes to both cache and main memory, keeping them always synchronized — eviction never requires a writeback because main memory always has the current value."
  explanation: "The dirty bit is minimal bookkeeping that makes write-back work: instead of writing every store to memory, the cache notes which lines need attention at eviction time. It trades memory bandwidth (fewer writes) for a small amount of hardware bookkeeping and occasional eviction stalls — a tradeoff that pays off enormously in performance."
```

## Explainer

From your study of cache design, you know that caches exploit temporal and spatial locality to keep frequently accessed data close to the processor. But reads are only half the story — the cache must also handle writes, and the policy it uses has significant implications for performance, complexity, and correctness. The two fundamental approaches are **write-through** and **write-back**, and understanding their tradeoffs is essential to reasoning about memory system behavior.

In a **write-through** cache, every write updates both the cache line and main memory simultaneously. The advantage is simplicity: main memory always contains the most recent data, so there is never a question of staleness. If the cache line is evicted, nothing special needs to happen because memory already has the current value. The disadvantage is bandwidth: every store instruction generates a write to main memory, which is slow (hundreds of cycles). To mitigate this, write-through caches typically use a **write buffer** — a small queue that absorbs writes so the processor does not stall waiting for each one to reach memory. As long as writes arrive slower than the buffer can drain, the processor runs at full speed.

In a **write-back** cache, writes update only the cache line. The line is marked with a **dirty bit** indicating that it has been modified and differs from main memory. The modified data is written to memory only when the line is evicted (replaced by a new line). This dramatically reduces memory traffic — if a program writes to the same variable 100 times, only one write reaches memory, on eviction. The cost is complexity: the cache controller must track dirty bits, and eviction of a dirty line stalls the incoming load until the writeback completes. Many designs add a **write-back buffer** to overlap this writeback with the new line's fetch.

The choice between policies becomes critical in **multiprocessor systems**. With write-through, other cores can snoop the memory bus to see writes as they happen, keeping their caches consistent relatively easily. With write-back, a modified value may exist only in one core's cache, invisible to others. This is why write-back caches require **cache coherence protocols** (like MESI) to ensure that when one core modifies a line, other cores that hold copies are notified. Modern systems overwhelmingly use write-back for its bandwidth advantages, accepting the coherence complexity as a necessary cost. A related decision is **write-allocate** versus **no-write-allocate**: on a write miss, does the cache fetch the line first (write-allocate, paired with write-back) or write directly to memory without caching (no-write-allocate, often paired with write-through)?
