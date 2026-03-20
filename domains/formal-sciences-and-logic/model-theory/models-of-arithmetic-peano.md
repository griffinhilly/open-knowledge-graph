---
id: models-of-arithmetic-peano
title: Models of Peano Arithmetic and Non-Standard Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: hard
- id: complete-first-order-theories
  type: soft
- id: arithmetic-functions-and-multiplicativity
  type: soft
builds-toward:
- undecidability-and-godel
- omitting-types-theorem-countable
tags:
- peano-arithmetic
- non-standard-models
- arithmetic
stage: advanced
status: draft
---

# Models of Peano Arithmetic and Non-Standard Models

## Core Idea
Peano arithmetic (PA) has non-standard models: countably infinite models satisfying all PA axioms but containing infinite integers beyond all standard numerals. Every non-standard model contains a copy of the standard natural numbers followed by a densely ordered structure of infinitely large elements. Non-standard models demonstrate that first-order logic cannot axiomatize arithmetic uniquely.

## How It's Best Learned
Construct a non-standard model using the compactness theorem by adding a constant c and axioms c > n for all numerals n. Study the structure of the infinite part.

## Explainer

From your study of formal arithmetic and first-order logic, you know that Peano Arithmetic (PA) is a first-order theory with axioms for zero, successors, addition, and multiplication, plus an induction schema. You may have hoped these axioms uniquely pin down the natural numbers ℕ. The existence of **non-standard models** is the fundamental theorem showing they do not — and cannot.

The construction of a non-standard model is a direct application of the **compactness theorem**. Extend the language of PA with a new constant symbol c, and add the sentences c > 0, c > 1, c > 2, ... for every standard numeral. Each finite subset of these axioms is satisfiable (interpret c as a sufficiently large standard number). By compactness, the entire extended theory is satisfiable, producing a model M in which c is an "infinite integer" — greater than every standard natural number, yet satisfying all PA axioms. The elements corresponding to standard natural numbers form an initial segment isomorphic to ℕ, but M contains additional **non-standard elements** beyond this segment.

The structure of the non-standard part is illuminating. Every non-standard element z satisfies z > n for all standard n, yet z − 1, z − 2, ... are also elements of M, stretching infinitely in both directions within the non-standard region. The non-standard elements form a **densely ordered collection of copies of ℤ** — each "block" is isomorphic to the integers, and the blocks themselves have no least or greatest element. This contrasts sharply with the discrete, well-ordered structure of the standard naturals. PA's induction schema does not rule this out, because first-order induction only quantifies over properties *expressible in first-order logic* — and first-order logic cannot single out the standard model from among all its non-standard cousins.

The philosophical consequence is profound: **first-order logic cannot categorically axiomatize arithmetic**. No matter what first-order sentences you add to PA (as long as they are all true in ℕ), the resulting theory will still have non-standard models. This follows from the Löwenheim-Skolem theorem and compactness: any first-order theory with an infinite model has models of every infinite cardinality, and even among countable models, non-standard ones exist. The "true arithmetic" — the set of all first-order sentences true in ℕ — is not recursively axiomatizable (by Gödel's incompleteness theorem), and non-standard models witness exactly this gap: they satisfy every provable sentence but disagree with ℕ on some unprovable truths.
