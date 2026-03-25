---
id: hash-table-collision-resolution-chaining
title: 'Hash Tables: Collision Resolution by Chaining'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design-properties
  type: hard
- id: hash-tables
  type: soft
tags:
- hash-table
- chaining
- collision
stage: formal-systems
status: validated
---

# Hash Tables: Collision Resolution by Chaining

## Core Idea
Chaining stores colliding keys in a linked list at each bucket. Search/insert/delete is O(1 + α) expected, where α = n/m is the load factor. High α increases average chain length; rehashing when α > threshold maintains performance.

## Questions

```yaml
- question: "A chained hash table has m=100 buckets and n=400 keys, distributed uniformly. What is the expected time to search for a key?"
  type: multiple-choice
  options:
    - "O(1) — hashing always gives constant-time lookup regardless of how many keys are stored"
    - "O(log n) — chains are kept sorted for binary search"
    - "O(1 + n/m) — constant time to find the bucket, plus traversing an average chain of length 4"
    - "O(n) — in the worst case all keys collide, so the average must be O(n)"
  answer: 2
  explanation: "Expected search time under chaining is O(1 + α) where α = n/m is the load factor. Here α = 400/100 = 4, so expected time is O(5) = O(n/m). Option A is the misconception: O(1) only holds when α is bounded by a constant. Option D confuses worst case (all keys collide) with expected case under uniform hashing."

- question: "Why does deletion in a chained hash table avoid the 'tombstone marker' complication found in open addressing?"
  type: multiple-choice
  options:
    - "Chaining rehashes immediately after every deletion, so no marker is needed"
    - "Chaining does not support deletion; keys must remain until a full rehash"
    - "Deleted nodes are simply unlinked from their chain, leaving other chains and probe sequences unaffected"
    - "Chaining uses doubly-linked lists, and tombstones are only required in singly-linked structures"
  answer: 2
  explanation: "In open addressing, deleting a key from a probe sequence would break the chain for subsequent lookups — a tombstone marks the slot as 'was occupied' so probing continues past it. In chaining, each bucket's linked list is independent; removing a node from the list does not affect any other bucket or probe sequence. This is one of chaining's practical advantages over open addressing."

- question: "In a chained hash table, inserting a new key always takes O(1) time regardless of the current load factor."
  type: true-false
  answer: true
  explanation: "Insertion under chaining is O(1): compute the hash (O(1)) and prepend the new key to the front of the target bucket's list (O(1)). Unlike search, insertion never needs to traverse the chain — it always goes to the front. The load factor affects search and delete time (which must traverse the chain), but not insertion time."

- question: "A chained hash table with load factor α = 8 will produce incorrect search results because the chains have overflowed."
  type: true-false
  answer: false
  explanation: "Chaining degrades gracefully — there is no 'overflow.' When α = 8, expected search time is O(9), which is slow but correct. The linked lists grow without bound; they never become invalid. This is in contrast to open addressing, where performance degrades rapidly and fails entirely at α = 1. High α is a performance problem, not a correctness problem."

- question: "Explain why implementations rehash a chained hash table when the load factor exceeds a threshold, rather than simply allowing chains to grow indefinitely."
  type: short-answer
  answer: "As α grows, expected chain length grows proportionally, degrading search from O(1) to O(n) in the extreme. Rehashing — allocating a larger array and redistributing keys — resets α to a low value, restoring O(1) expected performance. Although rehashing costs O(n) per event, it occurs infrequently enough that the amortized cost per insertion remains O(1)."
  explanation: "The load factor is the single number governing performance: O(1 + α) search means doubling α doubles expected search time. Without rehashing, a table that starts efficient becomes a slow linear scan as more keys are inserted. The amortized analysis (doubling the array means rehashing occurs at sizes 1, 2, 4, 8, ... so the total work is O(1 + 2 + 4 + ... + n) = O(2n) = O(n) spread over n insertions) shows the strategy is efficient overall."
```

## Explainer

From your study of hash functions, you know that a hash function maps keys to array indices (buckets), enabling O(1) expected-time lookups. But no matter how good the hash function is, **collisions** — two different keys mapping to the same bucket — are inevitable once the number of stored keys approaches or exceeds the number of buckets. The **chaining** strategy handles collisions in the most intuitive way: each bucket holds not a single key, but a linked list (or other collection) of all keys that hash to that index. When a collision occurs, the new key is simply appended to the list at that bucket.

The operations under chaining are straightforward. To **insert** a key, compute its hash to find the bucket, then prepend the key to that bucket's list — O(1) time. To **search** for a key, hash it to find the bucket, then walk the linked list comparing keys until you find a match or reach the end. To **delete**, search for the key and remove it from the list. The cost of search and delete depends on the length of the chain at the target bucket. If keys are distributed uniformly across m buckets and there are n total keys, the expected chain length is **α = n/m**, called the **load factor**. This means search takes O(1 + α) expected time: O(1) to compute the hash and access the bucket, plus O(α) to traverse the chain.

The load factor is the single most important number governing a chained hash table's performance. When α is small (say, 0.5 to 1.0), most chains are very short — zero or one elements — and operations are effectively O(1). As α grows, chains lengthen and performance degrades toward O(n) in the extreme case where all keys land in the same bucket. To prevent this, implementations **rehash** when α crosses a threshold: allocate a new, larger array (typically double the size), recompute the hash for every existing key, and insert them into the new array. This is an O(n) operation, but it happens infrequently enough that the **amortized** cost of insertion remains O(1). The choice of rehash threshold balances memory usage against chain length — a lower threshold wastes more space but keeps chains shorter.

Chaining has several practical advantages over its main alternative, open addressing (where colliding keys probe for empty slots within the array itself). Chaining degrades gracefully as the load factor increases — performance worsens linearly rather than catastrophically. Deletion is simple and does not create complications like "tombstone" markers. And the chains can use any collection type: a linked list is simplest, but high-performance implementations sometimes use balanced BSTs (as Java's HashMap does for long chains) or dynamic arrays for better cache locality. The tradeoff is that each chain node requires a pointer, adding memory overhead and reducing cache friendliness compared to open addressing for low load factors. Understanding chaining gives you a clear mental model of how hash tables handle the collision problem, and sets the stage for studying open addressing as the alternative approach.
