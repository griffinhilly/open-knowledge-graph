---
id: linear-probing-double-hashing
title: 'Open Addressing: Linear Probing and Double Hashing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design
  type: hard
- id: hash-tables
  type: hard
tags:
- open-addressing
- hash-tables
- collision-resolution
- linear-probing
- double-hashing
stage: formal-systems
status: draft
---

# Open Addressing: Linear Probing and Double Hashing

## Core Idea
Open addressing resolves collisions by storing all keys in the table itself, probing for empty slots when collisions occur. Linear probing checks consecutive slots (h, h+1, h+2, ...), while double hashing uses a second hash function h(k, i) = (h1(k) + i*h2(k)) mod m to avoid clustering. Both achieve O(1) amortized lookup with load factor below 0.5–0.75.

## How It's Best Learned
Trace insertion and lookup with primary clustering visible in linear probing. Implement both methods and measure performance. Understand load factor and table resizing triggers. See how double hashing mitigates primary clustering better than linear probing.

## Common Misconceptions
- Open addressing is always faster than chaining (depends on load factor, cache locality, and implementation). - Linear probing is simpler and better than double hashing (double hashing avoids primary clustering).

## Explainer

You already know that a hash table maps keys to slots using a hash function, and that collisions are inevitable when two keys hash to the same index. Chaining solves this by hanging a linked list off each slot, but **open addressing** takes a fundamentally different approach: every key lives directly inside the table array. When a collision occurs, you probe — you check a sequence of alternative slots until you find an empty one. The entire question is how to choose that probe sequence.

**Linear probing** is the simplest strategy: if slot h is occupied, try h+1, then h+2, and so on (wrapping around at the end of the table). This has a beautiful advantage — because you are scanning consecutive memory locations, modern CPUs load these slots into cache lines together, giving you excellent cache performance. The downside is **primary clustering**: occupied slots clump together into long runs. Once a cluster forms, any new key that hashes anywhere into that cluster must scan to its end, and doing so extends the cluster further. The result is that as the table fills, clusters grow superlinearly and performance degrades much faster than you would expect from the load factor alone.

**Double hashing** eliminates primary clustering by making the probe step size itself depend on the key. Instead of always stepping by 1, you compute a second hash function h2(k) and probe at positions h1(k), h1(k) + h2(k), h1(k) + 2·h2(k), and so on. Because different keys that collide at the same initial slot will typically have different step sizes, their probe sequences diverge immediately rather than piling into the same cluster. The tradeoff is that you lose the cache-friendly sequential access pattern of linear probing, and you need a well-chosen h2 — it must never return zero, and ideally h2(k) should be coprime to the table size so the probe sequence visits every slot.

The load factor α (number of entries divided by table size) governs performance for both methods. For linear probing, the expected number of probes for a successful search is roughly 1/(1 − α), which explodes as α approaches 1. Double hashing performs better under high load because its probes are spread more uniformly, but both methods degrade as the table fills. In practice, open-addressing tables resize (typically doubling) when α exceeds a threshold — usually 0.5 for linear probing and 0.7 for double hashing. The key engineering insight is that open addressing trades the pointer overhead and allocation cost of chaining for simpler memory layout and better cache behavior, but demands careful load management to avoid the clustering pathologies that make probe sequences long.
