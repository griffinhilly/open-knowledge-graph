---
id: lebesgue-differentiation-theorem
title: The Lebesgue Differentiation Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
  - id: introduction-lebesgue-integral
    type: hard
  - id: lebesgue-measure-euclidean-space
    type: hard
  - id: dominated-convergence-theorem
    type: soft
  - id: fundamental-theorem-calculus-rigorous
    type: soft
builds-toward: []
tags: [measure-theory, lebesgue-integral, differentiation, maximal-function, absolute-continuity, lebesgue-points]
stage: expert
status: validated
---

# The Lebesgue Differentiation Theorem

## Core Idea
The Lebesgue differentiation theorem says that for a locally integrable function f on ℝⁿ, the average of f over the ball B(x, r) converges to f(x) as r → 0 for almost every x. In one dimension this gives the fundamental theorem of calculus for Lebesgue integrals: if F(x) = ∫ from a to x of f, then F'(x) = f(x) almost everywhere. The proof rests on the Hardy-Littlewood maximal function and a covering lemma. The theorem also explains which functions are integrals of their derivatives, namely the absolutely continuous ones.

## How It's Best Learned
Start with the continuous case, where averages converge to f(x) at every point by uniform continuity, and ask what can go wrong for an integrable f. Introduce the maximal function Mf(x) = sup over r > 0 of the average of |f| on B(x, r), and prove the weak-type estimate with the Vitali covering lemma. Then follow the standard pattern: approximate f by continuous functions in L¹ and use the maximal estimate to control the error. Close with the Cantor function as an example of a continuous increasing function that is not the integral of its derivative.

## Common Misconceptions
- The averages of f over shrinking balls converge to f(x) at every point. (Convergence holds only almost everywhere; changing f on a null set does not change any of the averages.)
- Every continuous, increasing function F satisfies F(b) - F(a) = ∫ from a to b of F'. (The Cantor function rises from 0 to 1 on [0, 1] yet has F' = 0 almost everywhere; the identity requires absolute continuity.)
- The maximal function of an integrable function is integrable. (Mf satisfies only a weak-type bound; for any f that is not zero almost everywhere on ℝⁿ, Mf is not integrable.)

## Questions

```yaml
- question: "For f ∈ L¹_loc(ℝⁿ), what does the Lebesgue differentiation theorem assert?"
  type: multiple-choice
  options:
    - "The ball averages of f converge to f(x) for every x"
    - "The ball averages of f converge to f(x) for almost every x"
    - "f is differentiable almost everywhere"
    - "f is continuous almost everywhere"
  answer: 1
  explanation: "The theorem concerns averages of f, not derivatives of f. The convergence holds outside a set of measure zero. An integrable function such as the indicator of the rationals is nowhere continuous, but its averages are all 0, matching the function almost everywhere."

- question: "The Cantor function F is continuous and increasing on [0, 1] with F(0) = 0 and F(1) = 1. Since F'(x) = 0 almost everywhere, ∫ from 0 to 1 of F' equals F(1) - F(0)."
  type: true-false
  answer: false
  explanation: "∫ from 0 to 1 of F' = 0, but F(1) - F(0) = 1. The Cantor function is not absolutely continuous, so the Lebesgue version of the fundamental theorem of calculus does not apply to it."

- question: "State the weak-type (1, 1) inequality for the Hardy-Littlewood maximal function on ℝⁿ."
  type: short-answer
  answer: "There is a constant C depending only on n (C = 3ⁿ works) such that |{x : Mf(x) > α}| ≤ (C/α)‖f‖₁ for every f ∈ L¹(ℝⁿ) and every α > 0."
  explanation: "The constant 3ⁿ comes from the Vitali covering lemma, which selects disjoint balls whose threefold enlargements cover the set. The estimate controls how large the set where averages are big can be, which is what the differentiation proof needs."

- question: "If f ∈ L¹[a, b] and F(x) = ∫ from a to x of f(t) dt, what can be said about F'?"
  type: short-answer
  answer: "F is differentiable almost everywhere on [a, b] and F'(x) = f(x) for almost every x."
  explanation: "The difference quotient (F(x + h) - F(x))/h is the average of f over an interval of length |h| next to x, so this is the one-dimensional case of the differentiation theorem, applied to one-sided intervals."
```

## Explainer

For a continuous function f on ℝ, the fundamental theorem of calculus says that d/dx ∫ from a to x of f = f(x) at every point. The difference quotient (F(x + h) - F(x))/h is the average of f over an interval of length |h|, and continuity makes these averages converge to f(x). Lebesgue integration allows far rougher functions. The natural question is whether averages still recover the function.

Theorem. If f is locally integrable on ℝⁿ, then for almost every x,

lim as r → 0 of (1/|B(x, r)|) ∫ over B(x, r) of f(y) dy = f(x).

In fact, almost every x is a Lebesgue point, meaning the average of |f(y) - f(x)| over B(x, r) tends to 0.

"Almost every" cannot be improved to "every." Changing f on a null set leaves every integral unchanged, so averages cannot detect the values of f on such a set.

The proof has a standard structure. If f is continuous with compact support, the result holds at every point. Continuous functions with compact support are dense in L¹, so write f = g + (f - g) with g continuous and ‖f - g‖₁ small. The error term needs a uniform bound on averages, supplied by the Hardy-Littlewood maximal function

Mf(x) = sup over r > 0 of (1/|B(x, r)|) ∫ over B(x, r) of |f(y)| dy.

The key estimate is weak type (1, 1): |{Mf > α}| ≤ (3ⁿ/α)‖f‖₁. It follows from the Vitali covering lemma. From any finite family of balls one can choose disjoint ones whose threefold enlargements cover the union. With this estimate, the set where the limit superior of |average of f - f(x)| exceeds 2α has outer measure at most a constant times ‖f - g‖₁/α. Letting ‖f - g‖₁ → 0 and then α → 0 shows the bad set has measure zero.

In one dimension the theorem gives the Lebesgue version of the fundamental theorem: if f ∈ L¹[a, b] and F(x) = ∫ from a to x of f, then F' = f almost everywhere. The reverse direction needs care. A function F satisfies F(x) = F(a) + ∫ from a to x of F' exactly when F is absolutely continuous. The Cantor function shows the condition is needed: it is continuous and increasing, rises from 0 to 1, and has derivative 0 at every point outside the Cantor set, which has measure zero.