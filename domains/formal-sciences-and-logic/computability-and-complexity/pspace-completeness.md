---
id: pspace-completeness
title: PSPACE and PSPACE-Completeness
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pspace-and-complexity-hierarchy
  type: hard
- id: polynomial-hierarchy
  type: hard
builds-toward:
- alternating-machines-hierarchy
tags:
- pspace
- space-complexity
- qbf
- pspace-complete
stage: advanced
status: draft
---

# PSPACE and PSPACE-Completeness

## Core Idea
PSPACE is the class of problems solvable in polynomial space (regardless of time). PSPACE contains the polynomial hierarchy and includes problems like quantified Boolean formulas (QBF) that are PSPACE-complete. The relationship between time and space complexity is subtle: PSPACE-completeness reveals problems harder than NP (under standard assumptions) yet solvable with modest space.

## How It's Best Learned
Understand the connection between polynomial space and polynomial alternation via Savitch's theorem. Study TQBF as the canonical PSPACE-complete problem.

## Explainer

From your study of the polynomial hierarchy, you know that NP and co-NP sit just above P, and that the hierarchy stratifies problems by how many layers of quantifier alternations they require. **PSPACE** sits above this entire tower. It contains every problem solvable by a Turing machine using only a polynomial amount of memory, with no restriction on time. Time is cheap; space is the binding resource.

The canonical PSPACE-complete problem is **TQBF** — the **True Quantified Boolean Formula** problem. Given a Boolean formula with all variables bound by ∃ and ∀ quantifiers, decide whether it is true. For example: ∀x ∃y (x ∨ y). Unlike SAT (which asks whether *some* assignment works), TQBF asks whether a formula is true no matter how the ∀-variables are set, assuming optimal ∃-choices. This is exactly the difference between a one-move puzzle (NP) and a two-player adversarial game (PSPACE): the existential player chooses some moves, the universal player chooses others, and you must determine who wins with perfect play.

This game interpretation is why so many combinatorial games — chess endgames, generalized Go, hex, and others — are PSPACE-complete. To decide who wins from any position, you must evaluate an exponentially large game tree where both players move optimally. PSPACE is the complexity class that captures "who wins a perfect-information polynomial-length game?"

**Savitch's theorem** provides a surprising technical result: NPSPACE = PSPACE. Nondeterminism barely helps when the resource is space. This contrasts sharply with time, where we strongly believe P ≠ NP. Intuitively, a nondeterministic space computation guessing a polynomial-length path through a configuration graph can be simulated deterministically by a recursive reachability algorithm — the deterministic machine uses space to remember its position in the search, not time. The recursion depth is polynomial, so the space blowup is only quadratic.

PSPACE-completeness therefore places problems that are strictly harder (under standard assumptions) than any level of the polynomial hierarchy, yet still tractable in terms of memory. Problems in PSPACE can often be solved by exhaustive game-tree search that reuses space. This makes PSPACE a natural home for planning, verification of reactive systems (model checking), and reasoning with alternating quantifiers — any domain where the "universe" of possibilities must be explored by an adversarial process rather than a simple search.
