---
id: double-integrals-cartesian-coordinates
title: Double Integrals over Rectangular Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro-domain
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- double-integrals-general-regions
tags:
- double-integrals
- integration
- cartesian
stage: formal-systems
status: draft
---

# Double Integrals over Rectangular Regions

## Core Idea
For a rectangle R = [a, b] × [c, d], the double integral ∬_R f(x, y) dA equals the iterated integral ∫_a^b ∫_c^d f(x, y) dy dx. By Fubini's theorem, the order of integration can be switched if f is continuous. The integral represents signed volume under the surface.

## Questions

```yaml
- question: "You want to evaluate ∬_R f(x,y) dA over the rectangle R = [0,1]×[0,1] where f(x,y) = sin(y²). Which iterated integral is computable in closed form?"
  type: multiple-choice
  options:
    - "∫₀¹ ∫₀¹ sin(y²) dy dx — integrate y first, then x"
    - "∫₀¹ ∫₀¹ sin(y²) dx dy — integrate x first, then y"
    - "Both orders produce the same computable antiderivative"
    - "Neither order produces a closed-form antiderivative, so the integral cannot be evaluated"
  answer: 1
  explanation: "sin(y²) has no elementary antiderivative with respect to y, so the dy-first order (option A) leaves an impossible inner integral. But sin(y²) is independent of x, so the dx-first inner integral ∫₀¹ sin(y²) dx = sin(y²)·[x]₀¹ = sin(y²). The outer integral then becomes ∫₀¹ sin(y²) dy, which still lacks a closed form on its own — but the key point is that the correct first step is to integrate with respect to x, yielding sin(y²), not to fight the impossible inner integral. Choosing the better order of integration is one of the most practical skills the theorem enables."

- question: "A student sets up ∫₀² ∫₀³ f(x,y) dy dx and gets the answer 12. Her partner switches the order to ∫₀³ ∫₀² f(x,y) dx dy. If f is continuous, what answer should her partner get?"
  type: multiple-choice
  options:
    - "−12, because reversing the order negates the integral"
    - "12, because Fubini's theorem guarantees both orders give the same value"
    - "It depends on whether f is positive or negative over the rectangle"
    - "Cannot be determined without knowing what f is"
  answer: 1
  explanation: "Fubini's theorem states that for a continuous function f on a rectangle, the double integral equals either iterated integral and both produce the same number. The double integral ∬_R f dA is a single well-defined value (the signed volume under the surface) — the order of integration is just a computational strategy to reach that value. Both students are computing the same geometric quantity by slicing it in perpendicular directions, so the answer must be 12."

- question: "A double integral ∬_R f(x,y) dA where f can take negative values represents a signed volume — regions where f < 0 contribute negatively."
  type: true-false
  answer: true
  explanation: "Just as a single-variable integral can be negative when the function dips below the x-axis, a double integral sums signed contributions: columns where f(x,y) > 0 contribute positive volume, columns where f(x,y) < 0 contribute negative volume. The total is the net signed volume. This is analogous to the 1D case — the double integral of f = 1 over R gives the area of R, while ∬_R (−1) dA gives the negative of that area."

- question: "Switching the order of integration in a double integral over a rectangle changes the value of the integral."
  type: true-false
  answer: false
  explanation: "For a continuous function on a closed rectangle, Fubini's theorem guarantees that both orders of integration produce the same value. The order of integration is a computational choice, not a mathematical one — both iterated integrals are evaluating the same double integral ∬_R f dA. The order can only matter in degenerate cases (discontinuous or non-integrable functions), not for the continuous functions encountered in standard multivariable calculus."

- question: "Explain why computing a double integral over a rectangle can be reduced to two successive single-variable integrals, and what Fubini's theorem adds to this."
  type: short-answer
  answer: "The double integral sums infinitely many thin rectangular columns of height f(x,y) and base area dA = dx dy. By first integrating with respect to y (for a fixed x), you compute the area of a cross-sectional slice of the solid at that x. Then integrating those slice areas with respect to x sweeps through all cross-sections and accumulates the total volume. Fubini's theorem adds the guarantee that the two possible orders (integrate y first or x first) yield the same result for continuous f, so you can choose whichever order produces a simpler antiderivative."
  explanation: "The geometric interpretation is key: both orders slice the same solid — one cuts it with vertical planes parallel to the yz-plane, the other with planes parallel to the xz-plane. Since there is only one correct volume regardless of how you slice it, both orders must agree. Without Fubini, you would need to prove this agreement for each specific function; the theorem does it once and for all under mild conditions."
```

## Explainer

From your study of multivariable functions, you know that a function f(x, y) assigns a height to each point (x, y) in the plane, producing a surface in three dimensions. The **double integral** ∬_R f(x, y) dA asks: what is the signed volume of the solid region between the surface z = f(x, y) and the xy-plane, over the region R? Just as the single-variable integral sums up infinitely many thin rectangular strips (each of width dx and height f(x)), the double integral sums up infinitely many thin rectangular columns (each of base area dA = dx dy and height f(x, y)).

For a rectangular region R = [a, b] × [c, d], the calculation proceeds by **iterated integration**. Fix x for a moment and integrate f(x, y) with respect to y from c to d — this gives the area of a cross-sectional "slice" of the solid at that x-value, A(x) = ∫_c^d f(x, y) dy. Now sweep x from a to b, integrating A(x): ∫_a^b A(x) dx = ∫_a^b [ ∫_c^d f(x, y) dy ] dx. The outer integral adds up all the cross-sectional areas, giving the total volume. This "slice and sweep" thinking is the same as the washer/shell methods from single-variable calculus — integrate a cross-section, then integrate those cross-sections.

**Fubini's theorem** guarantees that for continuous f (and more generally for integrable f), the order of integration can be reversed: ∫_a^b ∫_c^d f(x, y) dy dx = ∫_c^d ∫_a^b f(x, y) dx dy. Both orders give the same number because they are both computing the same volume; they just slice it in perpendicular directions. Choosing the better order can make a computation dramatically easier — sometimes one order leads to an elementary antiderivative and the other does not.

The machinery here is used constantly: integrals over non-rectangular regions (your next topic) require adjusting the limits of the inner integral as a function of the outer variable, but the iterated-integral structure remains. Double integrals also compute mass (when f is density), expected values in probability, and areas (when f = 1). The key skill to develop is correctly setting up the limits — draw the region, decide which variable is "outer" (fixed while the inner integral runs), and read the inner limits as functions of the outer variable from the boundary of the region.
