---
id: end-behavior-of-polynomials
title: End Behavior of Polynomials
domain: mathematics
course: algebra-2
prerequisites:
  - id: polynomial-functions-degree-and-leading-coefficient
    type: hard
builds-toward:
  - graphing-polynomial-functions
tags: [polynomials, end-behavior, leading-term]
stage: abstract-reasoning
status: validated
---

# End Behavior of Polynomials

## Core Idea
The end behavior of a polynomial describes what happens to f(x) as x approaches positive or negative infinity. It depends only on the leading term (highest degree term). For even degree with positive leading coefficient: both ends go up. For even degree with negative leading coefficient: both ends go down. For odd degree with positive leading coefficient: left down, right up. For odd degree with negative: left up, right down.

## How It's Best Learned
Create a 2x2 table (even/odd degree vs. positive/negative leading coefficient) and sketch the four end behavior patterns. Practice identifying end behavior from equations without graphing. Use graphing technology to confirm. Introduce arrow notation: as x -> infinity, f(x) -> infinity (or -infinity).

## Common Misconceptions
- Looking at the constant term or other terms instead of only the leading term.
- Confusing even/odd degree end behavior.
- Thinking end behavior tells you everything about the graph's shape in the middle.

## Explainer

You already know that the **leading term** of a polynomial is the term with the highest degree, and that the leading coefficient is its numerical factor. End behavior asks a simple question: as x grows enormous in either direction, which term controls the polynomial's value? The answer is always the leading term — because when x is very large, the highest-power term dwarfs every other term combined. If f(x) = 2x⁴ - 7x³ + 3x - 10 and x = 1000, then 2x⁴ = 2,000,000,000,000, while 7x³ = 7,000,000,000 — nearly a thousand times smaller. The lower-degree terms become negligible, so the function eventually behaves like 2x⁴.

This leads to the **two-variable rule**: end behavior depends on (1) whether the degree is even or odd, and (2) whether the leading coefficient is positive or negative. Think about what happens to xⁿ as x → ±∞. For even n: x² → +∞ from both sides (squaring makes negatives positive), so both ends of an even-degree polynomial point in the same direction. For odd n: x³ → +∞ on the right but x³ → -∞ on the left (cubing preserves sign), so odd-degree polynomials have ends pointing in opposite directions. The leading coefficient then tells you whether "up" means +∞ or -∞: positive coefficient means the right end rises, negative coefficient means it falls.

The four cases are: even degree, positive coefficient → both ends up (∪ shape at extremes); even degree, negative coefficient → both ends down (∩ shape at extremes); odd degree, positive coefficient → down on the left, up on the right; odd degree, negative coefficient → up on the left, down on the right. You can derive these without memorizing by asking: what does aₙxⁿ do as x → +∞ and as x → -∞?

Notice what end behavior does *not* tell you: it says nothing about the middle of the graph — the number of peaks and valleys, where the zeros are, whether the function has local maxima or minima. End behavior is only about the tails. A degree-5 polynomial and a simple line y = x have the same end behavior, but their graphs look completely different between the ends. Use end behavior as the starting frame for sketching a polynomial: get the tails right, then layer in the zeros and turning points separately.
