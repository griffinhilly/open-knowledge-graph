---
id: area-of-rectangles
title: Area of Rectangles
domain: mathematics
course: 4th-grade
prerequisites:
- id: perimeter
  type: soft
- id: arrays
  type: soft
- id: area-by-counting-squares
  type: soft
- id: area-by-unit-squares-3rd
  type: hard
builds-toward:
- volume-of-rectangular-prisms
- measurement-conversions-customary
tags:
- measurement
- geometry
- area
- multiplication
stage: concrete-operations
status: validated
---
# Area of Rectangles

## Core Idea
Area measures the amount of surface a shape covers, expressed in square units (square inches, square centimeters, etc.). For rectangles, area = length x width, because you can tile the rectangle with rows of unit squares: the number of rows times the number of squares per row gives the total count. Area is fundamentally a multiplication concept -- it is arguably the most important real-world model for what multiplication means. Understanding area prepares students for volume (which adds a third dimension) and for the area of more complex shapes in later grades.

## How It's Best Learned
Start with physical tiling: cover a rectangle with square tiles and count them. Then organize the count as rows-times-columns. Move from counting to the formula, but keep returning to the tiling interpretation to maintain meaning. Practice finding areas of composite shapes by decomposing them into rectangles. Always include units in answers.

## Common Misconceptions
- Confusing area with perimeter (adding side lengths instead of multiplying).
- Forgetting that area is measured in square units, not linear units.
- When finding the area of an L-shaped figure, double-counting or omitting the overlapping region when decomposing.

## Questions

```yaml
- question: "A rectangle is 8 cm long and 5 cm wide. Which of the following correctly states its area?"
  type: multiple-choice
  options: ["13 cm", "26 cm", "40 cm", "40 cm²"]
  answer: 3
  explanation: "Area = length × width = 8 × 5 = 40. The result must be in square centimeters (cm²), not centimeters — area measures surface, not length, so its unit is always a square unit. Option A (13 cm) adds the dimensions instead of multiplying, which finds neither area nor perimeter correctly. Option B (26 cm) finds the perimeter (2 × 8 + 2 × 5), a different measurement entirely. Option C (40 cm) gets the number right but uses the wrong unit."

- question: "Area and perimeter both measure the same property of a rectangle — they just use different formulas."
  type: true-false
  answer: false
  explanation: "Area and perimeter measure completely different things. Perimeter is the total length of the boundary — it is measured in linear units (cm, m, etc.) and tells you how far you would walk around the rectangle. Area is the amount of surface the rectangle covers — measured in square units (cm², m²) and tells you how many unit squares fit inside. Two rectangles can have the same perimeter but very different areas, and vice versa."

- question: "Explain in your own words why the area formula for a rectangle is length × width and not length + width."
  type: short-answer
  answer: "If you tile a rectangle with unit squares, the number of squares in each row equals the width, and the number of rows equals the length. The total count of squares is the number of rows times the number per row — length times width. Addition would only give the number of squares along two sides, not the full interior."
  explanation: "Multiplication counts the total entries in a rectangular array — this is the core model for what multiplication means. Area is arguably the most important physical application of this idea. Addition (length + width) is the wrong operation because it combines two measurements of different rows/columns rather than counting all squares across the entire grid."
```

## Explainer

When you want to know how much carpet covers a floor, how much paint covers a wall, or how much grass fits in a yard, you are asking about area — the amount of flat surface a shape takes up. Area is measured in square units: square centimeters (cm²), square feet (ft²), and so on, because you are counting how many unit squares fit inside the shape.

For a rectangle, the formula is area = length × width. The reason this works comes directly from the idea of tiling. Imagine filling the inside of a rectangle with 1-centimeter square tiles. They line up in neat rows: if the rectangle is 6 cm long and 4 cm wide, you get 4 tiles in each row and 6 rows total. The grand total is 6 × 4 = 24 tiles — 24 cm² of area. The formula packages this row-counting into a single multiplication, which is exactly why multiplication and area are so closely linked as concepts. Arrays — the rectangular arrangements of objects you may have seen in earlier grades — are the same idea in a different setting.

A mistake that catches many students is confusing area with perimeter. Perimeter is the distance all the way around the outside edge of the shape — you add up all the side lengths. For the same 6 × 4 rectangle, the perimeter is 6 + 4 + 6 + 4 = 20 cm (linear units, no squaring). Area fills the inside; perimeter traces the outside. They are measuring completely different things. A quick check: area answers "how much surface?", perimeter answers "how long is the border?"

The unit matters as much as the number. Area is always expressed in square units because you are counting squares. If you measure a room in feet and get 120, you must write 120 ft², not 120 ft. Writing 120 ft would mean a length of 120 feet — a very different claim. Making the unit explicit in every answer is part of doing the mathematics correctly, not just a bookkeeping habit.

Once you are comfortable with rectangles, you can find the area of more complex shapes — like L-shapes or staircases — by breaking them into smaller rectangles, finding each piece's area, and adding the pieces together. This decomposition strategy will appear again when you study volume (adding a third dimension to area) and when you work with irregular shapes in later geometry.
