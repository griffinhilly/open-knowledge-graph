---
id: metalogical-properties-and-theorems
title: Metalogical Properties and Foundational Theorems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: deductive-reasoning-and-formal-proofs
  type: hard
- id: logical-consequence-and-validity
  type: hard
builds-toward:
- fol-soundness-completeness
- compactness-theorem-model-theory
- undecidability-and-godel
tags:
- metatheory
- foundational-theorems
- formal-systems
stage: formal-systems
status: draft
---

# Metalogical Properties and Foundational Theorems

## Core Idea
Metalogical theorems relate syntax and semantics. Soundness: if Γ ⊢ φ then Γ ⊨ φ. Completeness: if Γ ⊨ φ then Γ ⊢ φ. Gödel's completeness theorem (1929) establishes both for first-order logic. Other results include the Compactness Theorem, Löwenheim-Skolem Theorem, and Gödel's Incompleteness Theorems, which reveal fundamental formal system limitations.

## How It's Best Learned
Study the statements and intuitive meanings of key theorems. Understand why soundness and completeness are desirable. Explore consequences: Compactness follows from completeness; Incompleteness shows arithmetic cannot be finitely axiomatized.

## Common Misconceptions
Thinking Incompleteness Theorem means logic is broken (it reveals profound insights). Confusing logic completeness with theory completeness. Assuming that validity makes finding proofs easy (Completeness is non-constructive).

## Questions

```yaml
- question: "Gödel's 1929 Completeness Theorem establishes that for first-order logic, if Γ ⊨ φ then Γ ⊢ φ. What does this mean in plain terms?"
  type: multiple-choice
  options:
    - "Every true statement can be proved from axioms alone, without any premises"
    - "Every semantically valid argument has a formal derivation using the inference rules"
    - "Any consistent set of axioms produces only true statements"
    - "All mathematical truths can be derived from a finite set of axioms"
  answer: 1
  explanation: "Completeness (Γ ⊨ φ → Γ ⊢ φ) says: if φ is true in every model where Γ is true, then there is a formal derivation of φ from Γ using the inference rules. It connects the semantic notion of consequence (⊨) to the syntactic notion of derivability (⊢). Options A and D are much stronger claims, and Gödel's Incompleteness Theorems (a different result) specifically refute D for arithmetic. Option C describes soundness, not completeness."

- question: "Which of the following correctly distinguishes Gödel's 1929 Completeness Theorem from his 1931 Incompleteness Theorems?"
  type: multiple-choice
  options:
    - "The Completeness Theorem applies to propositional logic; Incompleteness applies to first-order logic"
    - "Completeness shows the first-order proof system derives all semantically valid arguments; Incompleteness shows axiomatic theories of arithmetic cannot prove all arithmetic truths"
    - "Both concern the same property — Incompleteness refuted what Completeness claimed"
    - "Completeness shows arithmetic is provable from axioms; Incompleteness shows those axioms are inconsistent"
  answer: 1
  explanation: "These are entirely different results about different things. The Completeness Theorem (1929) concerns the *first-order proof system itself* — the standard inference rules are sufficient to derive every semantically valid consequence. The Incompleteness Theorems (1931) concern *specific axiomatic theories of arithmetic* — no consistent, sufficiently strong arithmetic axiom system can prove all truths about natural numbers. First-order logic is complete; arithmetic as a theory is incomplete. These facts are compatible."

- question: "Soundness of a formal proof system guarantees that every provable statement is true in all models of the premises."
  type: true-false
  answer: true
  explanation: "Soundness (Γ ⊢ φ → Γ ⊨ φ) means the proof system never proves something false: if you derive φ from Γ using the inference rules, then φ is true in every model of Γ. Soundness is typically proven by verifying each inference rule preserves truth, then arguing by induction on proof length. It is the minimum requirement for a proof system to be worth using — a system that proves false things is worse than useless."

- question: "Gödel's First Incompleteness Theorem shows that the first-order logic proof system is incomplete — there are logical consequences it cannot derive."
  type: true-false
  answer: false
  explanation: "This is the key confusion to avoid. Gödel's First Incompleteness Theorem (1931) concerns *arithmetic as a theory*: any consistent, sufficiently expressive axiom system for arithmetic leaves some arithmetic truths unprovable from those axioms. It says nothing about the first-order *proof system* being incomplete. Gödel's 1929 Completeness Theorem established the opposite: the first-order proof system IS complete — every logical consequence has a formal derivation. These are different theorems about different things."

- question: "Explain in your own words why the Compactness Theorem is a surprising consequence of completeness, and give an example of what it allows you to conclude."
  type: short-answer
  answer: "Compactness says: if every finite subset of an infinite set Γ has a model, then Γ itself has a model. It's surprising because infinitely many sentences together might seem to demand more than any finite subset. One consequence: you can build non-standard models of arithmetic by adding infinitely many axioms ('there exists a number greater than 0', '...greater than 1', '...greater than 2', ...). Every finite subset is satisfiable, so by compactness the entire infinite set is satisfiable — yielding a model containing an 'infinite' natural number."
  explanation: "Compactness follows from completeness because a formal proof uses only finitely many premises. If Γ had no model, by completeness there would be a proof of a contradiction from Γ — but that finite proof uses only finitely many sentences from Γ, so some finite subset is unsatisfiable, contradicting the assumption. This finite-witnessing property means first-order logic cannot express properties like 'infinitely many' in a way that pins down infinite cardinalities — any first-order sentence true in an infinite structure is also satisfiable in non-standard models."
```

## Explainer

You already know how to construct formal proofs from premises using inference rules, and you know that logical consequence (⊨) means truth in all models. Metalogical theorems live *above* the formal system: they are mathematical theorems *about* logic, proved using ordinary mathematical reasoning, not within the formal system itself. The two most fundamental properties are **soundness** and **completeness**, and they pair like two halves of a guarantee about the relationship between syntax (proofs) and semantics (truth).

**Soundness** says the proof system never lies: if Γ ⊢ φ (φ is derivable from Γ), then Γ ⊨ φ (φ is true in every model of Γ). Proving soundness is usually straightforward — you verify that every inference rule preserves truth, then argue by induction on proof length. Soundness is a minimum bar for a proof system to be worth using: a system that proves false things is useless. **Completeness** says the proof system never misses: if Γ ⊨ φ, then Γ ⊢ φ. Gödel's 1929 completeness theorem established this for first-order logic. Completeness is surprising and non-trivial: it says that *every* semantic truth has a syntactic proof, however long.

Beyond soundness and completeness, three theorems reshape how you think about the reach of formal systems. The **Compactness Theorem** (a consequence of completeness) says: if every finite subset of Γ has a model, then Γ itself has a model. This seems obvious but is powerful — it lets you build non-standard models by adding axioms one at a time and applying compactness to the whole infinite set. The **Löwenheim-Skolem Theorem** says that any first-order theory with an infinite model has models of every infinite cardinality. Combined, these theorems imply that first-order logic cannot "pin down" a unique structure up to isomorphism — there is no first-order sentence that uniquely characterizes the natural numbers, for instance.

Gödel's **Incompleteness Theorems** (1931) are metalogical results of a different kind. They concern not the proof system for logic but the axiomatic theories of arithmetic. The first theorem says that any consistent, sufficiently strong axiom system for arithmetic is **incomplete** in the sense of *theory completeness*: there exist sentences neither provable nor refutable from the axioms. Note the distinction: this is *not* a failure of logical completeness (the proof system still derives everything that is semantically valid). It is a limitation on what any fixed set of arithmetic axioms can prove. The second theorem adds that such a system cannot prove its own consistency. These results do not mean logic is broken — they reveal a fundamental, unavoidable horizon for formal axiomatic systems.
