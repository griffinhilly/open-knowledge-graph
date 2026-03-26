---
id: space-complexity-classes-formal
title: 'Space Complexity: PSPACE, L, and NL'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: nondeterministic-turing-machines
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
- id: algorithm-analysis-big-o
  type: soft
builds-toward:
- pspace-and-complexity-hierarchy
tags:
- complexity
- space-complexity
- PSPACE
- logarithmic-space
stage: advanced
status: validated
---

# Space Complexity: PSPACE, L, and NL

## Core Idea
Space complexity measures the number of tape cells a TM uses on an input of length n. PSPACE is the class of problems solvable in polynomial space; it contains both P and NP and is known to contain problems harder than any fixed polynomial. L and NL are the classes solvable in O(log n) space deterministically and nondeterministically; NL contains graph reachability (STCON). Savitch's theorem shows that nondeterministic space S(n) ≥ log n can be simulated deterministically in S(n)² space, so NPSPACE = PSPACE — a striking contrast to the unresolved P vs. NP question.

## How It's Best Learned
Contrast space with time: space can be reused across computation steps but time cannot. Work through Savitch's theorem to see why nondeterministic and deterministic space are polynomially related, while the analogous time question (NP ⊆ P?) remains open. Study QBF satisfiability as the canonical PSPACE-complete problem.

## Common Misconceptions
- Polynomial space does not imply polynomial time — PSPACE problems may require exponential time to solve.
- Logarithmic space is very restrictive: the working tape holds only O(log n) bits, enough for pointers into the input, while the input itself is read-only.

## Questions

```yaml
- question: "Savitch's theorem shows NPSPACE = PSPACE. Why doesn't the analogous argument collapse NP to P?"
  type: multiple-choice
  options: ["Space is reusable across computation steps, but time is not", "Savitch's theorem is incorrect for time complexity", "NP and P are equal but the proof has not been found", "Space is always larger than time so the theorem trivially applies to time too"]
  answer: 0
  explanation: "Space is reusable: a Turing machine can overwrite tape cells and use them again in later steps. Savitch's simulation exploits this to recursively reuse space, squashing nondeterministic S(n) space into deterministic O(S(n)²) space. Time is strictly sequential — each step is consumed once and cannot be shared. A nondeterministic path of length t requires t distinct time steps, so the recursive technique does not transfer."

- question: "A problem in PSPACE can generally be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "PSPACE contains problems that may require exponential time even though they use only polynomial space. PSPACE-complete problems like QBF (Quantified Boolean Formula satisfiability) are believed to require super-polynomial time. The space bound restricts memory usage, not the number of computation steps, which can be exponentially large."

- question: "What is the defining resource restriction for the class L (logarithmic space), and why is O(log n) bits sufficient to reason about positions in the input?"
  type: short-answer
  answer: "L allows only O(log n) bits on the working tape (the input is read-only and not counted). This is enough to store a constant number of integer indices into the input, since any position 0 to n-1 requires at most log₂ n bits to represent."
  explanation: "The key insight is that O(log n) bits can encode any index into a length-n input. This means an L-machine can maintain pointers to positions in the input and do pointer arithmetic, even though it cannot copy the input. Graph reachability (STCON) lies in NL because a nondeterministic machine only needs to store the current node (one index) as it guesses a path from s to t."
```

## Explainer

When we measure complexity by time, we count computation steps. Space complexity counts something different: the number of distinct tape cells written during the computation. The crucial difference is that space is *reusable* — after a machine finishes using part of the tape for an intermediate result, it can overwrite those cells. Time does not share this property; each step is consumed and cannot be revisited. This asymmetry is what makes space complexity behave so differently from time complexity.

PSPACE is the class of problems solvable using at most a polynomial number of tape cells. It contains both P and NP — any nondeterministic polynomial-time computation uses at most polynomial space — but PSPACE may contain harder problems still. The canonical PSPACE-complete problem is QBF (Quantified Boolean Formula satisfiability): determining the truth of a fully quantified Boolean formula such as ∀x∃y(x ∨ y). Solving QBF requires systematically exploring all assignments under alternating quantifiers, which is believed to require super-polynomial time despite using only polynomial space.

Savitch's theorem establishes a striking result: NPSPACE = PSPACE. Any nondeterministic machine using S(n) ≥ log n space can be simulated by a deterministic machine using O(S(n)²) space. The simulation works by a recursive divide-and-conquer: "can configuration A reach configuration B in k steps?" is answered by guessing a midpoint configuration M and recursively asking "can A reach M in k/2 steps?" and "can M reach B in k/2 steps?" Each recursive call reuses the same space, keeping total usage polynomial. Crucially, this technique cannot be applied to time because each recursive sub-call requires its own time steps — they cannot be reused or shared.

L and NL are the log-space classes, and they sit at the other end of the spectrum from PSPACE. L allows only O(log n) bits on the working tape — enough to store O(1) pointers into the input, but not enough to copy it. This is surprisingly powerful: O(log n) bits can represent any index from 0 to n-1, so a log-space machine can navigate the input freely using a handful of counters. NL adds nondeterminism and contains graph reachability (STCON): a nondeterministic log-space machine solves reachability by guessing one node at a time along the path, keeping only the current node in memory.

These classes fit into a containment hierarchy: L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXP. At least one of these containments is strict (PSPACE ⊊ EXP), but most boundaries — including P vs. NP and NL vs. P — remain unproven. Space complexity adds depth to the complexity landscape, revealing that the central open questions about hardness are just the most visible part of a much larger web of unresolved separations.
