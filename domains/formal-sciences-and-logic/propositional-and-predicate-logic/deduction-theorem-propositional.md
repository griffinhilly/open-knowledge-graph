---
id: deduction-theorem-propositional
title: Deduction Theorem for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
- id: hilbert-system-propositional
  type: hard
tags:
- propositional-logic
- deduction
- meta-logic
stage: formal-systems
status: draft
---

# Deduction Theorem for Propositional Logic

## Core Idea
The deduction theorem states that Γ, φ ⊢ ψ if and only if Γ ⊢ φ → ψ. This meta-logical result connects object-level deduction to the implication connective, allowing us to reduce proofs involving hypotheses to proofs of implications.

## Explainer

You have worked with Hilbert-style proof systems, where proofs are finite sequences of formulas each of which is either an axiom instance or follows from two earlier formulas by modus ponens. These systems are economical in rules but expensive in effort: to derive ψ from a hypothesis φ, you must somehow incorporate φ into the derivation, but there is no rule for "assume φ and see what follows." The **deduction theorem** bridges this gap: it says that Γ, φ ⊢ ψ (ψ is derivable from Γ with hypothesis φ) if and only if Γ ⊢ φ → ψ (the implication φ → ψ is derivable from Γ alone). Inferring one direction from the other converts hypothesis-based reasoning into reasoning about implications.

The proof is an induction on the length of the derivation of ψ from Γ ∪ {φ}. Three base cases arise. If ψ *is* φ, then Γ ⊢ φ → φ — this requires a short but non-trivial derivation using the Hilbert axiom schemas, not just modus ponens. If ψ is an axiom instance or a member of Γ, then ψ is already provable from Γ alone, and from ψ you can derive φ → ψ directly using the axiom schema "ψ → (φ → ψ)." The inductive case is modus ponens: if ψ was obtained from some χ and χ → ψ already in the derivation, the inductive hypothesis gives Γ ⊢ φ → χ and Γ ⊢ φ → (χ → ψ), and from these two implications the axiom schema for hypothetical syllogism yields Γ ⊢ φ → ψ. Every step in the original derivation can be "wrapped" in φ → (—).

The deduction theorem is a **meta-logical** result: it says something about the ⊢ relation itself, not about any specific formula. The relationship it encodes — that the turnstile and the implication connective → are tightly coupled — is so natural that many proof systems build it in directly. Natural deduction's **→-introduction rule** lets you discharge a hypothesis φ and conclude φ → ψ as a primitive inference step. The deduction theorem compensates for the absence of this rule in Hilbert systems by recovering it as a derived theorem about the system.

The practical import is substantial. Without the deduction theorem, to prove φ → (ψ → χ) in a Hilbert system you would need to construct a proof of χ from nothing but axioms while somehow incorporating both φ and ψ. With the deduction theorem, it suffices to assume φ and ψ as hypotheses and prove χ — a far more natural goal that admits the usual reasoning style. Every nested implication φ → (ψ → (χ → ...)) can be proved by peeling off hypotheses one at a time, proving the innermost formula, and then invoking the deduction theorem to re-wrap them. This conversion between "proof with hypotheses" and "proof of implication" is the formal justification for the natural-language move "assume φ; then...therefore χ; hence φ → χ."
