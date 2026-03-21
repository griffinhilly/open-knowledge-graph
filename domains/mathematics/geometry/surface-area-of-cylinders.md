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

## Questions

```yaml
- question: "When the curved lateral surface of a cylinder is cut along one edge and unrolled flat, what shape does it form?"
  type: multiple-choice
  options:
    - "A circle"
    - "A rectangle"
    - "A triangle"
    - "A trapezoid"
  answer: 1
  explanation: "The lateral surface of a cylinder — the 'side' of the can — unrolls into a flat rectangle. Its height equals the height of the cylinder (h), and its width equals the distance around the circular base, which is the circumference: 2πr. This is the key insight that makes the surface area formula understandable rather than memorized: the lateral area is just the area of that rectangle, width × height = 2πr × h = 2πrh. Visualizing or physically demonstrating this unrolling is the best way to internalize why the formula works."

- question: "A cylinder has radius 3 and height 5. What is its total surface area?"
  type: multiple-choice
  options:
    - "30π (lateral surface only: 2π × 3 × 5)"
    - "48π (two bases plus lateral: 2π(3²) + 2π(3)(5) = 18π + 30π)"
    - "39π (one base plus lateral: π(3²) + 2π(3)(5) = 9π + 30π)"
    - "33π (two bases plus half lateral: 2π(3²) + π(3)(5) = 18π + 15π)"
  answer: 1
  explanation: "Total surface area = 2πr² + 2πrh. With r = 3 and h = 5: two bases = 2π(9) = 18π; lateral surface = 2π(3)(5) = 30π; total = 48π. Option A (30π) is the common error of computing only the lateral surface and forgetting both circular bases — thinking of the cylinder as 'just the side.' Option C (39π) is the error of including only one base instead of two. The formula must include all three faces: top, bottom, and the unrolled side."

- question: "The width of the rectangle formed by unrolling a cylinder's lateral surface equals the circumference of the circular base."
  type: true-false
  answer: true
  explanation: "When you cut the lateral surface of a cylinder along a vertical line and unroll it, you travel exactly once around the circular base — a distance equal to the circumference, 2πr. This becomes the width of the resulting rectangle, while the height of the cylinder becomes the rectangle's height. Area = width × height = 2πr × h = 2πrh. Understanding why the width equals the circumference (not the diameter, not the radius) is the key to not just memorizing the formula but understanding it."

- question: "The lateral surface area of a cylinder with radius r and height h is πrh."
  type: true-false
  answer: false
  explanation: "The correct formula for lateral surface area is 2πrh, not πrh. The factor of 2 comes from the circumference of the circle, which is 2πr — this is the width of the rectangle the lateral surface unrolls into. The area is then 2πr × h = 2πrh. A common error is using πr (the radius times π without the factor of 2) instead of 2πr (the circumference). This typically happens when students confuse the radius with the circumference, or when they use πd and substitute r instead of d."

- question: "Explain in your own words why the formula for the lateral surface area of a cylinder is 2πrh. Where does each part of the formula come from?"
  type: short-answer
  answer: "If you cut the curved side of a cylinder along a straight vertical line and unroll it flat, you get a rectangle. The height of that rectangle is the same as the height h of the cylinder. The width of the rectangle is the distance all the way around the circular base — the circumference — which equals 2πr. The area of this rectangle is width × height = 2πr × h = 2πrh. So the formula comes directly from the fact that the lateral surface is a rectangle whose width equals the base's circumference."
  explanation: "Students who understand the unrolling insight can reconstruct the formula even if they forget it on a test. Those who only memorize '2πrh' are helpless when asked to derive or explain it. The formula also explains why both r and h matter equally in the lateral term: the width of the rectangle depends on r (through the circumference), and the height of the rectangle is h."
```

## Explainer

Surface area answers the question: if you peeled every face off a 3D shape and laid the pieces flat, how much total flat area would you have? For a **cylinder**, the shape has three faces: two circular bases (top and bottom) and one curved **lateral surface** (the side). Understanding the formula means understanding how each piece contributes.

The two circular bases are straightforward — you know from circle basics that the area of a circle is πr². There are two of them, so together they contribute 2πr².

The lateral surface is the insight. Imagine taking a soup can, cutting it vertically along one edge, and unrolling it flat. What you get is a rectangle. Its height is the same h as the cylinder's height — that hasn't changed. Its width is the distance you'd travel if you walked all the way around the base of the cylinder once, which is the circumference of the circular base: 2πr. So the lateral surface area is width × height = 2πr · h = 2πrh.

Adding all three pieces: **SA = 2πr² + 2πrh**. This can be factored as 2πr(r + h), which is a useful form to recognize. The r + h term tells you that both the radius and height matter equally to the lateral area. A very wide, short cylinder and a very narrow, tall cylinder can have the same surface area if r + h is the same.

A common error is forgetting one or both circular bases. This typically happens when students think of the cylinder as "just the side" — the tube. Remember that a closed cylinder has two lids. If a problem asks for the **lateral surface area only** (like the label on a can), the formula is just 2πrh. If it asks for the **total surface area**, include both bases. Reading carefully which quantity is asked for is as important as knowing the formula.
