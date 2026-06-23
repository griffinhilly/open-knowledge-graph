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
- id: isomorphism-and-structural-equivalence
  type: soft
- id: structure-homomorphisms-embeddings
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
status: validated
---

# Elementary Equivalence and Logical Indistinguishability

## Core Idea
Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences. This is weaker than isomorphism—structures can be elementarily equivalent with different domains—but captures the idea that first-order logic cannot distinguish them. Elementary equivalence is the central notion linking models to the sentences they satisfy.

## Questions

```yaml
- question: "The ordered fields (ℝ, +, ·, <, 0, 1) and (ℚ, +, ·, <, 0, 1) are not isomorphic. What does this tell us about whether they are elementarily equivalent?"
  type: multiple-choice
  options:
    - "They cannot be elementarily equivalent — non-isomorphic structures are always first-order distinguishable"
    - "They are still elementarily equivalent, because elementary equivalence is weaker than isomorphism"
    - "They are not elementarily equivalent, because the sentence '∃x (x · x = 2)' distinguishes them"
    - "Elementary equivalence does not apply to ordered fields, only to purely relational structures"
  answer: 2
  explanation: "This is a case where non-isomorphic structures are also NOT elementarily equivalent — the sentence '∃x (x · x = 2)' (√2 exists) is true in ℝ but false in ℚ. This distinguishes them in first-order logic. The key point is that non-isomorphic structures *might* or *might not* be elementarily equivalent — you cannot conclude either way from non-isomorphism alone. Option A would be correct only if first-order logic were expressive enough to detect all structural differences, which it is not."

- question: "The structures (ℚ, <) and (ℝ, <), viewed purely as dense linear orders without endpoints, are elementarily equivalent. What is the best explanation for this?"
  type: multiple-choice
  options:
    - "They are isomorphic — any two countably dense linear orders without endpoints are the same"
    - "Both are models of the complete theory DLO, so every first-order sentence in {<} that holds in one holds in the other"
    - "First-order logic cannot express any properties about dense linear orders, so all such structures look alike"
    - "Elementary equivalence only requires that the structures have the same cardinality"
  answer: 1
  explanation: "Both (ℚ, <) and (ℝ, <) are models of DLO (dense linear order without endpoints), which is a complete theory — meaning every first-order sentence in the language {<} is either a theorem or its negation is. Since both structures satisfy all axioms of DLO, and DLO is complete, they satisfy exactly the same first-order sentences: they are elementarily equivalent. Note they are NOT isomorphic (ℚ is countable, ℝ is uncountable) — this is a concrete example of elementary equivalence without isomorphism."

- question: "If two structures are isomorphic, they must be elementarily equivalent."
  type: true-false
  answer: true
  explanation: "Isomorphism is strictly stronger than elementary equivalence. An isomorphism φ: M → N is a bijection preserving all operations and relations; any first-order sentence true in M is true in N under the same interpretation (via the bijection). So isomorphic structures satisfy exactly the same first-order sentences — they are elementarily equivalent. The converse fails: elementary equivalence does not imply isomorphism."

- question: "Two structures that are elementarily equivalent should be isomorphic."
  type: true-false
  answer: false
  explanation: "This is the central misconception about elementary equivalence. Elementary equivalence is strictly weaker than isomorphism. The clearest example: the standard model of arithmetic (ℕ, +, ·, 0, 1) has nonstandard models that are elementarily equivalent to it (they satisfy the same first-order sentences) but are not isomorphic to ℕ — they contain 'infinitely large' elements invisible to any individual first-order sentence. Another example: (ℚ, <) and (ℝ, <) are elementarily equivalent but not isomorphic."

- question: "What does it mean for first-order logic to have 'limited expressive power,' and how does the existence of nonstandard models of arithmetic illustrate this?"
  type: short-answer
  answer: "First-order logic cannot express certain structural properties that distinguish structures from the outside. For arithmetic, no finite or infinite list of first-order sentences can force a model to be exactly ℕ — any consistent set of first-order sentences satisfied by ℕ also has models with 'extra' nonstandard elements that behave like infinitely large natural numbers. These nonstandard models satisfy all the same first-order sentences as ℕ because first-order quantifiers range only over elements of the structure, not over all formulas or all subsets — so the 'extra' elements can never be singled out by any individual sentence."
  explanation: "This connects to Gödel's incompleteness theorems and the compactness theorem. The inability to pin down ℕ up to isomorphism using first-order sentences is not a failure of any particular axiom system — it is a fundamental limit of first-order logic itself. Model theory studies what first-order logic can and cannot express, and elementary equivalence is the central tool for measuring exactly where this expressive boundary falls."
```

## Explainer

You already know what it means for a structure to satisfy a formula — a model M satisfies φ (written M ⊨ φ) when the interpretation makes the formula true. **Elementary equivalence** scales this up from single formulas to entire theories: two structures M and N are **elementarily equivalent** (written M ≡ N) when they satisfy exactly the same set of first-order sentences. No formula in the language can tell them apart. They are, from the perspective of first-order logic, indistinguishable.

This is strictly weaker than **isomorphism**. Isomorphic structures are always elementarily equivalent — any sentence true in one is true in both, because an isomorphism is a perfect renaming. But the converse fails. Consider the ordered fields (ℝ, +, ·, <, 0, 1) and (ℚ, +, ·, <, 0, 1). These are not isomorphic — ℝ is uncountable and ℚ is countable, and no bijection preserving all operations exists. Yet they are also not elementarily equivalent: the sentence "∃x (x · x = 2)" is true in ℝ but false in ℚ. In contrast, the structures (ℚ, <) and (ℝ, <), viewed purely as dense linear orders without endpoints, *are* elementarily equivalent: every first-order sentence in the language {<} that holds in one holds in the other, because both are models of the complete theory DLO (dense linear order without endpoints).

The deeper point is that first-order logic has limited expressive power — it cannot always detect structural differences that we can see from the outside. Two structures can look different to a set-theorist but look identical to a first-order logician. For example, the standard model of arithmetic (ℕ, +, ·, 0, 1) has **nonstandard models** — structures that satisfy exactly the same first-order sentences as ℕ but contain elements that behave like "infinitely large" natural numbers. These nonstandard models are elementarily equivalent to ℕ but not isomorphic to it; the "extra" elements are invisible to any individual first-order sentence because first-order logic cannot quantify over all formulas simultaneously (this is essentially what Gödel's incompleteness theorems exploit).

Elementary equivalence is the central equivalence relation of model theory. It partitions the class of all structures into **equivalence classes** of first-order indistinguishability. A **complete theory** is one in which every sentence is either a theorem or its negation is — equivalently, all its models are elementarily equivalent. When you study a theory like DLO or the theory of algebraically closed fields of characteristic zero, you are studying a complete theory precisely because any two models of it are elementarily equivalent. This is what makes such theories mathematically clean: the logic fully determines the first-order content of the structure, even if it cannot determine the cardinality.
