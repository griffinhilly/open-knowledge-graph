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

## Questions

```yaml
- question: "Side lengths of 5, 5, and 10 are given. Can these form a triangle?"
  type: multiple-choice
  options:
    - "Yes — two sides equal the third, which satisfies the Triangle Inequality"
    - "No — the two shorter sides must be strictly greater than the longest, but 5 + 5 = 10, not more than 10"
    - "Yes — any three positive lengths can form a triangle"
    - "No — only right triangles can have two equal sides"
  answer: 1
  explanation: "The Triangle Inequality requires a strict greater-than (>), not greater-than-or-equal. When 5 + 5 = 10, the three points are collinear — A, B, and C lie on a straight line and the shape collapses to a segment with zero area. This degenerate case is excluded by the strict inequality. Using ≥ instead of > is the most common error students make on this topic."

- question: "When checking whether three lengths can form a triangle, which inequality is the only one that can actually fail?"
  type: multiple-choice
  options:
    - "The two longer sides must exceed the shortest"
    - "The two shorter sides must exceed the longest"
    - "All three pairwise inequalities must be checked independently"
    - "The longest side must be more than twice the shortest"
  answer: 1
  explanation: "If the two shorter sides sum to more than the longest, the other two inequalities follow automatically — adding the longer of the two short sides to the longest side will always exceed the remaining short side. Only the binding constraint (shortest pair vs. longest side) can fail. This is why in practice you only need to check: do the two smaller lengths sum to more than the largest?"

- question: "If a + b = c for side lengths a, b, and c (where c is the longest), then a, b, and c form a valid (non-degenerate) triangle."
  type: true-false
  answer: false
  explanation: "When a + b = c exactly, the three points A, B, and C are collinear — the 'triangle' degenerates to a line segment with zero area. The Triangle Inequality requires strict greater-than (a + b > c), not greater-than-or-equal. This degenerate case is the most common source of error when students use ≥ instead of >."

- question: "The Triangle Inequality implies that traveling from point A to point C by detouring through any intermediate point B will always cover more distance than going directly from A to C."
  type: true-false
  answer: true
  explanation: "This is the geometric heart of the theorem. Going directly covers |AC|. Any detour through B covers |AB| + |BC|, which by the Triangle Inequality must be strictly greater than |AC|. The straight-line path is always the shortest. This extends beyond geometry — the Triangle Inequality is one of the axioms any well-defined distance function must satisfy in mathematics."

- question: "Why does the Triangle Inequality use strict greater-than (>) rather than greater-than-or-equal (≥), and what happens geometrically when equality holds?"
  type: short-answer
  answer: "When equality holds (a + b = c), the three vertices are collinear — they lie on a straight line, producing a degenerate 'triangle' with zero area that is geometrically just a segment. A true triangle requires the two shorter sides to actually 'reach past' the longest, not merely touch it. The strict inequality (>) excludes this degenerate case."
  explanation: "The distinction matters both for geometric correctness (a degenerate triangle is not a triangle) and for applying the theorem: the strict inequality is what ensures the three points form a closed polygon with positive area. Any problem that allows equality is implicitly permitting straight-line configurations, which violates the definition of a triangle."
```

## Explainer

You know that **distance** between two points is a positive quantity measuring how far apart they are. The **Triangle Inequality Theorem** makes a claim that feels intuitive but has precise consequences: the sum of the lengths of any two sides of a triangle must be strictly greater than the length of the third side. For side lengths a, b, and c, this means a + b > c, a + c > b, and b + c > a must all hold simultaneously.

Think of it physically. Lay the longest side flat on a table. The other two sides must pivot from the endpoints and meet somewhere above. If those two sides are too short to reach each other, no triangle forms — you cannot close the shape. Only the binding constraint matters: the two shorter sides together must exceed the longest. If that inequality holds, the other two follow automatically (because the shorter sides are already less than the longest, so adding anything to either one pushes comfortably past it). In practice, check only: do the two smaller lengths sum to more than the largest?

The strict inequality matters. If a + b = c exactly, the three points are **collinear** — A, B, and C lie on a straight line, and the "triangle" collapses to a segment with zero area. This **degenerate** case is excluded by the strict greater-than requirement. Using ≥ instead of > is the most common error; it allows the degenerate case through and produces answers that are geometrically incorrect.

The Triangle Inequality also carries a deeper geometric truth: the **shortest path between two points is a straight line**. Going directly from A to C covers distance |AC|. Detouring through any other point B requires |AB| + |BC| > |AC|, guaranteed by the theorem. This principle extends far beyond triangles: in any setting where "distance" is defined — coordinate planes, three-dimensional space, and even abstract metric spaces — the Triangle Inequality is one of the fundamental axioms that any reasonable distance function must satisfy. The geometric intuition you build here scales directly into analysis and topology.
