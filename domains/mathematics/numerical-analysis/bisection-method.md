---
id: bisection-method
title: Bisection Method for Root Finding
domain: mathematics
course: numerical-analysis
prerequisites:
- id: intermediate-value-theorem
  type: hard
builds-toward:
- order-of-convergence
tags:
- root-finding
- bisection
- convergence
stage: formal-systems
status: validated
---

# Bisection Method for Root Finding

## Core Idea
The bisection method finds roots by repeatedly halving an interval where the function changes sign, guaranteed by the intermediate value theorem. Each iteration halves the remaining uncertainty, achieving linear convergence. Although slow, bisection is robust and requires only continuity and an initial sign change, with no derivatives or special tuning needed.

## How It's Best Learned
Implement bisection for simple functions like x³ - 2 = 0, tracking how the interval shrinks with each iteration and observing linear error reduction.

## Common Misconceptions
- Thinking bisection is fast just because it converges reliably; convergence is slow compared to faster methods.
- Assuming bisection works without locating an initial sign change; finding such an interval is the user's responsibility.

## Questions

```yaml
- question: "A numerical analyst wants to find a root of f(x) = x³ − 2 on the interval [1, 2] to within error ε = 10⁻⁶. Approximately how many bisection iterations are required?"
  type: multiple-choice
  options:
    - "About 6 iterations — one per decimal place of accuracy"
    - "About 20 iterations — since (b − a)/2ⁿ ≤ ε gives 1/2ⁿ ≤ 10⁻⁶, so n ≥ log₂(10⁶) ≈ 20"
    - "About 3 iterations — bisection converges quickly once near the root"
    - "It cannot be determined without knowing the derivative of f near the root"
  answer: 1
  explanation: "After n iterations, the interval width is (b − a)/2ⁿ = 1/2ⁿ. Setting 1/2ⁿ ≤ 10⁻⁶ gives 2ⁿ ≥ 10⁶, so n ≥ log₂(10⁶) ≈ 19.9, meaning about 20 iterations. This is bisection's linear convergence in action: each iteration buys only about 0.3 decimal digits of accuracy (since log₁₀(2) ≈ 0.301). The number of iterations can be computed in advance without any information about f's shape near the root — this predictability is one of bisection's strengths."

- question: "Newton's method finds a root in 5 iterations; bisection requires 50 iterations on the same problem. A student concludes bisection is the inferior method in all practical situations. What is the critical flaw in this reasoning?"
  type: multiple-choice
  options:
    - "There is no flaw — Newton's method is strictly superior in all cases and bisection is obsolete"
    - "Bisection is faster for polynomial equations specifically, so the comparison is unfair"
    - "Newton's method requires computing the derivative f'(x) and can diverge or cycle if the initial guess is poorly chosen; bisection requires no derivative and guarantees convergence from any valid bracket — making it indispensable when derivatives are unavailable or the function is ill-behaved"
    - "Bisection converges faster than Newton's for functions with multiple roots"
  answer: 2
  explanation: "Newton's method achieves quadratic convergence (doubling correct digits per step) but requires f'(x) and can fail spectacularly — cycling, diverging to infinity, or converging to the wrong root — if the starting point is unlucky. Bisection has no such failure modes: given a valid bracket, it always converges. In practice, hybrid methods like Brent's method combine bisection's safety with faster methods' speed. Understanding bisection is the conceptual anchor for all such strategies."

- question: "After n bisection iterations starting from an interval [a, b], the interval containing the root is guaranteed to have width exactly (b − a)/2ⁿ, regardless of the function's behavior."
  type: true-false
  answer: true
  explanation: "Each bisection step discards exactly half the remaining interval, no matter what the function looks like — whether it is steeply sloped, nearly flat, or has complicated curvature near the root. The only information used is the sign of f at the midpoint. This geometric halving is what makes bisection's convergence rate perfectly predictable: the width after n steps is always exactly (b − a)/2ⁿ. It is also what makes convergence 'linear' — the number of correct bits grows at exactly 1 per iteration."

- question: "Bisection can be started from any two points a and b as long as f(a) ≠ f(b), without needing to check for a sign change."
  type: true-false
  answer: false
  explanation: "Bisection requires f(a) and f(b) to have *opposite signs* — not merely different values. The Intermediate Value Theorem only guarantees a root in [a, b] when f(a) < 0 and f(b) > 0 (or vice versa). If f(a) and f(b) have the same sign, there may be zero roots or an even number of roots in [a, b], and bisection provides no guarantee. Finding a valid bracket [a, b] with a sign change is the human judgment step — bisection cannot automate it."

- question: "Why is finding the initial bracket [a, b] the step that requires human judgment, and what mathematical condition must that bracket satisfy for bisection to be guaranteed to work?"
  type: short-answer
  answer: "The initial bracket must satisfy f(a) · f(b) < 0 — that is, f must have opposite signs at the two endpoints. This is the condition required by the Intermediate Value Theorem to guarantee a root exists in [a, b]. Finding such a bracket requires knowledge of the function's behavior: one might plot f, evaluate it at several candidate points, or use domain knowledge about where roots should lie. Bisection cannot automate this step because it has no mechanism to search for sign changes — it can only refine a bracket once one is provided."
  explanation: "This is not a limitation of bisection but a fundamental division of labor: the IVT guarantees existence given the bracket; bisection converts that existence guarantee into a root estimate. The user's job is to supply the existence condition. Once a valid bracket is given, the algorithm takes over entirely and delivers a convergence guarantee that requires no further human input."
```

## Explainer

The **Intermediate Value Theorem** — your prerequisite — states that if a continuous function f takes a positive value at one point and a negative value at another, it must cross zero somewhere in between. The bisection method turns that existence guarantee into a practical algorithm: if f(a) < 0 and f(b) > 0, evaluate f at the midpoint m = (a+b)/2. If f(m) < 0, the root must lie in [m, b]; if f(m) > 0, it must lie in [a, m]. Either way, you have halved the interval containing the root. Repeat until the interval is as small as you need.

The algorithm's simplicity is its greatest strength. At each step, you evaluate f exactly once and discard exactly half the remaining uncertainty. After n iterations, the interval containing the root has width (b − a)/2ⁿ. To achieve error ε, you need n ≈ log₂((b − a)/ε) iterations — computable in advance. There is no guessing, no tuning, no reliance on derivatives or smoothness beyond continuity. Bisection is the most trustworthy root-finding method precisely because it requires so little: a continuous function and an initial bracket [a, b] with a sign change.

The downside is **linear convergence**: the number of correct decimal digits grows by roughly 0.3 per iteration (since each step multiplies the error by 1/2 and log₁₀(1/2) ≈ −0.301). To gain one decimal digit of precision costs about 3.3 iterations; to gain ten digits costs 33 iterations. Faster methods like Newton's method achieve *quadratic convergence* — they roughly double the number of correct digits per iteration — but they require f'(x) and can fail if they wander away from the root. Bisection never wanders; it is the reliable backup when faster methods misbehave.

**Choosing the initial bracket** is the step that requires human judgment — bisection cannot do it for you. You might plot f to find sign changes, sample at several points, or use domain knowledge about where roots should be. Once you have a valid bracket, however, bisection takes over entirely and delivers a guaranteed result. In practice, numerical analysts often use bisection to get close to a root and then switch to a faster method (a hybrid approach exemplified by Brent's method). Understanding bisection gives you the conceptual anchor for all such strategies: controlled halving of uncertainty is the most fundamental idea in numerical root-finding.
