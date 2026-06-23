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
- id: area-as-multiplication-3rd
  type: hard
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

## Questions

```yaml
- question: "A parallelogram has a base of 8 cm, a slant side of 6 cm, and a perpendicular height of 5 cm. What is its area?"
  type: multiple-choice
  options:
    - "48 cm² (base × slant side)"
    - "40 cm² (base × perpendicular height)"
    - "24 cm² (½ × base × slant side)"
    - "20 cm² (½ × base × perpendicular height)"
  answer: 1
  explanation: "Area = base × perpendicular height = 8 × 5 = 40 cm². The slant side (6 cm) is not the height. Option A is the classic error: reaching for the slant side because it looks like a 'side length.' Options C and D apply the triangle formula (dividing by 2), which is wrong for a parallelogram. The perpendicular height is the straight-up distance from base to top — always shorter than the slant side."

- question: "Why does the area formula for a parallelogram use the perpendicular height rather than the length of the slant side?"
  type: multiple-choice
  options:
    - "Because the slant side is always longer, so using it would overcount the area of the angled corners"
    - "Because cutting a right triangle from one end and sliding it to the other converts the parallelogram into a rectangle — and the rectangle's height is the perpendicular measurement, not the slant"
    - "Because the slant side formula only applies when the parallelogram happens to be a rhombus"
    - "Because mathematicians defined the formula arbitrarily and the perpendicular height is easier to measure in practice"
  answer: 1
  explanation: "The cut-and-slide argument is the geometric proof: slice a right triangle off one end of a parallelogram along a vertical line, slide it to the other end, and you have a rectangle with the same base and perpendicular height. Since rearranging pieces preserves area, the parallelogram's area equals the rectangle's area = base × perpendicular height. This also explains why using the slant side gives too large an answer — the slant side is longer than the perpendicular height and does not correspond to any dimension of the equivalent rectangle."

- question: "The formula for the area of a parallelogram is different from the formula for the area of a rectangle."
  type: true-false
  answer: false
  explanation: "Both use A = base × height. The formulas are identical because a parallelogram can be rearranged into a rectangle with the same base and perpendicular height. The cut-and-slide transformation proves this geometrically. This is not a coincidence — it is why the same formula works for both shapes, and it is the conceptual foundation for deriving the triangle and trapezoid formulas from the same starting point."

- question: "The triangle area formula A = ½bh is derived from the parallelogram formula because two identical triangles can be joined to form a parallelogram with the same base and height."
  type: true-false
  answer: true
  explanation: "If you duplicate a triangle and flip it 180°, the two pieces fit together along their shared edge to form a parallelogram. Therefore the triangle is exactly half of a parallelogram with the same base and perpendicular height, giving A = ½ × (bh) = ½bh. Understanding this derivation means you can reconstruct the triangle formula from the parallelogram formula rather than memorizing it as an independent fact."

- question: "Explain why using the slant side of a parallelogram as the height always gives an area that is too large, and describe the geometric reasoning that shows why A = bh is correct."
  type: short-answer
  answer: "The slant side is always longer than the perpendicular height (the hypotenuse of a right triangle is always longer than either leg). Since the formula multiplies the base by this measurement, using the slant side produces a larger product than the true area. The correct formula comes from the cut-and-slide argument: cutting a right triangle from one end of the parallelogram and sliding it to the other end produces a rectangle with the same base and perpendicular height. Because rearranging preserves area, and the rectangle's area is base × perpendicular height, the parallelogram's area must be the same."
  explanation: "The geometric derivation is more than a memory aid — it reveals that area formulas are not arbitrary. The parallelogram formula works because of a conservation principle (rearranging doesn't change area) applied to a specific transformation (cut-and-slide). Students who understand this argument can reconstruct it and apply the same logic to derive related formulas for triangles and trapezoids."
```

## Explainer

You already know that the area of a rectangle is base × height. The area of a parallelogram uses the exact same formula — A = bh — and the reason why comes from a clever physical argument. Imagine cutting a parallelogram out of paper. Slice a right triangle off the left end, along a vertical line drawn from the top-left corner straight down to the base. Now slide that triangle over to the right end. The shape you have now is a rectangle with the same base and the same perpendicular height as the original parallelogram. Since rearranging pieces doesn't change area, the parallelogram must have the same area as the rectangle: base × height.

The critical detail is what "height" means. The **perpendicular height** is the distance measured straight up — at a right angle from the base to the top side. It is NOT the length of the slanted side. Think of a leaning tower: a tower that leans has the same floor-to-ceiling distance whether you measure straight up or along the slant, but the "height" for area purposes is always the straight-up measurement. In a parallelogram, the slant side is longer than the perpendicular height, and using the slant side will always give you an answer that's too large.

This formula is the foundation for two area formulas you'll learn next. A triangle is exactly half of a parallelogram: if you duplicate a triangle and flip it, the two copies fit together to form a parallelogram with the same base and height. So the triangle area formula A = ½bh is literally derived from the parallelogram formula by dividing by 2. A trapezoid can similarly be split or doubled to reveal its area formula. Understanding the parallelogram rearrangement argument — not just memorizing A = bh — gives you the intuition to derive these related formulas rather than memorizing each one separately.

When a problem gives you a parallelogram, always identify the base and its corresponding perpendicular height before multiplying. The height line will be perpendicular to the base and will often be drawn as a dashed line inside or outside the figure. If a problem gives you the slant side and an angle, you will need to use right-triangle reasoning to find the perpendicular height first. But in most prealgebra problems, the perpendicular height is labeled directly — your job is to pick the right number from the figure and not reach for the slanted side out of habit.
