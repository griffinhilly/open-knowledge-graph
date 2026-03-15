---
id: abelian-categories
title: Abelian Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: equalizers-and-coequalizers
  type: hard
- id: products-and-coproducts
  type: soft
- id: initial-and-terminal-objects
  type: soft
- id: group-definition-examples
  type: soft
- id: ring-definition-examples
  type: soft
- id: group-definition-and-examples
  type: soft
- id: vector-spaces
  type: soft
builds-toward:
- chain-complexes-exact-sequences
tags:
- abelian category
- additive category
- kernel
- cokernel
- exact sequence
- Ab-enriched
stage: advanced
status: draft
---
# Abelian Categories

## Core Idea
An abelian category is an additive category (enriched over abelian groups, with biproducts) in which every morphism has a kernel and cokernel, every monomorphism is the kernel of its cokernel, and every epimorphism is the cokernel of its kernel. This axiom system, formalized by Grothendieck and Buchsbaum, captures the essential properties of categories like Ab (abelian groups), R-Mod (modules over a ring), and sheaves of abelian groups, enabling homological algebra to be developed in a purely categorical setting. The Freyd-Mitchell embedding theorem shows every small abelian category embeds exactly into some R-Mod, justifying diagram-chasing arguments.

## How It's Best Learned
Verify the abelian category axioms for R-Mod: check that hom-sets are abelian groups, biproducts exist (direct sums), every morphism has a kernel and cokernel, and the canonical factorization image(f) → coimage(f) is an isomorphism. Then try to find a non-example: the category of free abelian groups is additive but not abelian (cokernels may not be free).

## Common Misconceptions
- Not every additive category is abelian; the existence of kernels and cokernels plus the factorization axiom are essential additional conditions.
- The Freyd-Mitchell embedding theorem applies only to small abelian categories; it does not mean every abelian category literally is a module category.
- An abelian category is not the same as an Ab-enriched category; abelian requires additional exactness properties beyond mere enrichment.
