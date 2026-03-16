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

## Explainer

You derived the sum identities — formulas expressing sin(A + B) and cos(A + B) in terms of functions of A and B separately. Double angle identities are what you get when you set B = A in those formulas. There is no new machinery: it is the same algebra applied to a special case. But the resulting formulas are used so often they deserve their own name and immediate recognition.

Setting B = A in sin(A + B) = sin A cos B + cos A sin B gives **sin(2A) = 2 sin A cos A**. Both terms merge because they're identical. Setting B = A in cos(A + B) = cos A cos B − sin A sin B gives **cos(2A) = cos²A − sin²A**. This can be rewritten two more ways using the Pythagorean identity sin²A + cos²A = 1: substituting sin²A = 1 − cos²A gives cos(2A) = 2cos²A − 1, and substituting cos²A = 1 − sin²A gives cos(2A) = 1 − 2sin²A. All three are equivalent — which one you use depends on what form is most convenient for the problem at hand.

The practical power of these identities comes from rearranging them into **power-reduction formulas**: cos²A = (1 + cos 2A)/2 and sin²A = (1 − cos 2A)/2. These convert squared trigonometric functions into first-power functions of a doubled angle. This transformation is essential in calculus: ∫ sin²x dx has no obvious antiderivative as written, but after substituting (1 − cos 2x)/2, it becomes ∫(1/2 − cos 2x/2) dx, which integrates directly. The double angle identity doesn't just simplify trig expressions — it unlocks entire families of integrals.

For tangent, dividing the sin formula by the cos formula gives **tan(2A) = 2 tan A / (1 − tan²A)**. This is less commonly memorized since it follows immediately from sin(2A)/cos(2A), but it appears in geometric derivations and trigonometric substitutions. The key fluency to develop is recognizing when to expand (sin or cos of a doubled argument → use the double-angle formula) versus when to reduce (squared trig function → use the power-reduction form). Both directions appear in calculus and both are just the same identity read from different ends.
