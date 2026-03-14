---
id: cumulative-hierarchy-ranks
title: The Cumulative Hierarchy and Ranks
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: von-neumann-ordinals
  type: hard
- id: axiom-of-regularity
  type: soft
builds-toward:
- constructible-universe
- absolute-formulas-models
tags:
- cumulative-hierarchy
- ranks
- von-neumann
- foundation
stage: formal-systems
status: draft
---

# The Cumulative Hierarchy and Ranks

## Core Idea
The cumulative hierarchy V is a stratification of all sets by rank. V₀ = ∅, V_{α+1} = P(V_α), and V_λ = ⋃_{α < λ} V_α for limit λ. Every set has a rank, the least ordinal α such that the set belongs to V_α. The union V = ⋃_α V_α is the universe of all sets in standard set theory, and foundation ensures every set is in some V_α.

## How It's Best Learned
Construct V₀, V₁, V₂, ... and describe which sets appear at each level. Show hereditarily finite sets occur in V_ω. Verify that rank(x) is well-defined by transfinite induction. Discuss absoluteness: the notion of rank is absolute across models of ZFC.

## Common Misconceptions
- Confusing rank with cardinality; rank is an ordinal measuring depth, not size.
- Forgetting that V itself is a proper class, not a set, due to the Burali-Forti paradox.
