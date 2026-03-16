---
id: graphing-tangent-and-reciprocal-trig
title: Graphing Tangent and Reciprocal Trigonometric Functions
domain: mathematics
course: precalculus
prerequisites:
  - id: graphing-sine-and-cosine
    type: hard
  - id: unit-circle
    type: hard
builds-toward:
  - derivatives-of-trigonometric-functions
  - trigonometric-substitution
tags: [trigonometry, graphing, tangent, secant, cosecant, cotangent]
stage: formal-systems
status: validated
---

# Graphing Tangent and Reciprocal Trigonometric Functions

## Core Idea
The tangent function y = tan(x) = sin(x)/cos(x) has period pi and vertical asymptotes where cosine is zero. The reciprocal functions (csc, sec, cot) are derived from sine, cosine, and tangent respectively. Each has its own characteristic shape, period, and asymptote pattern. These graphs complete the visual picture of the six trig functions.

## How It's Best Learned
Graph tangent by plotting sin/cos ratios at key angles, noting where the function is undefined. For reciprocal functions, start by graphing the parent function (sin, cos, or tan) lightly, then take reciprocals point by point: zeros become asymptotes, maxima/minima become minima/maxima. Practice identifying the period and asymptote locations.

## Common Misconceptions
- Believing tangent has amplitude (it does not, since it has no maximum or minimum).
- Confusing the period of tangent (pi) with the period of sine/cosine (2*pi).
- Mixing up cosecant (1/sin) and secant (1/cos).

## Explainer

From graphing sine and cosine, you know two smooth wave-shaped curves with period 2π, amplitude 1, and no undefined points. The tangent function breaks all three of those properties. Recall from the unit circle that tan(x) = sin(x)/cos(x). Wherever cos(x) = 0 — at x = π/2, 3π/2, −π/2, and every odd multiple of π/2 — tangent is undefined. These undefined points become **vertical asymptotes** on the graph. Between consecutive asymptotes, tangent sweeps through all real values from −∞ to +∞, completing one full cycle. So y = tan(x) has period π (not 2π), has no amplitude (it is unbounded), and has asymptotes at x = π/2 + nπ for every integer n.

To sketch y = tan(x), use key unit circle values: tan(0) = 0, tan(π/4) = 1, tan(−π/4) = −1, with asymptotes at x = ±π/2. The curve rises from −∞ near the left asymptote, passes through 0 at x = 0, and climbs toward +∞ near the right asymptote — an S-shaped sweep between each pair of asymptotes. The cotangent y = cot(x) = cos(x)/sin(x) mirrors this pattern: its asymptotes are at multiples of π (where sine is zero), and it *decreases* from +∞ to −∞ on each interval (0, π), (π, 2π), and so on.

The **reciprocal functions** secant and cosecant are best understood by starting from the parent curves you already know. For y = csc(x) = 1/sin(x): wherever sin(x) = 1 (its maximum), csc(x) = 1 (its minimum); wherever sin(x) = −1, csc(x) = −1; wherever sin(x) = 0, csc(x) has a vertical asymptote. The result is a series of U-shaped and inverted-U-shaped arcs, each nestled between consecutive asymptotes, touching the sine curve at its peaks and valleys. Secant y = sec(x) = 1/cos(x) works identically relative to cosine — same shape, shifted by π/2.

A useful rule to remember: **zeros become asymptotes, and extremes touch**. When you take the reciprocal of zero you get undefined (asymptote); when you take the reciprocal of ±1 you get ±1 (the reciprocal curve meets the parent curve). Between those contact points, the reciprocal curve bows outward away from the x-axis — the parent curve acts as an inner boundary that the reciprocal function never crosses. Keeping the parent curve lightly drawn while sketching the reciprocal makes it easy to place all the key features correctly.
