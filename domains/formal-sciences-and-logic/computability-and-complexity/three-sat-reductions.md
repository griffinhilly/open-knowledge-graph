---
id: three-sat-reductions
title: 3-SAT and Reduction-Based Hardness Proofs
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: sat-canonical-problem
  type: hard
builds-toward:
- hardness-approximation
- complexity-lower-bounds
tags:
- 3-sat
- reductions
- graph-problems
- hardness-proofs
stage: advanced
status: draft
---

# 3-SAT and Reduction-Based Hardness Proofs

## Core Idea
3-SAT restricts SAT to formulas in conjunctive normal form with exactly 3 literals per clause. Despite this restriction, 3-SAT remains NP-complete and is the most common source for polynomial-time reductions proving other problems NP-complete. It provides a practical template for constructing hardness proofs across scheduling, graph algorithms, and optimization problems.

## How It's Best Learned
Work through classic 3-SAT reductions (CLIQUE, VERTEX-COVER, INDEPENDENT-SET). Build a reduction from vertex cover to 3-SAT yourself.

## Common Misconceptions
- Confusing the direction: 3-SAT reduces to other problems, proving them NP-hard, not the reverse.
- Assuming 3-SAT is harder than general SAT; they are equally hard (both NP-complete).
