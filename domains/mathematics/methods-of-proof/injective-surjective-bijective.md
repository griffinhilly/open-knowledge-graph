---
id: injective-surjective-bijective
title: Injective, Surjective, and Bijective Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: binary-relations
  type: soft
- id: domain-and-range
  type: soft
- id: function-notation-review
  type: soft
- id: cartesian-product
  type: soft
- id: uniqueness-proofs
  type: soft
builds-toward:
- cardinality-and-countability
tags:
- injective
- one-to-one
- surjective
- onto
- bijective
- function-properties
- inverse-functions
stage: formal-systems
status: validated
---
# Injective, Surjective, and Bijective Functions

## Core Idea
A function f: A → B is injective (one-to-one) if f(a₁) = f(a₂) implies a₁ = a₂ — distinct inputs map to distinct outputs. It is surjective (onto) if for every b ∈ B there exists a ∈ A with f(a) = b — every output is hit. A bijection is both injective and surjective, establishing a perfect pairing between A and B. Bijections are central to cardinality: two sets have the same size if and only if there exists a bijection between them.

## How It's Best Learned
Test injectivity using the horizontal line test for real functions, and verify surjectivity by solving f(a) = b for an arbitrary b. Prove properties formally using definition-based arguments. Connect to inverse functions: f has an inverse if and only if f is bijective.

## Common Misconceptions
- Thinking 'one-to-one' means each output has exactly one input (that would be a function) rather than each output has at most one input.
- Confusing the codomain (declared target set) with the range (actual image) — surjectivity depends on the codomain.
- Assuming every injective function has a two-sided inverse when only a left inverse is guaranteed.
