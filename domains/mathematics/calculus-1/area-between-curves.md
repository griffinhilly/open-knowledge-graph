---
id: area-between-curves
title: Area Between Curves
domain: mathematics
course: calculus-1
prerequisites:
  - id: fundamental-theorem-of-calculus-part-2
    type: hard
  - id: u-substitution
    type: soft
builds-toward:
  - volumes-by-disk-method
  - volumes-by-washer-method
tags: [integration, applications, area]
stage: formal-systems
status: validated
---

# Area Between Curves

## Core Idea
The area between two curves y = f(x) and y = g(x) from x = a to x = b is the integral from a to b of |f(x) - g(x)| dx. In practice, you determine which function is on top in each subinterval and integrate (top - bottom). For curves better described as functions of y, you can integrate with respect to y using (right - left). This is the first major application of the definite integral beyond simple area under a curve.

## How It's Best Learned
Start by graphing the curves and finding intersection points. Set up the integral as (top - bottom) dx or (right - left) dy. Practice with cases requiring multiple integrals (when the curves cross). Emphasize the importance of sketching the region first.

## Common Misconceptions
- Integrating f(x) - g(x) without checking which is on top (can get a negative area).
- Missing intersection points and using wrong bounds.
- Not splitting the integral when the top and bottom curves switch within the interval.

## Explainer

The definite integral as you have learned it computes the net signed area between a curve y = f(x) and the x-axis. The area between two curves extends this idea by replacing the x-axis with a second curve. The region bounded by y = f(x) on top and y = g(x) on the bottom, from x = a to x = b, has area equal to the integral of [f(x) − g(x)] dx from a to b. The subtraction removes the area "below" g(x), leaving only the vertical gap between the two curves. When f(x) ≥ g(x) throughout [a, b], this difference is always non-negative and the integral gives the correct positive area.

The hardest part of most problems is the setup, not the integration itself. First, **sketch both curves** and identify the bounded region. Find the **intersection points** by setting f(x) = g(x) and solving for x — these become your limits of integration if the problem does not specify them. Then determine which curve is on top in each subinterval. If the curves cross within your interval, you must split the integral at each crossing, computing ∫(top − bottom) dx separately in each piece and adding the results. Omitting a split and integrating f − g across a crossing produces cancellation — positive and negative contributions partially cancel — giving an answer smaller than the true area.

Sometimes a region is more naturally described with x and y swapped. Consider the region between x = y² and x = y + 2. If you integrate with respect to x, you would need to solve for y as a function of x, producing square roots and requiring two separate integrals. Instead, integrate with respect to y: find intersections from y² = y + 2 (giving y = −1 and y = 2), then integrate [(y + 2) − y²] dy from −1 to 2, where (y + 2) is the rightmost curve and y² is the leftmost. The principle is identical — **(right − left) dy** instead of (top − bottom) dx — with the orientation rotated 90°.

This topic is not just an endpoint; it is the foundation for volumes of revolution. When you revolve a region about an axis to build a solid, the cross-sectional slices are disks or washers, and the "radius" of each washer is determined by the distance between two curves — precisely what you integrate here. Mastering the setup logic of area between curves makes the reasoning behind volumes of revolution feel like a natural extension rather than a new technique.
