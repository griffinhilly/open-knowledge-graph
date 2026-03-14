---
id: rices-theorem-applications
title: 'Rice''s Theorem: Deciding Properties of Programs'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: rices-theorem
  type: hard
- id: undecidability-proof-by-reduction
  type: hard
builds-toward:
- undecidability-and-gödel
tags:
- rice-theorem
- semantic-properties
- undecidability
stage: advanced
status: draft
---

# Rice's Theorem: Deciding Properties of Programs

## Core Idea
Rice's theorem states that every non-trivial semantic property of Turing machines is undecidable: there is no algorithm to determine whether a given machine computes a function with property P (where P is neither vacuously true nor false for all functions). This unifies dozens of undecidability results and shows that analyzing program behavior beyond syntax is fundamentally hard.

## How It's Best Learned
Identify which properties are semantic (depend on the computed function) versus syntactic (depend on the machine description), then apply Rice's theorem to candidate properties.

## Common Misconceptions
- Thinking Rice's theorem applies to syntactic properties (it does not; e.g., 'machine has ≥100 states' is decidable).
- Assuming all undecidable problems are trivial or artificial; Rice's theorem applies to all non-trivial properties of computations.
