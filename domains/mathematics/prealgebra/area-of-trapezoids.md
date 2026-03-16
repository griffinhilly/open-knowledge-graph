---
id: area-of-trapezoids
title: Area of Trapezoids
domain: mathematics
course: prealgebra
prerequisites:
- id: area-of-parallelograms
  type: hard
- id: area-of-triangles
  type: soft
- id: adding-fractions-unlike-denominators
  type: soft
builds-toward:
- surface-area-intro
- area-of-regular-polygons
tags:
- area
- trapezoids
- geometry
- measurement
stage: abstract-reasoning
status: validated
---
# Area of Trapezoids

## Core Idea
The area of a trapezoid is A = (1/2)(b₁ + b₂)h, where b₁ and b₂ are the two parallel bases and h is the perpendicular height between them. This formula can be understood by doubling the trapezoid — flip a copy upside down and attach it to the original to form a parallelogram with base (b₁ + b₂) and height h. The trapezoid's area is half of that parallelogram. Alternatively, it is the average of the two bases times the height. This topic reinforces the idea that all polygon area formulas are connected through decomposition and rearrangement.

## How It's Best Learned
Show the "double the trapezoid" derivation visually. Also show decomposing the trapezoid into a rectangle and two triangles. Practice identifying the two parallel bases and the height. Use the "average of the bases times the height" interpretation as an intuitive shortcut. Include problems where the trapezoid is oriented in non-standard ways.

## Common Misconceptions
- Using a non-parallel side as one of the bases.
- Forgetting to add the two bases before multiplying by the height.
- Forgetting to multiply by 1/2 (computing (b₁ + b₂)h instead of half of that).

## Explainer

A **trapezoid** is a quadrilateral with exactly one pair of parallel sides. Those two parallel sides are called the **bases** (b₁ and b₂), and the perpendicular distance between them is the **height** (h). The fact that the bases are parallel — and not just any two sides — is what makes the area formula work. Before deriving it, notice that you already know the area of a parallelogram from your prerequisite: A = base × height. The trapezoid formula is a direct extension of that idea.

Here is the cleanest derivation. Take your trapezoid and flip an identical copy upside down. Attach the flipped copy to the original along the longer base. The combined shape is a **parallelogram** with base (b₁ + b₂) and height h. Its area is (b₁ + b₂) × h. Since two trapezoids make one parallelogram, one trapezoid is exactly half: A = (1/2)(b₁ + b₂)h. You can also read this as the **average of the two bases** multiplied by the height — think of it as if you replaced the trapezoid with a rectangle whose base is midway between the two parallel sides.

To use the formula correctly, you must identify the two parallel sides, not just any two sides. In a typical trapezoid drawn with one base at the bottom and a shorter base at the top, the height is the vertical distance between them — not the length of the slanted sides. The slanted sides (the **legs**) are irrelevant to the area calculation. If the trapezoid is tilted or drawn in a non-standard orientation, look for the pair of sides that run in the same direction, and drop a perpendicular between them to find h.

The formula connects the trapezoid to the whole family of polygon area results. A parallelogram is a special trapezoid where b₁ = b₂, so (1/2)(b + b)h = bh — exactly the parallelogram formula. A triangle is a degenerate trapezoid where one base shrinks to zero: (1/2)(b + 0)h = (1/2)bh — exactly the triangle formula. This shows that all three formulas are the same formula at heart, and every polygon area can be understood through decomposition and rearrangement of shapes you already know.
