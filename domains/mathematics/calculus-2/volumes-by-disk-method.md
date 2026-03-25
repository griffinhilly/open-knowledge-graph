---
id: volumes-by-disk-method
title: Volumes by Disk Method
domain: mathematics
course: calculus-2
prerequisites:
- id: area-between-curves
  type: hard
- id: surface-area-of-revolution
  type: soft
builds-toward:
- volumes-by-washer-method
tags:
- integration
- applications
- volumes
- revolution
stage: formal-systems
status: validated
---
# Volumes by Disk Method

## Core Idea
When a region bounded by y = f(x) and the x-axis is revolved about the x-axis, the resulting solid's volume is V = integral from a to b of pi * [f(x)]^2 dx. Each cross-section perpendicular to the axis of revolution is a disk with radius f(x). This is the simplest volume-of-revolution method and the natural starting point for understanding solids of revolution.

## How It's Best Learned
Visualize the solid by sketching the region and imagining rotation. Identify the radius of each disk. Set up and evaluate the integral for simple curves (e.g., revolving y = sqrt(x) about the x-axis). Practice both revolution about the x-axis and about the y-axis.

## Common Misconceptions
- Forgetting to square the radius function (volume uses r^2, not r).
- Forgetting the pi factor.
- Using the disk method when there is a gap between the curve and the axis of revolution (washer method needed).

## Questions

```yaml
- question: "The region bounded by y = x² and the x-axis from x = 0 to x = 2 is revolved about the x-axis. Which integral correctly gives the volume?"
  type: multiple-choice
  options:
    - "π ∫₀² x² dx"
    - "π ∫₀² x⁴ dx"
    - "∫₀² x² dx"
    - "π ∫₀² 2x dx"
  answer: 1
  explanation: "The disk method gives V = π ∫ₐᵇ [f(x)]² dx. Here f(x) = x², so [f(x)]² = (x²)² = x⁴. The most common error is forgetting to square the radius function — using x² instead of x⁴. The radius of each disk is f(x) = x², and volume requires πr², so squaring is essential. Forgetting π is another frequent mistake, but option C also drops the squaring."

- question: "A region is bounded by y = 3 and the x-axis from x = 0 to x = 5, and revolved about the line y = 3 (not the x-axis). What is the radius of each disk cross-section?"
  type: multiple-choice
  options:
    - "3, because the function value is 3"
    - "0, because the curve lies on the axis of revolution"
    - "The radius varies with x — it equals f(x) − 3"
    - "5, because the region extends to x = 5"
  answer: 1
  explanation: "When the curve y = 3 is revolved about the axis y = 3, the curve lies exactly on the axis of revolution. Every point on the curve has zero distance from the axis, so each disk has radius 0 — the solid is a degenerate flat disk with zero volume. The key principle: the radius is always the perpendicular distance from the axis of revolution to the curve, which here is |f(x) − 3| = |3 − 3| = 0. This is the situation where a washer method with inner radius > 0 would be needed for a different curve configuration."

- question: "If the region between y = f(x) and the x-axis has a gap — meaning the curve does not touch the x-axis — the disk method still correctly gives the volume of the solid formed by revolving this region about the x-axis."
  type: true-false
  answer: false
  explanation: "When there is a gap between the curve and the axis of revolution, each cross-section is not a solid disk but an annulus (washer) — a disk with a hole through the center. The washer method is required: V = π ∫ₐᵇ ([outer radius]² − [inner radius]²) dx. Applying the disk method in this situation would incorrectly include volume in the hole that doesn't exist in the actual solid."

- question: "The volume formula for the disk method, V = π ∫ₐᵇ [f(x)]² dx, requires squaring f(x) because we are computing areas of circular cross-sections, not lengths."
  type: true-false
  answer: true
  explanation: "Each thin cross-section perpendicular to the axis is a circle with radius f(x). The area of that circle is πr² = π[f(x)]². Multiplying by the infinitesimal thickness dx and integrating accumulates these circular areas into volume. The squaring is exactly the same πr² formula for circular area, applied infinitesimally. This is why forgetting the square is the most conceptually damaging error — it would be computing something proportional to arc length, not area."

- question: "Explain in terms of circular cross-sections why the disk method formula is V = π ∫ₐᵇ [f(x)]² dx and not V = ∫ₐᵇ f(x) dx."
  type: short-answer
  answer: "When a region is revolved about the x-axis, each thin vertical strip of width dx sweeps out a disk. The disk's radius is f(x) — the height of the strip — and its thickness is dx. The volume of that thin disk is π·(radius)²·(thickness) = π[f(x)]²dx. The formula ∫f(x)dx would compute area of the original 2D region, not volume. The squaring comes from the cross-sectional area being πr², and the π is part of the circle area formula — both are essential."
  explanation: "The intuition is that area accumulates lengths (∫f(x)dx), while volume accumulates areas (∫π[f(x)]²dx). The transition from 2D to 3D adds one power of the radius — it's the difference between a line segment and the circle it sweeps when rotated."
```

## Explainer

You've already computed areas between curves by slicing a region into infinitely thin vertical strips and integrating their areas. The disk method extends this idea into three dimensions by rotating those strips around an axis. Each thin vertical strip, when rotated, sweeps out a disk. The disk's radius is the height of the strip (the function value f(x)), and its thickness is dx. The volume of each thin disk is π·[radius]²·[thickness] = π·[f(x)]²·dx. Integrating these disk volumes from a to b gives the total volume of the solid.

The formula V = π∫ₐᵇ [f(x)]² dx is simply the area formula πr² applied infinitesimally and then accumulated. Think of a solid formed by revolving y = √x around the x-axis from 0 to 4. At each position x, the radius of the cross-sectional disk is √x, so each disk has area π(√x)² = πx. Integrating: V = π∫₀⁴ x dx = π·[x²/2]₀⁴ = 8π. The solid looks like a bowl — narrow at the left, wide at the right — and the integral captures this because the radius (and hence each disk's area) increases with x.

The most common setup errors come from not clearly identifying the **radius function** before writing the integral. The radius is always the perpendicular distance from the axis of revolution to the curve. When revolving around the x-axis, the radius is |f(x)|. When revolving around the y-axis, integrate with respect to y and use the radius |g(y)| where g is x as a function of y. When revolving around a horizontal line y = k, the radius becomes |f(x) - k|. In every case, sketch the region first, identify which direction you're stacking disks, and write down the radius explicitly before forming the integral.

The disk method is the simplest case of a general principle: to find the volume of a solid, integrate its cross-sectional areas. When cross-sections are disks (circles), you get πr². When there's a gap between the curve and the axis — a hole through the center of each cross-section — you'll need the **washer method**, which subtracts the inner circle's area from the outer. But the logic is identical: area of cross-section times infinitesimal thickness, integrated along the axis of revolution.
