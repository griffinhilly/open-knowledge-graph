---
id: conic-sections-ellipses
title: 'Conic Sections: Ellipses'
domain: mathematics
course: algebra-2
prerequisites:
- id: conic-sections-circles
  type: hard
- id: conic-sections-parabolas
  type: soft
builds-toward:
- conic-sections-hyperbolas
- conic-sections-overview
tags:
- conics
- ellipses
- foci
- major-axis
- minor-axis
stage: abstract-reasoning
status: validated
---
# Conic Sections: Ellipses

## Core Idea
An ellipse is the set of all points where the sum of distances to two fixed points (foci) is constant. Standard form: (x-h)^2/a^2 + (y-k)^2/b^2 = 1, where a > b means horizontal major axis. The center is (h,k), vertices are a units from the center along the major axis, co-vertices are b units along the minor axis, and foci are c units from the center where c^2 = a^2 - b^2. A circle is a special ellipse where a = b.

## How It's Best Learned
Start from the definition with two thumbtacks and a string (physically tracing an ellipse). Derive key relationships: a, b, c, and c^2 = a^2 - b^2. Practice identifying center, vertices, co-vertices, and foci from equations. Graph by plotting these key points. Convert from general form using completing the square. Discuss eccentricity (e = c/a) as a measure of "ovalness."

## Common Misconceptions
- Confusing a and b (a is always the larger denominator, regardless of whether it is under x or y).
- Using c^2 = a^2 + b^2 (that is the hyperbola relationship; for ellipses it is c^2 = a^2 - b^2).
- Thinking the foci are at the endpoints of the major axis (they are inside, between center and vertex).
- Not recognizing that a circle is a special case with a = b.

## Explainer

From circles, you know that a circle is the set of all points at a fixed distance from a single center point. An **ellipse** is the natural generalization: instead of one fixed point, you use two fixed points called **foci** (singular: focus), and instead of a fixed distance to one point, you require that the *sum* of distances to both foci is constant. Imagine pinning two thumbtacks in a corkboard, looping a string around them, pulling the string taut with a pencil, and tracing a curve — the resulting shape is an ellipse. As the two foci get closer together, the ellipse approaches a circle; when they coincide, it *is* a circle. This is why the circle is a special case of the ellipse (a = b, so c = 0, meaning both foci are at the center).

The standard equation **(x−h)²/a² + (y−k)²/b² = 1** encodes the geometry. The center is (h, k). The parameter **a** is always the larger denominator — it gives the distance from the center to the **vertices**, the endpoints of the longer (**major**) axis. The parameter **b** gives the distance to the **co-vertices**, the endpoints of the shorter (**minor**) axis. The **foci** are located at distance c from the center along the major axis, where **c² = a² − b²**. This relationship follows from the Pythagorean theorem applied to a right triangle formed by a, b, and c at a special point on the ellipse: at an endpoint of the minor axis, the two distances to the foci each equal a (since their sum equals 2a and by symmetry they are equal), so a² = b² + c².

To identify the orientation, look at which denominator is larger. If a² is under (x−h)², the major axis runs horizontally and the vertices are to the left and right of center. If a² is under (y−k)², the major axis is vertical. A common mistake is to assume x always gets a² — it does not. The rule is simply: a is the bigger number, whichever variable it goes with, and the major axis runs in that direction.

The **eccentricity** e = c/a measures how "stretched" the ellipse is, ranging from 0 (a perfect circle, c = 0) to just below 1 (a very elongated ellipse, c approaching a). Earth's orbit is an ellipse with eccentricity about 0.017 — nearly circular, with the Sun at one focus. Halley's comet has eccentricity about 0.97 — a dramatically elongated ellipse. Understanding eccentricity connects the geometric definition (ratio of distances) to the algebraic parameters and prepares you for hyperbolas, where eccentricity exceeds 1.
