---
id: hash-tables
title: Hash Tables
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: hard
- id: modular-arithmetic
  type: soft
- id: amortized-analysis
  type: soft
builds-toward:
- tries
- memoization-and-tabulation
tags:
- hash-table
- hashing
- collision
- dictionary
- key-value
stage: formal-systems
status: validated
---
# Hash Tables

## Core Idea
A hash table stores key-value pairs and supports O(1) average-case insertion, deletion, and lookup. A hash function maps keys to array indices; since the key domain is typically larger than the table size, collisions (two keys mapping to the same index) are inevitable. Common collision resolution strategies are chaining (each slot holds a linked list) and open addressing (probe for the next open slot). A good hash function distributes keys uniformly; poor hash functions lead to many collisions and degrade performance to O(n).

## How It's Best Learned
Implement a simple hash table with chaining from scratch. Experiment with different hash functions and load factors to observe their effect on collision rates. Then examine how Python's dict handles resizing.

## Common Misconceptions
- O(1) average case assumes a good hash function and a low load factor; worst case is O(n) with many collisions.
- Hash tables do not preserve insertion order in most implementations (Python 3.7+ dicts are an exception).
- Hash tables and hash sets are distinct: a set stores only keys; a map stores key-value pairs.

## Questions

```yaml
- question: "A hash table has 10 slots and currently holds 9 items (load factor = 0.9). What is the most accurate characterization of its performance risk?"
  type: multiple-choice
  options:
    - "O(1) is still guaranteed because the hash function is deterministic"
    - "The high load factor increases collision probability, risking O(n) operations if collisions cluster"
    - "Performance is unaffected; only the hash function quality matters, not the load factor"
    - "The table must immediately resize or all insert operations will fail"
  answer: 1
  explanation: "Load factor measures how full the table is. As load factor approaches 1, collisions become frequent even with a good hash function — many keys compete for few slots. In chaining, long lists form; in open addressing, many probe steps are needed. Most implementations resize (typically by doubling) when load factor exceeds a threshold (often 0.7–0.75) to keep average-case O(1) realistic."

- question: "Hash tables always preserve the insertion order of keys."
  type: true-false
  answer: false
  explanation: "In most hash table implementations, keys are placed at array indices determined by their hash values, not insertion order, so retrieval order is unpredictable. Python 3.7+ dicts happen to preserve insertion order as an implementation detail (now part of the language spec), but this is an exception — not a property of hash tables in general. Relying on hash table ordering in other languages (Java's HashMap, C++ unordered_map) is a bug."

- question: "Why is worst-case O(n) lookup possible in a hash table even when the hash function is perfectly uniform on average?"
  type: short-answer
  answer: "An adversary (or unlucky input) can supply keys that all hash to the same slot. With chaining, that slot's linked list grows to length n, and lookup must scan the entire list. With open addressing, the probe sequence degrades similarly. Uniform average-case performance assumes keys are effectively random with respect to the hash function — a condition that does not hold for adversarial or poorly distributed inputs."
  explanation: "This is why cryptographic hash functions or randomized hash functions (like universal hashing) are used in security-sensitive contexts: an attacker who knows the hash function can craft inputs that cause O(n) behavior, a technique called hash flooding. Python uses randomized hash seeds at startup (since 3.3) to prevent this attack."
```

## Explainer

You already know that arrays give O(1) access by index — if you know the position, retrieval is instant. But what if you want to look things up by name rather than position? Hash tables solve exactly this problem: they let you store and retrieve values using arbitrary keys (strings, integers, objects) in O(1) average time.

The mechanism is elegant: a hash function converts any key into an integer, and that integer (modulo the table size) becomes the array index. For example, the key `"alice"` might hash to 42, and with a table of 100 slots, she is stored at index 42. Lookup is then O(1): hash the key, go to that index, done. The challenge is that the key space is typically enormous (all possible strings, for instance) while the table size is small, so many keys inevitably map to the same index — a collision. This is not a failure; it is expected and must be handled.

The two dominant collision resolution strategies are chaining and open addressing. Chaining stores a linked list at each slot; colliding entries are appended to the list. Open addressing keeps the table flat: on collision, the algorithm probes a sequence of other slots (linear probing, quadratic probing, or double hashing) until it finds an empty one. Chaining handles high load factors gracefully; open addressing has better cache performance because everything stays in the array. The choice between them is a real engineering tradeoff.

Performance degrades when the load factor (items / slots) grows too high. With many items and few slots, collisions become frequent and collision chains grow long, pushing lookup toward O(n). This is why hash tables resize — typically doubling the array size and rehashing all entries — when the load factor exceeds a threshold. The resizing itself is O(n), but it happens infrequently enough that the average cost per insertion is still O(1), which is an amortized analysis result you may have seen in that prerequisite topic.

A subtle misconception worth addressing: the O(1) claim assumes a good hash function and a low load factor. A bad hash function that maps all keys to the same slot gives O(n) always. And because adversaries can sometimes craft inputs that break a fixed hash function, production systems often use randomized hash seeds — so that even if an attacker knows your table size, they cannot predict which keys will collide. This is why Python randomizes its hash seed at startup.
