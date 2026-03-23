---
id: stirling-numbers
title: Stirling Numbers of the First and Second Kind
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: permutations-and-combinations
  type: hard
- id: catalan-numbers
  type: soft
tags:
- combinatorics
- counting
stage: formal-systems
status: draft
---
# Stirling Numbers of the First and Second Kind

## Core Idea
Stirling numbers of the second kind S(n,k) count partitions of n elements into k non-empty subsets; Stirling numbers of the first kind s(n,k) count permutations with exactly k cycles. These numbers satisfy recurrences and appear in identities relating falling and rising factorials. They are central to partitions, cycle structures, and combinatorial applications.

## How It's Best Learned
Derive the recurrence relations for both kinds and verify with small examples (n ≤ 4) by explicit enumeration.

## Common Misconceptions
The two kinds of Stirling numbers are different; S(n,k) counts partitions into subsets while s(n,k) counts cycle permutations.

## Questions

```yaml
- question: "S(3, 2) = 3. Which explanation is correct?"
  type: multiple-choice
  options:
    - "There are 3 ordered ways to assign 3 labeled balls into 2 labeled boxes with no box empty"
    - "There are 3 unordered ways to split the labeled set {1,2,3} into exactly 2 non-empty subsets: {1}|{2,3}, {2}|{1,3}, {3}|{1,2}"
    - "There are 3 permutations of {1,2,3} with exactly 2 cycles"
    - "There are 3 ways to arrange 3 elements into 2 groups where order within groups matters"
  answer: 1
  explanation: "S(n,k) counts partitions of a labeled set into unlabeled non-empty subsets. For {1,2,3} into 2 parts: the three ways are {1}|{2,3}, {2}|{1,3}, and {3}|{1,2} — the singleton can be any of the three elements. The subsets are *unlabeled* (so {1}|{2,3} is the same as {2,3}|{1}), but the elements are *labeled* (so {1,2}|{3} differs from {1,3}|{2}). Option A describes ordered boxes (Stirling-like but not S(n,k)); option C describes c(3,2), the first kind (permutations with exactly 2 cycles); option D adds order within subsets, which S(n,k) does not."

- question: "The recurrence S(n, k) = k·S(n−1, k) + S(n−1, k−1) reflects what two possible situations for the nth element?"
  type: multiple-choice
  options:
    - "The nth element either forms a new subset alone, or merges with a previously formed subset"
    - "The nth element either joins one of the k existing subsets (k choices), or it starts a new singleton group that increases the count to k"
    - "The nth element either moves to the largest existing subset or the smallest"
    - "The nth element is either fixed or cycles with other elements"
  answer: 1
  explanation: "The recurrence splits based on what the nth element does when added to the configuration of n−1 elements. Case 1: the nth element joins one of the existing k subsets — there are k choices, giving k·S(n−1, k). Case 2: the nth element forms a new singleton subset, which means the previous n−1 elements were already arranged into k−1 subsets (so the new singleton brings the total to k) — giving S(n−1, k−1). These two cases are exhaustive and mutually exclusive, which is why their sum equals S(n, k). Understanding this recurrence makes Stirling numbers computable from small base cases."

- question: "The Stirling number of the first kind c(n, k) counts the number of permutations of n elements that have exactly k disjoint cycles."
  type: true-false
  answer: true
  explanation: "This is the correct definition of the (unsigned) Stirling number of the first kind. Every permutation can be written as a product of disjoint cycles — for example, the permutation sending 1→2→3→1 and 4→4 has two cycles: a 3-cycle and a fixed point. c(n, k) counts how many permutations of {1, 2, ..., n} have exactly k such cycles. For example, c(3, 2) = 3: the permutations of {1,2,3} with exactly 2 cycles are (12)(3), (13)(2), and (23)(1) — three transpositions each paired with a fixed point. This is a fundamentally different counting problem from S(n,k)."

- question: "The Stirling numbers of the first and second kind both count different aspects of the same combinatorial objects — set partitions."
  type: true-false
  answer: false
  explanation: "The two kinds count entirely different combinatorial objects. S(n, k) — second kind — counts partitions of a set of n labeled elements into k non-empty unlabeled subsets. c(n, k) — first kind — counts permutations of n elements with exactly k disjoint cycles. These are different structures: a partition divides a set into non-overlapping groups (no order implied), while a permutation is a bijection from a set to itself (order in each cycle matters). The confusion between them is the most common error when learning Stirling numbers — they have related recurrence structures but answer completely different questions."

- question: "Explain the role of Stirling numbers as 'change of basis' coefficients between falling factorials and ordinary powers of x."
  type: short-answer
  answer: "The falling factorial x^(n) = x(x−1)(x−2)···(x−n+1) and the ordinary power x^n are two different polynomial bases. Stirling numbers are the coefficients that convert between them. The falling factorial can be expanded as a sum of ordinary powers x^k, where the coefficients are (signed) Stirling numbers of the first kind: x^(n) = Σ s(n,k) x^k. Conversely, ordinary powers can be written as sums of falling factorials using Stirling numbers of the second kind: x^n = Σ S(n,k) x^(k). This 'change of basis' role is why Stirling numbers appear naturally in analysis (especially in finite differences and probability generating functions) wherever one basis is analytically convenient and the other is needed."
  explanation: "The polynomial basis analogy makes Stirling numbers analogous to binomial coefficients, which convert between the standard monomial basis and the choose-coefficient basis. The role of Stirling numbers as basis change operators explains their ubiquity: whenever an expression involves a factorial or power polynomial and you need to convert between representations, Stirling numbers are the natural tool. This connects combinatorics to analysis in a deep way — the cycle and partition structures of finite sets determine the algebra of polynomial operations on continuous variables."
```

## Explainer

From your work on permutations and combinations, you know how to count arrangements and selections of objects. Stirling numbers extend this toolkit to answer two questions that ordinary binomial coefficients cannot: how many ways can you partition a set into non-empty groups, and how many permutations have a specific cycle structure?

**Stirling numbers of the second kind**, written S(n, k), count the number of ways to partition a set of n labeled elements into exactly k non-empty, unlabeled subsets. For example, S(3, 2) = 3 because the set {1, 2, 3} can be split into two non-empty parts in exactly three ways: {1} and {2, 3}, {2} and {1, 3}, or {3} and {1, 2}. The subsets are unordered (so {1} | {2,3} is the same partition as {2,3} | {1}), but the elements within them are labeled. These numbers satisfy the recurrence S(n, k) = k·S(n−1, k) + S(n−1, k−1): either the nth element joins one of the k existing groups (k choices), or it forms a new singleton group.

**Stirling numbers of the first kind**, written c(n, k) or sometimes s(n, k) with appropriate sign conventions, count permutations of n elements with exactly k **cycles**. Recall from your combinatorics background that every permutation can be written as a product of disjoint cycles — for instance, the permutation (1→2→3→1, 4→4) has cycle type (3)(1). The Stirling number of the first kind c(4, 2) counts permutations of {1,2,3,4} with exactly 2 cycles. These also satisfy a recurrence: c(n, k) = c(n−1, k−1) + (n−1)·c(n−1, k), because the nth element either starts its own fixed cycle or inserts into one of the (n−1) positions within existing cycles.

The deeper reason these numbers matter is their connection to **falling and rising factorials**. The falling factorial x(x−1)(x−2)···(x−n+1) can be expanded as a sum of powers xᵏ with coefficients that are (signed) Stirling numbers of the first kind. Conversely, powers xⁿ can be expressed as sums of falling factorials using Stirling numbers of the second kind. This makes Stirling numbers the natural "change of basis" coefficients between two important polynomial bases — a role analogous to binomial coefficients transforming between ordinary and factorial polynomial families.
