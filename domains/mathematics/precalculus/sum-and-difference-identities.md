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

## Questions

```yaml
- question: "A student computes sin(45° + 30°) by writing sin(45°) + sin(30°) = 0.707 + 0.500 = 1.207. What is wrong, and what is the correct value?"
  type: multiple-choice
  options:
    - "Nothing is wrong — distributing sine over addition is valid when the angles sum to 75°"
    - "The student used the wrong identity; the correct answer is (√6 + √2)/4 ≈ 0.966, not 1.207"
    - "The student should have multiplied the sines instead: sin(45°) × sin(30°)"
    - "The student's method works only when both angles are from the standard unit circle"
  answer: 1
  explanation: "Sine is not a linear function — it does not distribute over addition. The sum and difference identity gives sin(45° + 30°) = sin45°cos30° + cos45°sin30° = (√2/2)(√3/2) + (√2/2)(1/2) = (√6+√2)/4 ≈ 0.966. A quick sanity check: sin(75°) must be less than 1 since 75° ≠ 90°, so 1.207 is already impossible. The misconception that sin(A+B) = sinA + sinB is the single most common error in trigonometry."

- question: "Which of the following correctly states the cosine difference formula?"
  type: multiple-choice
  options:
    - "cos(A − B) = cos A cos B − sin A sin B"
    - "cos(A − B) = cos A cos B + sin A sin B"
    - "cos(A − B) = sin A cos B − cos A sin B"
    - "cos(A − B) = cos A sin B + sin A cos B"
  answer: 1
  explanation: "The cosine formulas follow the pattern 'cosine changes sign': cos(A+B) = cosAcosB − sinAsinB (minus) and cos(A−B) = cosAcosB + sinAsinB (plus). The minus in the sum becomes a plus in the difference. This is opposite to the sine formulas, where the sign in the identity matches the sign of the argument. A useful check: cos(0) = cos(A−A) = cos²A + sin²A = 1 ✓."

- question: "The formula cos(A + B) = cos A cos B + sin A sin B is correct."
  type: true-false
  answer: false
  explanation: "This is false — the correct formula has a minus sign: cos(A+B) = cosAcosB − sinAsinB. The sign pattern for cosine is that the sum formula has a minus and the difference formula has a plus. This is opposite to sine (where sum → plus, difference → minus). A useful check: cos(60°) = cos(30°+30°) = cos²30° − sin²30° = 3/4 − 1/4 = 1/2 ✓. Using plus would give 3/4 + 1/4 = 1, which would mean cos(60°) = 1 — clearly wrong."

- question: "The formulas for sin(A + B) and sin(A − B) differ only in the sign between their two terms."
  type: true-false
  answer: true
  explanation: "True. sin(A+B) = sinAcosB + cosAsinB, and sin(A−B) = sinAcosB − cosAsinB. The two terms are identical; only the connecting sign changes. This pattern (sign matches the ± in the argument) applies to sine but not cosine, where the signs are inverted."

- question: "Why can't you compute sin(A + B) simply by adding sin A and sin B? Explain using a specific counterexample."
  type: short-answer
  answer: "Because sine is a nonlinear function — it doesn't distribute over addition. Counterexample: sin(30° + 60°) = sin(90°) = 1, but sin(30°) + sin(60°) = 0.5 + 0.866 = 1.366 ≠ 1. The correct formula requires cross terms: sin(A+B) = sinAcosB + cosAsinB. These cross terms reflect how the angles interact geometrically on the unit circle."
  explanation: "The linearity property f(A+B) = f(A)+f(B) holds for functions like f(x) = kx, but not for trigonometric functions. The correct formula has four terms (two products), capturing the interaction between the two angles. The counterexample with 30°+60°=90° is particularly clean because sin(90°)=1 is a known value, making the error in the naive approach obvious."
```

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
