---
id: fourier-series-definition
title: 'Fourier Series: Definition and Coefficients'
domain: mathematics
course: differential-equations
prerequisites:
- id: definite-integral-definition
  type: hard
- id: integration-by-parts
  type: hard
- id: trigonometric-identities-pythagorean
  type: hard
builds-toward:
- convergence-fourier-series
tags:
- fourier-series
- orthogonal-functions
- periodic
stage: advanced
status: validated
---

# Fourier Series: Definition and Coefficients

## Core Idea
A function f on [-L, L] can be written as f(x) = a₀/2 + Σ(aₙcos(nπx/L) + bₙsin(nπx/L)) with coefficients given by integrals of f against the basis functions. Fourier series decompose a function into sines and cosines, revealing frequency content. The coefficients measure the contribution of each harmonic to the overall function.

## How It's Best Learned
Compute the series for the square wave f = −1 on (−π, 0) and 1 on (0, π). All aₙ are 0 because f is odd, and bₙ = (2/(nπ))(1 − cos nπ), which is 4/(nπ) for odd n and 0 for even n. Then plot partial sums with 1, 3 and 10 nonzero terms against f to see the sum take shape and overshoot near the jumps.

## Common Misconceptions
- The coefficient formulas are a definition you have to memorize. (They follow from orthogonality: multiply the series by one basis function, integrate over [−L, L], and every other term drops out.)
- Every textbook means the same thing by a₀. (Some write the constant term as a₀/2 and some as a₀, which changes the formula for a₀ by a factor of 2; check the convention before comparing answers.)
- Only periodic functions have Fourier series. (A function defined only on [−L, L] has a Fourier series too; the series represents its periodic extension outside that interval.)
- A function with a jump cannot be represented by smooth sines and cosines. (Its Fourier series still converges at every point for piecewise smooth f, to the midpoint of the jump at a discontinuity.)

## Questions

```yaml
- question: "The Fourier coefficient a₁ for f on [-L, L] is computed as which of the following?"
  type: multiple-choice
  options: ["(1/L) ∫₋ₗᴸ f(x) dx", "(1/L) ∫₋ₗᴸ f(x) cos(πx/L) dx", "(2/L) ∫₋ₗᴸ f(x) cos(πx/L) dx", "(2/L) ∫₋ₗᴸ f(x) sin(πx/L) dx"]
  answer: 1
  explanation: "The general formula is aₙ = (1/L) ∫₋ₗᴸ f(x) cos(nπx/L) dx for n ≥ 1, so a₁ = (1/L) ∫₋ₗᴸ f(x) cos(πx/L) dx. Option A is a₀ (with the a₀/2 convention), option C doubles the correct factor, and option D has the wrong factor and the sine, so it is not a cosine coefficient. The key insight is that orthogonality of the cosine functions under integration isolates each coefficient."

- question: "A Fourier series always converges to f(x) at every point where f is defined."
  type: true-false
  answer: false
  explanation: "At a jump discontinuity, the Fourier series converges to the average of the left- and right-hand limits, not to f(x) itself. Additionally, near a jump discontinuity the partial sums exhibit the Gibbs phenomenon — an overshoot of about 9% that does not disappear as more terms are added. Pointwise convergence to f(x) requires additional conditions (e.g., f is continuous and piecewise smooth)."

- question: "Why do sines and cosines form a useful basis for representing arbitrary periodic functions?"
  type: short-answer
  answer: "The sine and cosine functions on [-L, L] are orthogonal: the integral of the product of any two distinct basis functions over the interval is zero. This orthogonality means we can isolate each coefficient by multiplying both sides by a single basis function and integrating — all other terms vanish."
  explanation: "Orthogonality is the key structural property. Just as perpendicular vectors in a plane have zero dot product (allowing you to find components independently), orthogonal functions have zero inner product (the integral of their product). This lets you compute each Fourier coefficient aₙ or bₙ independently of all the others — a property that would fail if the basis functions were not orthogonal."
```

## Explainer

You have been computing definite integrals and working with trigonometric identities. Fourier series bring these two tools together to answer a surprising question: can every periodic function be written as an infinite sum of sines and cosines? The answer is yes — under fairly mild conditions — and the formula for *how* to write it is what the Fourier series definition gives you.

The central idea is frequency decomposition. A complicated periodic signal — a square wave, a sawtooth, a human vowel sound — can be built by layering simple sinusoids of increasing frequency: the "fundamental" frequency, then twice that frequency (the first harmonic), then three times, and so on. The Fourier coefficients aₙ and bₙ tell you *how much* of each harmonic to include. A large a₂ means the function has significant content at the second harmonic frequency; a coefficient near zero means that harmonic contributes almost nothing.

Why do the integral formulas for the coefficients work? The reason is *orthogonality*. The integral of cos(mπx/L) × cos(nπx/L) over [-L, L] equals zero whenever m ≠ n, and equals L when m = n. (This is where your trigonometric identities earn their keep — the product-to-sum identities reduce these integrals to elementary ones.) This is directly analogous to perpendicular vectors: when you dot two perpendicular unit vectors you get zero. Because the basis functions are orthogonal, you can isolate each coefficient independently: multiply both sides of the Fourier series by cos(nπx/L), integrate, and every term except the aₙ term vanishes.

The a₀/2 convention for the constant term is worth a moment's attention. The formula for aₙ with n ≥ 1 gives a factor of 1/L from the normalization. For n = 0, cos(0) = 1 everywhere, and its self-integral is 2L instead of L, producing a factor of 1/(2L). Writing the constant term as a₀/2 in the series (rather than a₀) lets all coefficients share the same formula: aₙ = (1/L) ∫₋ₗᴸ f(x) cos(nπx/L) dx for n = 0, 1, 2, ... — a notational convenience worth recognizing when you encounter both conventions.

Fourier series do not always converge pointwise to f(x) at every point. At a jump discontinuity, the series converges to the midpoint of the jump, and the partial sums overshoot near the discontinuity (the Gibbs phenomenon). These convergence subtleties are studied in a follow-on topic, but for now the practical takeaway is: Fourier series are a powerful tool for smooth and piecewise-smooth periodic functions, and the coefficient integrals are the machinery that makes them computable.

