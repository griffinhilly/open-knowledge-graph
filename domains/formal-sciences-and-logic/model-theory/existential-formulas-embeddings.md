---
id: existential-formulas-embeddings
title: Existential Formulas and Preservation under Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
builds-toward:
- model-completeness-theorems
- definable-algebraic-closure
tags:
- existential-formulas
- preservation
- embeddings
stage: advanced
status: draft
---

# Existential Formulas and Preservation under Embeddings

## Core Idea
An existential formula (of the form ∃x φ where φ is quantifier-free) is preserved under embeddings: if an existential formula holds in a structure, it holds in any embedding of that structure. This dual preservation property characterizes which formulas propagate forward through embeddings.

## Explainer

You already know how to interpret a first-order formula in a structure — you assign elements to variables and check whether the formula is satisfied. An **embedding** is a structure map that injects one structure into another while preserving all the basic relational facts: if a relation holds between elements in the small structure, it holds between their images in the large structure. Think of embedding the integers into the rationals, or a subgraph into a larger graph. The question preservation theory asks is: which formulas, once satisfied in a small structure, must stay satisfied in any larger structure containing it?

**Existential formulas** are exactly the formulas of the form ∃x₁ ∃x₂ … ∃xₙ φ(x₁,…,xₙ) where φ contains no quantifiers. The key insight is that existential formulas only require *witness elements to exist* — they never assert that something fails to exist or that all elements have some property. If the witnesses are present in the small structure, they are present in any structure that embeds the small one (since embeddings are injective and preserve relations). So satisfying an existential formula is "upward stable" along embeddings.

A concrete example: "there exist two elements a, b such that a ≠ b and E(a,b)" is an existential formula asserting that the graph has at least one edge. If a graph G satisfies this, any graph H into which G embeds also satisfies it — because the same two vertices a, b with edge E(a,b) appear in H. Contrast this with a universal formula "for all a, b, if E(a,b) then E(b,a)" (symmetry of the edge relation). This can fail after embedding: you might add asymmetric edges in the larger structure. Universal formulas are preserved under *substructures* (going downward), not embeddings.

The **Łoś-Tarski theorem** makes this connection precise: a first-order formula (or set of formulas) is preserved under embeddings if and only if it is logically equivalent to an existential formula. This is a characterization theorem — it says the syntactic property of being existential and the semantic property of being preserved under embeddings are the same thing. This is a model-theoretic analog of a compactness argument: you cannot express a property that vanishes after embedding unless it has universal quantifiers.

The practical importance is in algebra and combinatorics. When you study classes of structures defined by existential conditions — graphs containing a triangle, groups with a non-identity element of finite order, fields with a root of a polynomial — you know these properties are inherited by larger structures. Conversely, if a property can be lost after extending a structure (e.g., torsion-freeness, which can fail after taking quotients), it cannot be captured by existential sentences alone. Preservation theorems are one of the core tools for matching syntactic form to semantic behavior in model theory.
