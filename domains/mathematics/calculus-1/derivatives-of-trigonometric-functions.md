---
id: derivatives-of-trigonometric-functions
title: Derivatives of Trigonometric Functions
domain: mathematics
course: calculus-1
prerequisites:
- id: chain-rule
  type: soft
- id: squeeze-theorem
  type: hard
- id: trigonometric-identities-pythagorean
  type: hard
- id: graphing-sine-and-cosine
  type: soft
- id: graphing-tangent-and-reciprocal-trig
  type: soft
builds-toward:
- trigonometric-integrals
tags:
- derivatives
- trigonometry
stage: formal-systems
status: validated
---
# Derivatives of Trigonometric Functions

## Core Idea
The derivatives of the six trig functions are: d/dx[sin(x)] = cos(x), d/dx[cos(x)] = -sin(x), d/dx[tan(x)] = sec^2(x), d/dx[cot(x)] = -csc^2(x), d/dx[sec(x)] = sec(x)tan(x), d/dx[csc(x)] = -csc(x)cot(x). The sine and cosine derivatives follow from the limit definition using lim sin(h)/h = 1 (proved by the squeeze theorem). The others are derived using the quotient rule and Pythagorean identities.

## How It's Best Learned
Derive d/dx[sin(x)] from the limit definition using sum identity and the two key limits. Derive d/dx[cos(x)] similarly or from the chain rule with sin(pi/2 - x). Derive the remaining four using quotient rule. Practice with the chain rule: d/dx[sin(3x)] = 3cos(3x).

## Common Misconceptions
- Forgetting the negative sign in d/dx[cos(x)] = -sin(x).
- Not applying the chain rule when the argument is not just x.
- Mixing up the derivative pairs (sec goes with sec*tan, csc goes with -csc*cot).

## Questions

```yaml
- question: "What is d/dx[cos(2x)]?"
  type: multiple-choice
  options:
    - "sin(2x)"
    - "-sin(2x)"
    - "2sin(2x)"
    - "-2sin(2x)"
  answer: 3
  explanation: "Two errors combine here: forgetting the negative sign (d/dx[cos(x)] = -sin(x), not sin(x)) and applying or omitting the chain rule. The chain rule requires multiplying by the derivative of the inner function 2x, which is 2. So d/dx[cos(2x)] = -sin(2x) · 2 = -2sin(2x). Option A forgets both the negative and the chain rule. Option B forgets only the chain rule. Option C forgets only the negative sign."

- question: "The formula d/dx[sin(x)] = cos(x) is established by:"
  type: multiple-choice
  options:
    - "Observing empirically that the sine and cosine graphs seem related"
    - "Applying the limit definition of the derivative and the squeeze theorem result lim(h→0) sin(h)/h = 1"
    - "Applying the chain rule to the unit circle parametrization"
    - "Noting that the second derivative of sin(x) is -sin(x), so the first must be cos(x)"
  answer: 1
  explanation: "The derivation applies the limit definition (sin(x+h) - sin(x))/h, expands using the angle addition identity sin(x+h) = sin(x)cos(h) + cos(x)sin(h), and uses two limits established by the squeeze theorem: lim sin(h)/h = 1 and lim (cos(h)-1)/h = 0. The result follows rigorously from these limit facts. The other options are informal or circular — option D in particular assumes you already know the answer."

- question: "All four secondary trig derivatives (tan, cot, sec, csc) can be derived from the sine and cosine derivatives using only the quotient rule and Pythagorean identities."
  type: true-false
  answer: true
  explanation: "This is exactly how the derivations work. For example, tan(x) = sin(x)/cos(x), so the quotient rule gives (cos²(x) + sin²(x))/cos²(x), and the Pythagorean identity sin²(x) + cos²(x) = 1 simplifies this to 1/cos²(x) = sec²(x). The same pattern applies to cot, sec, and csc — each is expressed as a ratio of sin and cos, the quotient rule is applied, and a Pythagorean identity compresses the numerator."

- question: "d/dx[sec(x)] = sec(x)cot(x)"
  type: true-false
  answer: false
  explanation: "The correct derivative is d/dx[sec(x)] = sec(x)tan(x), not sec(x)cot(x). Since sec(x) = 1/cos(x), the quotient rule gives sin(x)/cos²(x) = (1/cos(x)) · (sin(x)/cos(x)) = sec(x)tan(x). A useful mnemonic: sec pairs with tan, and csc pairs with -csc·cot (the co-functions form the negated pair). Mixing them up — putting cot with sec — is the most common error."

- question: "Why must you apply the chain rule when differentiating sin(3x), but the formula d/dx[sin(x)] = cos(x) alone is sufficient for sin(x)?"
  type: short-answer
  answer: "sin(x) has the identity function x as its argument, whose derivative is 1, so the chain rule multiplier is 1 and can be ignored. In sin(3x), the argument is the function 3x, whose derivative is 3. The chain rule says: differentiate the outer function (keeping the inner function untouched), then multiply by the derivative of the inner function. So d/dx[sin(3x)] = cos(3x) · 3 = 3cos(3x)."
  explanation: "The six trig derivative formulas assume the argument is simply x. Whenever the argument is any other expression — 3x, x², x²+1 — the chain rule adds an extra multiplicative factor equal to the derivative of that expression. Failure to apply the chain rule is the most common error in trig differentiation practice."
```

## Explainer

The derivatives of the six trigonometric functions are not arbitrary formulas to memorize in isolation — they follow directly from two foundational limits and systematic application of the rules you already know. The entire structure builds from one key limit proved by the squeeze theorem: lim(h→0) sin(h)/h = 1. If you've worked through the squeeze theorem, you've already established the machinery that makes trig differentiation possible.

To find d/dx[sin(x)], apply the limit definition of the derivative: (sin(x+h) − sin(x))/h as h → 0. Expand sin(x+h) using the angle addition identity sin(x+h) = sin(x)cos(h) + cos(x)sin(h). The expression becomes [sin(x)cos(h) + cos(x)sin(h) − sin(x)]/h = sin(x) · (cos(h)−1)/h + cos(x) · sin(h)/h. As h → 0, sin(h)/h → 1 and (cos(h)−1)/h → 0 (a second squeeze theorem limit). The result: **d/dx[sin(x)] = cos(x)**. The cosine derivative follows by the same method or by treating cos(x) = sin(π/2 − x) and applying the chain rule: d/dx[cos(x)] = −sin(x).

The remaining four derivatives come from expressing each function in terms of sine and cosine and applying the quotient rule. For example, tan(x) = sin(x)/cos(x), so by the quotient rule: d/dx[tan(x)] = (cos²(x) + sin²(x))/cos²(x) = 1/cos²(x) = sec²(x). The Pythagorean identity sin²(x) + cos²(x) = 1 is the algebraic glue that simplifies these quotient-rule results into clean forms. The pattern across all six: **co-functions pick up a minus sign** (d/dx[cos] = −sin, d/dx[cot] = −csc², d/dx[csc] = −csc·cot).

In practice, you'll combine these derivatives constantly with the chain rule. When the argument isn't simply x — say sin(3x²) — the chain rule adds an outer derivative: d/dx[sin(3x²)] = cos(3x²) · 6x. Every composite trig function follows this pattern: differentiate the outer trig function (using the table), leave the inner function alone, then multiply by the inner function's derivative. Mastering trig derivatives is mostly mastering this interplay between the six basic formulas and the chain rule.
