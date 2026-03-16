---
id: model-instantiation-structures
title: Model Instantiation and Structure Realization
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: signature-and-vocabulary-model-theory
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
- id: set-fundamentals
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- embedding-and-preservation-properties
- complete-theory-of-structures
tags:
- instantiation
- realization
- semantic-interpretation
- universe
stage: abstract-reasoning
status: draft
---

# Model Instantiation and Structure Realization

## Core Idea
A structure M (or model) in a signature σ assigns to each symbol in σ a concrete mathematical object: constants become elements, function symbols become operations, and relation symbols become sets of tuples. The universe (domain) of M is the non-empty set over which these interpretations are defined.

## How It's Best Learned
Work through explicit examples: the group (Z, +) as a model of the group signature, or (R, 0, 1, +, ·, <) as a model of the ordered field signature. Verify satisfaction of key axioms.

## Common Misconceptions
A structure is not an abstract syntax tree—it is a concrete assignment. Distinct structures can satisfy the same theory but differ in their interpretations of function/relation symbols.

## Explainer

You have already studied signatures and satisfaction at an abstract level. **Model instantiation** is the process of making this abstract machinery concrete: given a signature σ (a list of constant, function, and relation symbols), you choose an actual mathematical object — a set, a group, a graph, the integers — and specify what each symbol in σ means within that object. The result is a **σ-structure** M, also called a **realization** of σ.

Let's trace through a specific example. The group signature σ_G contains one binary function symbol · (multiplication) and one constant symbol e (identity). To instantiate σ_G as the integers under addition, you set: the domain (universe) of M to be ℤ, the interpretation of · to be ordinary integer addition +, and the interpretation of e to be the integer 0. Now M = (ℤ, +, 0) is a σ_G-structure. Separately, M' = (ℝ*, ×, 1) — the nonzero reals under multiplication — is *also* a σ_G-structure. Both M and M' are instantiations of the same signature, and both satisfy the group axioms, but they are structurally very different: ℤ under + has no element of order 2 except... actually it does: (-1) has order 2 in (ℤ,+) since -1 + -1 = -2 ≠ 0. Point being: same signature, same theory satisfied, but the two structures have different internal properties.

The **universe** of a structure is the set over which all variables range and all functions operate — it must be non-empty by definition. This is why structures are sometimes called *interpretations*: every symbol in the signature gets interpreted as something specific in the universe. A **relation symbol** R of arity k gets interpreted as a subset R^M ⊆ M^k (the set of k-tuples satisfying R). A **function symbol** f of arity k gets interpreted as a total function f^M : M^k → M. A **constant symbol** c gets interpreted as a specific element c^M ∈ M. This three-way assignment is the complete definition of a structure.

Why does this matter? Because **satisfaction** is defined over structures, not over abstract symbols. When you ask "does the group axiom ∀x∀y (x·y = y·x) hold?", the answer depends entirely on which structure you're looking at. For (ℤ, +, 0) the answer is yes (integers commute). For (GL₂(ℝ), ×, I) — 2×2 invertible matrices — the answer is no (matrix multiplication does not commute). The same sentence, opposite truth values, in two different structures over the same signature. **Instantiation is what transforms syntactic symbols into mathematical entities that can be true or false of, and this is the bridge between logic and mathematics.**

