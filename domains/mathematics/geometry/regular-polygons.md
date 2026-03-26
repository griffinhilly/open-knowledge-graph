---
id: regular-polygons
title: Regular Polygons
domain: mathematics
course: geometry
prerequisites:
  - id: polygon-angle-sums
    type: hard
builds-toward:
  - area-of-regular-polygons
tags: [polygons, regular-polygons, symmetry, interior-angles]
stage: abstract-reasoning
status: validated
---

# Regular Polygons

## Core Idea
A regular polygon has all sides congruent and all angles congruent. Each interior angle of a regular n-gon measures (n-2)(180)/n degrees. Each exterior angle measures 360/n degrees. Regular polygons have n lines of symmetry and rotational symmetry of order n. They tile the plane only for n = 3, 4, and 6 (equilateral triangles, squares, regular hexagons).

## How It's Best Learned
Compute interior angles for regular polygons with n = 3 through 10. Observe that as n increases, the interior angle approaches 180. Explore symmetry by folding and rotating. Connect to the inscribed polygon inside a circle. Discuss tilings and why only three regular polygons tile the plane.

## Common Misconceptions
- Assuming any equilateral polygon is regular (equilateral does not imply equiangular for polygons with more than 3 sides, e.g., a rhombus is equilateral but not regular).
- Confusing the interior angle formula with the angle sum formula.
- Thinking all regular polygons can tile the plane.

## Questions

```yaml
- question: "A rhombus has all four sides equal but its angles are not all equal. Is a rhombus a regular polygon?"
  type: multiple-choice
  options:
    - "Yes — a polygon only needs equal sides to be regular"
    - "No — a regular polygon requires both all sides equal AND all angles equal"
    - "Yes, but only if all angles are multiples of 90°"
    - "No — regular polygons must have more than four sides"
  answer: 1
  explanation: "A regular polygon must satisfy two conditions simultaneously: all sides congruent (equilateral) AND all angles congruent (equiangular). A rhombus is equilateral but not equiangular — its acute and obtuse angles differ — so it is not regular. This distinction matters for n > 3: only triangles are automatically equiangular when equilateral. For all other polygons, the two conditions are independent."

- question: "Why can't regular pentagons tile the plane, while regular hexagons can?"
  type: multiple-choice
  options:
    - "Pentagons have too many sides to fit together without gaps"
    - "The interior angle of a regular pentagon (108°) does not divide evenly into 360°, so pentagons cannot meet exactly at a vertex"
    - "Pentagons are not symmetric enough to form a tiling pattern"
    - "Regular pentagons have exterior angles too large to allow edge-to-edge contact"
  answer: 1
  explanation: "For tiles to meet at a vertex without gaps or overlaps, their angles must sum to exactly 360°. A regular hexagon's interior angle is 120°, and 360 ÷ 120 = 3 — so exactly three hexagons meet at each vertex. A regular pentagon's interior angle is 108°, and 360 ÷ 108 is not a whole number (≈ 3.33), so pentagons cannot meet exactly at a vertex. Only equilateral triangles (60°, six per vertex), squares (90°, four per vertex), and regular hexagons (120°, three per vertex) satisfy this divisibility condition."

- question: "The exterior angle of a regular polygon equals 360° divided by the number of sides."
  type: true-false
  answer: true
  explanation: "This follows from a simple walking argument: if you traverse all edges of any convex polygon, you turn a full 360° total. For a regular polygon, every turn is equal, so each exterior angle is 360°/n. For example, a regular octagon (n = 8) has exterior angles of 45°, and 8 × 45° = 360°. This formula is actually simpler than the interior angle formula and makes geometric sense as n grows: as n increases, 360°/n approaches 0°, meaning the polygon approaches a circle with almost no turning at each vertex."

- question: "Any polygon with most sides equal (equilateral) is also a regular polygon."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about regular polygons. A rhombus is equilateral — all four sides are equal — but its angles are not equal (it has two pairs of angles: acute and obtuse). So a rhombus is equilateral but NOT regular. For polygons with more than three sides, equilateral does not imply equiangular. Only for triangles is this automatically true: an equilateral triangle must also be equiangular (all 60°). For all other polygons, you must verify both conditions independently."

- question: "Exactly three regular polygons can tile the plane by themselves. What determines whether a regular polygon can tile the plane, and why does this rule out most polygons?"
  type: short-answer
  answer: "A regular polygon can tile the plane if and only if its interior angle divides evenly into 360°. At each vertex of a tiling, the angles of the meeting polygons must sum to exactly 360° with no gaps or overlaps. For equilateral triangles (60°): 360 ÷ 60 = 6 ✓. For squares (90°): 360 ÷ 90 = 4 ✓. For regular hexagons (120°): 360 ÷ 120 = 3 ✓. For regular pentagons (108°): 360 ÷ 108 ≈ 3.33 ✗. For regular heptagons and beyond, interior angles exceed 120°, so fewer than 3 could meet at a vertex, still not dividing 360° evenly. This divisibility test eliminates all other regular polygons."
  explanation: "The key insight is that tiling is a constraint on angles at vertices, not on edge lengths. Any regular polygon can have its edges matched (they're all equal), but unless its interior angle divides 360° evenly, vertices cannot close up without leaving a gap or forcing an overlap. This makes tiling a number-theoretic question disguised as a geometry problem."
```

## Explainer

From your work on **polygon angle sums**, you know that an n-gon's interior angles sum to (n−2) × 180°. A **regular polygon** has one extra condition on top of that: all sides equal *and* all angles equal. Because all n interior angles are equal and they sum to (n−2) × 180°, each interior angle measures (n−2) × 180° / n. For a triangle (n = 3): (1 × 180°)/3 = 60°. For a square (n = 4): (2 × 180°)/4 = 90°. For a regular hexagon (n = 6): (4 × 180°)/6 = 120°. As n grows, the formula approaches 180°, which makes geometric sense — a polygon with very many sides looks like a circle, and its angles approach the "straight" 180°.

The **exterior angle** is the supplement of the interior angle: 180° − (n−2)×180°/n = 360°/n. This is simpler to remember and deeply intuitive: if you walk all the way around any convex polygon, you turn a total of 360°. For a regular polygon, every turn is equal, so each exterior angle is 360°/n. A regular pentagon has exterior angles of 72°; a regular octagon has 45°. This formula also shows why there's no regular polygon with fewer than 3 sides — you'd need to divide 360° into fewer than 3 parts and still have an interior angle that's positive.

Regular polygons have a rich **symmetry** structure. An n-gon has n lines of reflection symmetry (through each vertex and the midpoint of the opposite side for even n; through each vertex and opposite edge midpoint for odd n) and rotational symmetry of order n (it looks the same after rotations of 360°/n). This double symmetry — reflective and rotational — is what distinguishes regular polygons from merely equilateral or merely equiangular ones.

The question of which regular polygons **tile the plane** (cover it without gaps or overlaps using identical copies) comes down to whether the interior angle divides evenly into 360°. For tiles meeting at a vertex, the angles must sum to exactly 360°. The interior angles of equilateral triangles (60°), squares (90°), and regular hexagons (120°) all divide 360° evenly (6, 4, and 3 meeting at each vertex). For pentagons the interior angle is 108°, and 360/108 is not a whole number, so regular pentagons cannot tile the plane alone. This reasoning about angle divisibility is why exactly three regular polygons admit a regular tiling.
