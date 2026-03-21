---
id: double-integrals-cartesian
title: Double Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: iterated-integrals
  type: hard
builds-toward:
- double-integrals-polar
- area-volume-integrals
tags:
- double-integral
- area-volume
stage: formal-systems
status: draft
---

# Double Integrals in Cartesian Coordinates

## Core Idea
The double integral ∬_R f(x,y) dA gives the volume under z = f(x,y) above region R. For non-rectangular regions, bounds depend on neighboring variables: ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx.

## Questions

```yaml
- question: "You are computing ∬_R f(x,y) dA over the region bounded by y = x² (below) and y = x (above) for 0 ≤ x ≤ 1. A student sets up ∫₀¹ ∫₀¹ f(x,y) dy dx. What is wrong?"
  type: multiple-choice
  options:
    - "The outer limits should run from 0 to 1 in y, not x, since y is the inner variable"
    - "The inner limits should be functions of x (from x² to x), not the constants 0 to 1"
    - "Double integrals over non-rectangular regions can only be evaluated in polar coordinates"
    - "Nothing is wrong — Fubini's theorem allows constant limits regardless of the region's shape"
  answer: 1
  explanation: "The error is treating a non-rectangular region as if it were a rectangle. For a fixed x in [0,1], y doesn't range over all of [0,1] — it only ranges from the lower boundary x² up to the upper boundary x. The correct setup is ∫₀¹ ∫_{x²}^{x} f(x,y) dy dx. Option D is the classic mistake: Fubini's theorem guarantees that switching integration order gives the same answer for well-behaved f, but it does NOT allow you to ignore the actual shape of the region."

- question: "When should you prefer slicing a region horizontally (fixing y and integrating x from a left boundary to a right boundary) over slicing vertically?"
  type: multiple-choice
  options:
    - "Always — horizontal slicing is the standard convention in Cartesian double integrals"
    - "Only when f(x,y) depends solely on y and not on x"
    - "When the horizontal boundaries are simpler to express as functions of y than the vertical boundaries as functions of x"
    - "Only when the region is symmetric about the y-axis"
  answer: 2
  explanation: "The choice of slicing direction is a strategic one based on which description of the region's boundary gives cleaner limits. For the region between y = x and y = x², vertical slices give simple limits (y from x² to x). But a different region — say, bounded by x = y² and x = y — is more naturally described with horizontal slices. Always sketch the region first and ask: which boundary curves are easier to express as functions of the outer variable? That's the direction to slice."

- question: "For any region R, the double integral ∬_R 1 dA equals the area of R."
  type: true-false
  answer: true
  explanation: "When f(x,y) = 1, the double integral sums up infinitesimal area elements dA over the entire region, giving the total area. This is a useful check: if you compute a 'volume' with f = 1 and get a negative number, or if your area is implausibly large, the limits are wrong. More generally, if f represents surface density, ∬_R f dA gives total mass — the double integral is a summation over the region, and f = 1 is just the constant-density (uniform) case."

- question: "To reverse the order of integration in a double integral over a non-rectangular region, you can simply swap the inner and outer bounds without re-examining the region."
  type: true-false
  answer: false
  explanation: "Reversing integration order on a non-rectangular region requires re-describing the region's boundaries from scratch for the new slicing direction. The old limits cannot simply be swapped — they were derived for a specific slicing direction and are only valid for that direction. You must sketch the region again, determine the new outer variable's range, and re-derive the inner variable's bounds as functions of the new outer variable. Swapping without this step produces wrong limits."

- question: "Why does the inner integral in a double integral over a non-rectangular region have limits that are functions of the outer variable, rather than constants?"
  type: short-answer
  answer: "Because for each fixed value of the outer variable, the range of the inner variable depends on where the region's boundaries are at that particular cross-section. Think of slicing the region into thin strips: each strip at position x spans a different y-range (from the lower boundary curve g₁(x) to the upper boundary curve g₂(x)). Constants would only work if every strip had the same height — which is true only for rectangles."
  explanation: "The variable limits are what distinguish integrating over a shaped region from integrating over a rectangle. They encode the geometry of the region directly into the integral. Getting them right requires understanding the region's shape, which is why sketching before setting up is essential — the limits are a description of the region's boundaries, and that description changes depending on which direction you slice."
```

## Explainer

You already know how to compute **iterated integrals** — integrals computed step by step, one variable at a time. A double integral over a rectangular region is just an iterated integral where the bounds are all constants: ∫_a^b ∫_c^d f(x,y) dy dx means "for each fixed x in [a,b], integrate f(x,y) over y from c to d, then integrate the result over x." Fubini's theorem guarantees that for well-behaved f you can switch the order of integration freely on a rectangle, and the answer is the same either way.

The more interesting case — and the one requiring real care — is integration over **non-rectangular regions**. The region R might be bounded above by a curve y = g₂(x) and below by y = g₁(x), for x running from a to b. For a given x, y only ranges from g₁(x) to g₂(x), not all the way from c to d. So the inner integral's limits become functions of x: ∫_a^b [∫_{g₁(x)}^{g₂(x)} f(x,y) dy] dx. The inner integral (in y) is computed first with x treated as a constant, producing a function of x alone. Then the outer integral finishes the job. Think of slicing the region R into thin vertical strips of width dx; for each strip at position x, you integrate f from the bottom boundary curve up to the top boundary curve.

You can also slice horizontally: fix y and let x run from some left boundary h₁(y) to some right boundary h₂(y), then integrate over y. The choice of orientation depends on which gives simpler limits. A region bounded by y = x and y = x² from x = 0 to x = 1 is easy to describe with vertical slices (x from 0 to 1, y from x² to x) and awkward to describe with horizontal slices. Always sketch the region first, then decide which slicing direction gives cleaner limits.

The geometric meaning reinforces the algebra. If f(x,y) ≥ 0, then ∬_R f(x,y) dA is the volume of the solid above R and below the surface z = f(x,y). When f = 1, ∬_R 1 dA = area of R — the double integral reduces to an area formula. More generally, if f represents a surface density (mass per unit area), then the double integral gives total mass. These physical interpretations are a useful check: if your computed volume is negative or your computed area is enormous, something has gone wrong with the limits.
