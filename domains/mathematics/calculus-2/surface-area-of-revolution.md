---
id: surface-area-of-revolution
title: Surface Area of Revolution
domain: mathematics
course: calculus-2
prerequisites:
  - id: arc-length
    type: hard
builds-toward: []
tags: [integration, applications, surface-area, revolution]
stage: formal-systems
status: validated
---

# Surface Area of Revolution

## Core Idea
When a curve y = f(x) is revolved about the x-axis, the surface area is S = integral from a to b of 2*pi*f(x) * sqrt(1 + (f'(x))^2) dx. The formula multiplies the arc length element by the circumference of the circle traced by each point (2*pi*r, where r = f(x) for revolution about the x-axis). For revolution about the y-axis, the radius term changes accordingly.

## How It's Best Learned
Derive from the arc length formula by adding the circumference factor. Practice with curves that yield tractable integrals. Compare with volume of revolution formulas to see the parallel structure.

## Common Misconceptions
- Confusing surface area with volume of revolution (surface area uses the arc length element, volume uses dx or dy).
- Using the wrong radius of revolution (which axis is the curve revolving around?).
- Forgetting the 2*pi factor.

## Explainer

From **arc length**, you know that the length of a curve y = f(x) from a to b is ∫√(1 + (f'(x))²) dx — a result that comes from adding up infinitesimally small hypotenuse segments along the curve. Surface area of revolution builds directly on this idea by asking: if you spin that curve around an axis, what is the area of the resulting surface?

Picture a thin strip of the curve at position x, with arc length element ds = √(1 + (f'(x))²) dx. When you rotate this strip around the x-axis, it sweeps out a thin band, like a ring cut from a cone or cylinder. The area of that ring is its circumference times its width: 2π · r · ds, where r is the distance from the strip to the x-axis. For revolution about the x-axis, r = f(x) (the height of the curve at that point). Integrating these ring areas gives **S = ∫₍ₐ₎^b 2π f(x) √(1 + (f'(x))²) dx**. The 2πf(x) term is the circumference of the circle traced by the point (x, f(x)), and the √(1 + (f'(x))²) dx term is the arc length element from your prerequisite.

The key distinction from volume formulas is the *type of geometric element* being accumulated. **Volume** of revolution accumulates cross-sectional *areas* (disks of area πr²) — you're stacking up filled circles. **Surface area** accumulates the *rim* of those circles — you're wrapping tape around the outside. This is why surface area uses the arc length element (measuring along the curve's slope) while volume uses a simple dx (measuring straight horizontal slices). A sphere of radius R provides a useful check: the formula gives S = 4πR², matching the known result.

For revolution about the **y-axis**, the logic is identical but the radius changes. If you're revolving y = f(x) about the y-axis, the distance from a point on the curve to the y-axis is x (not f(x)), so the formula becomes S = ∫₍ₐ₎^b 2πx √(1 + (f'(x))²) dx. Alternatively, you can express x as a function of y and integrate with respect to y. The structure is always the same: (2π · radius) · (arc length element), integrated over the parameter of your choice. Always identify the axis of revolution first, then determine what expression gives the radius of each circular ring.
