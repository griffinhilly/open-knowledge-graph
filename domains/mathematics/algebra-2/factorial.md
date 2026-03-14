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
