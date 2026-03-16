---
id: proof-by-cases-exhaustion
title: Proof by Cases
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-terminology
  type: hard
- id: set-operations-union-intersection-complement
  type: soft
builds-toward:
- mathematical-induction-intro
tags:
- proof
- cases
- exhaustion
stage: formal-systems
status: draft
---

# Proof by Cases

## Core Idea
A proof by cases partitions the domain into exhaustive, non-overlapping cases and proves the goal within each case. If the goal holds for every case, it holds overall. This technique is essential when direct proof requires considering different scenarios or when natural divisions in the domain suggest different proof strategies.

## Explainer

You know the standard proof structure: state what you assume, state what you want to show, provide a valid sequence of steps. Proof by cases applies when a single chain of reasoning cannot handle every element of the domain at once — different parts of the domain require different arguments. The key idea is **partitioning**: you divide the domain into a finite collection of cases whose union covers the entire domain (exhaustive) and whose pairwise intersections are empty (non-overlapping). Prove the goal for each case, and the union of those proofs constitutes a proof for all elements.

The exhaustiveness requirement is non-negotiable. If you miss a case, your proof has a gap — there exist elements the argument does not cover, and the conclusion may fail there. From your prerequisite knowledge of set operations, exhaustiveness means the union of your cases equals the entire domain. Non-overlapping means the cases' pairwise intersections are empty, though in practice some overlap is allowed as long as every element is covered — what matters is that no element falls through the cracks.

A classic example illustrates the technique cleanly. **Claim**: For any integer n, n² + n is even. Proof by cases on the parity of n. *Case 1: n is even.* Then n = 2k for some integer k, so n² + n = 4k² + 2k = 2(2k² + k), which is even. *Case 2: n is odd.* Then n = 2k + 1 for some integer k, so n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 1 + 2k + 1 = 4k² + 6k + 2 = 2(2k² + 3k + 1), which is even. Since every integer is either even or odd (exhaustive), and these cases are non-overlapping, the result holds for all integers.

The art of proof by cases is identifying the right partition. Natural partitions arise from sign (positive, zero, negative), parity (even, odd), ordering (x < y, x = y, x > y), or membership in a set. In more advanced proofs, the partition may arise from whether a certain condition holds (satisfies property P vs. does not satisfy P). Good cases are ones where the proof inside each case simplifies — if your cases don't make the internal argument easier, you have probably chosen the wrong partition. Practice recognizing the natural fault lines in a problem before writing the proof.
