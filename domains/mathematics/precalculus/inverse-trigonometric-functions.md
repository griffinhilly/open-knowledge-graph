---
id: inverse-trigonometric-functions
title: Inverse Trigonometric Functions
domain: mathematics
course: precalculus
prerequisites:
  - id: inverse-functions-review
    type: hard
  - id: unit-circle
    type: hard
builds-toward:
  - solving-trigonometric-equations
  - implicit-differentiation
  - trigonometric-substitution
tags: [trigonometry, inverse-functions, arcsin, arccos, arctan]
stage: formal-systems
status: validated
---

# Inverse Trigonometric Functions

## Core Idea
Since trig functions are periodic (not one-to-one), we restrict their domains to create invertible versions: arcsin on [-pi/2, pi/2], arccos on [0, pi], arctan on (-pi/2, pi/2). These inverse trig functions answer the question "what angle has this trig value?" Understanding their restricted ranges is critical for getting correct answers in equations and for the derivative formulas in calculus.

## How It's Best Learned
Start with why restriction is necessary (horizontal line test fails on unrestricted trig). Graph each inverse function as a reflection of the restricted parent. Practice evaluating arcsin(1/2), arccos(-sqrt(2)/2), etc. by thinking about the unit circle within the restricted range.

## Common Misconceptions
- Confusing sin^(-1)(x) with 1/sin(x).
- Ignoring the restricted range and giving multiple answers when only one is correct.
- Evaluating arcsin(sin(5*pi/4)) as 5*pi/4 instead of adjusting to the range [-pi/2, pi/2].

## Questions

```yaml
- question: "What is the value of arcsin(sin(5π/4))?"
  type: multiple-choice
  options:
    - "5π/4"
    - "−π/4"
    - "3π/4"
    - "π/4"
  answer: 1
  explanation: "sin(5π/4) = −√2/2. Now arcsin must return a value in [−π/2, π/2]. The angle in that range with sine −√2/2 is −π/4. The answer is NOT 5π/4, even though sin(5π/4) was the input — arcsin only 'undoes' sine for angles already in [−π/2, π/2]. 5π/4 lies outside that range, so the function forgets which branch it came from, just as √(x²) gives |x|, not x."

- question: "A student writes: 'sin⁻¹(x) = 1/sin(x), so arcsin(2) = 1/sin(2).' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — sin⁻¹ and 1/sin(x) are the same by the exponent rule"
    - "sin⁻¹(x) means the inverse function of sine, not the reciprocal; and arcsin(2) is undefined since 2 > 1"
    - "The formula is correct but arcsin(2) should be evaluated in degrees, not radians"
    - "sin⁻¹(x) = 1/sin(x) only for x in [0, 1]"
  answer: 1
  explanation: "The notation sin⁻¹(x) means the arcsine — the inverse function — not 1/sin(x). The reciprocal of sine is csc(x). Additionally, arcsin has domain [−1, 1] because sine only takes values in that range; arcsin(2) is simply undefined. This confusion between inverse functions and reciprocals is extremely common and leads to systematic errors."

- question: "arccos(−√2/2) = 3π/4, which is outside the range [0, π/2], so arccos can rarely be correct here."
  type: true-false
  answer: false
  explanation: "The range of arccos is [0, π], not [0, π/2]. 3π/4 is in [0, π], so it is a valid output of arccos. Indeed, cos(3π/4) = −√2/2, confirming the result. The restricted domain for arccos covers the upper semicircle — all the way from 0 to π — precisely so that it can handle negative values, which correspond to angles in the second quadrant."

- question: "The notation sin⁻¹(x) and the notation arcsin(x) always refer to the same function."
  type: true-false
  answer: true
  explanation: "Both notations mean the inverse sine function — the function that takes a value in [−1, 1] and returns the unique angle in [−π/2, π/2] with that sine. They are completely interchangeable. The potential for confusion is that the '−1' in sin⁻¹ looks like an exponent, which would mean 1/sin(x), but in function notation f⁻¹ always means the inverse function."

- question: "Why must the domain of sine be restricted before we can define arcsin, and which restriction is chosen?"
  type: short-answer
  answer: "Sine is periodic and therefore not one-to-one — every horizontal line between −1 and 1 intersects the sine curve infinitely many times. An inverse function can only exist for a one-to-one (injective) function. We restrict sine to [−π/2, π/2], one arc from the bottom to the top of the curve, where it is strictly increasing and passes the horizontal line test. This interval is chosen by convention because it includes 0 and is centered at the origin."
  explanation: "The restriction is not arbitrary geometry — it is a logical necessity. Without restricting the domain, 'arcsin(1/2)' would have infinitely many valid answers (π/6, 5π/6, π/6 ± 2π, etc.), making it not a function. The standard restriction [−π/2, π/2] is simply the most natural and convenient single branch; arccos uses [0, π] and arctan uses (−π/2, π/2) for analogous reasons."
```

## Explainer

From the unit circle, you know that sin(π/6) = 1/2. But if someone asks "what angle has a sine of 1/2?", there is a problem: infinitely many angles do. Every full rotation brings you back to the same y-coordinate, so π/6, π/6 + 2π, π/6 − 2π, and also 5π/6, 5π/6 + 2π, and so on all have sine equal to 1/2. You know from inverse functions that a function must be one-to-one (pass the horizontal line test) to have an inverse. Sine fails that test badly — every horizontal line between −1 and 1 hits the sine curve infinitely many times.

The solution is **domain restriction**: we agree to keep only a portion of the sine curve where it is one-to-one, then define the inverse on that restricted piece. For sine, we use [−π/2, π/2] — one arc from the bottom to the top. This gives **arcsin** (also written sin^−1), which takes a value in [−1, 1] and returns the unique angle in [−π/2, π/2] with that sine. So arcsin(1/2) = π/6, not 5π/6. Both are valid angles with sine 1/2, but only π/6 falls in the agreed-upon range. The restriction is a convention — we had to pick one branch, and these are the standard choices.

For **arccos**, the restriction is [0, π] — the upper semicircle of the unit circle. For **arctan**, the restriction is (−π/2, π/2) — one period of the tangent function (open because tangent has vertical asymptotes at the endpoints). These choices make each inverse function produce a single, predictable output. The notation sin^−1(x) means the arcsine, *not* 1/sin(x). If you mean the reciprocal, write csc(x). This distinction matters constantly.

The most common mistake is forgetting the range when composing a trig function with its inverse. arcsin(sin(θ)) = θ is *only* true when θ is already in [−π/2, π/2]. If θ = 5π/4, then sin(5π/4) = −√2/2, and arcsin(−√2/2) = −π/4, not 5π/4. The function "undo" only works within the restricted range. Think of it like taking a square root: √(x²) = |x|, not always x, because squaring destroys the sign information. Similarly, applying sin then arcsin "forgets" which branch you were on if you started outside the principal range. Keeping the restricted ranges firmly in mind — [−π/2, π/2] for arcsin, [0, π] for arccos, (−π/2, π/2) for arctan — prevents this entire family of errors.
