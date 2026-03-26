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

## Questions

```yaml
- question: "What is lim(x→∞) (4x² + 3x) / (2x² − 5)?"
  type: multiple-choice
  options:
    - "∞, because the numerator grows without bound as x increases"
    - "2, because the ratio of the leading coefficients is 4/2"
    - "0, because the denominator eventually dominates any numerator"
    - "3/(-5) = −3/5, from the ratio of the non-leading constant terms"
  answer: 1
  explanation: "Dividing numerator and denominator by x² gives (4 + 3/x) / (2 − 5/x²). As x→∞, both 3/x and 5/x² vanish to 0, leaving 4/2 = 2. The degree-comparison shortcut: when numerator and denominator have equal degree, the limit at infinity equals the ratio of leading coefficients. Option A is wrong because although the numerator grows, so does the denominator at the same rate. Option D substitutes constants as if x=0, which is invalid."

- question: "A student says: 'lim(x→∞) f(x) = ∞ and lim(x→0⁺) g(x) = ∞ both involve infinity, so they describe the same type of behavior.' What error is the student making?"
  type: multiple-choice
  options:
    - "No error — both expressions describe a function growing without bound, which is the same phenomenon"
    - "They are confusing a limit at infinity (end behavior as x → ∞) with an infinite limit at a finite point (a vertical asymptote near x = 0)"
    - "They are confusing horizontal asymptotes with limits that fail to exist"
    - "They are treating ∞ as a real number that can be substituted into functions"
  answer: 1
  explanation: "These are fundamentally different phenomena. lim(x→∞) f(x) = ∞ means f grows without bound as x runs to infinity — this describes end behavior along the x-axis, and y = ∞ is not a horizontal asymptote (the function has none). lim(x→0⁺) g(x) = ∞ describes a vertical asymptote near x = 0 — f blows up as you approach a specific finite x-value. The notation looks similar, but the geometric meaning and analysis techniques are entirely different."

- question: "Most rational function has exactly one horizontal asymptote."
  type: true-false
  answer: false
  explanation: "A rational function has a horizontal asymptote only when the degree of the numerator is less than or equal to the degree of the denominator. If the numerator has higher degree, the function grows without bound — no horizontal asymptote. Furthermore, non-rational functions like f(x) = x / √(x² + 1) can have two different horizontal asymptotes (y = 1 as x → +∞ and y = −1 as x → −∞), because √(x²) = |x| behaves differently in the two directions."

- question: "A function can cross its horizontal asymptote for some finite value of x, even though the asymptote describes the function's behavior only as x → ∞."
  type: true-false
  answer: true
  explanation: "A horizontal asymptote describes limit behavior — what the function approaches far out along the x-axis. It says nothing about what happens at finite x. For example, f(x) = sin(x)/x has a horizontal asymptote y = 0 as x → ±∞, but it crosses y = 0 infinitely many times at every x = nπ. This is a common misconception: asymptotes describe end behavior, not a boundary the function can never reach."

- question: "Explain why lim(x→∞) (3x² + 1) / (x² − 5) = 3 rather than ∞/∞, and describe the technique that makes this clear."
  type: short-answer
  answer: "Substituting ∞ directly would give the indeterminate form ∞/∞, which is undefined. The standard technique is to divide every term in the numerator and denominator by the highest power of x in the denominator — here, x². This gives (3 + 1/x²) / (1 − 5/x²). As x → ∞, both 1/x² and 5/x² approach 0, leaving 3/1 = 3. The technique works because it converts a ratio of growing polynomials into a ratio of terms with known limits."
  explanation: "The key insight is that infinity cannot be substituted as a number — doing so produces ∞/∞, which is indeterminate, not a ratio. Dividing by x² first reveals the true limiting behavior by isolating the leading terms. This same 'divide by highest power' strategy applies to all rational functions and extends to functions with radicals, where the technique requires care about the sign of √(x²) = |x|."
```

## Explainer

A **limit at infinity** asks: what value does f(x) settle toward as x grows without bound? You already have informal intuition for this from studying rational functions and asymptotes. Calculus formalizes that intuition with limit notation: writing lim(x→∞) f(x) = L means that f(x) gets arbitrarily close to L for all sufficiently large x. The line y = L is then a **horizontal asymptote** — the function approaches it as a target but may never touch it (though it can cross a horizontal asymptote for finite x).

The core technique for rational functions is **dividing by the highest power of x** in the denominator. Consider (3x² + 5x) / (x² − 2). Dividing every term top and bottom by x² gives (3 + 5/x) / (1 − 2/x²). Now apply the fundamental fact your limit laws guarantee: for any positive power n, lim(x→∞) 1/xⁿ = 0. As x → ∞, the terms 5/x and 2/x² vanish, leaving 3/1 = 3. The **degree comparison shortcut** follows directly: if the numerator and denominator have the same degree, the limit is the ratio of leading coefficients. If the numerator has lower degree, the limit is 0. If the numerator has higher degree, the function grows without bound (no horizontal asymptote).

For functions involving square roots or other radicals, the same "divide by highest power" idea applies, but you must be careful: √(x²) = |x|, which equals x when x > 0 but −x when x < 0. This is why lim(x→+∞) and lim(x→−∞) can give different horizontal asymptotes. For example, f(x) = x / √(x² + 1) has limit 1 as x → +∞ and limit −1 as x → −∞ — two different horizontal asymptotes.

It is worth distinguishing clearly between the two types of limit involving infinity. A **limit at infinity** — lim(x→∞) f(x) = L — describes end behavior: what happens far out along the x-axis. An **infinite limit** — lim(x→a) f(x) = ∞ — describes a vertical asymptote: what happens near a specific x-value where the function blows up. These are entirely different phenomena with different geometric meaning, and confusing them is the single most common error when infinity appears in limit notation.
