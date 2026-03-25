---
id: 2d-shapes-attributes-2nd
title: Attributes of Two-Dimensional Shapes
domain: mathematics
course: 2nd-grade
prerequisites:
- id: 2d-shapes-attributes
  type: hard
- id: classifying-and-sorting-shapes
  type: soft
- id: 3d-shapes-sorting-2nd
  type: soft
tags:
- shapes
- 2d-shapes
- attributes
stage: concrete-operations
status: validated
---
# Attributes of Two-Dimensional Shapes

## Core Idea
Two-dimensional shapes have attributes: sides (edges), vertices (corners), and angles. Triangles have 3 sides; rectangles have 4 sides with right angles; circles have no sides or corners. Shapes can be sorted by these attributes.

## Questions

```yaml
- question: "A shape has 4 sides, 4 vertices, and all 4 angles are right angles, but one pair of sides is longer than the other pair. What is this shape?"
  type: multiple-choice
  options:
    - "A square — any 4-sided shape with right angles is a square"
    - "Not a real shape — rectangles must have all four sides equal"
    - "A rectangle — rectangles require 4 right angles but sides do not need to be equal"
    - "A rhombus — any quadrilateral with unequal sides is a rhombus"
  answer: 2
  explanation: "A rectangle is defined by two attributes: 4 sides (making it a quadrilateral) and 4 right angles. Side lengths can vary — a rectangle 3 cm × 7 cm is still a rectangle. A square is a special rectangle where all four sides are also equal. Option A confuses rectangles and squares; option D confuses rectangles and rhombuses (which have equal sides but not necessarily right angles)."

- question: "Which attribute do ALL quadrilaterals share, regardless of any other differences?"
  type: multiple-choice
  options:
    - "4 right angles"
    - "4 equal sides"
    - "4 sides and 4 vertices"
    - "At least one pair of parallel sides"
  answer: 2
  explanation: "A quadrilateral is defined as any 2D shape with exactly 4 sides and 4 vertices — nothing more. Rectangles, squares, rhombuses, trapezoids, and irregular four-sided figures are all quadrilaterals simply because they all have 4 sides and 4 vertices. Only some quadrilaterals have right angles (option A), equal sides (option B), or parallel sides (option D). The 4 sides / 4 vertices count is the one thing they all share."

- question: "For any polygon (a closed 2D shape with only straight sides), the number of sides always equals the number of vertices."
  type: true-false
  answer: true
  explanation: "Every time a side ends, it creates a vertex where it meets the next side. A triangle has 3 sides meeting at 3 corners. A pentagon has 5 sides and 5 corners. This is true for all polygons: you can count one or the other, and the result is always the same. This is a useful check: if you count 7 corners on a shape, you should find exactly 7 sides."

- question: "A circle is classified as a shape with 1 very long curved side and 0 vertices."
  type: true-false
  answer: false
  explanation: "A circle has no sides and no vertices at all. Sides are defined as straight line segments that form the boundary of a polygon. A circle's boundary is a continuous curve with no straight segments and no corner points. Circles are specifically excluded from the category of polygons precisely because they have no straight sides and no vertices. Describing a curve as '1 side' misapplies the definition."

- question: "Why is it more reliable to classify a shape by counting its sides, vertices, and angles than by what it looks like? Give an example where appearance might be misleading."
  type: short-answer
  answer: "Appearance is affected by rotation, size, and proportion, which can make shapes look unfamiliar. A rectangle turned 45 degrees still has 4 sides, 4 vertices, and 4 right angles — but it might look like a diamond and be misidentified. By checking attributes (does it have 4 sides? 4 right angles?), you classify correctly regardless of orientation or size. A very 'squashed' rectangle might not look like a 'typical' rectangle, but counting its attributes confirms it is one."
  explanation: "Attribute-based classification is the beginning of mathematical reasoning: you apply a rule rather than pattern-match to a prototype. This matters especially as shapes become less 'typical' — an irregular triangle might not look like the textbook equilateral triangle, but it still has exactly 3 sides and 3 vertices and qualifies as a triangle. Counting attributes is the reliable method; visual matching is not."
```

## Explainer

Every two-dimensional shape has a set of measurable, countable properties called **attributes**. The three most important attributes are **sides** (the straight line segments that form the boundary of the shape), **vertices** (the corner points where two sides meet), and **angles** (the amount of turn at each vertex). You already know how to name and recognize basic shapes — now the goal is to describe *why* a triangle is a triangle and *why* a rectangle is a rectangle using these precise attributes.

Counting sides and vertices is the most reliable way to classify a shape. A triangle always has exactly 3 sides and 3 vertices. A quadrilateral always has 4 sides and 4 vertices — rectangles, squares, and rhombuses are all quadrilaterals because they all share this count. Pentagons have 5, hexagons have 6. Notice a pattern: for straight-sided shapes, the number of sides always equals the number of vertices. If you count 5 corners on a shape, you will always find 5 sides.

Angles add a deeper layer of description. A **right angle** looks like the corner of a piece of paper — it is a perfect 90-degree turn. Rectangles are special quadrilaterals because *all four* of their angles are right angles. A square is even more special: it has four right angles *and* all four sides equal. Triangles can have right angles too, but they cannot have more than one (three right angles would require more than 180 degrees total, which a triangle cannot have). Circles are the exception to all of this: they have no sides, no vertices, and no angles — just one continuous curved boundary.

Sorting shapes by attributes is a powerful reasoning tool. Instead of memorizing that "this looks like a rectangle," you can check: Does it have 4 sides? Yes. Does it have 4 right angles? Yes. Then it is a rectangle, no matter how it is rotated or what size it is. Two shapes can share some attributes but not others — a square and a non-square rectangle both have 4 right angles, but only the square has all sides equal. Learning to ask "what do these shapes have in common?" and "how are they different?" is the beginning of geometric reasoning.
