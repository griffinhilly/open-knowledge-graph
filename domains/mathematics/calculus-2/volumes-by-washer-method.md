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
- id: surface-area-of-revolution
  type: soft
builds-toward:
- volumes-by-shell-method
tags:
- integration
- applications
- volumes
- revolution
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

## Questions

```yaml
- question: "A region between y = 3 and y = 1 (where both are above the x-axis) is revolved about the x-axis. Which expression gives the area of a washer cross-section?"
  type: multiple-choice
  options:
    - "π(3 − 1)² = 4π"
    - "π(3² − 1²) = 8π"
    - "π(3 + 1)² = 16π"
    - "π · 3² = 9π"
  answer: 1
  explanation: "The washer is a disk of radius R = 3 with a disk of radius r = 1 removed from its center. Its area is the difference of the two circular areas: πR² − πr² = π(9 − 1) = 8π. The most common error is computing π(R − r)² = π(4) = 4π — this squares the difference rather than taking the difference of squares. π(R−r)² ≠ π(R²−r²) unless r = 0."

- question: "The region between y = x² and y = x (where x² ≤ x for 0 ≤ x ≤ 1) is revolved about the axis y = −1. What are the outer and inner radii for the washer at position x?"
  type: multiple-choice
  options:
    - "R = x, r = x²"
    - "R = x + 1, r = x² + 1"
    - "R = x − 1, r = x² − 1"
    - "R = 1 − x, r = 1 − x²"
  answer: 1
  explanation: "The axis is y = −1. The outer radius is the distance from the axis to the farther curve (y = x, the upper curve): R = x − (−1) = x + 1. The inner radius is the distance to the closer curve (y = x²): r = x² − (−1) = x² + 1. When revolving about an axis other than y = 0, you must express each radius as the distance from the axis, not the raw y-value. Forgetting to add 1 (the axis offset) to both radii is the most common setup error."

- question: "The washer method can be viewed as computing the volume of a large solid of revolution and subtracting the volume of a smaller solid of revolution that corresponds to the hollow interior."
  type: true-false
  answer: true
  explanation: "This is the conceptual foundation of the washer method. When you revolve the region between two curves, you sweep out the volume the outer curve would create (the full disk) minus the volume the inner curve would create (the hole). Integrating πR²(x) gives the outer solid's volume; subtracting ∫πr²(x) removes the hollow interior. Writing V = ∫π(R² − r²) dx is just doing both in one step."

- question: "If f(x) > g(x) > 0 and you revolve the region between them about y = 0, the washer volume formula V = ∫π(f − g)² dx is correct."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception in the washer method. The correct formula is V = ∫π(f² − g²) dx, not V = ∫π(f − g)² dx. The difference of squares ≠ the square of the difference: f² − g² = (f+g)(f−g), while (f−g)² = f² − 2fg + g². Using (R−r)² instead of (R²−r²) gives a wrong volume."

- question: "Explain why, when revolving about the axis y = k (where k ≠ 0), you must adjust the radii rather than using the raw y-values of the boundary curves."
  type: short-answer
  answer: "The radius of each cross-sectional ring must be the perpendicular distance from the axis of revolution to the curve, not the curve's y-value. When the axis is y = k, the distance from the axis to a curve at height y is |y − k|, not y. Using raw y-values only works when k = 0 because then distance = |y − 0| = y (for y > 0)."
  explanation: "The formula π(R² − r²) requires R and r to be radii — distances from the center of each circular cross-section to its boundary. The axis of revolution is that center. If the axis is y = 2 and a curve is at y = 5, the ring's outer radius is 5 − 2 = 3, not 5. Drawing the cross-section explicitly and labeling the distances from the axis (not from y = 0) is the reliable way to set up these problems correctly."
```

## Explainer

You already know the disk method: revolve a region bounded between a curve and the axis, slice perpendicular to the axis, and each cross-section is a disk of area πR². The washer method handles the more general situation where the region does not touch the axis — instead, it lies between two curves, and revolving it produces a solid with a hole through the middle, like a hollow cylinder.

The key insight is that a **washer** is just a big disk with a smaller disk removed from its center. Its area is the difference of the two circular areas: π R² − π r² = π(R² − r²), where R is the outer radius and r is the inner radius. Integrating this cross-sectional area gives the volume: V = ∫ₐᵇ π(R(x)² − r(x)²) dx. This is identical to subtracting the volume of the inner solid from the volume of the outer solid — the region you actually swept out minus the hollow interior you did not.

Setting up the radii correctly is the main challenge. For revolution about the x-axis, R(x) is the distance from the axis to the farther curve (whichever has larger |y|), and r(x) is the distance from the axis to the closer curve. If y = f(x) lies above y = g(x) ≥ 0, then R(x) = f(x) and r(x) = g(x). If the region is between curves on opposite sides of the axis, the analysis requires care, but the area formula still subtracts inner from outer.

Revolution about a non-standard axis — say y = 2 instead of y = 0 — shifts both radii. If y = f(x) is the upper curve, its distance from the axis y = 2 is |f(x) − 2|, not just f(x). Always express R and r as distances from the axis, not raw y-values. You can also revolve about a vertical axis (x = k) and integrate with respect to y, applying the same formula with y as the variable. The strategy in either case is identical: identify the outer and inner boundary, write their distances from the axis, substitute into π(R² − r²), and integrate over the appropriate interval. Drawing the cross-section as an actual washer — labeling both radii — before writing any formula will prevent the most common setup errors.
