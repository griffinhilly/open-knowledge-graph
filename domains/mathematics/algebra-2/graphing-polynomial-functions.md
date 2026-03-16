---
id: graphing-polynomial-functions
title: Graphing Polynomial Functions
domain: mathematics
course: algebra-2
prerequisites:
  - id: end-behavior-of-polynomials
    type: hard
  - id: polynomial-functions-degree-and-leading-coefficient
    type: hard
  - id: solving-quadratics-by-factoring
    type: hard
builds-toward:
  - polynomial-long-division
  - fundamental-theorem-of-algebra
tags: [polynomials, graphing, zeros, multiplicity, turning-points]
stage: abstract-reasoning
status: validated
---

# Graphing Polynomial Functions

## Core Idea
To graph a polynomial: (1) determine end behavior from the leading term, (2) find x-intercepts by factoring or using known zeros, (3) determine the behavior at each zero based on multiplicity (odd multiplicity: crosses the axis; even multiplicity: touches and turns), (4) find the y-intercept, (5) plot additional points as needed. The graph is smooth and continuous with at most n-1 turning points.

## How It's Best Learned
Start with factored polynomials so zeros are immediate. Discuss multiplicity and its effect on the graph. Practice sketching by hand using end behavior, zeros, and sign analysis between zeros. Verify with graphing technology. Build from cubic to quartic to higher degrees.

## Common Misconceptions
- Not considering multiplicity (treating all zeros the same way).
- Drawing sharp corners or breaks (polynomial graphs are smooth and continuous).
- Assuming the maximum number of turning points always occurs (a degree-n polynomial has at most n-1, but may have fewer).

## Explainer

A polynomial graph is determined almost entirely by three features you already know: the leading term's degree and sign (from end behavior), the zeros and their multiplicities (from factoring), and the y-intercept (from plugging in x = 0). Graphing by hand means assembling these features into a coherent picture — not plotting hundreds of points.

**End behavior** sets the "frame" of the graph. Recall that for large |x|, the leading term dominates all others. A positive even-degree polynomial (like x⁴) rises on both sides; a negative even-degree polynomial falls on both sides; a positive odd-degree polynomial falls left and rises right; a negative odd-degree polynomial rises left and falls right. Sketch these tails first — they tell you where the graph heads as it leaves your view.

**Zeros and multiplicity** determine the graph's behavior at each x-intercept. You know from factoring quadratics that zeros come from setting factors equal to zero. For higher-degree polynomials, the same logic applies, but multiplicity adds nuance. If a zero x = a appears as a **simple zero** (multiplicity 1), the factor (x − a)¹ changes sign at a, so the graph crosses the x-axis there. If x = a is a **double zero** (multiplicity 2), the factor (x − a)² is always non-negative, so the graph touches the axis and bounces back — like a parabola's vertex sitting on the axis. Triple zeros (multiplicity 3) produce an S-shaped crossing that flattens near the axis, similar to y = x³ near the origin. The rule: odd multiplicity → crosses; even multiplicity → bounces.

With end behavior and zeros established, you can sketch the full graph by doing **sign analysis** between zeros. Pick a test point between consecutive zeros, substitute into the polynomial (or its factored form), and determine whether the output is positive or negative. This tells you whether the curve is above or below the x-axis in each interval. The graph must stay smooth — no sharp corners, no breaks — and can change direction at most n−1 times for a degree-n polynomial. Connecting the dots between your anchor points (zeros, y-intercept) while respecting sign and end behavior produces an accurate sketch without any calculus.
