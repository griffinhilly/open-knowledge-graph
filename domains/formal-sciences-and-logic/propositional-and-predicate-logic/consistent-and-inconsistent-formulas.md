---
id: consistent-and-inconsistent-formulas
title: Consistency and Inconsistency
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-validity
  type: hard
builds-toward:
- model-theory-basics
- complete-first-order-theories
tags:
- semantics
- consistency
- first-order-logic
stage: formal-systems
status: validated
---

# Consistency and Inconsistency

## Core Idea
A set of formulas Γ is consistent (satisfiable) if there exists at least one structure satisfying all formulas in Γ. A set is inconsistent if no such structure exists. Consistency is fundamental: inconsistent theories prove everything and are useless, while consistent theories have models.

## Questions

```yaml
- question: "The set Γ = {P, ¬P, Q → R} is inconsistent. What does this mean for the formula 'The moon is made of cheese'?"
  type: multiple-choice
  options:
    - "Γ neither entails nor refutes it — an inconsistency in Γ has no bearing on unrelated formulas"
    - "Γ entails it — ex falso quodlibet means an inconsistent set entails every formula, including absurd ones"
    - "Γ refutes it — an inconsistent set cannot entail any positive claim"
    - "It depends on whether Q → R is relevant to statements about the moon"
  answer: 1
  explanation: "Ex falso quodlibet ('from falsehood, anything follows') is a theorem of classical logic: if Γ ⊨ ⊥ (falsehood is a consequence of Γ), then Γ ⊨ φ for every formula φ. Semantically, this is vacuously true — there are no models of Γ, so the condition 'every model of Γ satisfies φ' is satisfied trivially by there being nothing to check. An inconsistent set is useless precisely because it entails everything: it cannot distinguish true claims from false ones, making it uninformative as a description of any state of affairs."

- question: "To prove that a set of formulas Γ = {P, Q → R} is consistent, which of the following do you need to do?"
  type: multiple-choice
  options:
    - "Prove that every formula in Γ is a tautology"
    - "Show that no formula in Γ contradicts another formula in Γ"
    - "Exhibit at least one assignment or structure under which all formulas in Γ are simultaneously true"
    - "Derive a contradiction from Γ and then show it is avoidable"
  answer: 2
  explanation: "Consistency is existential: you only need one witness — a single satisfying assignment or structure. For {P, Q → R}, the assignment P = T, Q = F makes both formulas true simultaneously, so the set is consistent. Option B is a common error: formulas can 'look like they don't contradict' but still be collectively unsatisfiable (e.g., {P → Q, Q → ¬P, P} has no pairwise contradiction between any two formulas, but the three together are inconsistent). You must check global simultaneous satisfiability, not pairwise compatibility."

- question: "A set of formulas containing both P and ¬P as members entails every formula in the language."
  type: true-false
  answer: true
  explanation: "A set containing both P and ¬P is inconsistent — no assignment can make P and ¬P simultaneously true, so the set has no models. By ex falso quodlibet, an inconsistent set entails every formula: Γ ⊨ φ for all φ. The semantic definition of entailment ('every model of Γ satisfies φ') is vacuously true when Γ has no models. This is not a curiosity — it is a fundamental feature of classical logic that explains why inconsistency is catastrophic for any formal theory."

- question: "If a set of formulas Γ is inconsistent, it means each individual formula in Γ, taken alone, is logically false."
  type: true-false
  answer: false
  explanation: "Inconsistency is a property of the SET, not of individual members. Each formula in an inconsistent set may be individually satisfiable — even individually valid. For example, {P, ¬P} contains two individually satisfiable formulas that cannot be simultaneously satisfied. Similarly, {P → Q, Q → ¬P, P} contains three formulas each satisfiable on its own, but together they are inconsistent (P and Q → ¬P and P → Q force a contradiction). Inconsistency is about the impossibility of simultaneous truth, not individual falsehood."

- question: "Why is ex falso quodlibet ('from falsehood, anything follows') catastrophic for a formal theory, and what condition must a theory satisfy to be useful?"
  type: short-answer
  answer: "Ex falso quodlibet means that if a theory is inconsistent — if it has no models — then it entails every formula, including contradictions. A theory that entails everything conveys no information: it cannot distinguish true claims from false ones because it declares both true. For a theory to be useful, it must be consistent: there must exist at least one model (structure or assignment) satisfying all its axioms. Only then can the theory's entailments carry meaning — 'this follows from the theory' is informative only if the theory rules out some states of affairs."
  explanation: "Consistency is the minimum condition of meaningfulness for any formal theory. Without it, the theory's logical consequences are trivially all formulas, which is equivalent to saying nothing at all. This is why, in mathematics and logic, consistency proofs — showing that an axiom system has at least one model — are themselves significant results. Gödel's completeness theorem and subsequent work in model theory all rest on the prior question: is this theory consistent? A theory that is not consistent cannot be completed, extended, or used for anything."
```

## Explainer

You already know what logical consequence means: Γ ⊨ φ when every model of Γ is also a model of φ. **Consistency** is the prior question — whether Γ has any models at all. A set of formulas is **consistent** (equivalently, **satisfiable**) if there is at least one assignment or structure under which all its members are simultaneously true. It is **inconsistent** if no such structure exists: the formulas collectively rule out every possible world.

A simple propositional example makes the point concrete. The set {P, Q, P → ¬Q} is inconsistent. Any assignment making P and Q both true makes P → ¬Q false; any assignment making P → ¬Q true while P is true forces Q to be false. No assignment satisfies all three simultaneously. In contrast, {P, Q → R} is consistent — just set P = T, Q = F (or Q = T and R = T); multiple satisfying assignments exist. The key is that consistency is existential: you only need one witness. Inconsistency, on the other hand, requires showing that every candidate fails.

The catastrophic consequence of inconsistency is called **ex falso quodlibet** ("from falsehood, anything follows"): if Γ is inconsistent, then Γ ⊨ φ for every formula φ. In terms of logical consequence, an inconsistent set entails everything — both a formula and its negation. Semantically, this is vacuously true: there are no models of Γ, so the condition "every model of Γ satisfies φ" is vacuously satisfied. This is why inconsistency is lethal to a theory: an inconsistent theory cannot communicate any information because it cannot distinguish true claims from false ones.

Consistency is therefore the minimum condition of usefulness for any theory. From your prerequisite on logical consequence and validity, you know that a formula is valid when it is true in all structures. The connection is: Γ is inconsistent if and only if the empty conjunction of its members is unsatisfiable, if and only if its negation is valid, if and only if ⊥ (falsehood) is a logical consequence of Γ. Checking consistency is equivalent to checking whether Γ ⊨ ⊥ — whether falsehood follows. If it does, Γ has failed as a description of any possible state of affairs. This is the foundation on which model theory, proof theory, and formal verification all rest: before asking what a theory proves, ask whether it is consistent enough to prove anything meaningful at all.
