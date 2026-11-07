---
id: convex-hull-algorithms
title: "Convex Hull Algorithms: Graham Scan and Gift Wrapping"
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: stacks-data-structure
  type: hard
- id: asymptotic-notation-big-o-omega-theta
  type: hard
- id: merge-sort
  type: soft
- id: sorting-lower-bounds
  type: soft
- id: cross-product
  type: soft
builds-toward: []
tags:
- computational-geometry
- convex-hull
- graham-scan
- jarvis-march
- orientation-test
- output-sensitive
stage: advanced
status: validated
---
# Convex Hull Algorithms: Graham Scan and Gift Wrapping

## Core Idea
The convex hull of a finite set of points in the plane is the smallest convex polygon that contains them all; picture a rubber band snapped around nails. Computing it is a basic problem of computational geometry. Graham scan sorts the points by angle around a starting point and then sweeps through them with a stack, discarding any point that would create a clockwise (right) turn, for O(n log n) time overall. Jarvis's march, or gift wrapping, walks around the hull one vertex at a time in O(nh) time, where h is the number of hull vertices, so it is faster when the hull is small. Both rely on a constant-time orientation test computed with a cross product.

## How It's Best Learned
Begin with the orientation test: compute the sign of the cross product for a few point triples by hand and connect the sign to left and right turns. Trace Graham scan on 8 to 10 points drawn on grid paper, writing the stack after each step, as in the computational geometry chapter of Cormen, Leiserson, Rivest and Stein. Then compare running times of Graham scan and gift wrapping on random points in a disk (many hull points) and in a square (few hull points).

## Common Misconceptions
- Hull algorithms need trigonometry to compare angles. (Sorting by angle and testing turns can be done with cross products, which use only multiplication and subtraction and avoid rounding error from angle functions.)
- Gift wrapping is always slower than Graham scan. (Gift wrapping runs in O(nh) time, which beats O(n log n) when the number of hull vertices h is smaller than about log n.)
- With clever enough code, a convex hull of unsorted points can be found in linear time. (Listing the hull vertices in order can be used to sort numbers, so in the standard algebraic decision tree model the problem needs Omega(n log n) time in the worst case.)

## Questions

```yaml
- question: "Using the cross product (b - a) x (c - a) = (bx - ax)(cy - ay) - (by - ay)(cx - ax), classify the turn from a = (0, 0) to b = (4, 0) to c = (2, 3)."
  type: multiple-choice
  options:
    - "Counterclockwise (left) turn, because the value is positive"
    - "Clockwise (right) turn, because the value is negative"
    - "The points are collinear, because the value is zero"
    - "The test cannot be applied, because c lies between a and b in x"
  answer: 0
  explanation: "(4 - 0)(3 - 0) - (0 - 0)(2 - 0) = 12 - 0 = 12, which is positive. A positive value means a counterclockwise, or left, turn at b. Graham scan keeps points that make left turns when walking the hull counterclockwise."

- question: "For which input is Jarvis's march (gift wrapping) expected to be faster than Graham scan?"
  type: multiple-choice
  options:
    - "A million points placed on a circle, all of them on the hull"
    - "A million points: three that form a large triangle, and all the rest strictly inside it, so the hull has exactly 3 vertices"
    - "Any input, because gift wrapping is always faster"
    - "No input, because gift wrapping is always slower"
  answer: 1
  explanation: "Gift wrapping costs O(n) per hull vertex, O(nh) in total. With h = 3, that is linear time and beats the O(n log n) of Graham scan. With every point on the hull, h = n and gift wrapping takes O(n^2) time."

- question: "In the algebraic decision tree model, a convex hull algorithm that outputs the hull vertices in order can run in O(n) worst-case time on arbitrary unsorted input."
  type: true-false
  answer: false
  explanation: "Map numbers x1, ..., xn to points (xi, xi^2) on a parabola. Every point is on the hull, and the hull's vertex order is the sorted order of the numbers. Since sorting needs Omega(n log n) time in this model, so does computing an ordered hull."

- question: "During Graham scan, the stack holds hull candidates. Explain what the algorithm does when the next point p makes a right turn with the top two points on the stack, and why."
  type: short-answer
  answer: "It pops the top point and checks again, repeating until the top two stack points and p make a left turn, and then pushes p. A right turn means the popped point lies inside or on the triangle formed by p0, the point below it on the stack, and p, so it cannot be a vertex of the convex hull."
  explanation: "Each point is pushed once and popped at most once, so the scan after sorting takes O(n) time. The O(n log n) sort dominates the total."
```

## Explainer

Given n points in the plane, the **convex hull** is the smallest convex polygon that encloses them. Its vertices are a subset of the points. Hulls are used in collision detection, geographic mapping, pattern recognition and as a first step in many other geometric algorithms.

Every hull algorithm rests on one primitive: the **orientation test**. For points a, b and c, compute

(b - a) x (c - a) = (bx - ax)(cy - ay) - (by - ay)(cx - ax).

A positive value means a → b → c turns counterclockwise (left), negative means clockwise (right), and zero means the points are collinear. The test uses only multiplication and subtraction, so with integer coordinates it is exact.

**Graham scan**, published by Ronald Graham in 1972, works in two phases. First, pick the point with the lowest y-coordinate, breaking ties by x, as the anchor p0. Sort the other points by their polar angle around p0, comparing angles with the orientation test instead of trigonometry. Second, scan the sorted points with a stack. Push p0 and the first point. For each new point p, look at the top two stack entries. If they and p make a right turn, the top entry cannot be on the hull, because it lies inside or on the triangle formed by p0, the entry below it and p, so pop it and test again. When the turn is left, push p. At the end the stack holds the hull in counterclockwise order. Each point is pushed once and popped at most once, so the scan costs O(n). With the O(n log n) sort, the total is **O(n log n)**.

**Jarvis's march**, or gift wrapping, published by R. A. Jarvis in 1973, takes a different route. Start at a point certain to be on the hull, such as the leftmost. Find the point that every other point lies to the left of, as seen from the current point, using one pass of orientation tests. That point is the next hull vertex. Repeat until you return to the start. Each step costs O(n), and there are h steps, so the total is **O(nh)**. This is an **output-sensitive** bound: fast when the hull is small, but O(n^2) when every point is on the hull.

Can we beat O(n log n) in general? Not in the standard algebraic decision tree model. Place numbers x1, ..., xn at points (xi, xi^2) on a parabola. All of them are hull vertices, and reading the hull in order sorts the numbers. Sorting requires Omega(n log n) comparisons, so ordered hulls do too. Timothy Chan's 1996 algorithm reaches O(n log h), which is optimal when measured by both n and h.
