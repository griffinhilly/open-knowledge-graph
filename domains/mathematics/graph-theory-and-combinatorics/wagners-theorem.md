---
id: wagners-theorem
title: Wagner's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: kuratowskis-theorem
  type: hard
builds-toward:
- graph-minors
tags:
- graph-theory
- planar-graphs
- minors
stage: abstract-reasoning
status: draft
---

# Wagner's Theorem

## Core Idea
Wagner's Theorem states that a graph is planar if and only if it contains neither K₅ nor K₃,₃ as minors. This formulation is equivalent to Kuratowski's theorem but uses the stronger minor relation, showing that planarity can be characterized by two forbidden minors alone.

## How It's Best Learned
Study the relationship between subdivisions and minors; understand why contracting edges gives a weaker condition than just forbidding subdivisions.

## Common Misconceptions
Forbidding K₅ and K₃,₃ as minors is sufficient; you do not need to check any other minors or forbidden subgraphs.
