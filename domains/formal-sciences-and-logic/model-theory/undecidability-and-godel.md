---
id: undecidability-and-godel
title: Undecidability of First-Order Theories
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: decidability-and-undecidability
  type: hard
- id: godels-incompleteness-theorems
  type: soft
builds-toward: []
tags:
- undecidability
- gödel
- church
stage: expert
status: validated
---
# Undecidability of First-Order Theories

## Core Idea
By the completeness theorem and Church-Turing unsolvability, many natural theories are undecidable: Peano arithmetic, ZFC set theory, and even the theory of groups. Model-theoretic techniques show undecidability by proving a theory is expressive enough to encode the halting problem or Diophantine equation solvability.

## How It's Best Learned
Study the undecidability of Peano arithmetic and first-order theory of groups. Understand the reduction from Diophantine problems.

## Questions

```yaml
- question: "A mathematician claims that by choosing a richer, more carefully axiomatized version of Peano arithmetic, we could make it decidable. What is the fundamental flaw in this claim?"
  type: multiple-choice
  options:
    - "PA is already decidable — the issue is only incompleteness, not decidability"
    - "Adding axioms would make PA inconsistent before it could become decidable"
    - "PA's undecidability follows from the fact that it is expressive enough to encode the halting problem — any consistent extension that still captures basic arithmetic inherits this encoding"
    - "The claim is correct for certain axiom systems but not for PA specifically"
  answer: 2
  explanation: "Undecidability of PA is proved by reduction: if PA were decidable, we could translate any halting problem instance into a PA sentence and decide it, solving the halting problem — which is impossible. This reduction works because PA can encode Turing machine computation within its language of addition and multiplication over the natural numbers. Adding axioms does not remove this expressive power as long as the system remains consistent and arithmetically adequate. More axioms might prove more sentences, but they cannot remove the encoding that makes the halting problem translatable."

- question: "A first-order theory T is both complete (for every sentence σ, either T ⊢ σ or T ⊢ ¬σ) and recursively axiomatizable. What follows?"
  type: multiple-choice
  options:
    - "T is necessarily undecidable, since completeness requires non-standard models"
    - "T is necessarily decidable — we can enumerate all proofs and eventually verify any sentence or its negation"
    - "T cannot be consistent, by Gödel's second incompleteness theorem"
    - "T must be an extension of Peano arithmetic"
  answer: 1
  explanation: "A complete, recursively axiomatizable theory is decidable: to decide whether T ⊢ σ, enumerate all proofs of T in order. Since T is complete, either σ or ¬σ has a proof, and the enumeration will find it in finite time. This is why undecidable theories are necessarily incomplete — they cannot be both complete and recursive. PA is undecidable precisely because it is incomplete: there exist sentences that PA neither proves nor refutes, corresponding to sentences true in the standard model but unprovable."

- question: "Gödel's incompleteness theorems apply only to sufficiently expressive formal systems — for instance, they do not apply to a complete theory like the first-order theory of real closed fields."
  type: true-false
  answer: true
  explanation: "This is correct. Gödel's theorems require that the system be able to encode basic arithmetic (Peano arithmetic or Robinson arithmetic Q is enough). The first-order theory of real closed fields (Tarski's result) is complete and decidable, so incompleteness theorems do not apply to it. The key is expressiveness: real closed fields cannot define the natural numbers within them, so they escape the encoding that drives Gödel's proof. Incompleteness is not a universal fate of all formal systems — only those expressive enough to do arithmetic."

- question: "A theory is undecidable if and only if it contains sentences that are true but unprovable from its axioms."
  type: true-false
  answer: false
  explanation: "Undecidability and incompleteness are related but distinct. Undecidability means no algorithm can determine, for every sentence σ, whether T ⊢ σ. Incompleteness means there exist sentences that are true (in the standard/intended model) but unprovable. A theory can be undecidable without having a clear 'standard model' against which truth is measured, and incompleteness describes a gap between provability and truth, not between provability and algorithmic decidability. Gödel's incompleteness theorems do help explain why PA is undecidable, but the concepts themselves are distinct."

- question: "Why does the expressive power of Peano arithmetic — specifically, its ability to talk about addition and multiplication over natural numbers — imply that PA is undecidable?"
  type: short-answer
  answer: "Because within PA's language, you can encode any Turing machine computation as an arithmetic statement. The question 'does this program halt on this input?' translates into a PA sentence about natural numbers. If PA were decidable — if there were an algorithm that, given any sentence, determined whether PA proves it — that algorithm could solve the halting problem. Since the halting problem is provably unsolvable, PA cannot be decidable. PA's undecidability is not a weakness but a consequence of its strength: it is powerful enough to simulate computation, and that power imports the undecidability of the halting problem."
```

## Explainer

You already know that **decidability** asks whether a Turing machine can determine membership in a set — answering yes or no in finite time on every input. Applied to a first-order theory T, the decision problem is: given a sentence σ, does T ⊢ σ? A theory is **decidable** if an algorithm can answer this question for every σ; it is **undecidable** if no such algorithm exists. The surprise is that many theories you might expect to be tractable — the first-order theory of arithmetic, of fields, of groups — are provably undecidable.

The standard strategy for showing a theory T is undecidable is **reduction from a known undecidable problem**. The halting problem, Hilbert's tenth problem (Diophantine equation solvability), and other benchmarks all serve this role. To show Peano arithmetic (PA) is undecidable, you show that if you could decide all PA sentences, you could decide the halting problem. The key ingredient is that PA is **expressive enough**: within the language of addition and multiplication over the natural numbers, you can encode computation. The question "does this program halt on this input?" translates into an arithmetic sentence, and if PA were decidable, halting would be too — a contradiction.

**Gödel's incompleteness theorems** reveal something deeper. The first theorem says that any consistent, sufficiently expressive axiom system cannot be both consistent and complete — there exist true sentences that cannot be proved. The second says such a system cannot prove its own consistency. These results are not merely about provability gaps; they explain why undecidability is inevitable. If PA were decidable, we could enumerate all proofs and check every sentence, but Gödel shows there will always be sentences beyond any fixed axiom system's reach.

The model-theoretic perspective reframes undecidability in terms of variety among models. If a theory T is complete, its models are all elementarily equivalent, and completeness plus axiomatizability implies decidability. Undecidable theories are necessarily incomplete — they have models satisfying σ and other models satisfying ¬σ. PA is undecidable because it has **non-standard models** of arithmetic: structures satisfying all PA axioms but containing "infinite" elements beyond the standard natural numbers, leading to sentences that are true in the standard model but unprovable from the axioms. The connection between undecidability, incompleteness, and model diversity is one of the deepest results in logic.
