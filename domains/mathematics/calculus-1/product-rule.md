---
id: product-rule
title: Product Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: constant-multiple-and-sum-rules
    type: hard
builds-toward:
  - quotient-rule
  - integration-by-parts
tags: [derivatives, rules, product-rule]
stage: formal-systems
status: validated
---

# Product Rule

## Core Idea
The product rule states that d/dx[f(x)*g(x)] = f'(x)*g(x) + f(x)*g'(x). The derivative of a product is NOT the product of the derivatives. Instead, you differentiate each factor while keeping the other unchanged, then add the results. This rule is necessary whenever two non-constant functions are multiplied together.

## How It's Best Learned
Derive from the limit definition by adding and subtracting f(x+h)*g(x). Practice with products of polynomials (verifiable by expanding first), then with products involving trig and exponential functions. Use the mnemonic "first times derivative of second plus second times derivative of first."

## Common Misconceptions
- Believing (fg)' = f'g': this is the single most common calculus error.
- Forgetting one of the two terms in the product rule.
- Not recognizing when the product rule is needed vs. when the constant multiple rule suffices (if one factor is a constant, use the simpler rule).

## Questions

```yaml
- question: "A student differentiates h(x) = x²sin(x) by reasoning: 'The derivative of x² is 2x and the derivative of sin(x) is cos(x), so h'(x) = 2x·cos(x).' What error did they make?"
  type: multiple-choice
  options:
    - "They should have used the chain rule instead of the product rule"
    - "They multiplied the two derivatives together instead of applying the product rule"
    - "They forgot to add a constant of integration"
    - "They differentiated sin(x) incorrectly"
  answer: 1
  explanation: "The student committed the most common calculus error: assuming (fg)' = f'g'. The correct product rule gives h'(x) = 2x·sin(x) + x²·cos(x) — differentiate each factor while holding the other fixed, then add both results. Multiplying the derivatives (2x·cos(x)) gives the wrong answer because it misses the cross-term interactions."

- question: "Which expression correctly gives d/dx[x³·eˣ]?"
  type: multiple-choice
  options:
    - "3x²·eˣ + x³·eˣ"
    - "3x²·eˣ"
    - "x³·eˣ"
    - "3x²·eˣ · x³·eˣ"
  answer: 0
  explanation: "Applying the product rule with f = x³ and g = eˣ: f' = 3x² and g' = eˣ. The result is f'g + fg' = 3x²·eˣ + x³·eˣ. Option 1 is the 'just differentiate the first factor' error; option 2 is the 'just differentiate the second factor' error; option 3 multiplies the derivatives together — all three reflect the mistaken belief that (fg)' = f'g'."

- question: "The product rule is needed whenever you differentiate an expression involving multiplication."
  type: true-false
  answer: false
  explanation: "If one factor is a constant, the constant multiple rule suffices — d/dx[5sin(x)] = 5cos(x) directly, no product rule needed. The product rule is only required when BOTH factors depend on x. Recognizing when to use the simpler rule (constant multiple) vs. the product rule is itself a key skill."

- question: "The product rule correctly states that d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)."
  type: true-false
  answer: true
  explanation: "This is the product rule. The geometric intuition: imagine a rectangle with sides f and g (area = fg). When x increases slightly, the area gains two strips — one of height g and width f'Δx, one of width f and height g'Δx — giving (f'g + fg')Δx in total new area. The tiny corner piece (f'g'(Δx)²) vanishes in the limit, leaving exactly this formula."

- question: "Why is the derivative of a product NOT simply the product of the derivatives? Explain using an example."
  type: short-answer
  answer: "When two quantities both depend on x, each one's change interacts with the other's current value — creating two cross-terms, not one. For example, if f(x) = g(x) = x, then f(x)g(x) = x², whose derivative is 2x. But f'(x)·g'(x) = 1·1 = 1 ≠ 2x. The product rule captures both interactions: f'g = 1·x = x and fg' = x·1 = x, summing to 2x."
  explanation: "The error (fg)' = f'g' treats the two factors as independent, but they are not — they share the same variable x. The rectangle analogy makes this concrete: two sides both growing simultaneously create two strips of new area, not one. Calculus must account for both."
```

## Explainer

From your work with the constant multiple and sum rules, you know that differentiation is linear: you can pull out constants and differentiate term by term. A natural next question is whether multiplication works similarly — can you just differentiate each factor and multiply the results? The answer is no, and understanding why is the first step to internalizing the product rule. Consider f(x) = x and g(x) = x, so f(x)g(x) = x². If (fg)' = f'g', you would get 1·1 = 1. But d/dx[x²] = 2x. The error grows with x because multiplying two changing quantities creates an interaction that the "differentiate each part separately" idea misses.

The correct formula is d/dx[f(x)g(x)] = **f'(x)g(x) + f(x)g'(x)**. A geometric analogy makes this intuitive. Imagine a rectangle with side lengths f(x) and g(x). Its area is A(x) = f(x)g(x). When x increases by a tiny amount Δx, both sides grow: f increases by Δf ≈ f'Δx and g increases by Δg ≈ g'Δx. The new area has three new pieces: a strip of width Δf and height g (contributing f'g Δx), a strip of width f and height Δg (contributing fg' Δx), and a tiny corner of area ΔfΔg (which is negligible in the limit because it is second-order in Δx). So ΔA ≈ (f'g + fg')Δx, giving dA/dx = f'g + fg'. Each term in the product rule corresponds to one strip of the rectangle.

Applying the rule is straightforward once you identify the two factors. For h(x) = x³sin(x), take f = x³ and g = sin(x). Then f' = 3x² and g' = cos(x), giving h'(x) = 3x²·sin(x) + x³·cos(x). The key habit is to always write out both terms — skipping one is the most common error. The mnemonic "first times derivative of second, plus second times derivative of first" (or "d-first, d-second") helps. Note also when the rule is not needed: if one factor is a constant, like h(x) = 5sin(x), the constant multiple rule gives h'(x) = 5cos(x) directly. The product rule is only necessary when both factors depend on x.

The product rule also reveals why integration by parts — which you will encounter next — works the way it does. Rearranging the product rule: f(x)g'(x) = [f(x)g(x)]' − f'(x)g(x). Integrating both sides gives the integration-by-parts formula. So the product rule is not just a differentiation technique; it is the foundation of one of the most important integration strategies in calculus. Internalizing it now pays dividends throughout the rest of the course.
