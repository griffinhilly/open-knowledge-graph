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
stage: formal-systems
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

## Explainer

Classical logic, as you know from natural deduction, freely uses the **law of excluded middle** (LEM: φ ∨ ¬φ) and proof by contradiction (from ¬φ ⊢ ⊥, conclude φ). These rules let you prove existence by assuming non-existence leads to contradiction — you never need to exhibit the object. Intuitionistic logic asks: what if we demand that every proof be a *construction*? This is not a philosophical quibble; it has mathematical consequences.

The **Brouwer-Heyting-Kolmogorov (BHK) interpretation** makes the constructive reading precise. A proof of φ ∧ ψ is a pair (proof of φ, proof of ψ). A proof of φ ∨ ψ is either a proof of φ or a proof of ψ, together with a label saying which. A proof of φ → ψ is a function that transforms any proof of φ into a proof of ψ. A proof of ∀x.φ(x) is a function mapping each object a to a proof of φ(a). Crucially: there is no proof of φ ∨ ¬φ in general, because to prove a disjunction you must commit to one side. Classical logic's proof of "either there are infinitely many twin primes or there aren't" gives no information about which case holds; intuitionistically, such a proof would be rejected without a witness.

This shifts which theorems are provable. The intuitionistic propositional tautologies are a strict subset of classical ones. For example, ¬¬p → p fails intuitionistically: knowing you cannot have a refutation of p does not, constructively, give you a proof of p. However, p → ¬¬p holds: from a proof of p, you get a function that turns any proof of ¬p into a proof of ⊥. Double negation is strictly weaker than the original. The double negation translation (Gödel-Gentzen) embeds classical logic into intuitionistic logic: every classical tautology translates to an intuitionistic theorem under a systematic ¬¬ prefix.

The deep connection that makes intuitionistic logic central to modern computer science is the **Curry-Howard correspondence**: proofs in intuitionistic natural deduction correspond exactly to programs in simply-typed lambda calculus. A proof of φ → ψ *is* a function of type φ → ψ; a proof of φ ∧ ψ *is* a pair; a proof of φ ∨ ψ *is* a sum type with a tag. This means writing a terminating, well-typed program is the same act as constructing an intuitionistic proof. Classical logic, lacking this correspondence, is the logic of reasoning about computation — intuitionistic logic is the logic of computation itself.
