---
id: proof-by-cases
title: Proof by Cases
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
builds-toward:
- existence-proofs
tags:
- proof-by-cases
- exhaustive-proof
- case-analysis
- parity
stage: formal-systems
status: validated
---

# Proof by Cases

## Core Idea
A proof by cases (or exhaustive proof) divides the domain of possible inputs into a finite number of mutually exclusive, collectively exhaustive cases and proves the conclusion holds in each case. The proof is complete only if every case is covered. A common structure is dividing by parity (even vs. odd), by sign (positive, negative, zero), or by a modular condition. Proof by cases is essential when no single argument handles all possibilities uniformly.

## How It's Best Learned
Practice with small exhaustive cases: prove that n(n+1) is even for all integers n by considering n even and n odd. Emphasize the obligation to verify exhaustiveness — every possible scenario must fall into exactly one case.

## Common Misconceptions
- Missing a case (e.g., forgetting the n = 0 case when splitting positive and negative).
- Allowing cases to overlap without explicitly handling the overlap.
- Using proof by cases when a unified argument (e.g., modular arithmetic) would be simpler.
