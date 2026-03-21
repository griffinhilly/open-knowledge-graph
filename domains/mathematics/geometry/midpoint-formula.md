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

## Questions

```yaml
- question: "One endpoint of a segment is (-3, 7) and the midpoint is (2, 1). What are the coordinates of the other endpoint?"
  type: multiple-choice
  options:
    - "(-0.5, 4) — the midpoint of the given endpoint and midpoint"
    - "(7, -5) — solving the midpoint equation for the unknown endpoint"
    - "(5, -6) — subtracting the known endpoint from the midpoint"
    - "(-1, 4) — averaging the given endpoint and midpoint coordinates"
  answer: 1
  explanation: "Set up the midpoint equation: 2 = (-3 + x₂)/2, so -3 + x₂ = 4, giving x₂ = 7. Then 1 = (7 + y₂)/2, so 7 + y₂ = 2, giving y₂ = -5. Answer: (7, -5). The most common error is applying the midpoint formula again to the known endpoint and the midpoint — that gives the midpoint of a different segment entirely. The reverse problem requires setting up and solving an equation, not directly applying the formula."

- question: "What is the midpoint of the segment with endpoints (4, -6) and (-2, 8)?"
  type: multiple-choice
  options:
    - "(6, 2) — subtracting the coordinates instead of averaging"
    - "(2, 2) — averaging only the x-coordinates"
    - "(1, 1) — averaging both coordinate pairs correctly"
    - "(1, 7) — correct x, but adding instead of averaging the y-coordinates"
  answer: 2
  explanation: "Midpoint = ((4 + (-2))/2, (-6 + 8)/2) = (2/2, 2/2) = (1, 1). Each coordinate is computed independently by averaging: the x-midpoint is the average of the x-coordinates, and the y-midpoint is the average of the y-coordinates. Option A (subtracting) is the classic error — midpoint uses addition followed by division by 2, not subtraction."

- question: "The midpoint formula works by averaging the x-coordinates and averaging the y-coordinates independently — there is no interaction between the two dimensions."
  type: true-false
  answer: true
  explanation: "This is exactly right. The midpoint of (x₁, y₁) and (x₂, y₂) is ((x₁+x₂)/2, (y₁+y₂)/2). The x-calculation involves only x-coordinates, and the y-calculation involves only y-coordinates — just like finding the midpoint on a number line, applied twice. This independence is what makes the formula easy to remember and apply: it is just averaging, done separately for each coordinate."

- question: "To find a missing endpoint when given one endpoint and the midpoint, you apply the midpoint formula to the known endpoint and the midpoint."
  type: true-false
  answer: false
  explanation: "This is the most common error in 'reverse midpoint' problems. If you apply the midpoint formula to the known endpoint and the midpoint, you get the midpoint of a different (shorter) segment — not the missing endpoint. Instead, set up the midpoint equation with the unknown: M_x = (x₁ + x₂)/2, substitute the known values, and solve algebraically for the unknown coordinate. For example, if midpoint is (5, 3) and one endpoint is (2, 1): 5 = (2 + x₂)/2 → x₂ = 8, not 3.5."

- question: "A student finds the midpoint of (2, 8) and (6, 4) by computing (2+8)/2 = 5 and (6+4)/2 = 5, getting (5, 5). What error did they make, and what is the correct midpoint?"
  type: short-answer
  answer: "The student mixed up the coordinates — they averaged the x-coordinate of one point with the y-coordinate of the other, and vice versa. The correct calculation pairs coordinates by dimension: average the x-coordinates (2 and 6) to get (2+6)/2 = 4, and average the y-coordinates (8 and 4) to get (8+4)/2 = 6. The correct midpoint is (4, 6)."
  explanation: "The midpoint formula requires keeping x-coordinates together and y-coordinates together. The student computed (x₁+y₁)/2 and (x₂+y₂)/2 instead of (x₁+x₂)/2 and (y₁+y₂)/2 — a coordinate-mixing error. Staying organized by writing the formula first and substituting carefully prevents this. The answer (5,5) happens to look plausible since both coordinates are equal, which is why catching this error requires checking the setup, not just the arithmetic."
```

## Explainer

You already know how to locate points on a coordinate plane and measure the distance between them. The midpoint formula asks a simpler question: not how far apart are two points, but where is the exact center between them?

Start on a number line. If one end of a segment is at 3 and the other is at 7, the midpoint is at 5 — the average: (3 + 7)/2 = 5. This makes intuitive sense because averaging balances two values symmetrically. The midpoint sits equally far from both endpoints because the average splits the gap in half. If one endpoint shifts closer to zero, the average shifts in the same direction — the midpoint tracks faithfully between them.

The two-dimensional formula is nothing more than this idea applied to each coordinate independently. The midpoint of (x₁, y₁) and (x₂, y₂) is ((x₁ + x₂)/2, (y₁ + y₂)/2). You average the x-coordinates to find the horizontal center, and average the y-coordinates to find the vertical center. There is no interaction between x and y — each dimension is handled separately, exactly like the number-line case. This is why the formula is easy to remember: it's just averaging, done twice.

A common extension is finding a missing endpoint. If you know one endpoint and the midpoint, set up the equation: M_x = (x₁ + x₂)/2 and solve for x₂. For example, if the midpoint is (5, 3) and one endpoint is (2, 1): 5 = (2 + x₂)/2 gives x₂ = 8, and 3 = (1 + y₂)/2 gives y₂ = 5. This "reverse midpoint" problem appears often in coordinate proofs — for instance, proving that the diagonals of a parallelogram bisect each other requires showing that both diagonals share the same midpoint, which you check by applying the formula to each diagonal and comparing.
