---
id: double-integrals-rectangular-regions
title: Double Integrals over Rectangular Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: iterated-integrals-fubini
  type: hard
builds-toward:
- double-integrals-general-regions
- double-integrals-polar
tags:
- rectangular-regions
- computation
- bounds
stage: formal-systems
status: validated
---

# Double Integrals over Rectangular Regions

## Core Idea
For a rectangular region R = [a, b] × [c, d], the double integral ∬_R f dA = ∫_a^b ∫_c^d f(x, y) dy dx is straightforward: the bounds are constants. This is the entry point for computing double integrals; the order of integration does not matter for rectangles.

## Questions

```yaml
- question: "A student is computing ∬_R xy dA over R = [1,3]×[0,2], set up as ∫_1^3 ∫_0^2 xy dy dx. After evaluating the inner integral ∫_0^2 xy dy, they obtain 2x. What does this intermediate result represent?"
  type: multiple-choice
  options:
    - "The final answer to the double integral"
    - "A function of x giving the cross-sectional 'slice area' of the solid at each fixed x-value"
    - "An error — x should have been substituted with a constant before integrating"
    - "The volume of the region below z = xy along the y-axis only"
  answer: 1
  explanation: "During the inner integration, x is treated as a fixed parameter — not a variable, not substituted away. The result 2x is a function of x that represents the area of the cross-section (a slice perpendicular to the x-axis) at each value of x. The outer integral ∫_1^3 2x dx then sums all these cross-sections to get the total volume. This two-step process — slicing, then summing slices — is the geometric heart of iterated integration."

- question: "Why is it valid to switch the order of integration for a rectangular region, but not always for a non-rectangular region without changing the bounds?"
  type: multiple-choice
  options:
    - "Rectangular regions have more symmetry, which guarantees that both orders give equal results by symmetry"
    - "On rectangles all four bounds are constants, so neither bound depends on the other variable; on general regions, inner bounds depend on the outer variable and must be re-derived when switching"
    - "Fubini's theorem only applies to rectangular regions and has no extension to general shapes"
    - "Switching order on a non-rectangular region changes the numerical value of the integral"
  answer: 1
  explanation: "The key is constant bounds. On R = [a,b]×[c,d], the limits a, b, c, d are all fixed numbers — no bound depends on x or y. Whether you integrate y first (with x as the outer variable) or x first (with y as the outer variable), the same rectangle is covered. On a non-rectangular region, the inner limits are functions of the outer variable (e.g., ∫_0^1 ∫_0^x f dy dx). Switching order requires re-deriving the bounds to describe the same region correctly — the region itself hasn't changed, but the description has."

- question: "When evaluating the inner integral ∫_c^d f(x,y) dy in an iterated double integral over a rectangle, the variable x is treated as a varying quantity that changes as you integrate."
  type: true-false
  answer: false
  explanation: "During the inner integration over y, x is held fixed — treated as a constant parameter. You are computing the area of a single cross-sectional slice at one specific x-value. Only after the inner integral is fully evaluated (yielding a function of x) does x become the variable of integration in the outer integral. Treating x as varying during the inner step is the most common computational error in setting up iterated integrals."

- question: "For a rectangular region R = [a,b]×[c,d], ∬_R f dA = ∫_a^b ∫_c^d f(x,y) dy dx = ∫_c^d ∫_a^b f(x,y) dx dy, regardless of the form of f."
  type: true-false
  answer: true
  explanation: "This is exactly what Fubini's theorem guarantees for rectangles (assuming f is continuous, or more generally, integrable on R). Because the bounds are all constants, either order of integration covers the entire rectangle, and both iterated integrals compute the same double integral. In practice, one order may produce a simpler antiderivative than the other — the computational flexibility is a major advantage of working on rectangular regions."

- question: "Explain what happens mathematically when you evaluate the inner integral in an iterated double integral over a rectangle. What does the result represent, and how does it lead to the final answer?"
  type: short-answer
  answer: "The inner integral ∫_c^d f(x,y) dy treats x as a fixed constant and integrates f over the y-interval [c,d]. The result is a function A(x) representing the area of the cross-sectional slice of the solid z = f(x,y) at that fixed x-value. The outer integral ∫_a^b A(x) dx then sums all these cross-sectional areas across [a,b], accumulating them to produce the total volume (or signed volume if f takes negative values). This is the 'slice-then-sum' interpretation of iterated integration."
  explanation: "The two-step structure mirrors how single-variable integration works: the inner integral solves a single-variable problem (with x as a parameter), and the outer integral solves another single-variable problem using the result. The rectangle's constant bounds make this clean — no bounds need adjustment between steps. For non-rectangular regions, the bounds of the inner integral are functions of the outer variable, adding a layer of complexity that rectangular regions avoid."
```

## Explainer

From Fubini's theorem and iterated integrals, you already know the central result: a double integral over a rectangle can be evaluated by integrating one variable at a time. The **double integral** ∬_R f(x, y) dA accumulates the value of f(x, y) over every point in the region R, multiplied by an infinitesimal area element dA. Geometrically, when f ≥ 0, this equals the volume of the solid sitting between the xy-plane and the surface z = f(x, y) directly above R. When f takes negative values, the integral counts volume below the plane as negative — the signed volume interpretation parallels the single-variable signed area.

For a rectangular region R = [a, b] × [c, d], Fubini's theorem gives the computation rule: ∬_R f dA = ∫_a^b ∫_c^d f(x, y) dy dx. The inner integral ∫_c^d f(x, y) dy treats x as a fixed constant and integrates f over the y-interval [c, d]. The result is a function of x alone — call it A(x) — representing the "cross-sectional area" of the solid at that x-value. The outer integral ∫_a^b A(x) dx then adds up all those cross-sections across [a, b]. Think of slicing the solid with vertical planes perpendicular to the x-axis: you first compute each slice's area, then integrate the areas to get the total volume.

The critical feature of rectangular regions is that both pairs of bounds are **constants**: a, b, c, d do not depend on x or y. This means you can also integrate in the opposite order — ∫_c^d ∫_a^b f(x, y) dx dy — and get the same answer. Switching order is freely available on rectangles, which makes them computationally flexible. Choose whichever order makes the inner integral easier to compute. For non-rectangular regions, the bounds of the inner integral will depend on the outer variable, and switching order requires re-determining the bounds — a more involved process. Mastering constant-bound rectangles builds the mechanics (and the intuition for what "slicing" means) before that complication arises.

The setup step is as important as the antidifferentiation. Given ∬_R f dA, explicitly write R = [a, b] × [c, d], confirm both pairs of bounds are constants, declare your order of integration, and write the nested integral before computing. A clean setup prevents the most common errors: using a bound for the wrong variable, or accidentally treating an outer variable as a constant inside the inner integral. Once the setup is correct, the inner integral is a standard single-variable antiderivative problem — the outer variable is just a parameter held fixed while you do it.
