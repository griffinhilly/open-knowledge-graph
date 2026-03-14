---
id: cantor-set-example-uncountable
title: 'The Cantor Set: An Uncountable Nowhere Dense Example'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: uncountability-by-diagonal-argument
  type: hard
- id: set-operations-union-intersection-complement
  type: soft
builds-toward:
- descriptive-set-theory-intro
- measurable-cardinals-ultra-filters
tags:
- cantor-set
- uncountable
- nowhere-dense
- topology
stage: formal-systems
status: draft
---

# The Cantor Set: An Uncountable Nowhere Dense Example

## Core Idea
The Cantor set is constructed by iteratively removing the middle third of intervals: start with [0,1], remove (1/3, 2/3), then remove the middle thirds of remaining intervals, and repeat infinitely. The result is uncountable (equinumerous with [0,1]) yet has measure zero and is nowhere dense. It illustrates the subtlety of infinite sets and motivates descriptive set theory.

## How It's Best Learned
Construct the first few iterations visually. Show that points remaining have ternary expansions with no digit 1 (base-3 representations using only 0 and 2). Prove uncountability via the bijection with {0,1}^ℕ. Compute that the complement is dense.

## Common Misconceptions
- Assuming uncountable sets must be 'large' in measure; the Cantor set is uncountable but has measure zero.
- Forgetting that removing countably many intervals from [0,1] can leave an uncountable set.
