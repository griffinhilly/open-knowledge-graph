---
id: forcing-intro
title: Introduction to Forcing
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: independence-results-set-theory
  type: hard
- id: constructible-universe
  type: soft
builds-toward: []
tags:
- forcing
- Cohen forcing
- generic filters
- independence
- continuum hypothesis
- forcing conditions
stage: formal-systems
status: draft
---

# Introduction to Forcing

## Core Idea
Forcing, invented by Paul Cohen in 1963, is the principal technique for proving independence results in set theory. Starting from a countable transitive model M of ZFC (the ground model), one adjoins a new 'generic' object G that is not in M but is approximated by conditions in a partially ordered set (poset) P ∈ M. The forcing extension M[G] is again a model of ZFC, but may satisfy different statements than M — for example, M might satisfy CH while M[G] does not. Cohen used forcing with finite partial functions from ω × ω₂ to {0,1} to add ℵ₂ many new reals, producing a model where 2^{ℵ₀} = ℵ₂ and CH fails. Combined with Gödel's earlier proof that L satisfies CH, this established the independence of the continuum hypothesis from ZFC.

## How It's Best Learned
Begin with the analogy: forcing is like adding a new 'ideal' element to a structure while preserving axioms, similar to how ℝ extends ℚ. Study Cohen forcing (adding a generic real) as the first example. Understand the three key components: the poset P of forcing conditions, the generic filter G meeting all dense sets, and the forcing relation p ⊩ φ that lets you reason about the extension from within the ground model. Work through the proof that Cohen forcing preserves cardinals (using the countable chain condition) and adds new subsets of ω.

## Common Misconceptions
- Forcing does not produce 'fake' or 'nonstandard' models — M[G] is a legitimate model of ZFC. The independence results it yields are genuine: ZFC truly cannot decide CH.
- The generic filter G does not exist inside the ground model M — this is essential, not a defect. If G were in M, it would not add anything new.
