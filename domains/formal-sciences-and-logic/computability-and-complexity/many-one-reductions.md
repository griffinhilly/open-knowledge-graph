---
id: many-one-reductions
title: Many-One Reductions and Undecidability Proofs
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: undecidable-problems-examples
  type: hard
- id: computability-reductions
  type: hard
builds-toward:
- turing-degrees-equivalence
- np-hardness
tags:
- reductions
- undecidability
- proof-technique
stage: advanced
status: draft
---

# Many-One Reductions and Undecidability Proofs

## Core Idea
A many-one reduction from problem A to problem B is a total computable function that maps instances of A to instances of B, preserving the yes/no answer. If A is undecidable and there is a many-one reduction from A to B, then B is also undecidable. This technique systematically proves vast families of problems undecidable.

## Explainer

From your study of undecidable problems, you know the Halting Problem is undecidable — no Turing machine can decide whether an arbitrary program halts on a given input. From computability reductions, you know that undecidability spreads: if solving B would let you solve A, and A is undecidable, then B must be undecidable too. **Many-one reductions** are the sharpest and most widely used tool for formalizing this idea.

A **many-one reduction** from problem A to problem B is a total computable function f such that for every string x, x ∈ A if and only if f(x) ∈ B. Notice what this demands: f transforms *every* instance of A into an instance of B, preserving yes/no answers exactly. If such an f exists, we write A ≤_m B. The consequence is immediate: if A is undecidable and A ≤_m B, then B is undecidable. Any decision procedure for B could be turned into one for A by first applying f — contradicting A's undecidability.

The technique for proving undecidability via many-one reductions follows a consistent template. Take a known undecidable problem — typically the Halting Problem HALT = {⟨M, w⟩ : M halts on w} — as your base. To show B is undecidable, construct a computable function that transforms any instance ⟨M, w⟩ of HALT into an instance of B. The construction typically "simulates" M inside a machine or formula that witnesses B's property when M halts, and fails to witness it when M does not. The critical point is that the reduction function must itself be computable — you may not inspect whether M halts in the course of constructing the reduction.

Many-one reductions also reveal **degree structure**. Two problems are **many-one equivalent** if each reduces to the other. The Halting Problem, the problem of determining whether a Turing machine accepts any string, the equivalence problem for Turing machines, and the consequences of Rice's theorem all fall into the same many-one equivalence class. This gives a rich classification: some problems are strictly many-one harder than others, not just harder in the weaker Turing-reduction sense. Mastering this technique gives you the ability to prove virtually any natural problem about program behavior undecidable — by building the appropriate simulation argument — and to understand *why* those problems are all equivalent in computational difficulty.
