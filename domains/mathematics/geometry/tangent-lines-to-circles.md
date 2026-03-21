---
id: tangent-lines-to-circles
title: Tangent Lines to Circles
domain: mathematics
course: geometry
prerequisites:
  - id: circle-basics
    type: hard
  - id: pythagorean-theorem
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [circles, tangent-lines, perpendicularity, theorems]
stage: abstract-reasoning
status: validated
---

# Tangent Lines to Circles

## Core Idea
A tangent line touches a circle at exactly one point (the point of tangency). A fundamental theorem states that a tangent line is perpendicular to the radius drawn to the point of tangency. Conversely, if a line is perpendicular to a radius at its endpoint on the circle, it is tangent. Two tangent segments from the same external point are congruent. These properties are used extensively in circle problems and in calculus.

## How It's Best Learned
Draw tangent lines and radii, and verify perpendicularity. Prove the tangent-radius relationship using proof by contradiction. Practice using the Pythagorean theorem with the right angle formed by a tangent and radius. Prove the two-tangent theorem using congruent triangles (hypotenuse-leg).

## Common Misconceptions
- Thinking a tangent line passes through the center of the circle (it does not; it just touches the circle).
- Forgetting the perpendicularity condition and drawing tangent lines at arbitrary angles.
- Not recognizing when to apply the Pythagorean theorem using the tangent-radius right angle.

## Questions

```yaml
- question: "A point P is 13 units from the center of a circle with radius 5. A tangent segment is drawn from P to the point of tangency A. What is the length of PA?"
  type: multiple-choice
  options:
    - "8 (distance from P to the circle: 13 − 5)"
    - "12 (using the Pythagorean theorem: √(13² − 5²))"
    - "18 (sum of external distance and radius)"
    - "√194 (using PA² = OP² + OA²)"
  answer: 1
  explanation: "The tangent-radius perpendicularity creates a right angle at A: triangle OAP has a right angle at A, with hypotenuse OP = 13 and leg OA = 5. By the Pythagorean theorem, PA² = OP² − OA² = 169 − 25 = 144, so PA = 12. Option A represents the most common misconception — subtracting the radius from OP as if the tangent length were simply the 'gap' between P and the circle's surface. That calculation ignores the right-triangle geometry entirely."

- question: "Which condition is both necessary and sufficient to guarantee that a line is tangent to a circle?"
  type: multiple-choice
  options:
    - "The line passes through the center of the circle"
    - "The line intersects the circle at exactly one point"
    - "The line is perpendicular to the radius at the point where it meets the circle"
    - "The line is parallel to a diameter"
  answer: 2
  explanation: "Perpendicularity to the radius at the endpoint is the precise condition: a line is tangent if and only if it is perpendicular to the radius at that point. Option B is true of tangent lines, but it describes the result rather than the condition — a line could theoretically intersect at exactly one point without being perpendicular (think of a line tangent to a non-circular curve). The perpendicularity condition is what drives all tangent-line theorems and constructions. Option A describes a secant through the center, not a tangent."

- question: "Two tangent segments drawn from the same external point to a circle are always equal in length."
  type: true-false
  answer: true
  explanation: "This is the two-tangent theorem. If PA and PB are tangent from external point P to a circle with center O, triangles OAP and OBP are right triangles that share hypotenuse OP and have equal legs OA = OB (both radii). By the hypotenuse-leg theorem, the triangles are congruent, so PA = PB. This result holds for any external point and any circle, and it is why all circumscribed polygons (where every side is tangent to an inscribed circle) have a special property relating their side lengths."

- question: "A tangent line to a circle passes through the center of the circle."
  type: true-false
  answer: false
  explanation: "A tangent line only touches the circle at one external point — the point of tangency — and does not pass through the center. A line through the center is a secant (it intersects the circle at two diametrically opposite points). This is a common misconception: students sometimes picture the tangent as 'coming from' the center, confusing the radius drawn to the point of tangency with the tangent line itself. The radius and the tangent line are perpendicular at the tangency point; they are different lines."

- question: "Why does a tangent line form a right angle with the radius at the point of tangency? Explain the geometric reasoning, not just the theorem."
  type: short-answer
  answer: "The radius is the minimum distance from the center to any point on the circle. The tangent line, touching the circle at exactly one point, is the line for which that point is the closest point on the line to the center. The minimum distance from any point to a line is always the perpendicular distance. Therefore, the radius to the tangency point must be perpendicular to the tangent line."
  explanation: "This reasoning — minimum distance implies perpendicularity — connects the tangent-radius theorem to a general principle rather than leaving it as an isolated fact to memorize. It also explains the converse: if a line is perpendicular to a radius at the endpoint on the circle, it must be tangent, because no other point on that line can be closer to the center than the tangency point (the perpendicular is the unique minimum distance)."
```

## Explainer

A **tangent line** to a circle is a line that intersects the circle at exactly one point — the **point of tangency**. This is different from a **secant**, which crosses the circle at two points, and from a line that misses the circle entirely. The defining geometric fact about tangent lines is that they are always perpendicular to the radius at the point of tangency. This isn't just a fact to memorize — it has a clean logical explanation rooted in your circle basics: the radius is the shortest path from the center to any point on the circle. The tangent line, touching the circle at exactly one point, must be the line for which the radius to that point is the minimum distance from the center to the line. The minimum distance from a point to a line is always the perpendicular distance. So the radius to the tangency point must be perpendicular to the tangent.

This perpendicularity is your key to unlocking every tangent-line problem. Whenever you see a tangent touching a circle and a radius drawn to the tangency point, you have a right angle — and wherever there's a right angle in geometry, the **Pythagorean theorem** is available. The standard setup: a point P outside the circle, with a tangent segment PA from P to the point of tangency A, and the radius OA drawn perpendicular to PA. The line from P to the center O forms the hypotenuse: OP² = OA² + PA². You know the radius OA, you know (or want) the distance OP, and you can find PA. This triangle appears constantly in circle problems, and recognizing it immediately — tangent meets radius, forms right angle, draw the hypotenuse — is the central skill.

The **two-tangent theorem** follows elegantly from this setup. If two tangent segments PA and PB are drawn from the same external point P to a circle (A and B being the tangency points), then PA = PB. The proof uses congruent right triangles: triangles OAP and OBP share hypotenuse OP, both have a leg equal to the radius (OA = OB), and both have a right angle at the tangency point. By the hypotenuse-leg theorem, the triangles are congruent, so PA = PB. This is why the two tangent segments from any external point are always equal — a fact that appears in problems about circumscribed polygons (where every side is tangent to an inscribed circle) and in many construction problems.

The converse of the tangent-radius theorem is equally important: if a line is perpendicular to a radius at the point where the radius meets the circle, then that line is tangent. This lets you *construct* tangent lines, not just recognize them. Given a circle and an external point, you can find the tangency points geometrically using the fact that OA ⊥ PA and OP is the hypotenuse — the tangency point A lies on the circle of diameter OP (since any angle inscribed in a semicircle is a right angle, a circle with OP as diameter passes through all points making a right angle with OP, including the tangency points). This connection to inscribed angles ties the tangent concept into the broader web of circle theorems you'll continue building.
