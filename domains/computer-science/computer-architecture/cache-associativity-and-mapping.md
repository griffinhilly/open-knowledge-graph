---
id: cache-associativity-and-mapping
title: Cache Associativity and Address Mapping Strategies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-design-principles
  type: hard
- id: cache-replacement-policies
  type: soft
builds-toward:
- multilevel-cache-organization
tags:
- cache-associativity
- cache-mapping
- address-mapping
stage: formal-systems
status: draft
---

# Cache Associativity and Address Mapping Strategies

## Core Idea
Cache mapping strategy determines where a memory address can reside in the cache. Direct-mapped: each address maps to one cache location (fast but prone to conflicts). Fully associative: any address can be stored in any location (flexible but slow to search). N-way set-associative: intermediate approach, dividing the cache into sets and allowing N locations per set. Associativity increases hit rate but complexity.

## Explainer

From your study of cache design principles, you know that a cache stores recently accessed data closer to the processor to exploit temporal and spatial locality. The question **cache associativity** answers is: when a new block arrives from main memory, *where* in the cache can it be placed? This placement rule has profound implications for both hit rate and hardware complexity.

A **direct-mapped cache** is the simplest design. Each memory address maps to exactly one cache line, determined by the formula `cache_line = (block_address) mod (number_of_lines)`. Think of it like an apartment building where your unit number is determined entirely by the last two digits of your social security number — you have no choice of where to live. The hardware only needs to check one location, making lookups extremely fast. But the fatal flaw is **conflict misses**: if two frequently accessed addresses happen to map to the same cache line, they evict each other repeatedly, regardless of how much empty space exists elsewhere in the cache. Two arrays whose base addresses differ by exactly the cache size will thrash on every access.

A **fully associative cache** goes to the opposite extreme: any memory block can be stored in any cache line. This eliminates conflict misses entirely — a block is only evicted when the entire cache is full. But the hardware cost is severe: on every access, the cache must compare the requested address tag against *every* stored tag simultaneously, requiring a comparator for each cache line. This is feasible only for very small caches (like TLBs with 32–64 entries), not for the thousands of lines in a typical L1 data cache.

**Set-associative caches** split the difference. The cache is divided into sets, and each memory address maps to exactly one set (like direct-mapped), but within that set, the block can occupy any of N lines (like fully associative). A **4-way set-associative** cache, for instance, has 4 lines per set — the hardware needs only 4 comparators per lookup instead of thousands, yet conflict misses drop dramatically compared to direct-mapped. The address is split into three fields: the **offset** (which byte within a block), the **index** (which set), and the **tag** (which block within that set's mapping). Increasing associativity from 1-way (direct-mapped) to 2-way typically cuts conflict misses by roughly half; going from 2-way to 4-way helps further but with diminishing returns. Most modern L1 caches use 4-way or 8-way associativity, and the replacement policy you studied earlier (LRU, random, etc.) determines which line within a set gets evicted when a new block arrives.
