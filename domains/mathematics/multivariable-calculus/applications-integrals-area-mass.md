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
status: draft
---

# Applications of Double Integrals: Area, Mass, and Moments

## Core Idea
Double integrals compute: area as ∬_D dA, mass as ∬_D ρ(x, y) dA (with density ρ), moments M_x = ∬_D y ρ(x, y) dA and M_y = ∬_D x ρ(x, y) dA, and center of mass (x̄, ȳ) = (M_y/M, M_x/M).

## Explainer

You already know how to compute double integrals over general regions — summing up f(x, y) dA across a 2D domain D. Now you're applying that machinery to concrete physical and geometric quantities. The key insight is that **area**, **mass**, and **center of mass** are all double integrals; what changes is which function f(x, y) you integrate.

**Area** is the simplest case: ∬_D dA means integrating the constant function f = 1. You're summing infinitesimal area elements, which trivially yields total area. This is useful when D is described implicitly — "the region bounded by y = x² and y = x" — where direct integration is easier than finding a geometric formula. In polar coordinates, dA = r dr dθ, and many regions defined by r = g(θ) yield elegant area integrals.

**Mass** introduces a **density function** ρ(x, y) measuring mass per unit area. A thin plate whose material is denser near the center and lighter at the edges has total mass M = ∬_D ρ(x, y) dA — you're weighting each area element by the local density before summing. When ρ is constant, this reduces to ρ · Area(D), recovering the elementary formula. When ρ varies, the integral accounts for the distribution.

The **moments** M_x and M_y measure how mass is distributed relative to each coordinate axis. M_x = ∬_D y ρ(x, y) dA weights mass by its distance from the x-axis, and M_y = ∬_D x ρ(x, y) dA weights by distance from the y-axis. The **center of mass** (x̄, ȳ) = (M_y/M, M_x/M) is the single point where you could concentrate all the mass and preserve the same rotational behavior around any axis. Mechanically, it's the balance point of the plate: if you tried to support the plate on a pin at (x̄, ȳ), it would rest level. For a uniform plate (constant ρ), the center of mass equals the geometric centroid — a property of the shape alone, independent of density.
