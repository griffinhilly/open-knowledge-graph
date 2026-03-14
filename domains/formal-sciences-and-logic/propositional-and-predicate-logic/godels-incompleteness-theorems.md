---
id: godels-incompleteness-theorems
title: Gödel's Incompleteness Theorems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-soundness-completeness
  type: hard
- id: formal-arithmetic-and-expressibility
  type: hard
- id: decidability-and-undecidability
  type: soft
- id: lowenheim-skolem-theorem
  type: soft
- id: mathematical-induction
  type: soft
- id: cantor-diagonalization
  type: soft
builds-toward:
- intuitionistic-logic-intro
tags:
- incompleteness
- Godel
- consistency
- self-reference
- Peano-arithmetic
stage: formal-systems
status: validated
---

# Gödel's Incompleteness Theorems

## Core Idea
Gödel's First Incompleteness Theorem (1931) states that any consistent formal system T extending Peano Arithmetic is incomplete: there exists a sentence G that is true (in the standard model) but neither provable nor disprovable in T. The proof uses Gödel numbering to encode the statement 'this sentence is not provable in T' as an arithmetic formula. The Second Incompleteness Theorem states that such a system T cannot prove its own consistency — Con(T) is unprovable in T. These results shattered Hilbert's program of finding a complete, consistent, decidable foundation for all mathematics.

## How It's Best Learned
Understand the diagonal lemma (fixed-point lemma) first: every formula φ(x) has a sentence G such that T proves G ↔ φ(⌜G⌝). Then apply it with φ(x) = 'x is not provable in T'. Separate the philosophical implications from the precise mathematical statement.

## Common Misconceptions
- The incompleteness theorems do not say mathematics is broken or that truth is subjective — they are precise results about formal systems.
- The Gödel sentence G is artificial and contrived; most mathematically natural questions are decidable within standard theories.
- The theorems apply to sufficiently strong theories; very weak theories (like Presburger arithmetic) can be complete and decidable.
