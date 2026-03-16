---
id: factorial
title: Factorial
domain: mathematics
course: algebra-2
prerequisites:
  - id: multiplying-polynomials
    type: soft
builds-toward:
  - permutations
  - binomial-theorem
tags: [factorial, combinatorics, counting]
stage: abstract-reasoning
status: validated
---

# Factorial

## Core Idea
The factorial of a non-negative integer n, written n!, is the product of all positive integers from 1 to n: n! = n × (n−1) × (n−2) × ... × 2 × 1. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120. By convention, 0! = 1 (this is not arbitrary — it's required for combinatorial formulas to work correctly and is consistent with the empty product). Factorials grow extremely fast: 10! = 3,628,800 and 20! exceeds 2.4 × 10¹⁸. Factorials are fundamental to counting problems because n! counts the number of ways to arrange n distinct objects in a sequence (permutations), making them the building block for permutations, combinations, and the binomial theorem.

## How It's Best Learned
Start with a concrete counting problem: "How many ways can 3 people line up?" List all 6 arrangements, then show the multiplication principle (3 choices × 2 choices × 1 choice = 3! = 6). Extend to 4 and 5 people to build the pattern. Introduce the notation and the recursive definition: n! = n × (n−1)!. Address 0! = 1 by showing it's needed for formulas like C(n,0) = n!/0!n! = 1 to work. Practice computing factorials by hand for small values, then discuss how quickly they grow. Connect to permutations and combinations as the immediate applications.

## Common Misconceptions
- Thinking 0! = 0 — it equals 1 by definition, and this is essential for combinatorial formulas to remain consistent.
- Confusing n! with n × ! or treating the exclamation point as emphasis rather than a mathematical operation.
- Not recognizing how to simplify factorial expressions like 8!/6! = 8 × 7 = 56 (canceling common factors instead of computing both factorials separately).
- Underestimating factorial growth — students often don't realize that 20! is astronomically large while 20² is just 400.

## Explainer

Factorials emerge from a single concrete question: in how many different orders can you arrange a set of distinct objects? Suppose you have three books to place on a shelf. The first slot can hold any of the 3 books. Once placed, 2 books remain for the second slot. One book is left for the third. The **multiplication principle** — the number of sequences equals the product of choices at each step — gives 3 × 2 × 1 = 6. This is 3! (read "three factorial"). For n distinct objects, the count of possible orderings is n! = n × (n−1) × (n−2) × … × 2 × 1. Every factorial is answering this arrangement-counting question.

The growth of factorials is explosive compared to the other functions you've worked with. Polynomial growth (n², n³) and even exponential growth (2^n) are left behind quickly: 2^10 = 1,024, but 10! = 3,628,800. By 20!, you exceed 2.4 × 10¹⁸ — roughly the number of grains of sand on Earth. This explosive growth is why factorials appear in probability: a standard deck of 52 cards can be shuffled into 52! ≈ 8 × 10⁶⁷ possible orders, so a randomly shuffled deck has almost certainly never been in that exact arrangement before. Developing intuition for factorial magnitude helps you know when a result is plausible.

The convention **0! = 1** is not arbitrary. Think of it this way: "How many ways can you arrange zero objects?" There is exactly one way — the empty arrangement. This matches the general pattern: 1! = 1 (one arrangement of one object), and moving from n! to (n−1)! divides by n. Working backward: 1!/1 = 0! must equal 1. More practically, 0! = 1 is required for combinatorial formulas to be consistent. The combination C(n, 0) = n!/(0! · n!) must equal 1 (there is exactly one way to choose nothing from n items). If 0! = 0, this formula would be undefined, breaking every counting formula that uses it.

A critical computational skill is **canceling factorials** rather than expanding both. To compute 8!/6!, do not calculate each separately. Instead: 8!/6! = (8 × 7 × 6 × 5 × … × 1)/(6 × 5 × … × 1). Everything from 6 down to 1 appears in both numerator and denominator and cancels, leaving 8 × 7 = 56. This pattern is universal in combinatorics: the permutation formula P(n, r) = n!/(n−r)! always reduces to a product of exactly r consecutive integers from n downward. Recognizing and applying this cancellation transforms computations that would otherwise be intractable into one-step arithmetic.
