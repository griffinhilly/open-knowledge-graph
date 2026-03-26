---
id: spectral-sequences-algebraic
title: Spectral Sequences and Filtrations
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-equivalences-categories
tags:
- spectral-sequence
- filtration
- pages
- convergence
- grading
stage: expert
status: validated
---

# Spectral Sequences and Filtrations

## Core Idea
A spectral sequence is a systematic array of pages E_{p,q}^r with differentials d^r: E_{p,q}^r → E_{p-r,q+r-1}^r, organized by a filtration. Successive pages E^{r+1} are the homology of differentials on E^r, and the sequence converges to the associated graded of a target complex. Spectral sequences arise from filtered chain complexes, double complexes, and fibrations, providing powerful computational tools for homology that break hard problems into successively finer approximations.

## How It's Best Learned
Study the long exact sequence as a degenerate spectral sequence. Compute homology of the total complex of a double complex via spectral sequences. Apply the Serre spectral sequence to compute homology of fibration total spaces from base and fiber homology.

## Common Misconceptions
Spectral sequences compute the associated graded of the target, not the target directly; loss of information via filtration requires care. Differentials on higher pages depend on previous pages non-trivially; simply knowing early pages does not determine the full sequence. Convergence is a separate condition and can fail if the filtration is non-bounded or degenerates.

## Questions

```yaml
- question: "A mathematician computes the Serre spectral sequence for a fibration and determines all E^∞ terms. To find the actual homology groups H_n of the total space, what additional step may be required?"
  type: multiple-choice
  options:
    - "Nothing — the E^∞ terms directly give the homology groups H_n for each degree n"
    - "Solving extension problems — the E^∞ terms give the associated graded, and multiple non-isomorphic groups may have the same associated graded"
    - "Computing one more page of differentials, since E^∞ is one page before convergence"
    - "Applying the universal coefficient theorem to convert from one coefficient ring to another"
  answer: 1
  explanation: "Convergence gives you E^∞_{p,q} as the associated graded pieces of a filtration on H_{p+q}. Knowing the associated graded is not the same as knowing the group: for example, ℤ/4 and ℤ/2 ⊕ ℤ/2 have the same associated graded (ℤ/2 in each filtration level) but are non-isomorphic groups. This is the extension problem. The only case where it is automatic is when working over a field — then every short exact sequence of vector spaces splits and the associated graded uniquely determines the group."

- question: "On the r-th page of a spectral sequence, the differential d^r maps E_{p,q}^r to which bidegree?"
  type: multiple-choice
  options:
    - "E_{p+1, q}^r — shifts filtration degree by +1"
    - "E_{p-r, q+r-1}^r — shifts filtration degree by -r and total degree by +1 overall"
    - "E_{p, q-1}^r — shifts the complementary degree by -1"
    - "E_{p+r, q-r+1}^r — shifts filtration degree by +r"
  answer: 1
  explanation: "The differential d^r on the r-th page has bidegree (-r, r-1), mapping E_{p,q}^r → E_{p-r, q+r-1}^r. The total degree p+q shifts by -r + (r-1) = -1, consistent with differentials on a chain complex lowering degree by 1. As r increases, differentials reach farther across the page. The E^{r+1} page is the homology of d^r: E^{r+1}_{p,q} = ker(d^r at (p,q)) / im(d^r from (p+r, q-r+1))."

- question: "Once most E^∞ terms of a spectral sequence are known, the actual homology groups H_n are uniquely determined regardless of coefficient ring."
  type: true-false
  answer: false
  explanation: "E^∞ terms give the associated graded of the filtration on H_n, but extension problems may arise: multiple non-isomorphic groups can have the same associated graded. Over a field (like ℤ/2 or ℚ), every short exact sequence of vector spaces splits, so the associated graded uniquely determines the homology groups. Over ℤ, extension problems are common — this is why topology courses often introduce spectral sequences over field coefficients first, where computations are fully algorithmic."

- question: "Working with field coefficients (such as ℤ/2 or ℚ) eliminates extension problems in spectral sequence computations, making the E^∞ page sufficient to read off the homology groups."
  type: true-false
  answer: true
  explanation: "Over a field, every short exact sequence 0 → A → B → C → 0 of vector spaces splits: B ≅ A ⊕ C. This means the filtration on H_n always splits as a direct sum of its associated graded pieces E^∞_{p,q} with p+q = n. There is no ambiguity in assembling the homology group from the associated graded — you just take the direct sum. This is why field coefficients make spectral sequence computations cleaner and why most introductory examples use ℤ/2 or ℚ."

- question: "Explain the role of a filtration in a spectral sequence — why does the filtration make the homology computation tractable, and what information does it cause you to lose?"
  type: short-answer
  answer: "A filtration breaks a chain complex into nested layers, and the spectral sequence computes homology of the associated graded (the successive quotients F_pC / F_{p-1}C) rather than the whole complex at once. Each 'slice' is simpler to analyze, and the spectral sequence systematically tracks how slice-level homology assembles into the full answer through the pages of differentials. The information lost is: the filtration only determines the associated graded of H_*(C), not H_*(C) itself. To recover the actual homology from the associated graded, you must solve extension problems — determining which group has the given graded pieces. Over a field, all extensions are trivial (everything splits), so nothing is lost."
  explanation: "This is the fundamental trade-off in spectral sequence theory: the filtration makes a hard computation tractable by breaking it into layers, but the price is that you may lose information about how those layers assemble, requiring additional work (extension problems) to complete the answer."
```

## Explainer

From your prerequisites, you know that a chain complex (C_*, d) has homology groups H_n(C) measuring cycles that are not boundaries, and that exact sequences encode algebraic relationships between homology groups of different spaces. Spectral sequences generalize both: they are a systematic machine for computing homology of a complex when the complex has additional structure — a **filtration** — that lets you attack the computation in layers rather than all at once.

A **filtration** of a chain complex C is a nested sequence of subcomplexes: ... ⊆ F_{p-1}C ⊆ F_pC ⊆ F_{p+1}C ⊆ ... ⊆ C. The filtration breaks C into layers; each quotient F_pC/F_{p-1}C is a "slice" of the complex. The idea is that homology of these slices is easier to compute than homology of C directly, and a spectral sequence systematically tracks how those slice-level computations assemble into the full answer. The **E² page** (or E¹ in some conventions) is the array of homology groups of the associated graded complex — one entry E_{p,q} for each bidegree (p,q) where p tracks the filtration level and q tracks the complementary degree.

The mechanism is iterated approximation. The **E^r page** (the r-th page) consists of groups E_{p,q}^r together with **differentials** d^r: E_{p,q}^r → E_{p-r, q+r-1}^r that shift filtration degree by −r and total degree by +1. The E^{r+1} page is the homology of d^r: E_{p,q}^{r+1} = ker(d^r)/im(d^r). As r increases, successive differentials kill off groups that are "boundaries at the r-th order of approximation" and reveal the next layer of structure. For most applications, the differentials eventually vanish (d^r = 0 for all large r), and the sequence **converges**: E_{p,q}^∞ is the associated graded of the filtration on H_{p+q}(C). Think of it as repeatedly zooming in — each page refines your knowledge of the homology until nothing more is hidden.

A powerful concrete example: the **Serre spectral sequence** for a fibration F → E → B, where E is the total space, B the base, and F the fiber. Here the E² page has E_{p,q}² = H_p(B; H_q(F)), the homology of the base with coefficients in the homology of the fiber. The spectral sequence converges to H_*(E). If you know the homology of B and F, you can often compute H_*(E) by tracking which differentials d^r are nonzero. For example, the Hopf fibration S¹ → S³ → S² immediately tells you (via the Serre spectral sequence) what the differentials must be, recovering the homology of S³ from knowledge of S¹ and S² — a calculation that would be harder by direct methods.

The critical subtlety your misconceptions section raises is that convergence gives you the **associated graded** of H_*(C), not H_*(C) itself. There can be **extension problems**: even knowing all the associated graded pieces E_{p,q}^∞, there may be multiple non-isomorphic groups H_n(C) with that associated graded. (This is the same issue as knowing a group's composition factors without knowing the extension.) Spectral sequences with integer coefficients can have extension problems; spectral sequences with field coefficients do not, because every short exact sequence of vector spaces splits. In practice, working over a field eliminates extensions and makes spectral sequence computations fully algorithmic — which is why topology courses often introduce them over ℤ/2 or ℚ before tackling integer coefficients.
