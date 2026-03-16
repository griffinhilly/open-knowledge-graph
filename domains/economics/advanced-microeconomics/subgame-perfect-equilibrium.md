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

## Explainer

You already know that a Nash equilibrium is a set of strategies where no player can improve their payoff by unilaterally deviating. And from extensive-form games, you know how to represent sequential decisions as a game tree with nodes, branches, and payoffs at terminal nodes. The problem is that Nash equilibrium alone can sustain outcomes in sequential games that rely on threats no rational player would actually carry out. **Subgame perfect equilibrium** (SPE) is the refinement that eliminates these hollow threats by demanding rational play at every point in the game, not just at the start.

Consider a classic entry-deterrence game. An entrant decides whether to enter a market, and then an incumbent decides whether to fight (price war) or accommodate. Fighting is costly for both players. One Nash equilibrium has the incumbent threatening to fight if entry occurs, which deters the entrant. But this threat is **incredible** — if the entrant actually entered, the incumbent would prefer accommodating to a mutually destructive price war. The threat only works if the entrant believes the incumbent would irrationally hurt itself. Subgame perfect equilibrium rejects this: it requires that the incumbent's strategy be optimal even at the node where entry has already occurred.

The technique for finding SPE is **backward induction**. You start at the terminal nodes of the game tree and work backward. At each decision node, you determine what the player at that node would rationally choose, given what happens downstream. Then you fold that choice back into the analysis of earlier nodes. In the entry game, you first solve the incumbent's problem: fight or accommodate? Accommodation is better, so that is the incumbent's choice at that subgame. Knowing this, the entrant at the first node anticipates accommodation and enters. The subgame perfect equilibrium is (Enter, Accommodate) — the only outcome consistent with rational play at every stage.

A **subgame** is any portion of the game tree that starts at a single decision node (where the player knows exactly where they are), includes all subsequent nodes, and can stand alone as a complete game. SPE requires Nash equilibrium play within every such subgame. In games of perfect information — where every player observes all prior moves — backward induction always yields at least one subgame perfect equilibrium. This makes SPE especially powerful for analyzing bargaining, sequential market entry, and multi-stage strategic interactions where the credibility of threats and promises is the central question.
