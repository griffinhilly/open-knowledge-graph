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
- id: set-theory-basics
  type: soft
builds-toward: []
tags:
- forcing
- Cohen forcing
- generic filters
- independence
- continuum hypothesis
- forcing conditions
stage: advanced
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

## Explainer

You already know that the continuum hypothesis (CH) is independent of ZFC: Gödel proved that the constructible universe L satisfies CH, establishing its consistency, and Cohen proved the consistency of ¬CH. **Forcing** is Cohen's technique — the method for constructing M[G] from a ground model M in which new sets (like enough reals to violate CH) are added while preserving all the ZFC axioms. It is the most powerful and widely used tool in set theory for proving independence results.

The setup begins with a **ground model** M — for technical reasons, taken to be a countable transitive model of ZFC (such models exist as a consequence of the reflection theorem and Löwenheim-Skolem). Inside M, you choose a **poset** (partially ordered set) P, called the **forcing poset** or **notion of forcing**. Elements of P are called **forcing conditions**. They represent finite, partial approximations to the new object you want to add. For Cohen forcing — the forcing that adds a new real — a condition is a finite partial function p: ω → {0,1}: a finite amount of information about a new binary sequence. Conditions are ordered by extension: p ≤ q (p is stronger) if p extends q with more information. Stronger conditions are more informative about the object being added.

The new object G is a **generic filter** over P: a filter (upward-closed, closed under common lower bounds) that meets every **dense subset** of P that belongs to M. Dense subsets are the "requirements" — for each n ∈ ω, the set of conditions that decide the value at n is dense, so G must include such a condition for every n. This forces G to be a total function, defining a complete new real. The crucial fact is that G does not exist in M — if it did, it would not meet all dense sets in M in an independent way. G exists "outside" M, and M[G] is the smallest model extending M that contains G. Remarkably, M[G] satisfies all of ZFC, because the axioms can be verified using the **forcing relation** p ⊩ φ — a relation definable inside M that predicts which formulas will hold in M[G] based on which conditions are in G.

For Cohen forcing that makes CH fail, the poset consists of finite partial functions from ω × ω₂ to {0,1}: each condition specifies bits in up to ℵ₂ different binary sequences. A generic filter G codes ℵ₂ distinct new reals into M[G], making 2^{ℵ₀} ≥ ℵ₂. The key technical theorem is that Cohen forcing satisfies the **countable chain condition** (ccc): every antichain (set of pairwise incompatible conditions) is countable. This ensures that the generic extension M[G] does not collapse any cardinals from M — ℵ₁ and ℵ₂ in M remain ℵ₁ and ℵ₂ in M[G]. Combining this with Gödel's L ⊨ CH, we have: CH is consistent with ZFC, and ¬CH is consistent with ZFC, so ZFC neither proves nor refutes CH. Forcing is the proof that the universe of sets is genuinely underdetermined by the ZFC axioms.
