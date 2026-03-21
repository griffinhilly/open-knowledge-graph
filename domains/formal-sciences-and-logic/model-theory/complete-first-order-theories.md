---
id: complete-first-order-theories
title: Complete First-Order Theories
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: elementary-equivalence-indistinguishability
  type: hard
builds-toward:
- first-order-types-and-formulas
- quantifier-elimination-decidability
tags:
- complete theory
- maximal consistency
- decidability
- Th(M)
stage: advanced
status: draft
---

# Complete First-Order Theories

## Core Idea
A first-order theory T is complete if for every sentence σ, either T ⊢ σ or T ⊢ ¬σ. Equivalently, all models of T are elementarily equivalent. Complete theories are maximal consistent sets corresponding to the theories of single structures (Th(M)). Completeness is a strong restriction forcing model uniqueness up to elementary equivalence.

## Questions

```yaml
- question: "A theory T has two models M and N such that M satisfies sentence σ but N satisfies ¬σ. What does this tell us about T?"
  type: multiple-choice
  options:
    - "T is consistent, since both models exist without contradiction"
    - "T is incomplete, because T decides neither σ nor ¬σ"
    - "T is complete, because the sentence σ distinguishes the models"
    - "T is inconsistent, because no theory can have models disagreeing on any sentence"
  answer: 1
  explanation: "For T to be complete, it must decide every sentence — that is, for every σ, either T ⊢ σ or T ⊢ ¬σ. If M ⊨ σ but N ⊨ ¬σ, then σ is not provable from T (or N would be a countermodel to provability) and ¬σ is not provable either (or M would be a countermodel). So T leaves σ undecided — T is incomplete. Option A confuses consistency (no contradiction) with completeness (every sentence decided). Option C misreads the situation: the fact that σ distinguishes the models is precisely what makes T incomplete."

- question: "Why does a recursively enumerable complete theory have a decidable truth set — that is, why can you algorithmically determine whether any sentence is a theorem?"
  type: multiple-choice
  options:
    - "Because complete theories have finitely many sentences, making exhaustive search feasible"
    - "Because completeness guarantees that enumerating proofs will eventually find a proof of σ or ¬σ for any σ"
    - "Because complete theories have only one model, making truth evaluation straightforward"
    - "Because completeness implies the theory has no undecidable sentences by Gödel's theorem"
  answer: 1
  explanation: "Given a recursively enumerable complete theory T: to decide whether σ is a theorem, simultaneously enumerate all proofs from T. By completeness, either T ⊢ σ or T ⊢ ¬σ — one of these proofs must exist and will eventually be enumerated. The search always terminates. Without completeness, you might search forever and never know whether the absence of a proof means 'not provable' or 'just not found yet.' Option C is wrong: complete theories can have multiple non-isomorphic models (e.g., different infinite cardinalities)."

- question: "If a first-order theory is complete, then all of its models are isomorphic to each other."
  type: true-false
  answer: false
  explanation: "Completeness guarantees only that all models are elementarily equivalent — they agree on the truth of every first-order sentence. But elementary equivalence does not imply isomorphism. For example, the theory of dense linear orders without endpoints (Th(ℚ, <)) is complete, but it has models of every infinite cardinality: ℚ, ℝ, and uncountable dense linear orders are all models, yet none are isomorphic to each other. A theory whose models are all isomorphic is called categorical (for a given cardinality), which is a stronger property than completeness."

- question: "For any structure M, the set of all first-order sentences true in M — written Th(M) — is automatically a complete theory."
  type: true-false
  answer: true
  explanation: "For any sentence σ, M either satisfies σ or it doesn't — there is no third option. Therefore either σ ∈ Th(M) or ¬σ ∈ Th(M), which means Th(M) decides every sentence. This is the semantic route to completeness: Th(M) picks a definite side on every question, and no consistent extension can add any new sentence without it already being in Th(M). Every complete theory arises in this way — as the theory of some structure (or equivalently, as the theory of an equivalence class of elementarily equivalent structures)."

- question: "What is the precise relationship between a theory being complete and all of its models being elementarily equivalent? Why do these two conditions coincide?"
  type: short-answer
  answer: "The two conditions are equivalent. If T is complete, then for every sentence σ, all models agree on σ (because T proves one of σ or ¬σ, and all models satisfy T). Conversely, if all models of T are elementarily equivalent, then for every σ all models agree on its truth value, which means T cannot have models of both σ and ¬σ, so T must prove one of them — making T complete. The equivalence holds because both conditions say exactly the same thing: T leaves no first-order question open."
  explanation: "Understanding this equivalence is central to model theory: completeness (a syntactic/proof-theoretic condition) and all-models-elementarily-equivalent (a semantic condition) are two faces of the same restriction. This is why proving that all models of a theory are elementarily equivalent is a standard strategy for proving completeness, and it is the approach used in quantifier elimination arguments."
```

## Explainer

You already know what **elementary equivalence** means: two structures are elementarily equivalent when no first-order sentence can tell them apart. A **complete theory** is precisely a theory that can only be satisfied by elementarily equivalent models — all its models look the same to first-order logic, even if they differ in size or internal structure. The two definitions (every sentence decided, all models elementarily equivalent) are two sides of the same coin, and understanding why they coincide is the core insight here.

Start from the deductive side. A theory T is a set of sentences closed under logical consequence. T is **consistent** if it does not prove a contradiction. Adding completeness means T has no "gaps" — for every sentence, T takes a stand. This is a maximality condition: you cannot add any new sentence to T without either making it inconsistent or finding it was already derivable. Such a theory is uniquely determined up to logical equivalence, and every model satisfying T must agree on the truth value of every sentence.

Now the semantic side. Given any structure M, its **theory Th(M)** — the set of all first-order sentences true in M — is automatically complete. Why? For any sentence σ, M either satisfies it or doesn't; so σ ∈ Th(M) or ¬σ ∈ Th(M). Every complete theory arises this way: it is the theory of some structure. Two structures have the same complete theory if and only if they are elementarily equivalent, so complete theories precisely classify structures up to first-order indistinguishability.

Completeness is a strong and useful property because it controls the diversity of models. An incomplete theory can have models with wildly different first-order properties — some satisfying σ, others satisfying ¬σ. A complete theory does not allow this: all models agree on every sentence. This is why completeness is linked to **decidability**. If a theory T is complete and axiomatizable (its axioms are recursively enumerable), then T is decidable: to check whether σ is a theorem, enumerate all proofs until you find a proof of σ or of ¬σ — one of them must exist, and the completeness guarantee says the search terminates. This connection drives much of the interest in identifying which natural theories are or are not complete.
