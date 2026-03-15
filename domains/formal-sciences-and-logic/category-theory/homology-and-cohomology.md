---
id: homology-and-cohomology
title: Homology and Cohomology
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: functors
  type: soft
- id: vector-spaces
  type: soft
builds-toward:
- derived-functors
tags:
- homology
- cohomology
- long exact sequence
- snake lemma
- connecting homomorphism
- homological algebra
stage: advanced
status: draft
---
# Homology and Cohomology

## Core Idea
The homology of a chain complex C_* in an abelian category is the sequence of objects H_n(C) = ker(d_n) / im(d_{n+1}), measuring the failure of the complex to be exact at each degree. Cohomology arises dually from cochain complexes. The central structural result is the long exact sequence in homology: a short exact sequence of chain complexes 0 → A_* → B_* → C_* → 0 induces a long exact sequence ··· → H_n(A) → H_n(B) → H_n(C) → H_{n-1}(A) → ···, connected by boundary maps constructed via the snake lemma. This machinery transforms short exact sequences of complexes into computable algebraic invariants across algebra, topology, and geometry.

## How It's Best Learned
Compute homology of a simple chain complex of abelian groups by hand: find the kernel, find the image, and take the quotient. Then take a short exact sequence of chain complexes and construct the long exact sequence, tracing the connecting homomorphism through the snake lemma diagram. The snake lemma proof, while technical, is the engine of homological algebra and rewards careful study.

## Common Misconceptions
- Homology and cohomology are not the same thing, even though they often carry equivalent information; cohomology has a natural ring structure (cup product) that homology lacks.
- The connecting homomorphism in the long exact sequence is not arbitrary; it arises canonically from the snake lemma and is natural in the short exact sequence.
- Zero homology does not mean the complex is trivial; it means the complex is exact, which is a strong and useful condition.
