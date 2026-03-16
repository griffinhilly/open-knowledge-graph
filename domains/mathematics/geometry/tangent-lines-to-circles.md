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

## Explainer

A **tangent line** to a circle is a line that intersects the circle at exactly one point — the **point of tangency**. This is different from a **secant**, which crosses the circle at two points, and from a line that misses the circle entirely. The defining geometric fact about tangent lines is that they are always perpendicular to the radius at the point of tangency. This isn't just a fact to memorize — it has a clean logical explanation rooted in your circle basics: the radius is the shortest path from the center to any point on the circle. The tangent line, touching the circle at exactly one point, must be the line for which the radius to that point is the minimum distance from the center to the line. The minimum distance from a point to a line is always the perpendicular distance. So the radius to the tangency point must be perpendicular to the tangent.

This perpendicularity is your key to unlocking every tangent-line problem. Whenever you see a tangent touching a circle and a radius drawn to the tangency point, you have a right angle — and wherever there's a right angle in geometry, the **Pythagorean theorem** is available. The standard setup: a point P outside the circle, with a tangent segment PA from P to the point of tangency A, and the radius OA drawn perpendicular to PA. The line from P to the center O forms the hypotenuse: OP² = OA² + PA². You know the radius OA, you know (or want) the distance OP, and you can find PA. This triangle appears constantly in circle problems, and recognizing it immediately — tangent meets radius, forms right angle, draw the hypotenuse — is the central skill.

The **two-tangent theorem** follows elegantly from this setup. If two tangent segments PA and PB are drawn from the same external point P to a circle (A and B being the tangency points), then PA = PB. The proof uses congruent right triangles: triangles OAP and OBP share hypotenuse OP, both have a leg equal to the radius (OA = OB), and both have a right angle at the tangency point. By the hypotenuse-leg theorem, the triangles are congruent, so PA = PB. This is why the two tangent segments from any external point are always equal — a fact that appears in problems about circumscribed polygons (where every side is tangent to an inscribed circle) and in many construction problems.

The converse of the tangent-radius theorem is equally important: if a line is perpendicular to a radius at the point where the radius meets the circle, then that line is tangent. This lets you *construct* tangent lines, not just recognize them. Given a circle and an external point, you can find the tangency points geometrically using the fact that OA ⊥ PA and OP is the hypotenuse — the tangency point A lies on the circle of diameter OP (since any angle inscribed in a semicircle is a right angle, a circle with OP as diameter passes through all points making a right angle with OP, including the tangency points). This connection to inscribed angles ties the tangent concept into the broader web of circle theorems you'll continue building.
