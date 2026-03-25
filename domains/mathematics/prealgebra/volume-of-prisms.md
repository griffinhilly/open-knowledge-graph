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
- id: surface-area-intro
  type: soft
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

## Questions

```yaml
- question: "A triangular prism has triangular faces with base 4 cm and height 3 cm, and the prism is 10 cm long. What is its volume?"
  type: multiple-choice
  options:
    - "120 cm³"
    - "60 cm³"
    - "40 cm³"
    - "30 cm³"
  answer: 1
  explanation: "First compute the base area: B = (1/2)(4)(3) = 6 cm². Then multiply by the prism's height (the length between the two triangular faces): V = 6 × 10 = 60 cm³. The most common error is computing 4 × 3 × 10 = 120 cm³, which forgets the 1/2 in the triangle's area formula. The second most common error is using only one dimension of the triangle instead of computing its area first."

- question: "A student calculates the volume of a rectangular prism with dimensions 5 cm × 4 cm × 3 cm as '5 × 4 = 20 cm².' What is wrong, and what is the correct volume?"
  type: multiple-choice
  options:
    - "The student used the wrong formula; they should have added all dimensions: 5 + 4 + 3 = 12 cm³"
    - "The student only used two of the three dimensions and got a surface area instead of a volume; the correct volume is 5 × 4 × 3 = 60 cm³"
    - "The student got the right number but the wrong units; the answer should be 20 cm³"
    - "The student should have used V = (1/2)Bh since all prisms use that formula"
  answer: 1
  explanation: "The student computed the base area (B = 5 × 4 = 20 cm²) but forgot to multiply by the height (h = 3 cm). The correct volume is V = Bh = 20 × 3 = 60 cm³. The units also reveal the error: cm² is an area unit, not a volume unit. Volume must be in cubic units (cm³). The formula V = lwh requires all three dimensions."

- question: "The 'height' of a triangular prism and the 'height' of its triangular base are the same measurement."
  type: true-false
  answer: false
  explanation: "False — this is one of the most common errors with triangular prisms. The triangular base has its own internal height: the perpendicular distance from the base of the triangle to its opposite vertex (used in the area formula ½bh). The prism's height is a completely different measurement: the perpendicular distance between the two triangular faces (the length of the prism). You need both values separately: B = (1/2)(base of triangle)(height of triangle), then V = B × (height of prism)."

- question: "If a prism's dimensions are all measured in centimeters, its volume must be expressed in cubic centimeters (cm³)."
  type: true-false
  answer: true
  explanation: "True. Volume is computed by multiplying three lengths together: B (in cm²) × h (in cm) = cm² × cm = cm³. This makes physical sense — volume counts how many unit cubes fit inside, and each unit cube is 1 cm × 1 cm × 1 cm = 1 cm³. If your answer comes out in cm² or cm, you missed a dimension in your calculation. Always check units as a built-in error detector."

- question: "Why does the formula V = Bh work for all prisms, regardless of the shape of the base?"
  type: short-answer
  answer: "Any prism has the same cross-sectional shape throughout its entire length. You can think of the volume as stacking the base shape repeatedly to the given height — like stacking identical sheets of paper. The total volume is just the area of that shape (B) times how many layers tall it is (h). The base shape doesn't matter; the logic of 'stacking a flat area' is universal."
  explanation: "This is the key conceptual generalization. Whether the base is a rectangle, triangle, hexagon, or any other shape, V = Bh applies because a prism is defined as a solid with a constant cross-section. This same logic extends to cylinders, where B = πr². Understanding why the formula works — not just that it works — lets you apply it to unfamiliar cases without memorizing separate formulas."
```

## Explainer

You already know how to find the **area of a rectangle** (length × width) and the **area of a triangle** (½ × base × height). Volume extends that 2D thinking into 3D by asking: what if we stacked that flat shape upward? The formula V = Bh — base area times height — captures exactly this idea. B is the area of the flat cross-section (the "face" that gets stacked), and h is how tall the stack is.

The clearest way to see this is with unit cubes. A rectangular prism that is 3 cm long, 2 cm wide, and 4 cm tall holds 3 × 2 = 6 cubes in the bottom layer. Stacking four such layers gives 6 × 4 = 24 cubes total, so the volume is 24 cm³. The formula V = lwh just counts this systematically: l × w computes the base area B, and multiplying by h counts the layers. For a rectangular prism, B = lw, so V = lwh. But the logic works for any prism — any shape that has the same cross-section all the way through.

A **triangular prism** works the same way. The triangular base has area B = ½ × b × h_triangle (using the triangle's own base and height). Multiply by the prism's height (the length of the prism, the distance between the two triangular faces) and you get the volume. The key is that "height of the prism" and "height of the triangle" are two different measurements: the triangle's height is inside the triangular face, while the prism's height is the perpendicular distance between the two triangular ends.

Units are essential and follow directly from the multiplication. If dimensions are in centimeters, then B is in cm² and h is in cm, so V = B × h is in cm² × cm = cm³ — cubic centimeters. This makes physical sense: volume measures how many unit cubes fit inside, and each unit cube occupies 1 cm × 1 cm × 1 cm = 1 cm³ of space. When solving problems, always label your units at every step, and check that your final answer is in cubic units. If you end up with cm² or just cm, something went wrong in the calculation.
