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

## Explainer

**CPCTC** stands for "Corresponding Parts of Congruent Triangles are Congruent." Before unpacking it, recall what congruent triangles actually mean from your SSS, SAS, ASA, and AAS work. When you say △ABC ≅ △DEF, you are making an exact claim about which vertex matches which: A corresponds to D, B to E, C to F. From that correspondence, every pair of matching parts is equal — side AB equals side DE, angle B equals angle E, and so on for all six pairs. CPCTC is just the name for this logical consequence. It is not a new rule you must memorize; it is what "congruent triangles" *means*.

The reason CPCTC matters is that most geometry proofs do not ask you to prove triangles congruent for its own sake. They ask you to prove that two specific segments are equal, or two specific angles are equal — things like "prove that the diagonals of this parallelogram bisect each other" or "prove that the base angles of this isosceles triangle are equal." The strategy is always the same: find two triangles in the figure that contain the segments or angles you want to conclude are equal, prove those triangles congruent using SSS, SAS, ASA, or AAS, and then invoke CPCTC to extract the specific parts you need.

This makes CPCTC a two-step move: first establish congruence, then claim the parts. The order is non-negotiable. You cannot invoke CPCTC to *prove* the triangles congruent — that would be circular. CPCTC only fires after congruence is already on the table. Think of the congruence postulates (SSS, SAS, etc.) as the key that unlocks the door, and CPCTC as the ability to walk through it and grab what's on the other side.

Getting CPCTC right requires careful attention to correspondence. If you write △ABC ≅ △DEF, then angle A corresponds to angle D — not to angle E or F. Mis-labeling the correspondence is one of the most common errors in geometric proof. To avoid it, always write out the full congruence statement with vertices in matching order before citing any corresponding parts, and double-check that the correspondence you claimed is supported by whichever congruence postulate you applied.
