---
id: hash-function-design
title: Hash Function Design and Properties
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: modular-arithmetic
  type: soft
- id: modular-arithmetic-discrete
  type: soft
builds-toward:
- linear-probing-double-hashing
- separate-chaining-collisions
tags:
- hash-functions
- hash-tables
- uniform-distribution
- collision
stage: formal-systems
status: draft
---

# Hash Function Design and Properties

## Core Idea
A good hash function maps keys to table indices uniformly and efficiently, minimizing collisions and computing quickly. Common methods include division (h(k) = k mod m), multiplication, and polynomial rolling hash. Universal hashing provides theoretical guarantees: for random function selection, the expected number of collisions is minimized across all key distributions.

## How It's Best Learned
Design hash functions for strings (polynomial rolling hash, DJB2) and integers (multiply-and-shift). Measure collision rates empirically on diverse datasets. Study universal hashing families and understand how they bound expected collision counts.

## Common Misconceptions
- Good hash functions never produce collisions (impossible; they minimize collisions statistically). - Cryptographic hashes are best for hash tables (they're overkill; simpler, faster functions suffice).

## Questions

```yaml
- question: "A hash table uses h(k) = k mod 256. The keys stored are all 64-bit memory addresses that are multiples of 8. What problem arises?"
  type: multiple-choice
  options:
    - "Only indices 0, 8, 16, ..., 248 are ever used — 7/8 of the table is wasted and collision rates in the used slots are high"
    - "The modulo operation will be slow because 256 is a power of 2"
    - "All keys will hash to the same index because they share a common factor"
    - "No problem arises; modular hashing distributes all key patterns uniformly"
  answer: 0
  explanation: "When m is a power of 2, h(k) = k mod m depends only on the lowest-order bits of k. Keys that are multiples of 8 have their lowest 3 bits always 000, so mod 256 they take only values 0, 8, 16, ..., 248 — just 32 of the 256 possible slots. This is why choosing m as a prime not close to a power of 2 is recommended: it mixes more of the key's bits into the result, preventing structured patterns in the key set from causing systematic clustering."

- question: "A software team decides to use SHA-256 (a cryptographic hash) as their hash function for a hash table. Compared to a simpler hash like polynomial rolling hash, this choice:"
  type: multiple-choice
  options:
    - "Is unnecessarily slow — cryptographic strength is irrelevant for hash tables, which only need statistical uniformity and speed"
    - "Is ideal — SHA-256 guarantees zero collisions for any key set"
    - "Is better because it provides stronger collision resistance than non-cryptographic hashes"
    - "Is required for security — any other hash function can be exploited by an attacker"
  answer: 0
  explanation: "Hash tables need functions that are fast and distribute keys uniformly — they do not need cryptographic properties (preimage resistance, adversarial collision resistance) that SHA-256 provides. SHA-256 is hundreds of times slower than a simple polynomial hash, and that overhead compounds on every insertion and lookup. Collisions are unavoidable regardless of function choice (pigeonhole principle), so the relevant metric is statistical collision rate, not cryptographic hardness. Simpler functions like DJB2 or FNV achieve excellent distribution at a fraction of the cost."

- question: "A perfectly designed hash function will never produce collisions, as long as all keys being hashed are distinct."
  type: true-false
  answer: false
  explanation: "Collisions are unavoidable when the universe of possible keys is larger than the table size. By the pigeonhole principle, if you have more possible keys than table slots, at least two keys must map to the same index. The only way to guarantee no collisions for a specific key set is to design a perfect hash function tailored to that exact static set — which is only practical for pre-known, fixed key sets. For general-purpose hash tables, the design goal is minimizing collision probability, not eliminating it."

- question: "Universal hashing protects against adversarial inputs by randomly selecting a hash function from a family at startup, so no attacker can pre-compute a worst-case key set without knowing which function was chosen."
  type: true-false
  answer: true
  explanation: "A fixed hash function can be exploited: an adversary who knows the function can craft a key set where all keys collide, degrading O(1) expected performance to O(n). Universal hashing defeats this by randomizing the function selection. A universal hash family guarantees that for any two distinct keys, the probability of collision over the random choice of function is at most 1/m. Since the attacker doesn't know which function was selected, they cannot pre-compute a collision-inducing input set."

- question: "Why are collisions in a hash table unavoidable in theory, and what does good hash function design actually aim to achieve instead of eliminating collisions?"
  type: short-answer
  answer: "Collisions are unavoidable because hash tables map a large universe of possible keys into a small array of m slots. The pigeonhole principle guarantees that if the key universe is larger than m, at least two keys must share a slot. Good hash function design does not aim to eliminate collisions — it aims to distribute keys uniformly so collisions are no more frequent than expected by random chance. The ideal is that each key maps to any slot with equal probability 1/m, independent of other keys, minimizing expected collision rate and keeping average lookup time at O(1)."
  explanation: "The practical measure of a hash function's quality is how close to uniform its output distribution is on real-world data. A function that maps all strings starting with 'a' to index 0 is terrible for English words, even if it works fine on random data. Universal hashing provides the strongest theoretical guarantee: collision probability at most 1/m for any two keys, regardless of input distribution, because the function is randomized. Empirical designs (DJB2, FNV, MurmurHash) achieve near-uniform distribution in practice without formal guarantees but with lower overhead."
```

## Explainer

A hash function's job is deceptively simple: take a key (an integer, string, or any data) and produce an index into a fixed-size array. But the quality of this mapping determines whether your hash table runs in O(1) average time or degrades toward O(n). A good hash function must satisfy two goals simultaneously — it must be **fast to compute** (since you call it on every insertion, lookup, and deletion) and it must **distribute keys uniformly** across the table (so that collisions are rare and evenly spread).

The simplest approach is the **division method**: h(k) = k mod m, where m is the table size. From your background in modular arithmetic, you know this wraps any integer into the range [0, m−1]. The choice of m matters enormously. If m is a power of 2, the hash depends only on the lowest-order bits of k, which often share patterns in real data (think of memory addresses that are always multiples of 4). Choosing m as a prime number not close to a power of 2 produces much better distribution because the modular arithmetic mixes more bits of the input into the result. The **multiplication method** — h(k) = ⌊m · (k · A mod 1)⌋ for a carefully chosen constant A (Knuth suggests A ≈ 0.6180339887, the golden ratio's fractional part) — avoids the sensitivity to m entirely and works well with power-of-2 table sizes.

Hashing strings requires combining multiple characters into a single index. The standard approach is the **polynomial rolling hash**: treat the string as a polynomial where each character is a coefficient, and evaluate it at some base. For a string s₀s₁...sₙ, compute h = (s₀ · bⁿ + s₁ · bⁿ⁻¹ + ... + sₙ) mod m, where b is a base (often 31 or 37). This can be computed incrementally using Horner's method: start with 0, and for each character, multiply the running hash by b and add the character's value. This ensures that the order of characters matters — "abc" and "cba" hash differently — and that every character contributes to the final hash value.

No matter how good your hash function is, **collisions are inevitable**. If you are mapping a large universe of possible keys (all strings, all 64-bit integers) into a small table of m slots, the pigeonhole principle guarantees that multiple keys will eventually map to the same index. The goal is statistical: a good hash function makes collisions no more likely than random chance would predict. **Universal hashing** formalizes this guarantee. A universal hash family is a collection of functions where, for any two distinct keys, the probability of collision (when a function is chosen randomly from the family) is at most 1/m. By selecting a random function from the family at startup, you get provably good expected performance regardless of the input distribution — no adversary can craft a worst-case input without knowing which function was chosen.
