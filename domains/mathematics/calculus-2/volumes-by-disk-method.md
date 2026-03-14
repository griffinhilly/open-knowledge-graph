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
