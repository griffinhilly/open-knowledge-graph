---
id: cpctc
title: CPCTC (Corresponding Parts of Congruent Triangles are Congruent)
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sss
    type: hard
  - id: triangle-congruence-sas
    type: hard
  - id: triangle-congruence-asa-aas
    type: hard
builds-toward:
  - isosceles-triangle-theorem
  - perpendicular-bisectors
  - parallelogram-properties
tags: [congruence, CPCTC, proof]
stage: abstract-reasoning
status: validated
---

# CPCTC (Corresponding Parts of Congruent Triangles are Congruent)

## Core Idea
CPCTC is not a separate theorem but a logical consequence of the definition of congruent triangles: if two triangles are congruent, then every pair of corresponding parts (sides and angles) is congruent. In proofs, CPCTC is used as a follow-up step after establishing triangle congruence. First prove the triangles congruent (via SSS, SAS, ASA, or AAS), then cite CPCTC to conclude that a specific pair of sides or angles is congruent.

## How It's Best Learned
Present CPCTC as the "payoff" of congruence proofs. Work through multi-step proofs where the goal is to show two segments or angles congruent, and the strategy is to embed them as corresponding parts of congruent triangles. Emphasize that CPCTC can only be used after congruence is established, never before.

## Common Misconceptions
- Using CPCTC as the reason for triangle congruence rather than as a consequence of it.
- Forgetting to identify the correct correspondence between triangles before applying CPCTC.
- Thinking CPCTC is a postulate; it follows directly from the definition of congruence.

## Questions

```yaml
- question: "In a proof, a student wants to show that two specific angles in a figure are congruent. They plan to use CPCTC. What must appear in the proof before CPCTC can be cited?"
  type: multiple-choice
  options:
    - "The student must show that the two angles are corresponding parts of triangles in the figure"
    - "The student must establish that the two triangles containing those angles are congruent using SSS, SAS, ASA, or AAS"
    - "The student must prove the triangles are similar before proving them congruent"
    - "The student must show that all six pairs of corresponding parts are congruent, then apply CPCTC"
  answer: 1
  explanation: "CPCTC can only fire after triangle congruence is already established. The proof structure is always: (1) identify two triangles that contain the angles or sides you want to prove equal, (2) prove those triangles congruent via a congruence postulate or theorem (SSS, SAS, ASA, AAS), (3) then and only then cite CPCTC to extract the specific corresponding parts. Attempting to use CPCTC before proving congruence is circular reasoning. Option D describes what CPCTC already tells you — you don't prove all six pairs independently."

- question: "A proof establishes that △ABC ≅ △PQR. A student then concludes that ∠B ≅ ∠R by CPCTC. Is this valid?"
  type: multiple-choice
  options:
    - "Yes — B and R are both middle letters in their respective triangle names, so they correspond"
    - "No — CPCTC can only be used to prove side congruence, not angle congruence"
    - "No — the congruence statement △ABC ≅ △PQR means B corresponds to Q, not R, so ∠B ≅ ∠Q"
    - "Yes — any angle in a congruent triangle can be paired with any angle in the other triangle"
  answer: 2
  explanation: "Vertex correspondence in a congruence statement is positional: the first vertex of one triangle corresponds to the first vertex of the other, second to second, third to third. In △ABC ≅ △PQR, A↔P, B↔Q, C↔R. Therefore ∠B corresponds to ∠Q, not ∠R. This is one of the most common errors in CPCTC application — always read off correspondences in the order they appear in the congruence statement, not by letter similarity or position within the figure."

- question: "CPCTC can be used as the justification for proving that two triangles are congruent."
  type: true-false
  answer: false
  explanation: "This is the defining misconception about CPCTC. It is a consequence of triangle congruence, not a method for establishing it. Using CPCTC to prove congruence would be circular: 'the triangles are congruent because corresponding parts are congruent, and the parts are congruent because the triangles are congruent.' CPCTC only applies after SSS, SAS, ASA, or AAS has already established congruence in the proof."

- question: "The order in which vertices are listed in a triangle congruence statement determines which parts of the two triangles correspond to each other."
  type: true-false
  answer: true
  explanation: "This is fundamental to correctly applying CPCTC. △ABC ≅ △DEF is a specific claim: A↔D, B↔E, C↔F. This means AB↔DE, BC↔EF, AC↔DF, ∠A↔∠D, ∠B↔∠E, ∠C↔∠F. Writing the congruence statement in the wrong order would misidentify which parts correspond, leading to false conclusions. Always verify that the correspondence you write is actually supported by the congruence postulate you applied."

- question: "Explain why CPCTC cannot serve as the reason for establishing that two triangles are congruent."
  type: short-answer
  answer: "CPCTC is a logical consequence of what 'congruent triangles' means — it unpacks what is already included in the congruence claim. To use it as the reason for congruence would be circular: it would say the triangles are congruent because their corresponding parts are congruent, which is just restating the definition of congruence without proving it. Triangle congruence must first be established via SSS, SAS, ASA, or AAS — only then does CPCTC give you the right to extract any specific corresponding parts."
  explanation: "CPCTC is often called the 'payoff' of a congruence proof because it comes after the hard work is done. The congruence postulates (SSS, SAS, etc.) are what actually prove the triangles match. CPCTC is just the step that makes explicit which pairs of parts are now known to be equal as a result. Reversing the order — using CPCTC to justify congruence — gets the logical structure exactly backwards."
```

## Explainer

**CPCTC** stands for "Corresponding Parts of Congruent Triangles are Congruent." Before unpacking it, recall what congruent triangles actually mean from your SSS, SAS, ASA, and AAS work. When you say △ABC ≅ △DEF, you are making an exact claim about which vertex matches which: A corresponds to D, B to E, C to F. From that correspondence, every pair of matching parts is equal — side AB equals side DE, angle B equals angle E, and so on for all six pairs. CPCTC is just the name for this logical consequence. It is not a new rule you must memorize; it is what "congruent triangles" *means*.

The reason CPCTC matters is that most geometry proofs do not ask you to prove triangles congruent for its own sake. They ask you to prove that two specific segments are equal, or two specific angles are equal — things like "prove that the diagonals of this parallelogram bisect each other" or "prove that the base angles of this isosceles triangle are equal." The strategy is always the same: find two triangles in the figure that contain the segments or angles you want to conclude are equal, prove those triangles congruent using SSS, SAS, ASA, or AAS, and then invoke CPCTC to extract the specific parts you need.

This makes CPCTC a two-step move: first establish congruence, then claim the parts. The order is non-negotiable. You cannot invoke CPCTC to *prove* the triangles congruent — that would be circular. CPCTC only fires after congruence is already on the table. Think of the congruence postulates (SSS, SAS, etc.) as the key that unlocks the door, and CPCTC as the ability to walk through it and grab what's on the other side.

Getting CPCTC right requires careful attention to correspondence. If you write △ABC ≅ △DEF, then angle A corresponds to angle D — not to angle E or F. Mis-labeling the correspondence is one of the most common errors in geometric proof. To avoid it, always write out the full congruence statement with vertices in matching order before citing any corresponding parts, and double-check that the correspondence you claimed is supported by whichever congruence postulate you applied.
