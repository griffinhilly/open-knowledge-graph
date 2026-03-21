---
id: even-and-odd-functions
title: Even and Odd Functions
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
  - id: function-transformations
    type: soft
builds-toward:
  - trigonometric-identities-pythagorean
  - graphing-sine-and-cosine
tags: [functions, symmetry, parity]
stage: formal-systems
status: validated
---

# Even and Odd Functions

## Core Idea
A function is even if f(-x) = f(x) for all x in its domain (symmetric about the y-axis), and odd if f(-x) = -f(x) (symmetric about the origin). Most functions are neither. Recognizing parity simplifies graphing, integration, and identity work. For example, knowing that cosine is even and sine is odd is essential for trigonometric identities.

## How It's Best Learned
Test algebraically by substituting -x and simplifying. Verify graphically by checking for y-axis or origin symmetry. Work through a mix of polynomial, rational, and trigonometric examples.

## Common Misconceptions
- Assuming "even" and "odd" refer to the degree of a polynomial (they correlate but are not the same concept for general functions).
- Forgetting to check the entire domain, not just convenient points.
- Believing every function must be either even or odd.

## Questions

```yaml
- question: "Let f(x) = x² + x. What is f(−x), and what does this tell you about f?"
  type: multiple-choice
  options:
    - "f(−x) = x² + x = f(x), so f is even"
    - "f(−x) = x² − x, which is neither f(x) nor −f(x), so f is neither even nor odd"
    - "f(−x) = −x² − x = −f(x), so f is odd"
    - "f(−x) = −x² + x, and since the leading term has even degree, f is even"
  answer: 1
  explanation: "Substituting −x: f(−x) = (−x)² + (−x) = x² − x. Comparing: f(x) = x² + x and −f(x) = −x² − x. Since x² − x equals neither x² + x nor −x² − x, the function is neither even nor odd. This illustrates the key misconception: a polynomial with both even- and odd-degree terms is neither. The polynomial shortcut (even ↔ only even-degree terms; odd ↔ only odd-degree terms) requires *all* terms to have the same parity — mixing them breaks both symmetries."

- question: "A student claims: 'Since f(x) = x³ + 1 has an odd-degree leading term, it must be an odd function.' Which response is correct?"
  type: multiple-choice
  options:
    - "The student is correct — the leading term's degree determines the function's parity"
    - "The student is wrong — f(−x) = −x³ + 1, which is not equal to −f(x) = −x³ − 1, so f is neither even nor odd"
    - "The student is wrong — f is even because the constant term 1 acts as an even-degree term"
    - "The student is wrong — functions with a constant term are always even"
  answer: 1
  explanation: "f(−x) = (−x)³ + 1 = −x³ + 1. For f to be odd, we need f(−x) = −f(x) = −x³ − 1. Since −x³ + 1 ≠ −x³ − 1 (the constant term has the wrong sign), f is not odd — and f(−x) ≠ f(x) either, so it's not even. The student's error is applying the polynomial shortcut to just the leading term. The correct shortcut: a polynomial is odd only if *every* term has odd degree (no constants, no even-degree terms)."

- question: "Every polynomial function is either even or odd."
  type: true-false
  answer: false
  explanation: "Most polynomial functions are neither even nor odd. A polynomial is even only if it contains exclusively even-degree terms (e.g., 3x⁴ − x² + 5), and odd only if it contains exclusively odd-degree terms (e.g., 2x³ − x). Any polynomial mixing both types — such as x² + x or x³ + 1 — is neither. Since most polynomials mix degree types, most are neither. The even/odd classification must be checked algebraically for each function, and 'neither' is the most common outcome."

- question: "If f is an even function, then its graph is symmetric about the y-axis."
  type: true-false
  answer: true
  explanation: "This follows directly from the definition. f being even means f(−x) = f(x) for all x — the function assigns the same output to x and −x. Geometrically, this means the point (x, f(x)) and the point (−x, f(x)) are both on the graph, and these points are reflections of each other across the y-axis. Every point on the right half of the graph has a mirror image at the same height on the left half. Y-axis symmetry is the visual equivalent of the algebraic condition f(−x) = f(x)."

- question: "Why is it insufficient to test whether a function is even or odd by checking just a few specific input values, and what is the correct procedure?"
  type: short-answer
  answer: "A function must satisfy f(−x) = f(x) (even) or f(−x) = −f(x) (odd) for every x in its domain — a single counterexample rules out a symmetry, but no finite number of confirmations proves the property holds everywhere. The correct procedure is to substitute −x for x throughout the entire expression and simplify algebraically. If the result is identically equal to f(x), the function is even; if equal to −f(x), it is odd; if neither, it is neither."
  explanation: "For example, checking f(0) is useless for determining parity: f(−0) = f(0) always, so the origin is consistent with both even and odd and provides no information. A more subtle trap: a function might satisfy f(−x) = f(x) at many 'nice' values but fail at others. Only the algebraic substitution confirms the identity holds for all x simultaneously. Additionally, one must verify that the domain is symmetric about 0 — a function defined only for x ≥ 0 cannot be even or odd by convention."
```

## Explainer

You already know how to use **function notation**: f(x) means "evaluate the function f at input x." Even and odd functions are defined by what happens when you replace x with -x. If f(-x) = f(x) for every x in the domain, the function is **even** — negating the input leaves the output unchanged. If f(-x) = -f(x) for every x, the function is **odd** — negating the input negates the output. Most functions satisfy neither condition and are simply neither even nor odd.

The geometric meaning is immediate and worth visualizing. An even function produces the same output at x and -x, so its graph is symmetric across the y-axis: the right half is a mirror image of the left. The classic example is y = x²: (-3)² = 9 = 3², so the parabola looks the same on both sides of the y-axis. An odd function maps the pair (x, f(x)) to (-x, -f(x)) simultaneously, meaning the graph has **origin symmetry** — rotating it 180° around the origin leaves it unchanged. The classic example is y = x³: (-2)³ = -8 = -(2³), so the cubic has that characteristic S-shape symmetric about the origin.

To test a function algebraically, substitute -x everywhere x appears and simplify completely. If the result equals the original expression, it is even. If it equals the negative of the original, it is odd. If neither, it is neither. For polynomials there is a useful shortcut: a polynomial is even if and only if it contains only even-degree terms (constants, x², x⁴, ...), and odd if and only if it contains only odd-degree terms (x, x³, x⁵, ...). So f(x) = x⁴ - 3x² + 1 is even; g(x) = 2x³ - x is odd; h(x) = x² + x is neither. But this shortcut is only valid for polynomials — always return to the definition for rational functions, exponentials, or other forms.

This concept pays off substantially in later work. When you study **trigonometric functions**, you will find that cosine is even (cos(-θ) = cos(θ)) and sine is odd (sin(-θ) = -sin(θ)), and many identities follow directly from this parity. In calculus, if f is an odd function, then ∫_{-a}^{a} f(x) dx = 0 for any a — the positive and negative areas cancel exactly, so you can evaluate the integral without any computation at all. Recognizing parity is therefore not merely a classification exercise; it is a symmetry tool that shortcuts calculations throughout calculus, Fourier analysis, and physics.
