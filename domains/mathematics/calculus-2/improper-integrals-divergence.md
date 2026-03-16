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

## Explainer

From your work on convergence, you know how to evaluate improper integrals directly: replace the infinite limit with a parameter, integrate, then take the limit. But many integrands — e^(−x²), 1/(x⁴ + x + 1), sin(x)/x as x → ∞ — have no elementary antiderivative. You cannot evaluate them directly. Comparison tests let you answer "does this converge or diverge?" without ever finding an antiderivative.

The logic mirrors basic reasoning about size. If 0 ≤ f(x) ≤ g(x) and you pour a finite amount of "area" under g, the area under f must also be finite — it's smaller. Conversely, if the area under f is already infinite, then the larger g must also be infinite. The **Direct Comparison Test** formalizes this: for 0 ≤ f(x) ≤ g(x) on [a, ∞), if ∫g converges then ∫f converges; if ∫f diverges then ∫g diverges. Note the two *invalid* directions: bounding f *above* by a divergent function, or f *below* by a convergent function, tells you nothing — the comparison runs the wrong way.

Applying the test requires a **library of benchmarks** you know by heart. The most important: ∫₁^∞ (1/xᵖ) dx converges if and only if p > 1. So 1/x² converges, 1/x diverges, 1/x^(1/2) diverges. For example, to show ∫₁^∞ 1/(x³ + x) converges: note 0 ≤ 1/(x³ + x) ≤ 1/x³ for x ≥ 1 (the denominator is larger with the extra +x), and ∫₁^∞ 1/x³ converges (p = 3 > 1). Done.

When bounding directly is awkward, the **Limit Comparison Test** is more flexible. If lim_{x→∞} f(x)/g(x) = L where 0 < L < ∞, then ∫f and ∫g share the same convergence behavior. The intuition: if f and g are asymptotically proportional (same order of magnitude), their integrals must both be finite or both be infinite. For ∫₁^∞ 1/(x² + √x) dx, compare to 1/x²: the limit (1/(x² + √x))/(1/x²) = x²/(x² + √x) → 1. Since ∫1/x² converges, so does the original. The skill is choosing the benchmark — typically formed by keeping only the *dominant* terms in the numerator and denominator and discarding lower-order ones.
