---
id: proportions-in-similar-triangles
title: Proportions in Similar Triangles
domain: mathematics
course: geometry
prerequisites:
  - id: similar-triangles-aa
    type: hard
  - id: similar-triangles-sss-sas
    type: soft
  - id: proportions
    type: hard
builds-toward:
  - right-triangle-trigonometry-intro
  - coordinate-geometry-proofs
tags: [similarity, proportions, scale-factor, applications]
stage: abstract-reasoning
status: validated
---

# Proportions in Similar Triangles

## Core Idea
When two triangles are similar, all corresponding sides share the same scale factor. This allows us to find unknown side lengths by setting up and solving proportions. Key results include the Side-Splitter Theorem (a line parallel to one side of a triangle divides the other two sides proportionally) and the Triangle Angle Bisector Theorem (an angle bisector divides the opposite side in the ratio of the adjacent sides).

## How It's Best Learned
Practice setting up proportions carefully: match corresponding sides by identifying which vertex maps to which. Introduce the scale factor as the common ratio. Apply to real-world problems (shadow problems, map scales, indirect measurement). Prove the Side-Splitter Theorem using AA similarity.

## Common Misconceptions
- Setting up proportions with non-corresponding sides, leading to incorrect ratios.
- Confusing the scale factor with the actual side length.
- Forgetting that all three ratios must be equal, not just two.

## Explainer

You've already established from AA similarity (and SSS/SAS) that two triangles are similar when their angles match or their sides are proportional. Now you're extracting the practical payoff: if two triangles are similar, you can use the **scale factor** to find any unknown side. The scale factor k is the constant ratio between corresponding sides — if triangle ABC ~ triangle DEF, then DE/AB = EF/BC = FD/CA = k. This single number k encodes how the larger (or smaller) triangle stretches the original.

Setting up a proportion correctly requires matching corresponding vertices, not just matching sides by position in a diagram. The safest approach: use the similarity statement itself as a guide. If ΔABC ~ ΔDEF, then A↔D, B↔E, C↔F. So the proportion is AB/DE = BC/EF = AC/DF. A common error is pairing sides that look parallel or similarly placed in a figure but don't actually correspond — always trace back to the angle correspondence.

The **Side-Splitter Theorem** extends proportional reasoning into a triangle. If a line is parallel to one side of a triangle and intersects the other two sides, it divides those sides proportionally. Say line segment DE is parallel to BC in triangle ABC, with D on AB and E on AC. Then AD/DB = AE/EC. The proof uses AA similarity: triangle ADE ~ triangle ABC because the parallel line creates equal corresponding angles. Once you see DE as cutting out a smaller similar triangle from the top, the proportion falls out from the scale factor applied to each sub-segment.

The **Angle Bisector Theorem** is a different application of the same proportional logic: the bisector of an angle in a triangle divides the opposite side in the ratio of the two adjacent sides. If the bisector from A meets BC at point D, then BD/DC = AB/AC. This might seem surprising — it connects a ratio of segments to a ratio of sides that don't share an endpoint with those segments. The proof uses auxiliary parallel lines to create similar triangles, then applies the proportionality. Both theorems are powerful tools for indirect measurement: you don't need to physically measure something if you can identify a similar triangle (via shadows, mirrors, or scaled drawings) and solve the proportion instead.
