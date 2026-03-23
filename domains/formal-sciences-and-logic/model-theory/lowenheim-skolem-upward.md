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
stage: expert
status: validated
---

# Upward Löwenheim-Skolem Theorem

## Core Idea
The Upward Löwenheim-Skolem Theorem states: if a set of first-order sentences has an infinite model, it has models of arbitrarily large cardinality. Combined with the downward direction, this creates a complete spectrum—for most countable theories, models exist in every infinite cardinality.

## Questions

```yaml
- question: "A logician writes a first-order theory T whose only known model is the natural numbers ℕ (a countably infinite structure). A colleague claims T cannot have a model of size ℵ₁ (the first uncountable cardinality). Is the colleague correct?"
  type: multiple-choice
  options:
    - "Yes — since T was designed around ℕ, any model must be countable"
    - "Yes — first-order logic can distinguish countable from uncountable structures using the axiom of choice"
    - "No — by the Upward Löwenheim-Skolem Theorem, if T has any infinite model it has models of every infinite cardinality, including ℵ₁"
    - "No — but only if T explicitly contains constants that name uncountably many distinct elements"
  answer: 2
  explanation: "The Upward Löwenheim-Skolem Theorem guarantees that any first-order theory with an infinite model has models of every infinite cardinality. The proof adds κ fresh constants c_α (α < κ) and sentences c_α ≠ c_β for all α ≠ β to T. Every finite subset of this expanded theory is satisfiable using the original model M (just interpret finitely many constants as distinct elements of ℕ). Compactness then gives a model satisfying the whole expanded theory, which has cardinality at least κ. The logician's intuition that 'T is about ℕ so it must have countable models' is a category error — T does not 'know' the cardinality of its intended model; it only knows first-order sentences."

- question: "The Löwenheim-Skolem paradox notes that first-order set theory (ZFC) has a countable model, yet ZFC proves that uncountable sets exist (e.g., ℝ). How is this paradox resolved?"
  type: multiple-choice
  options:
    - "ZFC cannot prove the existence of uncountable sets — the apparent proof is an artifact of the formal system"
    - "The countable model of ZFC is internally inconsistent, which is why it admits an uncountable set"
    - "Within the countable model, 'uncountable' means there is no bijection between ℝ and ℕ that *exists inside the model* — but such a bijection may exist outside the model, which the model cannot see"
    - "The downward Löwenheim-Skolem theorem applies only to pure logic, not to mathematical theories like ZFC"
  answer: 2
  explanation: "The resolution is that 'uncountable' is a relative notion in first-order logic. The countable model M satisfies the ZFC sentence 'ℝ is uncountable' because M contains no function (no set within M's universe) that bijects M's version of ℕ with M's version of ℝ. But from outside M, we can observe that M's entire universe is countable — so there ARE bijections between M's ℕ and M's ℝ, they just aren't elements of M. The model is 'unaware' of its own countability. This is a deep illustration of why first-order logic cannot pin down cardinality: truth is relative to what exists in the model's universe, not to what exists in any larger context."

- question: "The Upward Löwenheim-Skolem Theorem implies that no first-order theory with an infinite model can be categorical for any uncountable cardinality."
  type: true-false
  answer: false
  explanation: "False. The theorem guarantees that models of every infinite cardinality *exist*, but it says nothing about uniqueness up to isomorphism. A theory can be κ-categorical — having exactly one model of cardinality κ up to isomorphism — while still having models at all other infinite cardinalities. For example, the theory of algebraically closed fields of characteristic zero is uncountably categorical (Morley categoricity theorem: κ-categorical for any uncountable κ if categorical for some). Upward LS tells us 'large models exist' not 'there are many non-isomorphic large models.' Categoricity theory is precisely the study of when that uniqueness holds."

- question: "First-order logic cannot express the statement 'this structure has exactly ℵ₀ elements' because any first-order theory with a countably infinite model also has models of every larger infinite cardinality."
  type: true-false
  answer: true
  explanation: "True, and this is one of the most important limitative results about first-order logic. You cannot write a first-order sentence that is true in all and only countably infinite structures. The Upward theorem shows any theory with a countably infinite model also has models of size ℵ₁, ℵ₂, and beyond. The Downward theorem shows theories with uncountable models also have countable ones. Together, they show that first-order logic is 'cardinality-blind' for infinite structures — it cannot pin the size down. Expressing 'exactly ℵ₀ elements' requires second-order logic or infinitary logic, which are expressively stronger but sacrifice completeness theorems."

- question: "The Upward Löwenheim-Skolem theorem is often summarized as showing that 'first-order logic cannot characterize infinite structures up to cardinality.' Explain what this means and how the proof of the theorem establishes it."
  type: short-answer
  answer: "The statement means: for any first-order theory T that has an infinite model, there is no way to add first-order axioms that pin down the model's size to exactly one infinite cardinality. No matter what first-order sentences you write, if your theory has one infinite model, it has models of every infinite cardinality. The proof uses compactness: take an infinite model M of T and a target cardinality κ. Expand the language with κ many new constants {c_α : α < κ} and add axioms c_α ≠ c_β for all α ≠ β. Every finite subset is satisfiable by interpreting finitely many c's as distinct elements of M. Compactness gives a model of the whole expanded theory — a model of T that contains at least κ distinct elements. Since κ was arbitrary, T has models of all infinite cardinalities."
  explanation: "This establishes a fundamental boundary of first-order logic: it is strong enough to capture algebraic and order-theoretic structure, but too weak to distinguish ℵ₀ from ℵ₁. Stronger logics (second-order logic, L(ω₁,ω)) can characterize cardinalities but lose the compactness and completeness theorems that make first-order logic so tractable. The tradeoff between expressiveness and metatheoretic properties is one of the central themes of mathematical logic."
```

## Explainer

You have already studied the Downward Löwenheim-Skolem theorem (which shrinks large models down to countable ones) and the Compactness Theorem (which builds models by satisfying infinite families of sentences). The Upward theorem runs in the other direction: any first-order theory with an infinite model has models of *every* infinite cardinality. The proof strategy uses compactness directly. Take an infinite model M of theory T. Add a fresh set of constant symbols {c_α : α < κ} for any target cardinality κ, together with the sentences c_α ≠ c_β for all α ≠ β. Every finite subset of this expanded theory is satisfiable (just interpret finitely many new constants as distinct elements of M). Compactness gives a model where all the new constants are interpreted distinctly — a model of cardinality at least κ.

The philosophical consequence is striking: **first-order logic cannot pin down the cardinality of an infinite structure**. If your theory has a model of size ℵ₀, it has one of size ℵ₁, ℵ₂, and every infinite cardinal beyond. This is the content of the **Löwenheim-Skolem paradox**: set theory, expressed in first-order logic, has a countable model — even though it proves that uncountable sets exist. The resolution is that "uncountable" in the model means "not bijectable with ℕ *within* the model's universe." The bijection exists outside the model, but the model cannot see it.

Together, the downward and upward directions create what model theorists call the **cardinality spectrum** of a theory. A countable theory has models in every infinite cardinality from ℵ₀ upward. This raises a deeper question: for which cardinalities does the theory have *exactly one* model (up to isomorphism)? A theory that has exactly one model of some infinite cardinality κ is called **κ-categorical**. Morley's theorem shows that if a countable theory is κ-categorical for any uncountable κ, it is categorical in all uncountable cardinals — a deep structural result that launched the modern field of stability theory.

Understanding the upward theorem also clarifies what first-order logic *cannot* express. You cannot write a first-order sentence saying "this structure is countable" — if countable models satisfy your theory, uncountable ones do too (upward LS). You cannot express "the domain is finite of arbitrary size" — if arbitrarily large finite models exist, compactness plus upward LS gives infinite ones. These constraints are not bugs but features: they reveal precisely where the expressive power of first-order logic ends and where stronger logics (second-order, infinitary) begin. The cardinality spectrum is therefore a diagnostic tool for measuring the strength of a first-order theory.
