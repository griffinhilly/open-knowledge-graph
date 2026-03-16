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

## Explainer

You already understand soundness and completeness for propositional logic — the proof system derives exactly the tautologies, no more and no less. First-order logic is vastly richer: formulas can quantify over elements of arbitrary structures, and the range of models is incomparably larger. The question of whether a natural deduction system for FOL still captures all valid reasoning is far from obvious. **Gödel's Completeness Theorem** (1930) answers it affirmatively: the standard proof rules are both sound and complete for first-order validity.

**Soundness** is the easier half: every derivable sentence ⊢ φ is logically valid ⊨ φ (true in all structures). The proof is a straightforward induction on the derivation — each inference rule preserves validity, and the axioms are valid. You can verify this for each rule of your natural deduction system directly.

**Completeness** is the deep direction: if φ is true in every model (⊨ φ), then φ is provable (⊢ φ). Equivalently — and this reformulation is crucial — if a set of sentences Γ is *consistent* (no contradiction is derivable from it), then Γ has a *model*. The proof uses the **Henkin construction**. Given a consistent theory T, extend it step by step: for every existential sentence ∃x φ(x) in the language, add a new constant symbol c and the axiom φ(c), acting as a *witness*. After closing under logical consequences and all such witnesses, you have a **Henkin theory** — a maximal consistent set that explicitly names a witness for every existential claim. The model is then built directly: the elements are equivalence classes of closed terms (under provable equality), and the interpretation of relations and functions is read off from what the theory proves. This syntactically constructed structure is a model of T.

The key conceptual move is using *syntax to build semantics*: the model's elements are not mathematical objects we invented, but the very terms of the language, grouped by what the theory equates. This technique reappears throughout model theory. The completeness theorem has two major corollaries: the **compactness theorem** (if every finite subset of Γ has a model, then Γ has a model — following because any inconsistency involves finitely many axioms) and the **Löwenheim-Skolem theorem** (satisfiable theories have models of every infinite cardinality). Both follow from the completeness proof and are the engines of classical model theory. And crucially: Gödel's *Incompleteness* Theorems do not contradict completeness. Completeness says the proof system captures all *logically valid* sentences — those true in every structure. Incompleteness says that for specific theories like arithmetic, there exist sentences true in ℕ but not provable from the axioms. These are entirely different claims about entirely different levels of the metatheory.
