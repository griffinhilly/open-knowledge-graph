---
id: triangle-inequality
title: Triangle Inequality Theorem
domain: mathematics
course: geometry
prerequisites:
- id: segment-and-distance
  type: hard
- id: triangle-angle-sum
  type: soft
- id: exterior-angle-theorem
  type: soft
builds-toward:
- similar-triangles-aa
tags:
- triangles
- inequality
- side-lengths
stage: abstract-reasoning
status: validated
---
# Triangle Inequality Theorem

## Core Idea
The Triangle Inequality Theorem states that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side. Equivalently, the difference of any two sides must be less than the third side. This determines whether three given lengths can form a triangle. It also implies that the shortest path between two points is a straight line.

## How It's Best Learned
Give students sets of three lengths and ask them to determine which can form triangles. Use physical sticks or straws to demonstrate that if two short sides cannot "reach" across the long side, no triangle forms. Formalize into three inequalities (a + b > c, a + c > b, b + c > a) and note that only the case with the longest side matters.

## Common Misconceptions
- Using >= instead of > (equality gives a degenerate triangle, which is a straight line, not a triangle).
- Checking only one inequality instead of all three (though the critical one is always the two shorter sides summing to more than the longest).
- Confusing this with the Pythagorean theorem inequality for classifying acute/obtuse triangles.
