---
id: triangle-congruence-asa-aas
title: "Triangle Congruence: ASA and AAS"
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sas
    type: soft
  - id: triangle-angle-sum
    type: hard
builds-toward:
  - cpctc
  - isosceles-triangle-theorem
tags: [congruence, triangles, ASA, AAS, proof]
stage: abstract-reasoning
status: validated
---

# Triangle Congruence: ASA and AAS

## Core Idea
ASA (Angle-Side-Angle) states that if two angles and the included side of one triangle are congruent to two angles and the included side of another, the triangles are congruent. AAS (Angle-Angle-Side) states that if two angles and a non-included side are congruent, the triangles are congruent. AAS follows from ASA because the third angle is determined by the Triangle Angle Sum Theorem. Together with SSS and SAS, these give four valid congruence criteria.

## How It's Best Learned
Show how fixing two angles and a side determines the triangle uniquely. Prove AAS from ASA using the angle sum theorem. Contrast with invalid criteria (AAA, SSA). Give proof exercises that require choosing the right criterion, forcing students to analyze what information is available.

## Common Misconceptions
- Confusing ASA (side is between the angles) with AAS (side is not between the angles); both are valid but distinct.
- Thinking AAA is a congruence criterion (it only proves similarity).
- Not recognizing when the angle sum theorem lets you derive a third angle to convert AAS to ASA.

## Questions

```yaml
- question: "Two triangles each have angles of 45° and 70°, and a corresponding non-included side of 5 cm. Which congruence criterion establishes they are congruent?"
  type: multiple-choice
  options:
    - "ASA, because two angles are known"
    - "AAS, because two angles and a non-included side are congruent"
    - "AAA, because all three angles can be determined"
    - "SSA, because a side and two angle measurements are given"
  answer: 1
  explanation: "This is AAS: two angles and a side that is not between them. AAA is wrong because it proves only similarity, not congruence — triangles with the same angles can have different sizes. SSA is wrong because it's two sides and a non-included angle, which is not the configuration here. AAS works because the Triangle Angle Sum Theorem gives you the third angle, reducing the situation to ASA."

- question: "AAS is a valid congruence criterion even though the known side is not between the two known angles. Why?"
  type: multiple-choice
  options:
    - "Because the non-included side determines scale more reliably than an included side"
    - "Because the Triangle Angle Sum Theorem gives you the third angle for free, so you effectively have all three angles plus one side — which fully determines the triangle"
    - "Because any two triangles with two matching angles are automatically congruent"
    - "Because AAS is actually just another name for ASA when the triangle is obtuse"
  answer: 1
  explanation: "The key is the angle sum theorem: if you know two angles, you know the third (180° − the other two). Now you have all three angles and one side, which is enough to determine a unique triangle. In effect, AAS secretly reduces to ASA — identify which two angles the known side falls between once you've computed the third angle. The common mistake is thinking the position of the known side makes AAS weaker; it doesn't, because angles constrain direction, and fixing all directions plus any one side locks down scale."

- question: "Two triangles with all three pairs of corresponding angles equal are congruent."
  type: true-false
  answer: false
  explanation: "AAA (Angle-Angle-Angle) proves that two triangles are similar — same shape — but not necessarily congruent. A small equilateral triangle and a large equilateral triangle both have three 60° angles but are clearly different sizes. Congruence requires fixing both shape and size; fixing all angles fixes shape but leaves scale free. You need at least one side to pin down the size."

- question: "Whenever you have AAS, you can invoke the Triangle Angle Sum Theorem to derive the third angle and then reinterpret the configuration as ASA."
  type: true-false
  answer: true
  explanation: "This is exactly why AAS works. The three angles of any triangle sum to 180°, so knowing two angles determines the third. Once you have all three angles, the known side sits between two specific angles — whichever pair it falls between gives you ASA. This derivation is not just a proof technique; it is the conceptual reason AAS is a valid criterion."

- question: "Explain why ASA and AAS succeed as congruence criteria but AAA does not, and why SSA also fails."
  type: short-answer
  answer: "ASA and AAS both fix the triangle's shape and scale completely. With two angles determined, the shape is set (all three angles determine a unique shape class, since the third is forced by the angle sum). One side then fixes the scale — there is no room left for the triangle to be larger or smaller. AAA fixes shape but not scale, so infinitely many similar triangles satisfy it. SSA fixes one angle and two sides but leaves ambiguity: depending on the lengths, two different triangles can satisfy the same SSA conditions (the 'ambiguous case'), so it does not guarantee uniqueness."
  explanation: "The deeper principle is that angles constrain direction and shape; sides constrain length and scale. You need enough information to eliminate all degrees of freedom. Two angles eliminate all shape freedom; one side then eliminates scale. But SSA has a side on the 'wrong' side of the fixed angle, which allows the opposite vertex to swing into two positions — the classic ambiguous case."
```

## Explainer

You already know SAS (Side-Angle-Side): fixing two sides and the angle between them determines a triangle uniquely. ASA and AAS extend this reasoning to situations where angles, not sides, are your primary information. The guiding question is always the same: does the given information lock down the triangle's shape and size completely, leaving no room for a different triangle to satisfy the same conditions?

**ASA (Angle-Side-Angle)** answers yes when you know two angles and the side between them. Imagine constructing the triangle: draw the given side. At one endpoint, draw a ray at the first given angle; at the other endpoint, draw a ray at the second given angle. These rays must meet at exactly one point — the third vertex. There is no flexibility: the side length and both angles determine where the rays go, and two non-parallel rays meet at exactly one location. So any two triangles satisfying the same ASA conditions are identical in shape and size: they are congruent.

**AAS (Angle-Angle-Side)** covers the case where the known side is not between the two known angles. At first this seems less constrained — but the **Triangle Angle Sum Theorem** closes the gap. If you know two angles of a triangle, you automatically know the third: the three must sum to 180°. So AAS immediately gives you all three angles plus one side, and knowing all three angles plus any one side determines a triangle completely. In effect, AAS secretly reduces to ASA: use the angle sum to find the missing third angle, and now your known side sits between two known angles. You have ASA.

This reduction has a practical payoff for proofs: when you see AAS in a proof, you can always re-identify which angle the side actually falls between (after invoking the angle sum theorem), and proceed as if you had ASA. The critical mistake to avoid is confusing AAS with **SSA** (two sides and a non-included angle), which looks structurally similar but fails to determine a unique triangle. The asymmetry is fundamental: angles constrain direction, not just length. With two angles fixed, the shape is entirely determined; the only remaining freedom is scale, and fixing any one side eliminates scale ambiguity. That is why ASA and AAS succeed as congruence criteria where SSA does not.
