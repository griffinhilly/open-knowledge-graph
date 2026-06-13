---
id: sequences-and-series-review
title: Sequences and Series Review
domain: mathematics
course: precalculus
prerequisites:
- id: function-notation-review
  type: soft
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

## Questions

```yaml
- question: "The partial sums of the geometric sequence 1, 1/2, 1/4, 1/8, ... are computed up to 10 terms, then 100 terms, then 1000 terms. What happens to these partial sums?"
  type: multiple-choice
  options:
    - "They grow without bound, since we are always adding positive terms"
    - "They approach 2, since the infinite geometric series converges to a₁/(1-r) = 1/(1-½) = 2"
    - "They approach 1, since the first term is 1 and the remaining terms are increasingly negligible"
    - "They fluctuate, since the terms alternate between larger and smaller values"
  answer: 1
  explanation: "The series has first term a₁ = 1 and ratio r = 1/2. Since |r| < 1, the partial sum formula Sₙ = a₁(1-rⁿ)/(1-r) = 2(1-(1/2)ⁿ) approaches 2 as n→∞. Option C is the tempting trap: students assume the first term dominates, but the infinite tail sums contribute a full additional 1 to the total. Adding infinitely many positive terms can still yield a finite sum — this is the key insight that launches all of Calculus 2 series convergence theory."

- question: "You are given the sequence 3, 6, 12, 24, 48, ... and asked to find the sum of the first 7 terms. Which formula applies?"
  type: multiple-choice
  options:
    - "Sₙ = n/2 · (a₁ + aₙ), because the sequence has a constant second difference"
    - "Sₙ = a₁(1-rⁿ)/(1-r) with r = 2, because this is a geometric sequence"
    - "Sₙ = a₁(1-rⁿ)/(1-r) with r = 3, because each term adds 3"
    - "Sₙ = n/2 · (a₁ + aₙ), because each term is double the previous"
  answer: 1
  explanation: "Each term is multiplied by 2 (constant ratio r = 2), making this a geometric sequence. The geometric partial sum formula gives S₇ = 3(1-2⁷)/(1-2) = 3(-127)/(-1) = 381. The arithmetic sum formula (average of first and last, times n) applies only when there is a constant difference. Identifying the sequence type before selecting a formula is the essential first step — applying the arithmetic formula here would give the wrong answer."

- question: "The series 1 + 3 + 5 + 7 + ... (the sum of odd numbers) and the sequence 1, 3, 5, 7, ... are two names for the same mathematical object."
  type: true-false
  answer: false
  explanation: "The sequence 1, 3, 5, 7, ... is an ordered list of terms. The series 1 + 3 + 5 + 7 + ... is the sum of those terms — a completely different object. The sequence is a function mapping integers to values; the series is a number (or a divergent accumulation). Sigma notation makes the distinction explicit: the sequence is aₙ = 2n-1, while the series is Σaₙ. Always ask: are we listing, or are we adding?"

- question: "The expression Σᵢ₌₀⁵ i² has 5 terms because the index runs from 0 to 5."
  type: true-false
  answer: false
  explanation: "The index runs through the values 0, 1, 2, 3, 4, 5 — that is 6 terms, not 5. When the index runs from a to b inclusive, the number of terms is b - a + 1. Σᵢ₌₀⁵ has 5 - 0 + 1 = 6 terms. This off-by-one error is extremely common with sigma notation and propagates into incorrect partial sum calculations."

- question: "What is the difference between a sequence and a series, and why does that distinction matter for understanding infinite sums?"
  type: short-answer
  answer: "A sequence is an ordered list of numbers (e.g., 1, 1/2, 1/4, ...); a series is the sum of the terms of a sequence (e.g., 1 + 1/2 + 1/4 + ...). The distinction matters because adding infinitely many terms does not necessarily produce infinity — it depends on whether the partial sums converge. The partial sums of a series form their own sequence, and asking whether that sequence converges to a finite limit is the central question of series theory."
  explanation: "A sequence can decrease toward zero without the series converging — the harmonic series 1 + 1/2 + 1/3 + ... diverges even though the terms go to 0. A series converges when the partial sum sequence has a finite limit. Understanding that a series is a sequence of partial sums — not just an infinite list — is what makes calculus-level convergence analysis possible."
```

## Explainer

You already know **function notation**: f(n) assigns a value to each input n. A **sequence** is simply a function whose domain is the positive integers (or non-negative integers). Writing aₙ instead of f(n) is just a notational convenience — aₙ is the n-th term of the sequence. The sequence 2, 5, 8, 11, ... could be described by the explicit formula aₙ = 2 + 3(n − 1), or recursively by a₁ = 2 and aₙ = aₙ₋₁ + 3. Both descriptions define the same sequence; the explicit formula is faster for finding the 100th term, while the recursive formula better captures how each term is built from the previous one.

The two fundamental sequence types to recognize are **arithmetic** (constant difference) and **geometric** (constant ratio). In an arithmetic sequence, each term adds a fixed number d: aₙ = a₁ + (n − 1)d. In a geometric sequence, each term multiplies by a fixed number r: aₙ = a₁ · rⁿ⁻¹. Identifying which type you have is the first step in any problem — once you know the type, the formula for its partial sum follows directly. For arithmetic sequences, the sum of the first n terms is Sₙ = n/2 · (a₁ + aₙ), which you can visualize by pairing the first and last terms, the second and second-to-last, and so on — each pair sums to the same value. For geometric sequences, Sₙ = a₁(1 − rⁿ)/(1 − r), derived algebraically by writing S − rS and watching most terms cancel.

A **series** is the sum of sequence terms, and **sigma notation** is the compact language for writing such sums. The expression Σᵢ₌₁ⁿ aᵢ means "sum aᵢ for i from 1 to n." The index variable (i here) is a placeholder — it only exists inside the sum. Common errors come from off-by-one mistakes: Σᵢ₌₀ⁿ has n + 1 terms, not n. Reading sigma notation fluently requires practice expanding a few examples before trying to compress expressions.

This review matters because **calculus** will ask whether infinite series converge. The geometric series is the key test case: Σᵢ₌₀^∞ rⁿ = 1/(1 − r) when |r| < 1, but diverges when |r| ≥ 1. You can see this from the partial sum formula: as n → ∞, rⁿ → 0 if |r| < 1, so Sₙ → a₁/(1 − r). Everything you study in Calculus 2 about series convergence is a generalization of this one finite-to-infinite leap. Knowing the arithmetic and geometric formulas cold — and being comfortable with sigma notation — means you can focus on the new ideas of convergence rather than re-learning foundational mechanics at the worst possible moment.
