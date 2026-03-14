---
id: halls-marriage-theorem
title: Hall's Marriage Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: bipartite-matching
  type: hard
builds-toward:
- konigs-theorem
tags:
- graph-theory
- matching
- bipartite
stage: abstract-reasoning
status: draft
---

# Hall's Marriage Theorem

## Core Idea
Hall's Marriage Theorem characterizes when a perfect matching exists in a bipartite graph: a perfect matching from set A to set B exists if and only if for every subset S of A, |N(S)| ≥ |S| (neighborhood has at least as many vertices). This elegant criterion translates matching existence into a set-theoretic condition.

## How It's Best Learned
Prove the forward direction (perfect matching ⟹ Hall's condition) directly, then apply Hall's condition to concrete examples like assigning students to dorm rooms.

## Common Misconceptions
The condition must hold for ALL subsets S, not just single vertices or pairs. Checking only single vertices is insufficient.
