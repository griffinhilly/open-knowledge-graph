---
id: permutations
title: Permutations
domain: mathematics
course: algebra-2
prerequisites:
  - id: factorial
    type: hard
  - id: counting-principles-probability-and-statistics
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

## Questions

```yaml
- question: "A club of 10 members needs to elect a president, vice president, and treasurer — three distinct roles. How many different outcomes are possible?"
  type: multiple-choice
  options:
    - "10^3 = 1,000, because there are 10 choices for each of the three roles"
    - "10! = 3,628,800, because all members must be assigned a position"
    - "P(10,3) = 720, because the same member cannot hold two roles and the roles are distinct"
    - "C(10,3) = 120, because we are selecting 3 people from 10"
  answer: 2
  explanation: "This is a permutation because the three roles are distinct — 'Alice-president, Bob-VP' is a different outcome from 'Bob-president, Alice-VP.' We fill 3 ordered slots from 10 candidates without replacement: 10 × 9 × 8 = P(10,3) = 720. Option A (10^3 = 1000) would be correct if the same person could hold multiple roles (repetition allowed). Option D (combinations) would be correct only if the roles were identical — which they are not."

- question: "A student creates a 3-digit PIN where digits can repeat (e.g., 007 is valid). Another student counts the number of ways to arrange 3 different digits from 0–9 onto a sequence of numbered slots. Which student is solving a permutation problem?"
  type: multiple-choice
  options:
    - "The first student, because PINs require order to matter"
    - "The second student, because permutations require no repetition"
    - "Both students, because both problems involve ordered arrangements"
    - "Neither student, because both problems involve digits, not objects"
  answer: 1
  explanation: "The second student is solving a standard permutation problem: P(10,3) = 720 ordered arrangements of 3 distinct digits. The first student's PIN problem allows repetition, giving 10 × 10 × 10 = 10^3 = 1,000 — this is not a permutation. Order matters in both problems, but permutations specifically assume no repetition. The common misconception is that P(n,r) = n^r; in fact, n^r counts ordered arrangements *with* replacement, while P(n,r) = n!/(n-r)! counts them *without*."

- question: "P(n,r) = n!/(n–r)! counts the number of ordered arrangements of r objects chosen from n distinct objects without replacement."
  type: true-false
  answer: true
  explanation: "This is the definition of a permutation. Filling r ordered slots from n objects without replacement gives n choices for slot 1, n–1 for slot 2, ..., down to n–r+1 for slot r. The product n × (n–1) × ··· × (n–r+1) equals n!/(n–r)! because dividing n! by (n–r)! cancels the unwanted factorial terms."

- question: "The number of ways to arrange most 5 books on a shelf equals P(5,3), because you are placing 5 objects in 3 possible positions."
  type: true-false
  answer: false
  explanation: "When arranging all n objects, the correct formula is P(n,n) = n!/0! = n!. Arranging 5 books on a shelf gives 5! = 120, not P(5,3) = 60. P(5,3) would count ordered arrangements of only 3 books chosen from 5 — that is, filling 3 labeled slots while leaving 2 books aside."

- question: "Why does P(n,r) = n!/(n–r)! rather than n^r? What scenario would n^r correctly count, and what makes it different from a permutation?"
  type: short-answer
  answer: "P(n,r) = n!/(n–r)! counts ordered arrangements without replacement: each object can appear at most once, so choices shrink at each slot (n, then n–1, then n–2…). n^r counts ordered arrangements with replacement: each slot is filled independently from all n options, so the number of choices stays constant at n per slot. The difference is whether the same object can appear more than once. For example, arranging 3 different winners from 10 runners is P(10,3) = 720; generating a 3-digit code where digits can repeat is 10^3 = 1,000."
  explanation: "The formula P(n,r) = n!/(n–r)! is derived from the counting principle applied to shrinking choices. n^r treats each position as an independent choice, which is correct when repetition is allowed — license plates, PINs, passwords. Permutations model scenarios like race placements or officer elections where one object cannot occupy two positions simultaneously."
```

## Explainer

Your prerequisite, **factorial**, gave you a formula for counting the total number of ways to arrange n distinct objects: n! = n × (n−1) × (n−2) × ··· × 1. Three books on a shelf: 3! = 6 arrangements. Five runners in a race: 5! = 120 finish orderings. Factorial arises naturally because you're filling positions one at a time — n choices for the first slot, n−1 for the second (one is taken), and so on. A **permutation** extends this to the case where you're only choosing r of the n objects, not all of them.

The key insight is to think of filling r numbered slots. For the first slot, you have n options. Once that's chosen, n−1 options remain for the second slot. Continuing: the rth slot has n−(r−1) = n−r+1 options. By the **fundamental counting principle**, multiply these together: n × (n−1) × ··· × (n−r+1). This product can be written compactly as **P(n,r) = n! / (n−r)!**, because dividing by (n−r)! cancels the factorial terms you don't need. For the special case r = n (arranging everything), P(n,n) = n!/0! = n!, recovering your factorial formula.

A concrete example: how many ways can a club of 10 members elect a president, vice president, and treasurer (three distinct offices)? This is P(10, 3) = 10 × 9 × 8 = 720. Order matters here because "Alice-president, Bob-VP" is different from "Bob-president, Alice-VP." Compare this to a lottery where you pick 3 numbers from 10 — there, order *doesn't* matter, so you'd use combinations instead. The single question "does order matter?" determines which formula to use, and in permutations the answer is always yes.

Watch out for a common trap: **permutations without replacement** (the standard formula) differ from arrangements **with replacement**. If you're creating a 3-digit code where digits can repeat, you have 10 × 10 × 10 = 10³ = 1000 options, not P(10,3) = 720. In standard permutations, each object can only appear once in the arrangement — once a runner finishes first, they can't also finish second. The formula P(n,r) = n!/(n−r)! always assumes no repetition.
