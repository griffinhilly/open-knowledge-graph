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
stage: formal-systems
status: validated
---

# Multilevel Cache Design and Coordination

## Core Idea
Modern processors use multiple cache levels: L1 (small, fast, on-core), L2 (larger, slower), L3 (shared, slowest). Each level acts as a victim cache for the next. Inclusion and coherence policies define relationships: an inclusive cache holds a superset of lower levels; an exclusive cache holds data not in lower levels. Proper coordination minimizes memory latency.

## Questions

```yaml
- question: "A multicore processor uses an inclusive L3 cache. Core A wants to modify a cache line that Core B might have cached. Why does the inclusive design simplify this coherence check?"
  type: multiple-choice
  options:
    - "Inclusive caches use hardware locks that serialize all cache accesses across cores"
    - "Because every L1 and L2 cache line is guaranteed to exist in L3, the coherence protocol only needs to probe L3 — if the line isn't there, it isn't anywhere"
    - "Inclusive caches are smaller and faster to search than exclusive caches"
    - "The shared L3 directly controls all L1 and L2 caches, so it can invalidate them without probing"
  answer: 1
  explanation: "The inclusion property guarantees that L3 is a superset of all data in any L1 or L2 on any core. A coherence check can therefore stop at L3: a cache line not in L3 cannot be in any private cache. Without this guarantee (as in exclusive or NINE caches), the protocol must potentially search across all levels, significantly increasing coherence complexity and latency."

- question: "Which workload scenario best illustrates the performance advantage of an exclusive cache hierarchy over an inclusive one?"
  type: multiple-choice
  options:
    - "Multiple cores frequently sharing the same hot data, requiring rapid cross-core coherence checks"
    - "Each core accessing a distinct, large private dataset where L2 misses rarely repeat, so avoiding duplicated data across levels maximizes total effective capacity"
    - "A workload requiring very frequent L1 hits, where L3 behavior is largely irrelevant"
    - "A single-threaded workload with a working set that fits entirely within L1"
  answer: 1
  explanation: "Exclusive caches eliminate data duplication: each line exists at exactly one level, so the sum of all cache sizes equals the effective total capacity. For workloads with large, private per-core datasets where duplicating data across levels wastes capacity, exclusive hierarchies significantly outperform inclusive ones. The tradeoff is more complex coherence protocols, which is why inclusive caches with their simpler probing are preferred when cross-core sharing is common."

- question: "In an inclusive cache hierarchy, every cache line present in an L1 cache is also guaranteed to be present in L2 and L3."
  type: true-false
  answer: true
  explanation: "Inclusive policy means each lower level is a superset of all higher levels combined. L3 contains everything in L2, which contains everything in L1. This redundancy simplifies coherence at the cost of effective capacity — L3 area is partially 'wasted' holding copies of L1 and L2 data rather than additional unique data."

- question: "A program whose entire working set fits within the L2 cache will run significantly faster on a processor with a larger L3 cache."
  type: true-false
  answer: false
  explanation: "If the working set fits in L2, memory accesses are satisfied without ever reaching L3. A larger L3 provides no latency benefit because L3 is never consulted. L3 only helps when L2 misses — which don't occur here. This illustrates why understanding your workload's working set size relative to each cache level is essential for predicting where cache size improvements will actually improve performance."

- question: "Explain why an exclusive cache hierarchy achieves greater total effective capacity than an inclusive one with the same physical cache sizes, and what tradeoff this introduces."
  type: short-answer
  answer: "In an inclusive hierarchy, every L1 and L2 cache line is duplicated in L3, so L3's capacity is partially consumed by holding redundant copies rather than additional unique data — the effective unique data capacity is bounded by L3 alone. In an exclusive hierarchy, each cache line resides at exactly one level, so total effective capacity is the sum of all levels (L1 + L2 + L3). The tradeoff is coherence complexity: the inclusive property allows coherence checks to stop at L3 (if not there, not anywhere), whereas exclusive hierarchies require probing across levels to locate a line, making the coherence protocol more complex and potentially slower."
  explanation: "Real processors often use non-inclusive, non-exclusive (NINE) policies as a pragmatic middle ground — lines are not guaranteed to be duplicated, but are not guaranteed to be unique either. This gives more flexibility in managing capacity while keeping coherence protocols tractable."
```

## Explainer

From your study of cache associativity and mapping, you understand how a single cache decides where to place data and how to find it again. Multilevel cache organization extends this idea by asking: what happens when one cache is not enough? The answer is a **hierarchy** — a series of progressively larger and slower caches between the processor and main memory, each absorbing misses from the level above it. The goal is to serve as many memory requests as possible from fast, nearby storage while keeping the total silicon area and power consumption manageable.

A typical modern processor has three levels. The **L1 cache** sits directly on the processor core, split into separate instruction and data caches (L1i and L1d), each typically 32–64 KB with 1–2 cycle access latency. L1 is tiny but blazingly fast. When L1 misses, the request falls through to the **L2 cache**, usually 256 KB to 1 MB per core, with 4–12 cycle latency. L2 is still private to a single core but trades size for speed. If L2 also misses, the request reaches the **L3 cache**, often 8–64 MB and shared across all cores, with 20–40 cycle latency. Only if L3 misses does the request finally go to main memory at 100+ cycles. Each level thus acts as a filter: L1 catches the hottest, most frequently accessed data; L2 catches the warm working set; L3 catches cross-core sharing and larger patterns.

The relationship between levels is governed by an **inclusion policy**. In an **inclusive** hierarchy, every line in L1 is guaranteed to also exist in L2 and L3. This simplifies coherence — when another core wants to check whether you have a particular cache line, it only needs to probe L3. If it's not there, it's not in any L1 or L2 either. The downside is wasted capacity, since lower levels duplicate upper-level data. In an **exclusive** hierarchy, a cache line exists at exactly one level, maximizing total effective capacity but complicating coherence checks. Many real processors use a **non-inclusive, non-exclusive** (NINE) policy as a pragmatic middle ground.

Coordination between levels also involves **coherence protocols**, which you've encountered as a prerequisite. In a multicore system with shared L3, if one core writes to a cache line that another core has cached, the coherence protocol must invalidate or update the stale copy. Multilevel caches make this harder because an invalidation at L3 might need to propagate down to L2 and L1 of another core. The interplay between cache size, associativity at each level, inclusion policy, and coherence protocol defines the memory subsystem's behavior — and small design changes can have outsized effects on workloads that share data across cores or have working sets that spill from one level to the next.
