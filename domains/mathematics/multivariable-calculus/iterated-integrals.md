---
id: iterated-integrals
title: Iterated Integrals and Fubini's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: antiderivatives
  type: hard
builds-toward:
- double-integrals-cartesian
- triple-integrals
tags:
- integrals
- fubini
stage: formal-systems
status: validated
---

# Iterated Integrals and Fubini's Theorem

## Core Idea
A double integral ∬ f(x,y) dA can be computed as an iterated integral ∫∫ f(x,y) dy dx. By Fubini's theorem, the order can be swapped if f is continuous; rewriting bounds requires understanding the region carefully.

## Questions

```yaml
- question: "A student sets up ∫₀¹ ∫₀ˣ f(x,y) dy dx over a triangular region. To switch the order of integration, what are the correct new bounds?"
  type: multiple-choice
  options:
    - "∫₀¹ ∫₀^y f(x,y) dx dy"
    - "∫₀¹ ∫_y^1 f(x,y) dx dy"
    - "∫₀¹ ∫₀¹ f(x,y) dx dy"
    - "∫₀¹ ∫₀ˣ f(x,y) dx dy"
  answer: 1
  explanation: "In the original, x goes 0 to 1 and y goes 0 to x — covering the triangle below the diagonal y = x. To reverse the order, describe the same triangle from y's perspective: y ranges from 0 to 1, and for each fixed y, x ranges from y to 1. This gives ∫₀¹ ∫_y^1 f(x,y) dx dy. Option A covers a different triangle (above the diagonal). Option C integrates over the full unit square — too large a region."

- question: "Fubini's theorem guarantees that for a continuous function over a rectangle [a,b] × [c,d]:"
  type: multiple-choice
  options:
    - "The iterated integral with dy dx always gives a larger value than the one with dx dy"
    - "The order of integration can be reversed without changing the result"
    - "The double integral equals the product of two single integrals"
    - "The outer integral must be evaluated before the inner integral"
  answer: 1
  explanation: "Fubini's theorem states that ∫ₐᵇ ∫_c^d f(x,y) dy dx = ∫_c^d ∫ₐᵇ f(x,y) dx dy for continuous f on a rectangle. The order can be reversed without changing the value. This is useful because one order may be algebraically much simpler. Option C is wrong — that would require f(x,y) to factor as g(x)h(y)."

- question: "When switching the order of integration for a non-rectangular region, the numerical bounds of integration stay the same — only the variable labels change."
  type: true-false
  answer: false
  explanation: "The bounds change substantively, not just in label. For example, ∫₀¹ ∫₀ˣ f dy dx becomes ∫₀¹ ∫_y^1 f dx dy — the inner bound shifts from 'x' (a function of the outer variable) to 'y' and '1'. You must re-describe the same 2D region from the new outer variable's perspective, which requires sketching the region and reading the new bounds directly from the geometry."

- question: "The key strategy behind iterated integrals is to compute a double integral as two sequential single-variable integrations, treating one variable as constant while integrating over the other."
  type: true-false
  answer: true
  explanation: "This is exactly the method: fix x, integrate f(x,y) over y to get a cross-sectional area function A(x), then integrate A(x) over x to accumulate total volume. Each step is a standard single-variable integral. The two-pass strategy reduces a 2D problem to sequential 1D problems that you already know how to handle."

- question: "Why does switching the order of integration for an iterated integral over a non-rectangular region require changing the integration bounds? What is the reliable technique for finding the new bounds?"
  type: short-answer
  answer: "The bounds encode a description of the integration region from the perspective of the outer variable. Switching which variable is outer requires re-describing the same region from the new perspective. For a triangle like 0 ≤ y ≤ x ≤ 1, x as outer variable means y runs 0 to x; y as outer variable means x runs y to 1. The reliable technique is to sketch the region, label corners and boundary curves, and read the new bounds directly from the sketch — asking 'for each fixed value of the outer variable, what range does the inner variable span?'"
  explanation: "Algebraic manipulation of the bounds alone is error-prone. The sketch-first approach directly reads the geometric constraints of the region and translates them into integration limits, which is far more reliable especially when dealing with curved boundaries."
```

## Explainer

You know from antiderivatives that a single integral ∫ₐᵇ f(x) dx computes the signed area under a curve on an interval. Now extend the question: what is the signed volume under a surface z = f(x, y) over a 2D region R in the xy-plane? The double integral ∬_R f(x, y) dA answers this, but computing it directly requires a strategy. The **iterated integral** reduces the 2D problem to two sequential 1D integrations, each of which you already know how to perform.

The idea is to slice the volume into thin cross-sections. Fix a value of x and integrate f(x, y) over y — this gives A(x), the area of the cross-sectional slice at that x. Then integrate A(x) over x to accumulate all slices into a total volume. Written explicitly: ∫ₐᵇ ( ∫_c^d f(x,y) dy ) dx. The inner integral treats x as a constant and integrates in y; the outer integral then integrates the result in x. The parentheses are usually omitted, and you simply evaluate the innermost integral first, working outward.

**Fubini's theorem** guarantees that when f is continuous on a rectangle [a,b] × [c,d], the order of integration can be reversed without changing the answer:

  ∫ₐᵇ ∫_c^d f(x,y) dy dx  =  ∫_c^d ∫ₐᵇ f(x,y) dx dy

This is powerful because one order may be algebraically much simpler than the other. If ∫ f(x,y) dy is hard to compute, try reversing the order and integrating in x first. The theorem guarantees you get the same answer, so algebraic convenience guides the choice.

For **non-rectangular regions**, the bounds of the inner integral become functions of the outer variable. Integrating over the triangular region where 0 ≤ x ≤ 1 and 0 ≤ y ≤ x gives ∫₀¹ ∫₀ˣ f(x,y) dy dx — y runs from 0 to x, a bound that depends on the current value of x. To reverse the order, you must re-describe the same region from y's perspective: y ranges from 0 to 1, and for each y, x ranges from y to 1. The reversed integral is ∫₀¹ ∫_y^1 f(x,y) dx dy. Always sketch the region first, label the corners and curves, and read the bounds directly from the sketch — this is the single most reliable technique for setting up iterated integrals correctly.
