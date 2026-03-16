---
id: surface-area-of-cylinders
title: Surface Area of Cylinders
domain: mathematics
course: geometry
prerequisites:
  - id: circle-basics
    type: hard
  - id: arc-length-circles
    type: soft
builds-toward:
  - volume-of-prisms-and-cylinders
tags: [3d-geometry, surface-area, cylinders]
stage: abstract-reasoning
status: validated
---

# Surface Area of Cylinders

## Core Idea
A cylinder has two circular bases connected by a curved lateral surface. The surface area is SA = 2*pi*r^2 + 2*pi*r*h (two circle bases plus the lateral rectangle that wraps around). The lateral surface, when unrolled, is a rectangle with width = circumference of the base (2*pi*r) and height = h.

## How It's Best Learned
Demonstrate the unrolling of the lateral surface: cut a paper towel tube lengthwise and flatten it to show it is a rectangle. Compute the area of the two circles and the rectangle. Practice with various radii and heights. Give problems where students must find missing dimensions given the surface area.

## Common Misconceptions
- Forgetting to include both circular bases.
- Not recognizing that the lateral surface unrolls to a rectangle whose width is the circumference.
- Confusing the formulas for surface area and volume.

## Explainer

Surface area answers the question: if you peeled every face off a 3D shape and laid the pieces flat, how much total flat area would you have? For a **cylinder**, the shape has three faces: two circular bases (top and bottom) and one curved **lateral surface** (the side). Understanding the formula means understanding how each piece contributes.

The two circular bases are straightforward — you know from circle basics that the area of a circle is πr². There are two of them, so together they contribute 2πr².

The lateral surface is the insight. Imagine taking a soup can, cutting it vertically along one edge, and unrolling it flat. What you get is a rectangle. Its height is the same h as the cylinder's height — that hasn't changed. Its width is the distance you'd travel if you walked all the way around the base of the cylinder once, which is the circumference of the circular base: 2πr. So the lateral surface area is width × height = 2πr · h = 2πrh.

Adding all three pieces: **SA = 2πr² + 2πrh**. This can be factored as 2πr(r + h), which is a useful form to recognize. The r + h term tells you that both the radius and height matter equally to the lateral area. A very wide, short cylinder and a very narrow, tall cylinder can have the same surface area if r + h is the same.

A common error is forgetting one or both circular bases. This typically happens when students think of the cylinder as "just the side" — the tube. Remember that a closed cylinder has two lids. If a problem asks for the **lateral surface area only** (like the label on a can), the formula is just 2πrh. If it asks for the **total surface area**, include both bases. Reading carefully which quantity is asked for is as important as knowing the formula.
