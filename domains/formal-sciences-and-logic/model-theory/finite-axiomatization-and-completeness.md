---
id: finite-axiomatization-and-completeness
title: Finite Axiomatizability and Complete Theories
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: complete-first-order-theories
  type: hard
- id: compactness-theorem-model-theory
  type: soft
builds-toward:
- undecidability-and-godel
- quantifier-elimination-and-decidability
tags:
- axiomatization
- completeness
- finiteness
stage: advanced
status: draft
---

# Finite Axiomatizability and Complete Theories

## Core Idea
Many natural theories are not finitely axiomatizable: Peano arithmetic, the theory of algebraically closed fields, and ZFC all require infinitely many axioms as first-order theories. By a classical result, a complete theory is finitely axiomatizable if and only if it is decidable. The compactness theorem shows finite axiomatizability implies uniformity of model structure.

## Explainer

You know that a **complete theory** is one that decides every first-order sentence: for every sentence φ, either T ⊢ φ or T ⊢ ¬φ. And you know from compactness that if every finite subset of an infinite set of sentences has a model, then the whole set has a model. These two tools together let us ask a sharp question: when can a theory be captured by finitely many axioms, versus requiring an infinite axiom scheme?

Consider the theory of **groups**: three axioms (associativity, identity, inverses) — finitely axiomatizable. Now consider **Peano arithmetic (PA)**: the axioms include the induction scheme, which is an infinite family of axioms (one for each formula φ(x) — "if φ(0) and ∀x(φ(x) → φ(x+1)) then ∀x φ(x)"). Can we replace all of these with finitely many axioms? The compactness theorem says no. If PA were equivalent to a finite set F of axioms, then F alone would have all the models that PA has. But one can construct a model that satisfies F and violates some instance of the induction scheme — a **non-standard model** — by compactness. More precisely, one adds a constant c and the axioms c > 0, c > 1, c > 2, … Each finite subset is satisfiable (by ordinary arithmetic with c set to a large integer), so by compactness the whole set is satisfiable, yielding an element larger than all standard naturals. A finitely axiomatized theory cannot rule this out, but the full induction scheme can.

The classical equivalence result is: **a complete theory is finitely axiomatizable if and only if it is decidable**. This connects two apparently different notions. The forward direction: if T is complete and finitely axiomatized, you can decide any sentence φ by running through all proofs from the finite axioms; since T is complete, eventually either a proof of φ or a proof of ¬φ will appear. The backward direction uses the fact that decidable complete theories can be "compressed" — their logical closure has a predictable structure.

A theory that *is* finitely axiomatizable tends to have uniform models: the finite axioms bound the variation in model structure. Compactness makes this precise — if a finite theory has arbitrarily large finite models, it has an infinite model, so the models form a coherent infinite family. The theory of **algebraically closed fields of characteristic 0** (ACF₀) is complete but not finitely axiomatizable: it requires the axiom scheme "every polynomial of degree n has a root" for each n, plus infinitely many axioms ruling out characteristic p > 0. These infinite axiom schemes are not mere technical overhead — they are what allows the theory to pin down model structure with enough precision to be complete.
