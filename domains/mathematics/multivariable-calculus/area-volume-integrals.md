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
status: draft
---

# Computing Areas and Volumes

## Core Idea
Area of region R: A = ∬_R 1 dA. Volume under z = f(x,y): V = ∬_R f(x,y) dA. Double integrals generalize single-variable formulas for area and volume.

## Explainer

In single-variable calculus, you computed areas by integrating ∫_a^b f(x) dx — summing infinitely many thin vertical strips, each of height f(x) and width dx. Double integrals generalize this in two directions. To find the **area** of a two-dimensional region R in the xy-plane, you integrate the constant function 1 over R: A = ∬_R 1 dA. Each infinitesimal area element dA contributes 1 to the sum, so the total is just the area. This is conceptually simpler than it sounds: you are counting the number of area elements in R, where each element has size dA.

To find the **volume** under a surface z = f(x, y) above a region R, you integrate f itself: V = ∬_R f(x,y) dA. Each infinitesimal column of height f(x,y) and base dA contributes f(x,y) dA to the volume. Summing these over the entire base region R gives the total volume — exactly the 3D analogue of the area-under-a-curve formula from single-variable calculus. When f(x,y) = c is a constant, the formula gives V = c · Area(R), which is just the volume of a prism: base times height.

The **key skill** is setting up the limits of integration correctly for the region R. If R is a rectangle [a,b] × [c,d], the limits are simply a ≤ x ≤ b and c ≤ y ≤ d. For non-rectangular regions, you describe R as either "x-simple" (for each fixed x in [a,b], y runs from a lower boundary g₁(x) to an upper boundary g₂(x)) or "y-simple" (for each fixed y in [c,d], x runs from h₁(y) to h₂(y)). Drawing the region and identifying these boundary functions is the core of the setup process.

Polar coordinates — which you may have encountered as a soft prerequisite — become essential when R has circular symmetry. The area element in polar coordinates is dA = r dr dθ rather than dx dy, since a small polar "rectangle" is not actually a rectangle but a wedge whose area depends on its radial position r. The factor of r in dA is the source of many errors if forgotten. A circle of radius a centered at the origin integrates as ∫₀²π ∫₀ᵃ r dr dθ = ∫₀²π (a²/2) dθ = πa², confirming the area formula you know from geometry.
