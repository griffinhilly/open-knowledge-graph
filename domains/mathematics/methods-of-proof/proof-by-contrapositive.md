---
id: proof-by-contrapositive
title: Proof by Contrapositive
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-and-biconditional-statements
  type: hard
- id: proof-structure-terminology
  type: hard
- id: proving-by-contrapositive
  type: soft
- id: direct-proof
  type: soft
- id: counterexamples-and-disproofs
  type: soft
tags:
- proof
- contrapositive
stage: formal-systems
status: validated
---
# Proof by Contrapositive

## Core Idea
To prove 'If P then Q', we can instead prove the contrapositive: 'If not Q then not P'. Since a conditional and its contrapositive are logically equivalent, proving one proves the other. This technique is powerful when the contrapositive is easier to establish than the original statement or when assuming the negation of the conclusion leads naturally to the negation of the hypothesis.

## Questions

```yaml
- question: "To prove 'If n² is odd, then n is odd,' a student assumes n is even and shows that n² must be even. Which proof technique is this?"
  type: multiple-choice
  options:
    - "Direct proof — the student proved the statement from its hypothesis"
    - "Proof by contrapositive — the student proved ¬Q → ¬P"
    - "Proof by contradiction — the student derived a contradiction from P and ¬Q simultaneously"
    - "Proof by exhaustion — the student checked all possible cases"
  answer: 1
  explanation: "The original statement is P → Q: 'If n² is odd (P), then n is odd (Q).' The contrapositive is ¬Q → ¬P: 'If n is even (¬Q), then n² is even (¬P).' The student assumed ¬Q and derived ¬P — the definition of proof by contrapositive. This is not contradiction: the student didn't assume P and ¬Q together and find an impossibility. The contrapositive flows cleanly here because 'n is even → n² is even' (n = 2k gives n² = 4k²) is immediate."

- question: "In a proof by contrapositive of 'If P, then Q,' what do you assume and what must you derive?"
  type: multiple-choice
  options:
    - "Assume P; derive Q"
    - "Assume ¬P; derive ¬Q"
    - "Assume ¬Q; derive ¬P"
    - "Assume P and ¬Q; derive any contradiction"
  answer: 2
  explanation: "The contrapositive of 'P → Q' is '¬Q → ¬P': assume the negation of the conclusion (¬Q) and derive the negation of the hypothesis (¬P). Option A is a direct proof. Option B proves the inverse (¬P → ¬Q), which is NOT logically equivalent to P → Q. Option D is proof by contradiction — you assume P and ¬Q together and reach an impossibility, rather than proving a positive conclusion."

- question: "A proof by contrapositive of 'If P then Q' constitutes a complete proof of 'If P then Q,' because the contrapositive and the original conditional are logically equivalent."
  type: true-false
  answer: true
  explanation: "P → Q and its contrapositive ¬Q → ¬P have identical truth tables — they are false in exactly the same situation (when P is true and Q is false). Proving one is therefore the same as proving the other. This is not an indirect workaround; it is a direct consequence of propositional logic. After proving ¬Q → ¬P, you can immediately conclude P → Q."

- question: "Proof by contrapositive and proof by contradiction are essentially the same technique, since both require negating the conclusion."
  type: true-false
  answer: false
  explanation: "Both methods negate Q, but they differ in structure and what they produce. In a contrapositive proof, you assume ¬Q alone and derive ¬P — you reach a positive conclusion. In contradiction, you assume both P and ¬Q simultaneously and derive any falsehood — you reach an impossibility. Contrapositive is cleaner when ¬Q is productive on its own. Contradiction is needed when the only path forward requires combining all hypotheses. The final moves also differ: contrapositive ends with '¬Q → ¬P, therefore P → Q'; contradiction ends with 'this is impossible, so ¬Q was wrong.'"

- question: "When should you choose proof by contrapositive over a direct proof, and what feature of the statement signals the contrapositive will be the more natural approach?"
  type: short-answer
  answer: "Choose the contrapositive when the negation of the conclusion (¬Q) is a more productive assumption than the hypothesis (P) itself. The signal is in the form of the conclusion: if Q is a positive statement ('x is rational,' 'n is even') whose negation opens concrete algebraic handles, the contrapositive is likely easier. For example, 'If n² is even, then n is even' — assuming 'n is odd' immediately gives n = 2k+1 and n² = 4k²+4k+1 = odd, deriving ¬P cleanly. Proving directly from 'n² is even' to 'n is even' requires a more roundabout argument."
  explanation: "The rule of thumb: if the conclusion has the form 'X has property Y,' its negation 'X lacks property Y' often provides a constructive assumption. The contrapositive is especially natural for proofs involving parity, rationality, divisibility, and set membership, where negations are concrete and algebraically tractable."
```

## Explainer

You already know from your work with conditional statements that "If P then Q" (P → Q) is equivalent to its **contrapositive** "If ¬Q then ¬P" (¬Q → ¬P). This equivalence is not a trick — it is a straightforward fact from truth tables: P → Q is false only when P is true and Q is false, which is exactly when ¬Q is true and ¬P is false. The two statements have identical truth tables in every case. Proof by contrapositive simply exploits this: instead of assuming P and deriving Q, you assume ¬Q and derive ¬P.

The strategic question is: when should you choose the contrapositive over a direct proof? The signal is almost always in the *form* of the conclusion. If Q is a positive statement ("x is rational," "n is divisible by 4"), its negation ¬Q may open useful algebraic handles ("x is irrational," "n is not divisible by 4"). Consider proving: "If n² is odd, then n is odd." Going directly, you must somehow derive a property of n from a property of n². Going via the contrapositive — "If n is even, then n² is even" — is immediate: if n = 2k, then n² = 4k², which is even. The contrapositive flows naturally; the direct proof would require working backwards.

The mechanics are straightforward. Write down the contrapositive: ¬Q → ¬P. State "We prove the contrapositive." Assume ¬Q. Derive ¬P using whatever tools apply. Conclude that ¬Q → ¬P, and therefore P → Q. That final logical step — invoking the equivalence — closes the proof. This is not "assuming the conclusion"; you are proving a *different but equivalent* statement directly, then transferring the result.

It helps to contrast contrapositive with **proof by contradiction**, which students often conflate. Contrapositive: assume ¬Q, prove ¬P — you reach a positive conclusion. Contradiction: assume both P and ¬Q, derive any falsehood — you reach an impossibility. Both methods involve negating the conclusion, but they differ in structure and what they produce. Contrapositive is the cleaner tool when ¬Q is a productive assumption in its own right; contradiction is better when the only path forward is showing that something impossible follows from all assumptions taken together.
