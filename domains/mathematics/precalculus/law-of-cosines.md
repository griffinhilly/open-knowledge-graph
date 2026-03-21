---
id: law-of-cosines
title: Law of Cosines
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-ratios-review
    type: hard
builds-toward:
  - dot-product
tags: [trigonometry, triangles, law-of-cosines]
stage: formal-systems
status: validated
---

# Law of Cosines

## Core Idea
The Law of Cosines states that c^2 = a^2 + b^2 - 2ab*cos(C), generalizing the Pythagorean theorem to non-right triangles (when C = 90, the formula reduces to c^2 = a^2 + b^2). It is used when you know two sides and the included angle (SAS) or all three sides (SSS). Combined with the Law of Sines, it allows you to solve any triangle.

## How It's Best Learned
Derive using coordinate geometry or the distance formula. Practice SAS cases (find the third side) and SSS cases (find an angle). Compare with the Pythagorean theorem to build intuition about the correction term -2ab*cos(C).

## Common Misconceptions
- Forgetting the negative sign in -2ab*cos(C), especially when the angle is obtuse (which makes cos(C) negative, so the term adds).
- Using the wrong angle in the formula (C must be the angle between sides a and b).
- Not recognizing when to use Law of Cosines vs. Law of Sines.

## Questions

```yaml
- question: "A triangle has sides a = 5, b = 7, and included angle C = 120°. When you apply the Law of Cosines, the correction term −2ab·cos(C) will be:"
  type: multiple-choice
  options:
    - "Negative, making c² smaller than a² + b²"
    - "Zero, because cos(120°) = 0"
    - "Positive, making c² larger than a² + b²"
    - "Irrelevant — the Law of Cosines only applies when C is acute"
  answer: 2
  explanation: "When C is obtuse (greater than 90°), cos(C) is negative. So −2ab·cos(C) becomes −2ab·(negative number) = a positive value. This positive correction stretches c² above a² + b², which makes geometric sense: an obtuse angle splays the two sides apart, making the opposite side longer than the Pythagorean theorem would predict for a right triangle. This is one of the most commonly missed subtleties — students who forget the sign of cos(C) for obtuse angles will miscalculate."

- question: "You know all three sides of a triangle (SSS) and want to find an angle. Which approach uses the Law of Cosines correctly?"
  type: multiple-choice
  options:
    - "Solve c² = a² + b² − 2ab·cos(C) for c, then use the result to find C"
    - "Rearrange to cos(C) = (a² + b² − c²) / (2ab), then apply arccosine"
    - "Use the Law of Sines: sin(C)/c = sin(A)/a, since it's simpler for SSS"
    - "SSS is indeterminate — you need at least one angle to apply the Law of Cosines"
  answer: 1
  explanation: "For SSS (all three sides known), rearrange the formula algebraically: cos(C) = (a² + b² − c²) / (2ab). Then C = arccos of that value. Option A solves for c (a side, not an angle), so it's wrong for this task. Option C is incorrect because Law of Sines requires at least one angle for SSS triangles; it is ambiguous and cannot be initiated from three sides alone. SSS is perfectly determinate — three side lengths uniquely define a triangle's angles."

- question: "For an obtuse triangle where angle C > 90°, the side c opposite angle C is longer than what the Pythagorean theorem would predict."
  type: true-false
  answer: true
  explanation: "The Pythagorean theorem predicts c² = a² + b² for a right angle. The correction term −2ab·cos(C) adjusts for the actual angle. When C > 90°, cos(C) < 0, so −2ab·cos(C) > 0, adding to a² + b². Therefore c² > a² + b², meaning c exceeds the Pythagorean prediction. This matches the geometric intuition: opening angle C beyond 90° pushes the vertex farther away, stretching the opposite side."

- question: "When C = 90°, the Law of Cosines reduces to c² = a² + b² because the correction term −2ab·cos(C) equals zero."
  type: true-false
  answer: true
  explanation: "cos(90°) = 0 exactly, so −2ab·cos(90°) = 0, and the formula reduces to the Pythagorean theorem. This is not a coincidence — the Law of Cosines is the generalization, and the Pythagorean theorem is the special case. Understanding this relationship shows that the Pythagorean theorem is not a separate law but a particular instance of a more general geometric truth about how side lengths and angles relate in any triangle."

- question: "Why does the correction term −2ab·cos(C) in the Law of Cosines change sign depending on whether C is acute or obtuse, and what does each case mean geometrically?"
  type: short-answer
  answer: "When C is acute, cos(C) > 0, so −2ab·cos(C) < 0 — c² is less than a² + b², meaning the opposite side is shorter than the right-triangle prediction. A narrow angle brings the two sides closer together. When C is obtuse, cos(C) < 0, so −2ab·cos(C) > 0 — c² exceeds a² + b², meaning the opposite side is longer. An obtuse angle splays the sides apart. The correction term adjusts the Pythagorean prediction based on how much the triangle deviates from a right angle."
  explanation: "The sign behavior of the correction term is the key to understanding the Law of Cosines as a continuous generalization of the Pythagorean theorem. At C = 90°, the correction is exactly zero. Below 90°, it subtracts; above 90°, it adds. This sign flip at 90° mirrors the behavior of cosine itself: positive in the first quadrant, zero at 90°, negative in the second. Recognizing this connection makes the formula memorable rather than arbitrary."
```

## Explainer

The **Law of Cosines** is a generalization of the Pythagorean theorem you've relied on for right triangles. The Pythagorean theorem says c² = a² + b² when angle C is exactly 90°. But most triangles don't have a right angle. The Law of Cosines corrects for the deviation: c² = a² + b² − 2ab·cos(C), where C is the angle opposite side c and between sides a and b. When C = 90°, cos(90°) = 0, so the correction term vanishes and you're back to the Pythagorean theorem. The law works for any angle in any triangle.

The intuition for the correction term comes from how the angle C pushes the opposite side c longer or shorter. When C is acute (less than 90°), cos(C) is positive, so −2ab·cos(C) is negative — the correction shrinks c² below a² + b². Think of it this way: a narrow angle brings two sides close together, making the opposite side shorter than the Pythagorean guess. When C is obtuse (greater than 90°), cos(C) is negative, so −2ab·cos(C) becomes positive — the correction stretches c² above a² + b². An obtuse angle splays the sides apart, making the opposite side longer than the right-angle case would suggest. This is why the formula makes geometric sense even when you can't visualize it directly.

You use the Law of Cosines in two situations based on what information you have. In the **SAS case** (two sides and the included angle), you know a, b, and C, and you compute c directly. In the **SSS case** (all three sides), you know a, b, and c, and you solve for the angle: cos(C) = (a² + b² − c²) / (2ab). Rearranging to find angles from sides is exactly backward from finding sides from angles — just divide through by 2ab and apply arccosine. When you need to find a remaining angle after using SAS to find the third side, you can either apply the Law of Cosines again or switch to the Law of Sines, whichever is more convenient.

The connection to the **dot product** you'll encounter later is not coincidental. The dot product of two vectors **a** and **b** is defined as |**a**||**b**|cos(θ), where θ is the angle between them. The Law of Cosines is essentially the statement that |**a** − **b**|² = |**a**|² + |**b**|² − 2**a**·**b**. In other words, the Law of Cosines is the dot product identity written in terms of side lengths and angles. This connection reveals why cosine appears naturally in triangle geometry — it measures the geometric projection of one side onto another.
