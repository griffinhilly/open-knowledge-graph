---
id: tensor-products-universal
title: Tensor Products as Universal Constructions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: universal-properties
  type: hard
- id: products-and-coproducts
  type: soft
builds-toward:
- monoidal-categories
- tor-derived-tensor
tags:
- tensor-products
- universal-properties
- bilinear
stage: advanced
status: draft
---

# Tensor Products as Universal Constructions

## Core Idea
The tensor product A ⊗ B is characterized by a universal property: it represents bilinear maps from A × B. Explicitly, Hom(A ⊗ B, C) is naturally isomorphic to Hom_bilinear(A × B, C). Tensor products exist in abelian categories and many others, providing a way to 'linearize' multilinear constructions and generalize tensor products of modules over a ring.
