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

## Questions

```yaml
- question: "A trapezoid has parallel sides of 5 cm and 9 cm, slanted legs of 6 cm each, and a perpendicular height of 4 cm. What is its area?"
  type: multiple-choice
  options:
    - "56 cm² — (5 + 9) × 4"
    - "28 cm² — (1/2)(5 + 9) × 4"
    - "24 cm² — (1/2)(6 + 6) × 4, using the slanted legs instead of the parallel sides"
    - "18 cm² — (1/2)(9) × 4, using only the longer base"
  answer: 1
  explanation: "The correct answer is 28 cm². The formula is A = (1/2)(b₁ + b₂)h, where b₁ and b₂ are the two parallel sides: (1/2)(5 + 9)(4) = (1/2)(14)(4) = 28. Option A forgets the essential 1/2 factor. Option C uses the slanted legs (6 cm each) instead of the parallel sides — the most common conceptual error, since the legs are irrelevant to area. Option D uses only one base instead of adding both."

- question: "Why does the trapezoid area formula include a factor of 1/2?"
  type: multiple-choice
  options:
    - "Because the two bases must be averaged by dividing their sum by 2 before multiplying by height"
    - "Because two identical trapezoids joined together form a parallelogram with area (b₁ + b₂)h, so each trapezoid is exactly half of that"
    - "Because the perpendicular height is always half the length of the slant height"
    - "Because only half of each base contributes to the enclosed interior area"
  answer: 1
  explanation: "The derivation: flip a copy of the trapezoid upside down and attach it to the original along one base. The result is a parallelogram with base (b₁ + b₂) and height h, whose area is (b₁ + b₂)h. Since two trapezoids make one parallelogram, one trapezoid is half: A = (1/2)(b₁ + b₂)h. Option A restates the formula's arithmetic equivalence (average of bases times height) but doesn't explain where the 1/2 comes from. Options C and D describe fictional geometric properties."

- question: "In the formula A = (1/2)(b₁ + b₂)h, b₁ and b₂ can represent any two sides of the trapezoid as long as they are the longest two sides."
  type: true-false
  answer: false
  explanation: "b₁ and b₂ must specifically be the two parallel sides — not the longest sides, not the slanted legs, and not any other pair. The formula only works because the parallel sides define the trapezoid's width at the top and bottom, and the perpendicular height measures the distance between them. Using the slanted legs instead is the most common area calculation error on trapezoid problems."

- question: "A parallelogram can be seen as a special case of a trapezoid where both parallel sides are equal, and applying the trapezoid formula to it produces the standard parallelogram area formula A = bh."
  type: true-false
  answer: true
  explanation: "When b₁ = b₂ = b, the formula becomes A = (1/2)(b + b)h = (1/2)(2b)h = bh — exactly the parallelogram formula. Similarly, when one base shrinks to zero, (1/2)(b + 0)h = (1/2)bh — the triangle formula. This shows all three formulas are the same formula in different conditions, and every polygon area can be understood through decomposition and rearrangement."

- question: "Describe the 'doubling' derivation of the trapezoid area formula. What shape results when two identical trapezoids are combined, and how does this explain both the (b₁ + b₂) term and the 1/2 factor?"
  type: short-answer
  answer: "Flip a copy of the trapezoid upside down and attach it to the original along one of its parallel sides. The result is a parallelogram whose base equals the sum of the two trapezoid bases (b₁ + b₂) and whose height equals the trapezoid's height h. This parallelogram has area (b₁ + b₂)h. Since two trapezoids make up this parallelogram, one trapezoid is half: A = (1/2)(b₁ + b₂)h."
  explanation: "The derivation works because every trapezoid can be paired with its mirror image to form a parallelogram with a clean area formula. The (b₁ + b₂) term arises because the top of one trapezoid and the bottom of its flipped copy together form the full base of the parallelogram. The 1/2 reflects that we want only one of the two trapezoids. This connection to the parallelogram formula shows the area formulas for parallelograms, trapezoids, and triangles as a unified family."
```

## Explainer

A **trapezoid** is a quadrilateral with exactly one pair of parallel sides. Those two parallel sides are called the **bases** (b₁ and b₂), and the perpendicular distance between them is the **height** (h). The fact that the bases are parallel — and not just any two sides — is what makes the area formula work. Before deriving it, notice that you already know the area of a parallelogram from your prerequisite: A = base × height. The trapezoid formula is a direct extension of that idea.

Here is the cleanest derivation. Take your trapezoid and flip an identical copy upside down. Attach the flipped copy to the original along the longer base. The combined shape is a **parallelogram** with base (b₁ + b₂) and height h. Its area is (b₁ + b₂) × h. Since two trapezoids make one parallelogram, one trapezoid is exactly half: A = (1/2)(b₁ + b₂)h. You can also read this as the **average of the two bases** multiplied by the height — think of it as if you replaced the trapezoid with a rectangle whose base is midway between the two parallel sides.

To use the formula correctly, you must identify the two parallel sides, not just any two sides. In a typical trapezoid drawn with one base at the bottom and a shorter base at the top, the height is the vertical distance between them — not the length of the slanted sides. The slanted sides (the **legs**) are irrelevant to the area calculation. If the trapezoid is tilted or drawn in a non-standard orientation, look for the pair of sides that run in the same direction, and drop a perpendicular between them to find h.

The formula connects the trapezoid to the whole family of polygon area results. A parallelogram is a special trapezoid where b₁ = b₂, so (1/2)(b + b)h = bh — exactly the parallelogram formula. A triangle is a degenerate trapezoid where one base shrinks to zero: (1/2)(b + 0)h = (1/2)bh — exactly the triangle formula. This shows that all three formulas are the same formula at heart, and every polygon area can be understood through decomposition and rearrangement of shapes you already know.
