---
id: deductive-reasoning-and-formal-proofs
title: Deductive Reasoning and Formal Proof Systems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-implication-entailment
  type: soft
- id: mathematical-proof-strategies
  type: soft
- id: mathematical-induction
  type: soft
- id: soundness-theorem-proof-systems
  type: soft
builds-toward:
- natural-deduction-propositional
- natural-deduction-fol
- resolution-fol
- sequent-calculus-intro
tags:
- proof-theory
- inference
- deduction
stage: formal-systems
status: validated
---
# Deductive Reasoning and Formal Proof Systems

## Core Idea
Deductive reasoning formalizes proving conclusions from premises using explicit inference rules. A proof system defines axioms and rules that allow deriving new formulas from given ones. A formula is provable from Γ (Γ ⊢ φ) if there exists a finite derivation sequence using the rules.

## How It's Best Learned
Study concrete proof systems and practice constructing proofs. Compare different systems (natural deduction is intuitive; sequent calculus is systematic; resolution is computational). Understand the syntactic/semantic distinction.

## Common Misconceptions
Thinking proof systems are purely mechanical. Confusing a proof of φ with proof that φ is true. Assuming different systems prove different theorems (Completeness Theorem shows they do not for first-order logic).

## Questions

```yaml
- question: "The Completeness Theorem for first-order logic states which of the following?"
  type: multiple-choice
  options:
    - "Every first-order sentence is either provable or its negation is provable"
    - "If Γ ⊢ φ, then Γ ⊨ φ — every formally derivable statement is semantically valid"
    - "If Γ ⊨ φ, then Γ ⊢ φ — every semantically valid statement has a formal proof"
    - "Every proof can be reduced to a finite sequence of applications of modus ponens"
  answer: 2
  explanation: "Completeness is the direction ⊨ implies ⊢: if φ is a semantic consequence of Γ (true in every model that satisfies Γ), then there exists a formal derivation of φ from Γ. This is the deep and surprising direction — it says the syntactic machinery of proof systems is powerful enough to capture all of semantic truth for first-order logic. Option B describes soundness (the easy direction: provable implies valid). Option A is a different property (completeness for a specific logic like classical propositional logic, but not what the theorem says)."

- question: "A researcher switches from natural deduction to resolution calculus hoping it will let her prove theorems that natural deduction could not. What does the Completeness Theorem tell us about this hope?"
  type: multiple-choice
  options:
    - "Resolution is indeed more powerful for first-order logic because it works on clausal normal form"
    - "Natural deduction is more powerful because it directly mirrors mathematical reasoning"
    - "Both systems prove exactly the same theorems for first-order logic — the choice affects proof style and computational efficiency, not which sentences are provable"
    - "Resolution can prove more sentences for decidable fragments, but natural deduction wins on undecidable ones"
  answer: 2
  explanation: "The Completeness Theorem guarantees that all sound and complete proof systems for first-order logic prove exactly the same sentences. Natural deduction, sequent calculus, Hilbert-style axiom systems, and resolution all derive the same theorems — because they all prove exactly the semantically valid consequences of the premises. Switching systems changes how proofs look and how efficiently they can be found by algorithms, but not what can be proved in principle."

- question: "Soundness of a proof system means that if Γ ⊢ φ (φ is formally derivable from Γ), then Γ ⊨ φ (φ is a semantic consequence of Γ)."
  type: true-false
  answer: true
  explanation: "True. Soundness is the 'correctness' direction: the proof system never derives false conclusions from true premises. Every inference rule in a sound system preserves semantic truth, so any chain of rule applications starting from valid premises produces a valid conclusion. Soundness is usually straightforward to prove by checking each rule individually. Completeness — the reverse direction — is what requires deep work."

- question: "A formal proof of φ from premises Γ establishes that φ is absolutely true in most possible worlds, regardless of whether Γ is true."
  type: true-false
  answer: false
  explanation: "False. A proof of φ from Γ establishes a conditional: if Γ is true, then φ must be true. The proof is valid (as a derivation) even if Γ contains false premises — the logical machinery makes no assumptions about whether premises are true. If you want to conclude φ is absolutely true (a tautology), you need Γ to be empty and φ to be provable from no premises at all. Formal proof is about inference, not certification of absolute truth — it guarantees that truth is preserved from premises to conclusion, nothing more."

- question: "What is the difference between soundness and completeness of a proof system, and which direction is more surprising and harder to prove?"
  type: short-answer
  answer: "Soundness (⊢ implies ⊨): everything the proof system can derive is actually semantically valid — the system makes no mistakes. Completeness (⊨ implies ⊢): everything semantically valid can be derived — the system misses nothing. Completeness is the surprising and hard direction. Soundness can be verified by checking that each inference rule preserves truth. Completeness requires showing that for every semantic consequence, there exists a finite formal derivation — a non-constructive existence proof. Gödel's 1929 completeness theorem established this for first-order logic, making it a landmark result. His later incompleteness theorems then showed that sufficiently strong formal systems (like arithmetic) cannot be both consistent and complete."
  explanation: "The slogan: soundness says 'you can't prove false things'; completeness says 'you can prove all true things.' The surprising one is completeness — it is far from obvious that the finite syntactic game of proof can capture all of infinite semantic truth."
```

## Explainer

You already understand logical implication: Γ ⊨ φ means every interpretation that satisfies all formulas in Γ also satisfies φ. That is a **semantic** notion — it talks about truth in models. A **proof system** introduces a parallel **syntactic** notion: Γ ⊢ φ means φ can be derived from Γ by applying a finite sequence of explicit rules, without ever asking what is "true." The relationship between ⊨ and ⊢ is the central question of proof theory.

A proof system has two components: **axioms** (formulas taken as given) and **inference rules** (patterns like "from formula A and formula A → B, derive B" — this particular rule is called modus ponens). A **proof** of φ from Γ is a finite sequence of formulas where each step is either an axiom, a member of Γ, or the result of applying an inference rule to earlier steps. The last formula in the sequence is φ. This is entirely syntactic: you can verify a proof by checking, line by line, that each step is licensed — no semantic judgment required.

Different proof systems — **natural deduction**, **sequent calculus**, **Hilbert-style axiom systems**, **resolution** — differ in how they organize the same logical machinery. Natural deduction mirrors mathematical practice: it has introduction and elimination rules for each connective (∧-introduction, →-elimination = modus ponens, etc.), and proofs look like the reasoning a mathematician actually writes. Sequent calculus uses a different format (Γ ⊢ Δ, asserting that not all of Γ can be true while all of Δ are false) and is more symmetric and algorithmic. Hilbert-style systems push almost everything into axioms and use very few rules. Resolution (your prerequisite for CNF) is designed for automated theorem proving.

The **Completeness Theorem** for first-order logic states that these systems all prove exactly the same theorems: Γ ⊢ φ if and only if Γ ⊨ φ. Provability and semantic consequence coincide. This is not trivially obvious — it is a deep theorem (proved by Gödel in 1929) that guarantees proof systems are not missing anything. **Soundness** (⊢ implies ⊨) is the easy direction: if you can prove φ from Γ, then φ really follows from Γ. **Completeness** (⊨ implies ⊢) is the hard direction: if φ follows semantically, then there is always a formal proof. Together they mean the syntactic game of proof and the semantic game of truth are perfectly matched — for first-order logic. (Gödel's *incompleteness* theorems, which you will encounter later, show arithmetic is a different story.)
