---
id: volumes-by-washer-method
title: Volumes by Washer Method
domain: mathematics
course: calculus-2
prerequisites:
  - id: volumes-by-disk-method
    type: hard
  - id: area-between-curves
    type: hard
builds-toward:
  - volumes-by-shell-method
tags: [integration, applications, volumes, revolution]
stage: formal-systems
status: validated
---

# Volumes by Washer Method

## Core Idea
When the region between two curves y = f(x) and y = g(x) is revolved about an axis, each cross-section is a washer (annular disk) with outer radius R(x) and inner radius r(x). The volume is V = integral from a to b of pi * (R^2 - r^2) dx. This generalizes the disk method to regions that do not touch the axis of revolution, creating a hollow center.

## How It's Best Learned
Start with disk method understanding, then introduce the "hole" by revolving a region between two curves. Carefully identify the outer and inner radii for each problem. Practice with revolution about horizontal and vertical axes, and about axes other than x = 0 or y = 0.

## Common Misconceptions
- Computing pi*(R - r)^2 instead of pi*(R^2 - r^2): the difference of squares is not the square of the difference.
- Swapping the outer and inner radii.
- Not adjusting the radii when revolving about an axis other than x = 0 or y = 0.

## Explainer

You already know the disk method: revolve a region bounded between a curve and the axis, slice perpendicular to the axis, and each cross-section is a disk of area πR². The washer method handles the more general situation where the region does not touch the axis — instead, it lies between two curves, and revolving it produces a solid with a hole through the middle, like a hollow cylinder.

The key insight is that a **washer** is just a big disk with a smaller disk removed from its center. Its area is the difference of the two circular areas: π R² − π r² = π(R² − r²), where R is the outer radius and r is the inner radius. Integrating this cross-sectional area gives the volume: V = ∫ₐᵇ π(R(x)² − r(x)²) dx. This is identical to subtracting the volume of the inner solid from the volume of the outer solid — the region you actually swept out minus the hollow interior you did not.

Setting up the radii correctly is the main challenge. For revolution about the x-axis, R(x) is the distance from the axis to the farther curve (whichever has larger |y|), and r(x) is the distance from the axis to the closer curve. If y = f(x) lies above y = g(x) ≥ 0, then R(x) = f(x) and r(x) = g(x). If the region is between curves on opposite sides of the axis, the analysis requires care, but the area formula still subtracts inner from outer.

Revolution about a non-standard axis — say y = 2 instead of y = 0 — shifts both radii. If y = f(x) is the upper curve, its distance from the axis y = 2 is |f(x) − 2|, not just f(x). Always express R and r as distances from the axis, not raw y-values. You can also revolve about a vertical axis (x = k) and integrate with respect to y, applying the same formula with y as the variable. The strategy in either case is identical: identify the outer and inner boundary, write their distances from the axis, substitute into π(R² − r²), and integrate over the appropriate interval. Drawing the cross-section as an actual washer — labeling both radii — before writing any formula will prevent the most common setup errors.
