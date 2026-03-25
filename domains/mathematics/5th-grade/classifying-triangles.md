---
id: classifying-triangles
title: Classifying Triangles
domain: mathematics
course: 5th-grade
prerequisites:
- id: classifying-2d-shapes
  type: hard
- id: measuring-angles
  type: soft
- id: classifying-quadrilaterals
  type: soft
builds-toward: []
tags:
- geometry
- triangles
- classification
- angles
stage: concrete-operations
status: validated
---
# Classifying Triangles

## Core Idea
Triangles are classified in two independent ways: by their angles and by their sides. By angles: acute (all angles < 90 degrees), right (one angle = 90 degrees), or obtuse (one angle > 90 degrees). By sides: equilateral (all sides equal), isosceles (at least two sides equal), or scalene (no sides equal). These classifications can combine: a triangle can be a right isosceles triangle or an obtuse scalene triangle, for example. A key fact is that the three angles of any triangle always sum to 180 degrees, which students begin to explore at this level.

## How It's Best Learned
Have students measure sides and angles of many triangles, then classify each using both systems. Use sorting activities where triangles are grouped by angle type, then re-grouped by side type. Explore the angle sum property by tearing off corners and arranging them to form a straight line (180 degrees). Draw triangles that meet specific dual classifications ("draw a right scalene triangle").

## Common Misconceptions
- Thinking equilateral and isosceles are mutually exclusive (an equilateral triangle is also isosceles, since it has at least two equal sides).
- Believing a triangle can have two obtuse angles or two right angles (impossible, since angles must sum to 180 degrees).
- Identifying triangles by appearance when rotated or scaled rather than by measured properties.

## Questions

```yaml
- question: "A student says: 'This triangle is equilateral, so it definitely can't also be isosceles — they're different categories.' Are they right?"
  type: multiple-choice
  options:
    - "Yes — equilateral and isosceles describe different properties and cannot apply to the same triangle"
    - "No — an equilateral triangle has all three sides equal, which satisfies the definition of isosceles ('at least two sides equal'), so every equilateral triangle is also isosceles"
    - "Yes — equilateral means all angles are 60°, while isosceles means two sides are equal, so the terms describe unrelated things"
    - "No — but only special equilateral triangles with certain angle measures count as isosceles"
  answer: 1
  explanation: "The student has the wrong mental model. The isosceles definition is 'at least two equal sides' — not 'exactly two equal sides.' An equilateral triangle has three equal sides, which certainly satisfies 'at least two.' So every equilateral triangle is automatically isosceles. The side-classification categories are nested, not exclusive: scalene ⊂ no equal sides, isosceles ⊂ at least two equal sides (which includes equilateral), equilateral ⊂ all three equal."

- question: "Which combination of triangle classifications is IMPOSSIBLE?"
  type: multiple-choice
  options:
    - "Acute and equilateral"
    - "Right and isosceles"
    - "Obtuse and scalene"
    - "Right and obtuse"
  answer: 3
  explanation: "A right angle is exactly 90° and an obtuse angle is more than 90°. A triangle can have at most one of each, because the three angles must sum to exactly 180°. If a triangle had one right angle (90°) and one obtuse angle (more than 90°), the two angles alone would exceed 180°, leaving nothing for the third angle. The angle sum constraint makes right-obtuse impossible. The other combinations are all valid: an equilateral triangle has three 60° acute angles; a right isosceles triangle has a 90° angle and two equal 45° angles; an obtuse scalene is common."

- question: "A triangle can have two obtuse angles as long as each one is only slightly greater than 90°."
  type: true-false
  answer: false
  explanation: "Even the smallest possible obtuse angle is just over 90°. Two angles each slightly over 90° would sum to just over 180° — but the three angles of a triangle must sum to exactly 180°, leaving zero or less for the third angle. This is impossible. The angle sum property is a hard constraint: you can have at most one obtuse (or right) angle in any triangle."

- question: "Every triangle has both an angle classification (acute, right, or obtuse) and a side classification (equilateral, isosceles, or scalene), and these two labels are independent of each other."
  type: true-false
  answer: true
  explanation: "The two classification systems describe different properties and can be combined freely (within the constraints of what is geometrically possible). A triangle can be right isosceles, acute scalene, obtuse isosceles, and so on. To fully describe a triangle, you need both labels. The systems are independent in the sense that knowing a triangle is, say, isosceles tells you nothing directly about whether it is acute, right, or obtuse — you need to measure the angles separately."

- question: "Why is it impossible for a triangle to have two right angles? Use the angle sum property in your explanation."
  type: short-answer
  answer: "The three angles of any triangle must sum to exactly 180°. A right angle is 90°. If a triangle had two right angles, those two alone would sum to 90° + 90° = 180°, using up the entire allowed sum. That would leave 0° for the third angle — which is not a real angle, and a triangle requires three distinct angles. Therefore, a triangle can have at most one right angle."
  explanation: "This is the angle sum property doing real logical work: it is not just a fact to memorize but a constraint that rules out certain combinations. The same reasoning extends to obtuse angles (each more than 90°): two obtuse angles already exceed 180°, so a triangle can also have at most one obtuse angle. Both the right and obtuse categories are limited to one per triangle for the same reason."
```

## Explainer

You know that triangles are three-sided polygons, and you've classified 2D shapes by their properties. Triangles get their own two-part classification system because they vary so much — a long skinny triangle looks almost nothing like a short wide one, yet both are triangles. To describe a triangle precisely, you need to answer two independent questions: what do its **angles** look like, and what do its **sides** look like?

Start with angle classification. You already know the angle types: acute (less than 90°), right (exactly 90°), and obtuse (greater than 90°). A triangle takes the name of its largest angle. If all three angles are acute, it's an **acute triangle**. If one angle is exactly 90°, it's a **right triangle** (the other two must be acute — they have to share the remaining 90°). If one angle is obtuse, it's an **obtuse triangle**. Here a key constraint kicks in: the three angles of any triangle always sum to exactly 180°. This means you can never have two right angles (90 + 90 = 180, with nothing left for the third), and never two obtuse angles (each would be more than 90°, already exceeding 180° together). The angle sum property isn't just a fact to memorize — it's a logical consequence of how triangles close.

Now classify by sides. **Equilateral** triangles have all three sides equal — and as a consequence, all three angles are also equal (each is 60°, since 180° ÷ 3 = 60°). **Isosceles** triangles have at least two equal sides; their two base angles are also equal. **Scalene** triangles have no equal sides and no equal angles. Notice that an equilateral triangle is also isosceles — it satisfies "at least two equal sides." These categories are not mutually exclusive; they nest.

The power of the two-part system is that you can combine them: a right isosceles triangle has one 90° angle and two equal legs. An obtuse scalene triangle has one obtuse angle and no equal sides. When you encounter a triangle and need to classify it fully, measure (or examine) the sides for equality, then examine the angles. Properties — not appearance — are what matter. A triangle flipped upside down or shrunk to half size is still the same type. Measuring builds the habit of trusting numbers over visual intuition.
