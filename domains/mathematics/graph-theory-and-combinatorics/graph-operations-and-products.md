---
id: graph-operations-and-products
title: Graph Operations and Products
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- graph-minors-robertson-seymour
tags:
- graph-operations
- cartesian-product
- graph-composition
stage: abstract-reasoning
status: draft
---

# Graph Operations and Products

## Core Idea
Graph products (Cartesian, tensor, strong, lexicographic) combine two graphs to form new graphs with inherited structural properties. Each product definition yields different degree sequences, diameter bounds, and connectivity properties. Operations like union, join, and complement are equally important for constructing specialized graph families.

## How It's Best Learned
Compute the Cartesian product of two small paths or cycles by hand, visualizing the grid structure. Then verify degree formulas and diameter bounds. Compare different products on the same pair of graphs to see how the definitions diverge.

## Common Misconceptions
- Assuming the Cartesian product of two connected graphs is always connected (true) or that all products preserve connectivity equally (false).
- Confusing edge definitions across product types; the tensor product and Cartesian product have fundamentally different edge sets.
