---
id: diagram-expansion-by-constants
title: Diagram and Expansion by Constants
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: signature-and-vocabulary-model-theory
  type: hard
builds-toward:
- existential-closure-homomorphism
- extension-lemma-embeddings
tags:
- diagram
- expansion
- constants
- language-extension
stage: abstract-reasoning
status: draft
---

# Diagram and Expansion by Constants

## Core Idea
The diagram of a structure M is formed by expanding the signature with a constant symbol for each element of M, then taking all atomic sentences true in M. The expanded theory allows explicit reference to elements and is crucial for proving extension lemmas and building homomorphism extensions.

## How It's Best Learned
Write out the diagram of a small structure like Z_3 (integers mod 3) with constants for each element, then extend embeddings using the diagram.

## Explainer

You've studied structures and signatures — a signature σ specifies function, relation, and constant symbols, and a structure M interprets them over a domain. The diagram technique gives you a precise way to "name" every element of a structure in the language, turning facts about M into sentences of a theory that other structures must satisfy.

The construction: start with a structure M with domain A. Expand the signature σ by adding a fresh **constant symbol** c_a for each element a ∈ A, producing the expanded signature σ_A. Interpret each c_a as the element a itself in the expanded structure M_A = (M, a)_{a∈A}. The **diagram** of M, written Diag(M), is the set of all **atomic sentences** and **negations of atomic sentences** in the language σ_A that are true in M_A. For a small structure like ℤ₃ with elements {0, 1, 2} and signature {+, 0}, the diagram includes sentences like c₀ + c₁ = c₁, c₁ + c₁ = c₂, c₁ + c₂ = c₀, ¬(c₀ = c₁), and so on — every true atomic fact about the elements, each named explicitly.

The key theorem is the **diagram lemma**: a σ-structure N (expanded to interpret the constants c_a) is a model of Diag(M) if and only if there exists an **embedding** (an injective homomorphism) from M into N. In other words, satisfying Diag(M) forces N to contain an isomorphic copy of M. This is the bridge between syntactic manipulation of theories and the semantic question of which structures embed into which. Whenever you want to extend M to a larger structure or find a model containing M, you work with Diag(M) — any model of Diag(M) works.

The **elementary diagram** ElDiag(M) extends this further: it includes all first-order sentences (not just atomic ones) true in M_A. A structure N is an **elementary extension** of M — meaning it satisfies exactly the same first-order sentences — if and only if N models ElDiag(M). This is the syntactic characterization of elementary extensions, and it is how the upward Löwenheim-Skolem theorem is typically proved: you add Diag(M) plus witnesses for new elements, apply compactness, and the resulting model is an elementary extension of M. The diagram construction is the workhorse for building larger models that preserve exactly the properties you care about.
