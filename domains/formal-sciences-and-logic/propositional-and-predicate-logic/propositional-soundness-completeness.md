---
id: propositional-soundness-completeness
title: Soundness and Completeness of Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: natural-deduction-propositional
  type: hard
- id: tautologies-and-contradictions
  type: hard
- id: sequent-calculus-intro
  type: soft
- id: mathematical-proof-strategies
  type: soft
builds-toward:
- propositional-compactness
- fol-soundness-completeness
tags:
- soundness
- completeness
- proof-theory
- model-theory
- metatheorem
stage: formal-systems
status: validated
---
# Soundness and Completeness of Propositional Logic

## Core Idea
Soundness means that every formula provable in the proof system is semantically valid: if ⊢ φ then ⊨ φ. Completeness is the converse: every valid formula is provable: if ⊨ φ then ⊢ φ. Together they establish that syntax and semantics perfectly align — proof and truth coincide for propositional logic. Soundness is proved by verifying each inference rule preserves validity. Completeness is proved by showing that any consistent set of formulas has a model (the Lindenbaum–Henkin construction is one approach). These two results certify that the proof system is neither too weak nor too strong.

## How It's Best Learned
Prove soundness first by structural induction on derivations. Then study the completeness proof as an example of the Lindenbaum lemma. See how each direction fails if rules are added or removed.

## Common Misconceptions
- Completeness does not mean 'every truth is provable in general' — it means every logically valid formula is provable.
- A system can be sound but incomplete (missing rules), or complete but unsound (too many rules admitting false conclusions).

## Questions

```yaml
- question: "Which statement correctly distinguishes soundness from completeness for propositional logic?"
  type: multiple-choice
  options:
    - "Soundness: every valid formula is provable (⊨ φ ⟹ ⊢ φ); Completeness: every provable formula is valid (⊢ φ ⟹ ⊨ φ)"
    - "Soundness: every provable formula is valid (⊢ φ ⟹ ⊨ φ); Completeness: every valid formula is provable (⊨ φ ⟹ ⊢ φ)"
    - "Soundness and completeness are the same property stated in different terms"
    - "Soundness concerns the axioms; completeness concerns the inference rules"
  answer: 1
  explanation: "Soundness goes from syntax to semantics: if you can derive φ (⊢ φ), then φ is logically valid (⊨ φ). It says the proof system never proves falsehoods. Completeness goes from semantics to syntax: if φ is logically valid (⊨ φ), then it is provable (⊢ φ). It says the proof system never misses a truth. The two directions are converses, not the same claim."

- question: "A proof system for propositional logic that includes most valid natural deduction rules plus additional rules that derive some non-tautologies is very likely to be complete."
  type: true-false
  answer: false
  explanation: "Adding rules that derive non-tautologies breaks soundness — the system can now prove formulas that are not valid. A system can only be meaningfully 'complete' if it is also sound; an unsound system trivially 'proves' everything (including contradictions) and the notion of completeness loses its meaning. Completeness is only a virtue in the context of a sound system."

- question: "Why is it necessary to prove both soundness AND completeness, rather than just one of them?"
  type: short-answer
  answer: "Soundness alone guarantees the proof system is trustworthy (no false theorems) but leaves open that some valid formulas may be unprovable — the system could be too weak. Completeness alone guarantees no valid formula is missed but does not prevent the system from also proving invalid formulas — it could be too permissive. Together they establish a perfect correspondence: ⊢ φ if and only if ⊨ φ. The proof system is neither too weak nor too strong — it captures exactly the valid formulas."
  explanation: "The joint result ⊢ φ ⟺ ⊨ φ means that provability and logical truth coincide. This is what makes the proof system a reliable decision procedure for validity: you can work entirely syntactically (manipulating symbols) and be guaranteed your conclusions match semantic reality (truth under all assignments)."
```

## Explainer

Throughout your study of propositional logic you have been working with two different notions of "correctness." On the **semantic** side, ⊨ φ means φ is a tautology — true under every truth-value assignment. On the **syntactic** side, ⊢ φ means φ is derivable using the rules of your proof system (natural deduction, sequent calculus, or another system). These are defined completely independently: semantics is about truth tables; syntax is about symbol manipulation. The questions of soundness and completeness ask whether these two notions align.

**Soundness** (⊢ φ ⟹ ⊨ φ) says: the proof system never proves a falsehood. Every formula you can derive is indeed a tautology. Proving soundness is typically a structural induction on derivations: you verify that the *axiom schemas* are all tautologies (base case) and that each *inference rule* preserves validity (inductive step). For example, modus ponens: if φ and φ → ψ are both valid, then ψ must be valid, because in any assignment where φ → ψ is true and φ is true, ψ must be true. Checking each rule this way establishes that no derivation can ever produce a non-tautology.

**Completeness** (⊨ φ ⟹ ⊢ φ) says: the proof system misses nothing. Every tautology has a proof. This is harder to prove because you must show an arbitrary tautology — of which there are infinitely many — has a derivation. One classical approach uses the **Lindenbaum lemma**: starting from the assumption that ¬φ is consistent (i.e., that φ is not provable), you construct a maximal consistent extension that becomes a model for ¬φ. If you successfully build such a model, you have shown ¬φ is satisfiable, which means φ is not a tautology — contrapositive gives you completeness. For propositional logic, a more direct approach uses truth-table methods to systematically construct proofs from a formula's structure.

It is instructive to consider what each property alone is worth. A proof system with only the rule "derive ⊤" (top) is sound — it only proves the tautology ⊤ — but it is extremely incomplete. A proof system with the additional rule "from any formula, derive any formula" is complete (trivially, everything is provable) but catastrophically unsound. Neither property is useful without the other. Together, soundness and completeness say that the proof system is a *faithful representation* of logical truth — you can safely replace semantic reasoning with syntactic proof.

This result matters because proofs are **finitary and mechanical**: a derivation is a finite object you can write down and check by algorithm. Tautologies, by contrast, are defined over all possible truth assignments — potentially an infinite check. Completeness tells you that the finite syntactic world of proofs and the infinite semantic world of models nevertheless agree perfectly. This equivalence is what justifies using formal proof systems as the foundation of mathematics and formal verification.


