---
id: axiom-of-choice
title: Axiom of Choice
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: binary-relations
  type: soft
builds-toward:
- well-ordering-theorem
- zorns-lemma
- cardinal-arithmetic
tags:
- ZFC
- axiom of choice
- choice function
- AC
- independence
stage: formal-systems
status: draft
---

# Axiom of Choice

## Core Idea
The axiom of choice (AC) states that for any collection of non-empty sets {A_i : i ∈ I}, there exists a choice function f satisfying f(i) ∈ A_i for every i ∈ I. AC is required whenever one needs to simultaneously select elements from infinitely many sets without an explicit selection rule. It is independent of ZF — neither provable nor refutable from the other axioms — yet accepted in ZFC. AC is equivalent over ZF to both Zorn's lemma and the well-ordering theorem; it implies non-constructive results like the existence of non-measurable sets (Vitali sets) and bases for all vector spaces.

## How It's Best Learned
Start with finite families (where choice is trivial) and countable families (where AC is provable from ZF). Study constructions that require full AC: bases for vector spaces over arbitrary fields, the fact that every surjection has a right inverse, and Tychonoff's theorem for products. Then study the equivalences with Zorn's lemma and the well-ordering theorem.

## Common Misconceptions
- For finite or countable families, choice is provable in ZF without the additional axiom.
- AC does not specify which element to choose — it only asserts that a choice exists; it is inherently non-constructive.
- AC is consistent with ZF; accepting it does not introduce contradictions.
