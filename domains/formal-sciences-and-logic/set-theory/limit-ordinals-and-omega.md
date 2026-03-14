---
id: limit-ordinals-and-omega
title: Limit Ordinals and Omega
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: finite-ordinals-as-natural-numbers
  type: hard
- id: von-neumann-ordinals
  type: soft
builds-toward:
- transfinite-induction
- ordinal-arithmetic-and-exponentiation
tags:
- ordinals
- limit-ordinals
- omega
- successor
stage: formal-systems
status: draft
---

# Limit Ordinals and Omega

## Core Idea
Limit ordinals are ordinals α with no immediate predecessor: α is not a successor ordinal (α ≠ β+1 for any β). The smallest limit ordinal is ω = {0, 1, 2, ...}, the order type of ℕ. Every ordinal is either 0, a successor, or a limit. Limits capture the idea of 'continuing indefinitely without end.'

## How It's Best Learned
Distinguish successor ordinals (n+1) from limits (ω, ω+ω, etc.). Show that ω is the union of all finite ordinals and verify it is indeed an ordinal. Explore ω+1, ω+2, ..., 2ω as further limits and successors.

## Common Misconceptions
- Confusing limit ordinals with suprema; limits are actual sets/ordinals, not limits in a topological sense.
- Forgetting that even very large ordinals have successors; the class of ordinals has no maximum.
