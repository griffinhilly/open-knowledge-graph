---
id: craig-lyndon-interpolation
title: Craig-Lyndon Interpolation Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
- id: interpolation-theorem
  type: soft
builds-toward:
- beth-definability-implicit-explicit
tags:
- Craig
- interpolation
- interpolant
- consequence
stage: formal-systems
status: draft
---

# Craig-Lyndon Interpolation Theorem

## Core Idea
If φ → ψ is a tautology, there exists an interpolant θ (using only symbols common to φ and ψ) such that φ → θ and θ → ψ are both tautologies. The Lyndon version strengthens this: the interpolant can be chosen to preserve the direction of implications in formulas. Interpolation theorems are fundamental for studying definability and relationships between formulas.

## Explainer

You already understand Craig interpolation from your prerequisite: when φ logically entails ψ, there is an interpolant θ using only the vocabulary shared by both, with φ ⊨ θ and θ ⊨ ψ. The **Craig-Lyndon theorem** refines this result by imposing an additional constraint on the interpolant — one that encodes not just *which* predicate symbols appear, but *how* they appear directionally.

The Lyndon strengthening concerns **polarity**. In a formula, a predicate symbol can appear **positively** (in a context where increasing its extension can only help the formula hold — for instance, not under any negation), **negatively** (where decreasing its extension helps), or both. The Lyndon refinement says the interpolant θ can be chosen so that any predicate occurring positively in θ occurs positively in both φ and ψ, and any predicate occurring negatively in θ occurs negatively in both. This is a strictly stronger claim than bare Craig interpolation: the vocabulary constraint remains, but now the *directional role* of each shared symbol is also preserved.

Why does this refinement matter? In formal verification, modal logic, and definability theory, polarity carries semantic weight: a predicate appearing only positively is monotone in that position. The Lyndon version guarantees that the interpolant's logical structure mirrors the polarity structure of the original entailment, which enables stronger applications. For example, the Lyndon version implies sharper definability results than Craig's version alone — when constructing an explicit definition from an implicit one, the definition can be chosen with controlled monotonicity properties.

Both versions connect to **Beth definability**: if a theory implicitly defines a predicate (its extension is uniquely determined by the rest of the theory in any model), then that predicate is explicitly definable using the theory's existing vocabulary. The Craig-Lyndon version strengthens this: the explicit definition can be chosen with controlled polarity. Together, these results reveal that the vocabulary-mediated structure of logical entailment is not arbitrary — there is always a principled "common content" mediating any entailment, and its internal directional structure can be isolated and expressed precisely.
