---
id: surface-area-of-prisms
title: Surface Area of Prisms
domain: mathematics
course: geometry
prerequisites:
  - id: area-of-regular-polygons
    type: soft
  - id: polygon-angle-sums
    type: soft
builds-toward:
  - volume-of-prisms-and-cylinders
tags: [3d-geometry, surface-area, prisms, nets]
stage: abstract-reasoning
status: validated
---

# Surface Area of Prisms

## Core Idea
A prism has two congruent parallel bases (any polygon) connected by rectangular lateral faces. The surface area is the sum of the areas of all faces: SA = 2B + Ph, where B is the base area, P is the base perimeter, and h is the height (distance between bases). This can be visualized by "unfolding" the prism into a net.

## How It's Best Learned
Start with nets: unfold a prism to show the two bases and the lateral rectangle. Compute the lateral area as perimeter times height. Practice with triangular, rectangular, and hexagonal prisms. Emphasize that the formula works for any polygon base.

## Common Misconceptions
- Forgetting to include both bases (multiplying B by 2).
- Confusing the height of the prism with the slant height.
- Not computing the base area correctly for non-rectangular bases.

## Explainer

You already know how to find areas of polygons — triangles, rectangles, regular hexagons, and so on. A prism takes one of those polygons and stretches it through space to create a 3D solid. The two identical polygon faces at the ends are called the **bases**, and the flat rectangular panels connecting them are the **lateral faces**. Finding the surface area means answering a simple question: if you peeled the entire exterior off the prism and laid it flat, how much area would it cover?

The most intuitive approach is to "unfold" — or **net** — the prism. Cut along the lateral edges and flatten the shape out. You'll see two copies of the base polygon, plus a long rectangle. The rectangle's height equals the prism's height h (the distance between the two bases). Its width is the full perimeter of the base polygon, because each side of the base corresponds to one lateral rectangular panel, and when those panels are unfolded side by side, they form one big rectangle of width P (perimeter). This gives the **lateral surface area** as P × h. Add the two bases, each with area B, and you get the total: SA = 2B + Ph.

Consider a triangular prism with a right triangle base (legs 3 and 4, hypotenuse 5) and height 10. The base area is ½ × 3 × 4 = 6. The perimeter is 3 + 4 + 5 = 12. So the lateral area is 12 × 10 = 120, and the total surface area is 2(6) + 120 = 132 square units. The formula works identically whether the base is a triangle, pentagon, or irregular hexagon — the only things that change are how you compute B and P. This is the power of the net approach: it turns a 3D problem into a 2D one.

One subtlety worth watching: the "height" in the formula is always the perpendicular distance between the two bases — the length of the lateral edges — not any measurement inside or along the base polygon. If the prism is oblique (leaning), the lateral faces become parallelograms rather than rectangles, and the formula changes. In the standard case of a **right prism** (lateral edges perpendicular to the bases), the lateral faces are guaranteed to be rectangles, and SA = 2B + Ph applies cleanly. When computing B, draw on your polygon area skills: use the appropriate formula for whatever base polygon you have.
