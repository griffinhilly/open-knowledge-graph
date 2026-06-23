---
id: similar-triangles-aa
title: 'Similar Triangles: AA Similarity'
domain: mathematics
course: geometry
prerequisites:
- id: triangle-angle-sum
  type: hard
- id: proportions
  type: hard
- id: triangle-inequality
  type: soft
- id: solving-proportions
  type: soft
builds-toward:
- similar-triangles-sss-sas
- proportions-in-similar-triangles
- right-triangle-trigonometry-intro
tags:
- similarity
- triangles
- AA
- proportionality
stage: abstract-reasoning
status: validated
---
# Similar Triangles: AA Similarity

## Core Idea
Two triangles are similar if their corresponding angles are congruent and corresponding sides are proportional. The AA (Angle-Angle) Similarity Postulate states that if two angles of one triangle are congruent to two angles of another, the triangles are similar (the third angle is automatically congruent by the angle sum theorem). Similar triangles have the same shape but not necessarily the same size. AA is the most commonly used similarity criterion.

## How It's Best Learned
Start with the intuition that same angles mean same shape. Use dynamic geometry software to show that changing size while preserving angles preserves proportionality. Practice identifying AA in diagrams, especially in configurations with parallel lines cutting transversals. Set up and solve proportions from similar triangles.

## Common Misconceptions
- Confusing similarity with congruence (similar triangles have proportional sides, not necessarily equal sides).
- Thinking you need all three angles to prove similarity (two suffice because of the angle sum theorem).
- Setting up proportions with non-corresponding sides.

## Questions

```yaml
- question: "Triangle ABC has angles 40°, 60°, and 80°. Triangle DEF has angles 40° and 60° (the third is unknown). What can you conclude?"
  type: multiple-choice
  options:
    - "The triangles are congruent because all three angles will be equal"
    - "The triangles are similar, and their corresponding sides are equal"
    - "The triangles are similar, and their corresponding sides are proportional"
    - "You need to know the side lengths before drawing any conclusion"
  answer: 2
  explanation: "Two matching angle pairs (40° and 60°) are sufficient for AA similarity — the third angle of DEF must be 80° by the angle sum theorem. Similar triangles have proportional sides, not necessarily equal sides. 'Congruent' would mean identical in size; 'similar' means same shape but possibly different sizes. The side lengths tell you the scale factor but don't determine whether the triangles are similar."

- question: "In the diagram, triangle PQR ~ triangle STU with PQ = 6, QR = 8, and ST = 9. What is TU?"
  type: multiple-choice
  options:
    - "11 — add the difference of the first pair (9 − 6 = 3) to QR"
    - "12 — the scale factor is 9/6 = 3/2, and 8 × (3/2) = 12"
    - "6 — TU corresponds to PQ, not QR"
    - "Cannot determine without knowing the angles"
  answer: 1
  explanation: "The scale factor from △PQR to △STU is ST/PQ = 9/6 = 3/2. Since QR corresponds to TU (B↔T, R↔U from the similarity statement), TU = QR × (3/2) = 8 × 3/2 = 12. The vertex correspondence in the similarity statement △PQR ~ △STU tells you which sides pair together: P↔S, Q↔T, R↔U. Answer A is the classic error of adding differences rather than multiplying by a scale factor."

- question: "To prove two triangles are similar using the AA postulate, you is expected to verify that most three pairs of corresponding angles are congruent."
  type: true-false
  answer: false
  explanation: "Only two pairs of angles are needed. Once two angles of one triangle match two angles of another, the third angles are automatically equal — because the angles of any triangle must sum to 180°. If angle A = angle D and angle B = angle E, then angle C = 180° − A − B = 180° − D − E = angle F. The AA postulate is powerful precisely because it reduces the verification burden from three pairs to two."

- question: "If two triangles are similar, then most corresponding sides are equal in length."
  type: true-false
  answer: false
  explanation: "Similar triangles have proportional sides, not equal sides. Equal sides would mean congruent triangles — same shape AND same size. Similarity only requires same shape, which means the ratios of corresponding sides are equal (they share a common scale factor k), but the sides themselves can be any length. A 3-4-5 right triangle and a 6-8-10 right triangle are similar but not congruent."

- question: "Why does knowing only two pairs of matching angles guarantee that two triangles are similar — why isn't a third angle check required?"
  type: short-answer
  answer: "Because the angles in any triangle must sum to 180°. If two angles of triangle A match two angles of triangle B, the third angle of each triangle is completely determined: it equals 180° minus the sum of the other two. Since the first two pairs already match, the third pair must also match. The angle sum theorem makes the third check redundant."
  explanation: "This is the key insight behind AA: the angle sum theorem acts as a 'free' third constraint. Because triangles are closed under the 180° rule, you never need to independently verify the third angle — it's logically forced by the first two. This is also why there is no 'A' (single angle) similarity shortcut: one angle is not enough to determine shape, since many different triangles share a single angle."
```

## Explainer

Similarity captures the idea of "same shape, different size." Think of a photograph and an enlargement of it: every angle in the enlarged photo matches the original, but all the lengths are scaled up by the same factor. Two triangles are **similar** (written ΔABC ~ ΔDEF) when corresponding angles are equal and corresponding sides are proportional. The **AA Similarity Postulate** says you only need to verify two pairs of angles — the third follows automatically from the angle sum theorem, which you've already studied: since the angles in any triangle add to 180°, matching two forces the third to match as well.

Why does matching angles guarantee proportional sides? Intuitively, fixing the angles of a triangle locks in its shape. You could scale it up or down, but you can't distort it — changing a side length without changing an angle would violate the law of sines. More concretely, if you know two angles are equal, you can place one triangle inside the other (parallel to the base) and show by properties of parallel lines that corresponding sides are in ratio. The AA postulate is what makes trigonometry work: the ratios sin, cos, and tan are defined for angles, not specific triangles, precisely because all right triangles with the same acute angle are similar.

The practical skill is setting up the **proportion** correctly. When ΔABC ~ ΔDEF, the correspondence of vertices matters: A corresponds to D, B to E, C to F. So the correct proportion pairs corresponding sides: AB/DE = BC/EF = AC/DF. All three ratios equal the same scale factor k. A common setup in geometry problems involves two triangles sharing a vertex angle and cut by a line parallel to one side — this creates two angles that are the same in both triangles (the shared vertex angle and equal corresponding angles from the parallel cut), so AA applies. From there, you set up a proportion and solve for an unknown length.

Similar triangles appear throughout geometry as a tool for measuring things indirectly. The classic application is shadow problems: a tree and a nearby stick both cast shadows; if you measure the stick's height and shadow and the tree's shadow, the two triangles formed by sun rays and objects are similar by AA, letting you calculate the tree's height without climbing it. This indirect-measurement power is why AA similarity is the foundation for the trigonometry you'll study next.
