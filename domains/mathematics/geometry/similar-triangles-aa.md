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

## Explainer

Similarity captures the idea of "same shape, different size." Think of a photograph and an enlargement of it: every angle in the enlarged photo matches the original, but all the lengths are scaled up by the same factor. Two triangles are **similar** (written ΔABC ~ ΔDEF) when corresponding angles are equal and corresponding sides are proportional. The **AA Similarity Postulate** says you only need to verify two pairs of angles — the third follows automatically from the angle sum theorem, which you've already studied: since the angles in any triangle add to 180°, matching two forces the third to match as well.

Why does matching angles guarantee proportional sides? Intuitively, fixing the angles of a triangle locks in its shape. You could scale it up or down, but you can't distort it — changing a side length without changing an angle would violate the law of sines. More concretely, if you know two angles are equal, you can place one triangle inside the other (parallel to the base) and show by properties of parallel lines that corresponding sides are in ratio. The AA postulate is what makes trigonometry work: the ratios sin, cos, and tan are defined for angles, not specific triangles, precisely because all right triangles with the same acute angle are similar.

The practical skill is setting up the **proportion** correctly. When ΔABC ~ ΔDEF, the correspondence of vertices matters: A corresponds to D, B to E, C to F. So the correct proportion pairs corresponding sides: AB/DE = BC/EF = AC/DF. All three ratios equal the same scale factor k. A common setup in geometry problems involves two triangles sharing a vertex angle and cut by a line parallel to one side — this creates two angles that are the same in both triangles (the shared vertex angle and equal corresponding angles from the parallel cut), so AA applies. From there, you set up a proportion and solve for an unknown length.

Similar triangles appear throughout geometry as a tool for measuring things indirectly. The classic application is shadow problems: a tree and a nearby stick both cast shadows; if you measure the stick's height and shadow and the tree's shadow, the two triangles formed by sun rays and objects are similar by AA, letting you calculate the tree's height without climbing it. This indirect-measurement power is why AA similarity is the foundation for the trigonometry you'll study next.
