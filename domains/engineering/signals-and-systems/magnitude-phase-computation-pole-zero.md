---
id: magnitude-phase-computation-pole-zero
title: Magnitude and Phase from Pole-Zero Geometry
domain: engineering
course: signals-and-systems
prerequisites:
- id: pole-zero-plot-stability-analysis
  type: hard
builds-toward:
- bode-plot-construction
- frequency-response-and-bode-plots
tags:
- frequency-response
- pole-zero
- magnitude
- phase
stage: abstract-reasoning
status: draft
---

# Magnitude and Phase from Pole-Zero Geometry

## Core Idea
The magnitude response is the product of distances from zeros divided by distances from poles to a point on the s-plane or z-plane. Phase is the sum of angles from poles minus sum of angles from zeros. This geometric interpretation allows rapid sketching of frequency response and understanding how pole-zero placement affects system behavior.

## How It's Best Learned
Plot a simple pole-zero diagram and measure distances and angles to points along the imaginary axis at increasing frequencies. Verify results with analytical transfer function evaluation.

## Common Misconceptions
- Forgetting to include contributions from all poles and zeros.
- Confusing which direction (pole or zero) multiplies vs divides magnitude.
- Using distances rather than complex magnitudes.
