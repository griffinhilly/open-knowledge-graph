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
status: validated
---

# Counterexamples and Refutation

## Core Idea
A counterexample to the claim that Γ ⊨ φ is an interpretation where all formulas in Γ are true but φ is false. Finding a counterexample is equivalent to finding a satisfying assignment for Γ ∧ ¬φ, making the connection between semantic consequence and satisfiability concrete and computationally relevant.

## Questions

```yaml
- question: "You claim: 'From the premises All mammals breathe air and All whales are mammals, it follows that All whales breathe air.' A classmate says this inference fails. What would the classmate need to produce to refute your claim?"
  type: multiple-choice
  options:
    - "A formal derivation showing the conclusion cannot be derived from the premises using inference rules"
    - "A specific interpretation — a domain and predicate assignments — where both premises are true but the conclusion is false"
    - "An alternative argument that leads to the opposite conclusion from the same premises"
    - "A dictionary definition of 'mammal' that does not include whales"
  answer: 1
  explanation: "To refute Γ ⊨ φ (semantic consequence), one must produce a counterexample: a specific interpretation where all premises in Γ are satisfied but φ is false. This is exactly a model of Γ ∪ {¬φ}. In this case, no such interpretation exists because the argument is valid — but the task of refutation is always to construct this model. A derivation failure (option A) concerns syntactic provability, not semantic consequence, and the two can diverge in first-order logic."

- question: "An automated theorem prover attempts to prove Γ ⊨ φ by adding ¬φ to the premises and using resolution to derive a contradiction. Why is this the correct strategy rather than trying to directly construct a proof of φ?"
  type: multiple-choice
  options:
    - "Resolution can only operate on formulas in negation normal form, and adding ¬φ converts φ into the required form"
    - "Γ ⊨ φ holds if and only if Γ ∪ {¬φ} is unsatisfiable — deriving ⊥ from the combined set shows no interpretation can make all premises true while making φ false"
    - "Direct proof of φ would require checking all possible interpretations, which is infinite, while refuting Γ ∪ {¬φ} requires only finite search"
    - "The prover cannot verify φ directly; it can only check whether a given set of formulas is satisfiable or unsatisfiable"
  answer: 1
  explanation: "By the fundamental logical equivalence: Γ ⊨ φ ⟺ Γ ∪ {¬φ} is unsatisfiable. If there is no interpretation where Γ is all-true and φ is false — i.e., where Γ ∪ {¬φ} is satisfied — then φ must hold in every model of Γ. Resolution proves unsatisfiability by deriving the empty clause (⊥). So refuting Γ ∪ {¬φ} is not a workaround; it is logically equivalent to proving Γ ⊨ φ. This equivalence is the theoretical foundation of all refutation-based automated reasoning."

- question: "A counterexample to the semantic consequence Γ ⊨ φ is precisely a satisfying model of the formula set Γ ∪ {¬φ}."
  type: true-false
  answer: true
  explanation: "True, and this equivalence is the central insight of the topic. A counterexample is an interpretation where all formulas in Γ are true but φ is false. 'φ is false' is the same as '¬φ is true.' So a counterexample satisfies Γ and satisfies ¬φ — exactly satisfying Γ ∪ {¬φ}. This transforms the question of semantic consequence (does every model of Γ satisfy φ?) into a question about satisfiability (does Γ ∪ {¬φ} have any model?), which is computationally more tractable and directly connects to proof search."

- question: "If no counterexample can be found after exhaustively checking all possible interpretations over domains of size 1, 2, and 3, then Γ ⊨ φ is proven to hold."
  type: true-false
  answer: false
  explanation: "False. For first-order logic, failing to find a counterexample over small finite domains does not constitute a proof. A counterexample might require a larger or even infinite domain. First-order logic is only semi-decidable: if Γ ⊨ φ holds, a resolution prover will eventually find a proof (completeness), but if Γ ⊭ φ, the counterexample search over finite domains may run forever without terminating. Counterexample search is valuable for quickly refuting false claims but cannot replace proof when the entailment actually holds — finite domain failure is evidence, not proof."

- question: "Explain why finding a counterexample to Γ ⊨ φ is equivalent to finding a satisfying assignment for Γ ∪ {¬φ}, and why this equivalence matters for automated theorem proving."
  type: short-answer
  answer: "Γ ⊨ φ means every interpretation making Γ all-true also makes φ true — equivalently, no interpretation makes Γ all-true and φ false. A counterexample is precisely such an interpretation: all of Γ satisfied, φ false. But φ false means ¬φ is true, so a counterexample satisfies Γ ∪ {¬φ}. The equivalence is: Γ ⊨ φ holds if and only if Γ ∪ {¬φ} has no satisfying model (is unsatisfiable). For automated theorem proving, this converts the problem of proving a consequence (checking all models — an infinitary condition) into the problem of showing a formula set is unsatisfiable (finding a contradiction — something resolution procedures do mechanically). If the resolution prover derives ⊥, the proof is complete; if it finds a satisfying assignment, it has discovered a counterexample."
  explanation: "This equivalence is foundational to the architecture of all refutation-based systems (DPLL SAT solvers, resolution provers, SMT solvers). Rather than constructing proofs directly, these systems attempt to find a model of the negation of the claim. Proof and counterexample search are two sides of the same coin: either the search terminates with a counterexample (the claim is false) or it terminates with a refutation (the claim is true). The theoretical underpinning is this biconditional equivalence."
```

## Explainer

From your study of the **satisfaction relation**, you know that a formula φ is satisfied by an interpretation (a domain plus variable assignments) when the formula evaluates to true under that interpretation. **Semantic consequence** — written Γ ⊨ φ — means that *every* interpretation satisfying all of Γ also satisfies φ. There is no world where the premises are true and the conclusion is false. A **counterexample** is exactly such a world: a specific interpretation that makes all of Γ true and φ false, showing the entailment fails.

The logical connection between counterexamples and satisfiability is tight and bidirectional. Γ ⊨ φ holds if and only if Γ ∪ {¬φ} is unsatisfiable — there is no model of the premises together with the negation of the conclusion. Equivalently, a counterexample to Γ ⊨ φ is precisely a **satisfying model** of Γ ∪ {¬φ}. This reframing turns a question about consequence (an infinitary condition — does every model of Γ satisfy φ?) into a question about satisfiability, which is often more tractable and directly connectable to proof search and automated reasoning.

In practice, constructing a counterexample requires explicit work. For propositional logic, you assign truth values to the atomic variables — making the premises true one by one, tracking which assignments are forced, and checking whether you can still make φ false. For first-order logic, you must also choose a **domain** and interpret predicates and functions over it. Your prerequisite work on **ground instances and instantiation** helps here: a counterexample often starts with a small domain (one or two elements) and instantiates universal claims to check if the conclusion can be blocked. If no assignment works for any domain, that is strong evidence (though not proof) that the entailment holds.

Refutation is the flip side of proof. A **refutation** of a claim is a demonstration that it fails — either by producing a counterexample (for semantic claims) or deriving a contradiction from the claim plus background axioms (for syntactic refutation). In resolution-based automated theorem proving, proving that Γ ⊨ φ is done by refuting Γ ∪ {¬φ}: if you can derive ⊥ from the combined set, you have proved the original entailment holds. The counterexample perspective thus directly motivates refutation-based proof systems: rather than building up a proof of φ, you attempt to build a world where φ fails, and if every such attempt collapses into contradiction, you have your proof.

The skill of finding counterexamples is as valuable as the skill of constructing proofs. When a claimed theorem seems false, the fastest path forward is trying small, simple interpretations: the trivial domain with one element, Boolean domains, permutations of a small set. A well-chosen counterexample not only refutes the claim but illuminates exactly which structural feature the claim wrongly assumed, guiding the repair of flawed arguments.
