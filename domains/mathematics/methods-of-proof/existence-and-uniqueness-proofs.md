---
id: existence-and-uniqueness-proofs
title: Existence and Uniqueness Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: predicates-and-quantifiers-intro
  type: hard
- id: proof-structure-terminology
  type: soft
tags:
- proof
- existence
- uniqueness
stage: formal-systems
status: draft
---

# Existence and Uniqueness Proofs

## Core Idea
To prove existence ('There exists x such that P(x)'), we construct or describe a specific x satisfying P. To prove uniqueness, we show that if both x and y satisfy P, then x = y. Combined in 'There exists a unique solution', these two components establish both presence and singularity, a powerful form of proof.

## Explainer

From your study of predicates and quantifiers, you know the difference between ∃x P(x) (there exists something satisfying P) and the stronger claim ∃!x P(x) (there exists exactly one thing satisfying P). Existence-and-uniqueness proofs are the standard technique for establishing this stronger claim. They always split into two parts — and understanding why each part is necessary is the first step.

**Existence** is proven by exhibiting a witness: you name a specific object and verify it satisfies P. This can be done by direct construction ("let x = ..."), by algorithm ("apply this procedure to obtain x"), or by a non-constructive argument ("one of these finitely many cases must satisfy P"). The key rule is that you must actually check that your candidate works — naming it is not enough. If you want to prove that there exists an integer x with x² = 4, you name x = 2 and verify 2² = 4. The verification is the proof.

**Uniqueness** is proven by the "assume two, show they're equal" strategy: suppose both x and y satisfy P(x) and P(y), then derive x = y. This is logically tight: if any two solutions must be equal, there can be at most one. For example, to prove that the additive identity in any group is unique, suppose both e and e′ satisfy the identity axiom. Then e = e · e′ = e′, so e = e′. The proof never assumes there is only one identity — it *proves* it by showing any two must coincide. You can also establish uniqueness by contradiction: assume x ≠ y both satisfy P, then derive an impossibility.

In practice, you will often see these proofs arise in differential equations (does a given initial value problem have a unique solution?), linear algebra (does Ax = b have a unique solution?), and optimization (is there a unique minimum?). The structure is always the same: existence tells you the problem is not vacuous, uniqueness tells you the solution is well-defined. Together they justify computing *the* solution rather than merely *a* solution — a distinction that matters whenever you need to trust that your answer is the only right one.
