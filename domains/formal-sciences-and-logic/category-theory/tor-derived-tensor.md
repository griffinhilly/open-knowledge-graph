---
id: tor-derived-tensor
title: Tor Functors as Derived Tensor Product
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: exact-sequences
  type: hard
- id: projective-objects
  type: hard
- id: tensor-products-universal
  type: soft
builds-toward:
- derived-functors
- homology-and-cohomology
tags:
- derived-functors
- homological-algebra
- tensor-products
stage: advanced
status: draft
---

# Tor Functors as Derived Tensor Product

## Core Idea
The Tor functor Tor_n(A, B) is the n-th left derived functor of − ⊗ B, computed via a projective resolution of A. Tor_1(A, B) measures the failure of A ⊗ − to be exact, capturing torsion phenomena. Higher Tor groups measure higher-order non-exactness. Tor is dual to Ext and crucial in computing tensor products of complexes and understanding flatness.
