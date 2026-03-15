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
