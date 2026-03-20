---
id: zfc-independence-from-other-axioms
title: Independence in ZFC and Limitations of Axiomatization
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: inner-models-relative-consistency
  type: hard
- id: forcing-intro
  type: hard
tags:
- independence
- zfc
- continuum
- axioms
stage: advanced
status: draft
---

# Independence in ZFC and Limitations of Axiomatization

## Core Idea
The continuum hypothesis (CH) and the axiom of choice (AC) are independent of ZFC: both ZFC + CH and ZFC + ¬CH are consistent, as are ZFC + AC and ZFC + ¬AC (without choice, not AC). Gödel proved ZFC ⊢ Con(ZFC → Con(ZFC+CH)); Cohen's forcing proved ZFC ⊢ Con(ZFC → Con(ZFC + ¬CH)). These results show that ZFC cannot uniquely determine all mathematical truths.

## How It's Best Learned
Understand Gödel's proof that CH holds in L. Learn forcing: Cohen's extension of models to produce violations of CH. Compare model-theoretic and syntactic consistency. Discuss implications for mathematical truth and foundational pluralism.

## Common Misconceptions
- Assuming independence means both options are 'equally true' (truth in V may favor one; we simply cannot prove it in ZFC).
- Confusing statement independence with the consistency of negating axioms; independence refers to theorems, not axioms themselves.

## Explainer

You have studied inner models and forcing — the two main technical tools for proving independence results in set theory. **Independence** means something precise: a statement φ is independent of ZFC if neither ZFC ⊢ φ nor ZFC ⊢ ¬φ. This is different from φ being unknown or contested. It means ZFC literally cannot settle the question, even with arbitrarily long valid proof chains. The **continuum hypothesis** (CH) — the claim that there is no set with cardinality strictly between ℵ₀ and 2^ℵ₀ — is the most celebrated example, and its independence was established by combining two completely different strategies: inner models and forcing.

Gödel's contribution was the **constructible universe L**: the smallest possible model of ZFC, built by iteratively adding only sets that are explicitly definable from what already exists. In L, the real numbers are tightly controlled — every real is definable from ordinals in a precise sense — and this minimal structure forces CH to hold. If ZFC is consistent, then ZFC+CH is consistent: you can always retreat to L as a model where CH is true. This is **relative consistency**, not a proof that CH is true in every model. The move is: "assuming ZFC has any model at all, L is a model where CH additionally holds, so adding CH cannot introduce contradiction."

Cohen's **forcing** technique works in the opposite direction. Starting from a model M of ZFC+CH, Cohen constructed a larger model M[G] by adjoining a "generic" extension object G — a collection of new reals indexed by ℵ₂ many conditions, carefully chosen so that no real in M can "anticipate" which conditions are in G. The resulting model M[G] satisfies 2^ℵ₀ ≥ ℵ₂, so CH fails. The technical heart of forcing is the **forcing relation** ⊩ — a way of deciding, inside M, which statements about the not-yet-constructed M[G] will be true — and proving that M[G] satisfies all ZFC axioms while violating CH. Together, Gödel and Cohen showed that ZFC has models where CH is true and models where CH is false: the axioms are completely silent on the question.

The deeper lesson is epistemological. Some set theorists take this to mean we should seek stronger axioms — large cardinal axioms, or **Forcing Axioms** like Martin's Maximum — that might settle CH (and indeed, many large cardinal axioms imply 2^ℵ₀ = ℵ₂, ruling out CH). Others adopt a **pluralist** position: different set-theoretic universes are equally legitimate mathematical objects, much as different geometries became equally legitimate after the independence of the parallel postulate from Euclid's other axioms was established. Either way, the independence results expose a hard ceiling on what formal axiomatization alone can accomplish — a ceiling Gödel's incompleteness theorems had already predicted at the metatheoretic level, now made concrete by specific unsettled mathematical questions about the size of the continuum.
