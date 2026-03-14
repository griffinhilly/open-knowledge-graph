---
id: triangulated-categories
title: Triangulated Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-equivalences
tags:
- triangulated
- distinguished-triangle
- long-exact-sequence
- derived-category
stage: advanced
status: draft
---

# Triangulated Categories

## Core Idea
A triangulated category is an additive category with a suspension functor and a distinguished collection of triangles satisfying four axioms (octahedral axiom and shift closure). Distinguished triangles behave like short exact sequences: they give rise to long exact sequences in homology and encode the composition structure of derived categories. Triangulated categories abstract the essential homological properties common to derived categories, homology, and cohomology theories.

## How It's Best Learned
Study the derived category D(R) of an abelian category, verifying that distinguished triangles come from short exact sequences in the derived category. Compute long exact sequences from triangles. Verify the octahedral axiom in concrete examples.

## Common Misconceptions
Triangulated categories are subtle; the axioms are more complex than they initially appear. Not every category that looks homological is triangulated—the axioms are necessary and restrictive. The octahedral axiom is deep and its necessity is not obvious; failure to satisfy it indicates missing triangulated structure.
