---
id: contraction-mapping
title: Contraction Mapping Theorem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: metric-spaces-definition
  type: hard
builds-toward:
- fixed-point-iteration
tags:
- contraction-mapping
- banach
- fixed-point
stage: formal-systems
status: draft
---

# Contraction Mapping Theorem

## Core Idea
The contraction mapping theorem (Banach fixed-point theorem) guarantees that if g is a contraction with Lipschitz constant L < 1 on a complete metric space, then g has a unique fixed point and iteration x_{n+1} = g(x_n) converges to it with exponential rate. This theorem justifies fixed-point and iterative methods throughout numerical analysis.

## Questions

```yaml
- question: "A function g on [0, 1] satisfies |g(x) − g(y)| ≤ 0.9|x − y| for all x, y. Starting from x_0 = 0.5, what does the Banach fixed-point theorem guarantee about the sequence x_{n+1} = g(x_n)?"
  type: multiple-choice
  options:
    - "The sequence may or may not converge, depending on the choice of x_0"
    - "The sequence converges to a unique fixed point at an exponential rate, regardless of the starting point"
    - "The sequence converges but may converge to different fixed points depending on x_0"
    - "The sequence converges only if x_0 is already close to the fixed point"
  answer: 1
  explanation: "The conditions are met: g has Lipschitz constant L = 0.9 < 1 on [0, 1] (which is a complete metric space as a closed subset of ℝ). The Banach fixed-point theorem therefore guarantees three things simultaneously: (1) there is exactly one fixed point x* in [0, 1], (2) it is unique, and (3) the iteration converges to x* from ANY starting point in [0, 1] — not just nearby ones. The error after n steps is bounded by L^n / (1 − L) · d(x_1, x_0), shrinking exponentially."

- question: "A student claims: 'With Lipschitz constant L = 0.999, the iteration x_{n+1} = g(x_n) will barely converge — L is so close to 1 that the theorem barely applies.' Is this correct?"
  type: multiple-choice
  options:
    - "Yes — L must be 0.5 or less for the theorem to guarantee meaningful convergence"
    - "No — the theorem guarantees convergence for any L strictly less than 1. L = 0.999 is a valid contraction; convergence is slower (each step reduces error by only 0.1%) but guaranteed"
    - "Yes — with L = 0.999, the geometric error bound diverges in practice"
    - "No — convergence requires only L ≤ 1, and L = 0.999 qualifies comfortably"
  answer: 1
  explanation: "The theorem's condition is L < 1 (strictly). L = 0.999 satisfies this, so all three guarantees hold: unique fixed point, convergence from any start, exponential error decay. The student is right that convergence is slow — the error shrinks by a factor of 0.999 per step, requiring about 6,900 steps to reduce error by a factor of 10⁶. But 'slow' and 'barely applies' are different claims; the theorem is not a near-miss. Option D is wrong because L = 1 does NOT satisfy the strict inequality — an isometry need not have any fixed point."

- question: "A contraction mapping on a complete metric space always has exactly one fixed point."
  type: true-false
  answer: true
  explanation: "This is precisely the conclusion of the Banach fixed-point theorem: existence AND uniqueness of the fixed point are both guaranteed. Existence follows from the Cauchy sequence argument (the iterates form a Cauchy sequence whose limit, by completeness, exists in the space, and continuity ensures g maps that limit to itself). Uniqueness follows because two distinct fixed points x* and y* would require d(g(x*), g(y*)) = d(x*, y*), but the contraction condition gives d(g(x*), g(y*)) ≤ L · d(x*, y*) < d(x*, y*) — a contradiction."

- question: "A function satisfying |g(x) − g(y)| = |x − y| for all x, y (Lipschitz constant L = 1) is a contraction, and the Banach theorem guarantees convergence of iteration to a fixed point."
  type: true-false
  answer: false
  explanation: "False — a contraction requires L strictly less than 1. L = 1 is an isometry (distance-preserving map) and does NOT satisfy the contraction condition. The theorem makes no guarantee when L = 1. For example, g(x) = x + 1 on ℝ has L = 1, no fixed point at all, and iteration diverges. Even a map like g(x) = x (the identity) has L = 1 and every point is a fixed point — but iteration doesn't 'converge' in any useful sense. The strict inequality L < 1 is essential, not a technicality."

- question: "Why does the Contraction Mapping Theorem require the metric space to be complete? What could go wrong without completeness?"
  type: short-answer
  answer: "Completeness ensures that every Cauchy sequence in the space converges to a point that is also within the space. The iteration x_{n+1} = g(x_n) produces a Cauchy sequence (provable via geometric series from the contraction condition), but without completeness, the limit of this sequence might not exist in the space — it could 'escape' to a missing boundary point. For example, consider g(x) = x/2 on the open interval (0, 1), which is not complete. Starting from x_0 = 0.5, the iteration gives 0.25, 0.125, ..., converging to 0. But 0 is not in (0, 1), so the fixed point exists in ℝ but not in the space where g was defined. Without completeness, the theorem's existence conclusion fails."
  explanation: "Completeness is often called a 'technical' condition by students, but this example shows it is load-bearing. The theorem bundles three guarantees — existence, uniqueness, convergence — and completeness is what makes existence work. In practice, the spaces used in numerical analysis (ℝ^n, closed bounded subsets) are all complete, which is why the theorem is so widely applicable."
```

## Explainer

You already know what a metric space is: a set with a distance function that satisfies the usual geometric axioms. A **contraction** is a function g on a metric space that brings any two points strictly closer together: d(g(x), g(y)) ≤ L · d(x, y) for some fixed **Lipschitz constant** L strictly less than 1. The function "squeezes" the space. No matter how far apart x and y start, after applying g they are at most L times as far apart. After applying g twice, at most L² times. Repeating indefinitely, the images of any two starting points converge to the same limit.

The **Banach fixed-point theorem** (contraction mapping theorem) makes this rigorous. If g is a contraction on a **complete** metric space — one where every Cauchy sequence converges to a point in the space — then three things are simultaneously guaranteed: (1) there is exactly one **fixed point** x* satisfying g(x*) = x*, (2) it is unique, and (3) the iteration x_{n+1} = g(x_n) converges to x* from any starting point. Completeness is essential: it rules out the limit "escaping" to a missing boundary point. The error at step n is bounded by d(x_n, x*) ≤ L^n / (1 − L) · d(x_1, x_0), a formula derived from the geometric series.

The convergence is **exponential** in n. Each step multiplies the error by at most L. If L = 0.5, the error halves every step — 20 iterations give a factor of 2²⁰ ≈ 10⁶ improvement in accuracy. The proof of the theorem is itself a model of clarity: form the sequence x_0, g(x_0), g(g(x_0)), … and show it is Cauchy by bounding consecutive distances with a geometric series. The limit exists by completeness; then verify g maps it to itself by continuity. Uniqueness follows because two fixed points would have distance L times themselves — forcing zero distance between them.

In numerical analysis, the contraction mapping theorem justifies iterative root-finding and equation-solving. Solving f(x) = 0 is equivalent to finding a fixed point of g(x) = x − αf(x) for suitable α. The theorem converts the question "will this iteration converge?" into "is g a contraction on some neighborhood of the solution?" If yes, you immediately have existence, uniqueness, and a concrete error bound. Newton's method, Picard iteration for differential equations, and the power iteration for eigenvalues all fit this framework. The theorem is not just an existence result — it is a computational guarantee that tells you precisely how many steps you need.
