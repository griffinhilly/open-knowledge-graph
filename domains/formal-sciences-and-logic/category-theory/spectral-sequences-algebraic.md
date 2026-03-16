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
stage: advanced
status: draft
---

# Spectral Sequences and Filtrations

## Core Idea
A spectral sequence is a systematic array of pages E_{p,q}^r with differentials d^r: E_{p,q}^r → E_{p-r,q+r-1}^r, organized by a filtration. Successive pages E^{r+1} are the homology of differentials on E^r, and the sequence converges to the associated graded of a target complex. Spectral sequences arise from filtered chain complexes, double complexes, and fibrations, providing powerful computational tools for homology that break hard problems into successively finer approximations.

## How It's Best Learned
Study the long exact sequence as a degenerate spectral sequence. Compute homology of the total complex of a double complex via spectral sequences. Apply the Serre spectral sequence to compute homology of fibration total spaces from base and fiber homology.

## Common Misconceptions
Spectral sequences compute the associated graded of the target, not the target directly; loss of information via filtration requires care. Differentials on higher pages depend on previous pages non-trivially; simply knowing early pages does not determine the full sequence. Convergence is a separate condition and can fail if the filtration is non-bounded or degenerates.

## Explainer

From your prerequisites, you know that a chain complex (C_*, d) has homology groups H_n(C) measuring cycles that are not boundaries, and that exact sequences encode algebraic relationships between homology groups of different spaces. Spectral sequences generalize both: they are a systematic machine for computing homology of a complex when the complex has additional structure — a **filtration** — that lets you attack the computation in layers rather than all at once.

A **filtration** of a chain complex C is a nested sequence of subcomplexes: ... ⊆ F_{p-1}C ⊆ F_pC ⊆ F_{p+1}C ⊆ ... ⊆ C. The filtration breaks C into layers; each quotient F_pC/F_{p-1}C is a "slice" of the complex. The idea is that homology of these slices is easier to compute than homology of C directly, and a spectral sequence systematically tracks how those slice-level computations assemble into the full answer. The **E² page** (or E¹ in some conventions) is the array of homology groups of the associated graded complex — one entry E_{p,q} for each bidegree (p,q) where p tracks the filtration level and q tracks the complementary degree.

The mechanism is iterated approximation. The **E^r page** (the r-th page) consists of groups E_{p,q}^r together with **differentials** d^r: E_{p,q}^r → E_{p-r, q+r-1}^r that shift filtration degree by −r and total degree by +1. The E^{r+1} page is the homology of d^r: E_{p,q}^{r+1} = ker(d^r)/im(d^r). As r increases, successive differentials kill off groups that are "boundaries at the r-th order of approximation" and reveal the next layer of structure. For most applications, the differentials eventually vanish (d^r = 0 for all large r), and the sequence **converges**: E_{p,q}^∞ is the associated graded of the filtration on H_{p+q}(C). Think of it as repeatedly zooming in — each page refines your knowledge of the homology until nothing more is hidden.

A powerful concrete example: the **Serre spectral sequence** for a fibration F → E → B, where E is the total space, B the base, and F the fiber. Here the E² page has E_{p,q}² = H_p(B; H_q(F)), the homology of the base with coefficients in the homology of the fiber. The spectral sequence converges to H_*(E). If you know the homology of B and F, you can often compute H_*(E) by tracking which differentials d^r are nonzero. For example, the Hopf fibration S¹ → S³ → S² immediately tells you (via the Serre spectral sequence) what the differentials must be, recovering the homology of S³ from knowledge of S¹ and S² — a calculation that would be harder by direct methods.

The critical subtlety your misconceptions section raises is that convergence gives you the **associated graded** of H_*(C), not H_*(C) itself. There can be **extension problems**: even knowing all the associated graded pieces E_{p,q}^∞, there may be multiple non-isomorphic groups H_n(C) with that associated graded. (This is the same issue as knowing a group's composition factors without knowing the extension.) Spectral sequences with integer coefficients can have extension problems; spectral sequences with field coefficients do not, because every short exact sequence of vector spaces splits. In practice, working over a field eliminates extensions and makes spectral sequence computations fully algorithmic — which is why topology courses often introduce them over ℤ/2 or ℚ before tackling integer coefficients.
