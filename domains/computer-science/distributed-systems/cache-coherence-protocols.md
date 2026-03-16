---
id: cache-coherence-protocols
title: Cache Coherence Protocols and Memory Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: synchronization-problem
  type: hard
tags:
- caching
- consistency
- coherence
stage: advanced
status: draft
---

# Cache Coherence Protocols and Memory Consistency

## Core Idea
Cache coherence protocols maintain consistency between multiple caches in a system. MESI (Modified, Exclusive, Shared, Invalid) is a common protocol that tracks cache line states and coordinates through snooping or directory-based schemes. Correct coherence is essential to prevent processes from seeing inconsistent data when multiple CPUs or nodes have copies of the same memory location.

## Explainer

From your work with consistency models and the synchronization problem, you know that when multiple processors or nodes share data, concurrent access without coordination leads to inconsistent views. **Cache coherence** is the specific instance of this problem that arises when multiple processors each maintain their own local cache of shared memory. If processor A writes a new value to address X in its cache, processor B's cache still holds the stale old value — and without a coherence protocol, B has no way of knowing its copy is outdated.

The **MESI protocol** solves this by assigning each cache line one of four states. **Modified** means this cache holds the only valid copy and it has been changed — main memory is stale. **Exclusive** means this cache holds the only copy and it matches main memory — no other cache has it. **Shared** means multiple caches hold this line and all copies match main memory. **Invalid** means this cache line is not usable — it has been invalidated because another processor modified the data. Every read and write triggers state transitions: when processor A writes to a Shared line, the protocol sends an invalidation message to all other caches holding that line, transitioning their copies to Invalid and A's copy to Modified.

There are two main coordination mechanisms. In **snooping protocols**, every cache watches (snoops on) a shared bus and reacts when it sees transactions involving addresses it holds. This works well for small numbers of processors sharing a bus, but does not scale — every cache must see every transaction. In **directory-based protocols**, a central directory tracks which caches hold copies of each memory block. When a write occurs, the directory sends targeted invalidation messages only to caches that actually hold the line, avoiding broadcast overhead. This scales to larger systems but adds latency for the directory lookup.

Understanding cache coherence bridges the gap between the abstract consistency models you have studied and the physical reality of how hardware enforces them. The consistency model tells you what ordering guarantees the system provides to programmers; the coherence protocol is the mechanism that delivers those guarantees at the hardware level. When coherence works correctly, programmers can reason about shared memory without thinking about caches at all. When it breaks down — or when the performance cost of maintaining coherence becomes the bottleneck — it explains phenomena like false sharing (two unrelated variables on the same cache line causing constant invalidations) and motivates the design of systems that minimize shared mutable state entirely.
