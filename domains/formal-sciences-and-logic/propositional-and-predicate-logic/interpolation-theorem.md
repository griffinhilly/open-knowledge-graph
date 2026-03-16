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

## Explainer

You have studied FOL compactness — the theorem that a set of sentences has a model if every finite subset does — and the basics of model theory, including the connection between syntactic provability and semantic truth. **Craig's interpolation theorem** combines these to reveal something fundamental about how logical entailment works at the vocabulary level.

Start with an entailment: suppose φ ⊨ ψ (every model of φ is also a model of ψ). The vocabulary of φ might include predicate symbols P, Q, R, while ψ uses Q, R, S. The shared vocabulary is {Q, R}. Craig's theorem guarantees the existence of a sentence θ — the **interpolant** — using *only* the shared symbols Q and R, such that φ ⊨ θ and θ ⊨ ψ. The entailment from φ to ψ is mediated entirely through what they have in common; the symbols unique to each side play no essential role in the logical connection between them.

To appreciate why this is non-trivial, consider that φ might use P extensively in its internal structure. Yet when it comes to implying ψ, all the "work" that P does can be captured by a formula in the shared language. The proof typically proceeds by showing that the set of sentences in the shared vocabulary that φ implies and the set that ψ refutes are inconsistent — then using compactness or cut-elimination to extract the interpolant. The interpolant is not unique: many different sentences in the shared vocabulary can serve as the mediating step.

**Beth's definability theorem** is perhaps the most useful consequence. Suppose a predicate symbol P is **implicitly defined** by a theory T: any two models of T that agree on all non-P symbols must also agree on P's extension. Intuitively, P's meaning is "locked in" by the rest of the theory. Beth's theorem says P is then **explicitly definable** — there exists a formula in T's non-P vocabulary whose extension equals P's in every model. The proof uses Craig interpolation: implicit definability yields an entailment between two copies of T (one using P, one using a renamed copy P'), sharing only non-P vocabulary; the interpolant provides the explicit definition. Together, Craig and Beth show that first-order logic has no "hidden vocabulary" — any symbol that is semantically determined by a theory can be syntactically defined within that theory's language.
