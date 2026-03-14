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
