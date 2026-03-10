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
tags:
- PSPACE
- L
- NL
- space-complexity
- Savitch
stage: advanced
status: draft
---

# Space Complexity: PSPACE, L, and NL

## Core Idea
Space complexity classes measure memory usage rather than time. PSPACE contains problems solvable in polynomial space (e.g., quantified Boolean formula satisfiability, TQBF), and is known to contain NP and P. The class L consists of problems solvable in logarithmic space on a deterministic TM; NL uses nondeterministic log space. Savitch's theorem shows NPSPACE = PSPACE, meaning nondeterminism buys much less in space than it might in time. Space and time complexity interact deeply: PSPACE ⊆ EXPTIME, and P ⊆ NP ⊆ PSPACE, but most containments are strict.

## How It's Best Learned
Work through the TQBF PSPACE-completeness proof as the space analogue of Cook-Levin. Understand NL-completeness of graph reachability (ST-Connectivity) and how the Immerman-Szelepcsényi theorem shows NL = co-NL.

## Common Misconceptions
- Thinking PSPACE is just 'NP with more memory' — PSPACE is strictly larger than NP is believed to be, and contains problems like two-player game evaluation that seem qualitatively harder.
- Assuming Savitch's theorem applies to time — it is specific to space; nondeterminism can provide exponential time savings in theory.
