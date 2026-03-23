---
id: computability-reductions
title: Computability Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: soft
- id: injective-surjective-bijective
  type: soft
builds-toward:
- rices-theorem
- re-and-co-re-languages
- polynomial-time-reductions
tags:
- reductions
- undecidability
- computability
- many-one-reducibility
stage: formal-systems
status: validated
---

# Computability Reductions

## Core Idea
A many-one reduction from problem A to problem B is a computable function f such that x ∈ A if and only if f(x) ∈ B. If such a reduction exists, B is 'at least as hard' as A: any algorithm for B can be used to solve A. Reductions are the primary tool for proving undecidability — to show a new problem is undecidable, reduce the halting problem to it. Turing reductions (oracle reductions) are more general and allow multiple adaptive queries, measuring relative computability rather than mere hardness.

## How It's Best Learned
Practice constructing explicit reduction functions on concrete problem pairs. A useful exercise: show that the acceptance problem (does TM M accept input w?) reduces to the halting problem and vice versa, establishing their Turing equivalence.

## Common Misconceptions
- Reduction direction is easy to confuse: to show B is hard, reduce a known-hard problem A *to* B, not B to A.
- Many-one reductions are stricter than Turing reductions; a Turing reduction allows multiple queries to an oracle while many-one allows exactly one.

## Questions

```yaml
- question: "To prove that problem B is undecidable, what is the correct reduction strategy?"
  type: multiple-choice
  options:
    - "Reduce B to the Halting Problem, showing B is no harder than Halting"
    - "Reduce the Halting Problem to B, showing B is at least as hard as Halting"
    - "Reduce B to a known decidable problem, then derive a contradiction"
    - "Show that B reduces to itself via the identity function"
  answer: 1
  explanation: "The direction is critical. A ≤m B means 'A reduces to B', which implies B is at least as hard as A. To show B is undecidable, you reduce a known-undecidable problem (like the Halting Problem) to B. If B were decidable, you could use that decision procedure to decide the Halting Problem — contradiction. The most common misconception is reversing the direction."

- question: "A many-one reduction from A to B and a Turing reduction from A to B are equivalent: both allow the solver to make multiple queries to B."
  type: true-false
  answer: false
  explanation: "Many-one reductions are strictly more constrained: the reduction f transforms a single input x into exactly one query f(x) to B, and the answer directly determines membership in A. A Turing reduction allows multiple adaptive queries to B as an oracle — earlier answers can influence later queries. Every many-one reduction is a Turing reduction, but not vice versa."

- question: "Why does a many-one reduction from A to B (written A ≤m B) imply that B is 'at least as hard' as A?"
  type: short-answer
  answer: "Any algorithm solving B can be converted into an algorithm solving A: given an A-input x, apply the computable function f to get f(x), then query the B-solver on f(x). By the reduction's correctness, x ∈ A iff f(x) ∈ B, so this procedure correctly decides A. If B were decidable, A would be too — meaning A cannot be strictly harder than B."
  explanation: "The key insight is that a reduction transfers computational resources from B to A. Whatever power is needed to solve B is sufficient to solve A. So if A is undecidable, B cannot be any easier."
```

## Explainer

Reductions are the fundamental tool for comparing the difficulty of computational problems. The core idea is simple: if you can transform any instance of problem A into an instance of problem B in a systematic, computable way, then B is 'at least as hard' as A. Anything that solves B can be repurposed to solve A — just run the transformation first, then apply B's solver. This lets you build a hierarchy of problems by hardness without having to analyze each problem from scratch.

A many-one reduction from A to B is a computable function f such that for every input x, x belongs to A if and only if f(x) belongs to B. The notation A ≤m B (read 'A many-one reduces to B') captures this: the subscript m stands for 'many-one' because many inputs to A might map to the same input to B. The reduction must be computable — you cannot use any magic oracle to build f itself — but it does not need to be efficient in the complexity-theoretic sense.

The most important application of reductions is proving undecidability. You already know the Halting Problem is undecidable. To show a new problem B is also undecidable, you construct a reduction from Halting to B: a computable f where (M, w) halts iff f(M, w) ∈ B. Now suppose, for contradiction, B were decidable. Then you could decide Halting by first applying f, then running B's decision procedure — contradicting the known undecidability of Halting. Pay close attention to the direction: you reduce the *known-hard* problem to the *new* problem, not the other way around.

Turing reductions (also called oracle reductions) generalize many-one reductions. Instead of transforming the input once and submitting a single query, a Turing reduction may make multiple adaptive queries to a B-oracle — where each query can depend on the answers to previous ones. This makes Turing reductions strictly more powerful: some problems are Turing-equivalent to the Halting Problem but not many-one equivalent. The acceptance problem (does M accept w?) and the Halting Problem are many-one equivalent to each other, which is why they are often treated as interchangeable in practice.

Reductions do not stop at computability — they extend directly into complexity theory. Polynomial-time many-one reductions (where f must run in polynomial time) are the backbone of NP-completeness theory. When you study NP-completeness, you will see the same pattern: to show a new problem is NP-hard, reduce a known NP-hard problem to it in polynomial time. The logical structure is identical to what you learned here; only the resource bound on f changes.
