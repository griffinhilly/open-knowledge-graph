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
stage: expert
status: draft
---

# Model Instantiation and Structure Realization

## Core Idea
A structure M (or model) in a signature σ assigns to each symbol in σ a concrete mathematical object: constants become elements, function symbols become operations, and relation symbols become sets of tuples. The universe (domain) of M is the non-empty set over which these interpretations are defined.

## How It's Best Learned
Work through explicit examples: the group (Z, +) as a model of the group signature, or (R, 0, 1, +, ·, <) as a model of the ordered field signature. Verify satisfaction of key axioms.

## Common Misconceptions
A structure is not an abstract syntax tree—it is a concrete assignment. Distinct structures can satisfy the same theory but differ in their interpretations of function/relation symbols.

## Questions

```yaml
- question: "Consider the sentence ∀x∀y(x·y = y·x) in the group signature. In which of the following structures is this sentence FALSE?"
  type: multiple-choice
  options:
    - "(ℤ, +, 0) — the integers under addition"
    - "(ℝ, ×, 1) — the nonzero real numbers under multiplication"
    - "(GL₂(ℝ), ×, I) — invertible 2×2 real matrices under matrix multiplication"
    - "(ℤ/2ℤ, +, 0) — integers mod 2 under addition"
  answer: 2
  explanation: "Matrix multiplication is not commutative: AB ≠ BA in general for 2×2 invertible matrices. So ∀x∀y(x·y = y·x) is false in (GL₂(ℝ), ×, I). The integers under addition and nonzero reals under multiplication are both commutative, so the sentence is true there. This illustrates the key point: the same sentence can have different truth values in different structures over the same signature. Truth is always relative to a specific interpretation."

- question: "Two structures M and M' both instantiate the same group signature and both satisfy all the group axioms. What can we conclude?"
  type: multiple-choice
  options:
    - "M and M' are isomorphic — they have the same structure up to renaming of elements"
    - "M and M' are identical — the same theory uniquely determines a structure"
    - "M and M' may be completely different structures with different properties, despite sharing the same theory"
    - "Any sentence true in M must also be true in M', and vice versa"
  answer: 2
  explanation: "Satisfying the same base theory (the group axioms) is a very weak constraint — it does not uniquely determine a structure. (ℤ, +, 0) and (ℝ*, ×, 1) both satisfy the group axioms but differ in cardinality, commutativity, divisibility, and many other properties. They are not isomorphic. Option D is wrong because sentences like ∀x∀y(x·y = y·x) are true in (ℤ, +, 0) but false in non-abelian groups, while both satisfy the group axioms."

- question: "In model theory, a sentence's truth value is determined by the specific structure in which it is evaluated, not by the signature alone."
  type: true-false
  answer: true
  explanation: "True. A signature is only syntactic scaffolding — a list of symbols with arities, carrying no mathematical content. A sentence like ∀x(f(x) = x) might be true in one structure (where f is the identity function) and false in another (where f is squaring). Only when you commit to a specific structure — assigning concrete mathematical objects to each symbol over a specified domain — does a sentence receive a truth value. Satisfaction is always relative to a particular interpretation."

- question: "Specifying a signature is sufficient to determine the mathematical content of a model — the structure and its signature are the same thing."
  type: true-false
  answer: false
  explanation: "False. The signature is just a list of symbols and arities — it has no mathematical content. A structure is a concrete interpretation that assigns each symbol to an actual mathematical object (an element, function, or relation) over a specified domain. Countless distinct structures can share the same signature. Every group is an instantiation of the group signature, but there are infinitely many non-isomorphic groups. The signature gives the vocabulary; the structure fills in the meaning."

- question: "What does it mean to say that model instantiation is 'the bridge between logic and mathematics'?"
  type: short-answer
  answer: "Logic operates on syntactic symbols — formulas, terms, sentences — without intrinsic meaning. Mathematics operates on concrete objects — numbers, sets, functions, groups. Model instantiation is the process of assigning mathematical objects to logical symbols, turning a syntactic signature into a mathematical structure. Through this assignment, logical sentences acquire truth values and mathematical structures become amenable to logical analysis. Without instantiation, logic and mathematics remain separate: one formal but contentless, the other concrete but pre-formal."
  explanation: "This bridge is what makes model theory powerful: it allows logical tools (compactness, Löwenheim–Skolem, definability) to be applied to mathematical structures, and allows mathematical constructions (ultraproducts, elementary extensions) to be used to study logical languages. The interplay is productive precisely because instantiation makes the connection explicit and controllable."
```

## Explainer

You have already studied signatures and satisfaction at an abstract level. **Model instantiation** is the process of making this abstract machinery concrete: given a signature σ (a list of constant, function, and relation symbols), you choose an actual mathematical object — a set, a group, a graph, the integers — and specify what each symbol in σ means within that object. The result is a **σ-structure** M, also called a **realization** of σ.

Let's trace through a specific example. The group signature σ_G contains one binary function symbol · (multiplication) and one constant symbol e (identity). To instantiate σ_G as the integers under addition, you set: the domain (universe) of M to be ℤ, the interpretation of · to be ordinary integer addition +, and the interpretation of e to be the integer 0. Now M = (ℤ, +, 0) is a σ_G-structure. Separately, M' = (ℝ*, ×, 1) — the nonzero reals under multiplication — is *also* a σ_G-structure. Both M and M' are instantiations of the same signature, and both satisfy the group axioms, but they are structurally very different: ℤ under + has no element of order 2 except... actually it does: (-1) has order 2 in (ℤ,+) since -1 + -1 = -2 ≠ 0. Point being: same signature, same theory satisfied, but the two structures have different internal properties.

The **universe** of a structure is the set over which all variables range and all functions operate — it must be non-empty by definition. This is why structures are sometimes called *interpretations*: every symbol in the signature gets interpreted as something specific in the universe. A **relation symbol** R of arity k gets interpreted as a subset R^M ⊆ M^k (the set of k-tuples satisfying R). A **function symbol** f of arity k gets interpreted as a total function f^M : M^k → M. A **constant symbol** c gets interpreted as a specific element c^M ∈ M. This three-way assignment is the complete definition of a structure.

Why does this matter? Because **satisfaction** is defined over structures, not over abstract symbols. When you ask "does the group axiom ∀x∀y (x·y = y·x) hold?", the answer depends entirely on which structure you're looking at. For (ℤ, +, 0) the answer is yes (integers commute). For (GL₂(ℝ), ×, I) — 2×2 invertible matrices — the answer is no (matrix multiplication does not commute). The same sentence, opposite truth values, in two different structures over the same signature. **Instantiation is what transforms syntactic symbols into mathematical entities that can be true or false of, and this is the bridge between logic and mathematics.**

