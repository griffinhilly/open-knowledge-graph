---
id: ordinal-addition-multiplication
title: Ordinal Addition and Multiplication
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordinal-numbers-and-order
  type: hard
- id: limit-ordinals-and-omega
  type: hard
builds-toward:
- ordinal-arithmetic
- transfinite-induction
tags:
- ordinals
- arithmetic
- order
- non-commutativity
stage: formal-systems
status: draft
---

# Ordinal Addition and Multiplication

## Core Idea
Ordinal addition and multiplication are defined recursively on ordinal order. Unlike cardinal arithmetic, ordinal operations are not commutative: 1 + ω = ω but ω + 1 ≠ ω. Multiplication is defined via repeated addition, and both operations respect order: if α < β, then γ + α < γ + β.

## How It's Best Learned
Compute concrete examples: 1 + ω (append one element at the end of ω), ω + 1 (place ω first, then one element), ω · 2 (two copies of ω in sequence), 2 · ω (infinite copies of the ordinal 2). Visualize as order types of specific sets.

## Common Misconceptions
- Assuming commutativity of ordinal addition (ω + 1 ≠ 1 + ω).
- Confusing ordinal operations with cardinal operations; they differ fundamentally.
