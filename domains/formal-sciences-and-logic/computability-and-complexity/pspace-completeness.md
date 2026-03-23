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
status: validated
---

# PSPACE and PSPACE-Completeness

## Core Idea
PSPACE is the class of problems solvable in polynomial space (regardless of time). PSPACE contains the polynomial hierarchy and includes problems like quantified Boolean formulas (QBF) that are PSPACE-complete. The relationship between time and space complexity is subtle: PSPACE-completeness reveals problems harder than NP (under standard assumptions) yet solvable with modest space.

## How It's Best Learned
Understand the connection between polynomial space and polynomial alternation via Savitch's theorem. Study TQBF as the canonical PSPACE-complete problem.

## Questions

```yaml
- question: "What is the key conceptual difference between SAT (an NP-complete problem) and TQBF (the canonical PSPACE-complete problem)?"
  type: multiple-choice
  options:
    - "SAT uses Boolean formulas while TQBF uses arithmetic formulas — the difference is purely syntactic"
    - "SAT asks whether some assignment satisfies the formula (one player, one move); TQBF asks whether a formula is true under all ∀-choices despite optimal ∃-choices (adversarial game, many moves)"
    - "SAT is solvable in polynomial time; TQBF requires exponential time, placing it outside NP"
    - "TQBF is just a generalization of SAT to longer formulas — if SAT were polynomial-time, so would TQBF"
  answer: 1
  explanation: "SAT is a one-player puzzle: find a single assignment that satisfies the formula. The certificate (the satisfying assignment) is polynomial in size and verifiable in polynomial time — that's what makes it NP. TQBF is an adversarial game between an existential player (∃) and a universal player (∀): does ∃ have a winning strategy no matter what ∀ does? Evaluating this requires exploring an exponentially large game tree where both players move optimally. No polynomial-size certificate exists for a 'yes' answer (you can't just exhibit one assignment), which is why TQBF is harder than NP under standard assumptions."

- question: "Many combinatorial board games — generalized chess endgames, generalized Hex, generalized Go — are PSPACE-complete. What property of two-player perfect-information games connects them to PSPACE?"
  type: multiple-choice
  options:
    - "These games have exponentially many board positions, placing them automatically in EXPTIME"
    - "Determining the winner with perfect play requires evaluating an adversarial game tree with alternating ∀/∃ quantifiers over polynomial-length plays, which is exactly what PSPACE captures"
    - "The games are PSPACE-complete because their rules can be encoded as a polynomial-space Turing machine computation"
    - "All games with more than two players are automatically PSPACE-complete due to coordination complexity"
  answer: 1
  explanation: "PSPACE is the complexity class that captures 'who wins a perfect-information polynomial-length game?' The connection is direct: game trees with alternating moves are equivalent to formulas with alternating ∀/∃ quantifiers. Evaluating who wins from any position — assuming both players play optimally — requires exploring every branch of the game tree (the ∀-player's moves must all be considered; the ∃-player's best move must be found). For games with polynomial-length plays, this corresponds exactly to evaluating a quantified Boolean formula — TQBF — which is PSPACE-complete."

- question: "PSPACE contains the entire polynomial hierarchy, including NP and co-NP."
  type: true-false
  answer: true
  explanation: "The containment chain is: P ⊆ NP ⊆ PH ⊆ PSPACE ⊆ EXPTIME. Problems in NP can be solved by a nondeterministic polynomial-time machine, which uses only polynomial space (the accepting path has polynomial length, and you can verify it in polynomial space). By Savitch's theorem, NPSPACE = PSPACE, so nondeterministic polynomial space equals deterministic polynomial space. The entire polynomial hierarchy — which stratifies problems by alternation depth — collapses into PSPACE, which handles unbounded quantifier alternation. Whether these containments are strict (i.e., P ≠ NP ≠ PSPACE) is open, but PSPACE-complete problems are believed to be strictly harder than any level of PH."

- question: "Since PSPACE problems are harder than NP problems, they require exponential space to solve."
  type: true-false
  answer: false
  explanation: "PSPACE is defined as the class of problems solvable using only polynomial space — that is the definition, not a lower bound. A problem being PSPACE-complete means it is among the hardest problems in PSPACE, but all problems in PSPACE are solvable with polynomial space (though possibly exponential time). The 'harder than NP' comparison refers to computational difficulty in terms of what strategies are needed, not that more space is required. PSPACE-hard problems can often be solved by exhaustive game-tree search that reuses the same polynomial space stack — space is cheap, time is what blows up."

- question: "Explain Savitch's theorem — that NPSPACE = PSPACE — and why this is surprising compared to what we believe about time complexity."
  type: short-answer
  answer: "Savitch's theorem says that nondeterminism buys at most a quadratic blowup in space: if a nondeterministic machine solves a problem in s(n) space, a deterministic machine can solve it in O(s(n)²) space. Applied to polynomial space: NPSPACE ⊆ PSPACE, so they are equal (since PSPACE ⊆ NPSPACE trivially). The proof uses recursive reachability: to check if a configuration C is reachable from C₀ in t steps, check if any intermediate configuration C_mid is reachable in t/2 steps from each endpoint — recursing to depth log(t). The recursion stack uses O(s·log t) space, which for polynomial s and polynomial t is still polynomial. This is surprising because with time, we strongly believe P ≠ NP — nondeterminism is conjectured to give an exponential advantage. With space, nondeterminism helps at most quadratically."
  explanation: "The contrast between time and space complexity is striking. For time, P ≠ NP is widely believed: nondeterminism is thought to give an exponential speedup for many problems. For space, nondeterminism barely helps: NPSPACE = PSPACE exactly. Intuitively, space can be reused across time steps in a way that time cannot be reused. A nondeterministic machine explores many paths, but deterministically you can verify reachability one configuration at a time, reusing the same space for each check. This reuse is what Savitch's algorithm exploits. It is one of the most elegant results in complexity theory and highlights that the properties of time and space as computational resources are fundamentally different."
```

## Explainer

From your study of the polynomial hierarchy, you know that NP and co-NP sit just above P, and that the hierarchy stratifies problems by how many layers of quantifier alternations they require. **PSPACE** sits above this entire tower. It contains every problem solvable by a Turing machine using only a polynomial amount of memory, with no restriction on time. Time is cheap; space is the binding resource.

The canonical PSPACE-complete problem is **TQBF** — the **True Quantified Boolean Formula** problem. Given a Boolean formula with all variables bound by ∃ and ∀ quantifiers, decide whether it is true. For example: ∀x ∃y (x ∨ y). Unlike SAT (which asks whether *some* assignment works), TQBF asks whether a formula is true no matter how the ∀-variables are set, assuming optimal ∃-choices. This is exactly the difference between a one-move puzzle (NP) and a two-player adversarial game (PSPACE): the existential player chooses some moves, the universal player chooses others, and you must determine who wins with perfect play.

This game interpretation is why so many combinatorial games — chess endgames, generalized Go, hex, and others — are PSPACE-complete. To decide who wins from any position, you must evaluate an exponentially large game tree where both players move optimally. PSPACE is the complexity class that captures "who wins a perfect-information polynomial-length game?"

**Savitch's theorem** provides a surprising technical result: NPSPACE = PSPACE. Nondeterminism barely helps when the resource is space. This contrasts sharply with time, where we strongly believe P ≠ NP. Intuitively, a nondeterministic space computation guessing a polynomial-length path through a configuration graph can be simulated deterministically by a recursive reachability algorithm — the deterministic machine uses space to remember its position in the search, not time. The recursion depth is polynomial, so the space blowup is only quadratic.

PSPACE-completeness therefore places problems that are strictly harder (under standard assumptions) than any level of the polynomial hierarchy, yet still tractable in terms of memory. Problems in PSPACE can often be solved by exhaustive game-tree search that reuses space. This makes PSPACE a natural home for planning, verification of reactive systems (model checking), and reasoning with alternating quantifiers — any domain where the "universe" of possibilities must be explored by an adversarial process rather than a simple search.
