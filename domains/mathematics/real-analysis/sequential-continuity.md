---
id: sequential-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
tags:
- continuity
- sequences
- equivalence
stage: advanced
status: draft
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) with xₙ → c, we have f(xₙ) → f(c). This equivalence allows switching between ε-δ and sequential definitions: use sequences when natural, ε-δ when rigor demands it. The equivalence is a fundamental tool for proofs.

## How It's Best Learned
Prove f(x) = x² is continuous at 2 using both definitions, then use sequences to show f(x) = ⌊x⌋ is not continuous at integers.

## Common Misconceptions
- Assuming sequences must approach the continuity point monotonically or regularly; any convergent sequence works.
- Forgetting the 'if and only if': the equivalence works in both directions.
- Thinking sequential continuity is weaker; it is equivalent to ε-δ continuity in ℝ.
