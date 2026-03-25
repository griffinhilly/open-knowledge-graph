---
id: order-of-convergence
title: Order of Convergence
domain: mathematics
course: numerical-analysis
prerequisites:
- id: bisection-method
  type: hard
- id: newton-method-convergence
  type: hard
- id: convergence-iterative-methods
  type: soft
tags:
- convergence
- error-reduction
- rates
stage: formal-systems
status: validated
---
# Order of Convergence

## Core Idea
The order of convergence describes how fast iteration errors decrease. Linear convergence (order 1) reduces error by a constant factor each step; quadratic (order 2) roughly squares the error each step. Higher orders reach tolerance in fewer iterations, but convergence order only holds asymptotically near the solution—far away, even superlinear methods may behave slowly.

## How It's Best Learned
Compare error reduction for bisection, Newton, and secant methods on the same problem, plotting error vs. iteration on a log scale to see the different slopes.

## Common Misconceptions
- Confusing order of convergence with speed; a method with lower order but fewer function evaluations per step may be faster overall.
- Assuming quadratic convergence from the first iteration; convergence order applies only in the final iterations when close to the solution.

## Questions

```yaml
- question: "Newton's method has quadratic convergence and bisection has linear convergence on a problem. Starting from the same initial guess x₀, which method is guaranteed to have a smaller error after the first iteration?"
  type: multiple-choice
  options:
    - "Newton's method, because quadratic convergence always beats linear convergence"
    - "Bisection, because it guarantees halving the interval every step"
    - "Neither — convergence order is asymptotic and says nothing about early iterations far from the root"
    - "They will have the same error after the first iteration"
  answer: 2
  explanation: "Order of convergence is an asymptotic property: it describes how errors shrink when x_n is already close to the solution x*. Far from the root, Newton's method can behave poorly — it may overshoot, oscillate, or even diverge. Bisection is the one that guarantees halving the error every step regardless of starting point. The practical implication: when far from the root, lower-order but globally convergent methods like bisection may be preferable; switch to Newton's method once you are close enough that quadratic convergence kicks in."

- question: "A method with order 2 (Newton's) requires evaluating both f and f′ per iteration, while a method with order 1.618 (secant) requires only one function evaluation per iteration. If evaluating f′ is very expensive, which method might deliver more accuracy per unit of computational cost?"
  type: multiple-choice
  options:
    - "Newton's method, because quadratic convergence always dominates in total iterations needed"
    - "The secant method, because fewer expensive evaluations per step may compensate for slightly lower convergence order"
    - "They are equivalent in practice because the secant method's order is close enough to 2"
    - "Newton's method, because it requires fewer total iterations to reach any given tolerance"
  answer: 1
  explanation: "Order of convergence counts accuracy per iteration, not accuracy per function evaluation. If evaluating f′ costs as much as 5 evaluations of f, then Newton's method may be 5× more expensive per step despite needing fewer steps. The secant method needs only one new function evaluation per step (it reuses the previous one), making it highly competitive. The right comparison is accuracy per unit of computational work, not accuracy per iteration — a distinction that matters greatly when f is expensive to evaluate."

- question: "For a method with quadratic convergence, once the error is around 10⁻⁴, the next iteration's error will be approximately 10⁻⁸."
  type: true-false
  answer: true
  explanation: "Quadratic convergence means |e_{n+1}| ≈ C·|e_n|². With e_n ≈ 10⁻⁴ and C ≈ 1, we get e_{n+1} ≈ (10⁻⁴)² = 10⁻⁸. The number of correct decimal digits roughly doubles each step — from 4 to 8 in this case. This doubling behavior is what makes quadratic convergence so powerful in the final iterations: a few steps deliver enormous accuracy gains that linear convergence would take hundreds of steps to achieve."

- question: "If a numerical method has quadratic convergence, it will converge to the solution faster than a linear method starting from any initial guess."
  type: true-false
  answer: false
  explanation: "Order of convergence is asymptotic — it only describes behavior in the tail of the iteration sequence, when x_n is already very close to x*. Starting from an arbitrary initial guess, quadratic methods like Newton's are not guaranteed to outperform linear methods and may even diverge. Bisection, despite its linear (order 1) convergence, converges reliably from any starting interval. The comparison 'quadratic beats linear' only applies once you are close enough that the asymptotic regime has kicked in."

- question: "Why is 'order of convergence' not the same as 'efficiency' of a numerical method? Give an example."
  type: short-answer
  answer: "Order of convergence measures how quickly errors shrink per iteration, not per unit of computational work. A method with lower order may be more efficient if each iteration is cheaper. For example, Newton's method (order 2) requires both f and f′ per step; the secant method (order ≈ 1.618) requires only one function evaluation. If f′ is expensive, the secant method may produce more accuracy per computation even though it needs slightly more iterations."
  explanation: "The distinction between per-iteration and per-evaluation efficiency is crucial in practice. In scientific computing, function evaluations may involve solving PDEs or running simulations, costing minutes each. In such settings, the secant or even Brent's method (which avoids derivatives entirely) often outperforms Newton's despite technically lower order. Always measure computational cost, not just iteration count."
```

## Explainer

From studying bisection and Newton's method, you have seen that iterative methods get closer to a solution step by step — but they don't all close the gap at the same rate. The **order of convergence** gives a precise language for this. Let e_n = |x_n − x*| be the error at step n. A method has **order p** if |e_{n+1}| / |e_n|^p → C for some constant C > 0 called the **asymptotic error constant**. The exponent p is what determines how dramatically the error shrinks with each step.

**Linear convergence** (order 1, C < 1) means each step reduces error by the same fraction: e_{n+1} ≈ C · e_n. Bisection is the prototype — each step halves the interval, so C = 0.5. Starting with e_0 = 1, after 10 steps you have e_{10} ≈ 10^{−3}. You gain roughly log₁₀(1/C) correct decimal digits per step, which is constant. On a log-scale error plot, linear convergence appears as a straight line with slope equal to the convergence factor.

**Quadratic convergence** (order 2) is qualitatively different. If e_n ≈ 10^{−4}, then e_{n+1} ≈ C · (10^{−4})² = C · 10^{−8}: the number of correct decimal digits roughly doubles with every step. Newton's method achieves this near a simple root where f′(x*) ≠ 0 — the reason it is the default choice for smooth root-finding. The secant method achieves superlinear order ≈ 1.618 (the golden ratio), faster than linear but slower than quadratic. A few iterations of quadratic convergence accomplish what thousands of iterations of linear convergence would require once you're close enough to the solution.

Two important caveats flow directly from your prerequisite methods. First, convergence order is an **asymptotic** statement — it describes behavior only when x_n is already close to x*. Far from the solution, even Newton's method can diverge or cycle. Second, order is not the same as efficiency. Newton's method requires both f and f′ per step; if evaluating f′ is expensive, a lower-order method requiring only f evaluations may deliver more accuracy per unit of computational cost. The right metric is accuracy per function evaluation, not accuracy per iteration — a distinction that matters greatly in expensive simulations or optimization problems.
