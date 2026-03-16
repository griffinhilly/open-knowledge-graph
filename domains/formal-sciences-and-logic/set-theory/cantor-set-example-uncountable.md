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

## Explainer

You already know Cantor's diagonal argument: the real numbers are uncountable because any attempted enumeration misses a real number constructed by differing from each listed entry in its nth decimal digit. The **Cantor set** C is a concrete, visualizable uncountable set with paradoxical properties that make the subtleties of uncountability tangible rather than abstract. It is constructed iteratively: start with [0, 1], remove the open middle third (1/3, 2/3), then remove the middle third of each remaining interval, and repeat infinitely. What remains after infinitely many removals is C.

The most striking fact is what gets removed versus what remains. At each stage, you remove intervals — at stage 1, one interval of length 1/3; at stage 2, two intervals of length 1/9 each; at stage n, 2^(n−1) intervals of length 3^(−n). The total length removed is the geometric series 1/3 + 2/9 + 4/27 + ··· = (1/3) / (1 − 2/3) = 1. So C has **measure zero** — in terms of "length on the line," C contributes nothing. Yet C is **uncountable**, with as many points as [0, 1] itself. The proof uses the ternary (base-3) representation: a point x ∈ [0,1] survives the construction if and only if its ternary expansion uses only the digits 0 and 2 (never 1). The map sending 0 ↦ 0 and 2 ↦ 1 defines a bijection between C and the set {0,1}^ℕ of infinite binary sequences, which is uncountable by the diagonal argument you already know.

The Cantor set is also **nowhere dense**: it contains no open interval. Every interval (a, b) ⊂ [0,1] contains a middle-third interval that was removed, so C cannot contain (a, b). Yet C is **perfect** — every point of C is a limit of other points of C. These two properties together — nowhere dense and perfect — define a **Cantor space** in topology, and the Cantor set is the prototypical example. It embeds into essentially any uncountable Polish space, which is why it appears throughout descriptive set theory.

The Cantor set demolishes two naive intuitions simultaneously. First, "big" in cardinality does not mean "big" in measure — an uncountable set can have measure zero. Second, "large" in measure does not mean "dense" — the complement of C, the removed intervals, is dense in [0,1] and has measure 1, while C itself is meager (a countable union of nowhere dense sets). These decouplings — cardinality from measure, density from measure — are foundational in real analysis and motivate the need for a formal measure theory rather than relying on cardinality or topology alone.
