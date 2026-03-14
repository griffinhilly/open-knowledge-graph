---
id: triangulated-categories
title: Triangulated Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: chain-complexes-exact-sequences
  type: hard
- id: derived-functors
  type: soft
builds-toward:
- derived-categories
- spectral-sequences-introduction
tags:
- triangulated-structure
- distinguished-triangles
- rotation
- homological-algebra
stage: abstract-reasoning
status: draft
---

# Triangulated Categories

## Core Idea
A triangulated category is an additive category equipped with an auto-equivalence (the translation functor) and a collection of distinguished triangles satisfying axioms that abstract the structure of short exact sequences and distinguished triangles in derived categories. Triangulated categories provide a framework for homological algebra that applies beyond the derived category setting.

## How It's Best Learned
Study the derived category of an abelian category, which is the canonical example of a triangulated category. Understand distinguished triangles as the categorical analogue of short exact sequences. Explore octahedral axioms and their consequences. Work with the rotation functor and its naturality.

## Common Misconceptions
A triangulated category is not necessarily the derived category of something; some triangulated categories have no t-structure or lift to an abelian category in a natural way. The octahedral axiom is non-obvious and its consequences require careful study.
