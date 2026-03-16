---
id: cache-replacement-policies
title: Cache Replacement Policies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-memory-design
  type: hard
builds-toward:
- virtual-memory-basics
tags:
- LRU
- FIFO
- replacement-policy
- cache-eviction
stage: formal-systems
status: validated
---

# Cache Replacement Policies

## Core Idea
When a cache is full and a new block must be loaded, a replacement policy chooses which existing block to evict. Least Recently Used (LRU) evicts the block not accessed for the longest time, exploiting temporal locality. First-In First-Out (FIFO) evicts the oldest loaded block regardless of access recency. Random replacement evicts a randomly chosen block and is surprisingly competitive in practice. LRU is optimal for many workloads but expensive to implement exactly in large caches; pseudo-LRU approximations are used instead.

## How It's Best Learned
Simulate LRU, FIFO, and random replacement on a small cache with a fixed access sequence. Count misses for each policy and compare. Explore Belady's anomaly — FIFO can have more misses with a larger cache — as a counterintuitive result.

## Common Misconceptions
- LRU is not always optimal; it performs poorly on cyclic access patterns larger than the cache.
- Random replacement is not a naive fallback — it is a well-studied policy that avoids worst-case behavior and is used in some production CPUs.

## Explainer

From your study of cache memory design, you know that a cache holds a small, fast copy of recently accessed data from main memory. But caches are finite — a typical L1 cache might hold only 64 KB while main memory holds gigabytes. When every slot in a cache set is occupied and a new block needs to be loaded, the cache must **evict** one of the existing blocks to make room. The **replacement policy** is the rule that decides which block to sacrifice, and it has a direct impact on how often the cache misses.

The most intuitive policy is **Least Recently Used (LRU)**: evict whichever block has gone the longest without being accessed. The reasoning follows from **temporal locality** — if a block was used recently, it is likely to be used again soon, so evicting the least-recently-used block is the safest bet. For a 2-way set-associative cache, LRU is trivial: a single bit per set records which of the two blocks was accessed more recently. But for 8-way or 16-way associativity, true LRU requires tracking the full access order of all blocks in the set, which demands log2(n!) bits of state and complex update logic. This hardware cost is why real processors use **pseudo-LRU** approximations — tree-based schemes that track "roughly least recent" with far fewer bits.

**FIFO (First-In, First-Out)** takes a simpler approach: evict whichever block was *loaded* earliest, regardless of whether it was accessed recently. FIFO is cheaper to implement (just a circular pointer per set) and performs reasonably well, but it has a famous pathology called **Belady's anomaly**: increasing the cache size can actually *increase* the miss rate for certain access patterns. This counterintuitive result does not occur with LRU, which is one reason LRU is generally preferred despite its higher implementation cost.

**Random replacement** simply picks a victim at random. It requires almost no bookkeeping — just a pseudo-random number generator shared across the cache. While it sounds crude, random replacement avoids the worst-case access patterns that can degrade LRU and FIFO (such as cyclic scans through a working set slightly larger than the cache, where LRU evicts exactly the block that will be needed next). In practice, random replacement performs within a few percent of LRU for many workloads, which is why architectures like ARM Cortex processors have used it. The choice of replacement policy is ultimately an engineering tradeoff between hit rate, hardware complexity, and robustness to adversarial access patterns.
