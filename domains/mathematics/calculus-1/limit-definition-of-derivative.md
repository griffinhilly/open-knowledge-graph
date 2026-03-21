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

## Questions

```yaml
- question: "A student computes f'(a) for f(x) = x² using the limit definition. After forming the difference quotient [(a+h)² − a²]/h, they immediately substitute h = 0 and get 0/0. What went wrong?"
  type: multiple-choice
  options:
    - "They should have used h→∞ instead of h→0"
    - "They needed to simplify the expression algebraically before evaluating the limit"
    - "The derivative of x² doesn't exist, so 0/0 is the correct result"
    - "They should have computed (f(a) − f(a−h))/h instead"
  answer: 1
  explanation: "Substituting h = 0 directly yields the indeterminate form 0/0, which provides no information. The algebra must be done first — expand (a+h)², cancel the a² terms, factor out h from the numerator, and cancel it with the denominator. Only then can you evaluate at h = 0 to get the derivative. The entire point of the limit definition is that you simplify until the indeterminate form is resolved, then take the limit."

- question: "A function f is continuous at x = a but not differentiable there. Which example best illustrates this?"
  type: multiple-choice
  options:
    - "f(x) = x² at x = 0"
    - "f(x) = |x| at x = 0"
    - "f(x) = 1/x at x = 0"
    - "f(x) = sin(x) at x = 0"
  answer: 1
  explanation: "f(x) = |x| is continuous at x = 0 (no gap or jump), but the left-hand difference quotient approaches −1 while the right-hand difference quotient approaches +1. Since the one-sided limits disagree, the limit defining f'(0) does not exist — the derivative fails. This is the canonical example showing that continuity does not imply differentiability. Note: f(x) = 1/x is not even continuous at 0, so it doesn't illustrate the right distinction."

- question: "If the limit f'(a) = lim_{h→0} [f(a+h) − f(a)]/h exists, then f must be continuous at x = a."
  type: true-false
  answer: true
  explanation: "Differentiability implies continuity — this is a theorem, not just a rule of thumb. If the difference quotient has a finite limit, the numerator f(a+h) − f(a) must approach 0 as h → 0 (since the denominator h also approaches 0 and a finite ratio requires the numerator to vanish). That means f(a+h) → f(a), which is exactly the definition of continuity at a. The converse fails: continuous functions need not be differentiable (e.g., |x| at 0)."

- question: "The difference quotient [f(a+h) − f(a)]/h evaluates to 0/0 when h = 0, which means the derivative at a equals 0."
  type: true-false
  answer: false
  explanation: "0/0 is an indeterminate form — it does not equal 0 or any other specific number. It signals that direct substitution cannot determine the limit; the expression must be algebraically simplified first. For example, for f(x) = x², the difference quotient simplifies to 2a + h, and only then substituting h = 0 gives 2a — which is typically nonzero. The derivative is determined by the limit after simplification, not by the indeterminate form before it."

- question: "Why is it necessary to simplify the difference quotient algebraically before taking the limit, rather than substituting h = 0 directly?"
  type: short-answer
  answer: "Direct substitution gives 0/0 — an indeterminate form with no value. The algebraic work (expanding and simplifying the numerator) allows h to cancel from numerator and denominator, converting the expression into a form that can be evaluated at h = 0. The limit process works precisely because the cancellation removes the problematic h in the denominator before it reaches zero."
  explanation: "This is the computational heart of the limit definition. The difference quotient is designed to produce an indeterminate form — because you're trying to find the slope at a single point, which formally requires dividing zero by zero. The algebra resolves the indeterminacy by revealing what the expression approaches. Understanding this prevents the most common mechanical error in limit computations: premature substitution."
```

## Explainer

You already understand what a limit is: a number that an expression approaches as the input approaches some target value. And from your study of rates of change, you know that the **average rate of change** of f over an interval [a, a+h] is the slope of the secant line through the two points — computed as [f(a+h) − f(a)] / h. The derivative makes this exact by asking: what does this slope approach as the interval shrinks to nothing?

This expression [f(a+h) − f(a)] / h is called the **difference quotient**. For any fixed nonzero h, it gives the slope of the secant line through (a, f(a)) and (a+h, f(a+h)). As h → 0, the second point slides toward the first along the curve, the secant rotates, and in the limit it becomes the **tangent line** at (a, f(a)). The derivative f'(a) is exactly this limiting slope: f'(a) = lim(h→0) [f(a+h) − f(a)] / h. This is not a shortcut or an approximation — it is the definition. Every derivative rule you will learn (power rule, product rule, chain rule) is derived from this single formula.

Computing from the definition requires algebra. For f(x) = x², start with the difference quotient: [(a+h)² − a²] / h. Expand the numerator: [a² + 2ah + h² − a²] / h = [2ah + h²] / h. Factor out h: h(2a + h) / h = 2a + h. Now take the limit as h → 0: the result is 2a. The critical step is the cancellation of h from numerator and denominator — which is *why* you cannot substitute h = 0 at the start. Substituting h = 0 initially gives 0/0, an indeterminate form that yields no information. The limit process first simplifies the algebra until h cancels, then evaluates at h = 0.

Not every function has a derivative everywhere. Differentiability requires the limit to exist, which demands the function behave smoothly at that point — no sharp corners, no vertical tangents, no breaks. The function |x| is continuous everywhere but fails to be differentiable at x = 0: approaching from the left, the secant slope approaches −1; from the right, it approaches +1. The one-sided limits disagree, so the limit does not exist. Differentiability is a strictly stronger condition than continuity: every differentiable function is continuous, but not every continuous function is differentiable. Knowing this distinction will prevent errors when you apply derivative rules without checking whether they apply.
