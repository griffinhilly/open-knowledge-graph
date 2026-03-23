---
id: area-volume-integrals
title: Computing Areas and Volumes
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
- id: double-integrals-polar
  type: soft
builds-toward:
- triple-integrals
tags:
- area
- volume
stage: formal-systems
status: validated
---

# Computing Areas and Volumes

## Core Idea
Area of region R: A = ∬_R 1 dA. Volume under z = f(x,y): V = ∬_R f(x,y) dA. Double integrals generalize single-variable formulas for area and volume.

## Questions

```yaml
- question: "What does the double integral ∬_R 1 dA compute?"
  type: multiple-choice
  options:
    - "The perimeter of region R"
    - "The area of region R"
    - "The average height of the surface z = 1 over R"
    - "The surface area of the plane z = 1 above R"
  answer: 1
  explanation: "Integrating the constant function 1 over R sums all infinitesimal area elements dA across R, giving the total area of R. This is the 2D analogue of ∫_a^b 1 dx = b − a (the length of [a,b]). It also equals the volume under the surface z = 1 above R — a prism of height 1 — which gives base area × height = Area × 1 = Area, confirming the result."

- question: "A student calculates the area of a unit disk (radius 1) in polar coordinates as ∫₀²π ∫₀¹ 1 dr dθ = 2π, but the actual area is π. What went wrong?"
  type: multiple-choice
  options:
    - "The outer limits should be 0 to π, not 0 to 2π"
    - "The student forgot the factor of r in the polar area element; the correct integrand is r, not 1"
    - "The inner limits for r should be -1 to 1"
    - "The constant function 1 cannot be integrated in polar coordinates — f(r,θ) must depend on r"
  answer: 1
  explanation: "In polar coordinates the area element is dA = r dr dθ, not dr dθ. A small polar 'rectangle' at radius r has width dr and arc length r dθ, so its area is r dr dθ — the factor r appears because arcs get longer as you move away from the origin. The correct integral is ∫₀²π ∫₀¹ r dr dθ = ∫₀²π [r²/2]₀¹ dθ = ∫₀²π ½ dθ = π. Forgetting the factor of r is the single most common error in polar integration."

- question: "The formula V = ∬_R f(x,y) dA for volume under z = f(x,y) above R requires that f(x,y) > 0 everywhere on R."
  type: true-false
  answer: false
  explanation: "The formula applies regardless of the sign of f. When f(x,y) < 0, those regions contribute negatively to the integral, giving a 'signed volume.' The integral ∬_R f(x,y) dA is always defined; it just doesn't equal the total geometric volume between the surface and the xy-plane when f changes sign. For unsigned geometric volume where f < 0 somewhere, you would integrate |f(x,y)| or split the region."

- question: "For a continuous function f over a rectangular region [a,b] × [c,d], the double integral can be evaluated as ∫_a^b(∫_c^d f(x,y) dy) dx or as ∫_c^d(∫_a^b f(x,y) dx) dy, and both give the same result."
  type: true-false
  answer: true
  explanation: "Fubini's theorem guarantees that for a continuous function over a rectangle, the order of integration is interchangeable — both iterated integrals equal the double integral. This is a practical tool: you can choose whichever order makes the computation simpler. The theorem also extends to non-rectangular regions under appropriate conditions, but the rectangular case is the cleanest statement."

- question: "When setting up a double integral over a non-rectangular region R, what is the key step before writing down the limits of integration?"
  type: short-answer
  answer: "Draw the region R and identify its boundary curves. Then decide whether to treat R as x-simple (for each fixed x in [a,b], y runs from a lower boundary g₁(x) to an upper boundary g₂(x)) or y-simple (for each fixed y in [c,d], x runs between two boundary functions h₁(y) and h₂(y)). The inner limits are functions, the outer limits are constants — and the sketch reveals which description is simpler."
  explanation: "Setting up the limits correctly is the core skill of this topic. Students who skip the sketch often write incorrect limits or choose an order that leads to an impossible inner integral. The sketch reveals which boundaries are functions of which variable. Sometimes one order produces elementary integrals while the other is intractable — and you can only see this by understanding the region geometrically first."
```

## Explainer

In single-variable calculus, you computed areas by integrating ∫_a^b f(x) dx — summing infinitely many thin vertical strips, each of height f(x) and width dx. Double integrals generalize this in two directions. To find the **area** of a two-dimensional region R in the xy-plane, you integrate the constant function 1 over R: A = ∬_R 1 dA. Each infinitesimal area element dA contributes 1 to the sum, so the total is just the area. This is conceptually simpler than it sounds: you are counting the number of area elements in R, where each element has size dA.

To find the **volume** under a surface z = f(x, y) above a region R, you integrate f itself: V = ∬_R f(x,y) dA. Each infinitesimal column of height f(x,y) and base dA contributes f(x,y) dA to the volume. Summing these over the entire base region R gives the total volume — exactly the 3D analogue of the area-under-a-curve formula from single-variable calculus. When f(x,y) = c is a constant, the formula gives V = c · Area(R), which is just the volume of a prism: base times height.

The **key skill** is setting up the limits of integration correctly for the region R. If R is a rectangle [a,b] × [c,d], the limits are simply a ≤ x ≤ b and c ≤ y ≤ d. For non-rectangular regions, you describe R as either "x-simple" (for each fixed x in [a,b], y runs from a lower boundary g₁(x) to an upper boundary g₂(x)) or "y-simple" (for each fixed y in [c,d], x runs from h₁(y) to h₂(y)). Drawing the region and identifying these boundary functions is the core of the setup process.

Polar coordinates — which you may have encountered as a soft prerequisite — become essential when R has circular symmetry. The area element in polar coordinates is dA = r dr dθ rather than dx dy, since a small polar "rectangle" is not actually a rectangle but a wedge whose area depends on its radial position r. The factor of r in dA is the source of many errors if forgotten. A circle of radius a centered at the origin integrates as ∫₀²π ∫₀ᵃ r dr dθ = ∫₀²π (a²/2) dθ = πa², confirming the area formula you know from geometry.
