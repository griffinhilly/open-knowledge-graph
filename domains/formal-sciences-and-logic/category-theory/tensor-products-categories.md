---
id: tensor-products-categories
title: Tensor Products in Category Theory
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- symmetric-monoidal-categories
- compact-closed-categories
tags:
- tensor
- monoidal
- bilinear
- universal-property
stage: advanced
status: draft
---

# Tensor Products in Category Theory

## Core Idea
The tensor product of two objects in a monoidal category is characterized by a universal property: Hom(A ⊗ B, C) ≅ Bilin(A × B, C), where Bilin denotes bilinear morphisms. Tensor products formalize the notion of free algebra on generators and are definable in any monoidal category. They carry monoidal structure from their factors and interact naturally with functors that preserve the monoidal structure.

## How It's Best Learned
Begin with tensor products in abelian groups and vector spaces, verifying the bilinear universal property. Compute tensor products of finite abelian groups and polynomial rings. Study how tensor products interact with limits and colimits.

## Common Misconceptions
Tensor product is not Cartesian product—it is right adjoint to hom in the appropriate monoidal category. Not every category admits a tensor product structure. Tensor products of categories (as opposed to objects within a monoidal category) follow different rules.
