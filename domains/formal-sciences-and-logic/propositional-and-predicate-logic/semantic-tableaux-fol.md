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

## Questions

```yaml
- question: "You are building a first-order tableau and encounter ∃x P(x) on a branch. Constants a and b already appear on the branch. How should you correctly apply the δ rule?"
  type: multiple-choice
  options:
    - "Add P(a) and remove ∃x P(x) from the branch, since a is already present"
    - "Add P(b) because b is the most recently introduced constant"
    - "Introduce a fresh constant c (not appearing anywhere in the tableau) and add P(c)"
    - "Add both P(a) and P(b) to cover all existing constants"
  answer: 2
  explanation: "The δ rule requires a *fresh* constant — one that does not appear anywhere in the tableau. This freshness condition enforces that c is an arbitrary, unnamed witness for the existential claim. If you reuse an existing constant like a, you are asserting that the thing satisfying P(x) is the same object as a, which is unjustified and could conflate distinct witnesses, invalidating the proof. The δ rule is applied once per existential formula on a branch; the formula can then be set aside (unlike the γ rule)."

- question: "You run a fair tableau procedure on a first-order formula φ. After many rule applications, the procedure has not terminated. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "φ is definitely invalid (satisfiable), because valid formulas always terminate quickly"
    - "φ is definitely valid, because an infinite procedure indicates completeness searching"
    - "Non-termination is expected for invalid formulas; the open branches accumulating on the tableau are building a countermodel, but we cannot yet conclude anything definitive"
    - "The procedure has a bug — a correct fair tableau procedure always terminates"
  answer: 2
  explanation: "FOL validity is not decidable (Church's theorem), so no sound and complete procedure can always terminate. The fair tableau method is *semi-decidable*: if φ is valid, the tableau closes in finitely many steps; if φ is invalid, the procedure may run forever as the γ rule generates new terms requiring new instantiations. Non-termination does not prove invalidity — it only means we haven't yet found either a proof or a finite countermodel. The open branches are building toward a countermodel, but we cannot conclude invalidity without a completed open branch."

- question: "After applying the γ rule to ∀x φ(x) on a branch, the formula ∀x φ(x) must remain on the branch for potential future instantiations."
  type: true-false
  answer: true
  explanation: "This is the defining feature of the γ rule and what distinguishes it from the δ rule. A universal formula ∀x φ(x) says φ holds for *every* domain element — no single instantiation exhausts it. You may need to instantiate it with different terms as new constants are introduced by δ-rule applications. If you removed ∀x φ(x) after one instantiation, you would lose the ability to use it again, making the procedure incomplete. The δ rule, by contrast, is applied once — the fresh constant witnesses the existential claim, and the formula can be retired."

- question: "A completed fair tableau with at least one open branch proves that the original formula (before negation) is not valid, because the open branch defines a countermodel."
  type: true-false
  answer: true
  explanation: "Soundness of the tableau method guarantees this: if every branch were closable, the formula would be valid. An open completed fair branch contains no contradiction and has been fully developed — every universal formula has been instantiated with every relevant term. Reading off the branch: the domain is the set of constants appearing on the branch, and each predicate P is true of exactly the tuples for which P(c₁,...,cₙ) appears positively on the branch. This interpretation satisfies the negation of the original formula, meaning the original formula is false in that interpretation — a genuine countermodel."

- question: "Why is the fairness condition necessary for the completeness of first-order tableaux? What could go wrong without it?"
  type: short-answer
  answer: "Without fairness, the procedure might repeatedly instantiate one universal formula while ignoring another, or use only old constants and never the fresh ones introduced by δ applications. This could leave a branch open indefinitely even though it should close — the procedure would fail to find the required instantiation."
  explanation: "Concretely: suppose a branch has ∀x ∀y R(x,y) and an existential introduces fresh constant c. A strategy that only ever instantiates ∀x ∀y R(x,y) with the original constant a would never produce R(c, a) or R(a, c), which might be exactly what is needed to close the branch. Fairness requires that every universal formula be eventually instantiated with every term on the branch, including those introduced later by δ applications. Without this guarantee, the tableau is sound but not complete — it can prove valid formulas valid, but may fail to close branches that should close."
```

## Explainer

From your prerequisite study of propositional tableaux, you know the method: to test a formula for validity, negate it and try to build a countermodel by systematically decomposing the negation. Branches close when they contain a contradiction (a formula and its negation); if every branch closes, the original formula is valid. First-order tableaux extend this to the predicate logic you've studied in first-order semantics, but quantifiers introduce a new challenge — you can't just split on truth values, because quantifiers range over an unbounded domain.

The two quantifier rules encode the semantic meaning of ∀ and ∃ directly. The **γ rule** (universal elimination) says: if you have ∀x φ(x) on a branch, you may add φ(t) for any term t already appearing on the branch (or a fresh constant if none exist yet). Critically, the formula ∀x φ(x) *stays on the branch* — you may need to instantiate it again with different terms later. This mirrors the semantics: ∀x φ(x) is true only if φ holds for every domain element, so no single instantiation exhausts it. The **δ rule** (existential instantiation) says: from ∃x φ(x), introduce a *fresh* constant c not occurring anywhere in the tableau so far, and add φ(c). The freshness condition enforces that c is a new, arbitrary witness for the existential claim — it must not be confused with anything already named.

The **fairness condition** is what makes the procedure complete. Without it, you might keep applying the γ rule with the same term over and over while never using the term needed to close a branch. A fair strategy ensures that every universal formula ∀x φ(x) on a branch is eventually instantiated with every term that appears on that branch. This guarantees that if a branch can be closed, it will be. An **open completed fair branch** — one that cannot be closed and has been developed fairly — defines a countermodel: the domain is the set of constants appearing on the branch, and each predicate symbol P is interpreted as holding of exactly those tuples (c₁, …, cₙ) for which P(c₁, …, cₙ) appears positively on the branch.

The key difference from the propositional case is that FOL tableaux may run forever: the γ rule can generate new terms, which prompt new γ-rule applications, potentially without end. This is unavoidable — FOL validity is not decidable (by Church's theorem), so no sound and complete procedure can always terminate. What the fair tableau method provides is **semi-decidability**: if a formula is valid, the tableau closes in finitely many steps; if it is not valid, the procedure may run forever, but the open branch accumulates into a countermodel. This matches the first-order semantics you know: checking validity requires checking all interpretations, but falsifiability can be witnessed by a single (possibly infinite) model constructed step by step on the open branch.
