---
id: graph-minors-robertson-seymour
title: Graph Minors and the Robertson–Seymour Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs-kuratowski-wagner
  type: soft
tags:
- graph-minors
- robertson-seymour
- well-quasi-order
stage: abstract-reasoning
status: draft
---

# Graph Minors and the Robertson–Seymour Theorem

## Core Idea
A graph H is a minor of G if H can be obtained by deleting and contracting edges of G. The Robertson–Seymour theorem proves that the minor relation is a well-quasi-order, implying every minor-closed graph family is defined by finitely many forbidden minors. This deep result has profound algorithmic implications.

## How It's Best Learned
Compute minors by hand for small graphs, understanding how deletions and contractions reduce size. Recognize that tree-width and pathwidth are natural parameters arising from minor theory.
