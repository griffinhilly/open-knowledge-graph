---
id: bloom-filters-distributed-systems
title: Bloom Filters in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-hash-tables
  type: soft
builds-toward:
- merkle-trees-data-consistency
tags:
- bloom-filter
- probabilistic
- membership
- space-efficient
stage: advanced
status: draft
---

# Bloom Filters in Distributed Systems

## Core Idea
Bloom filters are space-efficient probabilistic data structures that answer 'is element X in the set?' with no false negatives and controllable false positives. In distributed systems, they efficiently share set membership information (e.g., which keys a replica has), allowing quick rejection without full data transfer.

## How It's Best Learned
Implement a simple Bloom filter (bit array + hash functions). Observe false positives as you add elements, then increase the bit array size and observe the rate drop. Use it in an anti-entropy protocol: exchange Bloom filters first to identify likely mismatches.

## Common Misconceptions
- Bloom filters have no false negatives; they can incorrectly report membership (false positive).
- Bloom filters are always smaller than the data; as false positive rates must go to zero, the bit array grows; they are small for small target false positive rates.
