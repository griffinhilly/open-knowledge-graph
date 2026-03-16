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
status: draft
---

# Cache Memory: Design Principles and Trade-Offs

## Core Idea
Caches exploit locality by storing recently accessed data closer to the CPU. Key design parameters—block size, associativity, capacity, and replacement policy—balance hit rate, miss latency, and hardware cost.

## Explainer

From your study of the memory hierarchy, you know that faster memory is more expensive per bit, creating a pyramid where small, fast storage sits near the processor and large, slow storage sits further away. A cache is the mechanism that makes this pyramid work transparently — it automatically keeps copies of recently and frequently accessed data in fast memory so that most accesses complete quickly, without the programmer having to manage data placement manually.

The first major design parameter is **block size** (also called line size) — the unit of data transferred between the cache and the level below it. Caches don't fetch individual bytes; they fetch aligned blocks, typically 32 or 64 bytes. Larger blocks exploit **spatial locality** (if you accessed address N, you'll likely access N+1 soon), but they also increase the **miss penalty** (each miss transfers more data) and can cause **cache pollution** (bringing in data you won't actually use, evicting data you will). The sweet spot depends on the workload, but most modern caches use 64-byte blocks as a practical compromise.

The second parameter is **associativity**, which determines where a given memory block can be placed in the cache. In a **direct-mapped** cache, each block maps to exactly one cache slot (determined by its address modulo the number of slots). This is simple and fast to look up but vulnerable to **conflict misses** — two frequently accessed blocks that happen to map to the same slot thrash back and forth, evicting each other repeatedly. A **fully associative** cache allows any block to go anywhere, eliminating conflict misses but requiring expensive parallel comparison hardware to search every slot on each access. **Set-associative** caches split the difference: the cache is divided into sets, each containing a few slots (ways). A block maps to one set but can go in any way within that set. A 4-way set-associative cache, for instance, gives each block four possible locations — enough to virtually eliminate conflict misses for most workloads while keeping lookup hardware manageable.

When a set is full and a new block arrives, the cache must choose a victim to evict. The **replacement policy** makes this decision. **Least Recently Used (LRU)** evicts the block that hasn't been accessed for the longest time, which works well in practice because of temporal locality. True LRU requires tracking access order across all ways, which gets expensive at high associativity, so real caches often use approximations like pseudo-LRU or random replacement. The final dimension is **total capacity**: larger caches have higher hit rates but occupy more chip area, consume more power, and have longer access times. This is why modern processors use multiple cache levels — a small, fast L1 cache (often split into separate instruction and data caches), a medium L2, and a large shared L3 — each trading speed for capacity at a different point in the design space.
