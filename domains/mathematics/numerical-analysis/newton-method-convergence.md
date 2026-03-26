---
id: newton-method-convergence
title: 'Newton''s Method: Convergence Analysis'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: fixed-point-iteration
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- order-of-convergence
- secant-method
tags:
- newton-method
- root-finding
- convergence
stage: formal-systems
status: validated
---
# Newton's Method: Convergence Analysis

## Core Idea
Newton's method iterates x_{n+1} = x_n - f(x_n)/f'(x_n) to find roots of f. Under suitable conditions (f' continuous and nonzero at the root, sufficiently close initial guess), Newton's method converges quadratically—the number of correct digits roughly doubles with each iteration. The method is fast and powerful but requires derivative computation and can fail with poor initial guesses.

## How It's Best Learned
Implement Newton's method for familiar functions like finding √2, observing how error shrinks quadratically compared to bisection's linear shrinkage.

## Common Misconceptions
- Thinking Newton's method always converges from any starting point; convergence is local, requiring closeness to the root.
- Assuming Newton's method is cheaper than bisection; it requires derivative evaluation, which may be expensive or unavailable.

## Questions

```yaml
- question: "Newton's method is converging to a root with current error e_n. In the next iteration, the error will be approximately proportional to which of the following?"
  type: multiple-choice
  options:
    - "e_n (the same factor reduction each step)"
    - "e_n² (the error is squared)"
    - "e_n/2 (the error is halved each step)"
    - "√e_n (the square root of the current error)"
  answer: 1
  explanation: "Newton's method exhibits quadratic convergence: e_{n+1} ≈ C·e_n², where C = f''(r)/(2f'(r)). The error is squared each step, not just multiplied by a fixed factor. If the current error is 0.01, the next error is on the order of 0.0001; the one after that around 10⁻⁸. This is what it means for the number of correct digits to roughly double with each iteration. Linear convergence (option A) is what bisection achieves — a constant factor reduction per step."

- question: "You begin applying Newton's method to a function f starting far from the root. A classmate says: 'Newton's method is guaranteed to converge quadratically no matter where we start.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — quadratic convergence is guaranteed for any differentiable function"
    - "Quadratic convergence only holds near a simple root; far from the root the method may diverge, cycle, or converge to a different root"
    - "The method will always converge but only linearly when started far away"
    - "Quadratic convergence requires that f'' = 0 at the root"
  answer: 1
  explanation: "Quadratic convergence is a *local* result: the Taylor series analysis assumes x_n is already close to the root r. Far from the root, f'(x_n) may be near zero (causing the iterate to shoot far away), the quadratic approximation breaks down, and the method can cycle or diverge entirely. The standard practice is to use a globally reliable method like bisection to get within the convergence neighborhood, then switch to Newton's method for rapid final convergence — combining reliability with speed."

- question: "If f'(r) = 0 at the true root r, Newton's method applied near r cannot exhibit quadratic convergence."
  type: true-false
  answer: true
  explanation: "The quadratic convergence constant is C = f''(r)/(2f'(r)). When f'(r) = 0, this blows up — the analysis breaks down entirely. Geometrically, a zero derivative at the root means the tangent line is horizontal, and its x-intercept (the next Newton iterate) flies off to infinity. Such roots are called 'multiple' or 'repeated' roots, and Newton's method degrades to linear convergence at them rather than quadratic. Modified methods (such as iterating on f/f') restore faster convergence for repeated roots."

- question: "Newton's method always converges faster than bisection because each Newton step reduces the error by a fixed factor, whereas bisection only halves the interval."
  type: true-false
  answer: false
  explanation: "This confuses quadratic convergence with linear convergence. Bisection IS the method that reduces error by a fixed factor (1/2 per step) — that is linear convergence. Newton's method is faster when it works because it squares the error each step (quadratic), not because it uses a fixed factor. Moreover, Newton's method requires a good initial guess to converge at all; bisection is globally reliable. A Newton iteration starting far from the root may not converge, making bisection the only method that reaches the answer."

- question: "Why does Newton's method converge quadratically? Use the Taylor series argument to explain why the error is squared each step rather than reduced by a constant factor."
  type: short-answer
  answer: "Expanding f around the current iterate x_n near root r gives: f(r) = f(x_n) + f'(x_n)(r−x_n) + (f''(ξ)/2)(r−x_n)². Since f(r) = 0, the Newton update x_{n+1} = x_n − f(x_n)/f'(x_n) leaves error e_{n+1} ≈ [f''(r)/(2f'(r))]·e_n². The error is squared because the Newton step exactly cancels the linear term in the Taylor expansion, leaving only the quadratic remainder."
  explanation: "The deeper insight is that Newton's method is fixed-point iteration g(x) = x − f(x)/f'(x), and g'(r) = 0 at any simple root. For generic fixed-point iteration, the convergence rate is |g'(r)| — which gives linear convergence when nonzero. Newton's method is the exceptional case where g'(r) = 0, making the linear term vanish and leaving only the quadratic term to govern convergence. This zero derivative is why the number of correct digits roughly doubles with each step."
```

## Explainer

From fixed-point iteration, you know that iterating g(x) gives linear convergence when |g'(r)| < 1 at the fixed point r — the error shrinks by a constant factor |g'(r)| each step. Newton's method is a special case of fixed-point iteration: applying it to f(x) = 0 means iterating g(x) = x - f(x)/f'(x). What makes Newton's method special is that g'(r) = 0 when f(r) = 0, meaning the linear-convergence factor vanishes entirely. This is why the method is so fast.

The Taylor series from your prerequisites makes this precise. Expand f around the current guess x_n near the true root r: f(r) = f(x_n) + f'(x_n)(r - x_n) + (f''(ξ)/2)(r - x_n)² for some ξ between x_n and r. Since f(r) = 0, rearranging gives: r - x_{n+1} = r - (x_n - f(x_n)/f'(x_n)) = -(f''(ξ)/2f'(x_n)) · (r - x_n)². If you write e_n = x_n - r for the error at step n, this becomes e_{n+1} ≈ C · e_n² where C = f''(r)/(2f'(r)). The error is squared each step — this is **quadratic convergence**.

The practical consequence is dramatic: if your current error is 0.01, after one Newton step it is roughly (0.01)² = 0.0001; after another it is roughly 0.00000001. The number of correct decimal digits roughly doubles with each iteration. Compare this to bisection or fixed-point iteration, which add roughly one correct bit per step. Starting from a reasonable initial guess, Newton's method typically converges in 5–10 iterations to machine precision, regardless of the problem.

However, quadratic convergence is a local guarantee. The analysis assumes x_n is already close to r, f' is nonzero at r, and f'' is bounded nearby. Far from the root, Newton's method can cycle, diverge, or converge to a different root than intended. A flat derivative f'(x_n) ≈ 0 means dividing by a near-zero number, sending the iterate far from r. This is why the common practice is to use a globally-convergent method like bisection to get within the neighborhood, then switch to Newton's method for the final rapid convergence — combining reliability with speed.
