---
id: mathematical-induction-intro
title: Mathematical Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-terminology
  type: hard
- id: predicates-and-quantifiers-intro
  type: soft
builds-toward:
- strong-induction-well-ordering
tags:
- proof
- induction
- recursion
stage: formal-systems
status: draft
---

# Mathematical Induction

## Core Idea
Mathematical induction proves that a statement P(n) holds for all natural numbers n ≥ base by proving: (1) the base case P(base) is true, and (2) the inductive step: for any n, if P(n) is true then P(n+1) is true. The inductive hypothesis allows us to assume P(n) when deriving P(n+1), enabling proofs of infinitely many statements with finite arguments.

## Explainer

From your prerequisite on proof structure, you know that a proof must establish its conclusion with certainty — no gaps, no hand-waving. Induction is the canonical tool when a statement depends on a natural number and you want to prove it for infinitely many values. The key insight is that the natural numbers have a special recursive structure: every natural number other than the base is the successor of some smaller number. Induction exploits this structure to reduce an infinite claim to two finite ones.

The metaphor of a line of dominoes captures the logic perfectly. Each domino represents one instance of the statement P(n). Knocking over the first domino (the **base case**) starts the chain. The **inductive step** guarantees that whenever domino n falls, it knocks over domino n+1. Together, these two facts guarantee every domino falls — for every natural number n, P(n) is true. Neither alone is sufficient: the base case without the inductive step only proves P(1); the inductive step without the base case proves "if any domino falls, all subsequent ones do," which says nothing if none fall to start.

The part that confuses beginners most is the **inductive hypothesis**: during the inductive step, you are allowed to *assume* P(n) is true and use it to derive P(n+1). This feels circular — how can you assume what you're proving? But it isn't circular, because you are proving a conditional: "IF P(n) THEN P(n+1)." You assume the antecedent and derive the consequent. The truth of P(n) itself is not assumed globally; it is assumed only within the scope of proving the implication. The dominos metaphor helps: you're not assuming all dominos fall — you're proving that the mechanical relationship "if this one falls, the next does" holds between each adjacent pair.

Writing an induction proof cleanly involves four steps: state the claim P(n) explicitly; prove the base case directly; write "Assume P(n) holds for some n ≥ base" (the inductive hypothesis); then derive P(n+1) using that assumption. The final line should explicitly cite the inductive hypothesis in the derivation. A common template: "By the inductive hypothesis, [P(n) restated]. Therefore, [algebraic or logical step], which gives P(n+1)." The structure from your proof-writing prerequisite — claim, justification, conclusion — maps directly onto these four steps.
