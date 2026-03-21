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

## Questions

```yaml
- question: "Savitch's theorem proves PSPACE = NPSPACE. Why doesn't the same argument prove P = NP?"
  type: multiple-choice
  options:
    - "The theorem only applies to space resources — time cannot be reused the way space can, so the argument breaks down for time"
    - "Savitch's theorem only applies to polynomial bounds, and NP uses exponential time"
    - "Nondeterministic space machines are a fundamentally different model than nondeterministic time machines"
    - "Savitch's theorem requires the computation to be deterministic, which P already satisfies by definition"
  answer: 0
  explanation: "The key insight of Savitch's theorem is that space can be reused: a deterministic machine can simulate nondeterminism by exploring each branch sequentially, reusing the same polynomial memory for each branch. Time cannot be reused — once a time step passes, it's gone. Simulating nondeterminism deterministically in time requires storing or re-running all branches, which can cost exponential time. This asymmetry between space and time is why PSPACE = NPSPACE is proven while P vs NP remains open."

- question: "Why is evaluating game positions (like generalized chess on an n×n board) typically PSPACE-complete rather than NP-complete?"
  type: multiple-choice
  options:
    - "Game trees are too large to store in polynomial space, requiring exponential space"
    - "Chess positions require exponential time to evaluate but only polynomial space, which is the definition of PSPACE-complete"
    - "Determining whether a player has a winning strategy requires reasoning over all possible opponent responses to all possible moves — an alternating quantifier structure that exceeds what a single existential witness can capture"
    - "NP problems cannot have game-theoretic formulations because games require interaction between players"
  answer: 2
  explanation: "NP is characterized by problems where you can verify a solution with a single existential witness ('there exists a satisfying assignment'). Games require alternating quantifiers: 'there exists a move such that for all opponent moves, there exists a reply such that...' This alternation of ∃ and ∀ is exactly the structure of TQBF (True Quantified Boolean Formulas), the canonical PSPACE-complete problem. The depth of this alternation makes game evaluation strictly harder than NP (assuming PSPACE ≠ NP), since no single witness can certify a winning strategy against all possible opponents."

- question: "A polynomial-space machine can, in principle, run for exponential time without contradiction, because it can cycle through exponentially many distinct configurations before repeating a state."
  type: true-false
  answer: true
  explanation: "A machine with p(n) tape cells can be in at most 2^p(n) distinct configurations (combining all possible tape contents, head positions, and states). A polynomial-space machine therefore has exponentially many configurations before any state must repeat. By the halting argument, a machine that hasn't halted and hasn't repeated a configuration will halt within this exponential bound. This is why PSPACE ⊆ EXPTIME: polynomial space implies exponential time, but not vice versa."

- question: "We have proven that PSPACE is strictly larger than NP — that there exist problems in PSPACE that are not in NP."
  type: true-false
  answer: false
  explanation: "This is unproven. We know NP ⊆ PSPACE (every NP problem can be solved in polynomial space by trying all certificates), and we believe the containment is strict, but no proof exists. We cannot even prove P ≠ NP, which is a weaker separation. The only known strict separation in this region is P ≠ EXPTIME (from the time hierarchy theorem), which guarantees that at least one of the containments P ⊆ NP ⊆ PSPACE ⊆ EXPTIME is strict — but we don't know which ones."

- question: "Why can a deterministic machine solve any NPSPACE problem using only polynomial space (Savitch's theorem), while the analogous argument for time — that any NP problem can be solved deterministically in polynomial time — remains unproven?"
  type: short-answer
  answer: "Space can be reused, but time cannot. To simulate nondeterminism, a deterministic machine must explore all nondeterministic branches. If we're counting space, we can explore each branch one at a time, reusing the same polynomial memory for each branch — we just need to keep track of where we are in the search. The total space remains polynomial, though the time required may be exponential. If we're counting time, exploring all branches deterministically requires running through each one, and the number of branches may be exponential — we can't 'reuse' the time steps already consumed."
  explanation: "This asymmetry reflects a deep structural difference between space and time as computational resources. Space is a shared pool that can be reclaimed after a branch is explored; time is a one-way sequence of irreversible steps. Savitch's theorem exploits this by framing reachability as a space-efficient recursion (can you reach the accepting configuration from the start in 2^k steps?) that reuses space at each recursive call."
```

## Explainer

From your study of space complexity classes, you know that computational resources can be measured in space (tape cells used) rather than time (steps taken). **PSPACE** is the class of all decision problems solvable using a polynomial amount of memory, with no restriction on how long the computation takes. This is a powerful resource model: a machine with polynomial space can run for exponential time (since it can cycle through exponentially many configurations before repeating a state), making PSPACE a very large class.

The most striking fact about PSPACE is **Savitch's theorem**: any problem solvable by a nondeterministic Turing machine in polynomial space can also be solved by a deterministic machine in polynomial space. In other words, PSPACE = NPSPACE. This stands in sharp contrast to the time-bounded world, where the question of whether nondeterminism helps (P vs NP) remains open. The intuition behind Savitch's theorem is that space can be reused — a deterministic machine can systematically explore all nondeterministic branches one at a time, reusing the same memory for each branch, at the cost of taking much longer.

The known containment chain is P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. Every polynomial-time problem uses at most polynomial space (you cannot write to more cells than you have steps), so P ⊆ PSPACE. Every NP problem can be solved in PSPACE by deterministically trying all possible certificates. We believe all these containments are strict — that PSPACE is genuinely larger than NP and P — but no separation has been proven between P and PSPACE. We do know that P ≠ EXPTIME (by the time hierarchy theorem), which means at least one of these containments is strict.

The canonical **PSPACE-complete** problem is **TQBF** (True Quantified Boolean Formulas): given a fully quantified Boolean formula with alternating "for all" and "there exists" quantifiers, determine whether it is true. The alternation of quantifiers is what makes TQBF harder than SAT — it captures the back-and-forth reasoning of two-player games. This is why evaluating game positions (generalized chess, Go on an n×n board) tends to be PSPACE-complete: determining whether a player has a winning strategy requires reasoning about all possible opponent responses to all possible moves, a structure naturally expressed with quantifier alternation.
