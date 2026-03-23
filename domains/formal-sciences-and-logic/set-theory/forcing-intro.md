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
status: validated
---

# Introduction to Forcing

## Core Idea
Forcing, invented by Paul Cohen in 1963, is the principal technique for proving independence results in set theory. Starting from a countable transitive model M of ZFC (the ground model), one adjoins a new 'generic' object G that is not in M but is approximated by conditions in a partially ordered set (poset) P ∈ M. The forcing extension M[G] is again a model of ZFC, but may satisfy different statements than M — for example, M might satisfy CH while M[G] does not. Cohen used forcing with finite partial functions from ω × ω₂ to {0,1} to add ℵ₂ many new reals, producing a model where 2^{ℵ₀} = ℵ₂ and CH fails. Combined with Gödel's earlier proof that L satisfies CH, this established the independence of the continuum hypothesis from ZFC.

## How It's Best Learned
Begin with the analogy: forcing is like adding a new 'ideal' element to a structure while preserving axioms, similar to how ℝ extends ℚ. Study Cohen forcing (adding a generic real) as the first example. Understand the three key components: the poset P of forcing conditions, the generic filter G meeting all dense sets, and the forcing relation p ⊩ φ that lets you reason about the extension from within the ground model. Work through the proof that Cohen forcing preserves cardinals (using the countable chain condition) and adds new subsets of ω.

## Common Misconceptions
- Forcing does not produce 'fake' or 'nonstandard' models — M[G] is a legitimate model of ZFC. The independence results it yields are genuine: ZFC truly cannot decide CH.
- The generic filter G does not exist inside the ground model M — this is essential, not a defect. If G were in M, it would not add anything new.

## Questions

```yaml
- question: "A student objects: 'Cohen forcing cannot genuinely add a new real number to the ground model M, because any finite partial function from ω to {0,1} already exists in M.' What is the correct response to this objection?"
  type: multiple-choice
  options:
    - "The objection is correct — Cohen forcing does not add new reals; it only changes which reals M believes are countable."
    - "The objection confuses finite conditions with the generic filter itself. Individual finite conditions exist in M, but the generic filter G — an infinite consistent combination meeting every dense set — does not exist in M."
    - "The objection fails because forcing uses infinite partial functions, not finite ones, and infinite functions do not exist in M."
    - "The objection is valid for Cohen forcing but not for other kinds of forcing."
  answer: 1
  explanation: "Individual forcing conditions (finite partial functions) are indeed in M — they are the approximations. But the generic filter G is an infinite consistent assembly of conditions that simultaneously meets every dense subset of the poset that belongs to M. The set of dense subsets of P in M is too rich for any single element of M to meet them all. G 'escapes' M precisely by meeting requirements that no element of M can simultaneously satisfy. This is exactly analogous to how an irrational number is not any single rational approximation but the limit of approximations that no single rational equals."

- question: "Why is it essential that the generic filter G does NOT exist inside the ground model M?"
  type: multiple-choice
  options:
    - "If G were in M, it would violate the axiom of foundation, since G would then be a member of itself."
    - "If G were in M, it would meet all dense sets trivially and add no new information — the extension M[G] would equal M, proving nothing."
    - "ZFC prohibits any filter from existing within a model of set theory."
    - "If G were in M, the forcing relation p ⊩ φ would be undefined."
  answer: 1
  explanation: "Dense subsets of P in M represent requirements: for each n, the set of conditions specifying the value at n is dense. A filter that met all these requirements from inside M would define a complete total function — a new real — but M already contains all the sets it 'knows about.' If G were in M, it would mean M already knew the generic object, contradicting the purpose of the extension. The whole point of G is to be a new object that M was 'unaware of,' obtained by meeting infinitely many dense-set requirements simultaneously in a way no element of M can do."

- question: "Forcing produces models of ZFC where statements like CH can be made true or false, but these are 'nonstandard' or 'fake' models — not genuine models of set theory."
  type: true-false
  answer: false
  explanation: "This is a fundamental misconception. M[G] is a fully legitimate model of ZFC — all axioms hold in M[G], verified via the forcing relation. The models produced by forcing are as 'real' as the ground model or any other model of ZFC. What forcing shows is that ZFC is genuinely underdetermined: there exist models satisfying CH and models satisfying ¬CH, both of which are perfectly valid set-theoretic universes. The independence of CH is not a quirk of nonstandard models; it is a genuine feature of ZFC's incompleteness."

- question: "The forcing relation p ⊩ φ is definable within the ground model M, meaning one can determine which statements will be true in M[G] before G is actually constructed."
  type: true-false
  answer: true
  explanation: "This is one of the most remarkable features of forcing. The forcing relation p ⊩ φ ('condition p forces formula φ') is a syntactic relation definable in M: you can compute, entirely within M, which conditions force which statements to be true in any generic extension. This is what makes forcing a proof technique rather than a mere existence claim. You prove, within M, that certain dense sets must be met and what their forcing of key statements implies, then conclude that the generic extension M[G] has the desired properties — without leaving M."

- question: "Proving the independence of CH from ZFC required two separate results. What does each contribute, and why is neither alone sufficient?"
  type: short-answer
  answer: "Gödel's result (1938) showed that the constructible universe L is a model of ZFC in which CH holds, establishing that ZFC cannot DISPROVE CH (¬CH is not a theorem of ZFC). Cohen's forcing (1963) constructed a model M[G] of ZFC in which CH fails — 2^{ℵ₀} ≥ ℵ₂ — establishing that ZFC cannot PROVE CH. Together, these show that CH is independent: neither provable nor disprovable from ZFC. Gödel alone would only show CH is consistent; Cohen alone would only show ¬CH is consistent. Independence requires both directions."
  explanation: "The key technical feature of Cohen forcing that makes it work is the countable chain condition (ccc): every antichain in the forcing poset is countable. This ensures no cardinals are collapsed in M[G], so ℵ₁ and ℵ₂ in M remain ℵ₁ and ℵ₂ in M[G], and adding ℵ₂ new reals genuinely makes 2^{ℵ₀} ≥ ℵ₂ without inadvertently making ℵ₂ countable."
```

## Explainer

You already know that the continuum hypothesis (CH) is independent of ZFC: Gödel proved that the constructible universe L satisfies CH, establishing its consistency, and Cohen proved the consistency of ¬CH. **Forcing** is Cohen's technique — the method for constructing M[G] from a ground model M in which new sets (like enough reals to violate CH) are added while preserving all the ZFC axioms. It is the most powerful and widely used tool in set theory for proving independence results.

The setup begins with a **ground model** M — for technical reasons, taken to be a countable transitive model of ZFC (such models exist as a consequence of the reflection theorem and Löwenheim-Skolem). Inside M, you choose a **poset** (partially ordered set) P, called the **forcing poset** or **notion of forcing**. Elements of P are called **forcing conditions**. They represent finite, partial approximations to the new object you want to add. For Cohen forcing — the forcing that adds a new real — a condition is a finite partial function p: ω → {0,1}: a finite amount of information about a new binary sequence. Conditions are ordered by extension: p ≤ q (p is stronger) if p extends q with more information. Stronger conditions are more informative about the object being added.

The new object G is a **generic filter** over P: a filter (upward-closed, closed under common lower bounds) that meets every **dense subset** of P that belongs to M. Dense subsets are the "requirements" — for each n ∈ ω, the set of conditions that decide the value at n is dense, so G must include such a condition for every n. This forces G to be a total function, defining a complete new real. The crucial fact is that G does not exist in M — if it did, it would not meet all dense sets in M in an independent way. G exists "outside" M, and M[G] is the smallest model extending M that contains G. Remarkably, M[G] satisfies all of ZFC, because the axioms can be verified using the **forcing relation** p ⊩ φ — a relation definable inside M that predicts which formulas will hold in M[G] based on which conditions are in G.

For Cohen forcing that makes CH fail, the poset consists of finite partial functions from ω × ω₂ to {0,1}: each condition specifies bits in up to ℵ₂ different binary sequences. A generic filter G codes ℵ₂ distinct new reals into M[G], making 2^{ℵ₀} ≥ ℵ₂. The key technical theorem is that Cohen forcing satisfies the **countable chain condition** (ccc): every antichain (set of pairwise incompatible conditions) is countable. This ensures that the generic extension M[G] does not collapse any cardinals from M — ℵ₁ and ℵ₂ in M remain ℵ₁ and ℵ₂ in M[G]. Combining this with Gödel's L ⊨ CH, we have: CH is consistent with ZFC, and ¬CH is consistent with ZFC, so ZFC neither proves nor refutes CH. Forcing is the proof that the universe of sets is genuinely underdetermined by the ZFC axioms.
