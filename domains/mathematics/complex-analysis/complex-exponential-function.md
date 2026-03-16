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

## Explainer

You already know Euler's formula from complex exponential form: e^(iθ) = cos θ + i sin θ, which places e^(iθ) on the unit circle at angle θ. The complex exponential generalizes this to all complex inputs. For z = x + iy, define **e^z = e^x (cos y + i sin y)**. The real part x controls the *magnitude* (e^x), and the imaginary part y controls the *angle* (y radians from the positive real axis). So e^z is a point at distance e^x from the origin, rotated y radians counterclockwise.

This decomposition has a striking consequence: the **magnitude |e^z| = e^x depends only on the real part of z, never on the imaginary part**. The imaginary part shifts the angle but leaves the radius unchanged. As a result, e^z is never zero — e^x > 0 for all real x, so no choice of y can make the magnitude vanish. This is why the image of the complex exponential is ℂ \ {0}: it covers every nonzero complex number, but zero is permanently excluded.

The most important property distinguishing the complex exponential from its real counterpart is **periodicity**: e^(z + 2πi) = e^z for all z. Because e^(2πi) = cos(2π) + i sin(2π) = 1, adding 2πi to z completes a full 360° rotation — returning to the same image point. The real exponential is strictly increasing and injective; the complex exponential is surjective but not injective. The vertical strip 0 ≤ Im(z) < 2π is a **fundamental domain**: every nonzero complex number has exactly one preimage there. Shift vertically by any multiple of 2π and you land on the same output.

Since e^z satisfies (e^z)' = e^z and is holomorphic everywhere — meaning differentiable at every point in ℂ — it is an **entire function** with no singularities, no branch cuts, and no restricted domain. This makes it the simplest and best-behaved transcendental function in complex analysis. All the other elementary transcendental functions are built from it: the complex sine and cosine are cos z = (e^(iz) + e^(−iz))/2 and sin z = (e^(iz) − e^(−iz))/(2i), and the complex logarithm is the inverse of e^z. Understanding e^z is the foundation for everything that follows.
