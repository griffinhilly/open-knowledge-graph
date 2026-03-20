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
status: draft
---

# Bisection Method for Root Finding

## Core Idea
The bisection method finds roots by repeatedly halving an interval where the function changes sign, guaranteed by the intermediate value theorem. Each iteration halves the remaining uncertainty, achieving linear convergence. Although slow, bisection is robust and requires only continuity and an initial sign change, with no derivatives or special tuning needed.

## How It's Best Learned
Implement bisection for simple functions like x³ - 2 = 0, tracking how the interval shrinks with each iteration and observing linear error reduction.

## Common Misconceptions
- Thinking bisection is fast just because it converges reliably; convergence is slow compared to faster methods.
- Assuming bisection works without locating an initial sign change; finding such an interval is the user's responsibility.

## Explainer

The **Intermediate Value Theorem** — your prerequisite — states that if a continuous function f takes a positive value at one point and a negative value at another, it must cross zero somewhere in between. The bisection method turns that existence guarantee into a practical algorithm: if f(a) < 0 and f(b) > 0, evaluate f at the midpoint m = (a+b)/2. If f(m) < 0, the root must lie in [m, b]; if f(m) > 0, it must lie in [a, m]. Either way, you have halved the interval containing the root. Repeat until the interval is as small as you need.

The algorithm's simplicity is its greatest strength. At each step, you evaluate f exactly once and discard exactly half the remaining uncertainty. After n iterations, the interval containing the root has width (b − a)/2ⁿ. To achieve error ε, you need n ≈ log₂((b − a)/ε) iterations — computable in advance. There is no guessing, no tuning, no reliance on derivatives or smoothness beyond continuity. Bisection is the most trustworthy root-finding method precisely because it requires so little: a continuous function and an initial bracket [a, b] with a sign change.

The downside is **linear convergence**: the number of correct decimal digits grows by roughly 0.3 per iteration (since each step multiplies the error by 1/2 and log₁₀(1/2) ≈ −0.301). To gain one decimal digit of precision costs about 3.3 iterations; to gain ten digits costs 33 iterations. Faster methods like Newton's method achieve *quadratic convergence* — they roughly double the number of correct digits per iteration — but they require f'(x) and can fail if they wander away from the root. Bisection never wanders; it is the reliable backup when faster methods misbehave.

**Choosing the initial bracket** is the step that requires human judgment — bisection cannot do it for you. You might plot f to find sign changes, sample at several points, or use domain knowledge about where roots should be. Once you have a valid bracket, however, bisection takes over entirely and delivers a guaranteed result. In practice, numerical analysts often use bisection to get close to a root and then switch to a faster method (a hybrid approach exemplified by Brent's method). Understanding bisection gives you the conceptual anchor for all such strategies: controlled halving of uncertainty is the most fundamental idea in numerical root-finding.
