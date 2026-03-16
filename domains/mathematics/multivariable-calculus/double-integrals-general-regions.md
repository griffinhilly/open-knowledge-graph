---
id: double-integrals-general-regions
title: Double Integrals over General Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian-coordinates
  type: hard
builds-toward:
- applications-integrals-area-mass
tags:
- double-integrals
- integration-bounds
- general-regions
stage: formal-systems
status: draft
---

# Double Integrals over General Regions

## Core Idea
For a region D described as {(x, y) : a ≤ x ≤ b, g₁(x) ≤ y ≤ g₂(x)}, the double integral ∬_D f(x, y) dA = ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x, y) dy dx. Describing regions correctly (both as Type I and Type II) allows choosing the easier integration order.

## Explainer

From your work with double integrals over rectangles, you know how to set up an iterated integral: hold one variable fixed, integrate over the other, then integrate the result. The rectangle was easy because the limits on each variable were constants — x runs from a to b, y runs from c to d, and neither range depends on the other. Real integration problems rarely have this convenience. Most regions of interest — triangles, disks, the area between two curves — have variable limits, and that is exactly what double integrals over general regions handle.

The key concept is the region description. A **Type I region** (also called x-simple) is bounded on the left and right by constants a and b, and above and below by functions of x: g₁(x) ≤ y ≤ g₂(x). The double integral over a Type I region becomes ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x, y) dy dx. You integrate with respect to y first (using the variable limits that depend on x), then with respect to x (using constant limits). Concretely: for each fixed x-slice of the region, integrate f in the y-direction between the two boundary curves.

A **Type II region** (y-simple) reverses the roles: constant limits on y, functions of y for x. The same region can often be described both ways. The strategy skill is recognizing which description leads to an integral you can actually compute. If integrating in x first simplifies the inner integrand, use a Type II description; if integrating in y first does, use Type I. This **order of integration reversal** is a practical tool: sometimes one order produces an antiderivative you can find, while the other produces something like ∫ e^(x²) dx, which has no closed form. Reversing the order (and adjusting the limits to match the new description of the same region) can unlock the problem.

The setup step — drawing and describing the region correctly — is where most errors occur. Before writing any integral, sketch the region, identify whether it is simpler to describe as Type I or Type II, find the intersection points of the boundary curves (these become your constant outer limits), and write the variable inner limits as functions of the outer variable. A mislabeled boundary or a swapped inequality in the limits will invalidate the entire integral, even if the antiderivative computation is perfect.
