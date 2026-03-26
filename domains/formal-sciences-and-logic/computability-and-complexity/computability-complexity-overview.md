---
id: computability-complexity-overview
title: 'Computability and Complexity: Overview and Connections'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: mu-recursive-functions
  type: soft
builds-toward:
- formal-computational-models
- undecidable-problems-examples
- complexity-class-definitions-hierarchy
tags:
- overview
- foundations
- computability
- complexity-theory
stage: formal-systems
status: validated
---
# Computability and Complexity: Overview and Connections

## Core Idea
Computability theory asks which problems can be solved algorithmically at all (decidability), while complexity theory asks which solvable problems can be solved efficiently. Together, they form the foundations of theoretical computer science, connecting mathematical logic to questions about practical computation limits.

## How It's Best Learned
Start with a high-level chronology: early undecidable problems, then complexity results starting from P vs NP. Connecting Gödel's incompleteness theorems to uncomputability helps build intuition.

## Common Misconceptions
- Confusing undecidable with hard-to-compute. Undecidable problems don't have algorithms at all, not even slow ones.
- Thinking P vs NP solves computability: P and NP are about efficient computation, not all computation.

## Questions

```yaml
- question: "A researcher proves that a decision problem Q is NP-complete. What does this tell us about whether Q can be solved at all?"
  type: multiple-choice
  options:
    - "Q is undecidable — no algorithm can solve it"
    - "Q is decidable but requires exponential time"
    - "Q is decidable — NP-complete problems have algorithms, just not ones known to run in polynomial time"
    - "Q is in P if and only if P = NP"
  answer: 2
  explanation: "NP-complete problems are decidable — they sit inside the decidable region, within the class NP. Algorithms that verify a solution in polynomial time are a prerequisite for NP membership, and exhaustive search algorithms can in principle solve them (just not efficiently). NP-completeness says nothing about undecidability; it is a statement about where a problem sits within the complexity hierarchy of solvable problems. Conflating 'no known efficient solution' with 'no solution at all' is the key misconception this question targets. Option D is partially true but incomplete — it describes what a proof that P = NP would imply, not what NP-completeness alone tells us."

- question: "The halting problem is difficult to solve efficiently — it requires super-polynomial time."
  type: true-false
  answer: false
  explanation: "The halting problem is not merely difficult to solve efficiently — it is impossible to solve at all. No algorithm exists that correctly answers 'does this program halt on this input?' for all possible program-input pairs. This is an undecidability result, proved by diagonalization, not a complexity result. Saying it 'requires super-polynomial time' implies that a slow algorithm exists, which is false. Undecidable problems are entirely outside the decidable region; complexity theory's classifications (P, NP, EXPTIME) only apply within it."

- question: "Any problem that requires more than polynomial time to solve should be undecidable."
  type: true-false
  answer: false
  explanation: "Many decidable problems require exponential time or more — they are in EXPTIME or higher complexity classes but are still decidable. For example, deciding the winner in certain board games (like generalized chess) requires exponential time in the board size but is perfectly decidable. Undecidability means no algorithm exists at all, regardless of time. The complexity hierarchy maps the structure of decidable problems by resource requirements; undecidability is a separate, outer boundary. Conflating 'hard' with 'unsolvable' is the core misconception in computability vs. complexity."

- question: "Computability theory and complexity theory both use reductions as a key proof technique, even though they address different questions."
  type: true-false
  answer: true
  explanation: "Reductions are the universal tool for comparing problem difficulty in both fields. In computability, many-one reductions show relative undecidability: if problem A reduces to B (A ≤_m B) and A is undecidable, then B is also undecidable. In complexity, polynomial-time reductions define NP-completeness: if A ≤_p B and A is NP-complete, then B is also NP-hard. Both uses share the same logical structure — 'if you could solve B, you could solve A, so B is at least as hard as A' — differing only in the resource constraints allowed for the reduction itself."

- question: "Why is 'P vs. NP' a question about efficient computation rather than about what can be computed at all?"
  type: short-answer
  answer: "P and NP are both subsets of the decidable problems — every problem in NP has an algorithm (verification is polynomial, and exhaustive search always terminates for decidable problems). The question P vs. NP asks whether problems whose solutions can be verified quickly can also be solved quickly — it is entirely about the efficiency of computation, not its existence. Undecidability is the outer boundary of what algorithms can do at all; P vs. NP concerns the inner structure of efficiently solvable problems within the decidable region. A problem like satisfiability (SAT) is NP-complete: it is decidable, but no polynomial-time algorithm is known. This is fundamentally different from the halting problem, for which no algorithm of any kind exists."
  explanation: "The mental map from the explainer is useful here: imagine problems arranged by solvability. Undecidable problems sit outside the decidable region entirely. P vs. NP is a question about where the boundary within the decidable region lies — specifically whether the efficiently-verifiable problems (NP) are also efficiently-solvable (P). The two questions are at completely different levels of the hierarchy."
```

## Explainer

The field of theoretical computer science begins with a question that preceded computers themselves: what can be computed at all? Alan Turing answered this in 1936 by defining a model of computation — the Turing machine — and showing that some problems cannot be solved by any algorithm whatsoever. This is the domain of **computability theory**: it identifies the outer boundary of algorithmic possibility, independent of time, space, or hardware. The classic example is the **halting problem**: no algorithm can correctly decide, for all program-input pairs, whether the program halts or runs forever. This is not a practical limitation — it is a mathematical impossibility, proved by a diagonal argument that constructs a program that contradicts any hypothetical decider.

Once we know a problem is computable, a second question arises: how *efficiently* can it be computed? This is the domain of **complexity theory**, which developed in the 1960s and 1970s. Complexity theory partitions decidable problems by the resources — primarily time and memory space — they require as input size grows. The complexity class **P** contains problems solvable in polynomial time; **NP** contains problems whose solutions can be *verified* in polynomial time. The central open question — whether P = NP — asks whether efficient verification always implies efficient solution. Most researchers believe P ≠ NP, but no proof exists either way.

The two fields share deep structural connections. Both use **diagonalization** — the technique Turing used to show the halting problem is undecidable — as a key proof method; the same idea yields the time and space hierarchy theorems in complexity. Both fields rely on **reductions**: transformations that convert one problem to another, preserving difficulty. In computability, many-one reductions define relative undecidability (if A reduces to B and A is undecidable, so is B). In complexity, polynomial-time reductions define NP-completeness. The Turing machine model is the foundation of both: computability asks whether a TM halts on a given input; complexity asks how quickly.

A useful mental map: imagine problems arranged by solvability. The outermost region is **undecidable** problems — no algorithm exists. Inside is the decidable region. Within that, the efficiently solvable ones form **P**. Complexity theory maps the interior of the decidable region in fine detail — PSPACE, the exponential classes, the NP-complete problems clustered on the boundary of P. Computability draws the outer boundary; complexity theory surveys the interior. Together they answer both halves of the fundamental question: what can be computed, and at what cost?
