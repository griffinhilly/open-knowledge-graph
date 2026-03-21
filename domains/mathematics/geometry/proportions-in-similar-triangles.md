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

## Questions

```yaml
- question: "ΔABC ~ ΔPQR, with AB = 6, BC = 8, and PQ = 9. A student sets up the proportion 6/9 = 8/QR to find QR. What is the student doing correctly or incorrectly?"
  type: multiple-choice
  options:
    - "This proportion is incorrect — the student should use AB/BC = PQ/QR (ratios within each triangle)"
    - "This proportion is correct — AB corresponds to PQ and BC corresponds to QR, giving QR = 12"
    - "This proportion is incorrect — the student should use AB/PQ = BC/QR but with the triangles switched"
    - "This proportion cannot be solved without knowing a third side"
  answer: 1
  explanation: "In ΔABC ~ ΔPQR, A↔P, B↔Q, C↔R, so AB corresponds to PQ and BC corresponds to QR. The proportion AB/PQ = BC/QR gives 6/9 = 8/QR, so QR = 12. This is the correct cross-triangle proportion matching corresponding sides. Option A describes ratios within a single triangle, which also works but is a different setup."

- question: "In triangle ABC, segment DE is parallel to BC with D on AB and E on AC. If AD = 4, DB = 6, and AE = 5, what is EC?"
  type: multiple-choice
  options:
    - "EC = 3"
    - "EC = 7.5"
    - "EC = 5"
    - "EC = 4"
  answer: 1
  explanation: "By the Side-Splitter Theorem, a line parallel to one side of a triangle divides the other two sides proportionally: AD/DB = AE/EC. So 4/6 = 5/EC, giving EC = 5 × 6/4 = 7.5. The parallel line creates the same ratio on both sides of the triangle."

- question: "If ΔABC ~ ΔDEF and AB/DE = BC/EF, it is possible that AC/DF is a different ratio."
  type: true-false
  answer: false
  explanation: "When two triangles are similar, ALL pairs of corresponding sides share the same scale factor k. If AB/DE = BC/EF = k, then AC/DF must also equal k. The scale factor is a single constant that relates every pair of corresponding sides simultaneously. Two of the three ratios being equal forces the third to be equal as well — this is a direct consequence of similarity."

- question: "When setting up proportions for similar triangles, you should identify corresponding sides using the similarity statement's vertex correspondence rather than matching sides that look similar in position in the diagram."
  type: true-false
  answer: true
  explanation: "Diagrams can be drawn in many orientations — a side that appears 'on the left' in one triangle may correspond to the side 'on the right' in the other. The similarity statement (e.g., ΔABC ~ ΔDEF) encodes the exact correspondence: A↔D, B↔E, C↔F, giving AB↔DE, BC↔EF, AC↔DF. Using the statement prevents mismatches that arise from reading visual position alone."

- question: "Explain why all three pairs of corresponding sides must share the same scale factor when two triangles are similar, rather than just requiring two pairs to match."
  type: short-answer
  answer: "Similarity means one triangle is a uniform scaling of the other — every distance is multiplied by the same scale factor k. This is not a property that can hold for two sides without holding for the third, because all three sides are transformed by the same multiplicative factor simultaneously. If two pairs of sides have the same ratio but the third does not, the triangles have different shapes — they are not similar."
  explanation: "In practice, once you establish similarity (via AA, SSS similarity, or SAS similarity), you can use any one pair of corresponding sides to find k, then apply that k to all other pairs. The three equal ratios are not independent facts but three expressions of a single underlying transformation — the scaling that maps one triangle onto the other."
```

## Explainer

You've already established from AA similarity (and SSS/SAS) that two triangles are similar when their angles match or their sides are proportional. Now you're extracting the practical payoff: if two triangles are similar, you can use the **scale factor** to find any unknown side. The scale factor k is the constant ratio between corresponding sides — if triangle ABC ~ triangle DEF, then DE/AB = EF/BC = FD/CA = k. This single number k encodes how the larger (or smaller) triangle stretches the original.

Setting up a proportion correctly requires matching corresponding vertices, not just matching sides by position in a diagram. The safest approach: use the similarity statement itself as a guide. If ΔABC ~ ΔDEF, then A↔D, B↔E, C↔F. So the proportion is AB/DE = BC/EF = AC/DF. A common error is pairing sides that look parallel or similarly placed in a figure but don't actually correspond — always trace back to the angle correspondence.

The **Side-Splitter Theorem** extends proportional reasoning into a triangle. If a line is parallel to one side of a triangle and intersects the other two sides, it divides those sides proportionally. Say line segment DE is parallel to BC in triangle ABC, with D on AB and E on AC. Then AD/DB = AE/EC. The proof uses AA similarity: triangle ADE ~ triangle ABC because the parallel line creates equal corresponding angles. Once you see DE as cutting out a smaller similar triangle from the top, the proportion falls out from the scale factor applied to each sub-segment.

The **Angle Bisector Theorem** is a different application of the same proportional logic: the bisector of an angle in a triangle divides the opposite side in the ratio of the two adjacent sides. If the bisector from A meets BC at point D, then BD/DC = AB/AC. This might seem surprising — it connects a ratio of segments to a ratio of sides that don't share an endpoint with those segments. The proof uses auxiliary parallel lines to create similar triangles, then applies the proportionality. Both theorems are powerful tools for indirect measurement: you don't need to physically measure something if you can identify a similar triangle (via shadows, mirrors, or scaled drawings) and solve the proportion instead.
