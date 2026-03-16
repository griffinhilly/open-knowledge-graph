---
id: hash-table-collision-resolution-open-addressing
title: 'Hash Tables: Collision Resolution by Open Addressing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design-universal
  type: hard
- id: hash-tables
  type: soft
tags:
- hash-table
- open-addressing
- collision
stage: formal-systems
status: draft
---

# Hash Tables: Collision Resolution by Open Addressing

## Core Idea
Open addressing probes for an empty slot when collision occurs. Linear probing (i+1, i+2, ...) is simple but suffers clustering. Quadratic probing (i+1², i+2², ...) and double hashing (second hash function) reduce clustering. Load factor α must stay low (< 0.5–0.75).

## Explainer

From your study of hash functions and hash tables, you know that a hash function maps keys to array indices and that collisions — two different keys mapping to the same index — are inevitable when the key space is larger than the table. The question is what to do when a collision occurs. In **open addressing**, the answer is: look for another empty slot *within the same array*. Unlike chaining (which stores colliding keys in linked lists), open addressing keeps everything in a single contiguous array, which gives it excellent **cache performance** since the CPU can prefetch nearby slots.

**Linear probing** is the simplest scheme: if slot h(k) is occupied, try h(k)+1, then h(k)+2, and so on (wrapping around at the end). It is cache-friendly because the probe sequence accesses consecutive memory locations. However, it suffers from **primary clustering** — occupied slots tend to clump together into long runs. Once a cluster forms, any new key that hashes into any position within the cluster will extend it further, making the cluster grow faster than expected. As the table fills up, these clusters merge into massive contiguous blocks, and the expected number of probes per operation grows sharply.

**Quadratic probing** addresses clustering by spacing out the probe sequence: try h(k)+1², h(k)+2², h(k)+3², and so on. Because the jumps grow larger, keys that collide at the same initial slot spread across the table rather than piling up in adjacent cells. This eliminates primary clustering but introduces **secondary clustering** — keys with the same hash value still follow the same probe sequence, so they compete with each other. **Double hashing** goes further by using a second, independent hash function to determine the probe step: the sequence is h₁(k), h₁(k)+h₂(k), h₁(k)+2·h₂(k), and so on. Since different keys (even those with the same h₁ value) will typically have different h₂ values, both primary and secondary clustering are eliminated. The probe sequences are effectively unique per key.

The **load factor** α = n/m (number of stored keys divided by table size) is the critical performance parameter. For linear probing with a good hash function, the expected number of probes for a successful search is roughly (1 + 1/(1-α)²)/2. At α = 0.5, this is about 2.5 probes — fast. At α = 0.9, it jumps to about 50 probes — unacceptable. This is why open-addressing tables resize (typically doubling) when α exceeds a threshold, commonly 0.5 for linear probing or 0.75 for double hashing. Deletion is also tricky: you cannot simply empty a slot, because that would break probe sequences for keys that were inserted after and probed past that slot. Instead, deleted slots are marked with a **tombstone** sentinel value that tells searches to keep probing but allows insertions to reuse the space. Accumulating too many tombstones degrades performance, which is another reason periodic resizing (which eliminates tombstones) is important.
