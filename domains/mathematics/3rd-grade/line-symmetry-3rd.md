---
id: line-symmetry-3rd
title: Line Symmetry in Shapes
domain: mathematics
course: 3rd-grade
prerequisites:
- id: shapes-2d-attributes-3rd
  type: hard
builds-toward:
- line-symmetry
tags:
- symmetry
- geometry
- shapes
stage: concrete-operations
status: draft
---

# Line Symmetry in Shapes

## Core Idea
A shape has line symmetry if it can be folded in half along a line so both halves match exactly. A square has 4 lines of symmetry; a rectangle has 2. Students identify and draw lines of symmetry using folding and mirrors.

## Questions

```yaml
- question: "How many lines of symmetry does a rectangle (that is not a square) have?"
  type: multiple-choice
  options:
    - "4, the same as a square"
    - "0, because rectangles have no symmetry"
    - "2, through the midpoints of opposite sides only"
    - "2, along both diagonals"
  answer: 2
  explanation: "A rectangle has exactly 2 lines of symmetry: one connecting the midpoints of the top and bottom sides, and one connecting the midpoints of the left and right sides. The diagonals are NOT lines of symmetry — when you fold a rectangle along a diagonal, the two triangular halves do not align (the corners don't match up). A square has 4 lines of symmetry because its equal side lengths allow the diagonal folds to work; a rectangle's unequal sides prevent this."

- question: "A student draws a diagonal line from corner to corner across a rectangle and claims it is a line of symmetry. Why is the student wrong?"
  type: multiple-choice
  options:
    - "Rectangles cannot have any lines of symmetry at all"
    - "When folded along the diagonal, the two triangular halves do not align — the shorter and longer sides swap positions, so corners don't stack"
    - "Lines of symmetry must always be vertical or horizontal"
    - "The diagonal creates two triangles, and triangles are not allowed in symmetry problems"
  answer: 1
  explanation: "The test for a line of symmetry is folding: both halves must stack exactly. When you fold a non-square rectangle along a diagonal, you get two right triangles — but the short side of one lands on the long side of the other. They don't match. This is the key difference between a rectangle and a square: a square's equal sides mean the diagonal fold works, giving it 4 lines of symmetry. For a rectangle, only the horizontal and vertical midpoint lines pass the fold test."

- question: "A line of symmetry divides a shape into two halves that, when folded along that line, land exactly on top of each other."
  type: true-false
  answer: true
  explanation: "True — this is the definition of a line of symmetry. Every point on one side of the line has a mirror-image point at the exact same distance on the other side. The fold test is what makes this concrete: if any part of one half sticks out past the other, the fold line is not a true line of symmetry. Both halves must be exactly the same shape and size."

- question: "A square and a rectangle always have the same number of lines of symmetry."
  type: true-false
  answer: false
  explanation: "False. A square has 4 lines of symmetry (2 through midpoints of opposite sides, plus 2 diagonals), while a rectangle that is not a square has only 2 (through midpoints of opposite sides). The diagonals of a rectangle fail the fold test because the unequal side lengths prevent the corners from aligning. Equal side lengths are what allow the diagonals to work as lines of symmetry in a square."

- question: "Explain why the fold test is the most reliable way to check whether a proposed line is truly a line of symmetry."
  type: short-answer
  answer: "The fold test directly checks the definition: fold the shape along the proposed line and see if both halves align perfectly. If any edges, corners, or parts of one half extend beyond the other, the line is not a line of symmetry. It replaces guessing based on appearance with a physical test that reveals whether every point on one side truly mirrors the other side."
  explanation: "Visual inspection can be misleading — a line can look like it divides a shape evenly without actually being a line of symmetry. The fold test (or placing a mirror along the line) forces a precise check: does every part of half A land on the corresponding part of half B? This is especially important for diagonal lines on rectangles, which look plausible but fail the test. Relying on 'it looks balanced' leads to the common error of claiming rectangles have 4 lines of symmetry."
```

## Explainer

You already know the attributes of 2D shapes — how many sides they have, whether sides are equal, whether angles are right angles. **Line symmetry** (also called **reflective symmetry**) adds a new kind of attribute: whether a shape can be folded along a line so that both halves land exactly on top of each other. The fold line is called a **line of symmetry**, and any point on one side of the line has a matching point at the exact same distance on the other side.

The most reliable way to find a line of symmetry is to imagine folding. If you fold a square in half diagonally, the two triangular halves stack perfectly — so the diagonal is a line of symmetry. A square has 4 lines of symmetry in total: two diagonals and two lines through the midpoints of opposite sides. A rectangle only has 2 lines of symmetry (both through midpoints of opposite sides), because folding it diagonally gives two halves that don't match up — the corners don't align.

Not every shape has a line of symmetry. A scalene triangle (with all different side lengths) has none. The letter Z has none. The letter A has one vertical line of symmetry. A regular hexagon has six. In general, the more equal a shape's sides and angles are, the more lines of symmetry it tends to have. Counting lines of symmetry is connected to what you know about regularity in shapes.

The practical test is always to fold (or place a mirror along the proposed line) and check. If the two halves don't stack perfectly, the line you drew is not a line of symmetry. The key requirement is that both halves must be exactly the same shape and size — not just similar-looking. Symmetry is about perfect balance, and the line of symmetry is exactly the dividing line where that balance holds.
