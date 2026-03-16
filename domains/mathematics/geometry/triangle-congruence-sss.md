---
id: triangle-congruence-sss
title: "Triangle Congruence: SSS"
domain: mathematics
course: geometry
prerequisites:
  - id: segment-and-distance
    type: hard
  - id: triangle-angle-sum
    type: soft
builds-toward:
  - cpctc
  - triangle-congruence-sas
tags: [congruence, triangles, SSS, proof]
stage: abstract-reasoning
status: validated
---

# Triangle Congruence: SSS

## Core Idea
The Side-Side-Side (SSS) Congruence Postulate states that if three sides of one triangle are congruent to three sides of another triangle, then the two triangles are congruent. This means all corresponding parts (both sides and angles) are congruent. SSS is intuitive: three fixed side lengths can form only one triangle shape (up to reflection). It is one of the primary tools for proving triangles congruent.

## How It's Best Learned
Use physical manipulatives or dynamic geometry software to show that fixing three side lengths determines a unique triangle. Present the postulate formally, then practice identifying SSS in diagrams by marking congruent sides (tick marks). Write two-column or paragraph proofs using SSS.

## Common Misconceptions
- Thinking that SSS also requires an angle to be known; it does not.
- Confusing SSS with AAA, which does NOT prove congruence (only similarity).
- Failing to identify shared sides in overlapping triangles (reflexive property).

## Explainer

Triangles are rigid. Unlike a square, which can be pushed into a parallelogram while keeping side lengths fixed, a triangle with fixed side lengths has only one possible shape. This rigidity — three side lengths uniquely determine a triangle — is the geometric intuition behind the **Side-Side-Side (SSS) congruence postulate**. If all three sides of one triangle match all three sides of another, the triangles are not merely similar; they are identical in shape and size and can be placed exactly on top of each other.

You can verify this physically. Fix three rigid sticks of lengths 3, 4, and 5 cm and try to form a different triangle with them. You cannot — there is only one triangle those lengths can form (plus its mirror image, which is congruent). From your prerequisite on segment and distance, you know what it means for segments to be equal in length; SSS simply requires all three corresponding pairs to match. The triangle's angles are fully locked in by the sides — you get the angles for free, even though you never measured them.

In a proof, establishing SSS means finding three pairs of congruent sides and labeling the correspondence clearly. One pair is often **given** explicitly. A second pair may come from the problem context — equal radii, equal distances from a fixed point, or a symmetric construction. The third is frequently a **shared side**: two triangles that share a common segment automatically have one pair of equal sides by the reflexive property (a segment is congruent to itself). This shared-side observation is one of the most commonly overlooked tools. Whenever you see two triangles that overlap or share an edge, ask whether that shared edge can serve as the third pair.

Once SSS is established, you can invoke CPCTC to conclude that corresponding *angles* are congruent — converting the side information into angle information. Note carefully what SSS cannot do: knowing three equal *angles* (AAA) does not prove congruence, only similarity. Triangles can share all three angle measures while having different sizes. SSS requires all three *side lengths* to match, not just shapes. This distinction between congruence (same shape and size) and similarity (same shape only) is one of the central themes the next topics will develop further.
