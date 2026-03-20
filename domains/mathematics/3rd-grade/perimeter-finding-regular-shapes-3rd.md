---
id: perimeter-finding-regular-shapes-3rd
title: Finding Perimeter of Rectangles and Squares
domain: mathematics
course: 3rd-grade
prerequisites:
- id: perimeter-finding-3rd
  type: hard
builds-toward:
- perimeter
tags:
- perimeter
- rectangles
- squares
stage: concrete-operations
status: draft
---

# Finding Perimeter of Rectangles and Squares

## Core Idea
Perimeter is the distance around a shape. For rectangles and squares, it's the sum of all side lengths. A rectangle with sides 3 and 5 has perimeter 3 + 5 + 3 + 5 = 16 units. For a square, perimeter = 4 × side length.

## Questions

```yaml
- question: "A rectangle has a length of 7 cm and a width of 4 cm. What is its perimeter?"
  type: multiple-choice
  options:
    - "11 cm — add length and width"
    - "28 cm — multiply length by width"
    - "22 cm — add all four sides: 7 + 4 + 7 + 4"
    - "14 cm — double the length only"
  answer: 2
  explanation: "Perimeter is the total distance around all four sides. A rectangle with length 7 and width 4 has sides of 7, 4, 7, and 4 (opposite sides are equal). Adding all four: 7 + 4 + 7 + 4 = 22 cm. Option A only adds two sides. Option B (7 × 4 = 28) calculates area — the space inside — not the distance around. Option D only doubles one side. The formula 2 × (7 + 4) = 22 gives the same correct answer."

- question: "A student computes 4 × 7 = 28 square centimeters for a rectangle with length 7 cm and width 4 cm. What measurement did the student calculate?"
  type: multiple-choice
  options:
    - "Perimeter — the distance around the rectangle"
    - "Area — the amount of space enclosed inside the rectangle"
    - "Both area and perimeter — they are the same for rectangles"
    - "Neither — you cannot use multiplication for rectangles"
  answer: 1
  explanation: "4 × 7 = 28 square centimeters is the area of the rectangle — how much surface is enclosed inside. Area is measured in square units (cm², m², ft²). Perimeter is 2 × 7 + 2 × 4 = 22 cm — the distance around the outside, measured in linear units (cm, m, ft). Confusing these two is one of the most persistent errors in geometry. They are different measurements, computed differently, used to answer different questions, and expressed in different units."

- question: "For a rectangle with length 5 and width 3, the perimeter equals 5 + 3 = 8 units."
  type: true-false
  answer: false
  explanation: "This is a very common error — adding only two sides instead of all four. A rectangle has four sides: two lengths and two widths. The perimeter is 5 + 3 + 5 + 3 = 16 units, or equivalently 2 × (5 + 3) = 16. Adding only length + width gives half the perimeter. Remember: perimeter is the distance all the way around the shape, which means you must account for every side."

- question: "Perimeter is measured in linear units (like cm or feet), not square units."
  type: true-false
  answer: true
  explanation: "Perimeter is a distance — how far you'd travel if you walked around the outside edge of a shape. Distance is measured in linear units: centimeters, meters, inches, feet. Area, by contrast, measures how much surface is enclosed, and is measured in square units (cm², m², ft²). Keeping this distinction clear matters for both calculation and interpretation: baseboard trim is measured in linear feet (perimeter), while carpet or flooring is measured in square feet (area)."

- question: "Why is the formula for the perimeter of a rectangle 2 × length + 2 × width, rather than just length × width?"
  type: short-answer
  answer: "Because perimeter is the sum of all four sides, not a product of two sides. A rectangle has two sides equal to the length and two equal to the width. Adding all four gives length + width + length + width, which is the same as 2 × length + 2 × width. Multiplying length × width gives area — the space inside — which is a completely different measurement."
  explanation: "The formula 2l + 2w is just a compressed way of adding all four sides of a rectangle: l + w + l + w = 2l + 2w. It's useful because it reduces four additions to two multiplications, but it comes directly from the definition of perimeter. Length × width is the area formula — it counts how many unit squares fit inside. These two formulas answer two completely different geometric questions about the same shape."
```

## Explainer

You've already worked with the general idea of perimeter — the total distance around the outside of a shape — by adding up all side lengths. Now you're focusing on two special shapes, **rectangles** and **squares**, where the side lengths follow predictable patterns that let you compute perimeter more efficiently.

For a rectangle with length 5 and width 3, the four sides are 5, 3, 5, and 3. Adding them: 5 + 3 + 5 + 3 = 16. Notice you're adding each dimension exactly twice. That pattern leads to a shortcut: **perimeter of a rectangle = 2 × length + 2 × width**, or equivalently 2 × (length + width). Both expressions are just compressed ways of adding all four sides. Use whichever feels more natural — they always give the same result.

A square is a rectangle where all four sides are equal. If one side is 6 units, perimeter = 6 + 6 + 6 + 6 = 24, or faster: **4 × side length**. This formula isn't a rule to memorize blindly — it falls directly out of the fact that you're adding the same number four times, which is what multiplication means. You already know multiplication, so a formula that replaces four additions with one multiplication is just efficiency.

An important distinction to keep clear: perimeter is a **linear measurement** — it's a distance, measured in units like centimeters or feet. Area, which you'll study soon, measures how much space is enclosed inside a shape — and uses square units. The perimeter of a room is how much baseboard trim you'd need along the walls; the area is how much flooring you'd need to cover the floor. Two different questions, two different measurements, both about the same shape. Keeping this distinction sharp now will prevent a very common confusion that trips students up for years.
