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

## Explainer

A hash function's job is deceptively simple: take a key (an integer, string, or any data) and produce an index into a fixed-size array. But the quality of this mapping determines whether your hash table runs in O(1) average time or degrades toward O(n). A good hash function must satisfy two goals simultaneously — it must be **fast to compute** (since you call it on every insertion, lookup, and deletion) and it must **distribute keys uniformly** across the table (so that collisions are rare and evenly spread).

The simplest approach is the **division method**: h(k) = k mod m, where m is the table size. From your background in modular arithmetic, you know this wraps any integer into the range [0, m−1]. The choice of m matters enormously. If m is a power of 2, the hash depends only on the lowest-order bits of k, which often share patterns in real data (think of memory addresses that are always multiples of 4). Choosing m as a prime number not close to a power of 2 produces much better distribution because the modular arithmetic mixes more bits of the input into the result. The **multiplication method** — h(k) = ⌊m · (k · A mod 1)⌋ for a carefully chosen constant A (Knuth suggests A ≈ 0.6180339887, the golden ratio's fractional part) — avoids the sensitivity to m entirely and works well with power-of-2 table sizes.

Hashing strings requires combining multiple characters into a single index. The standard approach is the **polynomial rolling hash**: treat the string as a polynomial where each character is a coefficient, and evaluate it at some base. For a string s₀s₁...sₙ, compute h = (s₀ · bⁿ + s₁ · bⁿ⁻¹ + ... + sₙ) mod m, where b is a base (often 31 or 37). This can be computed incrementally using Horner's method: start with 0, and for each character, multiply the running hash by b and add the character's value. This ensures that the order of characters matters — "abc" and "cba" hash differently — and that every character contributes to the final hash value.

No matter how good your hash function is, **collisions are inevitable**. If you are mapping a large universe of possible keys (all strings, all 64-bit integers) into a small table of m slots, the pigeonhole principle guarantees that multiple keys will eventually map to the same index. The goal is statistical: a good hash function makes collisions no more likely than random chance would predict. **Universal hashing** formalizes this guarantee. A universal hash family is a collection of functions where, for any two distinct keys, the probability of collision (when a function is chosen randomly from the family) is at most 1/m. By selecting a random function from the family at startup, you get provably good expected performance regardless of the input distribution — no adversary can craft a worst-case input without knowing which function was chosen.
