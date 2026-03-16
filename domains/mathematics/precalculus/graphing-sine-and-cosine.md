---
id: graphing-sine-and-cosine
title: Graphing Sine and Cosine
domain: mathematics
course: precalculus
prerequisites:
- id: unit-circle
  type: hard
- id: function-transformations
  type: hard
- id: converting-degrees-and-radians
  type: soft
- id: even-and-odd-functions
  type: soft
builds-toward:
- amplitude-period-phase-shift
- derivatives-of-trigonometric-functions
tags:
- trigonometry
- graphing
- sine
- cosine
stage: formal-systems
status: validated
---
# Graphing Sine and Cosine

## Core Idea
The graphs of y = sin(x) and y = cos(x) are smooth, periodic waves that repeat every 2*pi. They oscillate between -1 and 1, with cosine being a horizontal shift of sine by pi/2. Understanding these parent graphs is essential because all sinusoidal models (sound, light, tides, circuits) are transformations of these basic shapes.

## How It's Best Learned
Connect each point on the graph to the corresponding position on the unit circle. Plot key points (intercepts, maxima, minima) at 0, pi/2, pi, 3*pi/2, 2*pi. Then sketch the smooth curve through them. Use technology to explore how the graph relates to circular motion.

## Common Misconceptions
- Drawing sharp corners at maxima and minima instead of smooth curves.
- Confusing sine and cosine graphs (cosine starts at its maximum, sine starts at zero).
- Plotting in degrees on an axis labeled in radians.

## Questions

```yaml
- question: "The graph of y = cos(x) can be obtained from y = sin(x) by:"
  type: multiple-choice
  options:
    - "Shifting left by π/2"
    - "Shifting right by π/2"
    - "Reflecting over the x-axis"
    - "Stretching vertically by a factor of 2"
  answer: 0
  explanation: "cos(x) = sin(x + π/2), so cosine is sine shifted LEFT by π/2. This trips up many students because the '+' inside the function means shift left (the graph reaches its peak earlier). A shift right would be sin(x − π/2), which equals −cos(x), not cos(x)."

- question: "The graph of y = sin(x) has sharp corners at its maximum and minimum values."
  type: true-false
  answer: false
  explanation: "This is a very common drawing error. The sine function is differentiable everywhere — its derivative is cos(x), which exists at every point including peaks and troughs. At x = π/2 (a maximum), the derivative cos(π/2) = 0, so the tangent is horizontal. The graph is smooth with a flat top at each maximum and minimum, not a sharp corner."

- question: "How does the unit circle connect to the graph of y = sin(x)? What do you read off the circle to get each value?"
  type: short-answer
  answer: "For angle x, the point on the unit circle is (cos x, sin x). The y-coordinate of this point equals sin(x). As x increases from 0 to 2π, tracing around the circle, the y-coordinate traces out exactly one full period of the sine wave."
  explanation: "The unit circle is the source of truth for sine and cosine values. At angle x, the terminal point on the unit circle has coordinates (cos x, sin x). Reading the y-coordinate gives sin(x) and the x-coordinate gives cos(x). The five key points — (0,0), (π/2,1), (π,0), (3π/2,−1), (2π,0) — come directly from the circle's top, right, bottom, and left positions."
```

## Explainer

The graphs of sine and cosine are not arbitrary curves — they are a direct visual encoding of circular motion. If you watch a point moving counterclockwise around the unit circle at a steady rate, its height (y-coordinate) at angle x is exactly sin(x), and its horizontal position (x-coordinate) is cos(x). The wave shape you see when graphing these functions is simply what circular motion looks like when "unrolled" onto a flat axis.

Both functions share the same essential shape: they oscillate smoothly between −1 and 1 with a period of 2π. The **amplitude** (half the total height) is 1, the **period** (length of one full cycle) is 2π ≈ 6.28, and both functions are perfectly smooth with no corners or breaks. The key difference is their starting point: sin(0) = 0 (the wave starts at zero and rises), while cos(0) = 1 (the wave starts at its maximum). In fact, cos(x) = sin(x + π/2) — cosine is simply sine shifted left by a quarter-period.

To sketch y = sin(x) accurately, use the **five key points** of one period: (0, 0), (π/2, 1), (π, 0), (3π/2, −1), and (2π, 0). These correspond to the unit circle positions at 0°, 90°, 180°, 270°, and 360°. Plot these five points, then draw a smooth curve through them — smooth means no corners at the peaks and troughs, just a gentle turnaround. For y = cos(x), the same logic applies with a shifted starting point: (0, 1), (π/2, 0), (π, −1), (3π/2, 0), (2π, 1).

Understanding these parent graphs prepares you for the full range of sinusoidal transformations you will study next: amplitude changes (vertical stretches), period changes (horizontal stretches), phase shifts (horizontal slides), and vertical shifts. Every one of those transformations modifies the parent graphs y = sin(x) and y = cos(x) in predictable ways — which is why fluency with the parent shapes is the essential foundation.
