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

## Questions

```yaml
- question: "A student argues: 'All undecidable problems are equally hard — they're all beyond the reach of any Turing machine, so talking about degrees of difficulty among them is meaningless.' Which observation most directly refutes this claim?"
  type: multiple-choice
  options:
    - "All undecidable problems reduce to the Halting Problem via many-one reductions, proving they are equivalent"
    - "There exist pairs of undecidable problems at incomparable Turing degrees: neither can be solved using the other as an oracle, demonstrating genuinely different levels of computational hardness"
    - "Undecidable problems are by definition harder than all decidable problems, which forms the only meaningful distinction"
    - "Turing machines cannot make any progress on undecidable problems, so comparing them is indeed meaningless"
  answer: 1
  explanation: "The existence of incomparable Turing degrees — undecidable problems A and B where A ≰_T B and B ≰_T A — directly refutes the claim that all undecidable problems are equally hard. Such problems have genuinely different computational content: solving one gives you no ability to solve the other, even with oracle access. The degree structure is a rich partial order with incomparable elements, not just a two-tier 'decidable vs. undecidable' division. This was established by Friedberg and Muchnik's priority argument in 1956."

- question: "Problem A can be solved using an oracle for Problem B (A ≤_T B), and Problem B can be solved using an oracle for Problem A (B ≤_T A). Neither A nor B is decidable. What can we conclude?"
  type: multiple-choice
  options:
    - "A is strictly harder than B because it was listed as needing an oracle for B"
    - "A and B are in the same Turing degree — they are computationally interchangeable as oracle resources"
    - "A many-one reduces to B, which implies B many-one reduces to A"
    - "Both A and B are in Turing degree 0, the degree of all decidable languages"
  answer: 1
  explanation: "Turing equivalence (A ≡_T B) holds when A ≤_T B and B ≤_T A. Problems in the same Turing degree are computationally interchangeable in the sense that an oracle for one can simulate an oracle for the other. This does not imply that A many-one reduces to B (option C): Turing reductions are more general than many-one reductions. Degree 0 (option D) is the degree of decidable problems — a Turing oracle is unnecessary for them, and the problem statement says neither A nor B is decidable."

- question: "The Halting Problem has a strictly higher Turing degree than any decidable language — no decidable problem can serve as an oracle sufficient to decide the Halting Problem."
  type: true-false
  answer: true
  explanation: "This is the fundamental result separating degree 0 (decidable problems) from degree 0' (the degree of the Halting Problem). A decidable oracle provides no computational power beyond what a plain Turing machine already has — you can already solve it without the oracle. So decidable oracles cannot help with the Halting Problem. This establishes 0 < 0' in the degree ordering: there is a strict hierarchy, and the Halting Problem sits strictly above all decidable problems. The jump operator A → A' formalizes this, always producing a degree strictly above A."

- question: "A Turing reduction from A to B is strictly more restrictive than a many-one reduction from A to B: Turing reductions impose stronger conditions on how B is used."
  type: true-false
  answer: false
  explanation: "This has the relationship backwards. Many-one reductions are *more restrictive* (a special case of Turing reductions): they require a single computable function f such that x ∈ A iff f(x) ∈ B, using the oracle exactly once and returning its answer directly. Turing reductions are *more permissive*: the oracle may be queried multiple times, on adaptive inputs depending on previous answers, with arbitrary computation between queries. Every many-one reduction is automatically a Turing reduction, but not vice versa. Turing degrees are therefore coarser than many-one degree classes: problems that are many-one inequivalent may be Turing equivalent."

- question: "Explain the difference between a many-one reduction and a Turing reduction, and why Turing degrees capture a richer notion of relative computability than the many-one degree structure."
  type: short-answer
  answer: "A many-one reduction from A to B is a computable function f such that x ∈ A iff f(x) ∈ B — the oracle for B is consulted exactly once, on a transformed input, and its yes/no answer is returned directly. A Turing reduction models oracle computation: a Turing machine can query an oracle for B on any input, any number of times, in any order, using previous answers to determine future queries. The Turing reduction is strictly more permissive. Two problems that are not many-one equivalent can still be Turing equivalent if each is computable relative to the other through repeated, adaptive oracle calls. This makes Turing degrees coarser — they capture what a problem *contains* as computational information, regardless of how that information is encoded or accessed. The many-one degree structure distinguishes problems by their syntactic reducibility; Turing degrees distinguish them by their intrinsic computational content."
  explanation: "The richer structure of Turing degrees reveals the internal architecture of the undecidable. For example, the complement of the Halting Problem is not many-one equivalent to the Halting Problem (one is c.e., the other is not), but they are Turing equivalent — each reduces to the other. Turing degrees collapse this distinction and ask only: what oracle power does this problem provide? This is why Turing degrees, not many-one degrees, are the natural unit of 'degree of unsolvability' — they measure computational content independently of representation."
```

## Explainer

You already know that some languages are undecidable — the Halting Problem is the canonical example — and that many-one reductions let you compare the hardness of problems by showing one reduces to another. Turing degrees extend this into a full landscape of *relative* uncomputability. The key idea is to ask not "is this problem decidable?" but "what does it take to decide this problem?" Two problems at the same Turing degree are interchangeable computational resources; problems at different degrees represent genuinely different levels of information.

A **Turing reduction** from problem A to problem B says: A is solvable if you could call a subroutine that solves B. We model this formally as **oracle computation** — imagine a Turing machine with a special tape where it can write a query and instantly receive an answer from an oracle for B. If A is solvable with an oracle for B, we write A ≤_T B: A is Turing-reducible to B. The crucial difference from many-one reductions is flexibility: a Turing reduction can call the oracle multiple times, use the answers conditionally, and even call it on inputs derived from previous oracle answers. Many-one reductions are a special case that use the oracle exactly once and return its answer directly.

Two problems A and B are **Turing equivalent** (A ≡_T B) if A ≤_T B and B ≤_T A. The equivalence classes under this relation are **Turing degrees** (or **degrees of unsolvability**). The degree of all decidable languages is the bottom degree **0**: any decidable problem is Turing-reducible to any other, because an oracle is unnecessary for a decidable problem. The Halting Problem H sits at degree **0'** (zero-jump), strictly above 0. The degree 0' contains H and everything Turing-equivalent to H — problems that are exactly as hard as the Halting Problem, no harder and no easier.

The **jump operator** A → A' (the Turing jump) produces a problem strictly harder than A from any degree A. Starting from 0, the jump gives 0', 0'', 0''',… — an infinite tower of strictly harder and harder problems, each new degree encoding questions about the computability behavior of the previous level. But the structure of degrees is not just a tower: there are incomparable degrees (neither reduces to the other), and there are degrees strictly between 0 and 0'. This **rich partial order** has been studied intensively, revealing a complex lattice with no simple description.

The philosophical payoff of Turing degrees is that they reveal the undecidable is not monolithic. When you encounter an undecidable problem in logic or mathematics, its Turing degree locates it precisely in this hierarchy — is it as hard as the Halting Problem, harder, or incomparable? Problems at 0' are "computably enumerable but not decidable"; problems above 0'' often encode higher-order quantification over computability itself. This hierarchy gives a language for measuring exactly how much information or computational power lies beyond the decidable threshold.
