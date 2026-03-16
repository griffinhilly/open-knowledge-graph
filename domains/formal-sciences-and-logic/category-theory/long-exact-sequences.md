---
id: long-exact-sequences
title: Long Exact Sequences and the Connecting Morphism
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: the-snake-lemma
  type: hard
- id: derived-functors
  type: soft
builds-toward:
- homology-and-cohomology
- spectral-sequences-introduction
tags:
- exactness
- connecting-morphism
- homological-algebra
stage: abstract-reasoning
status: draft
---

# Long Exact Sequences and the Connecting Morphism

## Core Idea
When a short exact sequence of objects is processed through a left or right exact functor (such as Hom or Tor), the result is often a long exact sequence that includes connecting morphisms relating different homological degrees. Long exact sequences are central to extracting computational information from homological algebra and are generated systematically via the snake lemma.

## How It's Best Learned
Study the fundamental long exact sequence in homology associated to a short exact sequence of complexes. Compute specific examples in Ext and Tor. Practice deriving segments of long exact sequences and understanding how connecting morphisms arise.

## Common Misconceptions
Not every application of a functor to a short exact sequence yields a long exact sequence; only specific functors (left/right exact or derived functors) do. The positions of connecting morphisms require careful attention to homological degree.

## Explainer

A short exact sequence 0 → A → B → C → 0 packages three objects and the maps between them into a compact statement: A embeds into B (the first map is injective), and C is the "quotient" of B by the image of A (the second map is surjective with kernel equal to the image of the first). This is familiar from linear algebra (subspaces and quotients), group theory (normal subgroups and quotient groups), and module theory. When you apply a functor F to such a sequence, you might hope to get another short exact sequence 0 → FA → FB → FC → 0. That hope is rarely fulfilled — it fails exactly when F is not exact — and the **long exact sequence** is the systematic account of that failure.

If F is a **left-exact functor** (like Hom(−, M) or Hom(M, −) for modules), it preserves the left end of exactness but may fail on the right. Applying it to 0 → A → B → C → 0 gives exactness at FA and FB but not necessarily at FC: 0 → FA → FB → FC may not end with a surjection. The right-derived functors R^n F (which you know from your prerequisite on derived functors) measure the failure degree by degree. The result is a long exact sequence extending rightward: 0 → FA → FB → FC → R¹FA → R¹FB → R¹FC → R²FA → ···. For Hom(−, M), the derived functors are Ext^n(−, M); for the tensor product ⊗ M (which is right-exact), the derived functors are Tor_n(−, M) and the long exact sequence extends leftward.

The **connecting morphism** δ: R^n FC → R^(n+1) FA is the critical new ingredient that makes the sequence long. It is not produced by functoriality of F applied to the original sequence — it is produced by the **snake lemma** applied diagram-by-diagram to the short exact sequence of injective or projective resolutions used to compute the derived functors. Your prerequisite on the snake lemma is literally the engine here: the connecting homomorphism in the snake lemma, applied at each homological degree, yields the connecting morphisms in the long exact sequence. This is why the snake lemma is foundational: it is not just a diagram-chasing trick but the generator of all connecting morphisms.

The long exact sequence is enormously powerful in computation because it relates three objects' derived invariants. Knowing two terms often determines the third by exactness. For example, if Ext^n(B, M) = 0 for all n ≥ 1 (B is projective), then the long exact sequence breaks into split short exact sequences: Ext^n(C, M) ≅ Ext^(n+1)(A, M) for all n ≥ 1, giving a **dimension shift** formula that lets you bootstrap computations to higher degrees. This kind of argument — exploiting long exact sequences to shift, compare, and compute homological invariants — is the basic technique of homological algebra and appears throughout algebraic topology, algebraic geometry, and representation theory.
