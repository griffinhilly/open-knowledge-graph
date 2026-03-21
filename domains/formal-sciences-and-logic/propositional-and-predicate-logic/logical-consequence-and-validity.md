---
id: logical-consequence-and-validity
title: Logical Consequence and Validity
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: satisfaction-in-structures
  type: hard
- id: logical-implication-entailment
  type: soft
builds-toward:
- fol-soundness-completeness
- model-theory-basics
tags:
- semantics
- entailment
- first-order-logic
stage: formal-systems
status: draft
---

# Logical Consequence and Validity

## Core Idea
Γ semantically entails φ (Γ ⊨ φ) if every structure satisfying all formulas in Γ also satisfies φ. A formula is valid if it is entailed by the empty set—true in every structure. Gödel's completeness theorem establishes that syntactic consequence (provability) equals semantic consequence for first-order logic.

## How It's Best Learned
Build counterexamples to refute proposed consequences. Identify valid formulas (like ∀x (P(x) → P(x))) and satisfiable-but-invalid formulas.

## Questions

```yaml
- question: "Someone claims that ∃x P(x) semantically entails ∀x P(x). What is the most direct way to show this claim is FALSE?"
  type: multiple-choice
  options:
    - "Prove that ∀x P(x) is not a tautology using a truth table"
    - "Construct a structure with a domain where ∃x P(x) is true and ∀x P(x) is false"
    - "Show that the inference violates a rule of the formal deduction system"
    - "Demonstrate that ∃x P(x) is satisfiable but not valid"
  answer: 1
  explanation: "To refute a claimed entailment Γ ⊭ φ, you construct a countermodel: a specific structure M in which every formula of Γ is true and φ is false. For this case: take a domain {a, b} where P holds of a but not of b. Then ∃x P(x) is true (a witnesses it) but ∀x P(x) is false (b fails it). One countermodel suffices. Option A (truth table) applies to propositional logic, not FOL. Option C is a syntactic approach — the task asks for semantic refutation. Option D is true but doesn't directly refute the entailment claim."

- question: "Which of the following correctly describes a valid formula in first-order logic?"
  type: multiple-choice
  options:
    - "A formula that is true in some structure under some assignment"
    - "A formula that is provable from at least one consistent set of premises"
    - "A formula that is true in every structure under every variable assignment"
    - "A formula whose negation is unsatisfiable in standard models only"
  answer: 2
  explanation: "A valid formula (also called a logical truth or tautology in FOL) is one that is true in every structure under every assignment — there is no possible counterexample. Option A describes satisfiability, not validity. Option B is weaker than validity and misdescribes it — a formula provable from some premises need not be valid. Option D is almost right (a formula is valid iff its negation is unsatisfiable), but the qualifier 'in standard models only' makes it incorrect. Validity has no model-theoretic restrictions of that kind in standard FOL semantics."

- question: "If Γ semantically entails φ, then φ must itself be a valid formula — true in every structure."
  type: true-false
  answer: false
  explanation: "This is a subtle but important error. Γ ⊨ φ means every model of Γ is also a model of φ — but φ might only be true in models where Γ holds. φ need not be true in all structures. For example: {∀x P(x)} ⊨ P(a) — if everything has P, then a has P. But P(a) is not valid — there are structures where a does not have P (specifically, any structure where P(a) is false, which also fails to satisfy the premise ∀x P(x)). Validity requires truth in every structure with no premises; entailment only requires truth in every structure that satisfies the premises."

- question: "A formula φ is valid if and only if the empty set of premises semantically entails it (∅ ⊨ φ)."
  type: true-false
  answer: true
  explanation: "This biconditional captures the relationship between validity and entailment precisely. ∅ ⊨ φ means every structure satisfying all formulas in the empty set also satisfies φ. But every structure vacuously satisfies the empty set of premises (there are no conditions to fail). So ∅ ⊨ φ holds exactly when φ is true in every structure under every assignment — which is the definition of validity. This shows that validity is a special case of entailment: entailment from nothing at all."

- question: "What does Gödel's Completeness Theorem establish about first-order logic, and why is this result surprising or non-trivial?"
  type: short-answer
  answer: "Gödel's Completeness Theorem (1930) establishes that syntactic provability (Γ ⊢ φ) and semantic consequence (Γ ⊨ φ) coincide for first-order logic: Γ ⊨ φ if and only if Γ ⊢ φ. Soundness (⊢ implies ⊨) is relatively straightforward — each inference rule preserves truth. The deep direction is completeness (⊨ implies ⊢): if φ is semantically entailed by Γ, then there exists a finite formal proof of φ from Γ. This is non-trivial because semantic consequence is defined over all possible structures — an infinite, uncountable class — while a formal proof is a finite syntactic object. The theorem says these two independently defined notions leave no gaps between them in FOL."
  explanation: "The theorem fails for higher-order logics (second-order logic is not complete), which is why FOL occupies a privileged position in mathematical logic. In second-order logic, there are semantic consequences that cannot be captured by any finite proof system. Completeness for FOL means that proof systems are not merely convenient tools — they are provably adequate for all semantic reasoning in that logic."
```

## Explainer

From satisfaction in structures, you know what it means for a formula φ to be true in a structure M under an assignment s: written M ⊨ φ[s], this is defined recursively by the semantics of connectives and quantifiers. With that foundation, you can define the central semantic notions of logic. A formula φ is **satisfiable** if there exists some structure M and assignment s such that M ⊨ φ[s]. A formula is **valid** (also called a **tautology** or **logically true**) if it is true in every structure under every assignment — no counterexample exists. Validity is the strongest semantic property a formula can have.

**Logical consequence** lifts these notions to sets of formulas. A set of premises Γ **semantically entails** a conclusion φ, written Γ ⊨ φ, if every structure that satisfies all formulas in Γ also satisfies φ. Equivalently, there is no structure in which all premises are true but the conclusion is false — every model of Γ is automatically a model of φ. This is the semantic definition of "follows necessarily from": if you accept all the premises, you must accept the conclusion, because rejecting the conclusion would force you to reject at least one premise. Note that φ is valid if and only if ∅ ⊨ φ — the empty set of premises entails φ — because a valid formula is true in every structure, with no premises required.

The key proof strategy for establishing Γ ⊨ φ is to show that any structure satisfying Γ has no choice but to satisfy φ. The key refutation strategy — showing Γ ⊭ φ — is to **construct a countermodel**: a specific structure M in which every formula of Γ is true and φ is false. Finding a countermodel is often easier than proving entailment, because you're constructing a concrete object. For example, to show that ∃x P(x) does not entail ∀x P(x), take the structure with domain {a, b} where P(a) holds but P(b) does not: the premise is satisfied (something has P) but the conclusion fails (not everything has P). One countermodel suffices to refute a claimed entailment.

**Gödel's Completeness Theorem** (1930) ties the semantic notion Γ ⊨ φ to the syntactic notion Γ ⊢ φ (provability from Γ using a formal deductive system). The theorem states that these two notions coincide for first-order logic: Γ ⊨ φ if and only if Γ ⊢ φ. **Soundness** (⊢ implies ⊨) is the easier direction: every inference rule preserves truth, so anything provable is semantically true. **Completeness** (⊨ implies ⊢) is the deep direction: if φ is a semantic consequence of Γ, then there exists a finite formal proof of φ from Γ. This means first-order logic has no semantic "gaps" — nothing is entailed that cannot also be proved. The completeness theorem underpins the entire use of proof systems as a tool for semantic reasoning, and it is what distinguishes first-order logic from higher-order logics, for which completeness fails.
