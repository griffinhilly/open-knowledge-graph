---
id: area-rectilinear-shapes
title: Area of Rectilinear Shapes
domain: mathematics
course: 3rd-grade
prerequisites:
- id: area-by-counting-squares
  type: hard
- id: area-of-rectangles
  type: hard
builds-toward:
- area-of-parallelograms
- area-of-triangles
- decomposing-shapes
tags:
- area
- rectilinear
- decompose
- compound-shapes
stage: concrete-operations
status: validated
---

# Area of Rectilinear Shapes

## Core Idea
Rectilinear shapes are polygons with all right angles — L-shapes, T-shapes, and other stepped figures. Their area is found by decomposing (breaking apart) the shape into non-overlapping rectangles, finding each rectangle's area, and adding the parts together. Alternatively, students can find the area of a larger containing rectangle and subtract the missing piece.

## How It's Best Learned
Draw dashed lines on L-shapes to show the decomposition. Have students label the dimensions of each resulting rectangle, calculate each area, and add. Comparing the 'add parts' and 'subtract missing piece' strategies builds flexibility.

## Common Misconceptions
- Forgetting to find missing side lengths before calculating area.
- Adding both the part areas and the total area (double-counting).

## Questions

```yaml
- question: "A student calculates the area of an L-shaped figure. The bounding rectangle (the smallest rectangle that surrounds the L) would be 10 × 8 = 80 square units. The rectangular notch cut from the corner is 4 × 3 = 12 square units. The student writes 80 + 12 = 92 square units as the answer. What went wrong?"
  type: multiple-choice
  options:
    - "The student should have multiplied both areas together instead"
    - "The student added the notch area instead of subtracting it — the notch is the part that is missing, so it must be removed from the total"
    - "The subtraction method does not work for L-shapes; only splitting into rectangles is valid"
    - "The student calculated the bounding rectangle incorrectly"
  answer: 1
  explanation: "The subtraction strategy works by finding the area of the large containing rectangle, then removing the area of the missing piece. The notch is not part of the shape — it is a chunk that was cut away — so its area must be subtracted, not added. 80 − 12 = 68 square units is the correct answer. Adding the notch is a common error that results from misunderstanding what the notch represents: a missing piece, not an extra piece."

- question: "When decomposing an L-shape into two rectangles to find total area, a student gets the wrong answer even though her multiplication is correct. What is the most likely cause?"
  type: multiple-choice
  options:
    - "She should have used addition instead of multiplication for each rectangle's area"
    - "She forgot to add the two rectangle areas at the end"
    - "She used incorrect side lengths for the component rectangles, likely because she did not figure out the missing dimensions first"
    - "L-shapes cannot be decomposed into exactly two rectangles"
  answer: 2
  explanation: "Correct multiplication is only useful if the dimensions fed into it are correct. The critical prerequisite step is determining any missing side lengths from the labeled dimensions. In rectilinear shapes, opposite sides along any straight line must total the same amount, which is how missing lengths are derived. Skipping this step means the rectangle dimensions are wrong, and even perfect multiplication produces the wrong area."

- question: "To find the area of a rectilinear shape, you must always split it into rectangles and add the parts — the subtraction method is not a valid alternative."
  type: true-false
  answer: false
  explanation: "Both strategies are equally valid and always produce the same answer. The 'add the parts' method decomposes the shape into non-overlapping rectangles, computes each area, and sums them. The 'subtract the missing piece' method computes the area of a bounding rectangle and subtracts the rectangular notch. The choice between them depends on which side lengths are easier to work with — not on which method is more correct."

- question: "In a rectilinear shape, you can calculate any missing side length by looking at the dimensions on the opposite side of the figure."
  type: true-false
  answer: true
  explanation: "Because all angles in a rectilinear shape are right angles, every horizontal span must be accounted for by horizontal dimensions, and every vertical span by vertical dimensions. Opposite sides along a straight run must sum to the same total. This means any unlabeled side length can be found by subtracting the labeled partial lengths on the same side from the total length given on the opposite side."

- question: "Why is finding the missing side lengths the most critical step when calculating the area of an L-shaped figure?"
  type: short-answer
  answer: "The missing side lengths define the dimensions of the component rectangles. Without them, you cannot compute any rectangle's area — you do not know what to multiply. In an L-shape, not all sides are labeled; you must derive the unlabeled lengths from the labeled ones by recognizing that opposite sides must account for the same total span. If you skip this step, every area calculation that follows will be based on wrong dimensions, no matter how accurately you apply length × width."
  explanation: "This step is where most errors in rectilinear area problems originate. The arithmetic (multiplication and addition or subtraction) is usually straightforward; the conceptual challenge is seeing that the shape's right-angle structure provides enough information to determine all missing lengths before any calculation begins."
```

## Explainer

You already know two things: how to find the area of a rectangle using length × width, and that area counts the unit squares covering a surface. Now you will combine those skills to tackle shapes that aren't simple rectangles — the L-shapes, T-shapes, and stepped figures called **rectilinear shapes**. The key insight is that every rectilinear shape is secretly several rectangles stuck together.

Take an L-shape. It looks like a single irregular polygon, but draw one dashed line in the right place and it splits cleanly into two rectangles. Find each rectangle's dimensions, compute each area (length × width), and add the two results. The total area equals the sum of its parts. The tricky step is determining **missing side lengths** — the dimensions that aren't directly labeled on the figure. Because all angles in a rectilinear shape are right angles, every missing length can be calculated by looking at what's on the opposite side: sides facing each other along a straight line must add up to the same total.

A second strategy sometimes saves work: **subtraction**. Imagine drawing the smallest possible rectangle that completely surrounds the L-shape — a large rectangle with a rectangular notch cut out of one corner. Calculate the big rectangle's area, then calculate the notch's area, and subtract. Both the "add the pieces" method and the "subtract the missing chunk" method always produce the same answer. Choosing between them is just a matter of which side lengths are easier to work with on a given problem.

The deeper idea here is **decomposition**: when a shape seems too complicated, break it into simpler pieces you already know how to handle, solve each piece, then recombine. This strategy — reduce a hard problem to a collection of easy ones — extends far beyond geometry. It appears in every branch of mathematics and is one of the most important problem-solving habits you can build.
