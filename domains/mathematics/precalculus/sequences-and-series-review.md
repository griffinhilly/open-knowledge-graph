---
id: sequences-and-series-review
title: Sequences and Series Review
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
builds-toward:
  - sequences-convergence
  - series-definition-and-partial-sums
  - geometric-series
tags: [sequences, series, summation]
stage: formal-systems
status: validated
---

# Sequences and Series Review

## Core Idea
A sequence is an ordered list of numbers defined by a rule (explicit formula or recursive definition). A series is the sum of the terms of a sequence. Arithmetic sequences have a constant difference; geometric sequences have a constant ratio. Sigma notation provides a compact way to write sums. This review establishes the vocabulary and formulas needed for the rigorous convergence analysis in Calculus 2.

## How It's Best Learned
Practice writing explicit and recursive formulas for arithmetic and geometric sequences. Compute partial sums using the formulas (arithmetic: n/2 * (first + last), geometric: a(1 - r^n)/(1 - r)). Introduce sigma notation and practice expanding and condensing sums.

## Common Misconceptions
- Confusing sequences (lists) with series (sums).
- Using the wrong formula for geometric vs. arithmetic sums.
- Off-by-one errors in sigma notation (incorrect starting or ending index).

## Explainer

You already know **function notation**: f(n) assigns a value to each input n. A **sequence** is simply a function whose domain is the positive integers (or non-negative integers). Writing aₙ instead of f(n) is just a notational convenience — aₙ is the n-th term of the sequence. The sequence 2, 5, 8, 11, ... could be described by the explicit formula aₙ = 2 + 3(n − 1), or recursively by a₁ = 2 and aₙ = aₙ₋₁ + 3. Both descriptions define the same sequence; the explicit formula is faster for finding the 100th term, while the recursive formula better captures how each term is built from the previous one.

The two fundamental sequence types to recognize are **arithmetic** (constant difference) and **geometric** (constant ratio). In an arithmetic sequence, each term adds a fixed number d: aₙ = a₁ + (n − 1)d. In a geometric sequence, each term multiplies by a fixed number r: aₙ = a₁ · rⁿ⁻¹. Identifying which type you have is the first step in any problem — once you know the type, the formula for its partial sum follows directly. For arithmetic sequences, the sum of the first n terms is Sₙ = n/2 · (a₁ + aₙ), which you can visualize by pairing the first and last terms, the second and second-to-last, and so on — each pair sums to the same value. For geometric sequences, Sₙ = a₁(1 − rⁿ)/(1 − r), derived algebraically by writing S − rS and watching most terms cancel.

A **series** is the sum of sequence terms, and **sigma notation** is the compact language for writing such sums. The expression Σᵢ₌₁ⁿ aᵢ means "sum aᵢ for i from 1 to n." The index variable (i here) is a placeholder — it only exists inside the sum. Common errors come from off-by-one mistakes: Σᵢ₌₀ⁿ has n + 1 terms, not n. Reading sigma notation fluently requires practice expanding a few examples before trying to compress expressions.

This review matters because **calculus** will ask whether infinite series converge. The geometric series is the key test case: Σᵢ₌₀^∞ rⁿ = 1/(1 − r) when |r| < 1, but diverges when |r| ≥ 1. You can see this from the partial sum formula: as n → ∞, rⁿ → 0 if |r| < 1, so Sₙ → a₁/(1 − r). Everything you study in Calculus 2 about series convergence is a generalization of this one finite-to-infinite leap. Knowing the arithmetic and geometric formulas cold — and being comfortable with sigma notation — means you can focus on the new ideas of convergence rather than re-learning foundational mechanics at the worst possible moment.
