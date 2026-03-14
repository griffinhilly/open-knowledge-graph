---
id: subgame-perfect-equilibrium
title: Subgame Perfect Equilibrium
domain: economics
course: advanced-microeconomics
prerequisites:
- id: extensive-form-games
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- perfect-bayesian-equilibrium
tags:
- game-theory
- sequential-games
- equilibrium-refinement
stage: advanced
status: draft
---

# Subgame Perfect Equilibrium

## Core Idea
Subgame perfect equilibrium requires that strategies form a Nash equilibrium in every subgame, not just the entire game. This eliminates incredible threats: actions that would not actually be chosen if reached. Backward induction finds subgame perfect equilibrium by solving from terminal nodes backward, ensuring strategic consistency throughout the game tree.
