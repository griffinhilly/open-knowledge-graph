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
status: draft
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
