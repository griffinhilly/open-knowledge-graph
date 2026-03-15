---
id: complex-exponential-function
title: The Complex Exponential Function
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-exponential-form
  type: hard
- id: holomorphic-functions
  type: soft
builds-toward:
- complex-logarithm-branch-cuts
- complex-trigonometric-functions
tags:
- exponential
- entire-function
- periodic
stage: advanced
status: draft
---

# The Complex Exponential Function

## Core Idea
The complex exponential is defined by e^z = e^x (cos y + i sin y) for z = x + iy. It is entire (holomorphic everywhere), satisfies (e^z)' = e^z, and is periodic with period 2πi: e^(z+2πi) = e^z. The exponential is surjective but not injective; its image avoids 0.

## How It's Best Learned
Verify that e^(iy) lies on the unit circle. Compute e^(1+iπ/4) and e^(2+i0) to see how the real and imaginary parts of the exponent affect magnitude and direction.

## Common Misconceptions
Assuming e^z behaves like the real exponential; it is periodic with period 2πi, not monotonic. Forgetting that |e^(x+iy)| = e^x independent of y, so e^z is not bounded as y varies.
