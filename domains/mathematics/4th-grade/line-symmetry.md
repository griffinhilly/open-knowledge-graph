---
id: line-symmetry
title: Line Symmetry
domain: mathematics
course: 4th-grade
prerequisites:
- id: points-lines-rays-segments
  type: soft
- id: line-symmetry-in-shapes-3rd
  type: soft
builds-toward:
- classifying-2d-shapes
tags:
- geometry
- symmetry
- shapes
stage: concrete-operations
status: validated
---
# Line Symmetry

## Core Idea
A figure has line symmetry if it can be folded along a line so that the two halves match exactly. The fold line is called the line of symmetry (or axis of symmetry). Some figures have one line of symmetry (like the letter A), some have multiple (a square has four), and some have none (a scalene triangle). Recognizing symmetry develops spatial reasoning and is important in art, design, nature, and later mathematics (symmetry of graphs, geometric transformations).

## How It's Best Learned
Fold paper cutouts to test for symmetry physically. Use mirrors along a proposed line of symmetry to see if the reflection completes the shape. Have students draw lines of symmetry on letters, shapes, and real-world images. Challenge students to find all lines of symmetry for regular polygons.

## Common Misconceptions
- Thinking every shape has a line of symmetry.
- Drawing diagonal lines on rectangles as lines of symmetry (only the horizontal and vertical midlines are lines of symmetry for non-square rectangles).
- Confusing line symmetry with rotational symmetry.

## Questions

```yaml
- question: "How many lines of symmetry does a square have?"
  type: multiple-choice
  options:
    - "1 — just the vertical midline"
    - "2 — the horizontal and vertical midlines only"
    - "4 — the two midlines and both diagonals"
    - "0 — the sides are equal, so no one line divides it differently"
  answer: 2
  explanation: "A square has 4 lines of symmetry: the vertical midline, the horizontal midline, and both diagonals. All four fold the square so both halves align perfectly. A non-square rectangle only has 2 (the two midlines) because its diagonals fold to triangles whose long and short sides don't match."

- question: "A student draws a diagonal on a non-square rectangle and says it is a line of symmetry because it 'divides the rectangle into two equal triangles.' What is the error in this reasoning?"
  type: multiple-choice
  options:
    - "A rectangle cannot be divided along a diagonal"
    - "Dividing into two pieces of equal area is not the same as a line of symmetry — the two triangles don't match when folded"
    - "Only horizontal lines can be lines of symmetry for rectangles"
    - "Non-square rectangles have no lines of symmetry at all"
  answer: 1
  explanation: "A line of symmetry requires the two halves to be mirror images that align exactly when folded. Folding a non-square rectangle along a diagonal produces two triangles that don't align: the long side of one overhang the short side of the other. Dividing in half by area is a weaker condition than symmetry — the rectangle has exactly 2 lines of symmetry, both midlines."

- question: "A shape can be divided into two halves of equal area without having a line of symmetry."
  type: true-false
  answer: true
  explanation: "True. Many lines can split a shape into equal areas without either half being a mirror image of the other. The diagonal of a non-square rectangle cuts it into two equal-area triangles, but they don't fold to match — corners land in wrong positions. Line symmetry requires mirror-image matching, not just equal areas."

- question: "A regular pentagon has exactly 5 lines of symmetry."
  type: true-false
  answer: true
  explanation: "True. A regular polygon with n sides has exactly n lines of symmetry. A regular pentagon has 5 sides, so it has 5 lines of symmetry — one through each vertex and the midpoint of the opposite side. This pattern holds for all regular polygons."

- question: "What does it mean for a line to be a 'line of symmetry'? Why does the vertical midline of a rectangle qualify, but its diagonal does not?"
  type: short-answer
  answer: "A line of symmetry divides a figure into two halves that are exact mirror images — when folded along that line, both halves align perfectly with no part sticking out. The vertical midline of a rectangle works because folding places the left half exactly over the right half. The diagonal doesn't work because the corners and sides land in wrong positions — the two triangles formed are congruent but do not fold onto each other."
  explanation: "The test for a line of symmetry is folding, not measuring area. 'Equal halves' by area is a weaker condition than mirror-image symmetry. For true symmetry, every point on one side must have a matching point at the same distance on the other side — and that only happens with the rectangle's midlines."
```

## Explainer

A **line of symmetry** is a line that divides a figure into two halves that are mirror images of each other — the two halves match exactly when the shape is folded along that line. Think of folding a piece of paper: if you can fold the figure so that both halves align perfectly and no part sticks out, the fold line is a line of symmetry. You've worked with lines, rays, and segments, so you can think of the line of symmetry as a special line with a particular relationship to the shape: every point on one side has a matching point at the same distance on the other side.

Not every shape has a line of symmetry, and those that do may have exactly one or several. The letter A has one vertical line of symmetry. A square has four — the two midlines (horizontal and vertical) and the two diagonals. An equilateral triangle has three lines of symmetry, one through each vertex and the midpoint of the opposite side. A **regular polygon** with n sides always has exactly n lines of symmetry, which is one reason regular polygons feel visually balanced and pleasing. A scalene triangle (all different side lengths) has zero.

A common trap with rectangles: it seems like the diagonal should be a line of symmetry because it "divides the rectangle in half," but half in area is not the same as half in shape. If you fold a non-square rectangle along a diagonal, the corners don't match — you get a right triangle overlapping a right triangle, but the long sides overhang. Only the horizontal and vertical midlines fold a rectangle so both halves line up perfectly. For a square, the diagonals also work, because all sides are equal.

Line symmetry shows up everywhere once you start looking: butterfly wings, human faces (approximately), letters of the alphabet, snowflakes, architectural facades, and leaf shapes. In mathematics, it reappears in function graphs — a parabola is symmetric about its vertical axis of symmetry, a foundational concept in algebra. The geometric intuition you build now — what it means for two halves to "match" — carries forward directly into those more abstract settings.
