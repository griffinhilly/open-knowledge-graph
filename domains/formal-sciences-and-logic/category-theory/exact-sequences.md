---
id: exact-sequences
title: Exact Sequences in Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
- id: vector-spaces
  type: soft
- id: linear-transformations-definition
  type: soft
builds-toward:
- snake-lemma
- abelian-structure-properties
- homology-and-cohomology
tags:
- sequences
- homological-algebra
- kernels-cokernels
stage: advanced
status: draft
---

# Exact Sequences in Categories

## Core Idea
An exact sequence is a sequence of morphisms f: A → B → C where the image of one equals the kernel of the next. Exactness encodes compatibility conditions between maps. Short exact sequences (0 → A → B → C → 0) characterize extensions and are central to homological algebra, capturing how one object fits inside another with a given quotient.

## Explainer

From your work on additive categories and linear transformations, you know that a morphism f: A → B in an abelian category has both a kernel (elements sent to 0) and an image (elements reached by f). Exactness is a condition on how consecutive morphisms in a sequence interact: in A →^f B →^g C, the sequence is **exact at B** if im(f) = ker(g). In words, everything that f sends into B is precisely the collection of things that g kills — no more, no less. Exactness is not about a single map, but about the compatibility of two consecutive maps.

A concrete linear algebra example grounds the abstraction. Let V be a vector space and T: V → W a linear transformation. The sequence 0 → ker(T) →^i V →^T im(T) → 0 is always exact, where i is the inclusion. Exactness at ker(T): the map from 0 is the zero map, and its image {0} equals the kernel of i (which is {0} since inclusions are injective). Exactness at V: the image of i is ker(T), and the kernel of T is — by definition — ker(T). Exactness at im(T): T is surjective onto im(T), so its image is all of im(T), and the kernel of the map to 0 is also all of im(T). This exact sequence encodes the rank-nullity theorem: it says that V is built from ker(T) and im(T) in a precise way.

The most important structure is the **short exact sequence** 0 → A →^f B →^g C → 0. Exactness at A says f is injective (kernel of f equals image of 0 → A, which is {0}). Exactness at C says g is surjective (image of g equals kernel of the map to 0, which is all of C). Exactness at B says im(f) = ker(g). This means A embeds into B as a subobject, and C is the quotient B/A. The short exact sequence is precisely the data of an **extension**: B is "between" A and C in the sense that A sits inside B and C is what's left over. Different short exact sequences with the same A and C correspond to different ways B can extend A by C — this is the subject of **Ext groups** in homological algebra.

The power of exact sequences is that they let you transfer information between objects. If you know two of the three objects and some maps in a short exact sequence, you can often deduce properties of the third. **Long exact sequences** — which arise naturally from derived functors — chain these short exact sequences together and allow you to compute cohomology groups by relating them across a sequence. The snake lemma (which this topic builds toward) is the key engine: it produces long exact sequences from diagrams of short exact sequences. Once you can manipulate exact sequences fluently, you have the core computational tool of homological algebra, algebraic topology, and much of modern algebra.
