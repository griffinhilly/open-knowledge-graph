---
id: similar-right-triangles-geometric-mean
title: Similar Right Triangles and the Geometric Mean
domain: mathematics
course: geometry
prerequisites:
  - id: similar-triangles-aa
    type: hard
  - id: proportions-in-similar-triangles
    type: hard
  - id: pythagorean-theorem
    type: soft
builds-toward:
  - right-triangle-trigonometry-intro
tags: [geometry, similarity, right-triangles, geometric-mean, altitude]
stage: abstract-reasoning
status: validated
---

# Similar Right Triangles and the Geometric Mean

## Core Idea
Drawing the altitude from the right angle of a right triangle to its hypotenuse splits it into two smaller right triangles, and all three triangles are similar. From that similarity come two geometric-mean relationships. The altitude is the geometric mean of the two hypotenuse segments it creates (h² = pq). Each leg is the geometric mean of the whole hypotenuse and the segment next to that leg (a² = cp). These relationships give a short proof of the Pythagorean theorem.

## How It's Best Learned
Have students cut a right triangle along the altitude to the hypotenuse and rotate the three pieces so matching angles line up. Have them label the triangles with consistent vertex order before writing any proportion. Introduce the geometric mean of two numbers x and y as √(xy) with a numeric example, then solve for missing lengths.

## Common Misconceptions
- The altitude to the hypotenuse cuts the hypotenuse in half. (It does so only when the right triangle is isosceles; in general the two segments have different lengths.)
- The geometric mean of two numbers is their average. (The geometric mean of x and y is √(xy); for 4 and 9 it is 6, while the average is 6.5.)
- Any segment from the right angle to the hypotenuse creates similar triangles. (The segment must be perpendicular to the hypotenuse.)

## Questions

```yaml
- question: "In right triangle ABC with right angle at C, the altitude from C meets hypotenuse AB at D. If AD = 4 and DB = 9, what is CD?"
  type: multiple-choice
  options: ["5", "6", "6.5", "13"]
  answer: 1
  explanation: "The altitude to the hypotenuse is the geometric mean of the two segments: CD² = AD · DB = 4 · 9 = 36, so CD = 6. The value 6.5 is the arithmetic mean and 13 is the whole hypotenuse."

- question: "The altitude drawn from the right angle to the hypotenuse always divides the hypotenuse into two equal parts."
  type: true-false
  answer: false
  explanation: "In the triangle with segments 4 and 9 the parts are unequal. The segments are equal only for an isosceles right triangle, where the altitude is also a median."

- question: "Using the same triangle (AD = 4, DB = 9), find the length of leg AC."
  type: short-answer
  answer: "AC = √(AD · AB) = √(4 · 13) = √52 = 2√13"
  explanation: "Leg AC is the geometric mean of the whole hypotenuse AB = 13 and the segment AD adjacent to it. A check: BC = √(9 · 13) = √117, and AC² + BC² = 52 + 117 = 169 = 13²."

- question: "Why are triangles ACD and ABC similar?"
  type: short-answer
  answer: "Both have a right angle (at D and at C) and they share angle A, so they are similar by AA."
  explanation: "Two pairs of congruent angles are enough for similarity. The same reasoning with shared angle B shows triangle CBD is similar to triangle ABC, so all three triangles are similar to one another."
```

## Explainer

Take right triangle ABC with the right angle at C, and draw the altitude from C perpendicular to the hypotenuse AB. Call its foot D. The altitude cuts the large triangle into two smaller right triangles, ACD and CBD.

Look at triangle ACD. It has a right angle at D, and it shares angle A with the original triangle ABC. Two pairs of congruent angles mean the triangles are similar by AA. In the same way, triangle CBD has a right angle at D and shares angle B with ABC, so it is similar to ABC too. Since both small triangles are similar to the large one, they are similar to each other. All three triangles have the same shape at different sizes.

Similar triangles have proportional sides, and two proportions are worth naming. Let p = AD and q = DB be the pieces of the hypotenuse, and let h = CD. Matching triangle ACD with triangle CBD gives AD/CD = CD/DB, which is p/h = h/q. Cross-multiplying gives h² = pq, so h = √(pq). The number √(pq) is called the geometric mean of p and q. So the altitude to the hypotenuse is the geometric mean of the two segments of the hypotenuse.

Matching triangle ACD with triangle ABC gives AD/AC = AC/AB, so AC² = AD · AB. Each leg is the geometric mean of the whole hypotenuse and the segment of the hypotenuse next to that leg. Likewise, BC² = DB · AB.

Here is a numeric example. If AD = 4 and DB = 9, then AB = 13 and the altitude is h = √(4 · 9) = 6. The legs are AC = √(4 · 13) = √52 and BC = √(9 · 13) = √117.

These relationships also prove the Pythagorean theorem. Add the two leg equations: AC² + BC² = AD · AB + DB · AB = (AD + DB) · AB = AB · AB = AB². In the example, 52 + 117 = 169 = 13². This proof uses only similarity, and it shows why the geometric mean appears naturally in right triangles. The same AA reasoning explains why the trigonometric ratios of an acute angle do not depend on the size of the right triangle.
