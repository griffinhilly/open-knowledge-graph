---
id: truth-assignments-and-valuations
title: Truth Assignments and Valuations
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-logic-introduction
  type: hard
- id: propositional-connectives
  type: hard
builds-toward:
- logical-implication-entailment
- logical-equivalence-propositional
- tautologies-and-contradictions
tags:
- semantics
- truth-conditions
- propositional
stage: formal-systems
status: draft
---

# Truth Assignments and Valuations

## Core Idea
A truth assignment assigns to each atomic proposition a truth value (true or false). Given an assignment, the truth value of any compound formula is determined recursively by the semantics of its connectives. This provides the foundation for defining satisfiability, validity, and contingency.

## How It's Best Learned
Construct truth tables for progressively complex formulas. Practice computing truth values under different assignments. Observe how changing one atomic proposition affects the overall formula.

## Common Misconceptions
Believing a formula's truth value is intrinsic rather than relative to an assignment. Confusing the number of possible assignments with the number of 'true' cases.

## Explainer

Propositional logic is built from atomic propositions — P, Q, R — combined with connectives. From your study of propositional connectives, you know that ∧, ∨, ¬, →, and ↔ each have precise truth-functional definitions. A **truth assignment** (or **valuation**) is the starting point: a function that maps each atomic proposition to either *true* (T) or *false* (F). Once you have a truth assignment, the truth value of any compound formula is determined completely mechanically by applying the connective semantics recursively from the leaves up. There are no judgments to make, no context to consult — just rule application bottom-up through the formula tree.

Consider (P ∧ Q) → R. Under the assignment P = T, Q = T, R = F: evaluate P ∧ Q = T, then T → F = F — the whole formula is false. Under P = T, Q = F, R = F: evaluate P ∧ Q = F, then F → F = T — the formula is true. The same formula has different truth values under different assignments, which is exactly what it means for a formula to be a **contingency** (neither always true nor always false). A formula true under *all* 2ⁿ assignments (for n atomic propositions) is a **tautology** — a logical law. A formula false under *all* assignments is a **contradiction**. Truth tables systematically enumerate all 2ⁿ assignments and record the output, making them a complete decision procedure for propositional logic.

The recursion is formalized as a **valuation function** V_A, where A is the specific assignment. V_A(P) = A(P) for atomic P; V_A(¬φ) = T iff V_A(φ) = F; V_A(φ ∧ ψ) = T iff both V_A(φ) = T and V_A(ψ) = T; and similarly for each connective. The crucial property is **compositionality**: the truth value of a compound formula depends only on the truth values of its immediate subformulas, not on their internal structure or form. This compositionality is what makes truth tables mechanical — you never need to look inside subformulas once you have their values.

Truth assignments ground all the key semantic concepts in propositional logic. **Satisfiability**: a formula is satisfiable iff some assignment makes it true — the computational problem SAT asks to find such an assignment or determine none exists. **Logical consequence**: φ entails ψ (written φ ⊨ ψ) iff every assignment making φ true also makes ψ true. **Logical equivalence**: φ ≡ ψ iff they have identical truth values under every assignment. These are all statements purely about truth assignments — they have nothing to do with proofs or derivations. Understanding that semantics (truth under assignments) and syntax (derivations using proof rules) are distinct, and that soundness and completeness theorems connect them, is the next major conceptual step your study of logic will take you through.
