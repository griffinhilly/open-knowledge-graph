---
id: exterior-angle-theorem
title: Exterior Angle Theorem
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-angle-sum
    type: hard
  - id: angle-pairs
    type: hard
builds-toward:
  - triangle-inequality
  - polygon-angle-sums
tags: [triangles, exterior-angles, angle-relationships]
stage: abstract-reasoning
status: validated
---

# Exterior Angle Theorem

## Core Idea
An exterior angle of a triangle is formed by extending one side. The Exterior Angle Theorem states that the measure of an exterior angle equals the sum of the two nonadjacent (remote) interior angles. This follows directly from the Triangle Angle Sum Theorem: the exterior angle and its adjacent interior angle are supplementary, so the exterior angle equals 180 minus the adjacent interior, which equals the sum of the other two.

## How It's Best Learned
Draw several triangles with extended sides. Measure to verify the relationship. Prove it algebraically from the angle sum theorem. Give problems where students must find exterior angles, and vice versa. Emphasize that this gives a quick shortcut for many angle problems.

## Common Misconceptions
- Confusing the exterior angle with one of the remote interior angles.
- Forgetting which two interior angles are "remote" (nonadjacent) to a given exterior angle.
- Thinking every triangle has only one exterior angle (each vertex has two, and there are six total, in congruent pairs).

## Questions

```yaml
- question: "Triangle ABC has ∠A = 48° and ∠B = 57°. A side is extended past vertex C, forming exterior angle E. What is m∠E?"
  type: multiple-choice
  options:
    - "75° — the remaining interior angle at C (180° − 48° − 57°)"
    - "105° — the sum of the two remote interior angles, ∠A + ∠B"
    - "132° — the supplement of ∠A"
    - "123° — the supplement of ∠B"
  answer: 1
  explanation: "By the Exterior Angle Theorem, the exterior angle equals the sum of the two remote (nonadjacent) interior angles. The remote angles here are ∠A and ∠B: 48° + 57° = 105°. Option A (75°) is the third interior angle at C — the angle adjacent to E — not E itself. The theorem gives a one-step shortcut: no need to find the third interior angle first and subtract from 180°."

- question: "A student calculates an exterior angle by first finding the adjacent interior angle (subtracting the two known angles from 180°), then subtracting that from 180°. A second student directly adds the two remote interior angles. Which is true?"
  type: multiple-choice
  options:
    - "Only the first method is valid — the Exterior Angle Theorem applies only to specific triangle configurations"
    - "Both methods are valid and always give the same answer; the second method is faster"
    - "Only the second method is valid — subtracting twice from 180° introduces errors"
    - "The methods may give different answers depending on whether the triangle is acute or obtuse"
  answer: 1
  explanation: "Both methods are correct and always agree — this is precisely what the Exterior Angle Theorem proves. Method 1: E = 180° − C (supplementary). Method 2: E = A + B (the theorem). They give the same result because C = 180° − A − B (angle sum theorem), so 180° − C = 180° − (180° − A − B) = A + B. The second method is simply faster — it skips the intermediate step of finding the third angle."

- question: "An exterior angle of a triangle is always larger than either of the two remote interior angles individually."
  type: true-false
  answer: true
  explanation: "Since the exterior angle equals the sum of the two remote interior angles (E = A + B) and both A and B are positive (all interior angles of a triangle are between 0° and 180°), E must be greater than each one individually: E = A + B > A (since B > 0) and E = A + B > B (since A > 0). This inequality is actually used to prove the Triangle Inequality theorem."

- question: "Each vertex of a triangle has exactly one exterior angle."
  type: true-false
  answer: false
  explanation: "Each vertex of a triangle has two exterior angles — one formed by extending each of the two sides that meet at that vertex. However, these two exterior angles are vertical angles (formed by two lines intersecting), so they are always congruent. In practice, 'the' exterior angle at a vertex refers to either one (since they're equal), but geometrically there are two. Each triangle has six exterior angles total, in three congruent pairs."

- question: "Prove the Exterior Angle Theorem using only the Triangle Angle Sum Theorem and the fact that angles on a straight line sum to 180°."
  type: short-answer
  answer: "Let the triangle have interior angles A, B, and C, and let E be the exterior angle formed at vertex C by extending one side. (1) Since E and C lie on a straight line, they are supplementary: E + C = 180°. (2) By the Triangle Angle Sum Theorem: A + B + C = 180°. (3) Both expressions equal 180°, so: E + C = A + B + C. (4) Subtracting C from both sides: E = A + B. Therefore the exterior angle equals the sum of the two remote interior angles."
  explanation: "The proof is elegant because it requires only two facts you already know, combined in a single step. The key move is recognizing that both E + C and A + B + C equal 180°, which forces E = A + B. This is also why the theorem is really just a restatement of the angle sum theorem — not an independent fact, but a consequence you can derive in two lines."
```

## Explainer

You know from the **Triangle Angle Sum Theorem** that the three interior angles of any triangle always add to 180°. The Exterior Angle Theorem is a short but powerful consequence of that fact. When you extend one side of a triangle past a vertex, the angle formed outside the triangle — the **exterior angle** — has a surprisingly direct relationship to the triangle's interior angles.

Here's the proof in two steps. Call the interior angles A, B, and C, where C is the angle adjacent to the exterior angle we'll call E. Because E and C are on a straight line, they are **supplementary**: E + C = 180°. But we also know A + B + C = 180°. Setting these equal: E + C = A + B + C. Subtract C from both sides and you get E = A + B. The exterior angle equals the sum of the two **remote interior angles** — the two interior angles that are *not* adjacent to it.

This result is more useful than it first appears because it converts a two-step calculation (find the third angle, subtract from 180°) into a one-step shortcut. If you know two angles of a triangle are 40° and 65°, you immediately know the exterior angle at the third vertex is 105° — no subtraction from 180° needed. The theorem also gives you a quick inequality: an exterior angle is always *larger* than either of the remote interior angles individually, since it equals their sum and both are positive. This inequality is actually the key ingredient in proving the Triangle Inequality (that any side of a triangle is shorter than the sum of the other two).

A common source of confusion is identifying the *right* remote interior angles for a given exterior angle. Remember: only one exterior angle is formed at each extended vertex, and the remote angles are the *other* two interior angles — the ones at the far ends of the triangle, not the one sitting right next to the exterior angle. Drawing a fresh diagram and labeling all three interior angles before using the theorem eliminates most errors.
