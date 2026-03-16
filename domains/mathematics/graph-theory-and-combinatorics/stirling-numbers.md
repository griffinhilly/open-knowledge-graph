---
id: stirling-numbers
title: Stirling Numbers of the First and Second Kind
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: permutations-and-combinations
  type: hard
tags:
- combinatorics
- counting
stage: abstract-reasoning
status: draft
---

# Stirling Numbers of the First and Second Kind

## Core Idea
Stirling numbers of the second kind S(n,k) count partitions of n elements into k non-empty subsets; Stirling numbers of the first kind s(n,k) count permutations with exactly k cycles. These numbers satisfy recurrences and appear in identities relating falling and rising factorials. They are central to partitions, cycle structures, and combinatorial applications.

## How It's Best Learned
Derive the recurrence relations for both kinds and verify with small examples (n ≤ 4) by explicit enumeration.

## Common Misconceptions
The two kinds of Stirling numbers are different; S(n,k) counts partitions into subsets while s(n,k) counts cycle permutations.

## Explainer

From your work on permutations and combinations, you know how to count arrangements and selections of objects. Stirling numbers extend this toolkit to answer two questions that ordinary binomial coefficients cannot: how many ways can you partition a set into non-empty groups, and how many permutations have a specific cycle structure?

**Stirling numbers of the second kind**, written S(n, k), count the number of ways to partition a set of n labeled elements into exactly k non-empty, unlabeled subsets. For example, S(3, 2) = 3 because the set {1, 2, 3} can be split into two non-empty parts in exactly three ways: {1} and {2, 3}, {2} and {1, 3}, or {3} and {1, 2}. The subsets are unordered (so {1} | {2,3} is the same partition as {2,3} | {1}), but the elements within them are labeled. These numbers satisfy the recurrence S(n, k) = k·S(n−1, k) + S(n−1, k−1): either the nth element joins one of the k existing groups (k choices), or it forms a new singleton group.

**Stirling numbers of the first kind**, written c(n, k) or sometimes s(n, k) with appropriate sign conventions, count permutations of n elements with exactly k **cycles**. Recall from your combinatorics background that every permutation can be written as a product of disjoint cycles — for instance, the permutation (1→2→3→1, 4→4) has cycle type (3)(1). The Stirling number of the first kind c(4, 2) counts permutations of {1,2,3,4} with exactly 2 cycles. These also satisfy a recurrence: c(n, k) = c(n−1, k−1) + (n−1)·c(n−1, k), because the nth element either starts its own fixed cycle or inserts into one of the (n−1) positions within existing cycles.

The deeper reason these numbers matter is their connection to **falling and rising factorials**. The falling factorial x(x−1)(x−2)···(x−n+1) can be expanded as a sum of powers xᵏ with coefficients that are (signed) Stirling numbers of the first kind. Conversely, powers xⁿ can be expressed as sums of falling factorials using Stirling numbers of the second kind. This makes Stirling numbers the natural "change of basis" coefficients between two important polynomial bases — a role analogous to binomial coefficients transforming between ordinary and factorial polynomial families.
