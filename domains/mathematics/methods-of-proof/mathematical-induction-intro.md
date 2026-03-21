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

## Questions

```yaml
- question: "A student proves the inductive step — that if P(n) holds, then P(n+1) holds — but omits the base case. What can they correctly conclude?"
  type: multiple-choice
  options:
    - "P(n) holds for all n ≥ 1, since the chain of implications is established"
    - "P(n) holds for all n ≥ 2, since the base case is only needed for n = 1"
    - "Nothing — without the base case there is no starting point to trigger the chain"
    - "P(n) holds for all sufficiently large n, even if not for small n"
  answer: 2
  explanation: "The inductive step only guarantees that *if* a domino falls, *the next one* falls. Without the base case, no domino is guaranteed to fall in the first place. The chain of implications is unanchored. Both components are strictly necessary: the base case starts the chain and the inductive step propagates it. Without the base case, the inductive step proves 'if any instance is true, all later instances are true' — a vacuously useless guarantee if nothing is true to begin with."

- question: "During the inductive step, a student is told to 'assume P(n) is true.' Their classmate objects: 'You can't assume what you're trying to prove — that's circular!' Which response is correct?"
  type: multiple-choice
  options:
    - "The classmate is right — the assumption of P(n) makes the proof circular and invalid"
    - "The student is proving the conditional 'IF P(n) THEN P(n+1),' so P(n) is the hypothesis of that conditional, not the final conclusion being proved"
    - "The student is allowed to assume P(n) because it was already proved in the base case"
    - "The assumption of P(n) is only valid if n is small enough to verify directly"
  answer: 1
  explanation: "The inductive step proves a conditional statement: for any fixed n, IF P(n) holds THEN P(n+1) holds. Assuming P(n) within that proof is not circular — it is assuming the antecedent of the conditional you are proving, which is standard logical procedure. The final conclusion of the whole induction proof is 'P(n) holds for all n,' which has not been assumed anywhere. The base case and the chain of conditionals together yield that universal conclusion."

- question: "Proving the inductive step alone — without any base case — is sufficient to conclude that P(n) holds for all n ≥ 1."
  type: true-false
  answer: false
  explanation: "The inductive step shows that truth propagates forward, but it doesn't guarantee any starting point. Without a base case, you only know: IF some P(k) is true, THEN all P(n) for n > k are true. If no P(k) is true anywhere, the implication is never triggered. The base case is what anchors the chain. In the domino metaphor: without the base case, you've shown each domino will knock over the next, but you haven't knocked the first one down."

- question: "When proving the inductive step, assuming P(n) is valid because you are only proving the conditional statement 'IF P(n) THEN P(n+1),' not asserting that P(n) is globally true."
  type: true-false
  answer: true
  explanation: "This is precisely why the inductive step is not circular. The assumption of P(n) lives inside the scope of the implication being proved — it is the antecedent, not the conclusion. The conclusion of the inductive step is the implication itself, and the overall conclusion of the entire proof is 'P(n) for all n,' which is derived by combining the base case with infinitely many applications of the implication."

- question: "Why are BOTH the base case and the inductive step required for a proof by induction? What goes wrong if either is missing?"
  type: short-answer
  answer: "The base case establishes that P holds for the starting value (e.g., P(1) is true). The inductive step establishes that truth propagates: if P(n) is true, then P(n+1) is true. Without the base case, the chain has no starting point — even if truth propagates, it never starts. Without the inductive step, you only know one specific case, not all subsequent ones. Both are needed: the base case fires the first domino, and the inductive step ensures every domino that falls knocks down the next."
  explanation: "A classic illustration of why the base case matters: the inductive step for 'all horses are the same color' can be 'proved' (falsely), but breaks down at the base case n=1 transitioning to n=2. An example of why the inductive step matters: you can verify P(1) directly, but that tells you nothing about P(2), P(3), etc. without the propagation guarantee."
```

## Explainer

From your prerequisite on proof structure, you know that a proof must establish its conclusion with certainty — no gaps, no hand-waving. Induction is the canonical tool when a statement depends on a natural number and you want to prove it for infinitely many values. The key insight is that the natural numbers have a special recursive structure: every natural number other than the base is the successor of some smaller number. Induction exploits this structure to reduce an infinite claim to two finite ones.

The metaphor of a line of dominoes captures the logic perfectly. Each domino represents one instance of the statement P(n). Knocking over the first domino (the **base case**) starts the chain. The **inductive step** guarantees that whenever domino n falls, it knocks over domino n+1. Together, these two facts guarantee every domino falls — for every natural number n, P(n) is true. Neither alone is sufficient: the base case without the inductive step only proves P(1); the inductive step without the base case proves "if any domino falls, all subsequent ones do," which says nothing if none fall to start.

The part that confuses beginners most is the **inductive hypothesis**: during the inductive step, you are allowed to *assume* P(n) is true and use it to derive P(n+1). This feels circular — how can you assume what you're proving? But it isn't circular, because you are proving a conditional: "IF P(n) THEN P(n+1)." You assume the antecedent and derive the consequent. The truth of P(n) itself is not assumed globally; it is assumed only within the scope of proving the implication. The dominos metaphor helps: you're not assuming all dominos fall — you're proving that the mechanical relationship "if this one falls, the next does" holds between each adjacent pair.

Writing an induction proof cleanly involves four steps: state the claim P(n) explicitly; prove the base case directly; write "Assume P(n) holds for some n ≥ base" (the inductive hypothesis); then derive P(n+1) using that assumption. The final line should explicitly cite the inductive hypothesis in the derivation. A common template: "By the inductive hypothesis, [P(n) restated]. Therefore, [algebraic or logical step], which gives P(n+1)." The structure from your proof-writing prerequisite — claim, justification, conclusion — maps directly onto these four steps.
