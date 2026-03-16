---
id: turing-degrees-equivalence
title: Turing Degrees and Degrees of Unsolvability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: many-one-reductions
  type: hard
- id: recursively-enumerable-languages
  type: hard
builds-toward:
- complexity-lower-bounds
tags:
- turing-degrees
- reduction
- uncomputability
- hierarchy
stage: advanced
status: draft
---

# Turing Degrees and Degrees of Unsolvability

## Core Idea
Two problems have the same Turing degree if each is computable relative to the other (Turing equivalent). Turing degrees form a hierarchy measuring relative uncomputability: the Halting Problem has a higher degree than the recursive languages. This degree structure reveals a rich landscape between the decidable and the undecidable.

## How It's Best Learned
Study Turing reductions as oracle computations: problem A is Turing-reducible to B if A is computable given an oracle for B. Compare with many-one reductions.

## Common Misconceptions
- Confusing Turing equivalence with many-one equivalence. Turing is more permissive and captures relative computability more fully.

## Explainer

You already know that some languages are undecidable — the Halting Problem is the canonical example — and that many-one reductions let you compare the hardness of problems by showing one reduces to another. Turing degrees extend this into a full landscape of *relative* uncomputability. The key idea is to ask not "is this problem decidable?" but "what does it take to decide this problem?" Two problems at the same Turing degree are interchangeable computational resources; problems at different degrees represent genuinely different levels of information.

A **Turing reduction** from problem A to problem B says: A is solvable if you could call a subroutine that solves B. We model this formally as **oracle computation** — imagine a Turing machine with a special tape where it can write a query and instantly receive an answer from an oracle for B. If A is solvable with an oracle for B, we write A ≤_T B: A is Turing-reducible to B. The crucial difference from many-one reductions is flexibility: a Turing reduction can call the oracle multiple times, use the answers conditionally, and even call it on inputs derived from previous oracle answers. Many-one reductions are a special case that use the oracle exactly once and return its answer directly.

Two problems A and B are **Turing equivalent** (A ≡_T B) if A ≤_T B and B ≤_T A. The equivalence classes under this relation are **Turing degrees** (or **degrees of unsolvability**). The degree of all decidable languages is the bottom degree **0**: any decidable problem is Turing-reducible to any other, because an oracle is unnecessary for a decidable problem. The Halting Problem H sits at degree **0'** (zero-jump), strictly above 0. The degree 0' contains H and everything Turing-equivalent to H — problems that are exactly as hard as the Halting Problem, no harder and no easier.

The **jump operator** A → A' (the Turing jump) produces a problem strictly harder than A from any degree A. Starting from 0, the jump gives 0', 0'', 0''',… — an infinite tower of strictly harder and harder problems, each new degree encoding questions about the computability behavior of the previous level. But the structure of degrees is not just a tower: there are incomparable degrees (neither reduces to the other), and there are degrees strictly between 0 and 0'. This **rich partial order** has been studied intensively, revealing a complex lattice with no simple description.

The philosophical payoff of Turing degrees is that they reveal the undecidable is not monolithic. When you encounter an undecidable problem in logic or mathematics, its Turing degree locates it precisely in this hierarchy — is it as hard as the Halting Problem, harder, or incomparable? Problems at 0' are "computably enumerable but not decidable"; problems above 0'' often encode higher-order quantification over computability itself. This hierarchy gives a language for measuring exactly how much information or computational power lies beyond the decidable threshold.
