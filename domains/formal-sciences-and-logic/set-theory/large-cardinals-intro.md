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

## Explainer

From infinite cardinals, you know that ℵ₀ < ℵ₁ < ℵ₂ < ... is just the beginning of a vast hierarchy of infinite sizes. And from the continuum hypothesis, you know that ZFC leaves the size of ℝ undetermined — neither CH nor ¬CH is provable from ZFC alone. Large cardinal axioms push this logic further: they assert the existence of cardinals so structurally rich that ZFC itself cannot prove they exist. The reason is profound — each large cardinal axiom implies Con(ZFC), and by Gödel's second incompleteness theorem, ZFC cannot prove its own consistency. So if κ is an inaccessible cardinal, ZFC + "κ exists" strictly outpowers plain ZFC.

An **inaccessible cardinal** κ satisfies two conditions beyond mere uncountability. First, it is **regular**: κ cannot be expressed as a union of fewer than κ sets each of size less than κ. (Contrast: ℵ_ω = sup{ℵ₀, ℵ₁, ℵ₂, ...} is a union of ω sets each smaller than ℵ_ω, so it's singular.) Second, it is a **strong limit**: for every λ < κ, the power set 2^λ is still less than κ — exponentiation cannot "jump over" κ. Together these conditions make κ a natural ceiling: the cumulative hierarchy V_κ satisfies every ZFC axiom, so κ's existence gives you a model of ZFC inside your universe.

**Mahlo cardinals** strengthen inaccessibility by requiring that inaccessible cardinals are *dense* below κ in a precise sense: the set of inaccessible cardinals less than κ is **stationary** (it intersects every club — closed unbounded — subset of κ). This is a richness condition on the structure of cardinals below κ, not just on κ itself. A Mahlo cardinal is inaccessible, but an inaccessible need not be Mahlo: the first inaccessible is not Mahlo, but Mahlo cardinals, if they exist, sit strictly above the first inaccessible in the consistency strength ordering.

**Measurable cardinals** introduce a genuinely new idea: a measurable cardinal κ carries a **κ-complete non-principal ultrafilter** U on κ. Informally, U is a consistent "voting system" where every large subset of κ wins. The completeness condition says that intersecting fewer than κ winning sets still gives a winning set. This ultrafilter lets you build an ultrapower of the set-theoretic universe, producing an **elementary embedding** j: V → M where M is an inner model and j(κ) > κ. The existence of such an embedding is extremely powerful — it implies, for instance, that every projective set of reals is Lebesgue measurable and has the Baire property, settling questions completely independent of ZFC alone.

These three levels — inaccessible, Mahlo, measurable — are just the beginning of a hierarchy that extends through Woodin cardinals, supercompact cardinals, and beyond. What unifies them is the concept of **consistency strength**: each level implies the consistency of all levels below it, so they form a well-ordered calibration scale. When mathematicians prove a theorem from ZFC + a large cardinal axiom, they are measuring how much logical strength the theorem requires. This gives large cardinals a central role not just in set theory, but as a measuring instrument for the rest of mathematics.

