---
id: taylor-polynomials
title: Taylor Polynomials
domain: mathematics
course: calculus-2
prerequisites:
- id: higher-order-derivatives
  type: hard
- id: linear-approximation
  type: hard
- id: power-series
  type: soft
- id: binomial-theorem-expansion
  type: soft
builds-toward:
- taylor-series
tags:
- series
- Taylor
- approximation
- polynomials
stage: formal-systems
status: validated
---
# Taylor Polynomials

## Core Idea
The nth-degree Taylor polynomial of f centered at a is P_n(x) = sum from k=0 to n of f^(k)(a)/k! * (x - a)^k. It is the unique polynomial of degree n that matches f and its first n derivatives at x = a. Taylor polynomials extend linear approximation to higher-order approximation: P_1 is the tangent line, P_2 adds curvature correction, and each additional term improves accuracy near a. The error (remainder) can be bounded by Taylor's inequality.

## How It's Best Learned
Start from linear approximation (n = 1), add the quadratic term (n = 2), and observe improvement. Compute Taylor polynomials for e^x, sin(x), cos(x) centered at 0. Plot the polynomials against the true function to see convergence. Introduce the Lagrange remainder for error estimation.

## Common Misconceptions
- Confusing Taylor polynomials (finite, exact at a) with Taylor series (infinite, convergent on an interval).
- Forgetting the k! in the denominator.
- Not understanding that the polynomial is exact at x = a and approximate elsewhere.

## Questions

```yaml
- question: "A student computes the degree-3 Taylor polynomial for sin(x) centered at 0: P₃(x) = x − x³/6. They claim this equals sin(x) for 'small x.' What is the most accurate statement about this claim?"
  type: multiple-choice
  options:
    - "P₃(x) = sin(x) for all x, because Taylor polynomials converge to the original function"
    - "P₃(x) equals sin(x) exactly at x = 0 and approximates sin(x) for small x, but does not equal it at any other point"
    - "P₃(x) equals sin(x) exactly on some interval around x = 0, but diverges outside it"
    - "P₃(x) is only useful for x > 0, where the approximation is valid"
  answer: 1
  explanation: "A Taylor polynomial is exact at exactly one point: the center a (here, x = 0). At x = 0, P₃(0) = 0 = sin(0) ✓, and matching derivatives are guaranteed by construction. Everywhere else, P₃(x) approximates sin(x), with error growing as |x| increases. The phrase 'equals sin(x) for small x' is imprecise — it should be 'closely approximates sin(x) for small x.' Convergence to the true function on an interval requires the full infinite Taylor series, not a finite polynomial."

- question: "The Taylor polynomial formula includes f^(k)(a)/k! as the coefficient of (x−a)^k. Why is the k! in the denominator?"
  type: multiple-choice
  options:
    - "To keep the polynomial's values bounded as k grows large"
    - "To cancel the k! factor that appears when differentiating (x−a)^k exactly k times, ensuring the k-th derivative condition is satisfied"
    - "To normalize the approximation so errors stay proportional to (x−a)"
    - "To make the formula dimensionally consistent across different functions"
  answer: 1
  explanation: "When you differentiate the monomial c_k(x−a)^k exactly k times and evaluate at x = a, the power rule produces k! · c_k (and all lower terms vanish, all higher terms contribute zero). Setting k! · c_k = f^(k)(a) gives c_k = f^(k)(a)/k!. The factorial in the denominator is not a normalization convention — it is the exact inverse of the factorial that differentiation produces. This is why the coefficients have this form: they're determined by solving for what makes the k-th derivative match."

- question: "The degree-n Taylor polynomial of f centered at a is the unique polynomial of degree at most n that matches f in both value and all derivatives up to order n at x = a."
  type: true-false
  answer: true
  explanation: "This is the defining property of the Taylor polynomial, and 'unique' is the key word. There is exactly one polynomial of degree ≤ n satisfying all n+1 conditions (matching f(a), f'(a), f''(a), ..., f^(n)(a)). This uniqueness is what makes the Taylor polynomial 'the best' degree-n polynomial approximation near a in a precise sense — no other polynomial of the same degree can match as many derivatives at a."

- question: "A Taylor polynomial and a Taylor series for the same function f, centered at the same point, represent the same mathematical object."
  type: true-false
  answer: false
  explanation: "A Taylor polynomial is a finite sum — P_n(x) has exactly n+1 terms and provides an approximation with bounded error. A Taylor series is an infinite sum that may converge to f(x) on some interval, but is a fundamentally different object. The polynomial is a partial sum of the series, not the series itself. For example, sin(x) = x − x³/6 + x⁵/120 − ··· is an infinite Taylor series that equals sin(x) everywhere; P₃(x) = x − x³/6 is just the first two non-zero terms and diverges from sin(x) for larger |x|."

- question: "Why does the Lagrange remainder formula turn Taylor polynomials from a useful approximation into a rigorous engineering tool? What problem does it solve that a plain polynomial cannot?"
  type: short-answer
  answer: "A Taylor polynomial tells you what approximation to use, but not how accurate it is at any specific point. The Lagrange remainder R_n(x) = f^(n+1)(c)/(n+1)! · (x−a)^(n+1) gives a concrete bound on the error: if you can bound |f^(n+1)| on the interval, you know the maximum possible error. This lets you certify 'my approximation is within 0.001 of the true value' — a guarantee, not just an intuition. Without it, you have no way to know whether your polynomial is close enough for a given application."
  explanation: "This is how calculators and software compute transcendental functions (sin, cos, exp, ln): they use Taylor polynomials of sufficient degree and use the remainder bound to guarantee that the result is accurate to the last bit of precision. The Lagrange remainder transforms Taylor polynomials from a mathematical curiosity into a constructive tool: 'I need accuracy ε on interval [a−δ, a+δ] — what degree n suffices?' The remainder formula answers this directly."
```

## Explainer

You already know **linear approximation**: near a point a, a differentiable function behaves like its tangent line L(x) = f(a) + f'(a)(x − a). This first-degree polynomial is exact at x = a (it matches f(a)) and its slope matches f'(a), so it is the best straight-line approximation near that point. A **Taylor polynomial** extends this idea: instead of matching only the value and first derivative, match the value and the first n derivatives simultaneously. Each additional derivative matched adds one more polynomial term and corrects a new layer of curvature that the previous approximation missed.

The formula forces itself on you once you accept the goal. If you want a polynomial P(x) = c₀ + c₁(x−a) + c₂(x−a)² + ··· + cₙ(x−a)ⁿ such that P^(k)(a) = f^(k)(a) for k = 0, 1, ..., n, you can solve for each coefficient by differentiating. When you differentiate P k times and set x = a, only the k-th term survives: P^(k)(a) = k! · cₖ. Setting this equal to f^(k)(a) gives **cₖ = f^(k)(a)/k!**. The k! in the denominator is not arbitrary — it is exactly what cancels the k! that differentiating a k-th degree monomial produces. The full formula is the sum from k=0 to n of f^(k)(a)/k! · (x−a)^k.

For the most useful Taylor polynomials centered at 0 (called **Maclaurin polynomials**), the pattern is memorable. For eˣ, every derivative evaluated at 0 is 1, so the polynomial is 1 + x + x²/2! + x³/3! + ···. For sin(x), the odd derivatives at 0 alternate ±1 and even derivatives vanish, giving x − x³/3! + x⁵/5! − ···. For cos(x), the reverse: 1 − x²/2! + x⁴/4! − ···. Plotting these polynomials of increasing degree against the true function on the same axes is the best way to internalize the idea: P₁ hugs the curve briefly near x = 0, P₃ hugs it longer, P₅ longer still.

The **Lagrange remainder** R_n(x) = f^(n+1)(c)/(n+1)! · (x−a)^(n+1) (for some c between a and x) tells you the maximum error you are making with your n-th degree approximation. This is Taylor's inequality in practice: bound |f^(n+1)| on the interval, then the remainder formula gives a concrete error guarantee. This turns Taylor polynomials from a neat algebraic trick into a rigorous engineering tool — you can certify that your approximation is within, say, 0.001 of the true value on a given interval, which is exactly what software and calculators do when they compute transcendental functions.
