---
id: large-cardinals-intro
title: Introduction to Large Cardinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: continuum-hypothesis
  type: soft
builds-toward: []
tags:
- large cardinals
- inaccessible cardinals
- Mahlo cardinals
- measurable cardinals
- consistency strength
stage: formal-systems
status: draft
---

# Introduction to Large Cardinals

## Core Idea
Large cardinal axioms postulate the existence of cardinals so large that their existence cannot be proved from ZFC alone — each one strengthens the consistency strength of the theory. An inaccessible cardinal κ is uncountable, regular (cf(κ) = κ), and a strong limit (2^λ < κ for all λ < κ); if such a cardinal exists, then V_κ is a model of ZFC, so ZFC cannot prove inaccessibles exist without proving its own consistency. Mahlo cardinals are inaccessible cardinals where the set of inaccessible cardinals below is stationary. Measurable cardinals carry a non-trivial κ-complete ultrafilter and imply the existence of elementary embeddings of the universe. These axioms form a roughly linear hierarchy of increasing consistency strength, providing a yardstick for measuring the logical power of mathematical statements.

## How It's Best Learned
Begin with inaccessible cardinals: verify that if κ is inaccessible then V_κ satisfies each ZFC axiom, so Con(ZFC + 'there exists an inaccessible') implies Con(ZFC). Then see how Mahlo cardinals strengthen inaccessibility by requiring 'many' inaccessibles below. For measurable cardinals, focus on the ultrafilter characterization before encountering elementary embeddings. The key insight is that each large cardinal axiom is a natural strengthening of the previous one, not an ad hoc addition.

## Common Misconceptions
- Large cardinals are not just 'very big numbers' — their defining property is logical strength (what new theorems they allow), not mere size.
- The large cardinal hierarchy is not strictly linear in every detail, but the main levels (inaccessible < Mahlo < measurable < supercompact < ...) are well-ordered by consistency strength.
