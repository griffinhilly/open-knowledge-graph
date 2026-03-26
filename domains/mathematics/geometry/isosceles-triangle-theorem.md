---
id: isosceles-triangle-theorem
title: Isosceles Triangle Theorem
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sas
    type: hard
  - id: cpctc
    type: hard
builds-toward:
  - perpendicular-bisectors
  - coordinate-geometry-proofs
tags: [triangles, isosceles, congruence, base-angles]
stage: abstract-reasoning
status: validated
---

# Isosceles Triangle Theorem

## Core Idea
The Isosceles Triangle Theorem states that if two sides of a triangle are congruent, then the angles opposite those sides (the base angles) are congruent. The converse is also true: if two angles are congruent, the sides opposite them are congruent. The proof uses the angle bisector from the vertex angle to create two congruent triangles via SAS. This theorem connects side relationships to angle relationships.

## How It's Best Learned
Draw the angle bisector from the vertex of an isosceles triangle and prove the two halves congruent. Solve problems with variable expressions for base angles. Extend to equilateral triangles (a special case where all three sides and all three angles are congruent, each 60 degrees).

## Common Misconceptions
- Confusing which angles are the "base angles" (they are opposite the congruent sides, not adjacent to them).
- Assuming the converse without proof.
- Forgetting that the equilateral triangle is a special case of isosceles.

## Questions

```yaml
- question: "Triangle PQR has PQ = PR. Angles are labeled ∠P (the angle at vertex P), ∠Q (at vertex Q), and ∠R (at vertex R). Which pair of angles must be congruent?"
  type: multiple-choice
  options:
    - "∠P and ∠Q — the vertex angle and one base angle are always equal"
    - "∠Q and ∠R — the angles opposite the two equal sides are congruent"
    - "∠P and ∠R — the vertex angle equals the opposite base angle"
    - "All three angles — equal sides always force all angles to be equal"
  answer: 1
  explanation: "The Isosceles Triangle Theorem states that angles opposite congruent sides are congruent. Since PQ = PR, the angles opposite those sides are ∠R (opposite PQ) and ∠Q (opposite PR). Both are base angles; ∠P is the vertex angle between the two equal sides. The common mistake is thinking the vertex angle is a base angle or that all three must be equal (that's only the equilateral case)."

- question: "The standard proof of the Isosceles Triangle Theorem draws the angle bisector from the vertex angle. Which congruence criterion establishes that the two resulting triangles are congruent?"
  type: multiple-choice
  options:
    - "SSS — the two legs, the two halves of the base, and the bisector are all paired"
    - "ASA — the bisected vertex angle, bisector, and a base angle are paired"
    - "SAS — the two legs, the two halves of the bisected vertex angle, and the shared bisector"
    - "AAS — two angles and a non-included side are equal in both triangles"
  answer: 2
  explanation: "The angle bisector from the vertex divides the isosceles triangle into two smaller triangles. For SAS, you need two sides and the included angle: (1) the two legs are given as congruent (the definition of isosceles), (2) the bisector creates two equal halves of the vertex angle (included between the leg and the bisector), and (3) the bisector itself is shared — equal to itself by the reflexive property. This gives Side-Angle-Side, establishing congruence. CPCTC then delivers the base angles as corresponding parts."

- question: "In an isosceles triangle drawn with the vertex angle at the top, the 'base angles' are typically the two angles at the geometric bottom of the figure."
  type: true-false
  answer: false
  explanation: "This is the most common identification error. 'Base angles' are defined by their relationship to the congruent sides — they are the angles opposite the two equal legs — not by their geometric position in a diagram. If the triangle is tilted, inverted, or oriented sideways, the base angles are still the two equal ones regardless of where they appear in the figure. The term 'base' is a conceptual label, not a positional one."

- question: "If two angles of a triangle are equal, then the sides opposite those angles must also be equal."
  type: true-false
  answer: true
  explanation: "This is the converse of the Isosceles Triangle Theorem, and it is also true. The converse establishes that the relationship between equal sides and equal opposite angles works in both directions. If you know angle information (two angles are equal), you can conclude side information (the sides opposite them are equal). This bidirectional relationship makes isosceles triangles the class where legs and base angles always come in matched pairs."

- question: "Outline the key steps of the proof of the Isosceles Triangle Theorem. What role does each of SAS and CPCTC play?"
  type: short-answer
  answer: "Draw the angle bisector from the vertex angle to the opposite side. This creates two smaller triangles. Apply SAS: the two legs of the original isosceles triangle are congruent (given), the angle bisector creates two equal halves of the vertex angle (included angle), and the bisector itself is shared by both smaller triangles (reflexive property). SAS establishes that the two smaller triangles are congruent. Then CPCTC (Corresponding Parts of Congruent Triangles are Congruent) delivers the conclusion: the base angles are corresponding parts of the now-proven congruent triangles, so they must be equal."
  explanation: "SAS does the structural work of establishing congruence; CPCTC does the logical work of extracting a conclusion about parts from the whole congruence. The clever move in this proof is creating a self-comparison — using the angle bisector to split one triangle into two that share a side and have known angle and side relationships — rather than comparing two external triangles."
```

## Explainer

Using your knowledge of SAS congruence and CPCTC, you can now understand why isosceles triangles behave so symmetrically. An **isosceles triangle** is one with two equal sides, called the **legs**. The angle between the two legs is the **vertex angle**, and the two remaining angles — each opposite one leg — are the **base angles**. The theorem says: equal sides force equal opposite angles.

The proof works by creating a clever self-comparison. Draw the **angle bisector** from the vertex angle down to the opposite side. This divides the triangle into two smaller triangles. Now check what SAS requires: two sides and the included angle. The two legs are given as equal (the definition of isosceles). The angle bisector creates two equal halves of the vertex angle. The bisector itself is shared by both smaller triangles — equal to itself by the reflexive property. That gives you two sides and the included angle equal in the two smaller triangles — exactly SAS. Now apply CPCTC: the base angles are corresponding parts of these congruent triangles, so they must be equal.

The **converse** works in the other direction: if two angles of a triangle are equal, the sides opposite them are equal. This means angle information implies side information, and vice versa. Together, theorem and converse establish that isosceles triangles are exactly those where legs and base angles come in matched pairs. The equilateral triangle is the limiting case — all three sides equal means all three angles equal, and since the angles must sum to 180°, each is exactly 60°.

When solving problems, the most common error is misidentifying the base angles. Base angles are opposite the congruent sides — they are not necessarily at the geometric "bottom" of the figure. If a diagram shows an isosceles triangle tilted or inverted, the base angles are still the two equal ones, wherever they happen to be. In algebraic problems, this equality lets you set up equations: if the base angles are expressed as (3x + 10)° and (5x − 14)°, setting them equal and solving gives x, and then the angle measure follows. The theorem converts the geometry into an equation.
