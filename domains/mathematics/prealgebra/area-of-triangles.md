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

## Questions

```yaml
- question: "A triangle has a base of 10 cm. The slant side adjacent to the base measures 8 cm, and the perpendicular height from the base to the opposite vertex is 6 cm. What is the area?"
  type: multiple-choice
  options:
    - "80 cm² — multiply base times slant side"
    - "40 cm² — use (1/2) × base × slant side"
    - "30 cm² — use (1/2) × base × perpendicular height"
    - "60 cm² — multiply base times perpendicular height"
  answer: 2
  explanation: "The formula A = (1/2)bh requires the *perpendicular* height h — the straight-line distance from the base to the opposite vertex, measured at a right angle. Here h = 6 cm, so A = (1/2)(10)(6) = 30 cm². Using the slant side (8 cm) instead of the height is the most common error with non-right triangles. The slant side is a side of the triangle, not its height."

- question: "A triangle has three base-height pairs that can be used to compute its area: (base 5, height 12) and (base 10, height 6). What must the height be when the third side of length 13 is used as the base?"
  type: multiple-choice
  options:
    - "13 — the height equals the base when a different side is chosen"
    - "≈ 4.6 — because all three base-height pairs must yield the same area"
    - "Cannot be determined without knowing the triangle's angles"
    - "6 — the height is fixed regardless of which base you choose"
  answer: 1
  explanation: "All three base-height pairs give the same area because there is only one area for a given triangle. Using (base 5, height 12): A = (1/2)(5)(12) = 30. Using (base 10, height 6): A = (1/2)(10)(6) = 30. So (1/2)(13)(h) = 30, giving h = 60/13 ≈ 4.6. This confirms that you can choose any side as the base as long as you use the *corresponding* perpendicular height."

- question: "The height of a triangle is typically one of its three sides."
  type: true-false
  answer: false
  explanation: "The height (altitude) of a triangle is the perpendicular distance from a chosen base to the opposite vertex — it is not a side of the triangle unless the triangle is a right triangle and you use the legs as base and height. For non-right triangles, the height is a separate segment drawn from the vertex perpendicular to the base (or the extended base). Using a slant side as the height is the most common error in computing triangle area."

- question: "If you double the height of a triangle while keeping the base the same, the area doubles."
  type: true-false
  answer: true
  explanation: "A = (1/2)bh. If h becomes 2h, the new area is (1/2)b(2h) = 2 × (1/2)bh = 2A. Area is directly proportional to height (and to base). This is a direct consequence of the formula and is useful for scaling: doubling any one dimension while holding the other constant doubles the area."

- question: "Why does the formula A = (1/2)bh for the area of a triangle include the factor of 1/2?"
  type: short-answer
  answer: "Because every triangle is exactly half of a parallelogram (or rectangle) with the same base and height. If you duplicate a triangle and rotate the copy 180°, the two triangles fit together to form a rectangle (for right triangles) or parallelogram (for any triangle). That parallelogram has area b × h, so each triangle is half: (1/2)bh."
  explanation: "This geometric reasoning makes the formula unforgettable once understood. It also explains why the height must be perpendicular: the area of the parallelogram is base times *perpendicular* height, so halving it gives (1/2) × base × perpendicular height. Using a slant dimension would give the wrong parallelogram area and thus the wrong triangle area."
```

## Explainer

The formula A = (1/2)bh is not just a rule to memorize — it has a clear geometric reason that makes it impossible to forget once you see it. You already know how to find the **area of a rectangle**: multiply length times width, or equivalently, base times height. Every triangle is secretly half of a rectangle (or parallelogram). Draw any right triangle; rotate a copy of it 180° and attach it to the hypotenuse: you get a rectangle. The triangle is exactly half that rectangle, so its area is half of base × height. The formula follows directly from your prerequisite knowledge.

But what about non-right triangles? Here the same idea still works, just with a little more care. Take any triangle and drop a **perpendicular** from the top vertex straight down to the base (or the extended base). This perpendicular is the height h — it measures the straight-up distance from the base to the opposite vertex, not the length of any slanted side. Now the triangle splits into two right triangles, and you can verify that together they have area exactly (1/2)bh. The critical insight: the height h is always the perpendicular distance, never a slanted side.

Because any of the three sides can serve as the base, every triangle actually has three different base-height pairs, all giving the same area. If you pick the bottom side as the base, h is the vertical drop from the top vertex. If you pick the left side as the base, h is the perpendicular from the right vertex to that side. The product (1/2) × base × corresponding height always gives the same number, since there's only one triangle with one area. This is worth checking on a specific triangle: compute the area three different ways and confirm they match.

Triangles are the building blocks of more complex shapes. Any polygon can be divided into triangles — this is called **triangulation** — and the total area is the sum of the triangle areas. When you compute surface areas of 3D shapes (coming up soon), you'll often slice faces into triangles and sum (1/2)bh for each. Getting fluent with identifying the correct base-height pair in any orientation, including when the height falls outside the triangle, is the skill that makes all of that downstream geometry tractable.
