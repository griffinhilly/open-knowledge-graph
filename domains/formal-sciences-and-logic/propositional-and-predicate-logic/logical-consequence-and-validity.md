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

## Explainer

From satisfaction in structures, you know what it means for a formula φ to be true in a structure M under an assignment s: written M ⊨ φ[s], this is defined recursively by the semantics of connectives and quantifiers. With that foundation, you can define the central semantic notions of logic. A formula φ is **satisfiable** if there exists some structure M and assignment s such that M ⊨ φ[s]. A formula is **valid** (also called a **tautology** or **logically true**) if it is true in every structure under every assignment — no counterexample exists. Validity is the strongest semantic property a formula can have.

**Logical consequence** lifts these notions to sets of formulas. A set of premises Γ **semantically entails** a conclusion φ, written Γ ⊨ φ, if every structure that satisfies all formulas in Γ also satisfies φ. Equivalently, there is no structure in which all premises are true but the conclusion is false — every model of Γ is automatically a model of φ. This is the semantic definition of "follows necessarily from": if you accept all the premises, you must accept the conclusion, because rejecting the conclusion would force you to reject at least one premise. Note that φ is valid if and only if ∅ ⊨ φ — the empty set of premises entails φ — because a valid formula is true in every structure, with no premises required.

The key proof strategy for establishing Γ ⊨ φ is to show that any structure satisfying Γ has no choice but to satisfy φ. The key refutation strategy — showing Γ ⊭ φ — is to **construct a countermodel**: a specific structure M in which every formula of Γ is true and φ is false. Finding a countermodel is often easier than proving entailment, because you're constructing a concrete object. For example, to show that ∃x P(x) does not entail ∀x P(x), take the structure with domain {a, b} where P(a) holds but P(b) does not: the premise is satisfied (something has P) but the conclusion fails (not everything has P). One countermodel suffices to refute a claimed entailment.

**Gödel's Completeness Theorem** (1930) ties the semantic notion Γ ⊨ φ to the syntactic notion Γ ⊢ φ (provability from Γ using a formal deductive system). The theorem states that these two notions coincide for first-order logic: Γ ⊨ φ if and only if Γ ⊢ φ. **Soundness** (⊢ implies ⊨) is the easier direction: every inference rule preserves truth, so anything provable is semantically true. **Completeness** (⊨ implies ⊢) is the deep direction: if φ is a semantic consequence of Γ, then there exists a finite formal proof of φ from Γ. This means first-order logic has no semantic "gaps" — nothing is entailed that cannot also be proved. The completeness theorem underpins the entire use of proof systems as a tool for semantic reasoning, and it is what distinguishes first-order logic from higher-order logics, for which completeness fails.
