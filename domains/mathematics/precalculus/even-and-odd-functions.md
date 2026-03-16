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

## Explainer

You already know how to use **function notation**: f(x) means "evaluate the function f at input x." Even and odd functions are defined by what happens when you replace x with -x. If f(-x) = f(x) for every x in the domain, the function is **even** — negating the input leaves the output unchanged. If f(-x) = -f(x) for every x, the function is **odd** — negating the input negates the output. Most functions satisfy neither condition and are simply neither even nor odd.

The geometric meaning is immediate and worth visualizing. An even function produces the same output at x and -x, so its graph is symmetric across the y-axis: the right half is a mirror image of the left. The classic example is y = x²: (-3)² = 9 = 3², so the parabola looks the same on both sides of the y-axis. An odd function maps the pair (x, f(x)) to (-x, -f(x)) simultaneously, meaning the graph has **origin symmetry** — rotating it 180° around the origin leaves it unchanged. The classic example is y = x³: (-2)³ = -8 = -(2³), so the cubic has that characteristic S-shape symmetric about the origin.

To test a function algebraically, substitute -x everywhere x appears and simplify completely. If the result equals the original expression, it is even. If it equals the negative of the original, it is odd. If neither, it is neither. For polynomials there is a useful shortcut: a polynomial is even if and only if it contains only even-degree terms (constants, x², x⁴, ...), and odd if and only if it contains only odd-degree terms (x, x³, x⁵, ...). So f(x) = x⁴ - 3x² + 1 is even; g(x) = 2x³ - x is odd; h(x) = x² + x is neither. But this shortcut is only valid for polynomials — always return to the definition for rational functions, exponentials, or other forms.

This concept pays off substantially in later work. When you study **trigonometric functions**, you will find that cosine is even (cos(-θ) = cos(θ)) and sine is odd (sin(-θ) = -sin(θ)), and many identities follow directly from this parity. In calculus, if f is an odd function, then ∫_{-a}^{a} f(x) dx = 0 for any a — the positive and negative areas cancel exactly, so you can evaluate the integral without any computation at all. Recognizing parity is therefore not merely a classification exercise; it is a symmetry tool that shortcuts calculations throughout calculus, Fourier analysis, and physics.
