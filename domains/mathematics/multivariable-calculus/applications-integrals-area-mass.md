---
id: applications-integrals-area-mass
title: 'Applications of Double Integrals: Area, Mass, and Moments'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-general-regions
  type: hard
builds-toward:
- triple-integrals-cartesian
tags:
- applications
- area
- mass
- moments
- centroid
stage: formal-systems
status: validated
---

# Applications of Double Integrals: Area, Mass, and Moments

## Core Idea
Double integrals compute: area as ∬_D dA, mass as ∬_D ρ(x, y) dA (with density ρ), moments M_x = ∬_D y ρ(x, y) dA and M_y = ∬_D x ρ(x, y) dA, and center of mass (x̄, ȳ) = (M_y/M, M_x/M).

## Questions

```yaml
- question: "A thin plate covers region D with density function ρ(x, y) = 2 + x. Which integral gives the total mass?"
  type: multiple-choice
  options:
    - "∬_D dA"
    - "∬_D (2 + x) dA"
    - "∬_D x · (2 + x) dA"
    - "∬_D (2 + x)² dA"
  answer: 1
  explanation: "Mass is the integral of density over area: M = ∬_D ρ(x, y) dA. You weight each infinitesimal area element dA by the local density at that point before summing. Option A computes area (density = 1 everywhere). Option C would compute M_y (the moment about the y-axis, weighting by x). Option D has no physical interpretation here."

- question: "A thin triangular plate has uniform density ρ. You compute its center of mass and get (x̄, ȳ). You then double the density everywhere uniformly to 2ρ. What happens to the center of mass?"
  type: multiple-choice
  options:
    - "It shifts toward the geometric centroid since density is now dominant"
    - "It stays at exactly (x̄, ȳ) — uniform scaling of density does not change the balance point"
    - "It moves to the center of the bounding rectangle"
    - "It becomes undefined because total mass changes"
  answer: 1
  explanation: "Center of mass is (M_y/M, M_x/M). When density is scaled uniformly by a constant c, every integral scales by the same c — both the moments and the total mass. The ratio M_y/M and M_x/M are unchanged. The center of mass depends only on the *distribution* of mass, not on how much total mass there is. Uniform scaling preserves the distribution."

- question: "Computing the area of a region D using a double integral requires integrating some function related to the geometry of the region, such as distance from the origin."
  type: true-false
  answer: false
  explanation: "Area is computed by integrating the constant function f = 1: Area = ∬_D dA. You are simply summing infinitesimal area elements with no weighting. The 'function' is literally 1. Distance, curvature, or other geometric properties are irrelevant. This is the baseline case: area is what you get before you introduce any weighting function."

- question: "For a plate with non-uniform density, the center of mass can fall in a region of low density, or even outside the plate entirely, depending on the shape and density distribution."
  type: true-false
  answer: true
  explanation: "The center of mass is a weighted average of position across the entire mass distribution — not simply the location of maximum density. For an L-shaped region with high density in one arm and low density in the other, the balance point can fall outside the high-density region. For a ring-shaped region with uniform density, the center of mass is in the center hole — outside the material entirely. The balance point depends on the whole distribution, not any local maximum."

- question: "What is the physical interpretation of the moments M_x and M_y, and how are they used to find the center of mass?"
  type: short-answer
  answer: "M_x = ∬_D y·ρ(x,y) dA measures how mass is distributed relative to the x-axis — each mass element is weighted by its y-distance from the x-axis, so mass far from the axis contributes more. M_y = ∬_D x·ρ(x,y) dA does the same for the y-axis. The center of mass is x̄ = M_y/M and ȳ = M_x/M — the position where all the mass could be concentrated to produce the same rotational tendency (torque) around any axis as the original distribution."
  explanation: "The notation is a common source of confusion: M_x uses y as the integrand (it measures the 'moment about the x-axis,' which depends on y-distance), and M_y uses x. Keeping the physical meaning in mind — moment about an axis depends on perpendicular distance from that axis — prevents subscript mix-ups."
```

## Explainer

You already know how to compute double integrals over general regions — summing up f(x, y) dA across a 2D domain D. Now you're applying that machinery to concrete physical and geometric quantities. The key insight is that **area**, **mass**, and **center of mass** are all double integrals; what changes is which function f(x, y) you integrate.

**Area** is the simplest case: ∬_D dA means integrating the constant function f = 1. You're summing infinitesimal area elements, which trivially yields total area. This is useful when D is described implicitly — "the region bounded by y = x² and y = x" — where direct integration is easier than finding a geometric formula. In polar coordinates, dA = r dr dθ, and many regions defined by r = g(θ) yield elegant area integrals.

**Mass** introduces a **density function** ρ(x, y) measuring mass per unit area. A thin plate whose material is denser near the center and lighter at the edges has total mass M = ∬_D ρ(x, y) dA — you're weighting each area element by the local density before summing. When ρ is constant, this reduces to ρ · Area(D), recovering the elementary formula. When ρ varies, the integral accounts for the distribution.

The **moments** M_x and M_y measure how mass is distributed relative to each coordinate axis. M_x = ∬_D y ρ(x, y) dA weights mass by its distance from the x-axis, and M_y = ∬_D x ρ(x, y) dA weights by distance from the y-axis. The **center of mass** (x̄, ȳ) = (M_y/M, M_x/M) is the single point where you could concentrate all the mass and preserve the same rotational behavior around any axis. Mechanically, it's the balance point of the plate: if you tried to support the plate on a pin at (x̄, ȳ), it would rest level. For a uniform plate (constant ρ), the center of mass equals the geometric centroid — a property of the shape alone, independent of density.
