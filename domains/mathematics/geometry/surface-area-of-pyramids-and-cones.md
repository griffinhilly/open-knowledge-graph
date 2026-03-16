---
id: surface-area-of-pyramids-and-cones
title: Surface Area of Pyramids and Cones
domain: mathematics
course: geometry
prerequisites:
  - id: surface-area-of-prisms
    type: soft
  - id: pythagorean-theorem
    type: hard
  - id: area-of-regular-polygons
    type: soft
builds-toward:
  - volume-of-pyramids-and-cones
tags: [3d-geometry, surface-area, pyramids, cones, slant-height]
stage: abstract-reasoning
status: validated
---

# Surface Area of Pyramids and Cones

## Core Idea
A pyramid has a polygon base and triangular lateral faces meeting at an apex. Its surface area is the base area plus the lateral area. For a regular pyramid, the lateral area is (1/2) * perimeter * slant height. A cone is the circular analog: SA = pi*r^2 + pi*r*l, where l is the slant height. The slant height, vertical height, and radius form a right triangle (related by the Pythagorean theorem).

## How It's Best Learned
Use nets to visualize the lateral surface. For cones, show that the lateral surface unrolls to a sector of a larger circle. Practice computing slant height from height and radius using the Pythagorean theorem. Work problems in both directions: given surface area, find missing dimensions.

## Common Misconceptions
- Confusing slant height with vertical height.
- Forgetting to include the base in the total surface area.
- For cones, using the height instead of the slant height in the lateral area formula.

## Explainer

From your work on prisms, you know the strategy for surface area: imagine cutting the solid apart and flattening it into a **net**, then add up the areas of all the flat pieces. That same strategy applies to pyramids and cones — the only new challenge is figuring out the shapes you get when you unfold the curved or triangular sides.

A **pyramid** has a polygon base and triangular lateral faces that meet at a point called the **apex**. When you unfold a regular pyramid (where the base is a regular polygon and the apex sits directly above its center), each lateral face is an isosceles triangle. The height of each triangle is not the vertical height of the pyramid — it is the distance from the apex down to the midpoint of a base edge, measured along the slant face. This is the **slant height**, usually called *l*. The lateral area of the whole pyramid is just the number of triangular faces times (1/2 × base × slant height), which collapses neatly to (1/2) × perimeter × *l*. Total surface area = base area + (1/2) × P × *l*.

A **cone** is the smooth, circular analog of a pyramid. Its lateral surface, when cut along one side and unrolled, becomes a flat sector of a circle (like a pie slice). The radius of that sector is the cone's slant height *l*, and the arc length of the sector equals the circumference of the cone's base circle, 2πr. Working out the area of that sector gives the lateral area as π*r*l. Adding the circular base gives: **SA = πr² + πrl**. The formula looks new, but it comes from the same unrolling idea you used for prisms.

The critical quantity in both formulas — and the most common source of errors — is the **slant height**. The slant height is not the vertical height *h* of the solid. If you drop a perpendicular from the apex straight down to the base, you get *h*. The slant height runs from the apex diagonally to the edge of the base. These three lengths form a right triangle: *h* (vertical leg), *r* (horizontal leg, from center to base edge), and *l* (hypotenuse). Your Pythagorean theorem prerequisite is what connects them: **l² = h² + r²**. Whenever a problem gives you *h* and *r* but the formula needs *l*, reach for the Pythagorean theorem first.
