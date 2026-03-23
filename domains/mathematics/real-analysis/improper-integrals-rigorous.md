---
id: improper-integrals-rigorous
title: Improper Integrals (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-properties
  type: hard
- id: series-convergence-rigorous
  type: soft
tags:
- improper-integrals
- convergence
- unbounded
stage: advanced
status: validated
---

# Improper Integrals (Rigorous)

## Core Idea
An improper integral extends the Riemann integral to unbounded intervals or unbounded integrands by taking limits. For infinite intervals, ∫ₐ^∞ f(x) dx = lim_{t→∞} ∫ₐᵗ f(x) dx; for unbounded integrands near a point c, ∫ₐᵇ f(x) dx = lim_{ε→0⁺} ∫ₐ^{c−ε} f(x) dx + lim_{ε→0⁺} ∫_{c+ε}ᵇ f(x) dx. The integral converges if these limits exist and are finite. Convergence criteria mirror those for series: comparison tests, limit comparison, and absolute convergence all apply. An integral can converge conditionally (like ∫₁^∞ sin(x)/x dx) without converging absolutely. These integrals arise naturally in probability, Fourier analysis, and Laplace transforms.

## How It's Best Learned
Work through the classic examples: ∫₁^∞ 1/xᵖ dx (converges iff p > 1), then ∫₀¹ 1/xᵖ dx (converges iff p < 1). These two cases build the intuition that convergence depends on how fast the integrand decays or blows up relative to the interval.

## Common Misconceptions
Students sometimes evaluate improper integrals by plugging in ∞ directly, skipping the limit process. This can produce correct-looking answers but obscures conditional convergence issues. Also, the two limits in a doubly improper integral must be taken independently—they cannot be combined into a single symmetric limit.

## Explainer

The Riemann integral ∫ₐᵇ f(x) dx, as you studied it, requires both a finite interval [a, b] and a bounded integrand f. **Improper integrals** extend this framework to two situations where these conditions fail: integrating over an infinite interval (like ∫₁^∞ 1/x² dx) or integrating a function with an unbounded singularity (like ∫₀¹ 1/√x dx). In both cases, the extension is made through limits — you compute a proper Riemann integral on a truncated domain and then take a limit as the domain grows to its full extent.

For integrals over infinite intervals, the definition is ∫ₐ^∞ f(x) dx = lim_{t→∞} ∫ₐᵗ f(x) dx. The integral **converges** if this limit exists and is finite; otherwise it **diverges**. The classic reference is ∫₁^∞ 1/xᵖ dx, which converges if and only if p > 1. When p = 2, the antiderivative is −1/x, and the limit gives ∫₁^∞ 1/x² dx = lim_{t→∞} (1 − 1/t) = 1. When p = 1, the antiderivative is ln(x), and lim_{t→∞} ln(t) = ∞, so the integral diverges. For integrals with singularities, a similar limit handles the blow-up: ∫₀¹ 1/xᵖ dx = lim_{ε→0⁺} ∫_ε¹ 1/xᵖ dx, which converges if and only if p < 1. The two conditions (p > 1 for infinity, p < 1 for zero) are complementary, reflecting the different nature of the two problems.

A critical subtlety arises with **doubly improper** integrals like ∫₋∞^∞ f(x) dx. The definition requires two independent limits: ∫₋∞^∞ f(x) dx = lim_{s→−∞} ∫_s⁰ f(x) dx + lim_{t→∞} ∫₀ᵗ f(x) dx. Both limits must exist independently. The symmetric limit lim_{T→∞} ∫₋ᵀᵀ f(x) dx — called the **Cauchy principal value** — is a weaker notion that can give a finite answer even when the integral diverges. For f(x) = x, the principal value is 0 (by symmetry), but ∫₀^∞ x dx = ∞, so the integral diverges. Conflating the principal value with the integral is a common and serious error.

The convergence theory for improper integrals closely parallels that of infinite series. **Comparison tests** work the same way: if 0 ≤ f(x) ≤ g(x) and ∫ g converges, then ∫ f converges. **Absolute convergence** (convergence of ∫ |f(x)| dx) implies convergence, but the converse fails — ∫₁^∞ sin(x)/x dx converges conditionally, meaning the oscillating cancellation produces a finite value even though ∫₁^∞ |sin(x)/x| dx diverges. This parallel is not a coincidence: both series and improper integrals are limits of accumulating quantities, and the same structural issues — decay rates, cancellation, comparison — govern convergence in both settings.

## Questions

```yaml
- question: "A student evaluates ∫₋∞^∞ x dx by noting that ∫₋ᵀ^ᵀ x dx = 0 for any T, and concludes the answer is 0. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the integral equals 0 by the symmetry of an odd function"
    - "The definition requires lim_{s→−∞} and lim_{t→+∞} of ∫ₛᵗ x dx taken independently; since neither limit exists finitely, the integral diverges"
    - "The student should verify using the substitution u = −x before concluding"
    - "The integral converges, but the value is indeterminate rather than 0"
  answer: 1
  explanation: "Taking the symmetric limit lim_{T→∞} ∫₋ᵀ^ᵀ x dx = 0 computes the Cauchy principal value, which is a weaker notion than convergence. The proper definition requires two independent limits: lim_{s→−∞} and lim_{t→+∞} of ∫ₛᵗ x dx. Since ∫₀ᵗ x dx = t²/2 → ∞, the integral toward +∞ alone diverges. The integral ∫₋∞^∞ x dx is divergent; the symmetric computation masks this by exploiting cancellation that the definition does not permit."

- question: "∫₁^∞ 1/xᵖ dx converges for p > 1, and ∫₀¹ 1/xᵖ dx converges for p < 1. A student claims these are contradictory — the same function 1/xᵖ cannot converge in opposite conditions. What is the correct response?"
  type: multiple-choice
  options:
    - "The student is right — both integrals actually share the same convergence condition"
    - "The conditions are complementary: the first probes decay at infinity, the second probes blow-up near 0; each has its own convergence requirement"
    - "The student is correct that only p between 0 and 1 makes both integrals converge simultaneously"
    - "The formulas apply only to integer values of p, so the comparison is invalid"
  answer: 1
  explanation: "The two integrals ask different questions. ∫₁^∞ 1/xᵖ dx asks whether 1/xᵖ decays fast enough at infinity — it does when p > 1. ∫₀¹ 1/xᵖ dx asks whether the blow-up near x = 0 is integrable — it is when p < 1 (so the singularity is mild enough). These are independent conditions about different behaviors of the same function. Working through both cases is the standard way to build intuition for improper integral convergence."

- question: "The improper integral ∫₁^∞ sin(x)/x dx diverges because the integrand does not approach 0 fast enough."
  type: true-false
  answer: false
  explanation: "This integral converges — it is the classic example of conditional convergence. sin(x)/x oscillates with decreasing amplitude and does approach 0, and the alternating cancellation makes the integral converge despite the fact that ∫₁^∞ |sin(x)/x| dx diverges. Conditional convergence is real: an improper integral can converge without converging absolutely, just as an alternating series can converge while the series of absolute values diverges."

- question: "The two limits in ∫₋∞^∞ f(x) dx must be taken independently; combining them into the symmetric limit lim_{T→∞} ∫₋ᵀ^ᵀ f(x) dx gives the Cauchy principal value, which may differ from the true integral value."
  type: true-false
  answer: true
  explanation: "This is precisely the subtlety the definition is designed to capture. The Cauchy principal value exploits symmetric cancellation that may not persist when the limits are taken independently. For odd functions like f(x) = x, the principal value is 0 but the integral diverges. For integrals that converge by the proper definition, the principal value agrees — but the definition must come first."

- question: "Explain why defining ∫ₐ^∞ f(x) dx as lim_{t→∞} ∫ₐᵗ f(x) dx, rather than 'plugging in ∞,' is necessary rather than a mere formality."
  type: short-answer
  answer: "Because ∞ is not a number and cannot be substituted. The limit formulation is essential for detecting when the integral diverges, for identifying conditional convergence, and for correctly handling doubly improper integrals by keeping the two independent limits separate. Without the limit framework, symmetric cancellation can make a divergent integral appear to have a finite value — the Cauchy principal value — which is a different and weaker notion than genuine convergence."
  explanation: "The limit definition is not bureaucratic precision for its own sake. It provides the only rigorous way to determine whether a definite value exists, and it exposes the difference between absolute and conditional convergence. Skipping the limit process and 'plugging in ∞' works for simple cases but breaks down on examples like ∫₋∞^∞ x dx, where the naive answer of 0 conceals a divergent integral."
```

