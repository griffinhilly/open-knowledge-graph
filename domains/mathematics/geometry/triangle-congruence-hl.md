---
id: triangle-congruence-hl
title: 'Triangle Congruence: HL (Hypotenuse-Leg)'
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sss
    type: hard
  - id: pythagorean-theorem
    type: hard
  - id: triangle-congruence-sas
    type: soft
builds-toward:
  - tangent-lines-to-circles
tags: [geometry, congruence, right-triangles, proof, hypotenuse-leg]
stage: abstract-reasoning
status: validated
---

# Triangle Congruence: HL (Hypotenuse-Leg)

## Core Idea
The Hypotenuse-Leg (HL) Theorem says that if the hypotenuse and one leg of a right triangle are congruent to the hypotenuse and one leg of another right triangle, the triangles are congruent. HL looks like the side-side-angle pattern, which does not prove congruence in general. It works here because the right angle, together with the Pythagorean theorem, fixes the length of the third side, which reduces HL to SSS.

## How It's Best Learned
Have students try to build two different right triangles with a hypotenuse of 13 and a leg of 5; they will find the other leg is forced to be 12. Then contrast with a general SSA example where two different triangles fit the same data. Practice proofs where a shared side or a perpendicular creates the right triangles, such as showing that the two tangent segments from an outside point to a circle are equal.

## Common Misconceptions
- Since SSA is not a congruence test, HL cannot be one either. (HL is a special case of SSA that does work, because the given angle is a right angle and the given non-included side is the hypotenuse.)
- HL can be used for any pair of triangles with two congruent sides. (Both triangles must be right triangles, and one congruent pair must be the hypotenuses.)
- Knowing two legs are congruent is an HL situation. (Two legs and the included right angle is SAS, sometimes called LL.)

## Questions

```yaml
- question: "Right triangles ABC and DEF have right angles at C and F. AB = DE = 10 and AC = DF = 6. Which statement is justified?"
  type: multiple-choice
  options:
    - "The triangles are congruent by SAS"
    - "The triangles are congruent by HL"
    - "No conclusion is possible because this is SSA"
    - "The triangles are similar but not necessarily congruent"
  answer: 1
  explanation: "AB and DE are the hypotenuses (they are opposite the right angles), and AC and DF are legs. Hypotenuse and leg congruent in two right triangles gives congruence by HL. The given angle is not between the two sides, so SAS does not apply."

- question: "Because SSA is not a valid congruence test, the Hypotenuse-Leg pattern also fails to prove congruence."
  type: true-false
  answer: false
  explanation: "HL is a case of SSA that always works. With a right angle, the Pythagorean theorem gives the third side from the other two, so both triangles have all three sides equal and are congruent by SSS."

- question: "A right triangle has hypotenuse 13 and one leg 5. Explain why every right triangle with these measurements is congruent to it."
  type: short-answer
  answer: "By the Pythagorean theorem the other leg is √(13² - 5²) = √144 = 12, so every such triangle has sides 5, 12, 13 and they are congruent by SSS."
  explanation: "The right angle removes the ambiguity that SSA normally has. Only one value of the missing leg is possible, so the triangle is determined."

- question: "From a point P outside a circle with center O, tangent segments PA and PB touch the circle at A and B. Which reasoning shows PA = PB?"
  type: multiple-choice
  options:
    - "Triangles OAP and OBP are congruent by HL, since angles OAP and OBP are right, OP is a shared hypotenuse, and OA = OB"
    - "Triangles OAP and OBP are congruent by AAA"
    - "Triangles OAP and OBP are congruent by SSA with no further facts needed"
    - "PA = PB because all segments from P to the circle are equal"
  answer: 0
  explanation: "A tangent is perpendicular to the radius at the point of tangency, so both triangles are right. They share hypotenuse OP and have congruent legs OA = OB (radii). By HL the triangles are congruent, and corresponding parts give PA = PB."
```

## Explainer

You have learned SSS, SAS, ASA and AAS as ways to prove two triangles congruent. You have also learned that SSA (two sides and an angle that is not between them) does not work in general. With an acute angle, a fixed side next to it, and a fixed side opposite it, the opposite side can often swing into two different positions, giving two different triangles.

There is one important exception. Suppose both triangles are right triangles, and you know that their hypotenuses are congruent and that one pair of legs is congruent. This is still a side-side-angle pattern, since the right angle is not between the hypotenuse and the given leg. Yet the triangles must be congruent. This is the Hypotenuse-Leg Theorem, usually written HL.

The reason comes from the Pythagorean theorem. In a right triangle with hypotenuse c and legs a and b, we have a² + b² = c². If you know c and a, then b = √(c² - a²), and there is only one positive value. So the third side is determined. Two right triangles with the same hypotenuse and the same leg therefore have all three sides equal, and SSS finishes the proof. For example, any right triangle with hypotenuse 13 and leg 5 has other leg √(169 - 25) = √144 = 12.

To use HL in a proof, you must establish three things: both triangles have a right angle, the hypotenuses are congruent, and one pair of legs is congruent. Watch for right angles that come from perpendicular lines, altitudes, or a tangent meeting a radius.

A classic application involves a circle. Draw tangent segments PA and PB from an outside point P, and draw radii OA and OB. A tangent is perpendicular to the radius at the point of tangency, so triangles OAP and OBP are right triangles. They share the hypotenuse OP, and OA = OB because both are radii. By HL the triangles are congruent, so PA = PB. Two tangent segments drawn to a circle from the same outside point are always equal in length.

Keep HL separate from the case of two congruent legs. Two legs with the right angle between them is an SAS situation, so it needs no special theorem.
