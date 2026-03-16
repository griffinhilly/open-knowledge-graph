---
id: hash-function-design-universal
title: Hash Function Design and Universal Hashing
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
builds-toward:
- hash-table-collision-resolution-chaining
- hash-table-collision-resolution-open-addressing
tags:
- hash-function
- hashing
- universal
stage: formal-systems
status: draft
---

# Hash Function Design and Universal Hashing

## Core Idea
Good hash functions distribute keys uniformly to minimize collisions. Division hashing (h(k) = k mod m), multiplication hashing, and universal hashing families (randomized) are common. Bad hashing leads to clustering and O(n) performance.

## Explainer

A hash function's job is deceptively simple: map a key (which could be any data — an integer, a string, an object) to an index in a fixed-size array. The quality of this mapping determines whether your hash table runs in O(1) average time or degrades toward O(n). A good hash function distributes keys **uniformly** across the available slots, minimizing the chance that two different keys land in the same slot (a **collision**). A bad hash function clumps keys together, creating long collision chains that turn your hash table into an expensive linked list.

The simplest approach is **division hashing**: `h(k) = k mod m`, where m is the table size. If m is 10 and your key is 47, the hash is 7. This works, but the choice of m matters enormously. If m is even, all odd keys hash to odd slots and all even keys hash to even slots — you have already lost half your distribution. If m is a power of 2, the hash depends only on the lowest-order bits of k, ignoring the rest. The standard advice is to choose m as a prime number not close to a power of 2, which forces the modular arithmetic to mix more bits of the key into the result. **Multiplication hashing** (`h(k) = floor(m × (k × A mod 1))` for a carefully chosen constant A) avoids the sensitivity to m entirely and works well with power-of-2 table sizes, making it popular in practice.

The deeper problem is that for *any* fixed hash function, an adversary (or just bad luck) can construct a set of keys that all hash to the same slot, producing worst-case O(n) behavior. **Universal hashing** solves this with randomization. Instead of choosing one hash function, you define a *family* of hash functions and randomly select one at runtime. A universal hash family guarantees that for any two distinct keys, the probability of collision is at most 1/m — no worse than if the hash values were perfectly random. A classic construction for integer keys is `h(k) = ((a × k + b) mod p) mod m`, where p is a prime larger than any key and a, b are chosen randomly at initialization. The adversary cannot construct a bad input because they do not know which function was chosen.

The choice of hash function is the foundation on which all collision resolution strategies rest. Whether you use chaining (linked lists at each slot) or open addressing (probing for empty slots), the expected number of collisions — and therefore the expected time per operation — depends directly on how uniformly your hash function distributes keys. Investing in a well-designed hash function, or using a universal family, is always cheaper than dealing with the clustering and performance degradation that a poor function produces.
