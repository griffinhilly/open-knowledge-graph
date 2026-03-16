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

## Explainer

You know the **midpoint formula**: the midpoint of a segment from (x₁, y₁) to (x₂, y₂) is ((x₁+x₂)/2, (y₁+y₂)/2). A **median** of a triangle puts that formula to work — it is the segment connecting a vertex to the midpoint of the opposite side. Since every triangle has three vertices, every triangle has three medians. Each one is easy to draw individually. Collectively, they do something remarkable: all three meet at a single point.

That meeting point is the **centroid**, and its existence (the three medians are concurrent) is a provable theorem. An elegant coordinate geometry proof shows that if you compute all three medians algebraically, they all pass through the point G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3). This is the average of the three vertices — coordinate averaging extended from two points (midpoint) to three. The centroid generalizes the midpoint: where the midpoint is the "middle" of a segment, the centroid is the "middle" of a triangle.

The centroid divides each median in a **2:1 ratio** measured from the vertex. If a median has total length 9, the centroid sits 6 units from the vertex and 3 units from the midpoint of the opposite side. The vertex end gets the larger share. This is the most commonly confused fact: the centroid is 2/3 of the way from the vertex, not 1/2 or 1/3. A good way to remember it — the centroid is closer to the midpoint side because the "heavy" vertex side pulls the balance point toward it.

That intuition points to the deepest meaning of the centroid: it is the **center of mass** (or **balance point**) of a triangle with uniform density. If you cut a triangle from cardboard, the centroid is the one point where you can balance it on a pencil tip. Physically, the centroid is the weighted average of all the mass, just as ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3) is the arithmetic average of the vertices. Unlike the circumcenter (equidistant from the three vertices) or the incenter (equidistant from the three sides), the centroid is the only triangle center guaranteed to stay inside the triangle for any shape — and the only one with a direct physical interpretation.
