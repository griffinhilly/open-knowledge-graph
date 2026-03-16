---
id: counterexamples-and-disproofs
title: Counterexamples and Disproofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: predicates-and-quantifiers-intro
  type: hard
- id: proof-structure-terminology
  type: soft
tags:
- proof
- counterexample
- negation
stage: formal-systems
status: draft
---

# Counterexamples and Disproofs

## Core Idea
To disprove a universal statement 'For all x, P(x)', we need only find a single counterexample where P(x) is false. A counterexample is a concrete instance proving the statement false. Disproofs by counterexample are often simpler than constructing positive proofs and are the primary tool for showing that conjectures are false.

## Explainer

From predicates and quantifiers, you know that a universal statement "For all x, P(x)" makes a sweeping claim — it must hold for every element in the domain. This creates a profound asymmetry: to prove such a statement true, you must account for every case; to prove it false, one case suffices. A **counterexample** is a single element c for which P(c) is false, and its existence immediately establishes ∃x ¬P(x) — the logical negation of the universal. Finding that single element is the entire disproof.

The strategy for finding counterexamples is guided by the structure of the claim. Extreme and degenerate cases are often the most productive starting points: 0 and 1 in arithmetic (does this property hold for the multiplicative identity?), the empty set in combinatorics, the zero vector in linear algebra, a constant function in analysis, a disconnected graph in graph theory. Many universal claims that seem plausible in the typical case fail at the boundary. The claim "every continuous function is differentiable" sounds reasonable, but f(x) = |x| is continuous everywhere and fails to be differentiable at exactly one point — x = 0 — which is all that is needed to disprove it.

A well-constructed counterexample is minimal and targeted. It directly violates the predicate with as little extraneous structure as possible. If the claim is "all primes are odd," the counterexample is 2 — not a long argument about even composites. Once found, the logical form of the disproof is always the same: exhibit the counterexample, confirm it satisfies the domain condition, and show that P(c) fails by direct calculation or reference to a known fact. The argument is short and the verification is explicit.

Counterexamples also do positive work: they calibrate conjectures. If a counterexample violates only a boundary condition, it suggests that the conjecture can be salvaged by restricting the domain — "all differentiable functions are continuous" does hold, even though the converse fails. If the counterexample is generic or central, the conjecture is fundamentally wrong and should be abandoned or rebuilt. In this sense, counterexamples are not just destroyers of claims — they are diagnostic tools that reveal exactly where the boundary between truth and falsity lies, pointing toward the correct, restricted statement worth proving.
