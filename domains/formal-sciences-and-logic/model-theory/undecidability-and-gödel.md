---
id: undecidability-and-gödel
title: Undecidability of First-Order Theories
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: decidability-and-undecidability
  type: hard
- id: godels-incompleteness-theorems
  type: soft
builds-toward:
- models-of-arithmetic-peano
- finite-axiomatization-and-completeness
tags:
- undecidability
- gödel
- church
stage: advanced
status: draft
---

# Undecidability of First-Order Theories

## Core Idea
By the completeness theorem and Church-Turing unsolvability, many natural theories are undecidable: Peano arithmetic, ZFC set theory, and even the theory of groups. Model-theoretic techniques show undecidability by proving a theory is expressive enough to encode the halting problem or Diophantine equation solvability.

## How It's Best Learned
Study the undecidability of Peano arithmetic and first-order theory of groups. Understand the reduction from Diophantine problems.

## Explainer

You already know that **decidability** asks whether a Turing machine can determine membership in a set — answering yes or no in finite time on every input. Applied to a first-order theory T, the decision problem is: given a sentence σ, does T ⊢ σ? A theory is **decidable** if an algorithm can answer this question for every σ; it is **undecidable** if no such algorithm exists. The surprise is that many theories you might expect to be tractable — the first-order theory of arithmetic, of fields, of groups — are provably undecidable.

The standard strategy for showing a theory T is undecidable is **reduction from a known undecidable problem**. The halting problem, Hilbert's tenth problem (Diophantine equation solvability), and other benchmarks all serve this role. To show Peano arithmetic (PA) is undecidable, you show that if you could decide all PA sentences, you could decide the halting problem. The key ingredient is that PA is **expressive enough**: within the language of addition and multiplication over the natural numbers, you can encode computation. The question "does this program halt on this input?" translates into an arithmetic sentence, and if PA were decidable, halting would be too — a contradiction.

**Gödel's incompleteness theorems** reveal something deeper. The first theorem says that any consistent, sufficiently expressive axiom system cannot be both consistent and complete — there exist true sentences that cannot be proved. The second says such a system cannot prove its own consistency. These results are not merely about provability gaps; they explain why undecidability is inevitable. If PA were decidable, we could enumerate all proofs and check every sentence, but Gödel shows there will always be sentences beyond any fixed axiom system's reach.

The model-theoretic perspective reframes undecidability in terms of variety among models. If a theory T is complete, its models are all elementarily equivalent, and completeness plus axiomatizability implies decidability. Undecidable theories are necessarily incomplete — they have models satisfying σ and other models satisfying ¬σ. PA is undecidable because it has **non-standard models** of arithmetic: structures satisfying all PA axioms but containing "infinite" elements beyond the standard natural numbers, leading to sentences that are true in the standard model but unprovable from the axioms. The connection between undecidability, incompleteness, and model diversity is one of the deepest results in logic.
