---
id: perimeter-finding-3rd
title: Finding Perimeter
domain: mathematics
course: 3rd-grade
prerequisites:
- id: perimeter
  type: soft
- id: measurement-units-standard
  type: hard
- id: perimeter-understanding-2nd
  type: soft
builds-toward:
- perimeter-of-complex-shapes
tags:
- perimeter
- distance
- measurement
stage: concrete-operations
status: validated
---
# Finding Perimeter

## Core Idea
Perimeter is the distance around a shape. Measure each side and add them. A rectangle with sides 4 cm and 3 cm has perimeter 4 + 3 + 4 + 3 = 14 cm.

## How It's Best Learned
Measure each side with a ruler. Use string traced around the shape.

## Common Misconceptions
Confusing perimeter with area; forgetting sides; misaligning the measuring tool.

## Questions

```yaml
- question: "A rectangle has a length of 8 cm and a width of 3 cm. What is its perimeter?"
  type: multiple-choice
  options:
    - "24 cm — multiply length times width"
    - "11 cm — add length and width"
    - "22 cm — add all four sides: 8 + 3 + 8 + 3"
    - "22 cm² — add all four sides using square units"
  answer: 2
  explanation: "Perimeter is the sum of all sides. A rectangle has four sides — two lengths and two widths — so 8 + 3 + 8 + 3 = 22 cm. Option A (24 cm) is the area. Option B (11 cm) adds only one length and one width, forgetting that opposite sides are equal and must both be counted. Option D has the right number but the wrong unit — perimeter is measured in cm (linear), not cm² (area)."

- question: "Two rectangles both have a perimeter of 20 cm. Rectangle A is a square with sides of 5 cm. Rectangle B is 9 cm long and 1 cm wide. What can you conclude about their areas?"
  type: multiple-choice
  options:
    - "Their areas are equal because their perimeters are equal"
    - "Rectangle A has more area — 25 cm² vs. 9 cm² for Rectangle B"
    - "Rectangle B has more area because it is longer"
    - "You cannot compare their areas without measuring the perimeter again"
  answer: 1
  explanation: "Equal perimeters do NOT imply equal areas. Rectangle A (5 × 5) has area 25 cm². Rectangle B (9 × 1) has area 9 cm² — much less, despite the same perimeter. Perimeter measures distance around the boundary; area measures the region inside. A shape stretched thin can have a large perimeter while enclosing very little area. These are independent measurements."

- question: "When finding the perimeter of a five-sided polygon, you must measure and add all five sides, even if two of them appear to be the same length."
  type: true-false
  answer: true
  explanation: "Every side contributes to the perimeter, regardless of how sides look. Unless a diagram explicitly labels sides as equal (or the shape is a known regular polygon), you must measure each one individually. Stopping after the sides that look different, or skipping unlabeled sides, gives an incomplete and incorrect perimeter."

- question: "A shape with a larger perimeter always encloses a larger area than a shape with a smaller perimeter."
  type: true-false
  answer: false
  explanation: "Perimeter and area are independent measurements. A very long, thin rectangle can have a large perimeter while enclosing a tiny area. For example, a 50 cm × 1 cm rectangle has perimeter 102 cm but area only 50 cm². A 10 cm × 10 cm square has perimeter 40 cm but area 100 cm² — smaller perimeter, larger area. The relationship between them depends entirely on the shape."

- question: "A garden is shaped like a rectangle with a length of 10 m and a width of 2 m. Your friend says the perimeter is 12 m. What mistake did your friend make, and what is the correct perimeter?"
  type: short-answer
  answer: "The friend added only one length and one width (10 + 2 = 12) instead of all four sides. A rectangle has two lengths and two widths, so the perimeter is 10 + 2 + 10 + 2 = 24 m. Equivalently: 2 × (10 + 2) = 2 × 12 = 24 m."
  explanation: "This is the most common perimeter error: treating a rectangle as if it only has two sides instead of four. Perimeter means the distance all the way around — you must traverse every side and return to the start. The shortcut 2 × (length + width) works because opposite sides of a rectangle are equal, but the student must first recognize that there are indeed four sides to account for."
```

## Explainer

You've already learned what perimeter means — the total distance around a shape — and you've worked with standard measurement units like centimeters and inches. Finding perimeter is what happens when you combine those two skills: you measure each side with the right unit, then add the lengths together.

The procedure is straightforward, but the discipline matters. Start at any corner of the shape, measure that side, record the length, then move to the next side. Work your way all the way around until you're back where you started. **Every side counts** — for an irregular polygon with five sides, that means five measurements; for a rectangle, four (even though two pairs are equal). A common mistake is stopping after measuring the sides you can see in a diagram and forgetting sides that aren't labeled.

Rectangles offer a useful shortcut worth understanding: opposite sides are equal, so a rectangle with length 6 cm and width 4 cm has perimeter 6 + 4 + 6 + 4 = 20 cm. You can also compute this as 2 × (6 + 4) = 2 × 10 = 20 cm. This "double the sum of length and width" formula works because of the structure of rectangles — but for any other shape, just add all the sides individually.

The key distinction to keep sharp is **perimeter vs. area**. Perimeter is a length — measured in cm, inches, meters — because it's a distance along the boundary. Area is a surface — measured in square cm, square inches — because it covers a region. A wide, flat rectangle and a tall, narrow rectangle can have the same perimeter but very different areas. When a problem asks "how far around?", that's perimeter. When it asks "how much surface?", that's area. Labeling your answer with the correct unit (cm, not cm²) is an easy way to check which one you computed.
