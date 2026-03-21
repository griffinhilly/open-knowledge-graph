---
id: fol-soundness-completeness
title: Soundness and Completeness of First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: first-order-semantics
  type: hard
- id: natural-deduction-fol
  type: hard
builds-toward:
- fol-compactness
- lowenheim-skolem-theorem
- godels-incompleteness-theorems
tags:
- completeness-theorem
- Godel-completeness
- soundness
- FOL
- metatheorem
stage: formal-systems
status: validated
---

# Soundness and Completeness of First-Order Logic

## Core Idea
Gödel's Completeness Theorem (1930) establishes that the standard proof system for first-order logic is both sound (⊢ φ implies ⊨ φ) and complete (⊨ φ implies ⊢ φ). Equivalently, a set of sentences is consistent (has no contradiction) if and only if it has a model. The completeness proof uses the Henkin construction: extend a consistent theory by adding witnesses for every existential claim, then take the quotient structure whose elements are equivalence classes of terms. This theorem is distinct from — and historically precedes — Gödel's Incompleteness Theorems.

## How It's Best Learned
Study soundness first (by induction on derivations) before tackling completeness. Trace the Henkin construction on a small example to see how a model is assembled from syntactic material. Contrast with incompleteness.

## Common Misconceptions
- Gödel's Completeness Theorem and Incompleteness Theorems are different results — completeness says the proof system captures all valid FOL inferences; incompleteness says no consistent recursive theory proves all arithmetical truths.
- Completeness does not mean every true sentence about natural numbers is provable — it means every logically valid sentence (true in all structures) is provable.

## Questions

```yaml
- question: "Gödel proved in 1931 that some true sentences of arithmetic are unprovable. A student concludes that this shows the FOL proof system is incomplete. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — Gödel's 1931 result directly refutes the Completeness Theorem"
    - "The Completeness Theorem only applies to propositional logic, not FOL"
    - "Gödel's Incompleteness Theorems concern specific theories like arithmetic, while Completeness concerns logical validity — sentences true in every structure"
    - "The Completeness Theorem was disproved; Gödel's result replaced it"
  answer: 2
  explanation: "These are different theorems at different levels. Completeness (1930) says: if a sentence φ is true in every possible FOL structure (logically valid), then φ is provable. Incompleteness (1931) says: in theories like Peano arithmetic, there are sentences that are true in ℕ but not provable from the axioms. These sentences are not logically valid — they are true in the natural numbers but false in other structures. There is no contradiction: the proof system captures all logical validities (completeness) but no fixed theory can capture all arithmetical truths (incompleteness)."

- question: "What does the Henkin construction accomplish in the proof of the Completeness Theorem?"
  type: multiple-choice
  options:
    - "It proves that all FOL axioms are valid by semantic inspection"
    - "It shows that any inconsistent theory has a contradiction derivable in finitely many steps"
    - "It builds a model for a consistent theory by treating terms of the language as the elements of the domain"
    - "It reduces completeness of FOL to the already-known completeness of propositional logic"
  answer: 2
  explanation: "The Henkin construction is a way of using syntax to construct semantics. Given a consistent theory T, you extend it to a maximal consistent theory with witnesses — a new constant for every existential claim. The model is then built directly: the elements of the domain are equivalence classes of closed terms, and relations are interpreted by what the theory proves about them. The key insight is that the model's objects are not external mathematical entities but the very terms of the language, organized by provable equality."

- question: "If ⊨ φ (φ is true in every FOL structure), then ⊢ φ (φ is provable in the standard proof system)."
  type: true-false
  answer: true
  explanation: "This is exactly what the Completeness Theorem states: the proof system is complete, meaning it can derive every logically valid sentence. The direction ⊢ φ implies ⊨ φ is soundness (easy direction). The direction ⊨ φ implies ⊢ φ is completeness (deep direction, proved by Gödel in 1930). Together they say the proof system captures exactly the logically valid sentences — no more (soundness) and no less (completeness)."

- question: "Gödel's Completeness Theorem implies that every sentence that is true about the natural numbers is provable from the axioms of first-order arithmetic."
  type: true-false
  answer: false
  explanation: "This is precisely the confusion the topic warns against. Completeness says every logically valid sentence — one true in ALL structures — is provable. A sentence like 'this Gödel sentence G is true in ℕ' is not logically valid; it is true in ℕ but false in non-standard models. Completeness guarantees nothing about sentences that are only true in some structures. Gödel's Incompleteness Theorems show that no consistent recursive axiomatization of arithmetic can prove all arithmetical truths."

- question: "Explain why Gödel's Completeness Theorem and his Incompleteness Theorems do not contradict each other."
  type: short-answer
  answer: "The theorems operate at different levels. The Completeness Theorem says: the FOL proof system derives exactly the sentences that are true in every model — the logically valid sentences. The Incompleteness Theorems say: for theories like arithmetic, there are sentences true in the intended model (ℕ) but not in every model, and these cannot be proved from the axioms. These 'incomplete' sentences are not logically valid — they fail in non-standard models. So completeness still holds: every sentence true in all models is provable. Incompleteness is about theory-specific truth, not logical validity."
  explanation: "The key distinction is between logical validity (true in all structures) and truth-in-a-specific-model (true in ℕ). The Completeness Theorem covers the former; Incompleteness concerns the latter. Gödel's 1930 result and 1931 result are both correct, and they address entirely different questions about entirely different things."
```

## Explainer

You already understand soundness and completeness for propositional logic — the proof system derives exactly the tautologies, no more and no less. First-order logic is vastly richer: formulas can quantify over elements of arbitrary structures, and the range of models is incomparably larger. The question of whether a natural deduction system for FOL still captures all valid reasoning is far from obvious. **Gödel's Completeness Theorem** (1930) answers it affirmatively: the standard proof rules are both sound and complete for first-order validity.

**Soundness** is the easier half: every derivable sentence ⊢ φ is logically valid ⊨ φ (true in all structures). The proof is a straightforward induction on the derivation — each inference rule preserves validity, and the axioms are valid. You can verify this for each rule of your natural deduction system directly.

**Completeness** is the deep direction: if φ is true in every model (⊨ φ), then φ is provable (⊢ φ). Equivalently — and this reformulation is crucial — if a set of sentences Γ is *consistent* (no contradiction is derivable from it), then Γ has a *model*. The proof uses the **Henkin construction**. Given a consistent theory T, extend it step by step: for every existential sentence ∃x φ(x) in the language, add a new constant symbol c and the axiom φ(c), acting as a *witness*. After closing under logical consequences and all such witnesses, you have a **Henkin theory** — a maximal consistent set that explicitly names a witness for every existential claim. The model is then built directly: the elements are equivalence classes of closed terms (under provable equality), and the interpretation of relations and functions is read off from what the theory proves. This syntactically constructed structure is a model of T.

The key conceptual move is using *syntax to build semantics*: the model's elements are not mathematical objects we invented, but the very terms of the language, grouped by what the theory equates. This technique reappears throughout model theory. The completeness theorem has two major corollaries: the **compactness theorem** (if every finite subset of Γ has a model, then Γ has a model — following because any inconsistency involves finitely many axioms) and the **Löwenheim-Skolem theorem** (satisfiable theories have models of every infinite cardinality). Both follow from the completeness proof and are the engines of classical model theory. And crucially: Gödel's *Incompleteness* Theorems do not contradict completeness. Completeness says the proof system captures all *logically valid* sentences — those true in every structure. Incompleteness says that for specific theories like arithmetic, there exist sentences true in ℕ but not provable from the axioms. These are entirely different claims about entirely different levels of the metatheory.
