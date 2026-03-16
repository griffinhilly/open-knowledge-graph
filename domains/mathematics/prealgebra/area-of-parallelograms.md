---
id: area-of-parallelograms
title: Area of Parallelograms
domain: mathematics
course: prealgebra
prerequisites:
- id: area-of-rectangles
  type: hard
- id: area-and-perimeter-problems
  type: soft
- id: area-rectilinear-shapes
  type: soft
builds-toward:
- area-of-triangles
- area-of-trapezoids
- surface-area-intro
tags:
- area
- parallelograms
- geometry
- measurement
stage: abstract-reasoning
status: validated
---
# Area of Parallelograms

## Core Idea
The area of a parallelogram is A = bh, where b is the base and h is the perpendicular height (not the slant side). This formula is identical to a rectangle's because any parallelogram can be rearranged into a rectangle: cut off a right triangle from one end and slide it to the other end. This geometric transformation is a beautiful example of how area is conserved under rearrangement. The parallelogram area formula is the parent formula from which triangle and trapezoid area formulas are derived.

## How It's Best Learned
Demonstrate the cut-and-rearrange transformation with physical paper cutouts or dynamic geometry software. Emphasize that the height is not the slant side — draw the height as a dashed perpendicular line from base to top. Practice with parallelograms in various orientations so students don't assume the bottom is always the base.

## Common Misconceptions
- Using the slant side length as the height instead of the perpendicular height.
- Multiplying base times side (using the wrong dimension entirely).
- Confusing the parallelogram formula with the triangle formula and dividing by 2 unnecessarily.

## Explainer

You already know that the area of a rectangle is base × height. The area of a parallelogram uses the exact same formula — A = bh — and the reason why comes from a clever physical argument. Imagine cutting a parallelogram out of paper. Slice a right triangle off the left end, along a vertical line drawn from the top-left corner straight down to the base. Now slide that triangle over to the right end. The shape you have now is a rectangle with the same base and the same perpendicular height as the original parallelogram. Since rearranging pieces doesn't change area, the parallelogram must have the same area as the rectangle: base × height.

The critical detail is what "height" means. The **perpendicular height** is the distance measured straight up — at a right angle from the base to the top side. It is NOT the length of the slanted side. Think of a leaning tower: a tower that leans has the same floor-to-ceiling distance whether you measure straight up or along the slant, but the "height" for area purposes is always the straight-up measurement. In a parallelogram, the slant side is longer than the perpendicular height, and using the slant side will always give you an answer that's too large.

This formula is the foundation for two area formulas you'll learn next. A triangle is exactly half of a parallelogram: if you duplicate a triangle and flip it, the two copies fit together to form a parallelogram with the same base and height. So the triangle area formula A = ½bh is literally derived from the parallelogram formula by dividing by 2. A trapezoid can similarly be split or doubled to reveal its area formula. Understanding the parallelogram rearrangement argument — not just memorizing A = bh — gives you the intuition to derive these related formulas rather than memorizing each one separately.

When a problem gives you a parallelogram, always identify the base and its corresponding perpendicular height before multiplying. The height line will be perpendicular to the base and will often be drawn as a dashed line inside or outside the figure. If a problem gives you the slant side and an angle, you will need to use right-triangle reasoning to find the perpendicular height first. But in most prealgebra problems, the perpendicular height is labeled directly — your job is to pick the right number from the figure and not reach for the slanted side out of habit.
