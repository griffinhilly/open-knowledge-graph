---
id: double-angle-identities
title: Double Angle Identities
domain: mathematics
course: precalculus
prerequisites:
  - id: sum-and-difference-identities
    type: hard
builds-toward:
  - half-angle-identities
  - solving-trigonometric-equations
  - trigonometric-integrals
tags: [trigonometry, identities, double-angle]
stage: formal-systems
status: validated
---

# Double Angle Identities

## Core Idea
The double angle identities express sin(2A), cos(2A), and tan(2A) in terms of functions of A alone. They are direct consequences of the sum identities with B = A. The cosine double angle identity has three equivalent forms: cos(2A) = cos^2(A) - sin^2(A) = 2cos^2(A) - 1 = 1 - 2sin^2(A). These are heavily used in calculus for integrating even powers of trig functions.

## How It's Best Learned
Derive each by setting B = A in the corresponding sum identity. Emphasize the three forms of cos(2A) and when each is most useful. Practice using them to solve equations, simplify expressions, and (looking ahead) reduce powers for integration.

## Common Misconceptions
- Thinking sin(2A) = 2sin(A) without the cos(A) factor.
- Not recognizing that the power-reduction formulas are just rearrangements of cos(2A).
- Failing to choose the most convenient form of cos(2A) for a given problem.

## Questions

```yaml
- question: "A student computes sin(60°) by writing: sin(60°) = sin(2 × 30°) = 2sin(30°) = 2 × (1/2) = 1. What error did they make?"
  type: multiple-choice
  options:
    - "sin(60°) cannot be written as sin(2 × 30°)"
    - "They omitted the cos(30°) factor — the correct identity is sin(2A) = 2sin(A)cos(A)"
    - "The double angle formula applies only to cosine, not to sine"
    - "sin(30°) = 1/2 is incorrect"
  answer: 1
  explanation: "The most common error with double angle identities is writing sin(2A) = 2sin(A), which is wrong. The correct formula is sin(2A) = 2sin(A)cos(A). The missing cos(A) factor is essential — it comes from setting B = A in sin(A + B) = sinA cosB + cosA sinB, where both terms merge into 2sinA cosA. The correct computation: sin(60°) = 2sin(30°)cos(30°) = 2·(1/2)·(√3/2) = √3/2 ≈ 0.866."

- question: "You need to evaluate ∫cos²(x) dx. Which form of the double angle identity is most directly useful?"
  type: multiple-choice
  options:
    - "cos(2A) = cos²A − sin²A, to convert to a difference of squares"
    - "cos(2A) = 2cos²A − 1, rearranged to cos²A = (1 + cos 2A)/2"
    - "cos(2A) = 1 − 2sin²A, to convert the integrand to a sine expression"
    - "tan(2A) = 2tanA / (1 − tan²A), to rewrite in terms of tangent"
  answer: 1
  explanation: "The power-reduction formula cos²A = (1 + cos 2A)/2 transforms a squared trig function into a first-power function of a doubled angle, which integrates directly: ∫cos²x dx = ∫(1 + cos 2x)/2 dx = x/2 + sin(2x)/4 + C. This is the standard approach for integrating even powers of trig functions in calculus. The form cos²A − sin²A isn't helpful here because it introduces sin²A, creating a new squared trig function to handle."

- question: "The double angle identities are independent results that require separate memorization from the sum identities."
  type: true-false
  answer: false
  explanation: "Double angle identities are not independent — they are the sum identities evaluated at the special case B = A. Setting B = A in sin(A + B) = sinA cosB + cosA sinB immediately gives sin(2A) = 2sinA cosA. Setting B = A in cos(A + B) = cosA cosB − sinA sinB gives cos(2A) = cos²A − sin²A. No new machinery is needed. The identities are worth recognizing on sight for speed, but understanding them as special cases of the sum formulas means you can always rederive them if you forget."

- question: "The power-reduction formula cos²A = (1 + cos 2A)/2 is an algebraic rearrangement of the double angle identity cos(2A) = 2cos²A − 1."
  type: true-false
  answer: true
  explanation: "Starting from cos(2A) = 2cos²A − 1: add 1 to both sides to get 1 + cos(2A) = 2cos²A, then divide by 2 to get cos²A = (1 + cos 2A)/2. These are the same equation, read from different directions. The power-reduction form is just the double angle identity solved for cos²A. Similarly, sin²A = (1 − cos 2A)/2 comes from rearranging cos(2A) = 1 − 2sin²A. The 'two' forms are literally one identity."

- question: "Why does cos(2A) have three equivalent forms, and how do they all arise from a single starting identity?"
  type: short-answer
  answer: "All three forms start from cos(2A) = cos²A − sin²A, which comes from setting B = A in the cosine sum formula. The Pythagorean identity sin²A + cos²A = 1 allows substitution in two directions: replacing sin²A = 1 − cos²A gives cos(2A) = 2cos²A − 1; replacing cos²A = 1 − sin²A gives cos(2A) = 1 − 2sin²A. Each form eliminates one of the two trig functions, which is useful when a problem already has one of them — you choose the form that reduces the number of distinct functions in the expression."
  explanation: "The three forms are most useful in different contexts: cos²A − sin²A when both are present and you want a single cosine; 2cos²A − 1 when only cosine appears; 1 − 2sin²A when only sine appears. In integration, you usually want a form with only one function, leading to the power-reduction formulas. Knowing the Pythagorean identity is what unlocks the flexibility — it's the bridge between all three."
```

## Explainer

You derived the sum identities — formulas expressing sin(A + B) and cos(A + B) in terms of functions of A and B separately. Double angle identities are what you get when you set B = A in those formulas. There is no new machinery: it is the same algebra applied to a special case. But the resulting formulas are used so often they deserve their own name and immediate recognition.

Setting B = A in sin(A + B) = sin A cos B + cos A sin B gives **sin(2A) = 2 sin A cos A**. Both terms merge because they're identical. Setting B = A in cos(A + B) = cos A cos B − sin A sin B gives **cos(2A) = cos²A − sin²A**. This can be rewritten two more ways using the Pythagorean identity sin²A + cos²A = 1: substituting sin²A = 1 − cos²A gives cos(2A) = 2cos²A − 1, and substituting cos²A = 1 − sin²A gives cos(2A) = 1 − 2sin²A. All three are equivalent — which one you use depends on what form is most convenient for the problem at hand.

The practical power of these identities comes from rearranging them into **power-reduction formulas**: cos²A = (1 + cos 2A)/2 and sin²A = (1 − cos 2A)/2. These convert squared trigonometric functions into first-power functions of a doubled angle. This transformation is essential in calculus: ∫ sin²x dx has no obvious antiderivative as written, but after substituting (1 − cos 2x)/2, it becomes ∫(1/2 − cos 2x/2) dx, which integrates directly. The double angle identity doesn't just simplify trig expressions — it unlocks entire families of integrals.

For tangent, dividing the sin formula by the cos formula gives **tan(2A) = 2 tan A / (1 − tan²A)**. This is less commonly memorized since it follows immediately from sin(2A)/cos(2A), but it appears in geometric derivations and trigonometric substitutions. The key fluency to develop is recognizing when to expand (sin or cos of a doubled argument → use the double-angle formula) versus when to reduce (squared trig function → use the power-reduction form). Both directions appear in calculus and both are just the same identity read from different ends.
