---
id: russells-paradox
title: Russell's Paradox
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: naive-set-theory
  type: hard
- id: set-theory-basics
  type: soft
builds-toward:
- zfc-axioms-overview
- axiom-of-separation
tags:
- paradox
- self-reference
- foundations
- russell
stage: formal-systems
status: validated
---

# Russell's Paradox

## Core Idea
Russell's paradox (1901) shows that naive set theory is inconsistent. Let R = {x : x ∉ x} be the set of all sets that are not members of themselves. If R ∈ R, then by definition R ∉ R; if R ∉ R, then R qualifies and R ∈ R — a contradiction either way. The paradox arises directly from the unrestricted comprehension axiom and forces a fundamental revision of the foundations of mathematics. Modern set theory resolves it by restricting comprehension to subsets of already-existing sets rather than allowing arbitrary predicate-defined collections.

## How It's Best Learned
Work through the paradox slowly: write out both cases of the biconditional R ∈ R ↔ R ∉ R and derive the contradiction explicitly. Compare with the informal 'barber paradox' as an analogue. The goal is to see precisely where unrestricted comprehension fails and why restricting to subsets of existing sets resolves it.

## Common Misconceptions
- Russell's paradox is not a mere philosophical puzzle — it is a formal proof that a specific axiom system is inconsistent.
- The resolution is not to ban self-reference entirely, but to prevent set-formation from quantifying over all sets at once.
- Russell's own solution (type theory) is one approach; Zermelo's separation axiom is the one adopted in standard set theory.
