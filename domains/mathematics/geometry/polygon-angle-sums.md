---
id: polygon-angle-sums
title: Polygon Angle Sums
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-angle-sum
    type: hard
  - id: exterior-angle-theorem
    type: soft
  - id: 2d-shape-properties-1st
    type: soft
builds-toward:
  - regular-polygons
tags: [polygons, angle-sum, interior-angles, exterior-angles]
stage: abstract-reasoning
status: validated
---

# Polygon Angle Sums

## Core Idea
The sum of the interior angles of an n-sided polygon is (n-2) times 180 degrees. This is derived by dividing the polygon into (n-2) triangles from one vertex. The sum of exterior angles of any convex polygon is always 360 degrees. These formulas enable finding individual angle measures, especially in regular polygons.

## How It's Best Learned
Draw diagonals from one vertex of various polygons and count the triangles formed. Establish the pattern: triangle (180), quadrilateral (360), pentagon (540), etc. Derive the general formula. For exterior angles, walk around the polygon making turns and observe that you complete one full rotation (360 degrees).

## Common Misconceptions
- Confusing interior and exterior angle sums.
- Using n instead of (n-2) in the formula.
- Applying the exterior angle sum of 360 to concave polygons without adjustment.
- Forgetting that exterior angle and interior angle at each vertex are supplementary.

## Questions

```yaml
- question: "A regular polygon has interior angles that each measure 150°. How many sides does it have?"
  type: multiple-choice
  options:
    - "10 sides"
    - "12 sides"
    - "8 sides"
    - "15 sides"
  answer: 1
  explanation: "Each interior angle is 150°, so each exterior angle is 180° − 150° = 30° (since interior and exterior angles at each vertex are supplementary). The exterior angle sum of any convex polygon is always 360°, so the number of sides = 360° ÷ 30° = 12. You can verify with the interior formula: (n−2)×180° ÷ n = 150° → (n−2)×180 = 150n → 180n − 360 = 150n → 30n = 360 → n = 12. The exterior angle shortcut is often faster."

- question: "How does the sum of interior angles change when a polygon gains one additional side — for example, going from a pentagon to a hexagon?"
  type: multiple-choice
  options:
    - "It stays the same — the interior angle sum formula always produces 360° regardless of n"
    - "It increases by 180° — each additional side adds exactly one more triangle to the triangulation"
    - "It doubles — a hexagon has twice the interior angle sum of a triangle"
    - "It increases by 360° — because the exterior angle sum is always 360°, the interior sum grows by the same amount"
  answer: 1
  explanation: "Each additional side adds exactly one more triangle to the triangulation from a fixed vertex: a pentagon splits into 3 triangles (sum = 540°), a hexagon into 4 (sum = 720°). The difference is always 180°. Formally: (6−2)×180° − (5−2)×180° = 4×180° − 3×180° = 180°. Every additional side contributes exactly one triangle's worth of angle to the total. This is why the formula is (n−2)×180° and not n×180°."

- question: "The sum of the exterior angles of a regular hexagon is greater than the sum of the exterior angles of a regular triangle, because the hexagon has more sides and therefore more exterior angles."
  type: true-false
  answer: false
  explanation: "The sum of exterior angles of any convex polygon is always exactly 360°, regardless of the number of sides. A triangle has three exterior angles of 120° each: 3 × 120° = 360°. A hexagon has six exterior angles of 60° each: 6 × 60° = 360°. More sides means each individual exterior angle is smaller, but there are more of them — the total is invariant at 360°. This constant exterior angle sum is what makes the walking-the-perimeter intuition work."

- question: "Every interior angle of a regular polygon with n sides measures (n−2) × 180° ÷ n degrees."
  type: true-false
  answer: true
  explanation: "In a regular polygon, all interior angles are equal. The total interior angle sum is (n−2)×180°, and dividing equally among n angles gives (n−2)×180° ÷ n per angle. For a regular hexagon: 4×180° ÷ 6 = 720° ÷ 6 = 120°. This is why hexagonal tiles fit together perfectly at vertices — three 120° angles sum to exactly 360°, filling the space around a point without gaps or overlap. For a regular triangle: 1×180° ÷ 3 = 60° per angle, as expected."

- question: "Why does the sum of exterior angles of any convex polygon always equal 360°, regardless of the number of sides?"
  type: short-answer
  answer: "Imagine walking the perimeter of a convex polygon. At each vertex, you turn by the exterior angle — the supplement of the interior angle. After completing the full circuit and returning to your starting position facing the original direction, you have rotated exactly once — a total of 360°. This total turning is invariant because it equals one complete revolution, regardless of how many sides the polygon has or how the 360° is distributed across individual turns."
  explanation: "With more sides, each individual turn is smaller, but there are more of them — the total is always 360°. For a triangle, three large turns (120° each) sum to 360°. For a regular decagon, ten small turns (36° each) also sum to 360°. The insight is that the total angular change depends on the topological fact that you traversed a simple closed curve and returned to your starting orientation — not on the specific number of sides. This also connects back to the interior formula: since interior + exterior = 180° at each vertex, total interior + 360° = n×180°, so total interior = (n−2)×180°."
```

## Explainer

You already know that the angles of a triangle sum to 180°. That single fact is the engine behind everything in this topic — the polygon angle-sum formula is just a systematic way of breaking any polygon into triangles and adding up what you already know.

Pick any vertex of a polygon and draw diagonals to every other non-adjacent vertex. A quadrilateral splits into 2 triangles, a pentagon into 3, a hexagon into 4. The pattern is always (n−2) triangles for an n-sided polygon, because from one vertex you can draw n−3 diagonals, creating n−2 triangular pieces. Since each triangle contributes 180°, the total **interior angle sum** is **(n−2) × 180°**. Check: quadrilateral gives 2 × 180 = 360°, which matches what you can verify by cutting a paper quadrilateral's corners and arranging them around a point.

The **exterior angle sum** has an even cleaner intuition. Imagine walking along the perimeter of a convex polygon. At each vertex, you turn by the exterior angle — the supplement of the interior angle at that vertex. After completing the full loop, you've turned a total of exactly 360°, because you're back facing the same direction after one full rotation. This gives the remarkable result that the sum of exterior angles is always **360°**, regardless of the number of sides. A triangle's exterior angles (120° + 120° + 120°) sum to 360°; so do a hexagon's (60° each, six of them).

These two formulas connect cleanly. The interior and exterior angles at each vertex are **supplementary**: interior + exterior = 180°. So the sum of all interior angles plus the sum of all exterior angles equals n × 180°. Since exterior angles sum to 360°, interior angles sum to n × 180° − 360° = (n−2) × 180° — the same formula, derived a different way. For **regular polygons**, every interior angle is equal, so each measures (n−2) × 180° ÷ n. For a regular hexagon: 4 × 180 ÷ 6 = 120°. This is the reason hexagonal tiles fit together perfectly at vertices — three 120° angles fill a full 360° rotation.
