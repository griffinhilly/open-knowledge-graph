---
id: integration-by-parts
title: Integration by Parts
domain: mathematics
course: calculus-2
prerequisites:
  - id: product-rule
    type: hard
  - id: u-substitution
    type: hard
builds-toward:
  - trigonometric-integrals
tags: [integration, techniques, by-parts]
stage: formal-systems
status: validated
---

# Integration by Parts

## Core Idea
Integration by parts reverses the product rule: the integral of u dv = uv - the integral of v du. It converts one integral into another, hopefully simpler one. The LIATE rule (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential) helps choose u. Common applications include integrals involving ln(x), x*e^x, x*sin(x), and arctan(x). Sometimes multiple applications or a cyclical trick are needed.

## How It's Best Learned
Derive from the product rule. Practice choosing u and dv using LIATE. Work through standard types: polynomial times exponential, polynomial times trig, logarithms. Show the tabular method for repeated integration by parts. Practice the cyclical case (e.g., integral of e^x sin(x) dx).

## Common Misconceptions
- Choosing u and dv poorly, making the integral harder instead of easier.
- Forgetting the minus sign in uv - integral of v du.
- Not recognizing when integration by parts needs to be applied multiple times or when a cyclical equation arises.

## Questions

```yaml
- question: "To evaluate ∫ x·eˣ dx by integration by parts, which choice of u and dv is most effective?"
  type: multiple-choice
  options: ["u = eˣ, dv = x dx", "u = x, dv = eˣ dx", "u = xeˣ, dv = dx", "Neither; u-substitution is needed instead"]
  answer: 1
  explanation: "Choosing u = x (Algebraic, per LIATE) and dv = eˣ dx gives du = dx and v = eˣ, so the formula yields x·eˣ − ∫eˣ dx = xeˣ − eˣ + C. The reverse choice (u = eˣ) differentiates eˣ into eˣ again, making the new integral ∫x·eˣ dx — the same integral you started with, which is no progress."

- question: "Evaluating ∫ ln(x) dx by integration by parts requires identifying a second function being multiplied by ln(x)."
  type: true-false
  answer: false
  explanation: "You can write ∫ ln(x) dx as ∫ ln(x)·1 dx and set u = ln(x), dv = 1 dx. Then du = (1/x) dx and v = x, giving x·ln(x) − ∫x·(1/x) dx = x·ln(x) − x + C. The factor of 1 is a perfectly valid dv, and this move — taking u to be the entire original integrand — is a standard technique for logarithms and inverse trig functions."

- question: "When integrating ∫ eˣ·sin(x) dx by parts twice, you obtain an equation of the form I = (expression) − I. How do you use this to find the integral?"
  type: short-answer
  answer: "Treat I = ∫ eˣ sin(x) dx as an unknown. After applying IBP twice you get I = eˣ(sin x − cos x) − I. Adding I to both sides gives 2I = eˣ(sin x − cos x), so I = eˣ(sin x − cos x)/2 + C."
  explanation: "The cyclical case arises because differentiating sin(x) twice brings back sin(x), and similarly for eˣ. Rather than being stuck in an infinite loop, the equation I = f(x) − I is algebraically solvable. This is a feature, not a failure — it gives a clean closed-form answer."
```

## Explainer

Integration by parts reverses the product rule. Differentiate the product u·v and you get (uv)' = u'v + uv'. Rearranging: uv' = (uv)' − u'v. Integrate both sides and you arrive at the IBP formula: ∫u dv = uv − ∫v du. The idea is to trade one integral for another — you hope the new integral ∫v du is simpler than what you started with.

The entire game is choosing u and dv wisely. The LIATE mnemonic provides a reliable ordering: favor choosing u from whichever category comes first — Logarithmic, Inverse trigonometric, Algebraic (polynomials), Trigonometric, Exponential. The logic is that functions at the top of LIATE differentiate into simpler forms (ln(x) becomes 1/x), while exponentials and trig at the bottom integrate as easily as they differentiate. For ∫ x·eˣ dx, choose u = x (Algebraic) and dv = eˣ dx. Then du = dx, v = eˣ, and the formula yields xeˣ − ∫ eˣ dx = xeˣ − eˣ + C.

A non-obvious but important case: ∫ ln(x) dx. There is no second function in sight, but you can write it as ∫ ln(x)·1 dx and choose u = ln(x), dv = dx. This gives v = x and the new integral ∫ x·(1/x) dx = ∫ 1 dx, which trivially integrates to x. Result: x·ln(x) − x + C. The same move works for arctan(x) and arcsin(x) — when the integrand is a lone logarithm or inverse trig, use 1 as the silent second factor.

Sometimes IBP must be applied repeatedly. For ∫ x²·eˣ dx, one application reduces the power from 2 to 1; a second reduces it from 1 to 0 and the integral evaluates. The tabular method (writing successive derivatives of u in one column and successive antiderivatives of dv in another, with alternating signs) streamlines this bookkeeping.

The cyclical case is the most surprising. Applying IBP to ∫ eˣ·sin(x) dx, then applying it again to the resulting integral, produces the original integral on the right-hand side — giving I = eˣ(sin x − cos x) − I. This looks circular but is actually useful: add I to both sides, and you get 2I = eˣ(sin x − cos x), so I = eˣ(sin x − cos x)/2 + C. Recognizing the cycle and solving algebraically rather than continuing to iterate is a key IBP skill.
