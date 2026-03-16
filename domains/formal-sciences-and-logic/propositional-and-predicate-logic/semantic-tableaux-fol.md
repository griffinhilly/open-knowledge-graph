---
id: semantic-tableaux-fol
title: Semantic Tableaux (First-Order)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-semantics
  type: hard
- id: semantic-tableaux-propositional
  type: soft
builds-toward:
- fol-soundness-completeness
tags:
- tableaux
- gamma-rule
- delta-rule
- fairness
- quantifier-instantiation
stage: formal-systems
status: draft
---

# Semantic Tableaux (First-Order)

## Core Idea
First-order tableaux extend propositional tableaux with rules for quantifiers. The gamma rule (∀-elimination) instantiates a universal formula ∀x φ(x) with any term t, producing φ(t) — and crucially, the universal formula remains on the branch for future instantiations. The delta rule (∃-elimination) introduces a fresh constant c to witness ∃x φ(x), producing φ(c). A fairness condition ensures that every universal formula is eventually instantiated with every relevant term, guaranteeing completeness. An open branch in a completed fair tableau defines a countermodel, while closure of all branches proves validity.

## How It's Best Learned
Build tableaux for simple first-order arguments, carefully tracking which terms have been used for gamma-rule instantiations. Construct a countermodel from an open branch by reading off the domain elements and predicate extensions directly from the branch literals.

## Common Misconceptions
- The gamma rule can be applied infinitely many times to the same formula — this is necessary for completeness but means the procedure may not terminate.
- Delta-rule constants must be genuinely new — reusing an existing constant conflates distinct witnesses and invalidates the proof.
- Fairness is not optional — an unfair strategy can miss the instantiation needed to close all branches, making the system incomplete.

## Explainer

From your prerequisite study of propositional tableaux, you know the method: to test a formula for validity, negate it and try to build a countermodel by systematically decomposing the negation. Branches close when they contain a contradiction (a formula and its negation); if every branch closes, the original formula is valid. First-order tableaux extend this to the predicate logic you've studied in first-order semantics, but quantifiers introduce a new challenge — you can't just split on truth values, because quantifiers range over an unbounded domain.

The two quantifier rules encode the semantic meaning of ∀ and ∃ directly. The **γ rule** (universal elimination) says: if you have ∀x φ(x) on a branch, you may add φ(t) for any term t already appearing on the branch (or a fresh constant if none exist yet). Critically, the formula ∀x φ(x) *stays on the branch* — you may need to instantiate it again with different terms later. This mirrors the semantics: ∀x φ(x) is true only if φ holds for every domain element, so no single instantiation exhausts it. The **δ rule** (existential instantiation) says: from ∃x φ(x), introduce a *fresh* constant c not occurring anywhere in the tableau so far, and add φ(c). The freshness condition enforces that c is a new, arbitrary witness for the existential claim — it must not be confused with anything already named.

The **fairness condition** is what makes the procedure complete. Without it, you might keep applying the γ rule with the same term over and over while never using the term needed to close a branch. A fair strategy ensures that every universal formula ∀x φ(x) on a branch is eventually instantiated with every term that appears on that branch. This guarantees that if a branch can be closed, it will be. An **open completed fair branch** — one that cannot be closed and has been developed fairly — defines a countermodel: the domain is the set of constants appearing on the branch, and each predicate symbol P is interpreted as holding of exactly those tuples (c₁, …, cₙ) for which P(c₁, …, cₙ) appears positively on the branch.

The key difference from the propositional case is that FOL tableaux may run forever: the γ rule can generate new terms, which prompt new γ-rule applications, potentially without end. This is unavoidable — FOL validity is not decidable (by Church's theorem), so no sound and complete procedure can always terminate. What the fair tableau method provides is **semi-decidability**: if a formula is valid, the tableau closes in finitely many steps; if it is not valid, the procedure may run forever, but the open branch accumulates into a countermodel. This matches the first-order semantics you know: checking validity requires checking all interpretations, but falsifiability can be witnessed by a single (possibly infinite) model constructed step by step on the open branch.
