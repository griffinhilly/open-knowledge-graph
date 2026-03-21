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

## Questions

```yaml
- question: "In triangle ABC, AB = 5, BC = 8, and angle A = 40°. Can you conclude that any triangle with AB = 5, BC = 8, and angle A = 40° is congruent to triangle ABC?"
  type: multiple-choice
  options:
    - "Yes — two sides and an angle are enough to determine a unique triangle"
    - "No — angle A is not the included angle between sides AB and BC, so this is SSA, which does not guarantee congruence"
    - "Yes — SAS applies because we have two sides and one angle"
    - "No — you would need all three sides to prove congruence"
  answer: 1
  explanation: "This is the classic SSA trap. Angle A is adjacent to side AB, but it is not between AB and BC — the included angle between those two sides would be angle B (at the vertex where AB and BC meet). With the angle at the far end of one of the sides rather than between them, two different triangles can satisfy these conditions (the ambiguous case). SAS requires the angle to be sandwiched between the two known sides. The arrangement here is SSA — not a valid congruence criterion."

- question: "In triangle XYZ, sides XY and YZ are congruent to the corresponding sides in triangle PQR, and angle Y = angle Q. Which congruence criterion justifies concluding the triangles are congruent?"
  type: multiple-choice
  options:
    - "SSS — because we know two sides and can infer the third"
    - "SSA — because we have two sides and the angle at Q"
    - "SAS — because angle Y is the included angle between sides XY and YZ, and angle Q is the included angle between the corresponding sides"
    - "No valid criterion applies — we need more information"
  answer: 2
  explanation: "Angle Y sits at the vertex where sides XY and YZ meet, making it the included angle between those two sides. The same is true of angle Q in triangle PQR. Two sides and the included (sandwiched) angle satisfy the SAS postulate, which guarantees triangle congruence. If the known angle were at a different vertex — not between the two known sides — we would have SSA, which is not a valid congruence criterion. Identifying the included angle correctly is the critical step."

- question: "If two sides and the included angle of one triangle are congruent to two sides and the included angle of another triangle, the triangles are congruent."
  type: true-false
  answer: true
  explanation: "This is the SAS (Side-Angle-Side) Congruence Postulate, and it is valid. The key is that the angle must be included — sandwiched between the two known sides. When you fix two sides of specified lengths and the angle between them, the triangle's shape is completely determined: the third vertex has no freedom to move, forcing the third side to a unique length. This geometric rigidity is why SAS works."

- question: "SSA (Side-Side-Angle) is a valid congruence criterion when the given angle is acute."
  type: true-false
  answer: false
  explanation: "SSA is not a valid congruence criterion regardless of whether the angle is acute, right, or obtuse (with one exception: a right angle with the right angle as the given angle, which is covered by HL). The 'ambiguous case' occurs precisely with acute angles — given two sides and a non-included acute angle, two different triangles may satisfy the conditions. The angle must be included (between the two known sides) to eliminate this ambiguity. No qualification about angle type makes SSA valid in general."

- question: "Why does the 'included' requirement matter in SAS? What goes wrong geometrically when you use SSA instead?"
  type: short-answer
  answer: "The included angle controls how the two known sides meet each other, leaving no freedom for the third vertex to vary. When the angle is between the two sides, fixing both sides and the angle between them uniquely determines the triangle. In SSA, the angle is at the far end of one side rather than between the two sides — so the opposite end of the shorter side can swing to two different positions that both satisfy the given measurements. This 'ambiguous case' means SSA does not guarantee a unique triangle, making it invalid as a congruence criterion."
  explanation: "Visualize it physically: pin two sticks together at a specific angle (SAS). The third vertex is locked in place. Now instead, hold two sticks of fixed length with a fixed angle at the far end of one stick — the other end of the shorter stick can arc to two positions that satisfy the constraint. That freedom is exactly what makes SSA fail. The SAS postulate works because the included angle eliminates all geometric ambiguity."
```

## Explainer

You already know **SSS** — if all three sides of one triangle match all three sides of another, the triangles are congruent. **SAS** (Side-Angle-Side) gets you congruence from less information: two sides and the **included angle** between them. Think of it physically: fix two sticks of given lengths and pin them together at a specific angle. The position of the far endpoints is now determined — you have no freedom in where the third vertex lands, and the third side is forced to a unique length. Two sides and their included angle completely determine the shape of the triangle.

Why does the angle have to be *included*? Consider what happens with SSA — two sides and a non-included angle. Given two sides of lengths 5 and 8 and an angle of 30° at the end of the side of length 5, two different triangles may satisfy those conditions. The angle isn't "sandwiched" between the two sides, so it doesn't constrain the triangle to a unique shape. This is the **ambiguous case**, and it's why SSA is not a valid congruence criterion. The SAS postulate works precisely because the included angle controls how the two sides meet, leaving no geometric ambiguity.

In two-column proofs, SAS plays out in two stages. First, establish that two pairs of sides are congruent — often from given information, a midpoint definition, or the **reflexive property** (a side shared by both triangles is congruent to itself). Then establish the included angle — often through vertical angles, an angle bisector, or given congruent angles. The conclusion "triangles congruent by SAS" then opens the door to **CPCTC**: Corresponding Parts of Congruent Triangles are Congruent. CPCTC lets you conclude that any remaining parts — the third side, the other angles — are also congruent. Most geometric proofs involving midpoints, bisectors, and parallel lines follow this pattern: prove congruence via SAS, then use CPCTC to extract the part you actually need.

A reliable way to identify the included angle: it is the angle *at the vertex where the two sides meet*. In triangle ABC, sides AB and BC share vertex B, so the included angle is ∠B. Sides AB and CA share vertex A, so their included angle is ∠A. If you name two sides and the angle is not at their shared vertex, you have SSA — not SAS — and the proof is invalid. Marking the congruent parts on a diagram before writing any steps will almost always reveal whether the angle is truly included.
