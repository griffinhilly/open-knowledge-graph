---
id: elementary-equivalence-indistinguishability
title: Elementary Equivalence and Logical Indistinguishability
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- complete-first-order-theories
- ehrenfeucht-fraisse-games-equivalence
- categorical-theories-and-uniqueness
tags:
- elementary equivalence
- indistinguishability
- sentences
- logical power
stage: advanced
status: draft
---

# Elementary Equivalence and Logical Indistinguishability

## Core Idea
Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences. This is weaker than isomorphism—structures can be elementarily equivalent with different domains—but captures the idea that first-order logic cannot distinguish them. Elementary equivalence is the central notion linking models to the sentences they satisfy.

## Explainer

You already know what it means for a structure to satisfy a formula — a model M satisfies φ (written M ⊨ φ) when the interpretation makes the formula true. **Elementary equivalence** scales this up from single formulas to entire theories: two structures M and N are **elementarily equivalent** (written M ≡ N) when they satisfy exactly the same set of first-order sentences. No formula in the language can tell them apart. They are, from the perspective of first-order logic, indistinguishable.

This is strictly weaker than **isomorphism**. Isomorphic structures are always elementarily equivalent — any sentence true in one is true in both, because an isomorphism is a perfect renaming. But the converse fails. Consider the ordered fields (ℝ, +, ·, <, 0, 1) and (ℚ, +, ·, <, 0, 1). These are not isomorphic — ℝ is uncountable and ℚ is countable, and no bijection preserving all operations exists. Yet they are also not elementarily equivalent: the sentence "∃x (x · x = 2)" is true in ℝ but false in ℚ. In contrast, the structures (ℚ, <) and (ℝ, <), viewed purely as dense linear orders without endpoints, *are* elementarily equivalent: every first-order sentence in the language {<} that holds in one holds in the other, because both are models of the complete theory DLO (dense linear order without endpoints).

The deeper point is that first-order logic has limited expressive power — it cannot always detect structural differences that we can see from the outside. Two structures can look different to a set-theorist but look identical to a first-order logician. For example, the standard model of arithmetic (ℕ, +, ·, 0, 1) has **nonstandard models** — structures that satisfy exactly the same first-order sentences as ℕ but contain elements that behave like "infinitely large" natural numbers. These nonstandard models are elementarily equivalent to ℕ but not isomorphic to it; the "extra" elements are invisible to any individual first-order sentence because first-order logic cannot quantify over all formulas simultaneously (this is essentially what Gödel's incompleteness theorems exploit).

Elementary equivalence is the central equivalence relation of model theory. It partitions the class of all structures into **equivalence classes** of first-order indistinguishability. A **complete theory** is one in which every sentence is either a theorem or its negation is — equivalently, all its models are elementarily equivalent. When you study a theory like DLO or the theory of algebraically closed fields of characteristic zero, you are studying a complete theory precisely because any two models of it are elementarily equivalent. This is what makes such theories mathematically clean: the logic fully determines the first-order content of the structure, even if it cannot determine the cardinality.
