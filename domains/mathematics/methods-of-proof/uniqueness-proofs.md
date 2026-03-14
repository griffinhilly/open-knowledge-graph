---
id: uniqueness-proofs
title: Uniqueness Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: existence-proofs
  type: hard
builds-toward:
- injective-surjective-bijective
tags:
- uniqueness
- existence-and-uniqueness
- proof-technique
stage: formal-systems
status: validated
---

# Uniqueness Proofs

## Core Idea
A uniqueness proof shows that if an object satisfying some property exists, it is the only one. The standard technique is to assume two objects a and b both satisfy the property and then prove a = b. Uniqueness proofs commonly appear after existence proofs (together they establish ∃!x P(x), 'there exists a unique x') and are ubiquitous in algebra and analysis — for example, unique inverses, unique limits, or unique prime factorizations.

## How It's Best Learned
Practice with: uniqueness of additive identity in the integers, uniqueness of prime factorization (at least the uniqueness part). Stress the structure: assume x and y both satisfy P, and derive x = y.

## Common Misconceptions
- Proving existence and neglecting the uniqueness argument entirely when ∃! is required.
- Assuming uniqueness follows from existence in all cases — it does not.
- Making circular arguments by simply restating that only one solution is possible.
