---
id: rolles-theorem
title: "Rolle's Theorem"
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
  - id: derivative-as-slope-of-tangent
    type: hard
builds-toward:
  - mean-value-theorem
tags: [theorems, Rolle, existence-theorems]
stage: formal-systems
status: validated
---

# Rolle's Theorem

## Core Idea
Rolle's Theorem is a special case of the Mean Value Theorem: if f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists at least one c in (a, b) where f'(c) = 0. Geometrically, if a smooth curve starts and ends at the same height, it must have at least one horizontal tangent in between. Rolle's Theorem is the stepping stone to proving the full MVT.

## How It's Best Learned
Visualize: draw curves that start and end at the same height and find where the tangent is horizontal. Verify with specific polynomial examples. Emphasize the three hypotheses and what can go wrong if any is violated.

## Common Misconceptions
- Applying Rolle's Theorem when f(a) does not equal f(b).
- Forgetting to check differentiability (|x| satisfies continuity and f(-1) = f(1) but has no horizontal tangent).
- Assuming the c given by Rolle's Theorem must be unique.

## Questions

```yaml
- question: "Consider f(x) = |x| on [-1, 1]. We have f(-1) = f(1) = 1 and f is continuous on [-1, 1]. Can Rolle's Theorem be applied to guarantee a point where f'(c) = 0?"
  type: multiple-choice
  options:
    - "Yes — all three hypotheses are satisfied, so Rolle's Theorem applies"
    - "No — Rolle's Theorem requires f(a) = f(b) = 0, but here f(-1) = f(1) = 1"
    - "No — f is not differentiable at x = 0, so the differentiability hypothesis fails"
    - "Yes — but since |x| has no local max or min in (-1,1), the theorem's conclusion fails, disproving the theorem"
  answer: 2
  explanation: "Rolle's Theorem requires differentiability on the open interval (a, b). The function |x| has a corner at x = 0 where the derivative does not exist, so the theorem cannot be applied. The fact that f(-1) = f(1) and the function is continuous is not enough — all three hypotheses must hold. Option A is the classic error: students who only remember the equal-endpoints and continuity conditions miss the differentiability check."

- question: "Rolle's Theorem is applied to f(x) = x³ − x on [−1, 1]. The theorem guarantees which of the following?"
  type: multiple-choice
  options:
    - "Exactly one c in (−1, 1) where f′(c) = 0"
    - "At least one c in (−1, 1) where f′(c) = 0"
    - "At least one c in [−1, 1] where f′(c) = 0, possibly at an endpoint"
    - "A unique c in (−1, 1) where f(c) = 0"
  answer: 1
  explanation: "Rolle's Theorem guarantees at least one such c — the conclusion is existential, not uniqueness. For this function, f′(x) = 3x² − 1 = 0 gives x = ±1/√3, so there are actually two such points in (−1, 1). The theorem promised at least one and delivered two. Option C is wrong because the theorem places c strictly inside the open interval (a, b), not at the endpoints."

- question: "If f satisfies most three hypotheses of Rolle's Theorem on [a, b], the theorem guarantees that there is exactly one interior point where f′ = 0."
  type: true-false
  answer: false
  explanation: "Rolle's Theorem guarantees the existence of at least one such point, not uniqueness. A function can satisfy all three hypotheses and have multiple horizontal tangents — for example, f(x) = x³ − x on [−1, 1] gives two points where f′(c) = 0. The theorem says 'there exists'; it says nothing about how many such points exist."

- question: "A function with a corner (non-differentiable point) on the interior of [a, b] cannot satisfy the hypotheses of Rolle's Theorem, even if it is continuous and f(a) = f(b)."
  type: true-false
  answer: true
  explanation: "Correct. Rolle's Theorem requires differentiability on the open interval (a, b). A corner is precisely a point where the derivative does not exist, so the second hypothesis fails. The example f(x) = |x| on [−1, 1] shows this clearly: it is continuous, satisfies f(−1) = f(1) = 1, but has a corner at x = 0, so Rolle's Theorem does not apply — and indeed f′(x) = ±1 wherever it exists, never zero."

- question: "Why are all three hypotheses in Rolle's Theorem necessary? Briefly describe what goes wrong — and give a specific example — when each hypothesis is dropped."
  type: short-answer
  answer: "Continuity on [a,b]: without it, a function can jump discontinuously from f(a) back to f(a) without any turning point. Example: f(x) = 0 on [0,1] except f(0.5) = 1; f(0) = f(1) = 0 but f′ ≠ 0 wherever defined. Differentiability on (a,b): without it, a function can have a corner that allows it to change direction without a zero derivative. Example: f(x) = |x| on [−1,1] has f(−1) = f(1) but f′(0) is undefined and f′ ≠ 0 elsewhere. Equal endpoint values f(a) = f(b): without it, the function has a net slope and need not turn around. Example: f(x) = x on [0,1] is smooth with f′(x) = 1 everywhere — no horizontal tangent."
  explanation: "Each hypothesis blocks a specific loophole. Continuity blocks teleportation (jumps). Differentiability blocks corners that allow direction changes without a zero slope. Equal endpoints forces the function to 'come back,' creating a turning point. Remove any one and you can construct a counterexample where the conclusion fails."
```

## Explainer

You know that a function's derivative describes its slope, and that the slope is zero wherever the function has a local maximum or minimum. Rolle's Theorem turns that observation into a formal guarantee: if a smooth curve begins and ends at the *same height*, something must have caused it to turn around in between, and that turning point is where the slope is exactly zero.

The three hypotheses are each essential. **Continuity on [a, b]** rules out jumps — a function that teleports can go from height h back to height h without ever having a horizontal tangent. **Differentiability on (a, b)** rules out corners — the absolute value function |x| satisfies f(-1) = f(1) = 1 and is continuous everywhere, but at x = 0 the derivative is undefined and f'(x) = ±1 everywhere it exists (never zero). **Equal endpoint values f(a) = f(b)** is the third condition; dropping it kills the conclusion immediately: f(x) = x is smooth on [0, 1] with f'(x) = 1 everywhere.

Think of a race: a runner starts and finishes at the same point on a circular track, and their position as a function of time is continuous and smooth. At some moment during the race, they must have been momentarily moving directly away from the finish at zero net progress — equivalently, velocity is zero at some turning point. That's exactly what Rolle's Theorem says. Concretely: f(x) = x³ - x on [-1, 1] has f(-1) = 0 = f(1), so the theorem applies. f'(x) = 3x² - 1 = 0 gives x = ±1/√3 ≈ ±0.577, both inside (-1, 1). The theorem guarantees at least one such c — here there are two.

Rolle's Theorem matters primarily as the foundation for the **Mean Value Theorem**, your next topic. The MVT generalizes it to the case where f(a) ≠ f(b): instead of a horizontal tangent, you get a tangent parallel to the secant line. The proof of the MVT constructs a new function h(x) = f(x) - [line from (a, f(a)) to (b, f(b))], which *does* satisfy h(a) = h(b) = 0, then applies Rolle's. Understanding Rolle's Theorem deeply — especially which hypotheses are doing the work and what fails when they're violated — gives you immediate leverage on the MVT and the many results that flow from it.
