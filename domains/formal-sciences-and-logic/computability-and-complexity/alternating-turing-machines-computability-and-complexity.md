---
id: alternating-turing-machines-computability-and-complexity
title: Alternating Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-turing-machines
  type: hard
- id: turing-machines-formal
  type: hard
builds-toward:
- pspace-and-complexity-hierarchy
tags:
- computation-models
- quantifiers
- complexity
stage: advanced
status: draft
---

# Alternating Turing Machines

## Core Idea
An alternating Turing machine is a nondeterministic Turing machine whose states are classified as existential (∃) or universal (∀). Computation branches existentially at ∃-states (seeking a 'yes' path) and universally at ∀-states (requiring all paths to lead to acceptance). The time and space complexity of ATMs characterize the polynomial hierarchy and PSPACE, respectively.

## Explainer

You already know that a **nondeterministic Turing machine** (NTM) accepts if *at least one* branch of its computation tree accepts — it is constantly searching for a "yes" witness. An **alternating Turing machine** (ATM) keeps that branching structure but adds a new control: each nondeterministic state is labeled either **existential** (∃) or **universal** (∀). At an existential state the machine accepts if *some* branch accepts (just like a plain NTM). At a universal state it accepts only if *all* branches accept. The acceptance condition is then evaluated bottom-up through the entire computation tree.

The easiest way to feel the difference is through quantifiers. Asking "does there exist an assignment that satisfies this formula?" is existential — one good assignment suffices. Asking "does every possible input lead to a valid output?" is universal — you have to survive every challenge. An ATM can interleave these two modes, asking "is there an x such that for every y there exists a z such that…" — exactly the quantifier alternations that define the **polynomial hierarchy**. A language is in Σ₂P if it can be decided by an ATM that starts with an existential state and makes at most one alternation to a universal state, all within polynomial time.

The deeper connection is with space complexity. An ATM running in time f(n) recognizes exactly the languages decidable in space f(n) by a deterministic machine (for f(n) ≥ log n). This gives the striking equalities **ALOGSPACE = P** and **AP = PSPACE**. Intuitively, alternation trades time for space: by exhaustively exploring all universal branches "simultaneously," an ATM can verify space-bounded computations in polynomial time by simulating the game-theoretic view of PSPACE — one player existentially guesses moves, the other universally challenges them. The machine accepts if the existential player has a winning strategy.

This means ATMs provide a computational characterization of every major class in the hierarchy. Each level of the polynomial hierarchy corresponds to an ATM with a fixed number of alternations starting from an existential state (Σ classes) or a universal state (Π classes). PSPACE itself is the union over all these levels. The ATM framework thus unifies the polynomial hierarchy and space complexity into a single machine model, making it one of the most conceptually economical tools in complexity theory.
