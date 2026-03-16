---
id: concavity-and-inflection-points
title: Concavity and Inflection Points
domain: mathematics
course: calculus-1
prerequisites:
- id: first-derivative-test
  type: hard
- id: higher-order-derivatives
  type: soft
builds-toward:
- second-derivative-test
- curve-sketching
tags:
- derivatives
- concavity
- inflection
- graphing
stage: formal-systems
status: validated
---
# Concavity and Inflection Points

## Core Idea
A function is concave up where f''(x) > 0 (the graph curves upward, like a cup) and concave down where f''(x) < 0 (the graph curves downward, like a cap). An inflection point is where the concavity changes. Concavity provides information the first derivative cannot: while f' tells you whether the function is increasing or decreasing, f'' tells you whether the rate of change is accelerating or decelerating.

## How It's Best Learned
Compute f'', find where it is zero or undefined, and build a sign chart. Identify intervals of concave up/down and locate inflection points. Practice on polynomials, then on functions involving trig and exponentials. Connect to physical interpretation: concave up = velocity increasing = acceleration positive.

## Common Misconceptions
- Assuming f''(c) = 0 guarantees an inflection point (concavity must actually change, e.g., f(x) = x^4 has f''(0) = 0 but no inflection point).
- Confusing concavity with increasing/decreasing.
- Believing inflection points are always where f'' = 0 (they can occur where f'' is undefined).

## Explainer

You already know how to use the first derivative to find where a function increases or decreases and to locate local extrema via the first derivative test. The second derivative adds a new dimension: it tells you not just the direction the function is moving, but whether that motion is accelerating or decelerating. Imagine driving: f(x) is your position, f′(x) is your speed, and f″(x) is your acceleration. A positive acceleration means you're speeding up; a negative acceleration means you're slowing down. Concavity is the geometric version of this acceleration story.

A function is **concave up** where f″(x) > 0. Geometrically, the curve bends upward like the inside of a bowl. The slope f′(x) is increasing — even if f itself is decreasing, it's decreasing more and more slowly (like a ball rolling into a valley). A function is **concave down** where f″(x) < 0. The curve bends downward like the top of a hill, and the slope is decreasing. A useful visual test: if you draw a tangent line at any point in a concave-up region, the curve lies above the tangent; in a concave-down region, the curve lies below it.

To find concavity, compute f″(x), then build a sign chart just as you did for f′ in the first derivative test. Find where f″ equals zero or is undefined, divide the number line at those points, and test the sign of f″ in each interval. Where f″ > 0, you have concave up; where f″ < 0, concave down. An **inflection point** is where the concavity actually switches — the curve changes from bowl-shaped to hill-shaped or vice versa. The critical requirement is that the sign of f″ must change, not merely that f″ = 0. The function f(x) = x⁴ has f″(0) = 0, but f″ stays non-negative on both sides, so x = 0 is not an inflection point.

Concavity and the first derivative are independent. A function can be increasing and concave up (accelerating upward), increasing and concave down (slowing as it rises), decreasing and concave up (slowing as it falls), or decreasing and concave down (accelerating downward). Working with both f′ and f″ together gives you the full qualitative picture of a curve's shape, which is the foundation for curve sketching and for the second derivative test you'll apply next.
