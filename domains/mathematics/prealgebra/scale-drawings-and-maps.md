---
id: scale-drawings-and-maps
title: Scale Drawings and Maps
domain: mathematics
course: prealgebra
prerequisites:
- id: proportions
  type: hard
- id: solving-proportions
  type: hard
builds-toward:
- similar-triangles-aa
tags:
- scale
- proportions
- geometry
- measurement
- applications
stage: abstract-reasoning
status: validated
---
# Scale Drawings and Maps

## Core Idea
A scale drawing is a proportional representation of an object or space, where every length in the drawing corresponds to a real length by a fixed ratio called the scale factor. If a map uses a scale of 1 cm = 50 km, then 3 cm on the map represents 150 km in reality. Scale drawings apply proportional reasoning to geometry — they are the practical application of equivalent ratios. This topic connects to the concept of similar figures in geometry, where corresponding lengths are proportional and corresponding angles are equal.

## How It's Best Learned
Have students create scale drawings of their classroom or bedroom. Use maps to calculate real distances. Practice setting up and solving proportions with the scale factor. Emphasize that the scale factor applies to all lengths uniformly but not to areas (area scales by the square of the scale factor).

## Common Misconceptions
- Applying the scale factor to area (a 2x scale doubles lengths but quadruples area).
- Setting up the proportion with mismatched units (mixing drawing units with real units incorrectly).
- Confusing "scale up" and "scale down" — the scale factor can be greater than or less than 1.

## Questions

```yaml
- question: "A floor plan uses a scale of 1 cm = 4 m. A room measures 3 cm × 5 cm on the plan. What is the room's actual area?"
  type: multiple-choice
  options:
    - "60 m² — multiply the drawing area (15 cm²) by the scale factor (4)"
    - "240 m² — the actual dimensions are 12 m × 20 m, so area = 240 m²"
    - "15 m² — area in the drawing equals area in reality when scale is applied"
    - "120 m² — multiply the drawing area by the scale factor squared divided by 2"
  answer: 1
  explanation: "The actual dimensions are 3 × 4 = 12 m and 5 × 4 = 20 m, giving an actual area of 12 × 20 = 240 m². The most tempting wrong answer is option A: students often multiply the drawing area (15 cm²) directly by the scale factor (4), getting 60 m². But area scales by the square of the scale factor — k = 4 means area scales by k² = 16. So 15 × 16 = 240 m². Lengths scale linearly; area does not."

- question: "A scale model of a car is built at 1:20 (every 1 cm on the model = 20 cm on the real car). If it takes 1 can of paint to cover the model, approximately how many cans would be needed to paint the real car's surface?"
  type: multiple-choice
  options:
    - "20 cans — the real car is 20 times larger, so it needs 20 times as much paint"
    - "40 cans — double the scale factor to account for both dimensions"
    - "400 cans — surface area scales by the square of the scale factor (20² = 400)"
    - "8,000 cans — volume scales by the cube of the scale factor"
  answer: 2
  explanation: "Paint covers surface area, and area scales by k² where k is the linear scale factor. Here k = 20, so area scales by 400. The real car needs 400 times as much paint as the model. Option A (×20) is the classic misconception — applying the linear scale factor to area. The scale factor of 20 applies to each linear dimension; since area = length × width, the scale factor applies twice: 20 × 20 = 400."

- question: "On a map with scale 1:50,000, a distance of 3 cm represents 1.5 km in reality."
  type: true-false
  answer: true
  explanation: "At 1:50,000, every 1 cm on the map represents 50,000 cm = 500 m = 0.5 km in reality. So 3 cm represents 3 × 0.5 = 1.5 km. This is correct. The proportion is straightforward: 1 cm → 0.5 km, so multiply both sides of the ratio by 3."

- question: "If a scale drawing is enlarged by a factor of 3 (most lengths become 3 times as long), the total area of the drawing also becomes 3 times as large."
  type: true-false
  answer: false
  explanation: "When lengths scale by a factor of 3, area scales by 3² = 9. A rectangle that is 2 × 4 has area 8; scaled up by 3, it becomes 6 × 12 = area 72 — nine times larger, not three times. Area is length × length, so the scale factor applies twice. Students commonly assume area scales linearly with lengths, but the exponent changes for different dimensions: lengths scale by k, areas by k², volumes by k³."

- question: "Why doesn't the scale factor for lengths also apply directly to areas? Explain the mathematical reason."
  type: short-answer
  answer: "Area is calculated by multiplying two lengths together (e.g., length × width). When you scale both lengths by a factor of k, the area becomes (k × length) × (k × width) = k² × (length × width). So the area is multiplied by k², not k. For example, if you double all lengths (k = 2), a 3 m × 4 m room becomes 6 m × 8 m, and the area goes from 12 m² to 48 m² — four times as large, not twice."
  explanation: "This is not a special rule — it follows directly from the definition of area as a product of two lengths. Any time you have a quantity formed by multiplying dimensions together, the scale factor applies once per dimension: lengths scale by k¹, areas (two dimensions) by k², volumes (three dimensions) by k³. Recognizing this pattern prevents the persistent error of applying the linear scale factor to areas."
```

## Explainer

You already know how to work with proportions: two ratios that are equal, like 3/6 = 1/2. A scale drawing is simply the physical application of that idea — every length in the drawing is in the same ratio to the corresponding real length. If the scale on a map says "1 inch = 50 miles," then 3 inches represents 150 miles, 0.5 inches represents 25 miles, and so on. The **scale factor** is that constant ratio: drawing length / real length (or equivalently real length / drawing length, as long as you're consistent). Once you know the scale factor, any measurement problem becomes a proportion.

Setting up the proportion correctly is the practical skill. Suppose a floor plan uses a scale of 1 cm = 4 m, and a room measures 3.5 cm on the plan. To find the real length, write: (1 cm)/(4 m) = (3.5 cm)/(? m). Cross-multiply: ? = 3.5 × 4 = 14 m. You can also think of it as: real length = drawing length × scale factor (where the scale factor here means "4 m per 1 cm"). The key is that the units must match within each ratio — drawing units on top in both fractions, real units on the bottom in both. Mismatching units is the most common error, and it always produces nonsensical answers.

The most important concept beyond basic conversions is how scaling affects **area**. If every length doubles (scale factor of 2), then a room that is 3 m × 4 m becomes 6 m × 8 m. The original area is 12 m², and the scaled area is 48 m² — it quadrupled. Lengths scale by the scale factor, but areas scale by the square of the scale factor. A scale factor of k multiplies every length by k and every area by k². This is not an exception or a trick — it follows directly from the definition of area as length × length, so applying k to each length gives k × k = k² applied to the area. A model car built at 1:20 scale has bodywork panels that are 1/20 the size in length, but only 1/400 the area.

Scale drawings appear everywhere: architectural blueprints, topographic maps, scientific diagrams of cells or solar systems, and model kits. In each case, the same logic applies — a fixed scale ratio links the representation to reality, and proportional reasoning unlocks every measurement. This topic connects forward to **similar figures** in geometry, where two shapes are similar when all corresponding lengths are in the same ratio. Scale drawings are, in effect, similar figures: the drawing and the real object have the same shape (corresponding angles equal) with all lengths in proportion.
