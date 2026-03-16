---
id: triple-integrals
title: Triple Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
builds-toward:
- triple-integrals-cylindrical
- triple-integrals-spherical
tags:
- triple-integral
- volume
stage: formal-systems
status: draft
---

# Triple Integrals in Cartesian Coordinates

## Core Idea
The triple integral ∭_W f(x,y,z) dV gives signed volume or accumulates density. In Cartesian coordinates, dV = dx dy dz, and the integral becomes an iterated integral with three steps.

## Explainer

You have already computed double integrals by slicing a two-dimensional region into strips and integrating layer by layer. A **triple integral** extends this process one dimension further: you slice a three-dimensional solid W into thin slabs, then into columns, then into small box-shaped pieces of volume dV = dx dy dz. The triple iterated integral ∫∫∫ f(x,y,z) dx dy dz integrates out one variable at a time, treating all other variables as constants during each step. The three integrations correspond to three nested loops: innermost first, outermost last.

The geometric meaning depends on f. When f(x,y,z) = 1, the triple integral ∭_W 1 dV equals the **volume** of W — every tiny box contributes its volume 1 · dx dy dz, and summing over W gives the total. When f represents mass density (mass per unit volume), ∭_W f dV equals total mass. When f represents charge density, the integral gives total charge. Triple integrals are the natural tool whenever a quantity is distributed continuously through a three-dimensional region and you want the total.

Setting up the limits requires describing the region W precisely. For a rectangular box a ≤ x ≤ b, c ≤ y ≤ d, e ≤ z ≤ g, all six limits are constants and the integral is straightforward. For a non-rectangular solid — say the region above the xy-plane, below z = 4 - x² - y², for x and y inside the unit square — the limits interact: z runs from 0 to 4 - x² - y², while x and y have constant limits. The inner integral (in z) is computed first with x and y fixed, producing a function of x and y; then the double integral over x and y finishes the calculation.

Choosing the order of integration is where the real skill lies. The same solid W can be described with any of six orderings (dx dy dz, dx dz dy, dy dx dz, and so on), and the correct limits differ for each. A solid described naturally as "for each (x, y) in region D, z runs from the lower surface to the upper surface" calls for integrating z first (inner), then (x, y) over D. If the solid is instead described by cross-sections perpendicular to the z-axis — "at height z, the cross-section is region D(z)" — then integrate over x and y first (inner and middle), z last (outer). Drawing the solid and identifying its natural description is always the first step before writing any integral limits.
