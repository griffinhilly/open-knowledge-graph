---
id: compactness-theorem-model-theory
title: Compactness Theorem in Model Theory
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: fol-compactness
  type: hard
- id: model-theory-basics
  type: hard
- id: set-theory-basics
  type: soft
- id: proof-structure-and-terminology
  type: soft
builds-toward:
- lowenheim-skolem-theorems-overview
tags:
- compactness
- satisfiability
- finite approximation
- infinite model
stage: advanced
status: draft
---

# Compactness Theorem in Model Theory

## Core Idea
The Compactness Theorem asserts that an infinite set Σ of first-order sentences has a model if and only if every finite subset has a model. This reduces satisfiability of infinite sentence sets to finite approximations, enabling construction of infinite models with prescribed properties through careful finite control.

## Explainer

From your study of first-order logic and the completeness theorem, you know that a set of sentences Σ is satisfiable if and only if it is consistent — has no finite proof of a contradiction. The Compactness Theorem is a direct corollary: a proof only invokes finitely many premises, so if every finite subset of Σ is consistent (satisfiable), then no finite proof from Σ can derive a contradiction, so Σ itself must be satisfiable. The heart of compactness is that **first-order logic is blind to infinite sets of sentences** — consistency is always witnessed by finite evidence.

The theorem's real power is in what it lets you *build*. The canonical application: suppose you want a model of the natural numbers that contains an element larger than every standard natural number. Take Σ to be the usual axioms of arithmetic, then add a new constant symbol c along with the infinite family of sentences {c > 0, c > 1, c > 2, c > 3, ...}. Any finite subset only requires c to exceed finitely many standard naturals, which is satisfiable (take c to be any sufficiently large standard number). Compactness then guarantees a model of the whole Σ — a **non-standard model of arithmetic** where c is infinitely large. No standard model satisfies this, yet the non-standard model exists and satisfies every first-order sentence true in ℕ.

This construction pattern appears repeatedly in model theory: to build a model with some "infinite" property, express it as an infinite set of first-order sentences, verify that every finite approximation is satisfiable, and invoke compactness to get the full model. The method works even when you cannot explicitly describe the model — compactness is an existence theorem, not a construction. Similarly, compactness shows that no first-order theory can *characterize* an infinite structure up to isomorphism: if a theory has any infinite model, it has models of all infinite cardinalities (by the Löwenheim-Skolem theorems, which themselves use compactness).

A complementary use of compactness is in proving **non-expressibility** results: if a property P cannot be approximated finitely (every finite approximation is satisfiable both by P-structures and non-P-structures), then no first-order sentence can express P. For example, "the domain is infinite" is not expressible by a single first-order sentence — you can express "there are at least n elements" for each finite n, but no finite sentence can force infinitely many. Compactness makes this precise: the union of finite-model sentences with "there are infinitely many elements" is satisfiable (every finite subset is), so the two properties cannot be separated by a first-order sentence. These non-expressibility results reveal the genuine limits of first-order logic compared to second-order logic or infinitary logic.
