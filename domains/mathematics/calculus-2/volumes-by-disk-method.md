---
id: volumes-by-disk-method
title: Volumes by Disk Method
domain: mathematics
course: calculus-2
prerequisites:
  - id: area-between-curves
    type: hard
builds-toward:
  - volumes-by-washer-method
tags: [integration, applications, volumes, revolution]
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

## Explainer

You've already computed areas between curves by slicing a region into infinitely thin vertical strips and integrating their areas. The disk method extends this idea into three dimensions by rotating those strips around an axis. Each thin vertical strip, when rotated, sweeps out a disk. The disk's radius is the height of the strip (the function value f(x)), and its thickness is dx. The volume of each thin disk is π·[radius]²·[thickness] = π·[f(x)]²·dx. Integrating these disk volumes from a to b gives the total volume of the solid.

The formula V = π∫ₐᵇ [f(x)]² dx is simply the area formula πr² applied infinitesimally and then accumulated. Think of a solid formed by revolving y = √x around the x-axis from 0 to 4. At each position x, the radius of the cross-sectional disk is √x, so each disk has area π(√x)² = πx. Integrating: V = π∫₀⁴ x dx = π·[x²/2]₀⁴ = 8π. The solid looks like a bowl — narrow at the left, wide at the right — and the integral captures this because the radius (and hence each disk's area) increases with x.

The most common setup errors come from not clearly identifying the **radius function** before writing the integral. The radius is always the perpendicular distance from the axis of revolution to the curve. When revolving around the x-axis, the radius is |f(x)|. When revolving around the y-axis, integrate with respect to y and use the radius |g(y)| where g is x as a function of y. When revolving around a horizontal line y = k, the radius becomes |f(x) - k|. In every case, sketch the region first, identify which direction you're stacking disks, and write down the radius explicitly before forming the integral.

The disk method is the simplest case of a general principle: to find the volume of a solid, integrate its cross-sectional areas. When cross-sections are disks (circles), you get πr². When there's a gap between the curve and the axis — a hole through the center of each cross-section — you'll need the **washer method**, which subtracts the inner circle's area from the outer. But the logic is identical: area of cross-section times infinitesimal thickness, integrated along the axis of revolution.
