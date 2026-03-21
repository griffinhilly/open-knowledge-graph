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

## Questions

```yaml
- question: "A student looks at f(x) = -3x⁵ + 100x⁴ + 5000 and claims 'the right end goes up because the x⁴ term has such a huge coefficient.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "They should use the constant term, not the x⁴ term, to determine end behavior"
    - "Only the leading term matters; -3x⁵ dominates as x grows large, so the right end goes down"
    - "The sign of the leading coefficient does not affect end behavior — only the degree matters"
    - "The coefficient 100 is large enough to outweigh -3, so the right end does go up"
  answer: 1
  explanation: "End behavior is determined solely by the leading term — the term with the highest degree. As x grows extremely large, xⁿ with higher n grows far faster than any lower-degree term, eventually dwarfing all others combined. Here the leading term is -3x⁵: odd degree with negative leading coefficient, so left end up, right end down. The coefficient 100 on x⁴ is irrelevant to end behavior, no matter how large it is."

- question: "Which polynomial has both ends pointing upward (∪ shape at the extremes)?"
  type: multiple-choice
  options:
    - "f(x) = -2x⁴ + 3x³ + 7"
    - "f(x) = 3x⁵ - x + 100"
    - "f(x) = 2x⁶ - 100x⁵ + x - 5"
    - "f(x) = -x³ + 2"
  answer: 2
  explanation: "Both-ends-up requires even degree AND positive leading coefficient. Option C has degree 6 (even) and leading coefficient 2 (positive) — both ends go up. Option A has even degree but a negative leading coefficient, so both ends go down. Options B and D have odd degree, so their ends go in opposite directions regardless of the leading coefficient sign."

- question: "The polynomial f(x) = x³ + 1000x² has both ends pointing upward because the x² term is always positive."
  type: true-false
  answer: false
  explanation: "The x² term is irrelevant to end behavior — only the leading term matters. Here the leading term is x³: odd degree, positive leading coefficient. That means the left end goes down and the right end goes up — opposite directions. The x² term, no matter how large its coefficient, cannot change the end behavior because x³ eventually dominates it for large values of x."

- question: "Two polynomials with the same leading term but completely different middle terms have identical end behavior."
  type: true-false
  answer: true
  explanation: "End behavior depends only on the leading term (degree and leading coefficient). As x → ±∞, the leading term overwhelms all other terms, so middle terms play no role. For example, f(x) = 2x⁴ and g(x) = 2x⁴ - 9999x³ + 5x - 1000 have identical end behavior: both ends up."

- question: "Why does the end behavior of a polynomial depend only on its leading term and not on any of the other terms?"
  type: short-answer
  answer: "As x grows extremely large (in either direction), the highest-power term grows far faster than all lower-degree terms. Eventually it dwarfs their combined total, so the polynomial's value is essentially determined by the leading term alone. For very large x, every other term becomes negligible in comparison."
  explanation: "Consider f(x) = 2x⁴ - 7x³ at x = 1000: the leading term is 2×10¹² while the next term is only 7×10⁹ — roughly 300 times smaller. This gap widens as x grows. End behavior captures only what happens at these extreme values, so the leading term is all that matters. Thinking about other terms when determining end behavior is the core misconception this topic addresses."
```

## Explainer

You already know that the **leading term** of a polynomial is the term with the highest degree, and that the leading coefficient is its numerical factor. End behavior asks a simple question: as x grows enormous in either direction, which term controls the polynomial's value? The answer is always the leading term — because when x is very large, the highest-power term dwarfs every other term combined. If f(x) = 2x⁴ - 7x³ + 3x - 10 and x = 1000, then 2x⁴ = 2,000,000,000,000, while 7x³ = 7,000,000,000 — nearly a thousand times smaller. The lower-degree terms become negligible, so the function eventually behaves like 2x⁴.

This leads to the **two-variable rule**: end behavior depends on (1) whether the degree is even or odd, and (2) whether the leading coefficient is positive or negative. Think about what happens to xⁿ as x → ±∞. For even n: x² → +∞ from both sides (squaring makes negatives positive), so both ends of an even-degree polynomial point in the same direction. For odd n: x³ → +∞ on the right but x³ → -∞ on the left (cubing preserves sign), so odd-degree polynomials have ends pointing in opposite directions. The leading coefficient then tells you whether "up" means +∞ or -∞: positive coefficient means the right end rises, negative coefficient means it falls.

The four cases are: even degree, positive coefficient → both ends up (∪ shape at extremes); even degree, negative coefficient → both ends down (∩ shape at extremes); odd degree, positive coefficient → down on the left, up on the right; odd degree, negative coefficient → up on the left, down on the right. You can derive these without memorizing by asking: what does aₙxⁿ do as x → +∞ and as x → -∞?

Notice what end behavior does *not* tell you: it says nothing about the middle of the graph — the number of peaks and valleys, where the zeros are, whether the function has local maxima or minima. End behavior is only about the tails. A degree-5 polynomial and a simple line y = x have the same end behavior, but their graphs look completely different between the ends. Use end behavior as the starting frame for sketching a polynomial: get the tails right, then layer in the zeros and turning points separately.
