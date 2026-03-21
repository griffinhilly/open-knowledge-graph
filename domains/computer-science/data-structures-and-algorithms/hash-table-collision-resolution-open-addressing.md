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

## Questions

```yaml
- question: "A hash table uses linear probing. After inserting many keys, you delete one by simply setting its slot to empty. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "No consequence — the slot is now available and future insertions will work correctly"
    - "Subsequent searches for keys that probed past this slot will terminate prematurely, failing to find them"
    - "The load factor drops, which improves performance"
    - "The next insertion at this position will automatically repair the probe sequence"
  answer: 1
  explanation: "Open addressing relies on unbroken probe sequences. If a key K was inserted by probing past slot S to reach slot T, then emptying slot S breaks the path — a search for K will probe to the empty S and conclude K is absent, even though K exists at T. This is why deletions use a tombstone marker: a special value that tells searches 'keep probing' but tells insertions 'you can reuse this slot.' Option A is the classic mistake students make when they forget that open addressing chains multiple keys through the same probe path."

- question: "A hash table has load factor α = 0.9 using linear probing. Which adjustment would most dramatically improve lookup performance?"
  type: multiple-choice
  options:
    - "Switch to a better hash function"
    - "Resize the table to reduce α to around 0.5"
    - "Sort the stored keys so binary search can be used"
    - "Use longer keys to reduce hash collisions"
  answer: 1
  explanation: "For linear probing, expected probes per successful search scales roughly as (1 + 1/(1-α)²)/2. At α=0.9, this is ~50 probes; at α=0.5, it's ~2.5 probes — a 20× improvement. The load factor is the dominant performance lever. A better hash function helps marginally with clustering but cannot overcome the fundamental explosion caused by a table that is 90% full. Sorting is inapplicable since the whole point of hashing is O(1) access, not binary search."

- question: "Double hashing eliminates both primary and secondary clustering, unlike linear or quadratic probing."
  type: true-false
  answer: true
  explanation: "Primary clustering (from linear probing) occurs when keys that collide at the same initial slot pile into adjacent cells, creating long runs. Quadratic probing breaks this by spacing probes farther apart, but keys sharing the same initial hash value still follow the same probe sequence — secondary clustering. Double hashing uses a second independent hash function h₂(k) to determine step size, so even keys with the same h₁ value diverge onto different probe paths. Both clustering forms are eliminated, giving effectively uniform probing at the cost of slightly more computation per probe."

- question: "A well-designed hash table using open addressing can safely maintain a load factor of 0.95 without significant performance degradation."
  type: true-false
  answer: false
  explanation: "Open-addressing performance degrades sharply as load factor approaches 1. At α=0.95 with linear probing, expected probes per lookup can exceed 200 — effectively destroying O(1) behavior. This is why practical implementations resize (typically doubling the table) when α exceeds a threshold: 0.5–0.75 for linear probing, up to 0.75 for double hashing. Chaining-based tables tolerate higher load factors better because their probe sequences don't share the same fixed array."

- question: "Why can't you simply empty a slot when deleting a key from an open-addressing hash table, and what is the standard solution?"
  type: short-answer
  answer: "Because open addressing stores keys along probe sequences that pass through other slots. A key K inserted after probing past slot S now sits beyond S in the probe path. If S is emptied, any future search for K will reach S, see an empty slot, and conclude K is absent — a false negative. The standard solution is to mark deleted slots with a tombstone sentinel. Tombstones tell search to continue probing (the chain isn't broken) but tell insertion to reuse the space (it counts as empty for storage). Periodic resizing clears tombstones and rebuilds the table cleanly."
  explanation: "This is the central subtlety of open addressing that distinguishes it from chaining. In chaining, deleting a node from a linked list has no effect on other nodes. In open addressing, every slot is part of one or more probe paths for keys that may have displaced themselves here or probed past here. The tombstone approach preserves probe-path integrity for reads while recovering space for writes. Accumulated tombstones degrade performance because searches must probe past them, which is why resizing (not just deletion) is part of table maintenance."
```

## Explainer

From your study of hash functions and hash tables, you know that a hash function maps keys to array indices and that collisions — two different keys mapping to the same index — are inevitable when the key space is larger than the table. The question is what to do when a collision occurs. In **open addressing**, the answer is: look for another empty slot *within the same array*. Unlike chaining (which stores colliding keys in linked lists), open addressing keeps everything in a single contiguous array, which gives it excellent **cache performance** since the CPU can prefetch nearby slots.

**Linear probing** is the simplest scheme: if slot h(k) is occupied, try h(k)+1, then h(k)+2, and so on (wrapping around at the end). It is cache-friendly because the probe sequence accesses consecutive memory locations. However, it suffers from **primary clustering** — occupied slots tend to clump together into long runs. Once a cluster forms, any new key that hashes into any position within the cluster will extend it further, making the cluster grow faster than expected. As the table fills up, these clusters merge into massive contiguous blocks, and the expected number of probes per operation grows sharply.

**Quadratic probing** addresses clustering by spacing out the probe sequence: try h(k)+1², h(k)+2², h(k)+3², and so on. Because the jumps grow larger, keys that collide at the same initial slot spread across the table rather than piling up in adjacent cells. This eliminates primary clustering but introduces **secondary clustering** — keys with the same hash value still follow the same probe sequence, so they compete with each other. **Double hashing** goes further by using a second, independent hash function to determine the probe step: the sequence is h₁(k), h₁(k)+h₂(k), h₁(k)+2·h₂(k), and so on. Since different keys (even those with the same h₁ value) will typically have different h₂ values, both primary and secondary clustering are eliminated. The probe sequences are effectively unique per key.

The **load factor** α = n/m (number of stored keys divided by table size) is the critical performance parameter. For linear probing with a good hash function, the expected number of probes for a successful search is roughly (1 + 1/(1-α)²)/2. At α = 0.5, this is about 2.5 probes — fast. At α = 0.9, it jumps to about 50 probes — unacceptable. This is why open-addressing tables resize (typically doubling) when α exceeds a threshold, commonly 0.5 for linear probing or 0.75 for double hashing. Deletion is also tricky: you cannot simply empty a slot, because that would break probe sequences for keys that were inserted after and probed past that slot. Instead, deleted slots are marked with a **tombstone** sentinel value that tells searches to keep probing but allows insertions to reuse the space. Accumulating too many tombstones degrades performance, which is another reason periodic resizing (which eliminates tombstones) is important.
