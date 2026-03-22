---
id: antiderivatives
title: Antiderivatives
domain: mathematics
course: calculus-1
prerequisites:
  - id: power-rule
    type: hard
  - id: derivatives-of-trigonometric-functions
    type: hard
  - id: derivatives-of-exponential-functions
    type: hard
builds-toward:
  - indefinite-integrals
  - fundamental-theorem-of-calculus-part-1
tags: [integration, antiderivatives, reverse-differentiation]
stage: formal-systems
status: validated
---

# Antiderivatives

## Core Idea
An antiderivative of f(x) is a function F(x) whose derivative is f(x): F'(x) = f(x). Finding antiderivatives is "undoing" differentiation. The general antiderivative includes an arbitrary constant C because the derivative of a constant is zero: if F'(x) = f(x), then (F(x) + C)' = f(x) too. Antiderivatives are the key to evaluating definite integrals via the Fundamental Theorem of Calculus.

## How It's Best Learned
Start by reversing known derivative rules: if d/dx[x^3] = 3x^2, then an antiderivative of 3x^2 is x^3. Build a table of basic antiderivatives from the derivative rules. Emphasize the +C and why it is necessary (different antiderivatives differ by a constant).

## Common Misconceptions
- Forgetting the constant of integration C.
- Trying to antidifferentiate products by antidifferentiating each factor (the product rule does not reverse this simply).
- Confusing the antiderivative of x^n (which uses (n+1), not (n-1)) with the derivative.

## Questions

```yaml
- question: "What is the antiderivative of f(x) = 4x³?"
  type: multiple-choice
  options:
    - "12x² + C"
    - "x⁴ + C"
    - "x⁴/3 + C"
    - "x⁴"
  answer: 1
  explanation: "Applying the power rule in reverse: increase the exponent from 3 to 4, then divide by the new exponent (4), giving 4x⁴/4 = x⁴. The +C is required because any constant added to F(x) also satisfies F'(x) = f(x). Option A applies the *derivative* rule (multiply by exponent, decrease exponent) instead of reversing it. Option C divides by the original exponent (3) rather than the new one (4). Option D is correct but omits the necessary +C."

- question: "Student A claims an antiderivative of 2x is x² + 3. Student B claims it is x² − 7. Who is correct?"
  type: multiple-choice
  options:
    - "Student A only — the constant 3 matches the original function's offset"
    - "Student B only — antiderivatives cannot have positive added constants"
    - "Both are correct — antiderivatives of the same function form a family differing by a constant"
    - "Neither — the only correct antiderivative of 2x is x²"
  answer: 2
  explanation: "Both x² + 3 and x² − 7 differentiate to 2x, because the derivative of any constant is zero. The *general* antiderivative is x² + C, where C can be any real number. There is no unique antiderivative without additional information (such as a specific point the function must pass through). Option D is the most common mistake: writing just x² is one valid antiderivative, but it is not the only one."

- question: "An antiderivative of a function is unique — for any given f(x), there is exactly one F(x) such that F'(x) = f(x)."
  type: true-false
  answer: false
  explanation: "Antiderivatives are never unique. Because the derivative of any constant is zero, if F(x) is an antiderivative of f(x), then so is F(x) + C for any constant C. This yields an entire family of antiderivatives, all shifted vertically from one another. Uniqueness is only recovered when an initial condition pins down the value of C."

- question: "To find the antiderivative of xⁿ (for n ≠ −1), you increase the exponent by one and divide by the new exponent."
  type: true-false
  answer: true
  explanation: "This is the power rule for antiderivatives: ∫xⁿ dx = x^(n+1)/(n+1) + C. It is the reverse of the derivative power rule. Differentiating x^(n+1)/(n+1) gives (n+1)·x^n/(n+1) = xⁿ, confirming the formula. The most common confusion is applying the derivative rule instead — multiplying by n and *decreasing* the exponent — which produces xⁿ⁻¹, not the antiderivative."

- question: "Explain why we must always include '+C' when writing a general antiderivative."
  type: short-answer
  answer: "Because the derivative of any constant is zero, adding a constant to an antiderivative produces another valid antiderivative. The general antiderivative therefore represents a whole family of functions differing by a vertical shift. The +C captures this ambiguity; C can only be determined with additional information, such as a known point the function passes through."
  explanation: "Omitting +C implies the antiderivative is unique, which is false. This matters in applications: when solving a differential equation or modeling a physical system, the constant C encodes the initial condition (e.g., starting position or initial velocity). Without +C, you cannot apply those conditions and your solution will be wrong for all but one arbitrary case."
```

## Explainer

You've spent weeks learning to differentiate functions. Antidifferentiation is the reverse question: given a function f(x), can you find a function F(x) whose derivative is f(x)? The answer is almost always yes, and building the skill to find F(x) opens the door to the Fundamental Theorem of Calculus — one of the most important results in all of mathematics.

The basic strategy is to read your differentiation rules backwards. Since d/dx[x^n] = nx^(n-1), working backwards: if you see x^n, you need x^(n+1)/(n+1), because differentiating that gives x^n. The **power rule for antiderivatives** says: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1). Notice the exponent *increases* by 1 — opposite of differentiation — and you divide by the new exponent. Similarly, since d/dx[sin x] = cos x, an antiderivative of cos x is sin x. Since d/dx[e^x] = e^x, an antiderivative of e^x is e^x itself. Build a table by reversing every derivative rule you know.

The **+C** — the constant of integration — is not optional bookkeeping. It's mathematically necessary. If F'(x) = f(x), then (F(x) + 7)' = f(x) too, and so does (F(x) - 12)'. All these functions have the same derivative because constants vanish when differentiated. The *general antiderivative* therefore represents an entire family of functions, all shifted vertically from each other. You can pin down C only when you have additional information — for instance, knowing that F(0) = 5 or that F passes through a specific point.

The constant of integration also reveals why antidifferentiating products is harder than differentiating them. The product rule d/dx[uv] = u'v + uv' means the derivative of a product is a sum of two terms. Going backwards, if you see a sum, you'd have to recognize it came from a product — which requires insight rather than a mechanical rule. This is why techniques like integration by parts are needed later: they translate difficult antiderivative problems back into solvable derivative computations. For now, the key skill is recognizing the basic patterns and applying the reverse rules accurately, always including +C.
