---
id: mean-value-theorem
title: Mean Value Theorem
domain: mathematics
course: calculus-1
prerequisites:
- id: continuity-definition
  type: hard
- id: derivative-as-slope-of-tangent
  type: hard
- id: rolles-theorem
  type: hard
- id: intermediate-value-theorem
  type: soft
builds-toward:
- first-derivative-test
- lhopitals-rule
tags:
- theorems
- MVT
- existence-theorems
stage: formal-systems
status: validated
---
# Mean Value Theorem

## Core Idea
The Mean Value Theorem (MVT) states that if f is continuous on [a, b] and differentiable on (a, b), then there exists at least one c in (a, b) where f'(c) = (f(b) - f(a))/(b - a). In other words, there is a point where the instantaneous rate of change equals the average rate of change over the interval. This theorem is the theoretical backbone for many results in calculus, including why zero derivative implies constant function.

## How It's Best Learned
Interpret geometrically: there is a tangent line parallel to the secant line through the endpoints. Verify with specific examples. Apply to prove corollaries: if f'(x) = 0 for all x, then f is constant; if f'(x) > 0, then f is increasing. Emphasize that MVT guarantees existence of c without finding it.

## Common Misconceptions
- Forgetting to verify the hypotheses (continuity on closed interval, differentiability on open interval).
- Confusing MVT with IVT (MVT is about derivatives, IVT is about function values).
- Believing there is exactly one c (there may be multiple).

## Explainer

The Mean Value Theorem says something intuitively obvious but mathematically powerful: if you drive 60 miles in 1 hour, your speedometer must have read exactly 60 mph at some moment during the trip. The average rate of change was 60 mph; the theorem guarantees that the instantaneous rate of change equaled that average at least once. From your study of derivatives, you know that f'(c) is the instantaneous rate of change at c, and (f(b) − f(a))/(b − a) is the average rate of change over [a, b]. The MVT says these two values must coincide somewhere inside.

The geometric interpretation makes this concrete. Draw the **secant line** connecting the endpoints (a, f(a)) and (b, f(b)) — its slope is the average rate of change. The MVT guarantees there is a point c in the open interval (a, b) where the **tangent line** is parallel to that secant. You have already proved Rolle's Theorem — the special case where f(a) = f(b), so the secant is horizontal and there must be a horizontal tangent somewhere inside. The MVT is Rolle's Theorem with the function tilted: a linear transformation that makes the secant horizontal reduces the general case to the Rolle case.

The hypotheses matter precisely. The function must be **continuous on the closed interval** [a, b] and **differentiable on the open interval** (a, b). Both conditions are necessary: a function with a corner (like |x| at x = 0) fails differentiability at a single interior point, and a function with a jump discontinuity could change values without the slope ever equaling the average. When both conditions hold, the function cannot "avoid" having a parallel tangent. Checking hypotheses is not a formality — examples where the conclusion fails always feature a violated hypothesis.

The MVT is most powerful as a proof tool rather than a computational one. If f'(x) = 0 everywhere on (a, b), then for any two points x₁ and x₂, the MVT says f(x₂) − f(x₁) = f'(c)(x₂ − x₁) = 0, so f is constant. If f'(x) > 0 everywhere, f is strictly increasing. These corollaries underpin the **First Derivative Test** for local extrema and are the theoretical basis for L'Hôpital's Rule — making the MVT one of the most load-bearing results in single-variable calculus.
