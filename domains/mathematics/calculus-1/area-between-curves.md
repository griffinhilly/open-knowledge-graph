---
id: area-between-curves
title: Area Between Curves
domain: mathematics
course: calculus-1
prerequisites:
  - id: fundamental-theorem-of-calculus-part-2
    type: hard
  - id: u-substitution
    type: soft
builds-toward:
  - volumes-by-disk-method
  - volumes-by-washer-method
tags: [integration, applications, area]
stage: formal-systems
status: validated
---

# Area Between Curves

## Core Idea
The area between two curves y = f(x) and y = g(x) from x = a to x = b is the integral from a to b of |f(x) - g(x)| dx. In practice, you determine which function is on top in each subinterval and integrate (top - bottom). For curves better described as functions of y, you can integrate with respect to y using (right - left). This is the first major application of the definite integral beyond simple area under a curve.

## How It's Best Learned
Start by graphing the curves and finding intersection points. Set up the integral as (top - bottom) dx or (right - left) dy. Practice with cases requiring multiple integrals (when the curves cross). Emphasize the importance of sketching the region first.

## Common Misconceptions
- Integrating f(x) - g(x) without checking which is on top (can get a negative area).
- Missing intersection points and using wrong bounds.
- Not splitting the integral when the top and bottom curves switch within the interval.

## Questions

```yaml
- question: "The curves y = x and y = x² intersect at x = 0 and x = 1. A student sets up ∫₀¹ (x² − x) dx to find the area between them. What is wrong?"
  type: multiple-choice
  options:
    - "The student should integrate with respect to y instead of x"
    - "The student has the subtraction backwards — on [0,1], x ≥ x², so the integrand should be (x − x²)"
    - "The student must add both ∫₀¹ x dx and ∫₀¹ x² dx and subtract the results"
    - "Nothing — both (x² − x) and (x − x²) give the same area after integration"
  answer: 1
  explanation: "On [0,1], x ≥ x² (the line is above the parabola), so the top-minus-bottom integrand must be (x − x²). The student's integrand (x² − x) is ≤ 0 on this interval, and its integral equals −1/6 — a negative number, which cannot be an area. Option D is wrong: the two integrals differ by a sign, giving 1/6 vs −1/6. Before setting up any area integral, you must determine which curve is on top in the interval and subtract in the correct order. Area is always non-negative; a negative result is a signal that the subtraction is backwards."

- question: "The curves y = cos(x) and y = sin(x) cross at x = π/4 within the interval [0, π/2]. A student computes ∫₀^(π/2) [sin(x) − cos(x)] dx without splitting the integral at x = π/4. The student's result:"
  type: multiple-choice
  options:
    - "Equals the true area between the curves"
    - "Is too large, because the student counted the overlapping region twice"
    - "Is too small, because near x = 0 where cos > sin, the integrand is negative and partially cancels the positive portion"
    - "Is correct as long as the student takes the absolute value of the final answer"
  answer: 2
  explanation: "On [0, π/4], cos(x) > sin(x), so sin(x) − cos(x) < 0 there. On [π/4, π/2], sin(x) > cos(x), so sin(x) − cos(x) > 0. The unsplit integral adds a negative contribution from [0, π/4] to a positive contribution from [π/4, π/2], causing partial cancellation. The result underestimates the true area. Option D (taking absolute value of the final integral) would also give the wrong answer — the absolute value of (positive − negative) is not the same as integrating |sin − cos|. The correct approach is to split at x = π/4 and compute ∫₀^(π/4)(cos−sin)dx + ∫_(π/4)^(π/2)(sin−cos)dx."

- question: "The area between two curves f(x) and g(x) on [a, b] can generally be correctly computed as the absolute value of ∫ₐᵇ [f(x) − g(x)] dx."
  type: true-false
  answer: false
  explanation: "Taking the absolute value of the integral only gives the correct area when one function is consistently on top throughout [a, b] — in that case the integral is either all positive or all negative, and taking absolute value fixes the sign. If the curves cross within [a, b], the integral accumulates positive and negative contributions that partially cancel before you take the absolute value. The absolute value of this reduced number is less than the true area. The correct procedure is to find all crossing points, split the integral at each one, compute ∫(top − bottom) on each piece (all positive), and sum the results."

- question: "When setting up an area-between-curves integral, the intersection points of the two curves are generally needed to determine the limits of integration."
  type: true-false
  answer: false
  explanation: "Intersection points are needed only when the problem does not specify the limits of integration and the region is defined by where the curves cross. If the problem specifies 'from x = 1 to x = 4,' those are your limits whether or not the curves intersect there. However, even when limits are given, you still need to check whether the curves *cross within the given interval*, because a crossing requires splitting the integral. So intersection points matter for two distinct purposes: establishing limits (if not given) and identifying where to split (even when limits are given)."

- question: "A student integrates (f(x) − g(x)) over an interval where the curves cross once, getting a result of 2. They take the absolute value and report the area as 2. Explain why this is likely wrong and describe the correct procedure."
  type: short-answer
  answer: "If the curves cross within the interval, (f − g) is positive on one subinterval and negative on the other. The integral adds these contributions with opposite signs, so cancellation occurs before the absolute value is applied. For example, if the integral is +5 on one piece and −3 on the other, the total integral is 2, but the true area is 5 + 3 = 8. The correct procedure: find the crossing point, split the integral there, integrate (top − bottom) — always positive — on each piece, and sum the positive results."
  explanation: "The absolute value of the whole integral is |5 + (−3)| = |2| = 2, while the correct area is 5 + 3 = 8. These are very different numbers. The error is applying absolute value after cancellation has already occurred. The fix — split at each crossing, integrate each piece as (top − bottom) dx, sum — ensures cancellation never happens because each piece is everywhere non-negative. This is why sketching the curves and identifying the topology of the region (which curve is on top, where do they cross) must precede the setup, not follow it."
```

## Explainer

The definite integral as you have learned it computes the net signed area between a curve y = f(x) and the x-axis. The area between two curves extends this idea by replacing the x-axis with a second curve. The region bounded by y = f(x) on top and y = g(x) on the bottom, from x = a to x = b, has area equal to the integral of [f(x) − g(x)] dx from a to b. The subtraction removes the area "below" g(x), leaving only the vertical gap between the two curves. When f(x) ≥ g(x) throughout [a, b], this difference is always non-negative and the integral gives the correct positive area.

The hardest part of most problems is the setup, not the integration itself. First, **sketch both curves** and identify the bounded region. Find the **intersection points** by setting f(x) = g(x) and solving for x — these become your limits of integration if the problem does not specify them. Then determine which curve is on top in each subinterval. If the curves cross within your interval, you must split the integral at each crossing, computing ∫(top − bottom) dx separately in each piece and adding the results. Omitting a split and integrating f − g across a crossing produces cancellation — positive and negative contributions partially cancel — giving an answer smaller than the true area.

Sometimes a region is more naturally described with x and y swapped. Consider the region between x = y² and x = y + 2. If you integrate with respect to x, you would need to solve for y as a function of x, producing square roots and requiring two separate integrals. Instead, integrate with respect to y: find intersections from y² = y + 2 (giving y = −1 and y = 2), then integrate [(y + 2) − y²] dy from −1 to 2, where (y + 2) is the rightmost curve and y² is the leftmost. The principle is identical — **(right − left) dy** instead of (top − bottom) dx — with the orientation rotated 90°.

This topic is not just an endpoint; it is the foundation for volumes of revolution. When you revolve a region about an axis to build a solid, the cross-sectional slices are disks or washers, and the "radius" of each washer is determined by the distance between two curves — precisely what you integrate here. Mastering the setup logic of area between curves makes the reasoning behind volumes of revolution feel like a natural extension rather than a new technique.
