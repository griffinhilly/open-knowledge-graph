---
id: interpolation-theorem
title: Craig Interpolation Theorem
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-compactness
  type: hard
- id: model-theory-basics
  type: hard
builds-toward:
- lowenheim-skolem-theorem
tags:
- Craig-interpolation
- Beth-definability
- implicit-definition
- explicit-definition
- interpolant
stage: formal-systems
status: draft
---

# Craig Interpolation Theorem

## Core Idea
Craig's interpolation theorem states that if φ ⊨ ψ (φ logically implies ψ), then there exists a sentence θ — the interpolant — whose non-logical vocabulary (predicate, function, and constant symbols) is contained in both φ and ψ, such that φ ⊨ θ and θ ⊨ ψ. The interpolant captures exactly the "common content" that mediates the entailment. Beth's definability theorem follows as a corollary: if a predicate is implicitly defined by a theory (its extension is uniquely determined), then it is explicitly definable by a formula in the theory's language. Together, these results reveal deep structural properties of first-order logic connecting semantics, syntax, and definability.

## How It's Best Learned
Take a concrete entailment (e.g., ∀x(P(x) → Q(x)) ⊨ ∀x(P(x) → Q(x) ∨ R(x))) and find the interpolant by hand — it must use only the shared vocabulary. Then study how Beth's theorem uses interpolation to convert implicit definitions into explicit ones.

## Common Misconceptions
- The interpolant is not unique — many different sentences can serve as the interpolant for a given entailment.
- Craig interpolation holds for standard first-order logic but fails for some extensions (e.g., certain fragments of second-order logic or logics with generalized quantifiers).
- Beth definability is not trivial — the fact that implicit definability implies explicit definability is a substantive result, not a tautology.
