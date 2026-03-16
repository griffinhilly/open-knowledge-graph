---
id: separate-chaining-collisions
title: Separate Chaining for Hash Table Collisions
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design
  type: hard
- id: hash-tables
  type: hard
- id: linked-lists
  type: soft
tags:
- hash-tables
- chaining
- collision-resolution
- linked-lists
stage: formal-systems
status: draft
---

# Separate Chaining for Hash Table Collisions

## Core Idea
Separate chaining resolves collisions by storing colliding keys in a linked list (or other structure) at each table bucket. With n keys in m buckets, expected chain length is n/m, yielding O(1 + n/m) average lookup. Chaining simplifies deletion compared to open addressing and handles high load factors gracefully.

## How It's Best Learned
Implement a chained hash table and trace insertions with collisions. Measure average chain length and lookup time as load factor increases. Compare to open addressing: chaining is simpler and more flexible, but uses extra memory for pointers.

## Common Misconceptions
- Chaining always suffers from many collisions (performance degrades gracefully with good hash functions). - Chains must be balanced (simple chaining works; advanced structures like self-balancing trees are overkill for most uses).

## Explainer

You know from studying hash tables that a hash function maps keys to array indices, and from linked lists that nodes can be chained together via pointers. **Separate chaining** combines these two ideas to handle the inevitable problem of collisions — when two different keys hash to the same index. Instead of each array slot holding a single key-value pair, each slot holds the head of a linked list. When a new key hashes to an already-occupied slot, it simply gets appended (or prepended) to that slot's list. To look up a key, you hash it to find the correct slot, then walk the linked list comparing keys until you find a match or reach the end.

The performance of separate chaining depends on how evenly the hash function distributes keys across buckets. The **load factor** α = n/m (number of keys divided by number of buckets) represents the average chain length. With a good hash function that distributes keys uniformly, most chains stay close to this average, so lookups take O(1 + α) time — the O(1) to compute the hash and jump to the bucket, plus O(α) to scan the chain. As long as you keep α reasonable (say, below 1 or 2) by resizing the table when it gets too full, average-case operations remain effectively O(1). This is the fundamental bargain of hashing: you trade a small amount of extra space for constant-time access.

Compared to **open addressing** (the other major collision strategy, where colliding keys probe for the next empty slot), separate chaining has several practical advantages. Deletion is straightforward — just remove the node from the linked list — whereas open addressing requires tombstone markers or complex rehashing after deletions. Chaining also tolerates load factors above 1.0 gracefully: performance degrades linearly as chains grow, rather than catastrophically as open-addressed tables approach full capacity. On the other hand, chaining uses extra memory for the linked list pointers and has worse cache locality than open addressing, since following pointers can jump around in memory rather than scanning contiguous array slots.

In practice, many real-world hash table implementations use separate chaining as their default strategy. Java's `HashMap`, for instance, uses chaining and even upgrades long chains from linked lists to balanced trees (red-black trees) when a single chain exceeds a threshold — a refinement that prevents worst-case O(n) lookups if a bad hash function or adversarial input concentrates many keys in one bucket. For most applications, though, a well-chosen hash function keeps chains short enough that a simple linked list per bucket is all you need. The key insight is that separate chaining turns the collision problem into a manageable linked-list traversal problem, and the expected length of that traversal is controlled entirely by the load factor and the quality of your hash function.
