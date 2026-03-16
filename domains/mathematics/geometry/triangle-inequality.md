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

## Explainer

You know that **distance** between two points is a positive quantity measuring how far apart they are. The **Triangle Inequality Theorem** makes a claim that feels intuitive but has precise consequences: the sum of the lengths of any two sides of a triangle must be strictly greater than the length of the third side. For side lengths a, b, and c, this means a + b > c, a + c > b, and b + c > a must all hold simultaneously.

Think of it physically. Lay the longest side flat on a table. The other two sides must pivot from the endpoints and meet somewhere above. If those two sides are too short to reach each other, no triangle forms — you cannot close the shape. Only the binding constraint matters: the two shorter sides together must exceed the longest. If that inequality holds, the other two follow automatically (because the shorter sides are already less than the longest, so adding anything to either one pushes comfortably past it). In practice, check only: do the two smaller lengths sum to more than the largest?

The strict inequality matters. If a + b = c exactly, the three points are **collinear** — A, B, and C lie on a straight line, and the "triangle" collapses to a segment with zero area. This **degenerate** case is excluded by the strict greater-than requirement. Using ≥ instead of > is the most common error; it allows the degenerate case through and produces answers that are geometrically incorrect.

The Triangle Inequality also carries a deeper geometric truth: the **shortest path between two points is a straight line**. Going directly from A to C covers distance |AC|. Detouring through any other point B requires |AB| + |BC| > |AC|, guaranteed by the theorem. This principle extends far beyond triangles: in any setting where "distance" is defined — coordinate planes, three-dimensional space, and even abstract metric spaces — the Triangle Inequality is one of the fundamental axioms that any reasonable distance function must satisfy. The geometric intuition you build here scales directly into analysis and topology.
