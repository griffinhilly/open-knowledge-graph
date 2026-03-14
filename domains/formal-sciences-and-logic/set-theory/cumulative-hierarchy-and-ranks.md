---
id: cumulative-hierarchy-and-ranks
title: The Cumulative Hierarchy and Set Ranks
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: natural-numbers-as-iterative-construction
  type: hard
- id: indexed-families-of-sets
  type: soft
builds-toward:
- axiom-of-regularity
- axiom-of-foundation
- constructible-universe
tags:
- hierarchy
- ranks
- foundation
stage: formal-systems
status: draft
---

# The Cumulative Hierarchy and Set Ranks

## Core Idea
The cumulative hierarchy V is defined iteratively: V₀ = ∅, V_{α+1} = 𝒫(V_α), and V_λ = ⋃_{α<λ} V_α for limit ordinals λ. Every set has a rank—the smallest ordinal α such that the set is in V_{α+1}. This formalization captures the intuition that sets are built successively from the empty set, with no circular dependencies.
