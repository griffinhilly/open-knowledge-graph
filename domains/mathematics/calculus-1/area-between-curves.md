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
