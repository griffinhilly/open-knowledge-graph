---
id: tarski-undefinability-truth
title: Tarski's Undefinability Theorem and Truth
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: beth-definability-implicit-explicit
  type: soft
builds-toward:
- undecidability-and-godel
- quantifier-elimination-and-decidability
tags:
- tarski
- truth
- undefinability
stage: advanced
status: draft
---

# Tarski's Undefinability Theorem and Truth

## Core Idea
Tarski's undefinability theorem shows that the set of true sentences of a model cannot be defined within the language of that model itself. Even though satisfaction can be defined in meta-mathematics, there is no formula in the object language expressing truth in the model. This fundamental limitation constrains what logical definability can achieve.

## Explainer

From your study of model interpretation and satisfaction, you know that truth in a model is defined at the *metalevel*: we say a formula φ is satisfied by structure M (written M ⊨ φ) by an inductive clause-by-clause definition given *outside* the object language. But could we bring this definition *inside*? Could we write a formula Truth(x) in the language of arithmetic, say, such that Truth(⌜φ⌝) is true if and only if the sentence φ is true? **Tarski's undefinability theorem** proves this is impossible.

The argument is a logical version of the Liar paradox. Begin by assuming, for contradiction, that there exists a formula Truth(x) in the language of arithmetic that correctly identifies the Gödel codes of true sentences. Using the **diagonal lemma** (a consequence of the expressibility of syntax within arithmetic), construct a sentence L such that L is provably equivalent to ¬Truth(⌜L⌝) — a sentence that "says" it is not true. Now ask whether L is true: if L is true, then Truth(⌜L⌝) holds, but then ¬Truth(⌜L⌝) is false, contradicting L's truth. If L is false, then ¬Truth(⌜L⌝) holds, but L is equivalent to ¬Truth(⌜L⌝), so L is true — a contradiction either way. Therefore no such Truth(x) formula can exist.

The key distinction Tarski's theorem establishes is between *object language* and *metalanguage*. Satisfaction (and truth in a model) *can* be defined — but only from outside the language, in a richer metalanguage that can refer to the original language's formulas as objects. This is not a defect of any particular formalization; it is a fundamental semantic limitation. The **Tarski hierarchy** captures this: truth for level-n sentences can be defined in a level-(n+1) metalanguage, but this generates an infinite regress rather than a single unified truth predicate. No language can pull itself up by its own semantic bootstraps.

The contrast with what *is* definable is illuminating. From your prerequisite work on Beth definability, you know that many semantic notions (satisfaction, definability, isomorphism) are perfectly well-defined in the metalanguage — they just cannot be *expressed* inside the object language as a formula. Arithmetic can talk about its own *syntax* (via Gödel coding) but not about its own *semantics* (what that syntax means). This is precisely the gap that Gödel's incompleteness theorems also exploit: the coding of syntax allows self-reference, but truth cannot be captured, only provability — and provability and truth diverge for sufficiently rich theories.
