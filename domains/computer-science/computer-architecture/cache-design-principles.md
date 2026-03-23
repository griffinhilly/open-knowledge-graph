---
id: cache-design-principles
title: 'Cache Memory: Design Principles and Trade-Offs'
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-hierarchy-overview
  type: hard
- id: cache-memory-design
  type: soft
builds-toward:
- cache-optimization-techniques
- instruction-pipeline-organization
tags:
- cache
- memory
- hierarchy
- performance
stage: formal-systems
status: validated
---

# Cache Memory: Design Principles and Trade-Offs

## Core Idea
Caches exploit locality by storing recently accessed data closer to the CPU. Key design parameters—block size, associativity, capacity, and replacement policy—balance hit rate, miss latency, and hardware cost.

## Questions

```yaml
- question: "A programmer accesses array elements sequentially (arr[0], arr[1], arr[2], ...). A cache with 64-byte blocks fetches an entire block on each miss. Which locality principle does this design exploit?"
  type: multiple-choice
  options:
    - "Temporal locality — accessing the same element repeatedly in a short time"
    - "Spatial locality — after accessing arr[0], nearby elements arr[1]–arr[15] are already in the fetched block"
    - "Random locality — accesses are distributed uniformly across memory"
    - "The cache does not exploit locality; it simply stores the most recently accessed byte"
  answer: 1
  explanation: "Spatial locality is the principle that if you access address N, you will likely soon access addresses near N. By fetching a full 64-byte block on every miss (not just the single requested byte), the cache pre-loads neighboring elements. In a sequential array traversal, most elements after the first in each block will already be cached when accessed. Temporal locality — the complementary principle that you will reuse the same address soon — is exploited by keeping recently accessed blocks in cache rather than evicting them immediately."

- question: "Why can a direct-mapped cache sometimes perform worse than a smaller fully-associative cache on certain workloads?"
  type: multiple-choice
  options:
    - "Direct-mapped caches are always slower due to simpler hardware design"
    - "Direct-mapped caches suffer conflict misses: two frequently used blocks that map to the same slot thrash each other out, even if many other slots are empty"
    - "Fully-associative caches are faster because they use more transistors"
    - "Direct-mapped caches cannot exploit temporal locality"
  answer: 1
  explanation: "In a direct-mapped cache, each memory block can only go in one specific slot. If two frequently accessed blocks happen to map to the same slot, they will repeatedly evict each other — conflict misses — even if many other cache slots are empty. A fully-associative cache lets any block go anywhere, eliminating conflict misses. A smaller fully-associative cache can outperform a larger direct-mapped cache for workloads that repeatedly access a small set of blocks that conflict in the direct-mapped scheme."

- question: "Increasing cache capacity always improves program performance."
  type: true-false
  answer: false
  explanation: "Larger caches have higher hit rates for workloads that benefit from more storage, but they also have longer access times (larger circuits take longer to search), consume more chip area and power, and may not fit the tight timing requirements of an L1 cache. A very large L1 cache might produce worse overall performance than a smaller one if its longer access latency outweighs the benefit of fewer misses. This is why real processors use multi-level cache hierarchies — small fast L1, medium L2, large L3 — each optimized for a different point in the speed-capacity tradeoff."

- question: "The Least Recently Used (LRU) replacement policy guarantees the highest possible cache hit rate for any access pattern."
  type: true-false
  answer: false
  explanation: "LRU works well in practice because temporal locality is common — recently used data tends to be used again soon. However, LRU is not optimal for all access patterns. A sequential scan through a dataset larger than the cache (a 'streaming' workload) will see every block evicted before it is reused, and LRU performs no better than random replacement in that case. Optimal replacement (Bélády's algorithm) requires knowing the future, which is impossible at runtime. LRU is a good heuristic, not a universal guarantee."

- question: "What trade-off does block size create in cache design, and why is there an optimal block size rather than 'bigger is always better'?"
  type: short-answer
  answer: "Larger blocks exploit spatial locality more aggressively — each miss brings in more neighboring data, reducing future misses if those neighbors are actually accessed. But larger blocks also increase miss penalty (each miss transfers more data from slow memory), cause cache pollution (bringing in data that won't be used while evicting data that will), and reduce the total number of blocks the cache can hold, which may increase conflict or capacity misses. The optimal block size balances spatial locality gains against miss penalty and pollution — typically 32–64 bytes for modern workloads."
  explanation: "This trade-off illustrates why cache design is a system-level optimization problem: the right parameters depend on the workload's access pattern, the latency gap between cache and memory, and total cache capacity available. No single parameter setting is universally best, which is why hardware designers characterize workloads carefully before fixing these parameters."
```

## Explainer

From your study of the memory hierarchy, you know that faster memory is more expensive per bit, creating a pyramid where small, fast storage sits near the processor and large, slow storage sits further away. A cache is the mechanism that makes this pyramid work transparently — it automatically keeps copies of recently and frequently accessed data in fast memory so that most accesses complete quickly, without the programmer having to manage data placement manually.

The first major design parameter is **block size** (also called line size) — the unit of data transferred between the cache and the level below it. Caches don't fetch individual bytes; they fetch aligned blocks, typically 32 or 64 bytes. Larger blocks exploit **spatial locality** (if you accessed address N, you'll likely access N+1 soon), but they also increase the **miss penalty** (each miss transfers more data) and can cause **cache pollution** (bringing in data you won't actually use, evicting data you will). The sweet spot depends on the workload, but most modern caches use 64-byte blocks as a practical compromise.

The second parameter is **associativity**, which determines where a given memory block can be placed in the cache. In a **direct-mapped** cache, each block maps to exactly one cache slot (determined by its address modulo the number of slots). This is simple and fast to look up but vulnerable to **conflict misses** — two frequently accessed blocks that happen to map to the same slot thrash back and forth, evicting each other repeatedly. A **fully associative** cache allows any block to go anywhere, eliminating conflict misses but requiring expensive parallel comparison hardware to search every slot on each access. **Set-associative** caches split the difference: the cache is divided into sets, each containing a few slots (ways). A block maps to one set but can go in any way within that set. A 4-way set-associative cache, for instance, gives each block four possible locations — enough to virtually eliminate conflict misses for most workloads while keeping lookup hardware manageable.

When a set is full and a new block arrives, the cache must choose a victim to evict. The **replacement policy** makes this decision. **Least Recently Used (LRU)** evicts the block that hasn't been accessed for the longest time, which works well in practice because of temporal locality. True LRU requires tracking access order across all ways, which gets expensive at high associativity, so real caches often use approximations like pseudo-LRU or random replacement. The final dimension is **total capacity**: larger caches have higher hit rates but occupy more chip area, consume more power, and have longer access times. This is why modern processors use multiple cache levels — a small, fast L1 cache (often split into separate instruction and data caches), a medium L2, and a large shared L3 — each trading speed for capacity at a different point in the design space.
