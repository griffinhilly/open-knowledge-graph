---
id: area-of-triangles
title: Area of Triangles
domain: mathematics
course: prealgebra
prerequisites:
- id: area-of-rectangles
  type: hard
- id: multiplying-integers
  type: hard
- id: area-and-perimeter-problems
  type: soft
- id: area-rectilinear-shapes
  type: soft
- id: area-of-parallelograms
  type: soft
builds-toward:
- area-of-trapezoids
- surface-area-intro
- area-of-regular-polygons
tags:
- area
- triangles
- geometry
- measurement
stage: abstract-reasoning
status: validated
---
# Area of Triangles

## Core Idea
The area of a triangle is A = (1/2)bh, where b is the base and h is the height (the perpendicular distance from the base to the opposite vertex). This formula comes directly from the fact that every triangle is exactly half of a parallelogram (or rectangle) with the same base and height. Understanding why the formula works — not just memorizing it — helps students apply it correctly in varied orientations and in composite shapes. Triangle area is foundational for surface area calculations and for more advanced geometry.

## How It's Best Learned
Start by drawing a rectangle, cutting it diagonally, and showing that each triangle is half the rectangle. Then show this works for non-right triangles by enclosing them in a rectangle and subtracting. Practice identifying the base and corresponding height in triangles drawn in different orientations — students must see that the height is always perpendicular to the chosen base.

## Common Misconceptions
- Forgetting to divide by 2 (computing bh instead of bh/2).
- Using a slant side as the height instead of the perpendicular height.
- Thinking only the bottom side can be the base — any side can be the base if the corresponding height is used.

## Explainer

The formula A = (1/2)bh is not just a rule to memorize — it has a clear geometric reason that makes it impossible to forget once you see it. You already know how to find the **area of a rectangle**: multiply length times width, or equivalently, base times height. Every triangle is secretly half of a rectangle (or parallelogram). Draw any right triangle; rotate a copy of it 180° and attach it to the hypotenuse: you get a rectangle. The triangle is exactly half that rectangle, so its area is half of base × height. The formula follows directly from your prerequisite knowledge.

But what about non-right triangles? Here the same idea still works, just with a little more care. Take any triangle and drop a **perpendicular** from the top vertex straight down to the base (or the extended base). This perpendicular is the height h — it measures the straight-up distance from the base to the opposite vertex, not the length of any slanted side. Now the triangle splits into two right triangles, and you can verify that together they have area exactly (1/2)bh. The critical insight: the height h is always the perpendicular distance, never a slanted side.

Because any of the three sides can serve as the base, every triangle actually has three different base-height pairs, all giving the same area. If you pick the bottom side as the base, h is the vertical drop from the top vertex. If you pick the left side as the base, h is the perpendicular from the right vertex to that side. The product (1/2) × base × corresponding height always gives the same number, since there's only one triangle with one area. This is worth checking on a specific triangle: compute the area three different ways and confirm they match.

Triangles are the building blocks of more complex shapes. Any polygon can be divided into triangles — this is called **triangulation** — and the total area is the sum of the triangle areas. When you compute surface areas of 3D shapes (coming up soon), you'll often slice faces into triangles and sum (1/2)bh for each. Getting fluent with identifying the correct base-height pair in any orientation, including when the height falls outside the triangle, is the skill that makes all of that downstream geometry tractable.
