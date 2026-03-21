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

## Questions

```yaml
- question: "A logician claims that Peano arithmetic (PA) can be replaced by a finite set of equivalent axioms. Why does the compactness theorem refute this claim?"
  type: multiple-choice
  options:
    - "The compactness theorem says PA is incomplete, so it cannot be finitely axiomatized"
    - "By compactness, one can construct a model satisfying any finite subset of PA's axioms yet containing non-standard elements that violate some instance of the induction scheme — no finite axiom set can rule this out"
    - "The compactness theorem applies only to uncountable languages, and PA is countable"
    - "Compactness implies PA is categorical, meaning all its models are isomorphic to the standard natural numbers"
  answer: 1
  explanation: "The argument: suppose PA were equivalent to a finite set F. Add to the language a constant c and the infinite set of sentences {c > 0, c > 1, c > 2, ...}. Every finite subset is satisfiable (interpret c as a large standard integer). By compactness, the whole set is satisfiable — giving a model of F with a non-standard element c larger than every standard natural. But the full induction scheme would exclude this non-standard element, while the finite set F cannot. So F is not equivalent to PA."

- question: "A theory T is complete and finitely axiomatizable. What follows from these two properties together?"
  type: multiple-choice
  options:
    - "T has only finitely many models up to isomorphism"
    - "T is decidable — there is an algorithm to determine, for any sentence φ, whether T ⊢ φ"
    - "T is categorical — all models of T are isomorphic to each other"
    - "T has no infinite models"
  answer: 1
  explanation: "The classical equivalence: a complete theory is finitely axiomatizable if and only if it is decidable. The forward direction is straightforward: enumerate all proofs from the finite axiom set. Since T is complete, for any sentence φ, either a proof of φ or a proof of ¬φ will eventually appear — giving a decision procedure. Categoricity (all models isomorphic) and finiteness of models are separate, stronger conditions that don't follow. Many complete, finitely axiomatizable theories have infinitely many non-isomorphic models."

- question: "The theory of algebraically closed fields of characteristic 0 (ACF₀) is complete but requires infinitely many axioms because each degree n requires its own axiom asserting that every degree-n polynomial has a root."
  type: true-false
  answer: true
  explanation: "ACF₀ is indeed complete (proved by Tarski via quantifier elimination) but not finitely axiomatizable. It requires: (1) the field axioms (finitely many); (2) for each n ≥ 1, the axiom 'every monic polynomial of degree n has a root' (infinitely many); (3) for each prime p, the axiom 'the characteristic is not p' (infinitely many). The infinite axiom schemes are not redundant — they jointly pin down model structure precisely enough to make the theory complete."

- question: "A finitely axiomatizable theory cannot have any infinite models, since finitely many axioms can only describe structures of bounded size."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Finitely many axioms can — and typically do — have infinite models. The group axioms (three sentences) have infinite models. The field axioms have infinite models like ℝ and ℂ. The compactness theorem actually shows the opposite: if a finite theory has arbitrarily large finite models, it must have an infinite model. What finite axiomatizability constrains is the logical structure of the theory, not the size of its models."

- question: "Explain why the compactness theorem implies that Peano arithmetic cannot be finitely axiomatized, using the concept of non-standard models."
  type: short-answer
  answer: "Suppose PA were finitely axiomatizable by a set F. Expand the language with a new constant symbol c and add the infinite set of sentences Σ = {c > n : n ∈ ℕ} (one sentence for each standard natural number). Every finite subset of F ∪ Σ is satisfiable: take the standard natural numbers as a model and interpret c as any sufficiently large integer. By the compactness theorem, the entire set F ∪ Σ has a model M. In M, c is an element greater than every standard natural — a non-standard element. M satisfies all of F but contains this non-standard element. However, the full induction scheme in PA would derive a contradiction from the existence of such an element (induction on the predicate 'x < c' would show no natural number is less than c, contradicting the successor structure). Since F cannot rule out non-standard elements but PA can, F is strictly weaker than PA and not equivalent to it."
  explanation: "The key move is using compactness to build a non-standard model of any finite fragment of PA. This technique — adding a constant and infinitely many lower bounds, then applying compactness — is a general method for showing theories are not finitely axiomatizable. It demonstrates that the infinite induction scheme does genuine logical work: each instance excludes a specific kind of non-standard behavior that no finite set of axioms can collectively exclude."
```

## Explainer

You know that a **complete theory** is one that decides every first-order sentence: for every sentence φ, either T ⊢ φ or T ⊢ ¬φ. And you know from compactness that if every finite subset of an infinite set of sentences has a model, then the whole set has a model. These two tools together let us ask a sharp question: when can a theory be captured by finitely many axioms, versus requiring an infinite axiom scheme?

Consider the theory of **groups**: three axioms (associativity, identity, inverses) — finitely axiomatizable. Now consider **Peano arithmetic (PA)**: the axioms include the induction scheme, which is an infinite family of axioms (one for each formula φ(x) — "if φ(0) and ∀x(φ(x) → φ(x+1)) then ∀x φ(x)"). Can we replace all of these with finitely many axioms? The compactness theorem says no. If PA were equivalent to a finite set F of axioms, then F alone would have all the models that PA has. But one can construct a model that satisfies F and violates some instance of the induction scheme — a **non-standard model** — by compactness. More precisely, one adds a constant c and the axioms c > 0, c > 1, c > 2, … Each finite subset is satisfiable (by ordinary arithmetic with c set to a large integer), so by compactness the whole set is satisfiable, yielding an element larger than all standard naturals. A finitely axiomatized theory cannot rule this out, but the full induction scheme can.

The classical equivalence result is: **a complete theory is finitely axiomatizable if and only if it is decidable**. This connects two apparently different notions. The forward direction: if T is complete and finitely axiomatized, you can decide any sentence φ by running through all proofs from the finite axioms; since T is complete, eventually either a proof of φ or a proof of ¬φ will appear. The backward direction uses the fact that decidable complete theories can be "compressed" — their logical closure has a predictable structure.

A theory that *is* finitely axiomatizable tends to have uniform models: the finite axioms bound the variation in model structure. Compactness makes this precise — if a finite theory has arbitrarily large finite models, it has an infinite model, so the models form a coherent infinite family. The theory of **algebraically closed fields of characteristic 0** (ACF₀) is complete but not finitely axiomatizable: it requires the axiom scheme "every polynomial of degree n has a root" for each n, plus infinitely many axioms ruling out characteristic p > 0. These infinite axiom schemes are not mere technical overhead — they are what allows the theory to pin down model structure with enough precision to be complete.
