---
id: medians-and-centroids
title: Medians and Centroids
domain: mathematics
course: geometry
prerequisites:
  - id: midpoint-formula
    type: hard
  - id: triangle-angle-sum
    type: soft
builds-toward:
  - coordinate-geometry-proofs
tags: [triangles, medians, centroid, balance-point]
stage: abstract-reasoning
status: validated
---

# Medians and Centroids

## Core Idea
A median of a triangle is a segment from a vertex to the midpoint of the opposite side. Every triangle has three medians, and they are concurrent at the centroid. The centroid divides each median in a 2:1 ratio from vertex to midpoint. The centroid is the triangle's center of mass (balance point). This connects geometry to physics and coordinate averaging.

## How It's Best Learned
Draw the three medians of a triangle and observe they meet at one point. Verify the 2:1 ratio by measurement. On the coordinate plane, show that the centroid coordinates are the average of the three vertices: ((x1+x2+x3)/3, (y1+y2+y3)/3). Use physical cutouts to demonstrate the balance point.

## Common Misconceptions
- Confusing median with midsegment or altitude.
- Getting the 2:1 ratio backwards (the centroid is 2/3 of the way from the vertex, not from the midpoint).
- Thinking the centroid, circumcenter, and incenter are the same point (they coincide only in equilateral triangles).

## Questions

```yaml
- question: "A median of a triangle has a total length of 12 units. How far is the centroid from the vertex, and how far is it from the midpoint of the opposite side?"
  type: multiple-choice
  options:
    - "6 units from the vertex, 6 units from the midpoint"
    - "4 units from the vertex, 8 units from the midpoint"
    - "8 units from the vertex, 4 units from the midpoint"
    - "3 units from the vertex, 9 units from the midpoint"
  answer: 2
  explanation: "The centroid divides each median in a 2:1 ratio measured FROM THE VERTEX. So the centroid is 2/3 of the total length from the vertex — (2/3)×12 = 8 — and 1/3 from the midpoint — (1/3)×12 = 4. Option A confuses this with a 1:1 split (the midpoint of the median), which is wrong. The centroid is closer to the midpoint side, not the vertex side."

- question: "A triangle has vertices at A(0, 0), B(6, 0), and C(0, 6). What are the coordinates of the centroid?"
  type: multiple-choice
  options:
    - "(3, 3)"
    - "(2, 2)"
    - "(6, 6)"
    - "(1, 1)"
  answer: 1
  explanation: "The centroid coordinates are the average of the three vertices: ((0+6+0)/3, (0+0+6)/3) = (6/3, 6/3) = (2, 2). Option A is a common error — students sometimes find the midpoint of one side rather than averaging all three vertices. The formula G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) always gives the correct centroid."

- question: "The centroid of a triangle is located one-third of the way from the vertex to the midpoint of the opposite side."
  type: true-false
  answer: false
  explanation: "This reverses the ratio. The centroid is TWO-THIRDS of the way from the vertex to the midpoint — not one-third. It is one-third from the midpoint side and two-thirds from the vertex. A way to remember: the centroid is the balance point, and it sits closer to the 'heavy' base than to the vertex tip."

- question: "For any triangle — whether acute, obtuse, or right — the centroid always lies inside the triangle."
  type: true-false
  answer: true
  explanation: "Unlike the circumcenter (which can fall outside an obtuse triangle) and the orthocenter (which falls outside obtuse triangles), the centroid is always inside the triangle. This follows from the fact that it is the average of the three vertices — an average of three points always lies within the convex hull of those points, and a triangle is convex."

- question: "Why is the centroid called the 'center of mass' or 'balance point' of a triangle, and how does this physical meaning connect to the coordinate formula ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)?"
  type: short-answer
  answer: "If a triangle is cut from a uniform material, every point has equal mass per unit area. The center of mass is the weighted average of all those mass positions. Because the triangle is uniform, this reduces to the simple arithmetic average of the three vertices' coordinates — (x₁+x₂+x₃)/3 and (y₁+y₂+y₃)/3. This is exactly the centroid formula, so the geometric centroid and the physical balance point coincide: you could balance the triangular cutout on a pin placed exactly at this coordinate."
  explanation: "The connection reveals why the formula works: averaging the vertex coordinates is equivalent to finding the center of mass of a uniform triangle. This also explains the 2:1 ratio — the centroid sits 2/3 of the way from each vertex because the 'mass' of the opposite half of the triangle pulls it toward the base."
```

## Explainer

You know the **midpoint formula**: the midpoint of a segment from (x₁, y₁) to (x₂, y₂) is ((x₁+x₂)/2, (y₁+y₂)/2). A **median** of a triangle puts that formula to work — it is the segment connecting a vertex to the midpoint of the opposite side. Since every triangle has three vertices, every triangle has three medians. Each one is easy to draw individually. Collectively, they do something remarkable: all three meet at a single point.

That meeting point is the **centroid**, and its existence (the three medians are concurrent) is a provable theorem. An elegant coordinate geometry proof shows that if you compute all three medians algebraically, they all pass through the point G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3). This is the average of the three vertices — coordinate averaging extended from two points (midpoint) to three. The centroid generalizes the midpoint: where the midpoint is the "middle" of a segment, the centroid is the "middle" of a triangle.

The centroid divides each median in a **2:1 ratio** measured from the vertex. If a median has total length 9, the centroid sits 6 units from the vertex and 3 units from the midpoint of the opposite side. The vertex end gets the larger share. This is the most commonly confused fact: the centroid is 2/3 of the way from the vertex, not 1/2 or 1/3. A good way to remember it — the centroid is closer to the midpoint side because the "heavy" vertex side pulls the balance point toward it.

That intuition points to the deepest meaning of the centroid: it is the **center of mass** (or **balance point**) of a triangle with uniform density. If you cut a triangle from cardboard, the centroid is the one point where you can balance it on a pencil tip. Physically, the centroid is the weighted average of all the mass, just as ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) is the arithmetic average of the vertices. Unlike the circumcenter (equidistant from the three vertices) or the incenter (equidistant from the three sides), the centroid is the only triangle center guaranteed to stay inside the triangle for any shape — and the only one with a direct physical interpretation.
