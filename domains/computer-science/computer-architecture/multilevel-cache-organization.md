---
id: multilevel-cache-organization
title: Multilevel Cache Design and Coordination
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-associativity-and-mapping
  type: hard
- id: cache-coherence-protocols
  type: soft
builds-toward:
- multi-core-system-design
tags:
- cache-hierarchy
- l1-l2-l3
- memory-hierarchy
stage: advanced
status: draft
---

# Multilevel Cache Design and Coordination

## Core Idea
Modern processors use multiple cache levels: L1 (small, fast, on-core), L2 (larger, slower), L3 (shared, slowest). Each level acts as a victim cache for the next. Inclusion and coherence policies define relationships: an inclusive cache holds a superset of lower levels; an exclusive cache holds data not in lower levels. Proper coordination minimizes memory latency.

## Explainer

From your study of cache associativity and mapping, you understand how a single cache decides where to place data and how to find it again. Multilevel cache organization extends this idea by asking: what happens when one cache is not enough? The answer is a **hierarchy** — a series of progressively larger and slower caches between the processor and main memory, each absorbing misses from the level above it. The goal is to serve as many memory requests as possible from fast, nearby storage while keeping the total silicon area and power consumption manageable.

A typical modern processor has three levels. The **L1 cache** sits directly on the processor core, split into separate instruction and data caches (L1i and L1d), each typically 32–64 KB with 1–2 cycle access latency. L1 is tiny but blazingly fast. When L1 misses, the request falls through to the **L2 cache**, usually 256 KB to 1 MB per core, with 4–12 cycle latency. L2 is still private to a single core but trades size for speed. If L2 also misses, the request reaches the **L3 cache**, often 8–64 MB and shared across all cores, with 20–40 cycle latency. Only if L3 misses does the request finally go to main memory at 100+ cycles. Each level thus acts as a filter: L1 catches the hottest, most frequently accessed data; L2 catches the warm working set; L3 catches cross-core sharing and larger patterns.

The relationship between levels is governed by an **inclusion policy**. In an **inclusive** hierarchy, every line in L1 is guaranteed to also exist in L2 and L3. This simplifies coherence — when another core wants to check whether you have a particular cache line, it only needs to probe L3. If it's not there, it's not in any L1 or L2 either. The downside is wasted capacity, since lower levels duplicate upper-level data. In an **exclusive** hierarchy, a cache line exists at exactly one level, maximizing total effective capacity but complicating coherence checks. Many real processors use a **non-inclusive, non-exclusive** (NINE) policy as a pragmatic middle ground.

Coordination between levels also involves **coherence protocols**, which you've encountered as a prerequisite. In a multicore system with shared L3, if one core writes to a cache line that another core has cached, the coherence protocol must invalidate or update the stale copy. Multilevel caches make this harder because an invalidation at L3 might need to propagate down to L2 and L1 of another core. The interplay between cache size, associativity at each level, inclusion policy, and coherence protocol defines the memory subsystem's behavior — and small design changes can have outsized effects on workloads that share data across cores or have working sets that spill from one level to the next.
