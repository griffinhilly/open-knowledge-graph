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

## Questions

```yaml
- question: "In a Hilbert-style proof system, you want to show that P → Q is derivable from a set of axioms Γ. The deduction theorem says this is equivalent to which proof task?"
  type: multiple-choice
  options:
    - "Showing that P and Q are both provable from Γ independently"
    - "Showing that Q is derivable from Γ together with the hypothesis P"
    - "Showing that P → Q is an axiom instance or follows from modus ponens alone"
    - "Showing that Q can be derived from P by a single application of modus ponens"
  answer: 1
  explanation: "The deduction theorem states Γ ⊢ φ → ψ if and only if Γ, φ ⊢ ψ. To prove P → Q from Γ, it suffices to assume P as a hypothesis and derive Q — a far more natural proof strategy than constructing a derivation of the implication from scratch. Option A is wrong because deriving P and Q separately says nothing about whether P implies Q. Option D is too restrictive — Q might require many steps from P, not just one modus ponens application."

- question: "A student applies the deduction theorem to convert a proof of ψ from {Γ, φ} into a proof of φ → ψ from Γ. They then conclude: 'Since I derived ψ assuming φ, I can also conclude that φ is true.' What error have they made?"
  type: multiple-choice
  options:
    - "The deduction theorem requires ψ to follow by modus ponens, not arbitrary derivation"
    - "The deduction theorem only converts the proof into φ → ψ; it says nothing about the truth of φ itself"
    - "The conclusion is valid — if ψ follows from φ, then both φ and ψ must hold"
    - "The deduction theorem cannot be applied when Γ is empty"
  answer: 1
  explanation: "The deduction theorem converts Γ, φ ⊢ ψ into Γ ⊢ φ → ψ — an implication. It says: *if* φ holds, *then* ψ follows. It does not assert that φ actually holds. The proof assumed φ as a hypothesis to derive ψ; that assumption is discharged when the implication is concluded. Confusing 'proved under assumption φ' with 'proved that φ is true' is a category error between object-level truth and meta-level derivability."

- question: "The deduction theorem is an object-level theorem — it proves a specific formula in propositional logic."
  type: true-false
  answer: false
  explanation: "The deduction theorem is a *meta-logical* result: it is a theorem *about* the ⊢ relation itself, not a formula derivable within propositional logic. It says something about the structure of proofs in a Hilbert system — specifically, that the derivability relation and the implication connective are tightly coupled. Meta-logical results like the deduction theorem, soundness, and completeness belong to a higher level of analysis than the object-language formulas they concern."

- question: "The deduction theorem compensates for the absence of a hypothesis-discharge rule in Hilbert systems by showing that any proof using hypothesis φ can be mechanically transformed into a proof of the corresponding implication."
  type: true-false
  answer: true
  explanation: "Natural deduction has the →-introduction rule, which lets you discharge a hypothesis φ and conclude φ → ψ as a primitive step. Hilbert systems have no such rule — they rely on axiom schemas and modus ponens only. The deduction theorem recovers this capability as a derived result: by induction on proof length, every step in a derivation of ψ from hypothesis φ can be 'wrapped' in the implication φ → (—), producing a proof of φ → ψ without using φ as a hypothesis. This makes Hilbert systems practically usable for reasoning about conditionals."

- question: "What does it mean to say the deduction theorem connects the 'object level' and the 'meta level' in logic, and why is this coupling significant?"
  type: short-answer
  answer: "The object level is the system of formulas and derivations within propositional logic — what can be proved. The meta level is reasoning *about* that system — properties of the ⊢ relation itself. The deduction theorem says that a meta-level fact (ψ is derivable from Γ ∪ {φ}) is equivalent to an object-level fact (the formula φ → ψ is derivable from Γ). This means the implication connective → exactly mirrors the derivability relation ⊢, so reasoning inside the logic about implications can substitute for reasoning outside it about derivability."
  explanation: "The significance is practical: it means you can prove implications by doing ordinary proofs with hypotheses, and any such proof can be mechanically converted into a proof of the implication. This coupling is so natural that systems like natural deduction build it in as a primitive rule. In Hilbert systems, the deduction theorem restores this capability as a derived result, making the otherwise austere Hilbert proof system usable for everyday conditional reasoning."
```

## Explainer

You have worked with Hilbert-style proof systems, where proofs are finite sequences of formulas each of which is either an axiom instance or follows from two earlier formulas by modus ponens. These systems are economical in rules but expensive in effort: to derive ψ from a hypothesis φ, you must somehow incorporate φ into the derivation, but there is no rule for "assume φ and see what follows." The **deduction theorem** bridges this gap: it says that Γ, φ ⊢ ψ (ψ is derivable from Γ with hypothesis φ) if and only if Γ ⊢ φ → ψ (the implication φ → ψ is derivable from Γ alone). Inferring one direction from the other converts hypothesis-based reasoning into reasoning about implications.

The proof is an induction on the length of the derivation of ψ from Γ ∪ {φ}. Three base cases arise. If ψ *is* φ, then Γ ⊢ φ → φ — this requires a short but non-trivial derivation using the Hilbert axiom schemas, not just modus ponens. If ψ is an axiom instance or a member of Γ, then ψ is already provable from Γ alone, and from ψ you can derive φ → ψ directly using the axiom schema "ψ → (φ → ψ)." The inductive case is modus ponens: if ψ was obtained from some χ and χ → ψ already in the derivation, the inductive hypothesis gives Γ ⊢ φ → χ and Γ ⊢ φ → (χ → ψ), and from these two implications the axiom schema for hypothetical syllogism yields Γ ⊢ φ → ψ. Every step in the original derivation can be "wrapped" in φ → (—).

The deduction theorem is a **meta-logical** result: it says something about the ⊢ relation itself, not about any specific formula. The relationship it encodes — that the turnstile and the implication connective → are tightly coupled — is so natural that many proof systems build it in directly. Natural deduction's **→-introduction rule** lets you discharge a hypothesis φ and conclude φ → ψ as a primitive inference step. The deduction theorem compensates for the absence of this rule in Hilbert systems by recovering it as a derived theorem about the system.

The practical import is substantial. Without the deduction theorem, to prove φ → (ψ → χ) in a Hilbert system you would need to construct a proof of χ from nothing but axioms while somehow incorporating both φ and ψ. With the deduction theorem, it suffices to assume φ and ψ as hypotheses and prove χ — a far more natural goal that admits the usual reasoning style. Every nested implication φ → (ψ → (χ → ...)) can be proved by peeling off hypotheses one at a time, proving the innermost formula, and then invoking the deduction theorem to re-wrap them. This conversion between "proof with hypotheses" and "proof of implication" is the formal justification for the natural-language move "assume φ; then...therefore χ; hence φ → χ."
