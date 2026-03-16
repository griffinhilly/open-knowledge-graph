---
id: limits-at-infinity
title: Limits at Infinity
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-laws
    type: hard
  - id: rational-functions-asymptotes-review
    type: hard
builds-toward:
  - lhopitals-rule
  - improper-integrals-convergence
tags: [limits, infinity, horizontal-asymptotes, end-behavior]
stage: formal-systems
status: validated
---

# Limits at Infinity

## Core Idea
A limit at infinity describes the behavior of f(x) as x grows without bound (x -> infinity or x -> -infinity). If lim(x->infinity) f(x) = L, the line y = L is a horizontal asymptote. For rational functions, the limit at infinity is determined by comparing the degrees of numerator and denominator. Limits at infinity formalize the concept of end behavior from precalculus and are essential for analyzing convergence.

## How It's Best Learned
Start with rational functions: divide numerator and denominator by the highest power of x. Then extend to functions involving radicals, exponentials, and logarithms. Use the principle that 1/x^n -> 0 as x -> infinity. Graph functions to verify algebraic results.

## Common Misconceptions
- Treating infinity as a number that can be substituted.
- Believing all functions have horizontal asymptotes (exponentials and polynomials do not).
- Confusing limits at infinity (end behavior) with infinite limits (vertical asymptotes).

## Explainer

A **limit at infinity** asks: what value does f(x) settle toward as x grows without bound? You already have informal intuition for this from studying rational functions and asymptotes. Calculus formalizes that intuition with limit notation: writing lim(x→∞) f(x) = L means that f(x) gets arbitrarily close to L for all sufficiently large x. The line y = L is then a **horizontal asymptote** — the function approaches it as a target but may never touch it (though it can cross a horizontal asymptote for finite x).

The core technique for rational functions is **dividing by the highest power of x** in the denominator. Consider (3x² + 5x) / (x² − 2). Dividing every term top and bottom by x² gives (3 + 5/x) / (1 − 2/x²). Now apply the fundamental fact your limit laws guarantee: for any positive power n, lim(x→∞) 1/xⁿ = 0. As x → ∞, the terms 5/x and 2/x² vanish, leaving 3/1 = 3. The **degree comparison shortcut** follows directly: if the numerator and denominator have the same degree, the limit is the ratio of leading coefficients. If the numerator has lower degree, the limit is 0. If the numerator has higher degree, the function grows without bound (no horizontal asymptote).

For functions involving square roots or other radicals, the same "divide by highest power" idea applies, but you must be careful: √(x²) = |x|, which equals x when x > 0 but −x when x < 0. This is why lim(x→+∞) and lim(x→−∞) can give different horizontal asymptotes. For example, f(x) = x / √(x² + 1) has limit 1 as x → +∞ and limit −1 as x → −∞ — two different horizontal asymptotes.

It is worth distinguishing clearly between the two types of limit involving infinity. A **limit at infinity** — lim(x→∞) f(x) = L — describes end behavior: what happens far out along the x-axis. An **infinite limit** — lim(x→a) f(x) = ∞ — describes a vertical asymptote: what happens near a specific x-value where the function blows up. These are entirely different phenomena with different geometric meaning, and confusing them is the single most common error when infinity appears in limit notation.
