---
id: trigonometric-ratios-review
title: Trigonometric Ratios Review
domain: mathematics
course: precalculus
prerequisites:
  - id: right-triangle-trigonometry-intro
    type: hard
builds-toward:
  - unit-circle
  - law-of-sines
  - law-of-cosines
tags: [trigonometry, ratios, right-triangles]
stage: formal-systems
status: validated
---

# Trigonometric Ratios Review

## Core Idea
The six trigonometric ratios (sine, cosine, tangent, cosecant, secant, cotangent) are defined as ratios of sides in a right triangle: opposite, adjacent, and hypotenuse relative to a given acute angle. These ratios connect angle measurement to side length relationships and are the foundation for all of trigonometry. SOH-CAH-TOA is the standard mnemonic.

## How It's Best Learned
Begin with right triangles and concrete calculations. Memorize the definitions via SOH-CAH-TOA and derive the reciprocal functions. Practice with 30-60-90 and 45-45-90 special triangles. Transition from triangles to the unit circle definition to extend trig to all angles.

## Common Misconceptions
- Mixing up which side is opposite vs. adjacent (it depends on which angle you reference).
- Forgetting that trig ratios are ratios, not lengths.
- Believing trig functions only apply to right triangles.

## Questions

```yaml
- question: "In a right triangle, angle θ sits at the bottom-left. The horizontal leg (along the bottom) has length 4 and the vertical leg has length 3. What is sin(θ)?"
  type: multiple-choice
  options: ["4/5", "3/5", "3/4", "4/3"]
  answer: 1
  explanation: "sin(θ) = opposite/hypotenuse. The side *opposite* angle θ (at bottom-left) is the vertical leg (length 3). The hypotenuse = √(3² + 4²) = 5. So sin(θ) = 3/5. The answer 4/5 is cos(θ) — using the adjacent leg instead of the opposite. Identifying which side is opposite is always relative to the angle in question."

- question: "If every side of a right triangle is doubled, the value of sin(θ) for any given angle θ in the triangle also doubles."
  type: true-false
  answer: false
  explanation: "Trig ratios are ratios of sides, so scaling all sides by the same factor cancels out. If opposite = 3 and hypotenuse = 5, then sin = 3/5. After doubling: opposite = 6, hypotenuse = 10, sin = 6/10 = 3/5 — unchanged. The angle determines the ratio; the size of the triangle does not."

- question: "Given sin(θ) = 3/5, what is csc(θ), and what is the general relationship between a trig function and its reciprocal counterpart?"
  type: short-answer
  answer: "csc(θ) = 5/3. Each reciprocal function is the multiplicative inverse of its primary function: csc = 1/sin, sec = 1/cos, cot = 1/tan."
  explanation: "The three reciprocal functions (cosecant, secant, cotangent) do not introduce new information — they are algebraic inverses of sine, cosine, and tangent. Knowing SOH-CAH-TOA and the reciprocal relationships gives you all six trig ratios from any right triangle."
```

## Explainer

The six trigonometric ratios formalize a simple observation: in any right triangle, once you fix an angle, the *ratios* of the sides are completely determined — no matter how big or small the triangle is. Two right triangles with the same acute angle are similar, so their sides are proportional and their ratios are identical. This is why a ratio like sin(30°) = 1/2 is a fact about angles, not about any particular triangle.

SOH-CAH-TOA gives you the three primary ratios relative to a chosen acute angle θ: **sin(θ) = opposite/hypotenuse**, **cos(θ) = adjacent/hypotenuse**, **tan(θ) = opposite/adjacent**. The "opposite" and "adjacent" labels are always relative to θ — this is the most common source of error. If you move the reference angle to the other acute corner, the opposite and adjacent sides swap, and every ratio changes accordingly. Always anchor the labels to the specific angle you are working with.

The three reciprocal functions — cosecant (csc), secant (sec), and cotangent (cot) — are simply the flipped versions: csc = 1/sin, sec = 1/cos, cot = 1/tan. They arise naturally in certain formulas and contexts (particularly in calculus integrals), but they carry no independent information. If you know sin(θ) = 3/5, you immediately know csc(θ) = 5/3. Memorizing these as separate definitions is less important than understanding the reciprocal structure.

One important misconception to correct: trig ratios being defined via right triangles does *not* mean they only apply to right triangles. The definition via right triangles is just the entry point. From here, you will extend these functions to all angles (including obtuse and negative angles) using the unit circle, and eventually to real-number inputs representing any rotation. The right-triangle definitions you are reviewing now are the concrete foundation; the unit circle is the generalization that makes trig applicable to waves, oscillations, complex numbers, and much more.

When working with the special triangles — the 30-60-90 (sides 1, √3, 2) and 45-45-90 (sides 1, 1, √2) — you should aim to recall the ratios directly rather than re-deriving each time. These angles appear constantly in physics, calculus, and engineering. Knowing that sin(45°) = cos(45°) = √2/2 and that sin(30°) = 1/2 while cos(30°) = √3/2 will save you significant time and reduce the chance of errors under pressure.
