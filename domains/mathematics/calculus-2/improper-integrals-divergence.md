---
id: improper-integrals-divergence
title: Improper Integrals - Divergence and Comparison
domain: mathematics
course: calculus-2
prerequisites:
  - id: improper-integrals-convergence
    type: hard
builds-toward:
  - comparison-test
tags: [integration, improper, divergence, comparison]
stage: formal-systems
status: validated
---

# Improper Integrals - Divergence and Comparison

## Core Idea
When an improper integral cannot be evaluated directly (no closed-form antiderivative), comparison tests determine convergence or divergence without computing the integral. The Direct Comparison Test says: if 0 <= f(x) <= g(x) and the integral of g converges, then the integral of f converges; if the integral of f diverges, so does the integral of g. The Limit Comparison Test uses lim f(x)/g(x) to draw the same conclusions more flexibly.

## How It's Best Learned
Build a library of known benchmarks (p-integrals, exponential decay). Practice bounding unfamiliar integrands above or below by known ones. Use the Limit Comparison Test when direct comparison is difficult. Emphasize that comparison only works for non-negative functions.

## Common Misconceptions
- Comparing in the wrong direction (bounding a convergent integral above by a divergent one proves nothing).
- Forgetting that comparison tests require non-negative integrands.
- Confusing the comparison test for integrals with the comparison test for series (same logic, different context).

## Questions

```yaml
- question: "For x ≥ 1, suppose 0 ≤ f(x) ≤ g(x) and ∫₁^∞ g(x) dx diverges. What does the Direct Comparison Test allow you to conclude about ∫₁^∞ f(x) dx?"
  type: multiple-choice
  options:
    - "It diverges, because f is bounded above by a divergent function"
    - "It converges, because f ≤ g and g blows up, so f must stay finite"
    - "Nothing can be concluded — a divergent upper bound gives no information about the smaller function"
    - "It diverges if and only if lim_{x→∞} f(x)/g(x) > 0"
  answer: 2
  explanation: "This is the most common error in applying comparison tests. Being bounded *above* by a divergent function tells you nothing — the smaller function could converge or diverge. For example, 1/x² ≤ 1/x on [1,∞), and ∫1/x diverges, yet ∫1/x² converges (p = 2 > 1). Divergence propagates *upward*: if the smaller f diverges, the larger g must also diverge. Convergence propagates *downward*: if the larger g converges, the smaller f must converge. The two invalid directions are: divergent upper bound and convergent lower bound."

- question: "You apply the Limit Comparison Test to ∫₁^∞ 1/(x⁴ + x + 1) dx using benchmark 1/x⁴. You compute lim_{x→∞} [1/(x⁴+x+1)] / [1/x⁴] = lim x⁴/(x⁴+x+1) = 1. What do you conclude?"
  type: multiple-choice
  options:
    - "Nothing; the limit equals 1 which is not strictly greater than zero so the test fails"
    - "The integral converges, since the limit is a finite positive number and ∫₁^∞ 1/x⁴ dx converges (p = 4 > 1)"
    - "The integral diverges, because 1/(x⁴+x+1) < 1/x⁴ for all x ≥ 1"
    - "The test is inconclusive; you must use direct comparison with a larger function instead"
  answer: 1
  explanation: "The Limit Comparison Test says: if lim f/g = L where 0 < L < ∞, then ∫f and ∫g share the same convergence behavior. Here L = 1, which is finite and positive, so the two integrals behave identically at infinity. Since ∫1/x⁴ converges (p-integral with p = 4 > 1), the original integral converges. The technique is to identify the dominant term in the denominator — here x⁴ — and use 1/x⁴ as the benchmark; the lower-order x + 1 terms become negligible as x → ∞."

- question: "If 0 ≤ f(x) ≤ g(x) on [1,∞) and ∫₁^∞ g(x) dx diverges, then ∫₁^∞ f(x) dx should also diverge."
  type: true-false
  answer: false
  explanation: "This reverses the valid direction of the test. The Direct Comparison Test transmits convergence downward (if the larger g converges, the smaller f must converge) and divergence upward (if the smaller f diverges, the larger g must diverge). A divergent upper bound proves nothing about the smaller function. Counterexample: 1/x² ≤ 1/x on [1,∞); ∫1/x diverges, yet ∫1/x² converges (p = 2 > 1)."

- question: "The Direct Comparison Test requires both functions to be non-negative on the interval of integration."
  type: true-false
  answer: true
  explanation: "The test's reasoning rests on area inequalities: if 0 ≤ f(x) ≤ g(x), the 'area' under f cannot exceed the 'area' under g. If either function takes negative values, this area ordering breaks down — a function with negative parts can have a smaller integral than a positive function without any meaningful size relationship. Non-negativity is not a technicality; it is what makes the bounding argument valid."

- question: "Why is choosing the right benchmark the key practical skill when applying comparison tests to improper integrals?"
  type: short-answer
  answer: "The benchmark must be a function with known convergence behavior whose magnitude is comparable to the integrand at infinity. For rational-like expressions, keep only the dominant terms and discard lower-order ones. A benchmark too different in magnitude will not yield a valid comparison; one with the same asymptotic order allows both direct and limit comparison. The most useful benchmarks are p-integrals (∫ 1/xᵖ, converges iff p > 1) and exponential decay functions."
  explanation: "The comparison test itself is mechanical once a benchmark is chosen, but the choice requires recognizing how the integrand behaves as x → ∞. For 1/(x³ + x²), the dominant term is 1/x³. For e^{-x²}, no power function works; use e^{-x} instead. Building a library of known-convergence benchmarks and recognizing which class a given integrand belongs to is the entire art of the technique."
```

## Explainer

From your work on convergence, you know how to evaluate improper integrals directly: replace the infinite limit with a parameter, integrate, then take the limit. But many integrands — e^(−x²), 1/(x⁴ + x + 1), sin(x)/x as x → ∞ — have no elementary antiderivative. You cannot evaluate them directly. Comparison tests let you answer "does this converge or diverge?" without ever finding an antiderivative.

The logic mirrors basic reasoning about size. If 0 ≤ f(x) ≤ g(x) and you pour a finite amount of "area" under g, the area under f must also be finite — it's smaller. Conversely, if the area under f is already infinite, then the larger g must also be infinite. The **Direct Comparison Test** formalizes this: for 0 ≤ f(x) ≤ g(x) on [a, ∞), if ∫g converges then ∫f converges; if ∫f diverges then ∫g diverges. Note the two *invalid* directions: bounding f *above* by a divergent function, or f *below* by a convergent function, tells you nothing — the comparison runs the wrong way.

Applying the test requires a **library of benchmarks** you know by heart. The most important: ∫₁^∞ (1/xᵖ) dx converges if and only if p > 1. So 1/x² converges, 1/x diverges, 1/x^(1/2) diverges. For example, to show ∫₁^∞ 1/(x³ + x) converges: note 0 ≤ 1/(x³ + x) ≤ 1/x³ for x ≥ 1 (the denominator is larger with the extra +x), and ∫₁^∞ 1/x³ converges (p = 3 > 1). Done.

When bounding directly is awkward, the **Limit Comparison Test** is more flexible. If lim_{x→∞} f(x)/g(x) = L where 0 < L < ∞, then ∫f and ∫g share the same convergence behavior. The intuition: if f and g are asymptotically proportional (same order of magnitude), their integrals must both be finite or both be infinite. For ∫₁^∞ 1/(x² + √x) dx, compare to 1/x²: the limit (1/(x² + √x))/(1/x²) = x²/(x² + √x) → 1. Since ∫1/x² converges, so does the original. The skill is choosing the benchmark — typically formed by keeping only the *dominant* terms in the numerator and denominator and discarding lower-order ones.
