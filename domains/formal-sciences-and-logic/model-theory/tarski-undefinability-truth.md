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

## Questions

```yaml
- question: "Gödel numbering allows arithmetic to encode statements about its own syntax. Tarski's theorem says arithmetic cannot do something analogous for semantics. What exactly is ruled out?"
  type: multiple-choice
  options:
    - "Arithmetic cannot prove its own consistency"
    - "Arithmetic cannot express any self-referential sentence"
    - "Arithmetic cannot define a formula Truth(x) that correctly identifies which sentences are true in the standard model"
    - "Arithmetic cannot quantify over all natural numbers simultaneously"
  answer: 2
  explanation: "Tarski's undefinability theorem rules out the existence of a formula Truth(x) in the language of arithmetic such that Truth(⌜φ⌝) ↔ φ holds for all sentences φ. Arithmetic can perfectly well encode syntactic facts (which strings are valid formulas, what the Gödel code of a formula is, whether one formula is a substitution instance of another) — these are recursive relations on natural numbers. What it cannot do is define what those formulas mean: it cannot express, from the inside, which of its sentences are actually true in the standard model. Option A describes Gödel's second incompleteness theorem; option B is false (the diagonal lemma constructs self-referential sentences); option D is wrong (bounded and unbounded quantification is standard in arithmetic)."

- question: "Tarski's theorem shows that truth in a model can never be rigorously defined — not even in a metalanguage."
  type: true-false
  answer: false
  explanation: "This is a critical misreading of the theorem. Tarski's theorem shows that truth in a model cannot be defined *within the object language itself*. It says nothing against defining truth from outside. Indeed, the standard Tarski semantics (M ⊨ φ defined by induction on formula structure) is a perfectly rigorous definition of truth — it just lives in the metalanguage. The theorem's lesson is not that truth is indefinable, but that it requires a richer language to define it than the language whose truth is being defined. A metalanguage can define object-language truth; the object language cannot define its own truth."

- question: "The Tarski hierarchy of metalanguages provides a single unified truth predicate that covers sentences at all levels."
  type: true-false
  answer: false
  explanation: "The Tarski hierarchy does the opposite: it generates an infinite regress rather than a unified predicate. Truth for level-n sentences is defined in a level-(n+1) metalanguage. But then that metalanguage's own truth requires a level-(n+2) language, and so on indefinitely. There is no level at which you can capture truth for all levels simultaneously — no 'super-language' that collapses the hierarchy. This infinite regress is a fundamental consequence of the undefinability theorem, not a defect to be engineered away. Tarski himself was clear that this prevents any language from having a single, self-contained truth predicate."

- question: "The Tarski hierarchy implies that there is no single unified truth predicate that covers sentences at all levels of the hierarchy."
  type: true-false
  answer: true
  explanation: "Tarski's theorem forces truth to be language-relative: truth for level-n sentences lives in a level-(n+1) metalanguage. Attempting to define a universal truth predicate collapses into the Liar paradox (via the diagonal lemma), as the proof shows. Any candidate for a unified truth predicate would allow construction of a self-referential Liar sentence, generating contradiction. The hierarchy is not optional scaffolding but a structural necessity imposed by the theorem."

- question: "What is the crucial distinction between arithmetic's ability to represent its own syntax and its inability to represent its own semantics, and why does this distinction matter?"
  type: short-answer
  answer: "Syntax concerns the formal structure of expressions — which strings are formulas, what their Gödel codes are, whether one formula is a substitution instance of another. These are all recursive (computable) functions on natural numbers, and arithmetic can define them. Semantics concerns what formulas mean — whether they are true in the standard model. Truth is not a recursive predicate; it cannot be captured by any arithmetical formula. The distinction matters because self-reference through syntax (via Gödel coding) is available in arithmetic and enables Gödel's incompleteness theorems, while self-reference through semantics is blocked by Tarski's theorem. Arithmetic can 'talk about' its own proofs (a syntactic notion) but cannot 'talk about' its own truth (a semantic notion). This explains why Gödel produced incompleteness results (using provability, not truth) while Tarski showed truth is irreducibly metalinguistic."
  explanation: "The syntax/semantics divide is one of the deepest distinctions in logic. Syntax is algorithmic — it can be mechanically checked and encoded. Semantics is interpretive — it requires a model, a structure, an interpretation that stands outside the formal system. Tarski's theorem makes this informal distinction into a mathematical theorem: the gap between syntax and semantics is not closable from within a sufficiently rich language."
```

## Explainer

From your study of model interpretation and satisfaction, you know that truth in a model is defined at the *metalevel*: we say a formula φ is satisfied by structure M (written M ⊨ φ) by an inductive clause-by-clause definition given *outside* the object language. But could we bring this definition *inside*? Could we write a formula Truth(x) in the language of arithmetic, say, such that Truth(⌜φ⌝) is true if and only if the sentence φ is true? **Tarski's undefinability theorem** proves this is impossible.

The argument is a logical version of the Liar paradox. Begin by assuming, for contradiction, that there exists a formula Truth(x) in the language of arithmetic that correctly identifies the Gödel codes of true sentences. Using the **diagonal lemma** (a consequence of the expressibility of syntax within arithmetic), construct a sentence L such that L is provably equivalent to ¬Truth(⌜L⌝) — a sentence that "says" it is not true. Now ask whether L is true: if L is true, then Truth(⌜L⌝) holds, but then ¬Truth(⌜L⌝) is false, contradicting L's truth. If L is false, then ¬Truth(⌜L⌝) holds, but L is equivalent to ¬Truth(⌜L⌝), so L is true — a contradiction either way. Therefore no such Truth(x) formula can exist.

The key distinction Tarski's theorem establishes is between *object language* and *metalanguage*. Satisfaction (and truth in a model) *can* be defined — but only from outside the language, in a richer metalanguage that can refer to the original language's formulas as objects. This is not a defect of any particular formalization; it is a fundamental semantic limitation. The **Tarski hierarchy** captures this: truth for level-n sentences can be defined in a level-(n+1) metalanguage, but this generates an infinite regress rather than a single unified truth predicate. No language can pull itself up by its own semantic bootstraps.

The contrast with what *is* definable is illuminating. From your prerequisite work on Beth definability, you know that many semantic notions (satisfaction, definability, isomorphism) are perfectly well-defined in the metalanguage — they just cannot be *expressed* inside the object language as a formula. Arithmetic can talk about its own *syntax* (via Gödel coding) but not about its own *semantics* (what that syntax means). This is precisely the gap that Gödel's incompleteness theorems also exploit: the coding of syntax allows self-reference, but truth cannot be captured, only provability — and provability and truth diverge for sufficiently rich theories.
