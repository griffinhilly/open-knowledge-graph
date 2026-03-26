---
id: logical-implication-entailment
title: Logical Implication and Semantic Entailment
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-assignments-and-valuations
  type: hard
builds-toward:
- logical-consequence-and-validity
- natural-deduction-propositional
- resolution-propositional
tags:
- semantics
- entailment
- validity
stage: formal-systems
status: validated
---

# Logical Implication and Semantic Entailment

## Core Idea
A set of formulas Γ semantically entails φ (written Γ ⊨ φ) if every truth assignment making all formulas in Γ true also makes φ true. This formalizes the intuition that φ logically follows from Γ. Valid formulas are entailed by the empty set.

## Questions

```yaml
- question: "What does {P → Q, ¬Q} ⊨ ¬P mean?"
  type: multiple-choice
  options:
    - "The formula (P → Q) ∧ ¬Q → ¬P is true under at least one truth assignment"
    - "Every truth assignment making both P → Q and ¬Q true also makes ¬P true"
    - "The formulas P → Q and ¬Q are logically equivalent to ¬P"
    - "There exists some truth assignment where P → Q, ¬Q, and ¬P are all simultaneously true"
  answer: 1
  explanation: "Γ ⊨ φ means that every truth assignment satisfying all formulas in Γ also satisfies φ. So {P → Q, ¬Q} ⊨ ¬P says: in every assignment where both P → Q is true and ¬Q is true, ¬P must also be true. Verify: Q = F (from ¬Q). For P → Q to hold with Q = F, we need P = F, so ¬P = T. The conclusion holds in every such assignment — this is modus tollens as a semantic fact. Option A only requires one assignment (not all); options C and D misstate what entailment means."

- question: "A student claims that {P} ⊨ Q holds because 'P entails something.' Why is this wrong?"
  type: multiple-choice
  options:
    - "Because entailment always requires at least two premises"
    - "Because the assignment P = T, Q = F satisfies the premise but falsifies the conclusion, serving as a counterexample"
    - "Because P and Q are independent variables and can never stand in an entailment relation"
    - "Because {P} ⊨ Q would require Q to be a tautology on its own"
  answer: 1
  explanation: "To refute Γ ⊨ φ, you need exactly one counterexample: a truth assignment that makes all formulas in Γ true while making φ false. For {P} ⊨ Q, the assignment P = T, Q = F does this: the premise P is satisfied, but Q is false. Therefore {P} ⊭ Q. Option D is almost right: ∅ ⊨ Q (entailment from the empty set) would require Q to be a tautology, but {P} ⊨ Q only requires Q to be true whenever P is — which is a strictly weaker condition. The counterexample P = T, Q = F shows even that weaker condition fails."

- question: "The semantic entailment {P → Q, ¬Q} ⊨ ¬P is true — there is no assignment making both premises true while the conclusion is false."
  type: true-false
  answer: true
  explanation: "This is modus tollens. Any assignment with ¬Q true has Q = F. For P → Q to be true with Q = F, we need P = F (since T → F = F). With P = F, ¬P = T. So in every assignment satisfying both premises, ¬P holds. There is no counterexample. This is a semantic validation — we are checking truth tables, not applying proof rules. The fact that it corresponds to a familiar inference pattern (modus tollens) is a consequence of soundness: valid proof rules correspond to genuine entailments."

- question: "The statement 'Γ semantically entails φ' makes a claim about a specific truth assignment in which most of Γ and φ happen to be true."
  type: true-false
  answer: false
  explanation: "Semantic entailment is a universal claim, not an existential one. Γ ⊨ φ says that in *every* truth assignment where all formulas in Γ are true, φ is also true. A single assignment where Γ and φ all hold is not enough — it could be a coincidence. To establish entailment you must show no counterexample exists; to refute it you need only one counterexample (an assignment making Γ true and φ false). This universal-vs-existential distinction is what separates entailment from mere satisfiability."

- question: "Explain the difference between the material conditional P → Q and the semantic entailment claim {P} ⊨ Q, and give an example showing they can come apart."
  type: short-answer
  answer: "P → Q is an object-language formula: it is assigned a truth value by each truth assignment — true when P is false or Q is true, false only when P = T and Q = F. Semantic entailment {P} ⊨ Q is a meta-level claim: it says that every assignment making P true also makes Q true. These come apart: P → Q can be true in a specific assignment even when {P} ⊭ Q. Example: the assignment P = F, Q = F makes P → Q true (F → F = T), yet {P} ⊭ Q in general because the assignment P = T, Q = F satisfies the premise but not the conclusion. In short, {P} ⊨ Q is equivalent to ⊨ (P → Q) — P → Q being a tautology — not merely P → Q being true somewhere."
  explanation: "The distinction is foundational for proof theory. Soundness says: if Γ ⊢ φ (syntactically derivable), then Γ ⊨ φ (semantically entailed). Completeness says the converse. These are meta-theorems about the relationship between syntax and semantics. Confusing P → Q (a formula in the object language) with Γ ⊨ φ (a statement in the metalanguage) makes it impossible to even state these theorems cleanly."
```

## Explainer

You already know how to evaluate a formula under a truth assignment — you know which rows of a truth table make a formula true and which make it false. **Semantic entailment** (written Γ ⊨ φ, read "Γ entails φ" or "Γ semantically implies φ") extends this: instead of asking whether φ is true under one assignment, you ask whether φ is true under *every* assignment that makes all of Γ true. The set Γ acts as a filter, narrowing the space of assignments you care about, and φ must hold in all of them.

A concrete example: let Γ = {P, P → Q}. Under any assignment making both P true and P → Q true, Q must also be true (since P is true and the conditional is true, Q cannot be false). So {P, P → Q} ⊨ Q. This is **modus ponens** stated as a semantic fact, not as a proof rule — you are checking the truth tables, not deriving anything. Now consider a different case: {P ∨ Q, ¬P} ⊨ Q. Any assignment making P ∨ Q true and ¬P true must have P = F, which forces Q = T for the disjunction to hold. So Q is guaranteed.

Two special cases sharpen the definition. First, when Γ is empty (∅ ⊨ φ), the condition is that φ is true under *every* truth assignment — there are no premises to satisfy, so φ must be universally true. This is exactly the definition of **validity** (also written ⊨ φ). Tautologies like P ∨ ¬P are entailed by the empty set. Second, the **material conditional** P → Q is a syntactic connective in the object language, while Γ ⊨ φ is a meta-level statement about truth preservation across all assignments. These are different levels of discourse: {P} ⊨ Q is a claim about every row where P is true; P → Q is a formula that can itself be assigned a truth value. They come apart: {P} ⊭ Q in general (make P = T, Q = F), but ⊨ (P → Q) → (P → Q) is trivially valid.

Understanding entailment is the foundation for proof systems. When you study natural deduction or resolution, you will find that these are **syntactic proof systems** — they derive conclusions by applying formal rules. The correctness requirement is that these proof systems agree with semantic entailment: you want every syntactically derivable conclusion to be a semantic consequence, and ideally every semantic consequence to be syntactically derivable. These are **soundness** and **completeness** respectively. The semantic notion (Γ ⊨ φ) is the ground truth — it defines what "logically follows" means. The syntactic notion (Γ ⊢ φ) is the algorithmic approximation. The relationship between them — and the remarkable fact that for classical logic they coincide — is the central theorem of mathematical logic.
