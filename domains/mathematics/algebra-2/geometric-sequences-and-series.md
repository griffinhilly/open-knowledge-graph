---
id: geometric-sequences-and-series
title: Geometric Sequences and Series
domain: mathematics
course: algebra-2
prerequisites:
- id: arithmetic-sequences-and-series
  type: soft
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- sigma-notation
- binomial-theorem
- series-definition-and-partial-sums
tags:
- sequences
- series
- geometric
- common-ratio
stage: formal-systems
status: validated
---
# Geometric Sequences and Series

## Core Idea
A geometric sequence has a constant ratio r between consecutive terms: a_n = a_1 * r^(n-1). The sum of the first n terms (geometric series) is S_n = a_1 * (1 - r^n)/(1 - r) for r != 1. If |r| < 1, the infinite geometric series converges to S = a_1/(1 - r). Geometric sequences model exponential growth and decay. The infinite series formula is foundational for calculus and finance.

## How It's Best Learned
Identify common ratios in sequences. Derive the finite sum formula by multiplying S_n by r and subtracting. Explore the infinite series by examining what happens as n grows when |r| < 1. Apply to compound interest, bouncing balls, and repeating decimals as infinite geometric series.

## Common Misconceptions
- Confusing common difference (arithmetic) with common ratio (geometric).
- Using the sum formula when r = 1 (division by zero; the sum is simply n*a_1).
- Applying the infinite series formula when |r| >= 1 (the series diverges).
- Sign errors in the sum formula when r is negative.

## Questions

```yaml
- question: "A student uses the infinite geometric series formula S = a₁/(1−r) on the series 2 + 4 + 8 + 16 + ... and gets S = 2/(1−2) = −2. What is the error?"
  type: multiple-choice
  options:
    - "The formula requires a₁ = 1; the student should divide everything by 2 first"
    - "The formula only applies when |r| < 1; this series has r = 2, so it diverges and has no finite sum"
    - "The formula gives a negative result because r > 1; the student should use S = a₁/(r−1) instead"
    - "The formula is correct; −2 is the Ramanujan sum of this series"
  answer: 1
  explanation: "The infinite series formula S = a₁/(1−r) is only valid when |r| < 1. Here r = 2 and |r| = 2 > 1, so the partial sums grow without bound — the series diverges. Plugging r = 2 into the formula gives −2, which is arithmetically valid but meaningless as a sum. The formula's derivation relies on r^n → 0 as n → ∞, which only occurs when |r| < 1. Students who forget this condition generate nonsensical 'answers' by blindly applying the formula."

- question: "The repeating decimal 0.272727... is an infinite geometric series. What is its exact fractional value?"
  type: multiple-choice
  options:
    - "3/11"
    - "27/100"
    - "272/999"
    - "3/10"
  answer: 0
  explanation: "0.272727... = 27/100 + 27/10000 + 27/1000000 + .... This is a geometric series with a₁ = 27/100 and r = 1/100. Since |r| = 0.01 < 1, the formula applies: S = (27/100)/(1 − 1/100) = (27/100)/(99/100) = 27/99 = 3/11. Verify: 3/11 = 0.272727..., confirming the formula gives the exact fractional equivalent of a repeating decimal. This technique works for any repeating decimal."

- question: "Nearly every infinite geometric series with a positive common ratio has a finite sum."
  type: true-false
  answer: false
  explanation: "Only geometric series with |r| < 1 have finite sums. If r ≥ 1, the terms do not shrink to zero — each term is at least as large as the previous one — and the partial sums grow without bound. For example, 1 + 2 + 4 + 8 + ... has r = 2 and diverges. Even r = 1 produces an infinite sum (1 + 1 + 1 + ... = ∞). A positive common ratio is no guarantee of convergence; the required condition is strictly |r| < 1."

- question: "A geometric sequence with r = −0.5 models exponential decay, because the terms decrease in magnitude with each step."
  type: true-false
  answer: true
  explanation: "A geometric sequence a_n = a₁·r^(n−1) is the discrete analogue of an exponential function, and r is the multiplicative factor at each step. For r = −0.5, the absolute value |r| = 0.5 < 1, so the terms shrink toward zero — this is exponential decay in magnitude. The terms also alternate in sign, so it's oscillating decay. The connection to exponential functions is genuine: the geometric sequence traces an exponential curve when plotted (with alternating sign). The key property of all geometric sequences — constant ratio between consecutive terms — is exactly the discrete version of constant multiplicative growth or decay."

- question: "Why does the infinite geometric series formula S = a₁/(1−r) only produce valid results when |r| < 1, and what happens when this condition fails?"
  type: short-answer
  answer: "The formula comes from taking the limit of S_n = a₁(1−r^n)/(1−r) as n → ∞. This limit only exists if r^n → 0, which requires |r| < 1. When |r| < 1, each term is a strictly smaller fraction of the previous one, so partial sums converge to a fixed value. When |r| ≥ 1, the terms don't shrink: if |r| > 1, partial sums grow without bound; if |r| = 1, every term has the same magnitude and sums grow linearly (or oscillate). The formula produces a finite number algebraically in these cases, but that number does not represent any ordinary sum."
  explanation: "Plugging r = 2 into the formula gives S = a₁/(1−2) = −a₁, a finite negative number — but the actual partial sums 2, 6, 14, 30, ... grow without bound. The formula's algebraic output is disconnected from the actual behavior of the series. This is why checking |r| < 1 before applying the formula is not optional — it's what determines whether the formula means anything at all."
```

## Explainer

You already understand exponential functions: y = a · r^x, where a is the starting value and r is the growth (or decay) factor applied repeatedly. A **geometric sequence** is the discrete version of exactly this idea. Instead of a continuous curve, you have a list: a₁, a₁r, a₁r², a₁r³, …. Each term is r times the previous one. The number r is the **common ratio** — the defining characteristic that makes a sequence geometric. To check whether a sequence is geometric, divide any term by the one before it: if you always get the same number, it is geometric.

The nth term formula a_n = a₁ · r^(n−1) follows directly from the exponential structure. Starting at a₁ (when n = 1, r⁰ = 1), each successive step multiplies by r. This connects to every exponential model you have seen: compound interest starts with a principal and multiplies by (1 + rate) each period; radioactive decay multiplies by a fraction each half-life; a bouncing ball reaches r times the previous height on each bounce. All of these are geometric sequences. Whether |r| > 1 (growth), 0 < |r| < 1 (decay), or r < 0 (alternating sign) determines the sequence's long-run behavior.

The **finite sum formula** S_n = a₁(1 − r^n)/(1 − r) is derived by an elegant algebraic trick. Write S_n = a₁ + a₁r + a₁r² + … + a₁r^(n−1). Multiply both sides by r: rS_n = a₁r + a₁r² + … + a₁r^n. Subtract: S_n − rS_n = a₁ − a₁r^n, so S_n(1 − r) = a₁(1 − r^n), giving the formula. This "multiply and subtract" technique is a foundational algebraic strategy that reappears in many contexts, including proving limits and summing other special series.

The **infinite series formula** S = a₁/(1 − r) for |r| < 1 emerges from taking the limit as n → ∞. When |r| < 1, the term r^n shrinks toward zero, so the factor (1 − r^n) in the numerator approaches 1, leaving a₁/(1 − r). The series converges because each additional term contributes a shrinking fraction of the last, and the cumulative total is bounded. A striking application: the repeating decimal 0.333… = 3/10 + 3/100 + 3/1000 + … is an infinite geometric series with a₁ = 3/10 and r = 1/10. The formula gives S = (3/10)/(1 − 1/10) = (3/10)/(9/10) = 1/3 exactly — confirming that 0.333… and 1/3 are the same number.
