---
id: basic-integration-rules
title: Basic Integration Rules
domain: mathematics
course: calculus-1
prerequisites:
  - id: indefinite-integrals
    type: hard
  - id: constant-multiple-and-sum-rules
    type: hard
builds-toward:
  - u-substitution
  - riemann-sums
tags: [integration, rules, power-rule-integration]
stage: formal-systems
status: validated
---

# Basic Integration Rules

## Core Idea
The basic integration rules are the reverses of the basic derivative rules: the integral of x^n dx = x^(n+1)/(n+1) + C (for n not equal to -1), the integral of 1/x dx = ln|x| + C, the integral of e^x dx = e^x + C, the integral of sin(x) dx = -cos(x) + C, the integral of cos(x) dx = sin(x) + C, and so on. The constant multiple and sum rules apply to integrals just as they do to derivatives: integration is linear.

## How It's Best Learned
Build a reference table of basic integrals alongside the corresponding derivative rules. Practice until the correspondence is automatic. Emphasize the special case n = -1 (integral of 1/x is ln|x|, not the power rule). Verify every integral by differentiating.

## Common Misconceptions
- Applying the power rule for integration when n = -1 (division by zero).
- Forgetting sign changes: the integral of sin(x) is -cos(x), not +cos(x).
- Assuming there is a product rule or quotient rule for integration (there is not directly).

## Questions

```yaml
- question: "What is ∫(1/x) dx?"
  type: multiple-choice
  options:
    - "x⁰/0 + C (applying the power rule with n = -1)"
    - "ln|x| + C"
    - "-1/x² + C"
    - "1/(2x²) + C"
  answer: 1
  explanation: "The power rule formula ∫xⁿ dx = xⁿ⁺¹/(n+1) + C fails when n = -1 because the denominator becomes zero — division by zero is undefined. The correct antiderivative is ln|x| + C, because d/dx[ln|x|] = 1/x. The absolute value is necessary to extend the domain to negative x, where ln would otherwise be undefined."

- question: "A student writes ∫sin(x) dx = cos(x) + C. What is wrong with this answer?"
  type: multiple-choice
  options:
    - "Nothing — both cos(x) and -cos(x) are valid antiderivatives of sin(x)"
    - "The sign is wrong; the correct answer is -cos(x) + C"
    - "Trigonometric functions cannot be integrated using basic rules"
    - "The answer should be -sin(x) + C"
  answer: 1
  explanation: "Since d/dx[cos(x)] = -sin(x), running this backwards gives ∫sin(x) dx = -cos(x) + C, not +cos(x). You can verify: differentiate -cos(x) to get -(-sin(x)) = sin(x). The minus sign is not an error — it reflects the minus sign already present in the derivative of cosine. This is the most common sign mistake in basic integration."

- question: "The integral of eˣ dx is eˣ + C."
  type: true-false
  answer: true
  explanation: "Since d/dx[eˣ] = eˣ, running this rule in reverse gives ∫eˣ dx = eˣ + C. The exponential function is its own derivative, making it also its own antiderivative. This is one of the simplest integrals precisely because no sign change or exponent adjustment occurs."

- question: "There is a product rule for integration analogous to the product rule for differentiation: ∫f(x)g(x) dx = (∫f dx)(∫g dx)."
  type: true-false
  answer: false
  explanation: "No such product rule exists for integration. Unlike differentiation, integration has no formula that lets you integrate a product by integrating each factor separately. Integration by parts exists for integrating products, but it is not a simple multiplicative rule — it requires a specific setup and transforms the problem rather than resolving it directly. Assuming a product rule is a common and costly error."

- question: "Explain why differentiating your answer is a reliable way to check an integration result, and use this method to find the correct sign of ∫sin(x) dx."
  type: short-answer
  answer: "An integral asks for a function whose derivative is the integrand. Differentiating the answer directly checks this. For ∫sin(x) dx, try -cos(x): d/dx[-cos(x)] = -(-sin(x)) = sin(x). Since we recover the original integrand, -cos(x) + C is correct."
  explanation: "This verification habit works because differentiation and integration are inverse operations. The derivative of the answer must equal the integrand — if it doesn't, the answer is wrong. For trig integrals especially, where sign errors are common, this check catches mistakes immediately rather than propagating them through a longer problem."
```

## Explainer

You already know that an indefinite integral asks: "what function, when differentiated, gives this?" Basic integration rules are just that question answered systematically for the most common functions. Every rule in this table is simply the corresponding derivative rule run in reverse.

The most important rule is the **power rule for integration**: ∫x^n dx = x^(n+1)/(n+1) + C. Compare this to the derivative rule d/dx[x^n] = nx^(n-1). Differentiation lowers the exponent by 1 and multiplies by the old exponent. Integration does the reverse: raise the exponent by 1 and divide by the new exponent. For example, ∫x³ dx = x⁴/4 + C — you can verify this by differentiating x⁴/4 to get x³. The linearity rules you learned for derivatives carry over unchanged: constants pull out of integrals (∫5x² dx = 5∫x² dx), and the integral of a sum is the sum of integrals.

The **exception at n = −1** deserves its own sentence. The power rule formula would give x⁰/0 + C, which is undefined. But the actual answer is well-defined: ∫(1/x) dx = ln|x| + C. This follows because d/dx[ln|x|] = 1/x — a derivative rule you know — so 1/x has an antiderivative, just not one the power rule formula produces. The absolute value matters: ln is only defined for positive inputs, but 1/x is defined for all x ≠ 0, and the antiderivative ln|x| handles both positive and negative x correctly.

For trigonometric functions, the sign changes are the trickiest part. You know that d/dx[sin x] = cos x and d/dx[cos x] = −sin x. Running these backwards gives ∫cos x dx = sin x + C and ∫sin x dx = −cos x + C. The minus sign in the second integral is not an error — it reflects the minus sign in the derivative of cosine. A reliable check: differentiate your answer and confirm you get back the integrand. This verification habit catches sign errors immediately and reinforces the derivative–integral inverse relationship at every step.
