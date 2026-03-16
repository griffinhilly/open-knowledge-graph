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

## Explainer

You already know what **elementary equivalence** means: two structures are elementarily equivalent when no first-order sentence can tell them apart. A **complete theory** is precisely a theory that can only be satisfied by elementarily equivalent models — all its models look the same to first-order logic, even if they differ in size or internal structure. The two definitions (every sentence decided, all models elementarily equivalent) are two sides of the same coin, and understanding why they coincide is the core insight here.

Start from the deductive side. A theory T is a set of sentences closed under logical consequence. T is **consistent** if it does not prove a contradiction. Adding completeness means T has no "gaps" — for every sentence, T takes a stand. This is a maximality condition: you cannot add any new sentence to T without either making it inconsistent or finding it was already derivable. Such a theory is uniquely determined up to logical equivalence, and every model satisfying T must agree on the truth value of every sentence.

Now the semantic side. Given any structure M, its **theory Th(M)** — the set of all first-order sentences true in M — is automatically complete. Why? For any sentence σ, M either satisfies it or doesn't; so σ ∈ Th(M) or ¬σ ∈ Th(M). Every complete theory arises this way: it is the theory of some structure. Two structures have the same complete theory if and only if they are elementarily equivalent, so complete theories precisely classify structures up to first-order indistinguishability.

Completeness is a strong and useful property because it controls the diversity of models. An incomplete theory can have models with wildly different first-order properties — some satisfying σ, others satisfying ¬σ. A complete theory does not allow this: all models agree on every sentence. This is why completeness is linked to **decidability**. If a theory T is complete and axiomatizable (its axioms are recursively enumerable), then T is decidable: to check whether σ is a theorem, enumerate all proofs until you find a proof of σ or of ¬σ — one of them must exist, and the completeness guarantee says the search terminates. This connection drives much of the interest in identifying which natural theories are or are not complete.
