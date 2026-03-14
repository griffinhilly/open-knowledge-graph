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
