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

## Explainer

From the memory hierarchy overview, you know the fundamental problem: processors are fast and main memory is slow, with a gap of 50–200x in access time. Cache memory solves this by keeping a small, fast copy of recently used data close to the processor. The design question is *how* to organize this small, fast memory — which determines how addresses map to cache locations, how quickly data can be found, and what happens when the cache is full.

Every memory address is split into three fields by the cache hardware: the **offset** (which byte within a cache line), the **index** (which cache set to look in), and the **tag** (which identifies the specific memory block stored there). In a **direct-mapped cache**, each memory block maps to exactly one cache line — determined by the index bits. This is the simplest and fastest design: the hardware uses the index to go directly to one line, compares the stored tag with the address's tag, and either hits or misses with no search needed. The problem is **conflict misses**: two frequently used addresses that happen to map to the same line keep evicting each other, even if most of the cache is empty. Imagine two arrays whose base addresses differ by exactly the cache size — every access to one evicts the other.

A **fully associative cache** is the opposite extreme: any block can go in any line. There are no conflict misses, because a new block can always go wherever there is space. But every access requires comparing the address tag against *every* tag in the cache simultaneously. This requires parallel comparator hardware for each line, which is expensive in area and power. Fully associative caches are practical only when they are very small (like TLBs with 32–64 entries).

The practical compromise is a **set-associative cache**. The cache is divided into sets, each containing multiple **ways** (lines). The index bits select the set, and the tag is compared against all ways within that set. A 4-way set-associative cache, for example, allows each address to reside in any of 4 lines within its set. This dramatically reduces conflict misses compared to direct-mapped (since you need 4+ competing addresses to cause eviction, not just 2), while keeping the comparator cost manageable (only 4 comparisons per access instead of hundreds). Most modern L1 caches are 4- to 8-way set-associative, balancing hit rate against access latency and power.

The three types of cache misses — **compulsory** (first access to a block), **capacity** (the working set exceeds cache size), and **conflict** (multiple blocks compete for the same set) — are the framework for evaluating any cache design. Increasing cache size reduces capacity misses. Increasing associativity reduces conflict misses. Neither can eliminate compulsory misses, though prefetching can hide their latency. Every real cache design is a point in this tradeoff space, optimized for the expected workload's access patterns.
