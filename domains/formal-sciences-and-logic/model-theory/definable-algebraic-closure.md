---
id: definable-algebraic-closure
title: Definable Closure and Algebraic Closure
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: definability-and-algebraic-applications
  type: hard
- id: structures-and-formal-languages
  type: soft
builds-toward:
- transcendence-and-independence
- strongly-minimal-and-geometry
tags:
- definable-closure
- algebraic-closure
- closure-operators
stage: advanced
status: draft
---

# Definable Closure and Algebraic Closure

## Core Idea
The definable closure dcl(A) consists of elements definable from A with parameters. The algebraic closure acl(A) consists of elements satisfying a formula over A with finitely many solutions. In stable theories, dcl(A) ⊆ acl(A), and when dcl(A) is also algebraically closed it forms a submodel. These closures provide structure theory for models of stable theories.

## Explainer

From your work on definability, you know that a set S ⊆ M^n is **definable** over a parameter set A if there is a formula φ(x̄, ā) with ā ∈ A such that S = {x̄ : M ⊨ φ(x̄, ā)}. Now consider what elements are "pinned down" by parameters in A. The **definable closure** dcl(A) consists of all elements b such that the singleton {b} is A-definable — that is, φ(x, ā) has exactly one solution, namely b. Think of it as the set of elements you can uniquely name using formulas with parameters from A.

The **algebraic closure** acl(A) relaxes unique definability: b ∈ acl(A) if there exists some formula φ(x, ā) with ā ∈ A such that b satisfies φ and φ has only *finitely many* solutions. The element isn't necessarily uniquely pinned down, but it lives in a finite "orbit" over A. Notice the analogy with field theory: in the field ℝ considered as a structure, √2 is algebraic over ℚ because it satisfies x² − 2 = 0, which has exactly two solutions. Indeed, in algebraically closed fields, model-theoretic acl agrees with the classical algebraic closure from field theory.

The inclusion dcl(A) ⊆ acl(A) is immediate from the definitions: if b is the unique element satisfying φ(x, ā), then φ has finitely many (specifically, one) solution, so b ∈ acl(A). Both operations are **closure operators**: A ⊆ dcl(A), dcl(dcl(A)) = dcl(A), and similarly for acl. In stable theories, these closures behave especially well — acl(A) is always a model-theoretically small structure carrying the "algebraic content" of A, and independence (non-forking) is intimately tied to the acl operator.

The structural importance of these closures comes into focus when building models. A set A is **algebraically closed** (in the model-theoretic sense) if acl(A) = A — every element finitely definable from A is already in A. Algebraically closed sets serve as the "good" parameter sets for independence theory, analogous to how algebraically closed fields are the "good" fields in algebraic geometry. When A = dcl(A), A forms a closed substructure that reflects the ambient theory; combining both conditions gives the structural building blocks for understanding models of stable theories.
