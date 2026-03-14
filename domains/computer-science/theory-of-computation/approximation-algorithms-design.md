---
id: approximation-algorithms-design
title: Approximation Algorithms and Approximation Ratios
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- hardness-of-approximation
tags:
- hardness
- approximation
- optimization
stage: advanced
status: draft
---

# Approximation Algorithms and Approximation Ratios

## Core Idea
For NP-hard optimization problems, approximation algorithms find near-optimal solutions in polynomial time. An algorithm is an α-approximation if its solution is at most α times the optimal (for minimization problems). Vertex cover has a simple 2-approximation (greedy edge selection); TSP has a 1.5-approximation (Christofides algorithm); general TSP permits no better than 1.001-approximation without P=NP. The field explores the boundary between hardness and tractability, showing approximate solutions often suffice where exact ones are intractable.

## How It's Best Learned
Implement greedy approximation algorithms and analyze their ratios empirically. Prove approximation guarantees mathematically. Compare approximation quality to hardness lower bounds.

## Common Misconceptions
Thinking approximation algorithms solve NP-complete problems in polynomial time (they trade exactness for speed). Confusing constant approximations with polynomial approximations (some problems cannot achieve constant approximation unless P=NP). Assuming all NP-hard problems admit good approximations (some are inapproximable).
