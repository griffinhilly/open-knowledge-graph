---
id: stability-theory-introduction
title: 'Stability Theory: Introduction'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: type-spaces-and-stone-topology
  type: hard
- id: morleys-uncountable-categoricity
  type: soft
builds-toward:
- o-minimality-and-tame-geometry
tags:
- stable theory
- instability
- order property
- Shelah stability
stage: advanced
status: draft
---

# Stability Theory: Introduction

## Core Idea
A theory T is stable if it does not encode an infinite linear order on a definable set (the 'combinatorial complexity' is bounded). Stability theory, developed by Shelah, classifies complete theories by complexity. Stable theories have good properties: elementary extensions exist, saturated models of any size exist, and model-theoretic study simplifies dramatically. Most 'natural' theories (ACF, simple groups) are stable.

## Explainer

From your work on type spaces and Stone topology, you know that a **type** p(x) over a set A is a maximal consistent set of formulas with parameter from A, and that the space S(A) of all types carries a natural topology making it a Stone (compact, Hausdorff, totally disconnected) space. Type spaces measure the "complexity" of a theory: a theory with very many types over every parameter set is hard to analyze, while one with few types is tractable. **Stability** makes this intuition precise.

A theory T is **stable** if for every infinite cardinal λ, the number of types over any set A of size λ is at most λ — that is, |S(A)| ≤ |A| for all sufficiently large A. Compare this to an unstable theory: in the theory of dense linear orders (ℚ, <), for any set A, you can find 2^|A| many types over A (one for each Dedekind cut). The linear order allows types to encode unboundedly many distinctions. Shelah's insight was that the presence or absence of a **definable linear order** is the key diagnostic: a theory is unstable precisely when some formula φ(x, y) defines a linear order on a definable set (the **order property**).

The payoff for stability is substantial. In a stable theory, the type space S(A) is compact and relatively small, which means you can analyze models systematically. **Saturated models** — models that realize all types over small subsets — exist in every uncountable cardinality. The theory of **prime** and **saturated** models is clean: there is essentially one saturated model of each uncountable size (up to isomorphism), giving a level of control over model structure unavailable in unstable theories. Elementary submodel relationships become tractable, and you can meaningfully talk about "the" model of size κ in a categorical way.

Examples help calibrate intuition. The theory **ACF** of algebraically closed fields is stable — in fact, it is **strongly minimal**, the lowest rung of the stability hierarchy, where every definable set is either finite or cofinite. The complete theory of the integers under successor is **superstable** (a stronger form of stability). The theory of dense linear orders without endpoints is **unstable** — it has the order property. The theory of the random graph (the Rado graph) is a **simple** theory, which generalizes stability by relaxing the forking symmetry axioms. Understanding where a theory sits in this landscape — stable, superstable, ω-stable, strongly minimal — tells you which model-theoretic tools apply and how complex the definable geometry of the structure is.

