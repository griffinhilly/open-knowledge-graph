---
id: extreme-value-theorem-rigorous
title: Extreme Value Theorem (Proof via Compactness)
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: compact-sets
  type: hard
builds-toward:
- uniform-continuity-compact-sets
tags:
- extreme-value
- compactness
- maxima-minima
stage: advanced
status: draft
---

# Extreme Value Theorem (Proof via Compactness)

## Core Idea
The Extreme Value Theorem states that a continuous function on a compact set attains its maximum and minimum values. The proof proceeds in two steps: first, the continuous image of a compact set is compact (since compactness is preserved under continuous maps); second, compact subsets of ℝ are closed and bounded by the Heine-Borel theorem, so they contain their supremum and infimum. This theorem is fundamental because it guarantees that optimization problems on closed bounded intervals have solutions. Without compactness, continuous functions may approach a supremum without attaining it, as shown by f(x) = 1/x on (0, 1].

## How It's Best Learned
First prove the supporting lemma that continuous images of compact sets are compact, then assemble the full proof. Studying counterexamples—continuous functions on open or unbounded domains that fail to attain extrema—solidifies understanding of why each hypothesis is necessary.

## Common Misconceptions
Students sometimes think continuity alone guarantees extrema, forgetting that the domain must be compact. The theorem also does not say where the extrema occur—they might be at interior points or boundary points.

