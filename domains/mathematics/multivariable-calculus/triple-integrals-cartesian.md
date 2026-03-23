---
id: triple-integrals-cartesian
title: Triple Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: applications-integrals-area-mass
  type: hard
builds-toward:
- triple-integrals-cylindrical-spherical
tags:
- triple-integrals
- cartesian
- volume
stage: formal-systems
status: validated
---

# Triple Integrals in Cartesian Coordinates

## Core Idea
For a region W in 3D, the triple integral ∭_W f(x, y, z) dV = ∫∫∫ f(x, y, z) dz dy dx represents volume (when f = 1) or weighted volume. Fubini's theorem permits changing order of integration. Setting up bounds for W requires careful description as a region in 3D.

## Questions

```yaml
- question: "You are integrating over the solid tetrahedron with vertices at (0,0,0), (1,0,0), (0,1,0), and (0,0,1), using the order dz dy dx. What is the correct upper bound for z in the innermost integral?"
  type: multiple-choice
  options:
    - "z = 1, since z ranges from 0 to 1 overall in the region"
    - "z = 1 − x, since the region's z-extent depends only on x"
    - "z = 1 − x − y, since the slanted face satisfies the plane x + y + z = 1"
    - "z = √(1 − x² − y²), the boundary of a hemisphere"
  answer: 2
  explanation: "The tetrahedron is bounded above by the plane x + y + z = 1, so z ≤ 1 − x − y for any fixed (x, y) inside the region. Using z = 1 as the upper bound (option A) is the most common error — it ignores that the ceiling on z depends on where you are in the xy-plane. Option B is also wrong; the bound depends on both x and y. This is the essential challenge of triple integrals: inner bounds are generally functions of the outer variables."

- question: "Which statement about changing the order of integration in a triple integral is correct?"
  type: multiple-choice
  options:
    - "The integral's value changes when you reorder because different bounds are used"
    - "You can freely swap any two variables without rederiving the bounds"
    - "The value is unchanged by Fubini's theorem, but the bounds must be completely rederived for the new ordering"
    - "Reordering is only valid if the integration region is a rectangular box"
  answer: 2
  explanation: "Fubini's theorem guarantees that any ordering of integration yields the same value — but only if you correctly re-describe the region W for the new ordering. The bounds for one ordering (e.g., the z bounds as a function of x and y) are completely different from the bounds for another ordering (the x bounds as a function of y and z). Reordering is not just swapping variable names — it requires redrawing and re-reading the geometry of the region from a new perspective."

- question: "For the unit cube [0,1]³, all six possible orderings of integration produce the same result with the same constant bounds [0,1] for each variable."
  type: true-false
  answer: true
  explanation: "The unit cube has constant bounds in every direction: x ∈ [0,1], y ∈ [0,1], z ∈ [0,1], independent of the other variables. So no matter what order you integrate, the bounds are always the same constants and the value is the same. This is the special simplicity of rectangular regions — the bounds decouple. For any non-rectangular region, the bounds of inner variables will depend on outer variables, so reordering requires re-deriving them."

- question: "For a non-rectangular region in 3D (like a tetrahedron or a ball), you can set the bounds for each variable independently of the other variables."
  type: true-false
  answer: false
  explanation: "For non-rectangular regions, inner bounds must account for the shape of the region at each fixed value of the outer variables. For example, integrating over the unit ball x² + y² + z² ≤ 1 in order dz dy dx, the z bounds are −√(1−x²−y²) to √(1−x²−y²) — depending on both x and y. Using fixed bounds [−1, 1] for all three variables would integrate over the cube containing the ball, not the ball itself, giving the wrong answer."

- question: "Why might you choose to change the order of integration in a triple integral even though the final value is the same regardless of order?"
  type: short-answer
  answer: "Different orderings produce different inner integrands, some of which may be far harder to evaluate analytically than others. For example, one ordering might require integrating e^(z³) with respect to z (which has no elementary antiderivative), while a different ordering avoids this entirely. By Fubini's theorem the value is the same, but choosing the right order can mean the difference between a tractable computation and one that cannot be done in closed form."
  explanation: "This is the practical payoff of understanding Fubini's theorem deeply. Recognizing that order can be changed — and that the key work is re-describing the region's bounds for the new order — is what allows you to turn impossible integrals into manageable ones. Sketching the region and asking 'which variable is easiest to integrate last?' (as the outermost integral) is a standard strategic move in multivariable calculus."
```

## Explainer

From double integrals, you know that ∬_R f(x, y) dA accumulates f over a two-dimensional region R, and that when f = 1, it returns the area of R. Triple integrals extend this pattern by one more dimension: ∭_W f(x, y, z) dV accumulates f over a three-dimensional region W. When f = 1, the triple integral gives the **volume** of W. When f is a density function (mass per unit volume), the triple integral gives total mass. The structure is the same; only the dimensionality changes.

Evaluating a triple integral means converting it to three nested single-variable integrals, applied from the inside out. For a region W, you first choose an order of integration — say dz dy dx — and then describe W as nested bounds: z ranges from z_low(x, y) to z_high(x, y) for fixed (x, y); y ranges from y_low(x) to y_high(x) for fixed x; and x ranges over a fixed interval [a, b]. The key skill is reading off these bounds from a geometric description of W. For a unit cube [0,1]³ the bounds are all constants. For a tetrahedron or a ball, they depend on the outer variables.

**Fubini's theorem** says the order of integration doesn't matter (for well-behaved f): you can integrate dz dy dx, or dx dy dz, or any of the six orderings, and get the same answer. This is powerful because some orderings produce far simpler integrals than others. The classic strategy is: if one ordering leads to a hard inner integral, try a different order. To change the order, you must re-describe the region W in terms of the new order of nesting — draw a sketch of W and re-read the bounds from the new perspective.

A common challenge is setting up bounds for regions defined by curved surfaces. For the region inside the sphere x² + y² + z² ≤ 1, Cartesian bounds require z ∈ [−√(1−x²−y²), √(1−x²−y²)] and y ∈ [−√(1−x²), √(1−x²)] and x ∈ [−1, 1] — correct but messy. This is exactly why cylindrical and spherical coordinates (the natural next topic) exist: they describe curved regions with clean constant bounds. Mastering triple integrals in Cartesian coordinates first builds the geometric intuition needed to recognize when a coordinate change will simplify a problem.
