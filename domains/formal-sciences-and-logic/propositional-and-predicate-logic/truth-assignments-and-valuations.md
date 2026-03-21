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

## Questions

```yaml
- question: "Under the truth assignment P = T, Q = F, what is the truth value of the formula (P → Q)?"
  type: multiple-choice
  options:
    - "True — because P is true, the implication is validated"
    - "False — because the antecedent is true but the consequent is false"
    - "True — because Q being false makes the implication vacuously true"
    - "Undefined — implications require both sides to have the same truth value"
  answer: 1
  explanation: "The material conditional (P → Q) is false only when the antecedent (P) is true and the consequent (Q) is false — exactly this assignment. P = T and Q = F gives T → F = F. Options A and C both make the same error: expecting that a true antecedent 'validates' the implication. The truth-functional definition of → says the opposite — a true antecedent with a false consequent is the one case that makes the implication false."

- question: "A formula has 2 atomic propositions and is true under 3 of the 4 possible truth assignments. Which category describes this formula?"
  type: multiple-choice
  options:
    - "Tautology — it is true under the majority of assignments"
    - "Contradiction — it is false under at least one assignment"
    - "Contingency — it is true under some assignments and false under others"
    - "Valid — it is true more often than false"
  answer: 2
  explanation: "A tautology is true under ALL assignments; a contradiction is false under ALL assignments; a contingency is true under SOME and false under SOME. This formula is true under 3/4 assignments and false under 1/4 — so it is a contingency. 'Majority' has no semantic significance. Note that option B confuses 'contradiction' (false under all assignments) with 'not a tautology' (false under some). The single false assignment is exactly what makes this a contingency rather than a tautology."

- question: "The truth value of a compound formula is determined entirely by the truth values of its atomic propositions and the connectives used — the subject matter or meaning of those propositions is irrelevant."
  type: true-false
  answer: true
  explanation: "This is the compositionality principle of truth-functional semantics. Once you have a truth assignment for the atomic propositions, the valuation function recursively computes truth values bottom-up through the formula tree. Whether P means 'It is raining' or 'The number is prime' plays no role — only whether it is assigned T or F. This is what makes propositional logic formal and mechanical: the computation is purely syntactic once you have the assignment."

- question: "A formula that is true under every truth assignment you have tested so far is therefore a tautology."
  type: true-false
  answer: false
  explanation: "A tautology must be true under ALL 2ⁿ possible truth assignments (for n atomic propositions). Testing a subset — even a large one — does not establish tautologyhood, because untested assignments might falsify the formula. The only complete method is a truth table enumerating all 2ⁿ assignments, or a proof in a formal system. Tautology is a universal quantifier over all assignments, not a statistical claim."

- question: "What does it mean for a formula to be a contingency, and why does the concept of a truth assignment make this possible?"
  type: short-answer
  answer: "A contingency is a formula that is true under some truth assignments and false under others — neither always true (tautology) nor always false (contradiction). The concept of a truth assignment makes this possible because it decouples a formula's truth value from any fixed meaning: the same formula can evaluate to T under one assignment and F under another. Without truth assignments, a formula would have a single fixed truth value, and the three-way distinction among tautology, contradiction, and contingency would not exist."
  explanation: "This is the crucial conceptual shift from natural language to formal logic. In natural language, 'It is raining' has a truth value determined by the world. In propositional logic, the atomic proposition P has no fixed truth value — it takes whatever value the assignment gives it. This freedom is what makes formal logic a tool for studying the structure of reasoning rather than specific empirical claims. A tautology is true regardless of what the propositions mean; a contingency's truth depends on what they happen to mean in a given context."
```

## Explainer

Propositional logic is built from atomic propositions — P, Q, R — combined with connectives. From your study of propositional connectives, you know that ∧, ∨, ¬, →, and ↔ each have precise truth-functional definitions. A **truth assignment** (or **valuation**) is the starting point: a function that maps each atomic proposition to either *true* (T) or *false* (F). Once you have a truth assignment, the truth value of any compound formula is determined completely mechanically by applying the connective semantics recursively from the leaves up. There are no judgments to make, no context to consult — just rule application bottom-up through the formula tree.

Consider (P ∧ Q) → R. Under the assignment P = T, Q = T, R = F: evaluate P ∧ Q = T, then T → F = F — the whole formula is false. Under P = T, Q = F, R = F: evaluate P ∧ Q = F, then F → F = T — the formula is true. The same formula has different truth values under different assignments, which is exactly what it means for a formula to be a **contingency** (neither always true nor always false). A formula true under *all* 2ⁿ assignments (for n atomic propositions) is a **tautology** — a logical law. A formula false under *all* assignments is a **contradiction**. Truth tables systematically enumerate all 2ⁿ assignments and record the output, making them a complete decision procedure for propositional logic.

The recursion is formalized as a **valuation function** V_A, where A is the specific assignment. V_A(P) = A(P) for atomic P; V_A(¬φ) = T iff V_A(φ) = F; V_A(φ ∧ ψ) = T iff both V_A(φ) = T and V_A(ψ) = T; and similarly for each connective. The crucial property is **compositionality**: the truth value of a compound formula depends only on the truth values of its immediate subformulas, not on their internal structure or form. This compositionality is what makes truth tables mechanical — you never need to look inside subformulas once you have their values.

Truth assignments ground all the key semantic concepts in propositional logic. **Satisfiability**: a formula is satisfiable iff some assignment makes it true — the computational problem SAT asks to find such an assignment or determine none exists. **Logical consequence**: φ entails ψ (written φ ⊨ ψ) iff every assignment making φ true also makes ψ true. **Logical equivalence**: φ ≡ ψ iff they have identical truth values under every assignment. These are all statements purely about truth assignments — they have nothing to do with proofs or derivations. Understanding that semantics (truth under assignments) and syntax (derivations using proof rules) are distinct, and that soundness and completeness theorems connect them, is the next major conceptual step your study of logic will take you through.
