---
id: pspace-complexity-class
title: PSPACE Complexity Class
domain: computer-science
course: theory-of-computation
prerequisites:
- id: space-complexity-classes
  type: hard
- id: complexity-class-p-definition
  type: hard
builds-toward:
- polynomial-hierarchy
- pspace-complete-problems
tags:
- complexity-classes
- space-bounded
stage: advanced
status: draft
---

# PSPACE Complexity Class

## Core Idea
PSPACE is the class of decision problems solvable by a deterministic Turing machine in polynomial space. A key result (Savitch's theorem) shows PSPACE = NPSPACE, contrasting sharply with the P vs NP question. PSPACE strictly contains NP and is believed strictly larger than P, though both containments are unproven. PSPACE-complete problems include TQBF (true quantified Boolean formulas) and game-position evaluation, representing problems intractable by polynomial time but feasible with polynomial space.

## Explainer

From your study of space complexity classes, you know that computational resources can be measured in space (tape cells used) rather than time (steps taken). **PSPACE** is the class of all decision problems solvable using a polynomial amount of memory, with no restriction on how long the computation takes. This is a powerful resource model: a machine with polynomial space can run for exponential time (since it can cycle through exponentially many configurations before repeating a state), making PSPACE a very large class.

The most striking fact about PSPACE is **Savitch's theorem**: any problem solvable by a nondeterministic Turing machine in polynomial space can also be solved by a deterministic machine in polynomial space. In other words, PSPACE = NPSPACE. This stands in sharp contrast to the time-bounded world, where the question of whether nondeterminism helps (P vs NP) remains open. The intuition behind Savitch's theorem is that space can be reused — a deterministic machine can systematically explore all nondeterministic branches one at a time, reusing the same memory for each branch, at the cost of taking much longer.

The known containment chain is P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. Every polynomial-time problem uses at most polynomial space (you cannot write to more cells than you have steps), so P ⊆ PSPACE. Every NP problem can be solved in PSPACE by deterministically trying all possible certificates. We believe all these containments are strict — that PSPACE is genuinely larger than NP and P — but no separation has been proven between P and PSPACE. We do know that P ≠ EXPTIME (by the time hierarchy theorem), which means at least one of these containments is strict.

The canonical **PSPACE-complete** problem is **TQBF** (True Quantified Boolean Formulas): given a fully quantified Boolean formula with alternating "for all" and "there exists" quantifiers, determine whether it is true. The alternation of quantifiers is what makes TQBF harder than SAT — it captures the back-and-forth reasoning of two-player games. This is why evaluating game positions (generalized chess, Go on an n×n board) tends to be PSPACE-complete: determining whether a player has a winning strategy requires reasoning about all possible opponent responses to all possible moves, a structure naturally expressed with quantifier alternation.
