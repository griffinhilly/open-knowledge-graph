---
id: counterexample-and-refutation
title: Counterexamples and Refutation
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: satisfaction-relation-fol
  type: hard
- id: ground-instances-and-instantiation
  type: soft
tags:
- first-order-logic
- proof-methods
- refutation
stage: advanced
status: draft
---

# Counterexamples and Refutation

## Core Idea
A counterexample to the claim that Γ ⊨ φ is an interpretation where all formulas in Γ are true but φ is false. Finding a counterexample is equivalent to finding a satisfying assignment for Γ ∧ ¬φ, making the connection between semantic consequence and satisfiability concrete and computationally relevant.

## Explainer

From your study of the **satisfaction relation**, you know that a formula φ is satisfied by an interpretation (a domain plus variable assignments) when the formula evaluates to true under that interpretation. **Semantic consequence** — written Γ ⊨ φ — means that *every* interpretation satisfying all of Γ also satisfies φ. There is no world where the premises are true and the conclusion is false. A **counterexample** is exactly such a world: a specific interpretation that makes all of Γ true and φ false, showing the entailment fails.

The logical connection between counterexamples and satisfiability is tight and bidirectional. Γ ⊨ φ holds if and only if Γ ∪ {¬φ} is unsatisfiable — there is no model of the premises together with the negation of the conclusion. Equivalently, a counterexample to Γ ⊨ φ is precisely a **satisfying model** of Γ ∪ {¬φ}. This reframing turns a question about consequence (an infinitary condition — does every model of Γ satisfy φ?) into a question about satisfiability, which is often more tractable and directly connectable to proof search and automated reasoning.

In practice, constructing a counterexample requires explicit work. For propositional logic, you assign truth values to the atomic variables — making the premises true one by one, tracking which assignments are forced, and checking whether you can still make φ false. For first-order logic, you must also choose a **domain** and interpret predicates and functions over it. Your prerequisite work on **ground instances and instantiation** helps here: a counterexample often starts with a small domain (one or two elements) and instantiates universal claims to check if the conclusion can be blocked. If no assignment works for any domain, that is strong evidence (though not proof) that the entailment holds.

Refutation is the flip side of proof. A **refutation** of a claim is a demonstration that it fails — either by producing a counterexample (for semantic claims) or deriving a contradiction from the claim plus background axioms (for syntactic refutation). In resolution-based automated theorem proving, proving that Γ ⊨ φ is done by refuting Γ ∪ {¬φ}: if you can derive ⊥ from the combined set, you have proved the original entailment holds. The counterexample perspective thus directly motivates refutation-based proof systems: rather than building up a proof of φ, you attempt to build a world where φ fails, and if every such attempt collapses into contradiction, you have your proof.

The skill of finding counterexamples is as valuable as the skill of constructing proofs. When a claimed theorem seems false, the fastest path forward is trying small, simple interpretations: the trivial domain with one element, Boolean domains, permutations of a small set. A well-chosen counterexample not only refutes the claim but illuminates exactly which structural feature the claim wrongly assumed, guiding the repair of flawed arguments.
