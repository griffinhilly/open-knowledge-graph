---
id: injections-surjections-bijections-classification
title: Injections, Surjections, and Bijections
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-mappings-formal
  type: hard
builds-toward:
- cardinality-and-equinumerosity
tags:
- injective
- surjective
- bijective
- one-to-one
- onto
stage: formal-systems
status: draft
---

# Injections, Surjections, and Bijections

## Core Idea
An injection preserves distinctness: f(a) = f(b) implies a = b. A surjection covers the codomain: every b ∈ B equals f(a) for some a. A bijection is both injective and surjective, establishing a perfect one-to-one correspondence. Bijections are invertible and preserve cardinality across sets.

## How It's Best Learned
Use definitions directly to prove properties. For example, f(x) = 2x on ℝ is bijective; f(x) = x² on ℝ is neither injective nor surjective, but becomes bijective when restricted to [0,∞) → [0,∞). Construct counterexamples to distinguish the concepts.

## Common Misconceptions
- Confusing 'onto' (surjective) with 'one-to-one' (injective). - Thinking a function must be defined by a formula; what matters is the assignment rule. - Assuming bijections exist only between finite sets (false; bijections exist between infinite sets of equal cardinality).
