---
id: natural-deduction-propositional
title: Natural Deduction for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: proof-structure-and-terminology
  type: hard
- id: direct-proof
  type: soft
- id: proof-by-contradiction
  type: soft
- id: logical-equivalences
  type: soft
- id: conditional-and-biconditional
  type: soft
- id: mathematical-induction
  type: soft
- id: logical-implication-entailment
  type: soft
builds-toward:
- sequent-calculus-intro
- propositional-soundness-completeness
- natural-deduction-fol
- intuitionistic-logic-intro
tags:
- natural-deduction
- proof-rules
- introduction-elimination
- derivation
stage: formal-systems
status: validated
---

# Natural Deduction for Propositional Logic

## Core Idea
Natural deduction is a proof system designed to mirror human reasoning, with introduction and elimination rules for each connective. Each connective has a rule for introducing it into a conclusion (e.g., ∧-introduction: from φ and ψ, conclude φ ∧ ψ) and a rule for eliminating it from a hypothesis (e.g., ∧-elimination: from φ ∧ ψ, conclude φ). Proofs are structured as derivation trees or Fitch-style columns where assumptions can be introduced and later discharged. The system was designed by Gentzen and Prawitz to make the logical structure of proofs transparent.

## How It's Best Learned
Write proofs in Fitch notation column by column, justifying every line with a rule name and the line numbers used. Start with ∧ and →, then add ¬ via proof by contradiction and ∨ via case analysis.

## Common Misconceptions
- Assumptions are not permanent — they must be discharged (cancelled) when applying rules like →-introduction.
- The order of rule applications matters; writing a conclusion on a line does not automatically validate the reasoning that led to it.

## Questions

```yaml
- question: "To apply →-introduction (the rule for concluding φ → ψ), you must:"
  type: multiple-choice
  options: ["Assert both φ and ψ as independent premises", "Derive ψ under the temporary assumption of φ, then discharge that assumption", "Find a proof of ψ from an empty set of assumptions", "Apply modus ponens to an existing conditional statement"]
  answer: 1
  explanation: "→-introduction works by opening a subproof: you temporarily assume φ, derive ψ within that scope, then close the subproof and conclude φ → ψ — with the assumption φ discharged (no longer in scope). This mirrors the informal pattern 'Suppose φ. Then ... so ψ. Therefore φ → ψ.' The other options describe different operations that do not produce a conditional."

- question: "In a Fitch-style natural deduction proof, once an assumption is written on a line it remains available for use anywhere later in the proof."
  type: true-false
  answer: false
  explanation: "Assumptions have scope. When you close a subproof (e.g., to apply →-introduction or proof by contradiction), the assumption that opened that subproof is discharged and is no longer available on subsequent lines. Using a discharged assumption as a justification is a proof error. This scoping is one of the features that makes natural deduction match informal reasoning, where 'suppose' clauses have limited scope."

- question: "What is the structural difference between an introduction rule and an elimination rule in natural deduction?"
  type: short-answer
  answer: "An introduction rule concludes a formula whose main connective is the connective in question (it builds complexity: e.g., ∧-intro derives φ ∧ ψ from φ and ψ separately). An elimination rule starts from a formula with that connective as its main operator and derives something simpler (it reduces complexity: e.g., ∧-elim derives φ from φ ∧ ψ). Together, each connective's intro and elim rules define what that connective means within the proof system."
  explanation: "This intro/elim pairing is the design principle of natural deduction. Prawitz observed that a 'detour' — introducing a connective only to immediately eliminate it — is always reducible to a shorter proof, which gives natural deduction its normalization theorem. The symmetry between introduction and elimination also corresponds to the Curry-Howard correspondence between proofs and programs."
```

## Explainer

When you learned propositional syntax, you saw how to build well-formed formulas from atomic propositions and connectives — but syntax says nothing about which formulas are *provable*. Natural deduction is a proof system that fills that gap by giving you a specific set of rules: one pair (introduction + elimination) for each connective. The goal is a proof system that feels like careful human reasoning rather than a mechanical symbol-manipulation game.

The style most commonly used today is Fitch notation, where proofs run as a vertical column of numbered lines. Each line states a formula and a justification: either it is a premise, it is an assumption you are temporarily introducing, or it is derived from earlier lines by citing a rule and the line numbers it uses. The ∧-introduction rule, for example, says: if line *m* contains φ and line *n* contains ψ, you may write φ ∧ ψ on a new line, citing ∧-intro, m, n. This is completely mechanical once you know which rule to apply.

The subtlety — and the most important thing to internalize — is assumption discharge. When you want to prove a conditional φ → ψ, you open a *subproof*: you indent, write φ as an assumption, and then derive ψ within that indented block. When you close the block and write φ → ψ on the outer level (citing →-intro), the assumption φ is *discharged*: it is gone, no longer available. This models the informal argument pattern "suppose φ; then we can show ψ; therefore φ → ψ," where the "suppose" does not carry over after the argument closes. Forgetting that assumptions go out of scope is the single most common error in natural deduction proofs.

Negation and disjunction require slightly more care. To derive ¬φ, you assume φ, derive a contradiction (⊥), and then discharge the assumption (¬-intro). To use a disjunction φ ∨ ψ to derive some conclusion χ, you open *two* subproofs — one assuming φ, one assuming ψ — and show χ in each; then ∨-elimination closes both and gives you χ on the outer level. This is case analysis: you know one disjunct must hold, so showing χ in every case is enough.

Natural deduction is not just an academic exercise: the Curry-Howard correspondence tells us that proofs in natural deduction *are* programs (in a typed lambda calculus), and proof normalization corresponds to program evaluation. Understanding intro/elim rules here will give you direct leverage on type theory, intuitionistic logic, and the foundations of proof assistants like Lean and Coq.
