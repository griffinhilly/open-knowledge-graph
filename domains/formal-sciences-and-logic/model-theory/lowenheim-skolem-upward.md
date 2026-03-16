---
id: lowenheim-skolem-upward
title: Upward Löwenheim-Skolem Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: lowenheim-skolem-theorems-overview
  type: hard
- id: compactness-theorem-model-theory
  type: hard
- id: aleph-hierarchy-and-cardinal-numbers
  type: soft
builds-toward:
- categorical-theories-and-uniqueness
tags:
- upward LS
- large models
- cardinality spectrum
stage: advanced
status: draft
---

# Upward Löwenheim-Skolem Theorem

## Core Idea
The Upward Löwenheim-Skolem Theorem states: if a set of first-order sentences has an infinite model, it has models of arbitrarily large cardinality. Combined with the downward direction, this creates a complete spectrum—for most countable theories, models exist in every infinite cardinality.

## Explainer

You have already studied the Downward Löwenheim-Skolem theorem (which shrinks large models down to countable ones) and the Compactness Theorem (which builds models by satisfying infinite families of sentences). The Upward theorem runs in the other direction: any first-order theory with an infinite model has models of *every* infinite cardinality. The proof strategy uses compactness directly. Take an infinite model M of theory T. Add a fresh set of constant symbols {c_α : α < κ} for any target cardinality κ, together with the sentences c_α ≠ c_β for all α ≠ β. Every finite subset of this expanded theory is satisfiable (just interpret finitely many new constants as distinct elements of M). Compactness gives a model where all the new constants are interpreted distinctly — a model of cardinality at least κ.

The philosophical consequence is striking: **first-order logic cannot pin down the cardinality of an infinite structure**. If your theory has a model of size ℵ₀, it has one of size ℵ₁, ℵ₂, and every infinite cardinal beyond. This is the content of the **Löwenheim-Skolem paradox**: set theory, expressed in first-order logic, has a countable model — even though it proves that uncountable sets exist. The resolution is that "uncountable" in the model means "not bijectable with ℕ *within* the model's universe." The bijection exists outside the model, but the model cannot see it.

Together, the downward and upward directions create what model theorists call the **cardinality spectrum** of a theory. A countable theory has models in every infinite cardinality from ℵ₀ upward. This raises a deeper question: for which cardinalities does the theory have *exactly one* model (up to isomorphism)? A theory that has exactly one model of some infinite cardinality κ is called **κ-categorical**. Morley's theorem shows that if a countable theory is κ-categorical for any uncountable κ, it is categorical in all uncountable cardinals — a deep structural result that launched the modern field of stability theory.

Understanding the upward theorem also clarifies what first-order logic *cannot* express. You cannot write a first-order sentence saying "this structure is countable" — if countable models satisfy your theory, uncountable ones do too (upward LS). You cannot express "the domain is finite of arbitrary size" — if arbitrarily large finite models exist, compactness plus upward LS gives infinite ones. These constraints are not bugs but features: they reveal precisely where the expressive power of first-order logic ends and where stronger logics (second-order, infinitary) begin. The cardinality spectrum is therefore a diagnostic tool for measuring the strength of a first-order theory.
