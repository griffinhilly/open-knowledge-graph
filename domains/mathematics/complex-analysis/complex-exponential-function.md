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
status: validated
---

# The Complex Exponential Function

## Core Idea
The complex exponential is defined by e^z = e^x (cos y + i sin y) for z = x + iy. It is entire (holomorphic everywhere), satisfies (e^z)' = e^z, and is periodic with period 2πi: e^(z+2πi) = e^z. The exponential is surjective but not injective; its image avoids 0.

## How It's Best Learned
Verify that e^(iy) lies on the unit circle. Compute e^(1+iπ/4) and e^(2+i0) to see how the real and imaginary parts of the exponent affect magnitude and direction.

## Common Misconceptions
Assuming e^z behaves like the real exponential; it is periodic with period 2πi, not monotonic. Forgetting that |e^(x+iy)| = e^x independent of y, so e^z is not bounded as y varies.

## Questions

```yaml
- question: "What is |e^(3 + 5i)|?"
  type: multiple-choice
  options:
    - "e^(3+5) = e^8"
    - "e^3"
    - "e^5"
    - "√(e^6 + e^{10})"
  answer: 1
  explanation: "For z = x + iy, the magnitude |e^z| = e^x — it depends only on the real part. Here x = 3, so |e^(3+5i)| = e^3. The imaginary part 5 controls only the angle (argument) of the result, rotating the output 5 radians counterclockwise from the positive real axis, but leaving the distance from the origin unchanged. Option A conflates magnitude with adding exponent components; option C confuses real and imaginary parts; option D applies the magnitude formula for a + bi incorrectly to the exponent."

- question: "Which statement correctly describes the periodicity of the complex exponential function?"
  type: multiple-choice
  options:
    - "e^z is periodic with period 2π — adding 2π to z gives the same output"
    - "e^z is periodic with period 2πi — adding 2πi to z gives the same output"
    - "e^z is not periodic — it is entire and strictly increasing like the real exponential"
    - "e^z repeats with period π because sin and cos both have period π"
  answer: 1
  explanation: "The complex exponential has period 2πi (not 2π). Adding 2πi to z shifts the imaginary part by 2π, completing a full rotation: e^{z+2πi} = e^z · e^{2πi} = e^z · 1 = e^z. The key is that the period is purely imaginary — it lives in the vertical (imaginary) direction in the complex plane. Adding a real 2π does not return to the same value unless the imaginary part also wraps around. This periodicity is what makes the complex exponential non-injective, unlike the real exponential."

- question: "The complex exponential e^z is injective (one-to-one): no two distinct values of z produce the same output."
  type: true-false
  answer: false
  explanation: "The complex exponential is NOT injective. Because e^(z + 2πi) = e^z for all z, infinitely many inputs map to the same output — specifically, the entire vertical family {z + 2πki : k ∈ ℤ} all map to the same value. This is the fundamental difference from the real exponential, which is strictly increasing and injective. The fundamental domain 0 ≤ Im(z) < 2π is the largest strip where e^z is one-to-one, and this non-injectivity is exactly why the complex logarithm requires branch cuts."

- question: "The complex exponential e^z avoids the value 0 — no complex number z satisfies e^z = 0."
  type: true-false
  answer: true
  explanation: "For any z = x + iy, we have |e^z| = e^x > 0, since the real exponential e^x is strictly positive for all real x. Because the magnitude is always positive, e^z can never equal zero. This means the image of e^z is ℂ \\ {0}: it covers every nonzero complex number (it is surjective onto ℂ \\ {0}), but zero is permanently excluded. This fact becomes important in complex analysis — for example, it means e^z has no zeros, making 1/e^z = e^{-z} entire."

- question: "Explain why the complex exponential is not injective, and describe the fundamental domain where it is one-to-one."
  type: short-answer
  answer: "The complex exponential is not injective because it is periodic with period 2πi: e^(z + 2πi) = e^z for all z, so the entire family {z + 2πki : k ∈ ℤ} maps to the same output. The fundamental domain where e^z is one-to-one is any horizontal strip of height 2π — conventionally the strip 0 ≤ Im(z) < 2π (or equivalently −π ≤ Im(z) < π). Every nonzero complex number has exactly one preimage in this strip."
  explanation: "The non-injectivity follows directly from the periodicity e^{2πi} = 1: adding 2πi to the exponent multiplies the output by 1, leaving it unchanged. This is the core reason the complex logarithm (the inverse of e^z) must be multi-valued and requires choosing a branch cut to make it single-valued."
```

## Explainer

You already know Euler's formula from complex exponential form: e^(iθ) = cos θ + i sin θ, which places e^(iθ) on the unit circle at angle θ. The complex exponential generalizes this to all complex inputs. For z = x + iy, define **e^z = e^x (cos y + i sin y)**. The real part x controls the *magnitude* (e^x), and the imaginary part y controls the *angle* (y radians from the positive real axis). So e^z is a point at distance e^x from the origin, rotated y radians counterclockwise.

This decomposition has a striking consequence: the **magnitude |e^z| = e^x depends only on the real part of z, never on the imaginary part**. The imaginary part shifts the angle but leaves the radius unchanged. As a result, e^z is never zero — e^x > 0 for all real x, so no choice of y can make the magnitude vanish. This is why the image of the complex exponential is ℂ \ {0}: it covers every nonzero complex number, but zero is permanently excluded.

The most important property distinguishing the complex exponential from its real counterpart is **periodicity**: e^(z + 2πi) = e^z for all z. Because e^(2πi) = cos(2π) + i sin(2π) = 1, adding 2πi to z completes a full 360° rotation — returning to the same image point. The real exponential is strictly increasing and injective; the complex exponential is surjective but not injective. The vertical strip 0 ≤ Im(z) < 2π is a **fundamental domain**: every nonzero complex number has exactly one preimage there. Shift vertically by any multiple of 2π and you land on the same output.

Since e^z satisfies (e^z)' = e^z and is holomorphic everywhere — meaning differentiable at every point in ℂ — it is an **entire function** with no singularities, no branch cuts, and no restricted domain. This makes it the simplest and best-behaved transcendental function in complex analysis. All the other elementary transcendental functions are built from it: the complex sine and cosine are cos z = (e^(iz) + e^(−iz))/2 and sin z = (e^(iz) − e^(−iz))/(2i), and the complex logarithm is the inverse of e^z. Understanding e^z is the foundation for everything that follows.
