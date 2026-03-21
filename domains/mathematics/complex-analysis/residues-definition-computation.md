---
id: residues-definition-computation
title: 'Residues: Definition and Computation'
domain: mathematics
course: complex-analysis
prerequisites:
- id: singularities-classification
  type: hard
- id: laurent-series
  type: soft
builds-toward:
- residue-theorem
- argument-principle
tags:
- residues
- laurent-coefficient
- computation
stage: advanced
status: draft
---

# Residues: Definition and Computation

## Core Idea
The residue of f at an isolated singularity z₀ is Res(f, z₀) = a₋₁, the coefficient of 1/(z - z₀) in the Laurent expansion. For a simple pole, Res(f, z₀) = lim_(z→z₀) (z - z₀)f(z). For a pole of order m, use Res(f, z₀) = (1/(m-1)!) d^(m-1)/dz^(m-1) [(z - z₀)^m f(z)] at z₀. Residues measure the strength of circulation around singularities.

## How It's Best Learned
Compute residues for f(z) = 1/(z(z-1)) at both z = 0 and z = 1 using the formulas. Verify by finding the Laurent series and extracting a₋₁.

## Common Misconceptions
Thinking residues are complicated to compute; there are simple formulas for simple and multiple poles. Assuming the residue formula applies to essential singularities; it doesn't — you must find the Laurent series.

## Questions

```yaml
- question: "Among all the Laurent coefficients ..., a₋₂, a₋₁, a₀, a₁, ... of a function near an isolated singularity, only a₋₁ is called the 'residue' and given special treatment. Why is this coefficient uniquely important?"
  type: multiple-choice
  options:
    - "It is always the largest coefficient in absolute value, so it dominates the behavior near the singularity"
    - "It is the only Laurent coefficient that is nonzero for poles — the others vanish for meromorphic functions"
    - "It is the only term in the Laurent series whose contour integral around the singularity is nonzero"
    - "It determines the order of the pole — a pole of order m has a₋₁ ≠ 0 but a₋m = 0"
  answer: 2
  explanation: "The key fact is that ∮ (z − z₀)ⁿ dz = 0 for every integer n ≠ −1 (because (z−z₀)ⁿ has an antiderivative), but ∮ 1/(z−z₀) dz = 2πi. So when you integrate the Laurent series term by term, every term except the n = −1 term vanishes. The contour integral of f picks out exactly 2πi · a₋₁ — the residue is the piece of f that survives integration. This is why it deserves a special name: it is the 'residue' left after all other terms integrate to zero."

- question: "What is Res(f, 2) for f(z) = 1 / ((z − 2)(z + 3))?"
  type: multiple-choice
  options:
    - "−1/5, because the formula gives 1/(2 + 3) with a sign error from the factored form"
    - "1/5, because lim_{z→2} (z − 2) · f(z) = lim_{z→2} 1/(z + 3) = 1/5"
    - "1/2, because the residue at a simple pole is the reciprocal of the value at the pole"
    - "The residue is undefined because the formula for simple poles only applies when the denominator has a simple zero"
  answer: 1
  explanation: "z = 2 is a simple pole (the denominator has a simple zero there). Applying the simple-pole formula: Res(f, 2) = lim_{z→2} (z − 2) · 1/((z − 2)(z + 3)) = lim_{z→2} 1/(z + 3) = 1/5. Option A gets the arithmetic right but invents a sign error. Option C confuses the residue formula with the 1/f'(z₀) formula that applies when f = g/h with h(z₀) = 0 and g(z₀) ≠ 0 (which gives the same answer here: g(2)/h'(2) = 1/(2·2+1) = 1/5, consistent). Option D is wrong — the formula applies here."

- question: "For a pole of order 2 at z₀, you can compute the residue without finding the full Laurent series by multiplying f(z) by (z − z₀)², differentiating once with respect to z, and then evaluating at z₀."
  type: true-false
  answer: true
  explanation: "This is the order-m residue formula with m = 2: Res(f, z₀) = (1/(2−1)!) · d/dz [(z−z₀)² f(z)] evaluated at z₀. Multiplying by (z−z₀)² clears the double pole, giving a function that is analytic near z₀. Differentiating once (and dividing by (m−1)! = 1! = 1) extracts the a₋₁ coefficient directly. This avoids computing the full Laurent expansion — you only need the leading behavior of the product near z₀."

- question: "For an essential singularity, the shortcut formula Res(f, z₀) = lim_{z→z₀} (z − z₀) f(z) still gives the correct a₋₁ coefficient, though the limit may be harder to evaluate than for a simple pole."
  type: true-false
  answer: false
  explanation: "This shortcut only works for simple poles. For an essential singularity, the Laurent series has infinitely many negative-power terms, and no finite power of (z − z₀) can clear all of them. The limit lim_{z→z₀} (z − z₀) f(z) does not isolate a₋₁ — near an essential singularity, f(z) oscillates wildly (by the Casorati-Weierstrass theorem), and this limit typically does not exist or gives zero, not a₋₁. For essential singularities, you must compute enough terms of the actual Laurent expansion to identify a₋₁ directly."

- question: "Why does the coefficient a₋₁ in the Laurent expansion deserve the special name 'residue,' and why is it uniquely important compared to all other Laurent coefficients?"
  type: short-answer
  answer: "The residue is the only Laurent coefficient that survives contour integration. When you integrate f(z) = Σ aₙ(z − z₀)ⁿ term by term around a small circle enclosing z₀, every term with n ≠ −1 integrates to zero (because (z − z₀)ⁿ has an antiderivative for n ≠ −1). Only the n = −1 term contributes: ∮ a₋₁/(z − z₀) dz = 2πi · a₋₁. So ∮_γ f(z) dz = 2πi · Res(f, z₀). The residue is literally what 'remains' — the residue — after all other terms cancel. This is why the residue theorem, which sums residues to evaluate contour integrals, is so powerful."
  explanation: "The naming is exact: residue comes from 'what remains.' All other Laurent terms integrate to zero, leaving behind only the a₋₁ contribution. This single number encodes everything about how f behaves under integration around the singularity, which is why residues are the computational workhorse of complex analysis."
```

## Explainer

From your study of singularities and Laurent series, you know that near an isolated singularity z₀, a function can be expanded as a Laurent series: f(z) = … + a₋₂/(z−z₀)² + a₋₁/(z−z₀) + a₀ + a₁(z−z₀) + … The **residue** of f at z₀ is defined as a₋₁, the coefficient of the 1/(z−z₀) term. At first this looks like just one number among many in the expansion — why does it deserve special attention?

The answer lies in integration. When you integrate a Laurent series term by term around a small circle enclosing z₀, almost every term integrates to zero: ∮ (z−z₀)ⁿ dz = 0 for n ≠ −1, because (z−z₀)ⁿ has an antiderivative. But the n = −1 term is different: ∮ 1/(z−z₀) dz = 2πi (this is the fundamental residue computation you verified when studying Laurent series). So ∮_γ f(z) dz = 2πi · a₋₁ = 2πi · Res(f, z₀). The residue is exactly the piece of the Laurent expansion that survives integration. Everything else cancels.

For computation, you rarely need to find the full Laurent series. If z₀ is a **simple pole** (order 1), the formula Res(f, z₀) = lim_{z→z₀} (z−z₀)f(z) extracts just a₋₁ by canceling the pole. For f(z) = 1/(z(z−1)), at z = 0: lim_{z→0} z · (1/(z(z−1))) = lim_{z→0} 1/(z−1) = −1. At z = 1: lim_{z→1} (z−1) · (1/(z(z−1))) = lim_{z→1} 1/z = 1. For a **pole of order m**, the formula involves differentiating m−1 times after multiplying by (z−z₀)^m to clear the pole, then evaluating at z₀ and dividing by (m−1)!. This is the repeated differentiation you know from power series manipulation.

For **essential singularities** — where infinitely many negative-power terms appear — none of these shortcuts apply. The Laurent series is truly infinite in the negative direction and cannot be cleared by multiplying by a finite power. You must find enough terms of the Laurent expansion to identify a₋₁ directly. The residue is still well-defined (it is still a₋₁), but the computation is harder. The key skill is recognizing which type of singularity you have before choosing your computational strategy.
