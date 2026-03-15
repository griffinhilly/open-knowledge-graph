---
id: bloom-filter-probabilistic-membership
title: 'Bloom Filters: Space-Efficient Probabilistic Set Membership'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-tables
  type: hard
- id: hash-function-design-properties
  type: soft
- id: probability
  type: soft
tags:
- hashing
- probabilistic
- memory
stage: formal-systems
status: draft
---

# Bloom Filters: Space-Efficient Probabilistic Set Membership

## Core Idea
A Bloom filter uses a bit array and k independent hash functions. To insert, set k bits; to test membership, check if all k bits are set. False positives are possible (k bits set by other elements) but false negatives are not. Space is O(n) bits regardless of element size.

## How It's Best Learned
Implement a Bloom filter, measure false positive rates with different k and table sizes, and use it for a practical problem (e.g., checking if a URL has been visited). Compare space to a hash set.

## Common Misconceptions
- Thinking Bloom filters have no false positives; they only guarantee false negatives are impossible.
- Not choosing k optimally; k ≈ (m/n) ln 2 minimizes false positives for m bits and n elements.
- Assuming Bloom filters are slower than hash tables; they're often faster due to better cache locality.
