---
id: space-complexity-classes
title: 'Space Complexity: PSPACE, L, and NL'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: nondeterministic-complexity
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
tags:
- PSPACE
- L
- NL
- space-complexity
- Savitch
stage: advanced
status: validated
---

# Space Complexity: PSPACE, L, and NL

## Core Idea
Space complexity classes measure memory usage rather than time. PSPACE contains problems solvable in polynomial space (e.g., quantified Boolean formula satisfiability, TQBF), and is known to contain NP and P. The class L consists of problems solvable in logarithmic space on a deterministic TM; NL uses nondeterministic log space. Savitch's theorem shows NPSPACE = PSPACE, meaning nondeterminism buys much less in space than it might in time. Space and time complexity interact deeply: PSPACE ⊆ EXPTIME, and P ⊆ NP ⊆ PSPACE, but most containments are strict.

## How It's Best Learned
Work through the TQBF PSPACE-completeness proof as the space analogue of Cook-Levin. Understand NL-completeness of graph reachability (ST-Connectivity) and how the Immerman-Szelepcsényi theorem shows NL = co-NL.

## Common Misconceptions
- Thinking PSPACE is just 'NP with more memory' — PSPACE is strictly larger than NP is believed to be, and contains problems like two-player game evaluation that seem qualitatively harder.
- Assuming Savitch's theorem applies to time — it is specific to space; nondeterminism can provide exponential time savings in theory.

## Explainer

From your study of time complexity, you know that P and NP classify problems by how much *time* a Turing machine needs. **Space complexity** asks a different question: how many tape cells does the machine use? This shift in resource leads to a different — and in some ways richer — hierarchy of complexity classes, because space can be reused (you can overwrite a tape cell) while time cannot be recovered.

**PSPACE** contains all problems solvable using a polynomial amount of memory, regardless of how long the computation takes. Its complete problem is **TQBF** (True Quantified Boolean Formulas): given a Boolean formula with alternating universal and existential quantifiers, determine whether it is true. Think of TQBF as a two-player game — one player tries to make the formula true, the other tries to make it false, and they alternate choosing variable assignments. This game-theoretic flavor is characteristic of PSPACE problems: evaluating game positions, planning under adversarial conditions, and verifying properties of systems with alternating control all tend to land in PSPACE. We know P ⊆ NP ⊆ PSPACE ⊆ EXPTIME, but whether any of these containments are strict remains open.

At the other end of the space spectrum, **L** (logarithmic space) contains problems solvable using only O(log n) bits of working memory beyond the read-only input. This is barely enough to store a constant number of pointers into the input. **NL** (nondeterministic log space) allows nondeterministic guessing on that same tiny workspace. The canonical NL-complete problem is **ST-Connectivity**: given a directed graph, is there a path from s to t? A nondeterministic machine can guess the path one node at a time, needing only enough memory to store the current node. A remarkable result — the **Immerman-Szelepcsényi theorem** — shows that NL = co-NL, meaning if you can nondeterministically verify reachability, you can also nondeterministically verify *non*-reachability in log space.

The most surprising structural result is **Savitch's theorem**: NSPACE(f(n)) ⊆ DSPACE(f(n)²). This means nondeterminism gives at most a quadratic advantage in space, unlike the potentially exponential advantage it might give in time (the P vs NP question). The proof is elegant — it uses a recursive divide-and-conquer strategy to check whether a configuration is reachable in 2^k steps by checking whether some midpoint configuration is reachable in 2^(k-1) steps from both ends. As an immediate corollary, NPSPACE = PSPACE, collapsing the nondeterministic and deterministic polynomial-space classes together. This contrasts sharply with time complexity, where NP and P are widely believed to differ.
