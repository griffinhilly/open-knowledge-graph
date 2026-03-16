---
id: sum-and-difference-identities
title: Sum and Difference Identities
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-identities-pythagorean
    type: hard
  - id: unit-circle
    type: hard
builds-toward:
  - double-angle-identities
  - solving-trigonometric-equations
tags: [trigonometry, identities, sum-difference]
stage: formal-systems
status: validated
---

# Sum and Difference Identities

## Core Idea
The sum and difference identities express sin(A +/- B), cos(A +/- B), and tan(A +/- B) in terms of sines and cosines of A and B individually. For example, sin(A + B) = sin(A)cos(B) + cos(A)sin(B). These identities are the engine behind many others (double angle, half angle) and are used to find exact values of non-standard angles, simplify expressions, and solve equations.

## How It's Best Learned
Derive the cosine difference formula geometrically using distance on the unit circle, then obtain the rest algebraically. Practice computing exact values like sin(75) = sin(45 + 30). Use the identities to derive double-angle formulas as a natural next step.

## Common Misconceptions
- Believing sin(A + B) = sin(A) + sin(B): this is the most common and damaging error.
- Mixing up the sign patterns between sine and cosine sum/difference formulas.
- Forgetting the tangent sum formula or not recognizing when to use it.

## Explainer

From your work with the unit circle and Pythagorean identities, you know that sin and cos describe coordinates on a unit circle, and that sin²θ + cos²θ = 1 no matter what angle θ is. The sum and difference identities extend this by answering a natural question: if I know sin A, cos A, sin B, and cos B separately, can I compute sin(A + B) without needing a calculator? The answer is yes — and the resulting formulas are among the most-used in all of trigonometry.

The four core identities are:
- sin(A + B) = sin A cos B + cos A sin B
- sin(A − B) = sin A cos B − cos A sin B
- cos(A + B) = cos A cos B − sin A sin B
- cos(A − B) = cos A cos B + sin A sin B

Notice the sign pattern: for cosine, the sign *flips* (cos of a sum has a minus sign); for sine, the sign *matches* (sin of a sum has a plus sign). A useful mnemonic is "cosine changes sign, sine stays the same as the ±." The most important thing to internalize is that **sin(A + B) ≠ sin A + sin B**. Sine is not a linear function — it does not distribute over addition. A quick counterexample: sin(30° + 60°) = sin 90° = 1, but sin 30° + sin 60° = 0.5 + 0.866 = 1.366 ≠ 1. If you try to distribute sine over a sum, you will consistently get wrong answers.

One of the best uses of these formulas is computing **exact values** of angles not on the standard unit circle. For example, sin 75° = sin(45° + 30°) = sin 45° cos 30° + cos 45° sin 30° = (√2/2)(√3/2) + (√2/2)(1/2) = (√6 + √2)/4. You have turned an unfamiliar angle into a combination of the 30-60-90 and 45-45-90 triangles you already know cold. Similarly, cos 15° = cos(45° − 30°) = cos 45° cos 30° + sin 45° sin 30° = (√6 + √2)/4. Many exam problems give you unusual angles precisely because they expect you to decompose them this way.

These identities are also the engine for deriving everything that follows. Set B = A in the sine sum formula and you immediately get sin 2A = 2 sin A cos A — the double angle formula. Set B = A in the cosine sum formula to get cos 2A = cos²A − sin²A. The half-angle formulas follow by solving for cos²A and sin²A. Every subsequent identity in trigonometry either is a sum/difference identity in disguise or is derived from one. Treating these four formulas as your foundation, rather than memorizing each derived identity separately, is a far more efficient strategy — and understanding the derivation once makes reconstructing a forgotten formula trivial.
