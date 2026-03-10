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
status: draft
---

# Cache Replacement Policies

## Core Idea
When a cache is full and a new block must be loaded, a replacement policy chooses which existing block to evict. Least Recently Used (LRU) evicts the block not accessed for the longest time, exploiting temporal locality. First-In First-Out (FIFO) evicts the oldest loaded block regardless of access recency. Random replacement evicts a randomly chosen block and is surprisingly competitive in practice. LRU is optimal for many workloads but expensive to implement exactly in large caches; pseudo-LRU approximations are used instead.

## How It's Best Learned
Simulate LRU, FIFO, and random replacement on a small cache with a fixed access sequence. Count misses for each policy and compare. Explore Belady's anomaly — FIFO can have more misses with a larger cache — as a counterintuitive result.

## Common Misconceptions
- LRU is not always optimal; it performs poorly on cyclic access patterns larger than the cache.
- Random replacement is not a naive fallback — it is a well-studied policy that avoids worst-case behavior and is used in some production CPUs.
