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
