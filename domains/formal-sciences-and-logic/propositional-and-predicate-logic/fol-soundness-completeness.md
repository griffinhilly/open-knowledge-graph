---
id: fol-soundness-completeness
title: Soundness and Completeness of First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: first-order-semantics
  type: hard
- id: natural-deduction-fol
  type: hard
builds-toward:
- fol-compactness
- lowenheim-skolem-theorem
- godels-incompleteness-theorems
tags:
- completeness-theorem
- Godel-completeness
- soundness
- FOL
- metatheorem
stage: formal-systems
status: validated
---

# Soundness and Completeness of First-Order Logic

## Core Idea
Gödel's Completeness Theorem (1930) establishes that the standard proof system for first-order logic is both sound (⊢ φ implies ⊨ φ) and complete (⊨ φ implies ⊢ φ). Equivalently, a set of sentences is consistent (has no contradiction) if and only if it has a model. The completeness proof uses the Henkin construction: extend a consistent theory by adding witnesses for every existential claim, then take the quotient structure whose elements are equivalence classes of terms. This theorem is distinct from — and historically precedes — Gödel's Incompleteness Theorems.

## How It's Best Learned
Study soundness first (by induction on derivations) before tackling completeness. Trace the Henkin construction on a small example to see how a model is assembled from syntactic material. Contrast with incompleteness.

## Common Misconceptions
- Gödel's Completeness Theorem and Incompleteness Theorems are different results — completeness says the proof system captures all valid FOL inferences; incompleteness says no consistent recursive theory proves all arithmetical truths.
- Completeness does not mean every true sentence about natural numbers is provable — it means every logically valid sentence (true in all structures) is provable.
