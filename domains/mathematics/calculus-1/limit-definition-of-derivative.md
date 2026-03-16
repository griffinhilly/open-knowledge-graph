---
id: limit-definition-of-derivative
title: Limit Definition of the Derivative
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: rates-of-change-preview
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- derivative-as-slope-of-tangent
- power-rule
tags:
- derivatives
- definition
- difference-quotient
stage: formal-systems
status: validated
---
# Limit Definition of the Derivative

## Core Idea
The derivative of f at x = a is defined as f'(a) = lim(h->0) (f(a + h) - f(a))/h, the limit of the difference quotient. This single formula captures the instantaneous rate of change by taking the average rate of change over a shrinking interval. When this limit exists, the function is said to be differentiable at a. Every derivative rule you will learn is a shortcut derived from this definition.

## How It's Best Learned
Compute derivatives from the definition for simple functions: f(x) = x^2, f(x) = 1/x, f(x) = sqrt(x). Show the algebra step by step, emphasizing how the h in the denominator cancels. Connect each computation to the slope of the tangent line. Then motivate the need for shortcut rules (the definition is correct but slow).

## Common Misconceptions
- Setting h = 0 instead of taking the limit as h approaches 0 (division by zero).
- Forgetting to expand (a + h)^n correctly.
- Believing the derivative exists everywhere just because the function is defined everywhere (absolute value at 0 is a counterexample).

## Explainer

You already understand what a limit is: a number that an expression approaches as the input approaches some target value. And from your study of rates of change, you know that the **average rate of change** of f over an interval [a, a+h] is the slope of the secant line through the two points — computed as [f(a+h) − f(a)] / h. The derivative makes this exact by asking: what does this slope approach as the interval shrinks to nothing?

This expression [f(a+h) − f(a)] / h is called the **difference quotient**. For any fixed nonzero h, it gives the slope of the secant line through (a, f(a)) and (a+h, f(a+h)). As h → 0, the second point slides toward the first along the curve, the secant rotates, and in the limit it becomes the **tangent line** at (a, f(a)). The derivative f'(a) is exactly this limiting slope: f'(a) = lim(h→0) [f(a+h) − f(a)] / h. This is not a shortcut or an approximation — it is the definition. Every derivative rule you will learn (power rule, product rule, chain rule) is derived from this single formula.

Computing from the definition requires algebra. For f(x) = x², start with the difference quotient: [(a+h)² − a²] / h. Expand the numerator: [a² + 2ah + h² − a²] / h = [2ah + h²] / h. Factor out h: h(2a + h) / h = 2a + h. Now take the limit as h → 0: the result is 2a. The critical step is the cancellation of h from numerator and denominator — which is *why* you cannot substitute h = 0 at the start. Substituting h = 0 initially gives 0/0, an indeterminate form that yields no information. The limit process first simplifies the algebra until h cancels, then evaluates at h = 0.

Not every function has a derivative everywhere. Differentiability requires the limit to exist, which demands the function behave smoothly at that point — no sharp corners, no vertical tangents, no breaks. The function |x| is continuous everywhere but fails to be differentiable at x = 0: approaching from the left, the secant slope approaches −1; from the right, it approaches +1. The one-sided limits disagree, so the limit does not exist. Differentiability is a strictly stronger condition than continuity: every differentiable function is continuous, but not every continuous function is differentiable. Knowing this distinction will prevent errors when you apply derivative rules without checking whether they apply.
