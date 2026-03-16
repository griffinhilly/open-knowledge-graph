---
id: polynomial-hierarchy
title: The Polynomial Hierarchy
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-np-definition
  type: hard
- id: pspace-complexity-class
  type: soft
tags:
- complexity-classes
- quantified-formulas
- hierarchy
stage: advanced
status: draft
---

# The Polynomial Hierarchy

## Core Idea
The polynomial hierarchy (PH) generalizes P and NP by permitting multiple alternations of existential (∃) and universal (∀) quantifiers in polynomial time. Σ₁^P = NP (∃-quantified), Π₁^P = coNP (∀-quantified), Σ₂^P adds ∃∀ conditions. The hierarchy is believed infinite and contained in PSPACE. If any level collapses (Σᵢ^P = Πᵢ^P), the entire hierarchy collapses to that level. PH captures all polynomial-time problems expressible with bounded quantifier depth.

## Explainer

From your study of NP, you know that NP problems have a characteristic structure: there **exists** a certificate that a polynomial-time verifier can check. Satisfiability asks "does there exist an assignment that makes this formula true?" The answer is verified deterministically once the certificate is provided. CoNP flips this to a **universal** quantifier: "for all assignments, is the formula true?" The polynomial hierarchy extends this pattern by asking: what happens when you stack these quantifiers?

The **Σ₂^P** level captures problems of the form "does there exist an x such that for all y, some polynomial-time predicate holds?" A concrete example: **minimum equivalent expression** asks whether a Boolean formula can be simplified to size at most k. This requires showing that a small formula exists (∃) and that it agrees with the original on all inputs (∀). Neither a single NP oracle call nor a single coNP oracle call suffices — you need both quantifier types working together. Each new level of the hierarchy adds another quantifier alternation: Σ₃^P has ∃∀∃ structure, Π₃^P has ∀∃∀, and so on.

A useful way to think about the hierarchy is through **oracle machines**. Σ₂^P is exactly the class of problems solvable in polynomial time by a nondeterministic Turing machine with access to an NP oracle — it can ask "is this subproblem in NP?" as a single step. Each level uses the previous level as its oracle, building a tower of increasingly powerful computational resources. The hierarchy sits entirely inside PSPACE, because a machine with polynomial space can simulate any bounded number of quantifier alternations by exhaustive search.

The most striking structural property of PH is its **fragility under collapse**. If any two adjacent levels turn out to be equal — say Σ₂^P = Π₂^P — then the entire hierarchy collapses to that level, meaning every higher level equals it too. This is analogous to how P = NP would collapse the entire hierarchy to P. The widespread belief that PH is infinite (no level collapses) is one of the strongest structural conjectures in complexity theory, and it serves as evidence for many separation results. When a complexity theorist shows that some assumption implies a collapse of PH, that assumption is generally considered unlikely — the polynomial hierarchy acts as a barometer for the plausibility of complexity-theoretic claims.
