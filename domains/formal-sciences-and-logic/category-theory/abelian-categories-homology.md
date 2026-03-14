---
id: abelian-categories-homology
title: Abelian Categories and Homological Algebra
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-functors
- triangulated-categories
tags:
- abelian
- homology
- exact-sequence
- kernel
- cokernel
stage: advanced
status: draft
---

# Abelian Categories and Homological Algebra

## Core Idea
An abelian category is an additive category with kernels, cokernels, and images, in which every monomorphism is a kernel and every epimorphism is a cokernel. Abelian categories provide the natural setting for homological algebra: chain complexes, homology, cohomology, and derived functors. Examples include module categories, vector spaces, and abelian groups. The theory of abelian categories abstracts homological algebra to axiomatic foundations.

## How It's Best Learned
Study module categories and vector space categories as canonical abelian examples. Verify the five lemma and snake lemma for abelian categories. Compute derived functors (Ext, Tor) via projective and injective resolutions in abelian categories.

## Common Misconceptions
Abelian categories generalize module categories but are not just 'categorical algebra'—they require specific exactness properties. Not every additive category is abelian; the kernel-cokernel conditions are non-trivial. Abelian category axioms are sufficient for homological algebra but some conclusions require additional structure (e.g., enough projectives).
