---
id: permutations
title: Permutations
domain: mathematics
course: algebra-2
prerequisites:
  - id: factorial
    type: hard
builds-toward:
  - combinations
  - probability-with-combinatorics
tags: [combinatorics, permutations, counting, order-matters]
stage: abstract-reasoning
status: validated
---

# Permutations

## Core Idea
A permutation is an arrangement of objects where order matters. The number of permutations of n objects taken r at a time is P(n,r) = n!/(n-r)!. For all n objects: P(n,n) = n!. The fundamental counting principle underlies permutations: if there are n1 choices for the first position, n2 for the second, etc., the total is n1 * n2 * ... Permutations with repetition, circular permutations, and permutations with identical objects are common extensions.

## How It's Best Learned
Start with concrete examples: how many ways to arrange 3 books on a shelf? Use the fundamental counting principle to derive the formula. Contrast with combinations (where order does not matter). Practice with word problems: race placements, seating arrangements, license plates.

## Common Misconceptions
- Confusing permutations (order matters) with combinations (order does not matter).
- Using the formula incorrectly when objects repeat.
- Thinking P(n,r) = n^r (that is the number of arrangements with replacement, not permutations).
- Not recognizing when a problem is a permutation problem vs. a combination problem.

## Explainer

Your prerequisite, **factorial**, gave you a formula for counting the total number of ways to arrange n distinct objects: n! = n × (n−1) × (n−2) × ··· × 1. Three books on a shelf: 3! = 6 arrangements. Five runners in a race: 5! = 120 finish orderings. Factorial arises naturally because you're filling positions one at a time — n choices for the first slot, n−1 for the second (one is taken), and so on. A **permutation** extends this to the case where you're only choosing r of the n objects, not all of them.

The key insight is to think of filling r numbered slots. For the first slot, you have n options. Once that's chosen, n−1 options remain for the second slot. Continuing: the rth slot has n−(r−1) = n−r+1 options. By the **fundamental counting principle**, multiply these together: n × (n−1) × ··· × (n−r+1). This product can be written compactly as **P(n,r) = n! / (n−r)!**, because dividing by (n−r)! cancels the factorial terms you don't need. For the special case r = n (arranging everything), P(n,n) = n!/0! = n!, recovering your factorial formula.

A concrete example: how many ways can a club of 10 members elect a president, vice president, and treasurer (three distinct offices)? This is P(10, 3) = 10 × 9 × 8 = 720. Order matters here because "Alice-president, Bob-VP" is different from "Bob-president, Alice-VP." Compare this to a lottery where you pick 3 numbers from 10 — there, order *doesn't* matter, so you'd use combinations instead. The single question "does order matter?" determines which formula to use, and in permutations the answer is always yes.

Watch out for a common trap: **permutations without replacement** (the standard formula) differ from arrangements **with replacement**. If you're creating a 3-digit code where digits can repeat, you have 10 × 10 × 10 = 10³ = 1000 options, not P(10,3) = 720. In standard permutations, each object can only appear once in the arrangement — once a runner finishes first, they can't also finish second. The formula P(n,r) = n!/(n−r)! always assumes no repetition.
