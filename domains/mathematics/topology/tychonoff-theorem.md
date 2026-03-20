---
id: tychonoff-theorem
title: Tychonoff's Theorem
domain: mathematics
course: topology
prerequisites:
- id: product-topology
  type: hard
- id: compact-spaces-open-covers
  type: hard
builds-toward:
- topological-manifolds-introduction
tags:
- tychonoff
- infinite-products
- compactness
stage: advanced
status: draft
---

# Tychonoff's Theorem

## Core Idea
Tychonoff's theorem states that an arbitrary product of compact topological spaces is compact in the product topology. For finite products this follows from elementary arguments, but the infinite case is a deep result equivalent to the Axiom of Choice. The proof typically uses Alexander's subbase theorem or Zorn's lemma to handle infinite open covers. Tychonoff's theorem is indispensable in functional analysis (the Banach-Alaoglu theorem depends on it), in probability (for constructing product measures), and throughout topology. It demonstrates that compactness, unlike many other properties, is perfectly preserved under arbitrary products.

## How It's Best Learned
First prove the finite product case directly, then study why the argument breaks for infinite products. Understanding where the Axiom of Choice enters—selecting finite subcovers simultaneously across infinitely many factors—clarifies both the theorem's depth and its logical status.

## Common Misconceptions
Students often assume the theorem is obvious because the finite case is straightforward. The infinite case is fundamentally different and requires a non-constructive choice principle. Also, the product topology (not the box topology) is essential—the theorem fails for the box topology on infinite products.

