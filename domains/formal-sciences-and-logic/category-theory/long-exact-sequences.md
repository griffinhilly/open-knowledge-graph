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
