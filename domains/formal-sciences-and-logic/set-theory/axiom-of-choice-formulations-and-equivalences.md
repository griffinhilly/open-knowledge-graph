---
id: axiom-of-choice-formulations-and-equivalences
title: The Axiom of Choice and Equivalent Formulations
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: indexed-families-of-sets
  type: hard
- id: injections-surjections-and-inverse-functions
  type: soft
- id: well-founded-relations-and-recursion
  type: soft
builds-toward:
- axiom-of-choice
- zorns-lemma
- well-ordering-theorem
tags:
- axiom-of-choice
- equivalences
- selection
stage: formal-systems
status: draft
---

# The Axiom of Choice and Equivalent Formulations

## Core Idea
The axiom of choice states: for any collection {S_i : i ∈ I} of non-empty sets, there exists a choice function f such that f(i) ∈ S_i for each i. This axiom is equivalent to Zorn's lemma (every partially ordered set with upper bounds has maximal elements) and the well-ordering theorem (every set can be well-ordered). It is independent of ZF.
