---
id: intuitionistic-logic-intro
title: Introduction to Intuitionistic Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: natural-deduction-propositional
  type: hard
- id: propositional-semantics
  type: soft
- id: godels-incompleteness-theorems
  type: soft
builds-toward:
- modal-logic-intro
tags:
- intuitionistic-logic
- constructive-logic
- Brouwer
- BHK
- law-of-excluded-middle
stage: advanced
status: validated
---
# Introduction to Intuitionistic Logic

## Core Idea
Intuitionistic logic rejects the law of excluded middle (LEM: φ ∨ ¬φ) and double negation elimination as universal logical laws. In the Brouwer-Heyting-Kolmogorov (BHK) interpretation, a proof of φ is a construction: a proof of φ ∧ ψ is a pair of proofs, a proof of φ → ψ is a function transforming proofs of φ into proofs of ψ, and — crucially — a proof of φ ∨ ψ requires either a proof of φ or a proof of ψ, not merely a refutation of both being false. Intuitionistic logic is complete for Kripke semantics (possible-worlds models) and corresponds via the Curry-Howard correspondence to simply-typed lambda calculus.

## How It's Best Learned
Modify natural deduction by removing the classical rules (RAA, LEM) and see which theorems become unprovable. Verify that ¬¬p → p fails intuitionistically. Explore the Curry-Howard correspondence between proofs and programs.

## Common Misconceptions
- Intuitionistic logic is not 'weaker' logic for doubters — it is a different logic for constructive reasoning, with its own completeness theorem.
- ¬¬φ does not imply φ intuitionistically; double negation is a strictly weaker statement than the original.

## Questions

```yaml
- question: "A mathematician announces: 'Either the Goldbach conjecture is true or it isn't — so we already know one of these is provable.' Why would an intuitionist reject this claim?"
  type: multiple-choice
  options:
    - "Intuitionists reject all disjunctions about unresolved mathematical questions"
    - "To assert φ ∨ ψ intuitionistically, you must produce a proof of one specific disjunct — knowing that both being false leads to contradiction is not enough"
    - "The claim is valid intuitionistically; intuitionistic logic agrees with classical logic on all tautologies"
    - "Intuitionists reject LEM only for empirical statements, not mathematical ones"
  answer: 1
  explanation: "Under the BHK interpretation, a proof of φ ∨ ψ requires either a proof of φ or a proof of ψ, together with a tag indicating which. Simply knowing that ¬(¬φ ∧ ¬ψ) — that both can't be false — does not supply a constructive proof of either disjunct. The classical 'law of excluded middle' φ ∨ ¬φ is not intuitionistically provable for arbitrary φ precisely because we cannot always commit to which side holds. Option B is the key insight of the BHK interpretation."

- question: "Which statement correctly describes the intuitionistic status of double negation?"
  type: multiple-choice
  options:
    - "Both p → ¬¬p and ¬¬p → p hold intuitionistically, as in classical logic"
    - "Neither p → ¬¬p nor ¬¬p → p holds intuitionistically"
    - "p → ¬¬p holds but ¬¬p → p fails intuitionistically"
    - "¬¬p → p holds but p → ¬¬p fails intuitionistically"
  answer: 2
  explanation: "p → ¬¬p holds intuitionistically: given a proof of p, construct a function that takes any proof of ¬p (i.e., p → ⊥) and applies it to the proof of p to get ⊥. This is a valid construction. But ¬¬p → p fails: knowing there is no refutation of p does not constructively supply a proof of p. The absence of a counterexample is weaker than the presence of a proof. This asymmetry is definitive of intuitionistic logic."

- question: "Intuitionistic logic is incomplete — it lacks a completeness theorem analogous to the one for classical logic."
  type: true-false
  answer: false
  explanation: "Intuitionistic logic has its own completeness theorem: it is sound and complete with respect to Kripke semantics (possible-worlds models where each world extends the knowledge at earlier worlds). Confusing 'cannot prove all classical tautologies' with 'is incomplete' is a common error. Intuitionistic logic is complete for its own semantics — it simply validates a different set of formulas than classical logic does."

- question: "Under the Curry-Howard correspondence, a proof of the formula φ → ψ in intuitionistic natural deduction corresponds to a function of type φ → ψ in simply-typed lambda calculus."
  type: true-false
  answer: true
  explanation: "The Curry-Howard correspondence ('proofs as programs') establishes an isomorphism between intuitionistic proofs and typed programs. A proof of φ → ψ is exactly a function that transforms any proof of φ into a proof of ψ — a term of type φ → ψ. A proof of φ ∧ ψ is a pair; a proof of φ ∨ ψ is a tagged sum type. This is why intuitionistic logic underlies programming language type theory: writing a well-typed terminating program is the same act as constructing an intuitionistic proof."

- question: "Why does ¬¬p → p fail in intuitionistic logic, even though it is a classical tautology?"
  type: short-answer
  answer: "In intuitionistic logic, ¬¬p means 'there is no proof that p is false' — it is evidence about the absence of a refutation, not a positive construction of p. Classically, because every proposition is either true or false, eliminating ¬p forces p. Intuitionistically, there is a third epistemic state: p may be neither proved nor refuted. To prove p constructively, you must exhibit a proof of p, and the mere impossibility of a refutation does not supply one."
  explanation: "This failure is the sharpest dividing line between classical and intuitionistic logic. Classical logic is bivalent, so ¬¬p collapses to p. Intuitionistic logic operates under the proof-theoretic interpretation that truth means 'there exists a construction,' and absence of refutation is strictly weaker than presence of proof. The Gödel-Gentzen translation embeds classical logic into intuitionistic logic by prepending ¬¬ to formulas, precisely acknowledging that classical truth is intuitionistic double-negation-truth."
```

## Explainer

Classical logic, as you know from natural deduction, freely uses the **law of excluded middle** (LEM: φ ∨ ¬φ) and proof by contradiction (from ¬φ ⊢ ⊥, conclude φ). These rules let you prove existence by assuming non-existence leads to contradiction — you never need to exhibit the object. Intuitionistic logic asks: what if we demand that every proof be a *construction*? This is not a philosophical quibble; it has mathematical consequences.

The **Brouwer-Heyting-Kolmogorov (BHK) interpretation** makes the constructive reading precise. A proof of φ ∧ ψ is a pair (proof of φ, proof of ψ). A proof of φ ∨ ψ is either a proof of φ or a proof of ψ, together with a label saying which. A proof of φ → ψ is a function that transforms any proof of φ into a proof of ψ. A proof of ∀x.φ(x) is a function mapping each object a to a proof of φ(a). Crucially: there is no proof of φ ∨ ¬φ in general, because to prove a disjunction you must commit to one side. Classical logic's proof of "either there are infinitely many twin primes or there aren't" gives no information about which case holds; intuitionistically, such a proof would be rejected without a witness.

This shifts which theorems are provable. The intuitionistic propositional tautologies are a strict subset of classical ones. For example, ¬¬p → p fails intuitionistically: knowing you cannot have a refutation of p does not, constructively, give you a proof of p. However, p → ¬¬p holds: from a proof of p, you get a function that turns any proof of ¬p into a proof of ⊥. Double negation is strictly weaker than the original. The double negation translation (Gödel-Gentzen) embeds classical logic into intuitionistic logic: every classical tautology translates to an intuitionistic theorem under a systematic ¬¬ prefix.

The deep connection that makes intuitionistic logic central to modern computer science is the **Curry-Howard correspondence**: proofs in intuitionistic natural deduction correspond exactly to programs in simply-typed lambda calculus. A proof of φ → ψ *is* a function of type φ → ψ; a proof of φ ∧ ψ *is* a pair; a proof of φ ∨ ψ *is* a sum type with a tag. This means writing a terminating, well-typed program is the same act as constructing an intuitionistic proof. Classical logic, lacking this correspondence, is the logic of reasoning about computation — intuitionistic logic is the logic of computation itself.
