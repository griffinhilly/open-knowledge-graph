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

## Questions

```yaml
- question: "A direct-mapped cache has 16 lines. Two frequently used arrays, A and B, happen to map to the same cache line. What happens when the program alternates between accessing elements of A and B?"
  type: multiple-choice
  options:
    - "The cache handles this efficiently by storing both arrays in the same line using compression"
    - "Every access causes a conflict miss: A evicts B, then B evicts A, even though the other 15 lines are empty"
    - "The CPU detects the conflict and automatically promotes the cache to 2-way associativity"
    - "The cache falls back to fully associative mode for those two addresses only"
  answer: 1
  explanation: "This is the classic conflict miss in a direct-mapped cache. Because each address maps to exactly one line, A and B compete for the same location regardless of how much other cache space is available. Every time A is accessed, it evicts B. Every time B is accessed, it evicts A. The result is 100% miss rate for these accesses despite the majority of the cache being empty. This is the fundamental weakness of direct-mapped design — capacity is not the constraint, placement rigidity is."

- question: "Why is fully associative mapping impractical for large L1 caches despite eliminating conflict misses entirely?"
  type: multiple-choice
  options:
    - "Fully associative caches require more bits per address tag than direct-mapped caches"
    - "On every access, the hardware must compare the requested address tag against every stored tag simultaneously, requiring a comparator per cache line — infeasible at thousands of lines"
    - "Fully associative caches cannot use LRU replacement, limiting their hit rates"
    - "Fully associative caches require the CPU to pause for one clock cycle per cache line checked, making lookups too slow"
  answer: 1
  explanation: "Full associativity requires simultaneous comparison of the incoming address tag against all stored tags to find a match in one cycle. This demands a hardware comparator for every cache line. For a TLB with 64 entries, 64 comparators is feasible. For an L1 cache with 4,096 lines, 4,096 parallel comparators would be enormous and power-hungry. The hardware cost scales linearly with cache size, which is why fully associative design is reserved for tiny, critical structures like TLBs."

- question: "In a direct-mapped cache, a conflict miss can occur even when most of the cache lines are empty."
  type: true-false
  answer: true
  explanation: "This is the core weakness of direct-mapped caches. Because each memory address maps to exactly one cache line, two addresses that happen to map to the same line will evict each other on every access — regardless of how many other lines are unused. The cache's overall occupancy is irrelevant to conflict miss frequency. This is why the miss rate of a direct-mapped cache can sometimes be worse than a smaller fully associative cache: it's not about total capacity, it's about placement flexibility."

- question: "Doubling cache associativity always doubles cache performance — a 4-way set-associative cache is always twice as fast as a 2-way cache."
  type: true-false
  answer: false
  explanation: "Associativity shows strongly diminishing returns. Going from 1-way (direct-mapped) to 2-way typically cuts conflict misses roughly in half — a substantial improvement. Going from 2-way to 4-way helps further but by a smaller margin. Beyond 8-way, improvements are minimal for most workloads, while hardware complexity and power continue growing. Performance depends on the specific access patterns: a workload with few conflicts sees little benefit from higher associativity; one with many conflicts sees large gains up to a point."

- question: "Explain why set-associative caches are described as a 'middle ground' between direct-mapped and fully associative designs. What does each design trade off?"
  type: short-answer
  answer: "Direct-mapped: every address maps to exactly one line — fast lookup (check one location) but vulnerable to conflict misses when multiple addresses compete for the same line. Fully associative: any address can go anywhere — no conflict misses but requires comparing every stored tag on every access, which is hardware-intensive and impractical for large caches. Set-associative divides the cache into sets; each address maps to one set (like direct-mapped, so lookup only checks N lines), but can occupy any of N lines within that set (like fully associative within the set, reducing conflicts). It limits search cost while gaining placement flexibility."
  explanation: "The design space of cache associativity is a continuous tradeoff between conflict miss rate and lookup hardware complexity. Direct-mapped minimizes hardware (one comparator) but maximizes conflicts. Fully associative minimizes conflicts but maximizes hardware. N-way set-associative uses N comparators per set and tolerates N competing addresses before conflicts arise. Most real L1 caches settle at 4-way or 8-way because that's where the conflict-miss curve flattens and the hardware cost is still acceptable."
```

## Explainer

From your study of cache design principles, you know that a cache stores recently accessed data closer to the processor to exploit temporal and spatial locality. The question **cache associativity** answers is: when a new block arrives from main memory, *where* in the cache can it be placed? This placement rule has profound implications for both hit rate and hardware complexity.

A **direct-mapped cache** is the simplest design. Each memory address maps to exactly one cache line, determined by the formula `cache_line = (block_address) mod (number_of_lines)`. Think of it like an apartment building where your unit number is determined entirely by the last two digits of your social security number — you have no choice of where to live. The hardware only needs to check one location, making lookups extremely fast. But the fatal flaw is **conflict misses**: if two frequently accessed addresses happen to map to the same cache line, they evict each other repeatedly, regardless of how much empty space exists elsewhere in the cache. Two arrays whose base addresses differ by exactly the cache size will thrash on every access.

A **fully associative cache** goes to the opposite extreme: any memory block can be stored in any cache line. This eliminates conflict misses entirely — a block is only evicted when the entire cache is full. But the hardware cost is severe: on every access, the cache must compare the requested address tag against *every* stored tag simultaneously, requiring a comparator for each cache line. This is feasible only for very small caches (like TLBs with 32–64 entries), not for the thousands of lines in a typical L1 data cache.

**Set-associative caches** split the difference. The cache is divided into sets, and each memory address maps to exactly one set (like direct-mapped), but within that set, the block can occupy any of N lines (like fully associative). A **4-way set-associative** cache, for instance, has 4 lines per set — the hardware needs only 4 comparators per lookup instead of thousands, yet conflict misses drop dramatically compared to direct-mapped. The address is split into three fields: the **offset** (which byte within a block), the **index** (which set), and the **tag** (which block within that set's mapping). Increasing associativity from 1-way (direct-mapped) to 2-way typically cuts conflict misses by roughly half; going from 2-way to 4-way helps further but with diminishing returns. Most modern L1 caches use 4-way or 8-way associativity, and the replacement policy you studied earlier (LRU, random, etc.) determines which line within a set gets evicted when a new block arrives.
