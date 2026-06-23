---
id: area-of-rectangles-3rd
title: Area of Rectangles
domain: mathematics
course: 3rd-grade
prerequisites:
- id: area-by-unit-squares-3rd
  type: hard
tags:
- area
- rectangles
- formula
stage: concrete-operations
status: validated
---

# Area of Rectangles

## Core Idea
The area of a rectangle is length times width: A = l × w. A 5-by-3 rectangle has area 5 × 3 = 15 square units. This works because length and width create the array structure.

## How It's Best Learned
Use grid paper to verify the formula. Measure rectangles and calculate area.

## Common Misconceptions
Using wrong dimensions; confusing area with perimeter; forgetting square units.

## Questions

```yaml
- question: "A rectangle is 7 centimeters long and 4 centimeters wide. What is its area?"
  type: multiple-choice
  options:
    - "11 square centimeters — add the length and width"
    - "22 centimeters — add all four sides"
    - "28 square centimeters — multiply length times width"
    - "28 centimeters — multiply length times width"
  answer: 2
  explanation: "Area = length × width = 7 × 4 = 28 square centimeters. Option A confuses area with addition. Option B gives the perimeter (2 × 7 + 2 × 4 = 22 cm). Option D has the right number but wrong units — area is always in square units because it measures a two-dimensional surface, not a one-dimensional length."

- question: "Why does the formula A = l × w work for finding the area of a rectangle?"
  type: multiple-choice
  options:
    - "Because length and width are the only two measurements of a rectangle, so they must be multiplied"
    - "Because multiplying is faster than adding, and area problems need quick answers"
    - "Because the rectangle can be filled with rows and columns of unit squares, and multiplication counts that array"
    - "Because area formulas are rules mathematicians agreed on, not explanations of why they work"
  answer: 2
  explanation: "The formula comes from the array structure. A 5-by-3 rectangle can be filled with 3 rows of 5 unit squares each — exactly the equal-groups model of multiplication. Multiplying counts all the squares without listing them one by one. The formula is not arbitrary — it is a shortcut for counting a rectangular arrangement of unit squares."

- question: "A rectangle with a perimeter of 20 cm has an area of 20 square centimeters."
  type: true-false
  answer: false
  explanation: "Perimeter and area are different measurements. A rectangle could have a perimeter of 20 cm with many different areas depending on its dimensions. For example, an 8×2 rectangle has perimeter 20 cm but area 16 sq cm; a 6×4 rectangle has perimeter 20 cm but area 24 sq cm. The two measures are independent."

- question: "If you know that 6 × 8 = 48, you already know the area of a 6-by-8 rectangle in square units — no separate formula is needed."
  type: true-false
  answer: true
  explanation: "The area formula A = l × w is simply multiplication applied to rectangle dimensions. Knowing 6 × 8 = 48 directly gives the area as 48 square units. The formula is not a separate procedure — it is the same multiplication you already know, applied to the specific case of a rectangular array of unit squares."

- question: "What is the difference between area and perimeter, and why must area always be expressed in square units rather than regular units?"
  type: short-answer
  answer: "Perimeter measures the distance around the outside of a shape — it is a length, measured in regular units (cm, inches). Area measures the surface covered — how many unit squares fill the shape — measured in square units (sq cm, sq in). Area requires square units because you are counting two-dimensional squares, not one-dimensional lengths."
  explanation: "The distinction comes down to what you are measuring: a line (1D, regular units) versus a surface (2D, square units). Forgetting square units is a persistent error because students write the number correctly but omit the 'square' qualifier. The unit matters: 28 cm describes a length; 28 sq cm describes a surface covering 28 unit squares."
```

## Explainer

You already know that **area** is measured by counting unit squares — small squares each covering exactly one square unit of space. When you covered a rectangle with unit squares before, you probably noticed that the squares lined up into neat rows and columns. A rectangle that is 5 units long and 3 units wide forms an array of squares: 5 columns of 3, or 3 rows of 5. Instead of counting all 15 squares one by one, you can multiply: 5 × 3 = 15. That is where the formula **A = l × w** (area equals length times width) comes from — it is just a shortcut for counting a rectangular array.

This connection to multiplication is not a coincidence. The same thinking that tells you "4 groups of 6 is 24" tells you that a 4-by-6 rectangle covers 24 square units. Area and multiplication are two ways of describing the same structure. When you draw grid lines on your rectangle and see 4 rows of 6 squares each, you are looking at a multiplication fact in geometric form.

The most important thing to remember is that area is measured in **square units** — not just units. A rectangle that is 5 inches long and 3 inches wide has an area of 15 **square inches**, because you are counting squares, not line segments. This is different from perimeter, which measures the distance around the outside of the shape and is counted in regular units (inches, centimeters). Perimeter goes around; area fills in. A common way to keep them straight: if you were fencing a yard, you need perimeter; if you were laying carpet, you need area.

To avoid using the wrong dimensions, always label what you measure. Length is one side of the rectangle; width is the adjacent side. It does not matter which you call "length" and which you call "width" — the product is the same. What matters is that you use two different sides, not the same side twice. If a rectangle is 6 cm on one pair of sides and 4 cm on the other pair, its area is 6 × 4 = 24 square centimeters.
