---
id: midpoint-formula
title: Midpoint Formula
domain: mathematics
course: geometry
prerequisites:
  - id: segment-and-distance
    type: hard
  - id: coordinate-plane-intro
    type: hard
builds-toward:
  - perpendicular-bisectors
  - midsegment-theorem
  - coordinate-geometry-proofs
tags: [coordinates, midpoint, segments]
stage: abstract-reasoning
status: validated
---

# Midpoint Formula

## Core Idea
The midpoint of a segment is the point that divides it into two equal parts. Given endpoints (x1, y1) and (x2, y2), the midpoint is ((x1+x2)/2, (y1+y2)/2). This is simply the average of the coordinates. The midpoint formula connects geometric bisection to algebraic averaging and is essential for coordinate geometry proofs.

## How It's Best Learned
Derive it intuitively: the midpoint is the "average location" of the two endpoints. Start on a number line (midpoint of 3 and 7 is 5), then extend to two dimensions. Practice both finding midpoints and finding missing endpoints given one endpoint and the midpoint.

## Common Misconceptions
- Subtracting coordinates instead of averaging them.
- Confusing the midpoint formula with the distance formula.
- When asked to find an endpoint given the midpoint and other endpoint, students often just apply the midpoint formula directly rather than solving for the unknown.

## Explainer

You already know how to locate points on a coordinate plane and measure the distance between them. The midpoint formula asks a simpler question: not how far apart are two points, but where is the exact center between them?

Start on a number line. If one end of a segment is at 3 and the other is at 7, the midpoint is at 5 — the average: (3 + 7)/2 = 5. This makes intuitive sense because averaging balances two values symmetrically. The midpoint sits equally far from both endpoints because the average splits the gap in half. If one endpoint shifts closer to zero, the average shifts in the same direction — the midpoint tracks faithfully between them.

The two-dimensional formula is nothing more than this idea applied to each coordinate independently. The midpoint of (x₁, y₁) and (x₂, y₂) is ((x₁ + x₂)/2, (y₁ + y₂)/2). You average the x-coordinates to find the horizontal center, and average the y-coordinates to find the vertical center. There is no interaction between x and y — each dimension is handled separately, exactly like the number-line case. This is why the formula is easy to remember: it's just averaging, done twice.

A common extension is finding a missing endpoint. If you know one endpoint and the midpoint, set up the equation: M_x = (x₁ + x₂)/2 and solve for x₂. For example, if the midpoint is (5, 3) and one endpoint is (2, 1): 5 = (2 + x₂)/2 gives x₂ = 8, and 3 = (1 + y₂)/2 gives y₂ = 5. This "reverse midpoint" problem appears often in coordinate proofs — for instance, proving that the diagonals of a parallelogram bisect each other requires showing that both diagonals share the same midpoint, which you check by applying the formula to each diagonal and comparing.
