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

## Questions

```yaml
- question: "A cone has vertical height 4 and base radius 3. What is its lateral surface area?"
  type: multiple-choice
  options:
    - "12π — computed using the vertical height in place of the slant height"
    - "15π — computed using the correct slant height of 5"
    - "9π — the base area only, omitting the lateral face"
    - "25π — computed by adding height and radius before multiplying"
  answer: 1
  explanation: "The lateral area of a cone is πrl, where l is the slant height, not the vertical height. First compute slant height using the Pythagorean theorem: l² = h² + r² = 16 + 9 = 25, so l = 5. Lateral area = π(3)(5) = 15π. Option A is the most common error — plugging the vertical height (4) directly into the formula without computing slant height first."

- question: "When the lateral surface of a cone is cut along one edge and unrolled flat, what shape results?"
  type: multiple-choice
  options:
    - "A rectangle, because the surface wraps smoothly around a circular base"
    - "A triangle, because the cone tapers to a point"
    - "A sector of a circle, with the slant height as its radius"
    - "A full circle with the base radius as its radius"
  answer: 2
  explanation: "Cutting the lateral surface of a cone along a straight line from apex to base edge and unrolling it produces a flat sector (pie slice) of a larger circle. The radius of that sector is the slant height l, and the arc length of the sector equals the base circumference 2πr. Working out the area of this sector yields the lateral area formula πrl. This 'net' approach is why the formula works."

- question: "The slant height of a right cone equals its vertical height."
  type: true-false
  answer: false
  explanation: "The vertical height h drops perpendicularly from the apex to the center of the base. The slant height l runs from the apex diagonally to the rim of the base. Together with the radius r, they form a right triangle where l is the hypotenuse: l² = h² + r². Since r > 0 for any real cone, l is always strictly greater than h."

- question: "The slant height of a cone is always greater than its vertical height."
  type: true-false
  answer: true
  explanation: "In the right triangle formed by the vertical height h (vertical leg), radius r (horizontal leg), and slant height l (hypotenuse), the hypotenuse is always longer than either leg when both legs are positive. Since any real cone has r > 0, we have l = √(h² + r²) > h. This is why substituting h for l always underestimates the lateral area."

- question: "Why must you compute slant height before applying the cone or pyramid surface area formula, even when the problem gives you the vertical height?"
  type: short-answer
  answer: "The lateral area formulas (πrl for cones, ½Pl for pyramids) come from the area of the actual slanted faces — the surface you would walk on going up the side. The slant height is the distance from apex to base edge measured along that face. Vertical height is perpendicular to the base and lies entirely inside the solid; it never appears on any lateral face. The Pythagorean theorem l² = h² + r² converts the given vertical height and radius into the slant height the formula needs."
  explanation: "This is the most common error in these problems. Students see h in the problem and plug it into the formula as if it were l. The fix is to treat every problem as two steps: (1) find l using the Pythagorean theorem, (2) substitute l into the area formula. The error is not algebraic — it is conceptual: confusing a height that points straight up with a height that runs up a slanted face."
```

## Explainer

From your work on prisms, you know the strategy for surface area: imagine cutting the solid apart and flattening it into a **net**, then add up the areas of all the flat pieces. That same strategy applies to pyramids and cones — the only new challenge is figuring out the shapes you get when you unfold the curved or triangular sides.

A **pyramid** has a polygon base and triangular lateral faces that meet at a point called the **apex**. When you unfold a regular pyramid (where the base is a regular polygon and the apex sits directly above its center), each lateral face is an isosceles triangle. The height of each triangle is not the vertical height of the pyramid — it is the distance from the apex down to the midpoint of a base edge, measured along the slant face. This is the **slant height**, usually called *l*. The lateral area of the whole pyramid is just the number of triangular faces times (1/2 × base × slant height), which collapses neatly to (1/2) × perimeter × *l*. Total surface area = base area + (1/2) × P × *l*.

A **cone** is the smooth, circular analog of a pyramid. Its lateral surface, when cut along one side and unrolled, becomes a flat sector of a circle (like a pie slice). The radius of that sector is the cone's slant height *l*, and the arc length of the sector equals the circumference of the cone's base circle, 2πr. Working out the area of that sector gives the lateral area as π*r*l. Adding the circular base gives: **SA = πr² + πrl**. The formula looks new, but it comes from the same unrolling idea you used for prisms.

The critical quantity in both formulas — and the most common source of errors — is the **slant height**. The slant height is not the vertical height *h* of the solid. If you drop a perpendicular from the apex straight down to the base, you get *h*. The slant height runs from the apex diagonally to the edge of the base. These three lengths form a right triangle: *h* (vertical leg), *r* (horizontal leg, from center to base edge), and *l* (hypotenuse). Your Pythagorean theorem prerequisite is what connects them: **l² = h² + r²**. Whenever a problem gives you *h* and *r* but the formula needs *l*, reach for the Pythagorean theorem first.
