---
id: u-substitution
title: U-Substitution
domain: mathematics
course: calculus-1
prerequisites:
- id: chain-rule
  type: hard
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: differentials
  type: soft
- id: basic-integration-rules
  type: soft
builds-toward:
- integration-by-parts
- trigonometric-substitution
tags:
- integration
- techniques
- u-substitution
stage: formal-systems
status: validated
---
# U-Substitution

## Core Idea
U-substitution is the integration counterpart of the chain rule. If the integrand has the form f(g(x)) * g'(x), substituting u = g(x), du = g'(x) dx transforms the integral into the simpler integral of f(u) du. This is the most commonly used integration technique. For definite integrals, you must also change the bounds from x-values to u-values.

## How It's Best Learned
Start by identifying the inner function u and checking that its derivative (or a constant multiple) appears in the integrand. Practice recognizing the pattern. Work through many examples with increasing complexity. Emphasize changing bounds for definite integrals (or converting back to x before evaluating).

## Common Misconceptions
- Forgetting to convert dx to du (or introducing a missing constant incorrectly).
- Not changing the limits of integration when doing definite integrals with substitution.
- Choosing the wrong u (a good u simplifies the integral; a bad choice makes it worse).

## Questions

```yaml
- question: "When evaluating ∫ 2x·cos(x²) dx, which substitution is most effective?"
  type: multiple-choice
  options: ["u = cos(x²)", "u = x²", "u = 2x", "u = sin(x²)"]
  answer: 1
  explanation: "Setting u = x² gives du = 2x dx, so the integral becomes ∫ cos(u) du = sin(u) + C = sin(x²) + C. The derivative of the inner function x² appears in the integrand, which is exactly the chain-rule structure u-substitution exploits."

- question: "When applying u-substitution to a definite integral ∫[a to b] f(g(x))·g'(x) dx, you can substitute u = g(x) and still use the original x-limits a and b."
  type: true-false
  answer: false
  explanation: "Once you substitute u = g(x), the variable of integration changes to u, so the limits must also change to u-values: the lower limit becomes g(a) and the upper becomes g(b). Using the original x-limits with u-expressions is a category error that produces an incorrect answer. Alternatively, you may convert the antiderivative back to x before applying the original limits."

- question: "Why is u-substitution considered the integration counterpart of the chain rule?"
  type: short-answer
  answer: "The chain rule states d/dx[f(g(x))] = f'(g(x))·g'(x). U-substitution reverses this: when an integrand has the form f'(g(x))·g'(x), substituting u = g(x) and du = g'(x) dx turns it into ∫f'(u) du = f(u) + C = f(g(x)) + C — exactly undoing the chain rule."
  explanation: "Every integration technique is the reverse of a differentiation rule. U-substitution undoes the chain rule just as the power rule for integration undoes the power rule for differentiation. Recognizing which differentiation rule produced the integrand tells you which technique to apply."
```

## Explainer

U-substitution reverses the chain rule. When you differentiated f(g(x)) with the chain rule, the result was f'(g(x)) · g'(x). U-substitution works backward: when the integrand has that structure — an outer function applied to an inner function, multiplied by the inner function's derivative — you can "undo" the chain rule in one move.

The core technique: choose u = g(x) (the inner function), write du = g'(x) dx, and rewrite the entire integral in terms of u. If the substitution is correct, all the x's disappear and what remains is a simpler integral ∫f'(u) du. After integrating, substitute back to get the answer in terms of x.

Recognizing a good substitution is the real skill. For ∫ 2x·cos(x²) dx, notice that x² is the inner function and 2x — its derivative — already appears in the integrand. Setting u = x² gives du = 2x dx, transforming the integral to ∫ cos(u) du = sin(u) + C = sin(x²) + C. When the derivative is off by a constant (e.g., ∫ x·cos(x²) dx), you can compensate: du = 2x dx means x dx = du/2, so the integral becomes (1/2)∫ cos(u) du.

For definite integrals, the bounds must change. If you integrate ∫[0 to 1] with u = x², the new limits are u = 0² = 0 and u = 1² = 1. In general the limits become g(a) and g(b). A common error is keeping the original x-limits while integrating in u — this mixes two different variables and gives a wrong answer. Either change the bounds, or convert the antiderivative back to x before evaluating.

A failed substitution announces itself clearly: if you substitute and x-terms remain that can't be expressed in u, the choice was wrong. A good substitution leaves a purely u-based integral that is simpler than what you started with. With practice, spotting the "inner function whose derivative is present" becomes automatic — and u-substitution, along with integration by parts, will handle the majority of integrals you encounter.
