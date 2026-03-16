---
id: pspace-complete-problems
title: PSPACE-Complete Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pspace-complexity-class
  type: hard
- id: np-completeness
  type: hard
tags:
- hardness
- completeness
- quantified-formulas
stage: advanced
status: draft
---

# PSPACE-Complete Problems

## Core Idea
A problem is PSPACE-complete if it is in PSPACE and every PSPACE problem polynomial-time reduces to it. The canonical example is TQBF: given a fully quantified Boolean formula with alternating ∃∀ quantifiers, determine if it evaluates to true. Other PSPACE-complete problems include game-position evaluation (can the current player force a win?) and certain pattern-matching with counting. PSPACE-completeness indicates inherent intractability that polynomial space cannot overcome.

## Explainer

You already understand NP-completeness — the idea that certain problems are the hardest in NP because every NP problem reduces to them in polynomial time. PSPACE-completeness applies the same logic one level up in the complexity hierarchy. A problem is **PSPACE-complete** if it lives in PSPACE (solvable with polynomial space) and is at least as hard as every other PSPACE problem, meaning any PSPACE problem can be polynomial-time reduced to it. Since NP ⊆ PSPACE, PSPACE-complete problems are at least as hard as NP-complete problems and are widely believed to be strictly harder.

The canonical PSPACE-complete problem is **TQBF** (True Quantified Boolean Formula). While SAT asks "does there exist an assignment making this formula true?", TQBF asks something more demanding: "is this formula true when some variables are existentially quantified (∃) and others are universally quantified (∀)?" For example, ∃x ∀y (x ∨ y) asks whether there exists an x such that for every y, the formula holds. The alternation of quantifiers is what makes TQBF harder than SAT — you cannot just guess a single satisfying assignment, because you must account for an adversary choosing the universally quantified variables. Savitch's theorem shows TQBF is solvable in polynomial space by recursively evaluating quantifier blocks, and the completeness proof demonstrates that every polynomial-space computation can be encoded as a TQBF instance.

The connection to games makes PSPACE-completeness intuitive. Two-player games with perfect information — like generalized versions of chess, checkers, or Go played on n×n boards — are naturally PSPACE-complete. The reason is structural: "can Player 1 force a win?" is equivalent to asking ∃(move₁) ∀(move₂) ∃(move₃) ∀(move₄)... leading to a winning position. The alternation between "I choose" and "my opponent chooses" maps directly to the ∃∀ alternation in TQBF. This is why game-solving feels fundamentally harder than optimization: you are not searching for one good solution but reasoning about all possible counter-strategies.

PSPACE-completeness tells you something specific about a problem's difficulty. It means the problem is unlikely to have a polynomial-time algorithm (since that would imply P = PSPACE, collapsing the entire hierarchy), but it also means the problem does not require exponential space — it can be solved with careful memory management, even if the time required is exponential. The practical consequence is that PSPACE-complete problems often admit solutions that are slow but memory-efficient, trading time for space in a way that NP-complete problems already allow but PSPACE-complete problems demand at a deeper level.
