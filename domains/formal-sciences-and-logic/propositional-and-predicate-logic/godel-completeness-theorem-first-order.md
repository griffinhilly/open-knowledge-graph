---
id: godel-completeness-theorem-first-order
title: Gödel's Completeness Theorem for First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-soundness-completeness
  type: hard
- id: compactness-theorem-model-theory
  type: hard
- id: logical-consequence-and-entailment
  type: soft
- id: proof-structure-and-terminology
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- godels-incompleteness-theorems
- compactness-theorem-applications
tags:
- gödel
- completeness
- first-order-logic
- proof-theory
stage: advanced
status: draft
---

# Gödel's Completeness Theorem for First-Order Logic

## Core Idea
Gödel's completeness theorem states that for first-order logic, semantic consequence and syntactic derivability coincide: Γ ⊨ φ if and only if Γ ⊢ φ. This is a fundamental metatheorem establishing the adequacy of formal proof systems for first-order logic. The completeness proof typically constructs a model from a maximal consistent set of formulas using the Lindenbaum-Henkin construction, leveraging the compactness theorem. Completeness shows that no valid first-order formula escapes any complete proof system—the expressive power of syntax matches semantics.

## How It's Best Learned
Begin with the contrapositive (if Γ is consistent, it has a model) and understand the Henkin construction. Work through a simplified completeness proof for propositional logic first. Discuss how completeness relates to the Löwenheim-Skolem theorem and compactness. Distinguish from the syntactic approach (Hilbert systems) vs. semantic approach (models).

## Common Misconceptions
- Thinking completeness applies to arithmetic (it doesn't — Gödel's incompleteness theorems show this).
- Confusing completeness (all valid formulas provable) with decidability (all formulas can be determined true or false).
- Assuming completeness implies axiomatizability (a consistent theory complete in FOL is still not necessarily recursively axiomatizable).

## Questions

```yaml
- question: "Gödel's incompleteness theorems show that Peano Arithmetic (PA) has true sentences that PA cannot prove. Does this contradict Gödel's completeness theorem for first-order logic?"
  type: multiple-choice
  options:
    - "Yes — completeness says all true sentences are provable, but incompleteness says some are not"
    - "No — completeness applies to logically *valid* sentences (true in all models), while the unprovable arithmetic sentences are true in the standard model but false in some non-standard model"
    - "No — completeness applies only to propositional logic, not first-order arithmetic"
    - "Yes — this is a known paradox in mathematical logic that remains unresolved"
  answer: 1
  explanation: "The two theorems address different objects. Completeness says: every formula that is *logically valid* (true in every model of every theory) is provable in first-order logic. The arithmetic sentences Gödel constructs are true in the standard natural numbers, but Peano Arithmetic has non-standard models where those sentences are false — so they are not logically valid, and completeness makes no promise about them. The incompleteness theorems show that PA (as a theory) is incomplete; the completeness theorem shows that first-order logic (as a proof system) is complete. These are claims about different things."

- question: "The Henkin construction in the completeness proof builds a model for any consistent theory by:"
  type: multiple-choice
  options:
    - "Translating the theory into a computable program and running it to enumerate all theorems"
    - "Extending the theory to a maximal consistent set, adding witness constants for existential claims, and defining a term model whose universe is the set of closed terms"
    - "Applying the axiom of choice to select one model from all possible interpretations"
    - "Constructing the unique minimal model of the theory and verifying it satisfies all axioms"
  answer: 1
  explanation: "The Henkin construction is a three-step process: (1) Use Lindenbaum's lemma to extend the consistent theory Γ to a maximal consistent set Γ* by adding, for each formula, either it or its negation while preserving consistency. (2) For each existential ∃x φ(x) in Γ*, introduce a fresh 'Henkin constant' c and add φ(c) — this gives every existence claim a named witness. (3) Define the term model: the domain is the set of closed terms (modulo provable equality), and each predicate is interpreted by whether the corresponding atomic sentence is in Γ*. This model is built entirely from syntax and satisfies every sentence in Γ*."

- question: "Gödel's completeness theorem for first-order logic states that every logically valid formula — one true in all interpretations — can be derived using the formal proof rules of first-order logic."
  type: true-false
  answer: true
  explanation: "This is the completeness theorem's precise statement: Γ ⊨ φ implies Γ ⊢ φ. In particular, if φ is valid (true in all models, i.e., ∅ ⊨ φ), then φ is provable (⊢ φ). This establishes the adequacy of formal first-order proof systems: the syntactic machinery captures all semantic truth at the logical level. No valid formula escapes provability. The converse direction — soundness (Γ ⊢ φ implies Γ ⊨ φ) — is easier to prove and holds as well, making the two directions perfectly symmetric."

- question: "Gödel's completeness theorem implies that any sufficiently strong first-order theory capable of expressing arithmetic must be able to prove or refute every sentence expressible in its language."
  type: true-false
  answer: false
  explanation: "This confuses completeness of first-order *logic* with completeness of a *theory*. The completeness theorem says first-order logic is a complete proof system for logical validity. A theory like Peano Arithmetic is a specific set of axioms, and whether PA can prove or refute every arithmetic sentence is the question of PA's theoretical completeness — which Gödel's incompleteness theorem shows is false. There exist arithmetic sentences neither provable nor refutable from PA. Completeness of logic ≠ completeness of any particular theory built on that logic."

- question: "What is the difference between 'first-order logic is complete' and 'Peano Arithmetic is complete'? Why does Gödel's completeness theorem not contradict his incompleteness theorem?"
  type: short-answer
  answer: "First-order logic is complete means: every formula that is logically valid (true in all models) is derivable using the proof rules of FOL. This is a claim about the proof system itself. Peano Arithmetic is complete would mean: for every sentence φ in the language of arithmetic, either PA ⊢ φ or PA ⊢ ¬φ. Gödel's incompleteness theorem says this fails — there are arithmetic sentences neither provable nor refutable from PA. There is no contradiction because the completeness theorem only guarantees proofs for *logically valid* sentences, while the Gödel sentences are not logically valid — they are true in the standard model but false in some non-standard model of PA."
  explanation: "The key bridge is non-standard models. PA has models beyond the standard natural numbers (by the compactness theorem applied to PA plus the axiom 'there is an element larger than 0, 1, 2, 3...'). A Gödel sentence G is true in the standard model but false in some non-standard model, so G is not logically valid (not true in *all* models). The completeness theorem promises nothing about sentences that fail in some model. This is why the two theorems coexist: completeness quantifies over all models; incompleteness exploits the existence of non-standard ones."
```

## Explainer

You already know that a proof system for first-order logic is **sound** if every formula it can derive is actually valid — every proof leads somewhere true. Soundness is the easy direction and is established by checking that each inference rule preserves truth. Gödel's Completeness Theorem proves the converse: every valid formula *can* be derived. The formal statement is Γ ⊨ φ if and only if Γ ⊢ φ — semantic entailment and syntactic derivability coincide perfectly. This is a profound alignment between two very different ways of asking "must φ be true?"

The key challenge in proving completeness is the construction direction: given a consistent set of formulas Γ, we must produce a model that satisfies all of them. The **Henkin construction** is the standard approach. First, extend Γ to a **maximal consistent set** Γ* by a Lindenbaum-style argument: enumerate all formulas, adding each one that keeps the set consistent. Then, for every existential statement ∃x φ(x) in Γ*, introduce a fresh **Henkin constant** c and add φ(c) to the set. This gives every existence claim a witness. The resulting theory has the **witness property**: every existential claim is backed by a named element. Finally, the **term model** — whose universe is the set of all closed terms, with equality interpreted by provable equality — satisfies every sentence in Γ*. The model is built entirely from syntax, making it countable regardless of the complexity of Γ.

A critical distinction prevents over-applying completeness. Gödel's Incompleteness Theorems show that the theory of arithmetic (PA) has true sentences that are not provable from its axioms. But completeness says all *valid* formulas are provable — valid means true in *all* models, not just the standard one. Arithmetic has non-standard models with elements that behave strangely, and completeness holds for the whole first-order language. The incompleteness theorems say something different: some true arithmetic sentences are not provable from PA, meaning they are not universally valid — they fail in some non-standard model. First-order logic is complete as a *logic*; arithmetic is incomplete as a *theory*. These are different claims about different objects.

Completeness also implies the Compactness Theorem as an immediate corollary: if every finite subset of Γ is consistent (has a model), then Γ itself is consistent. The proof is one line — proofs are finite objects, so any derivation of a contradiction from Γ uses only finitely many formulas, which form a finite inconsistent subset. This means completeness, compactness, and the Löwenheim-Skolem theorems are all tightly linked: together, they characterize exactly what first-order logic can and cannot express, and they do so by showing that syntax and semantics, at the first-order level, are perfectly matched.
