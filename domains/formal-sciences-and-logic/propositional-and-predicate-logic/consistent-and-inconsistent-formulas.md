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
status: draft
---

# Consistency and Inconsistency

## Core Idea
A set of formulas Γ is consistent (satisfiable) if there exists at least one structure satisfying all formulas in Γ. A set is inconsistent if no such structure exists. Consistency is fundamental: inconsistent theories prove everything and are useless, while consistent theories have models.

## Explainer

You already know what logical consequence means: Γ ⊨ φ when every model of Γ is also a model of φ. **Consistency** is the prior question — whether Γ has any models at all. A set of formulas is **consistent** (equivalently, **satisfiable**) if there is at least one assignment or structure under which all its members are simultaneously true. It is **inconsistent** if no such structure exists: the formulas collectively rule out every possible world.

A simple propositional example makes the point concrete. The set {P, Q, P → ¬Q} is inconsistent. Any assignment making P and Q both true makes P → ¬Q false; any assignment making P → ¬Q true while P is true forces Q to be false. No assignment satisfies all three simultaneously. In contrast, {P, Q → R} is consistent — just set P = T, Q = F (or Q = T and R = T); multiple satisfying assignments exist. The key is that consistency is existential: you only need one witness. Inconsistency, on the other hand, requires showing that every candidate fails.

The catastrophic consequence of inconsistency is called **ex falso quodlibet** ("from falsehood, anything follows"): if Γ is inconsistent, then Γ ⊨ φ for every formula φ. In terms of logical consequence, an inconsistent set entails everything — both a formula and its negation. Semantically, this is vacuously true: there are no models of Γ, so the condition "every model of Γ satisfies φ" is vacuously satisfied. This is why inconsistency is lethal to a theory: an inconsistent theory cannot communicate any information because it cannot distinguish true claims from false ones.

Consistency is therefore the minimum condition of usefulness for any theory. From your prerequisite on logical consequence and validity, you know that a formula is valid when it is true in all structures. The connection is: Γ is inconsistent if and only if the empty conjunction of its members is unsatisfiable, if and only if its negation is valid, if and only if ⊥ (falsehood) is a logical consequence of Γ. Checking consistency is equivalent to checking whether Γ ⊨ ⊥ — whether falsehood follows. If it does, Γ has failed as a description of any possible state of affairs. This is the foundation on which model theory, proof theory, and formal verification all rest: before asking what a theory proves, ask whether it is consistent enough to prove anything meaningful at all.
