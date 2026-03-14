---
id: yoneda-embedding-full-faithful
title: Yoneda Embedding and Full Faithfulness
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: representable-functors
  type: hard
builds-toward:
- presheaves
- topos-theory-intro
tags:
- yoneda
- embedding
- representable
- presheaf
stage: advanced
status: draft
---

# Yoneda Embedding and Full Faithfulness

## Core Idea
The Yoneda embedding is the functor Y: C → [C^op, Set] sending each object X to Hom(−, X), embedding any small category into its presheaf category. This embedding is always fully faithful, meaning it is injective on morphisms and surjective when restricted to hom-sets. The Yoneda embedding allows any category to be realized as a full subcategory of set-valued functors, making presheaves the universal model for categorical structures.

## How It's Best Learned
Work through the proof that Yoneda embedding is fully faithful using the Yoneda lemma directly. Apply it to finite posets and small categories, noting which presheaves are representable and which are not. Use the embedding to transfer categorical problems to set-valued functor problems.

## Common Misconceptions
The Yoneda embedding is fully faithful but not surjective on objects—many presheaves are not representable. The embedding's usefulness comes from allowing non-representable presheaves to exist and be studied systematically. Full faithfulness means the category is determined by its morphism structure alone.
