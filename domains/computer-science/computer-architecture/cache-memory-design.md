---
id: cache-memory-design
title: Cache Memory Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-hierarchy-overview
  type: hard
builds-toward:
- cache-replacement-policies
tags:
- cache
- direct-mapped
- set-associative
- fully-associative
- hit-rate
stage: formal-systems
status: validated
---

# Cache Memory Design

## Core Idea
Cache memory design determines how main memory addresses map to cache slots. In a direct-mapped cache, each memory block maps to exactly one cache line determined by the address modulo the cache size. A fully associative cache allows any block to reside in any line, requiring a search of all lines on every access. Set-associative cache is a compromise: blocks map to one set but can occupy any way within that set. A cache hit returns data in 1–5 cycles; a miss requires fetching from main memory at 50–200 cycle latency.

## How It's Best Learned
Trace memory access sequences through a direct-mapped cache manually, tracking hits, misses, and evictions. Compare hit rates for the same pattern under different associativity levels. Calculate cache address fields (tag, index, offset) for a given cache configuration.

## Common Misconceptions
- Higher associativity does not always mean better performance; very high associativity increases hit latency and power consumption.
- A cold miss (compulsory miss) occurs the first time any address is accessed and is unavoidable regardless of cache size or design.

## Questions

```yaml
- question: "A program alternately accesses two arrays. Both arrays' base addresses happen to differ by exactly the cache size, so they map to the same cache lines. Performance is poor despite the working set fitting in cache. What type of miss is causing this?"
  type: multiple-choice
  options:
    - "Compulsory miss — the data is accessed for the first time on each iteration"
    - "Capacity miss — the combined working set is too large for the cache"
    - "Conflict miss — the two arrays compete for the same cache lines, evicting each other"
    - "Write miss — the cache write policy is causing repeated flushes"
  answer: 2
  explanation: "This is a conflict miss, the characteristic failure mode of direct-mapped caches. Each memory block maps to exactly one cache line (determined by address mod cache size). When two frequently accessed blocks map to the same line, each access evicts the other — even though the cache has many empty lines elsewhere. The working set fits in the cache; the problem is the rigid mapping. This is why set-associative design exists: allowing each block to reside in any of N ways within its set dramatically reduces conflict misses."

- question: "Why are fully associative caches not used for large L1 caches, even though they eliminate all conflict misses?"
  type: multiple-choice
  options:
    - "Fully associative caches have higher miss rates than set-associative caches"
    - "Every cache access requires comparing the address tag against every line simultaneously, requiring parallel comparator hardware for each line — too expensive at scale"
    - "Fully associative caches are incompatible with modern processor pipeline designs"
    - "The replacement policy for fully associative caches is too slow to implement in hardware"
  answer: 1
  explanation: "In a fully associative cache, any block can reside in any line. To determine if a given address is cached, the hardware must check every line at once (a hit anywhere counts). This requires a parallel comparator for each cache line — hardware that grows linearly with cache size. For a small structure like a TLB with 32–64 entries this is feasible, but for an L1 cache with thousands of lines, the area and power cost is prohibitive. Set-associative design limits the parallel search to just N ways within the relevant set — manageable even for modern caches."

- question: "Increasing cache size from 32KB to 256KB will eliminate compulsory (cold) misses on the first access to each memory block."
  type: true-false
  answer: false
  explanation: "Compulsory misses occur on the very first access to any block — the data has never been in the cache before, so a miss is unavoidable regardless of cache size or associativity. Even an infinitely large cache would still incur a compulsory miss the first time each address is referenced. Cache size reduces capacity misses (where the working set exceeds the cache). Associativity reduces conflict misses. Neither can eliminate compulsory misses, though prefetching can hide their latency by fetching data before it is demanded."

- question: "A cold (compulsory) miss occurs on the first access to a memory block and cannot be eliminated by increasing cache size or associativity."
  type: true-false
  answer: true
  explanation: "Compulsory misses are unavoidable because they represent data that has genuinely never been in the cache. No matter how large or how associative the cache, the first time you access a block it will be a miss — there is nothing to hit. The three-C miss taxonomy (Compulsory, Capacity, Conflict) is precisely useful because it separates what you can fix (capacity misses with more cache, conflict misses with more associativity) from what you fundamentally cannot (compulsory misses, short of prefetching)."

- question: "Explain the conflict miss problem in direct-mapped caches and describe how set-associative design alleviates it."
  type: short-answer
  answer: "In a direct-mapped cache, each memory address maps to exactly one cache line (by the index bits). If two frequently accessed blocks share the same index — because their addresses differ by a multiple of the cache size — each access evicts the other, causing repeated misses even when most of the cache is empty. Set-associative design places multiple ways in each set, so a block can occupy any of N lines within its set. This means N blocks with the same index can coexist in cache simultaneously, dramatically reducing conflict evictions."
  explanation: "The direct-mapped conflict problem is deterministic and reproducible — it happens whenever two hot addresses are congruent modulo the cache size. With 4-way set associativity, you need at least 5 competing addresses mapping to the same set to cause an eviction, versus just 2 in direct-mapped. This is why most modern L1 caches are 4- to 8-way set-associative: the conflict miss reduction is substantial, the parallel comparator cost (4–8 comparisons per access) is manageable, and the latency overhead is minimal compared to a full main memory access."
```

## Explainer

From the memory hierarchy overview, you know the fundamental problem: processors are fast and main memory is slow, with a gap of 50–200x in access time. Cache memory solves this by keeping a small, fast copy of recently used data close to the processor. The design question is *how* to organize this small, fast memory — which determines how addresses map to cache locations, how quickly data can be found, and what happens when the cache is full.

Every memory address is split into three fields by the cache hardware: the **offset** (which byte within a cache line), the **index** (which cache set to look in), and the **tag** (which identifies the specific memory block stored there). In a **direct-mapped cache**, each memory block maps to exactly one cache line — determined by the index bits. This is the simplest and fastest design: the hardware uses the index to go directly to one line, compares the stored tag with the address's tag, and either hits or misses with no search needed. The problem is **conflict misses**: two frequently used addresses that happen to map to the same line keep evicting each other, even if most of the cache is empty. Imagine two arrays whose base addresses differ by exactly the cache size — every access to one evicts the other.

A **fully associative cache** is the opposite extreme: any block can go in any line. There are no conflict misses, because a new block can always go wherever there is space. But every access requires comparing the address tag against *every* tag in the cache simultaneously. This requires parallel comparator hardware for each line, which is expensive in area and power. Fully associative caches are practical only when they are very small (like TLBs with 32–64 entries).

The practical compromise is a **set-associative cache**. The cache is divided into sets, each containing multiple **ways** (lines). The index bits select the set, and the tag is compared against all ways within that set. A 4-way set-associative cache, for example, allows each address to reside in any of 4 lines within its set. This dramatically reduces conflict misses compared to direct-mapped (since you need 4+ competing addresses to cause eviction, not just 2), while keeping the comparator cost manageable (only 4 comparisons per access instead of hundreds). Most modern L1 caches are 4- to 8-way set-associative, balancing hit rate against access latency and power.

The three types of cache misses — **compulsory** (first access to a block), **capacity** (the working set exceeds cache size), and **conflict** (multiple blocks compete for the same set) — are the framework for evaluating any cache design. Increasing cache size reduces capacity misses. Increasing associativity reduces conflict misses. Neither can eliminate compulsory misses, though prefetching can hide their latency. Every real cache design is a point in this tradeoff space, optimized for the expected workload's access patterns.
