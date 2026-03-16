---
id: triangle-congruence-sas
title: "Triangle Congruence: SAS"
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sss
    type: soft
  - id: angle-basics-and-classification
    type: hard
builds-toward:
  - cpctc
  - isosceles-triangle-theorem
  - parallelogram-properties
tags: [congruence, triangles, SAS, proof]
stage: abstract-reasoning
status: validated
---

# Triangle Congruence: SAS

## Core Idea
The Side-Angle-Side (SAS) Congruence Postulate states that if two sides and the included angle of one triangle are congruent to two sides and the included angle of another, the triangles are congruent. The angle must be between (included by) the two sides. SAS is often the most commonly used congruence criterion in proofs.

## How It's Best Learned
Demonstrate with compass and straightedge: draw two sides of fixed length with a fixed angle between them, and the third side is forced. Contrast with SSA (which does NOT guarantee congruence) to emphasize the importance of the included angle. Practice two-column proofs using SAS.

## Common Misconceptions
- Forgetting the "included" requirement and trying to use SSA (Side-Side-Angle), which is not a valid congruence criterion.
- Marking the wrong angle as included when it is actually adjacent to only one of the two sides.
- Confusing SAS congruence with SAS similarity.

## Explainer

You already know **SSS** — if all three sides of one triangle match all three sides of another, the triangles are congruent. **SAS** (Side-Angle-Side) gets you congruence from less information: two sides and the **included angle** between them. Think of it physically: fix two sticks of given lengths and pin them together at a specific angle. The position of the far endpoints is now determined — you have no freedom in where the third vertex lands, and the third side is forced to a unique length. Two sides and their included angle completely determine the shape of the triangle.

Why does the angle have to be *included*? Consider what happens with SSA — two sides and a non-included angle. Given two sides of lengths 5 and 8 and an angle of 30° at the end of the side of length 5, two different triangles may satisfy those conditions. The angle isn't "sandwiched" between the two sides, so it doesn't constrain the triangle to a unique shape. This is the **ambiguous case**, and it's why SSA is not a valid congruence criterion. The SAS postulate works precisely because the included angle controls how the two sides meet, leaving no geometric ambiguity.

In two-column proofs, SAS plays out in two stages. First, establish that two pairs of sides are congruent — often from given information, a midpoint definition, or the **reflexive property** (a side shared by both triangles is congruent to itself). Then establish the included angle — often through vertical angles, an angle bisector, or given congruent angles. The conclusion "triangles congruent by SAS" then opens the door to **CPCTC**: Corresponding Parts of Congruent Triangles are Congruent. CPCTC lets you conclude that any remaining parts — the third side, the other angles — are also congruent. Most geometric proofs involving midpoints, bisectors, and parallel lines follow this pattern: prove congruence via SAS, then use CPCTC to extract the part you actually need.

A reliable way to identify the included angle: it is the angle *at the vertex where the two sides meet*. In triangle ABC, sides AB and BC share vertex B, so the included angle is ∠B. Sides AB and CA share vertex A, so their included angle is ∠A. If you name two sides and the angle is not at their shared vertex, you have SSA — not SAS — and the proof is invalid. Marking the congruent parts on a diagram before writing any steps will almost always reveal whether the angle is truly included.
