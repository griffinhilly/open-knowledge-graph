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
  - id: surface-area-intro
    type: hard
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

## Questions

```yaml
- question: "A right prism has a regular hexagonal base with area 24 square units and perimeter 18 units. The prism's height is 5 units. What is the total surface area?"
  type: multiple-choice
  options:
    - "24 + 90 = 114 square units"
    - "2(24) + 18(5) = 138 square units"
    - "18 × 5 = 90 square units"
    - "2(24) + 18 = 66 square units"
  answer: 1
  explanation: "SA = 2B + Ph = 2(24) + 18(5) = 48 + 90 = 138. The two bases each contribute B = 24, and the lateral surface area is perimeter times height = 18 × 5 = 90. Option A (114) is the classic error of counting only one base instead of two. Option C (90) calculates only the lateral area, forgetting both bases. The formula works identically for any polygon base — hexagon, triangle, or pentagon."

- question: "Why does unfolding a right prism into a net make the lateral surface area calculation straightforward?"
  type: multiple-choice
  options:
    - "The net shows that each lateral face is a triangle, making the triangle area formula applicable"
    - "The lateral faces, when unfolded side by side, form a single rectangle whose width equals the base perimeter and whose height equals the prism height"
    - "The net eliminates the need to calculate the base area separately"
    - "Each lateral face must be calculated separately even in the net; the net just shows them arranged neatly"
  answer: 1
  explanation: "Each side of the base polygon corresponds to one lateral rectangular panel. When those panels are unfolded and laid flat side by side, they form one large rectangle. Its height is h (the prism height), and its width is the sum of all base side lengths — the perimeter P. So lateral surface area = P × h. This insight is what makes SA = 2B + Ph not just a formula to memorize but a geometrically transparent result."

- question: "The formula SA = 2B + Ph applies to any right prism, regardless of the shape of the base polygon."
  type: true-false
  answer: true
  explanation: "This is the power of deriving the formula from a net rather than memorizing it for specific cases. Whether the base is a triangle, rectangle, regular hexagon, or irregular polygon, the structure is always the same: two congruent bases plus a lateral surface that unfolds into a rectangle of width P and height h. The only thing that changes is how you compute B (base area) and P (base perimeter) for the specific polygon involved."

- question: "In the formula SA = 2B + Ph, the variable h represents the height of the base polygon — for example, the height of the triangular base in a triangular prism."
  type: true-false
  answer: false
  explanation: "h is the height of the prism — the perpendicular distance between the two bases, which equals the length of the lateral edges. It has nothing to do with any measurement inside the base polygon. For a triangular prism, the triangle has its own height used in computing B (base area), but that is a separate quantity. Confusing these two heights is a common source of error, especially in triangular prisms where both exist."

- question: "Explain why the lateral surface area of a right prism equals P × h. Reference what happens when you unfold the lateral faces."
  type: short-answer
  answer: "Each side of the base polygon forms one lateral rectangular face. The width of that rectangle equals the length of that base side; its height equals h, the prism's height. When you cut the lateral faces along their vertical edges and unfold them flat, they lie side by side to form one big rectangle. The total width of this rectangle is the sum of all the base side lengths — the perimeter P. Therefore, the area of the unfolded rectangle is P × h, which is the entire lateral surface area."
  explanation: "This reasoning makes the formula understandable rather than arbitrary. It also generalizes immediately to any right prism: the net always produces two congruent bases and one lateral rectangle, regardless of the base polygon. Students who understand the net derivation can reconstruct the formula rather than needing to memorize it."
```

## Explainer

You already know how to find areas of polygons — triangles, rectangles, regular hexagons, and so on. A prism takes one of those polygons and stretches it through space to create a 3D solid. The two identical polygon faces at the ends are called the **bases**, and the flat rectangular panels connecting them are the **lateral faces**. Finding the surface area means answering a simple question: if you peeled the entire exterior off the prism and laid it flat, how much area would it cover?

The most intuitive approach is to "unfold" — or **net** — the prism. Cut along the lateral edges and flatten the shape out. You'll see two copies of the base polygon, plus a long rectangle. The rectangle's height equals the prism's height h (the distance between the two bases). Its width is the full perimeter of the base polygon, because each side of the base corresponds to one lateral rectangular panel, and when those panels are unfolded side by side, they form one big rectangle of width P (perimeter). This gives the **lateral surface area** as P × h. Add the two bases, each with area B, and you get the total: SA = 2B + Ph.

Consider a triangular prism with a right triangle base (legs 3 and 4, hypotenuse 5) and height 10. The base area is ½ × 3 × 4 = 6. The perimeter is 3 + 4 + 5 = 12. So the lateral area is 12 × 10 = 120, and the total surface area is 2(6) + 120 = 132 square units. The formula works identically whether the base is a triangle, pentagon, or irregular hexagon — the only things that change are how you compute B and P. This is the power of the net approach: it turns a 3D problem into a 2D one.

One subtlety worth watching: the "height" in the formula is always the perpendicular distance between the two bases — the length of the lateral edges — not any measurement inside or along the base polygon. If the prism is oblique (leaning), the lateral faces become parallelograms rather than rectangles, and the formula changes. In the standard case of a **right prism** (lateral edges perpendicular to the bases), the lateral faces are guaranteed to be rectangles, and SA = 2B + Ph applies cleanly. When computing B, draw on your polygon area skills: use the appropriate formula for whatever base polygon you have.
