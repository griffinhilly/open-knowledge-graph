---
id: permutations-arrangements-discrete
title: Permutations and Arrangements
domain: mathematics
course: discrete-math
prerequisites:
- id: counting-fundamentals-discrete
  type: hard
- id: factorial
  type: hard
builds-toward:
- combinations-selections-discrete
- binomial-theorem-discrete
tags:
- permutations
- arrangements
- ordering
- P(n,r)
stage: formal-systems
status: draft
---

# Permutations and Arrangements

## Core Idea
A permutation is an ordered arrangement of distinct objects. The number of r-permutations of n objects is P(n, r) = n!/(n−r)!. When order matters—choosing a president, vice-president, and treasurer—permutations apply.

## How It's Best Learned
Use the multiplication principle to derive P(n, r): first position has n choices, second has n−1, etc. Practice distinguishing permutations (order matters) from combinations (order doesn't).

## Common Misconceptions
Permutations require distinct objects; if objects repeat, the formula changes. The formula P(n, r) assumes choosing without replacement and that order distinguishes arrangements.

## Explainer

A **permutation** is any ordered arrangement of objects. "Ordered" is the key word: the arrangement (Alice, Bob, Carol) is different from (Bob, Alice, Carol), even though they involve the same three people. When you studied the multiplication principle in counting fundamentals, you learned to multiply independent choices. Permutations apply that principle to sequential slots where each choice reduces the available options.

Suppose you want to arrange 3 of 5 students in a line for a photo. The first slot has 5 choices. Once that student is placed, the second slot has only 4 remaining choices. The third slot has 3. The total is 5 × 4 × 3 = 60. This is **P(5, 3)** — the number of ways to arrange 3 objects chosen from 5, where order matters. In general, **P(n, r) = n × (n−1) × ⋯ × (n−r+1)**, which collapses neatly using the factorial you learned: P(n, r) = n! / (n−r)!. The (n−r)! in the denominator cancels the tail of the factorial that was never used.

The factorial connection is worth pausing on. Factorial was introduced as "the number of ways to arrange n distinct objects in a complete sequence." That is just P(n, n) = n!/0! = n!. Permutations generalize this to partial arrangements — you're selecting r of the n objects to place, and the order of placement distinguishes outcomes. When r = n, you recover the factorial.

The hardest skill in permutation problems is distinguishing whether order matters. Consider: "How many ways can you choose a president and a vice-president from a 10-person club?" The offices are distinct — who gets which role matters — so this is a permutation: P(10, 2) = 90. Compare to "How many 2-person committees can be chosen from 10 people?" Committees don't have ranked roles; {Alice, Bob} is the same committee as {Bob, Alice}. That is a combination problem, which you'll study next. The test is simple: if swapping two choices produces a different outcome, it's a permutation.

One important boundary: the standard formula assumes you are choosing **without replacement** (no object appears twice) and that all objects are **distinct**. If objects can repeat (e.g., digit sequences where the same digit can reappear), the count is n^r, not P(n, r). If objects are not all distinct (e.g., arrangements of the letters in "MISSISSIPPI"), the formula must be divided by the factorials of the repeated element counts. The formula P(n, r) = n!/(n−r)! is the clean, foundational case; understanding its assumptions helps you recognize when a variant is needed.
