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

## Explainer

You already know that the angles of a triangle sum to 180°. That single fact is the engine behind everything in this topic — the polygon angle-sum formula is just a systematic way of breaking any polygon into triangles and adding up what you already know.

Pick any vertex of a polygon and draw diagonals to every other non-adjacent vertex. A quadrilateral splits into 2 triangles, a pentagon into 3, a hexagon into 4. The pattern is always (n−2) triangles for an n-sided polygon, because from one vertex you can draw n−3 diagonals, creating n−2 triangular pieces. Since each triangle contributes 180°, the total **interior angle sum** is **(n−2) × 180°**. Check: quadrilateral gives 2 × 180 = 360°, which matches what you can verify by cutting a paper quadrilateral's corners and arranging them around a point.

The **exterior angle sum** has an even cleaner intuition. Imagine walking along the perimeter of a convex polygon. At each vertex, you turn by the exterior angle — the supplement of the interior angle at that vertex. After completing the full loop, you've turned a total of exactly 360°, because you're back facing the same direction after one full rotation. This gives the remarkable result that the sum of exterior angles is always **360°**, regardless of the number of sides. A triangle's exterior angles (120° + 120° + 120°) sum to 360°; so do a hexagon's (60° each, six of them).

These two formulas connect cleanly. The interior and exterior angles at each vertex are **supplementary**: interior + exterior = 180°. So the sum of all interior angles plus the sum of all exterior angles equals n × 180°. Since exterior angles sum to 360°, interior angles sum to n × 180° − 360° = (n−2) × 180° — the same formula, derived a different way. For **regular polygons**, every interior angle is equal, so each measures (n−2) × 180° ÷ n. For a regular hexagon: 4 × 180 ÷ 6 = 120°. This is the reason hexagonal tiles fit together perfectly at vertices — three 120° angles fill a full 360° rotation.
