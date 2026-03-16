---
id: sector-area
title: Sector Area
domain: mathematics
course: geometry
prerequisites:
  - id: arc-length-circles
    type: hard
  - id: central-angles-and-arcs
    type: hard
builds-toward:
  - radian-measure
tags: [circles, sector-area, proportionality]
stage: abstract-reasoning
status: validated
---

# Sector Area

## Core Idea
A sector is the "pie slice" region bounded by two radii and an arc. The area of a sector with central angle theta degrees in a circle of radius r is (theta/360) * pi * r^2. Like arc length, sector area is a proportional part of the total circle area. The relationship between arc length and sector area parallels the relationship between circumference and area.

## How It's Best Learned
Derive by proportional reasoning: the sector is the same fraction of the circle's area as the central angle is of 360. Practice computing sector areas. Give compound problems involving sectors and triangles (e.g., area of a segment = sector area minus triangle area).

## Common Misconceptions
- Confusing sector (the region) with arc (the curve).
- Using diameter instead of radius in pi*r^2.
- Confusing the arc length formula with the sector area formula.
- Forgetting to convert to a fraction of 360 when the angle is given.

## Explainer

You already know two things about circles: arc length tells you how long a curved piece of the boundary is, and central angles measure how wide the "opening" of that arc is. A **sector** adds a new element — it's the filled-in region, the entire "pie slice" bounded by two radii and the arc between them. Sector area asks not "how long is the crust?" but "how much pie is on the plate?"

The key insight is proportional reasoning, the same reasoning you used for arc length. A full circle has area πr². A sector with central angle θ (in degrees) is just the fraction θ/360 of the full circle — the same fraction you used for arc length. So sector area = (θ/360) · πr². Notice the parallel: arc length = (θ/360) · 2πr, and sector area = (θ/360) · πr². Both are just proportional parts of their respective whole-circle measurements. If the angle is 90°, you get a quarter of the circle; if it's 180°, a semicircle; if it's 60°, one-sixth of the circle, and so on.

The common misconceptions all trace back to mixing up the two formulas. Arc length involves the circumference 2πr (one factor of r), while sector area involves the full area πr² (two factors of r). The extra factor of r comes from the fact that area is two-dimensional while length is one-dimensional. A concrete check: a sector with θ = 60° in a circle of radius 3 has arc length (60/360)(2π·3) = π, and area (60/360)(π·9) = 3π/2. Notice the units reinforce the dimension: arc length is in the same unit as r, while area is in square units.

One elegant application extends this: the **area of a circular segment** (the region between a chord and its arc) equals the sector area minus the area of the triangle formed by the two radii and the chord. So sectors aren't just an isolated formula — they're a building block for more complex area calculations. When you encounter radian measure later, the sector formula becomes even cleaner: area = (1/2)r²θ, where θ is in radians, which is one reason radians are the "natural" unit for circle problems.
