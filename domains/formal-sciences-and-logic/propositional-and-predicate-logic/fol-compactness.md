---
id: fol-compactness
title: Compactness Theorem for First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-soundness-completeness
  type: hard
- id: propositional-compactness
  type: soft
builds-toward:
- lowenheim-skolem-theorem
- model-theory-basics
tags:
- compactness
- FOL
- ultraproducts
- non-standard-models
stage: formal-systems
status: draft
---

# Compactness Theorem for First-Order Logic

## Core Idea
The compactness theorem for first-order logic states that an infinite set of sentences has a model if and only if every finite subset has a model. This follows from completeness (proofs are finite, so any derivation of a contradiction uses only finitely many axioms). Compactness implies that first-order logic cannot characterize the natural numbers up to isomorphism: any first-order theory with an infinite model has models of every infinite cardinality (a consequence of Löwenheim-Skolem), and non-standard models of arithmetic exist. Compactness is a fundamental limitation of first-order expressivity.

## How It's Best Learned
Construct a non-standard model of arithmetic explicitly using compactness: add a new constant c and axioms c > n for each natural number n, then apply compactness to get a model containing an 'infinite' element.

## Common Misconceptions
- Compactness does not mean all relevant information is captured finitely — it means satisfiability is finitely determined.
- Non-standard models arising from compactness are fully legitimate models; they just satisfy extra sentences the intended model does not.
