---
id: hash-table-collision-resolution-chaining
title: 'Hash Tables: Collision Resolution by Chaining'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design-universal
  type: hard
- id: hash-tables
  type: soft
tags:
- hash-table
- chaining
- collision
stage: formal-systems
status: draft
---

# Hash Tables: Collision Resolution by Chaining

## Core Idea
Chaining stores colliding keys in a linked list at each bucket. Search/insert/delete is O(1 + α) expected, where α = n/m is the load factor. High α increases average chain length; rehashing when α > threshold maintains performance.

## Explainer

From your study of hash functions, you know that a hash function maps keys to array indices (buckets), enabling O(1) expected-time lookups. But no matter how good the hash function is, **collisions** — two different keys mapping to the same bucket — are inevitable once the number of stored keys approaches or exceeds the number of buckets. The **chaining** strategy handles collisions in the most intuitive way: each bucket holds not a single key, but a linked list (or other collection) of all keys that hash to that index. When a collision occurs, the new key is simply appended to the list at that bucket.

The operations under chaining are straightforward. To **insert** a key, compute its hash to find the bucket, then prepend the key to that bucket's list — O(1) time. To **search** for a key, hash it to find the bucket, then walk the linked list comparing keys until you find a match or reach the end. To **delete**, search for the key and remove it from the list. The cost of search and delete depends on the length of the chain at the target bucket. If keys are distributed uniformly across m buckets and there are n total keys, the expected chain length is **α = n/m**, called the **load factor**. This means search takes O(1 + α) expected time: O(1) to compute the hash and access the bucket, plus O(α) to traverse the chain.

The load factor is the single most important number governing a chained hash table's performance. When α is small (say, 0.5 to 1.0), most chains are very short — zero or one elements — and operations are effectively O(1). As α grows, chains lengthen and performance degrades toward O(n) in the extreme case where all keys land in the same bucket. To prevent this, implementations **rehash** when α crosses a threshold: allocate a new, larger array (typically double the size), recompute the hash for every existing key, and insert them into the new array. This is an O(n) operation, but it happens infrequently enough that the **amortized** cost of insertion remains O(1). The choice of rehash threshold balances memory usage against chain length — a lower threshold wastes more space but keeps chains shorter.

Chaining has several practical advantages over its main alternative, open addressing (where colliding keys probe for empty slots within the array itself). Chaining degrades gracefully as the load factor increases — performance worsens linearly rather than catastrophically. Deletion is simple and does not create complications like "tombstone" markers. And the chains can use any collection type: a linked list is simplest, but high-performance implementations sometimes use balanced BSTs (as Java's HashMap does for long chains) or dynamic arrays for better cache locality. The tradeoff is that each chain node requires a pointer, adding memory overhead and reducing cache friendliness compared to open addressing for low load factors. Understanding chaining gives you a clear mental model of how hash tables handle the collision problem, and sets the stage for studying open addressing as the alternative approach.
