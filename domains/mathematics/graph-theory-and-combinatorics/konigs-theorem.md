---
id: konigs-theorem
title: König's Theorem and Matching-Cover Duality
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: halls-marriage-theorem
  type: hard
tags:
- graph-theory
- matching
- vertex-cover
stage: formal-systems
status: draft
---

# König's Theorem and Matching-Cover Duality

## Core Idea
König's Theorem states that in a bipartite graph, the size of the maximum matching equals the size of the minimum vertex cover. This fundamental duality shows that finding maximum matchings and minimum covers are essentially the same problem in bipartite graphs, with profound implications for optimization.

## How It's Best Learned
Work through small bipartite graphs, computing maximum matchings and minimum covers, verifying they have equal size.

## Common Misconceptions
This equality holds ONLY for bipartite graphs; in general graphs, matching size can be strictly less than vertex cover size.
