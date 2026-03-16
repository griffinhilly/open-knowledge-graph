---
id: volume-of-prisms
title: Volume of Prisms
domain: mathematics
course: prealgebra
prerequisites:
- id: area-of-rectangles
  type: hard
- id: area-of-triangles
  type: soft
- id: multiplying-integers
  type: hard
builds-toward:
- volume-of-prisms-and-cylinders
tags:
- volume
- prisms
- 3d-shapes
- geometry
stage: abstract-reasoning
status: validated
---
# Volume of Prisms

## Core Idea
The volume of a prism is V = Bh, where B is the area of the base and h is the height (the perpendicular distance between the two parallel bases). For a rectangular prism, B = lw, so V = lwh. For a triangular prism, B = (1/2)bh_triangle. Volume measures the amount of space inside a 3D shape, answering "how much can it hold?" The unifying idea — base area times height — works for all prisms and extends naturally to cylinders. Volume is measured in cubic units.

## How It's Best Learned
Start with unit cubes: physically build rectangular prisms and count cubes to verify the formula. Then generalize: the base can be any shape, and stacking that shape to the given height gives the volume. Practice with rectangular and triangular prisms. Emphasize units: if dimensions are in centimeters, volume is in cubic centimeters. Include real-world problems (aquariums, shipping boxes, swimming pools).

## Common Misconceptions
- Confusing the base area with the base length (using just one dimension instead of computing the area first).
- Confusing surface area and volume formulas.
- Using the slant height of a triangular prism instead of the prism's height (the distance between the triangular bases).

## Explainer

You already know how to find the **area of a rectangle** (length × width) and the **area of a triangle** (½ × base × height). Volume extends that 2D thinking into 3D by asking: what if we stacked that flat shape upward? The formula V = Bh — base area times height — captures exactly this idea. B is the area of the flat cross-section (the "face" that gets stacked), and h is how tall the stack is.

The clearest way to see this is with unit cubes. A rectangular prism that is 3 cm long, 2 cm wide, and 4 cm tall holds 3 × 2 = 6 cubes in the bottom layer. Stacking four such layers gives 6 × 4 = 24 cubes total, so the volume is 24 cm³. The formula V = lwh just counts this systematically: l × w computes the base area B, and multiplying by h counts the layers. For a rectangular prism, B = lw, so V = lwh. But the logic works for any prism — any shape that has the same cross-section all the way through.

A **triangular prism** works the same way. The triangular base has area B = ½ × b × h_triangle (using the triangle's own base and height). Multiply by the prism's height (the length of the prism, the distance between the two triangular faces) and you get the volume. The key is that "height of the prism" and "height of the triangle" are two different measurements: the triangle's height is inside the triangular face, while the prism's height is the perpendicular distance between the two triangular ends.

Units are essential and follow directly from the multiplication. If dimensions are in centimeters, then B is in cm² and h is in cm, so V = B × h is in cm² × cm = cm³ — cubic centimeters. This makes physical sense: volume measures how many unit cubes fit inside, and each unit cube occupies 1 cm × 1 cm × 1 cm = 1 cm³ of space. When solving problems, always label your units at every step, and check that your final answer is in cubic units. If you end up with cm² or just cm, something went wrong in the calculation.
