---
id: the-snake-lemma
title: The Snake Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
- id: commutative-diagrams-and-composition
  type: hard
builds-toward:
  - the-five-lemma
tags:
- homological-algebra
- diagram-chasing
- connecting-morphism
stage: advanced
status: draft
---
# The Snake Lemma

## Core Idea
The snake lemma is a fundamental result in homological algebra stating that given a commutative diagram of short exact sequences in an abelian category, there exists a natural connecting morphism (the 'snake') from the kernel of one morphism to the cokernel of another, and the resulting six-term sequence is exact. It is a premier tool for deriving long exact sequences from short ones.

## How It's Best Learned
Draw the full commutative diagram and carefully trace through the construction of the connecting morphism using diagram chasing. Apply it to derive long exact sequences in homology and cohomology. Work through its proof in a concrete category first (abelian groups or modules).

## Common Misconceptions
The connecting morphism is not arbitrary; its construction involves careful diagram chasing and depends on exactness. Students sometimes apply the snake lemma without verifying that the input diagram genuinely consists of short exact sequences.

## Explainer

From your study of exact sequences, you know that a sequence A → B → C is exact at B when im(A → B) = ker(B → C): every element arriving from A is exactly the set of elements that map to zero in C. A short exact sequence 0 → A → B → C → 0 is exact at every term, which means A injects into B and B surjects onto C with kernel exactly the image of A. From abelian categories, you have the machinery of kernels, cokernels, and the fact that every morphism factors as an epimorphism followed by a monomorphism. The snake lemma takes these tools and uses them to build a surprising bridge across two short exact sequences.

The setup is a commutative diagram with exact rows: one short exact sequence 0 → A → B → C → 0 across the top, another 0 → A' → B' → C' → 0 across the bottom, and vertical morphisms α: A → A', β: B → B', γ: C → C' connecting them. The snake lemma asserts that there is a natural exact sequence of six terms: **ker α → ker β → ker γ →^δ coker α → coker β → coker γ**, where the first two and last two arrows are induced by the original row maps, and **δ** is the connecting morphism that crosses from one row to the other.

The construction of δ is the heart of the lemma and an introduction to **diagram chasing**. To define δ(x) for x ∈ ker γ: since γ(x) = 0, start from some preimage b ∈ B of x under the top row's surjection (this uses exactness). Apply β to get β(b) ∈ B'. Since the square commutes and x maps to 0, β(b) is in the kernel of B' → C', which by exactness of the bottom row means β(b) is the image of some a' ∈ A'. Set δ(x) = [a'] ∈ coker α. The construction requires checking: (1) a' exists because of exactness, (2) the cokernel class [a'] is independent of the choice of preimage b because any two choices differ by an element in ker(B → C) = im(A → B), which maps to im(A' → B') under commutativity, (3) the resulting map δ is a morphism.

The snake lemma is the engine behind **long exact sequences in homology**. Given a short exact sequence of chain complexes 0 → A_• → B_• → C_• → 0, applying the snake lemma level by level produces connecting morphisms δ_n: H_n(C) → H_{n-1}(A) and assembles the fragments into a long exact sequence ⋯ → H_n(A) → H_n(B) → H_n(C) →^δ H_{n-1}(A) → ⋯. This is why the snake lemma appears at the very beginning of any serious treatment of algebraic topology or homological algebra: it is the machine that converts short exact sequences of spaces or modules into long exact sequences of their invariants.
