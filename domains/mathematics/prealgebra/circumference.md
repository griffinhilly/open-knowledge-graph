---
id: circumference
title: Circumference of Circles
domain: mathematics
course: prealgebra
prerequisites:
  - id: decimal-place-value
    type: soft
  - id: ratios
    type: soft
builds-toward:
  - area-of-circles
  - arc-length
tags: [circumference, circles, pi, geometry]
stage: abstract-reasoning
status: validated
---

# Circumference of Circles

## Core Idea
Circumference is the distance around a circle. The formulas are C = pi * d (pi times the diameter) or equivalently C = 2 * pi * r (two times pi times the radius). The constant pi (approximately 3.14159) is the ratio of any circle's circumference to its diameter — this ratio is always the same regardless of the circle's size. Pi is irrational, meaning its decimal representation never terminates or repeats. Understanding circumference introduces students to this fundamental constant and to the geometry of curved shapes.

## How It's Best Learned
Have students measure the circumference and diameter of several circular objects (cans, plates, wheels) and compute the ratio — they will discover it is always approximately 3.14. This builds ownership of the concept rather than imposing the formula. Practice computing circumference given radius or diameter. Emphasize the relationship between radius and diameter (d = 2r). Use pi = 3.14 or the pi key on a calculator.

## Common Misconceptions
- Confusing radius and diameter (using one when the formula calls for the other).
- Squaring pi or squaring the diameter in the circumference formula (mixing up circumference and area formulas).
- Thinking pi = 3.14 exactly rather than understanding it is an approximation.

## Questions

```yaml
- question: "A student is asked to find the circumference of a circle with radius 6 cm. She uses the formula C = π × d and substitutes 6 for d, getting C = 6π cm. Is her answer correct?"
  type: multiple-choice
  options:
    - "Yes — both formulas give the same answer, so substituting either r or d produces 6π"
    - "No — she substituted the radius where the formula requires the diameter; the correct answer is 12π cm"
    - "No — she should have used C = 2πr, and that formula gives C = 36π cm"
    - "Yes — for a circle with radius 6, the diameter is also 6"
  answer: 1
  explanation: "C = πd requires the diameter, not the radius. The diameter is twice the radius, so d = 2 × 6 = 12 cm. The correct answer is C = π × 12 = 12π cm. Alternatively, using C = 2πr directly: C = 2 × π × 6 = 12π cm. Both formulas give the same answer because they express the same relationship — but you must use the right measurement in each formula. The most common error is plugging the radius into C = πd."

- question: "You measure the circumference and diameter of three circular objects: a coin, a dinner plate, and a bicycle wheel. You then compute C ÷ d for each. What should you find?"
  type: multiple-choice
  options:
    - "A different ratio for each object, since larger circles have a larger ratio"
    - "A ratio close to 3.14159 for each object, because this ratio is constant for all circles"
    - "A ratio equal to the radius of each circle"
    - "A ratio of exactly 3.14 for each, because π equals 3.14"
  answer: 1
  explanation: "Pi is defined as the ratio C/d, and this ratio is the same for every circle regardless of size. This is a discovered fact of geometry, not a human convention. A coin and a bicycle wheel have vastly different sizes but identical C/d ratios — approximately 3.14159. Note that 3.14 is only an approximation; the true value of π is irrational and never terminates or repeats exactly. This universality is what makes π a fundamental constant rather than a circle-specific measurement."

- question: "The ratio of circumference to diameter is the same for every circle, regardless of its size."
  type: true-false
  answer: true
  explanation: "This is the fundamental property that defines π. No matter how large or small the circle, C/d = π ≈ 3.14159. This can be verified empirically by measuring real circular objects and computing the ratio — it is always approximately the same value. Pi is a fixed constant of geometry, not a variable that depends on circle size. This is why it appears in both circumference formulas: the ratio is always π, so C = π × d."

- question: "The circumference of a circle with radius 5 cm is 5π cm."
  type: true-false
  answer: false
  explanation: "The circumference is C = 2πr = 2 × π × 5 = 10π cm. Equivalently, the diameter is d = 2r = 10 cm, so C = πd = 10π cm. The answer 5π would result from forgetting to multiply by 2 — either using C = πr (incorrect formula) or using the radius where the diameter belongs. This is the most common circumference error: confusing radius and diameter in the formula."

- question: "Explain why the formulas C = πd and C = 2πr give identical results for any circle. What is the relationship that makes them equivalent?"
  type: short-answer
  answer: "The diameter of a circle is always exactly twice its radius: d = 2r. Substituting this into C = πd gives C = π(2r) = 2πr, which is exactly the other formula. They express the same relationship in terms of different measurements of the same circle. If you know the radius, use C = 2πr. If you know the diameter, use C = πd. Both arrive at the same circumference because the two formulas are algebraically identical."
  explanation: "The equivalence is algebraic, not coincidental. The underlying truth is C/d = π for every circle, which gives C = πd. Since d = 2r always, substituting yields C = 2πr. Students sometimes think the two formulas are different rules — they are one rule expressed two ways depending on which circle measurement you start with."
```

## Explainer

**Circumference** is simply the distance you would walk if you followed the edge of a circle all the way around. If you unwrapped that edge and laid it flat, it would form a straight line segment — and that length is the circumference. The question is: how long is that line compared to the circle's size?

The key discovery is that the ratio of circumference to diameter is always the same, no matter how big or small the circle. A bicycle wheel three feet across has a circumference exactly pi times three feet. A coin a quarter-inch across has a circumference exactly pi times a quarter inch. The constant pi (approximately 3.14159) is built into the geometry of circles — it is not something humans invented or chose, but a fixed fact of mathematics. This is why pi appears in both formulas: C = pi × d (using diameter) and C = 2 × pi × r (using radius). Since the diameter is always twice the radius (d = 2r), these two formulas say exactly the same thing.

To use the formulas, you just need to know which measurement you have. If you know the diameter, multiply by pi. If you know the radius, multiply by 2 and then by pi. For example, a circle with radius 5 cm has circumference C = 2 × pi × 5 = 10pi ≈ 31.4 cm. A circle with diameter 10 cm gives C = pi × 10 = 10pi — the same answer, because a radius of 5 cm means a diameter of 10 cm.

Pi is an **irrational number**, which means its decimal expansion goes on forever without repeating: 3.14159265358979... Using 3.14 is an approximation that is good enough for most purposes. When a problem asks for an exact answer, leave it in terms of pi (write "10pi" rather than "31.4"). When a problem asks for a decimal approximation, use 3.14 or the pi key on your calculator. These two circumference formulas are the foundation for more advanced circle geometry — the area formula A = pi × r² uses the same ingredients, and arc length (a portion of circumference) extends the same idea to parts of circles.
