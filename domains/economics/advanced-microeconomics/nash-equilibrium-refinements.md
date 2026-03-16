---
id: nash-equilibrium-refinements
title: Nash Equilibrium Refinements
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
builds-toward:
- subgame-perfect-equilibrium
- perfect-bayesian-equilibrium
tags:
- game-theory
- equilibrium
- solution-concepts
stage: abstract-reasoning
status: draft
---

# Nash Equilibrium Refinements

## Core Idea
A Nash equilibrium refinement is a criterion that eliminates some Nash equilibria as implausible or unreasonable. Common refinements include subgame perfection (no implausible threats), perfect Bayesian equilibrium (consistent beliefs), and trembling-hand perfection (robustness to small errors). Refinements help pin down equilibrium when multiple equilibria exist.

## How It's Best Learned
Start with games that have multiple Nash equilibria. Show why some seem unreasonable. Apply different refinements and see which equilibria survive.

## Explainer

From Nash equilibrium, you know that an equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. This is a powerful concept, but in many games it is too permissive — it admits equilibria that rely on threats no rational player would actually carry out, beliefs that make no sense given the structure of the game, or strategies that would collapse if players made even tiny mistakes. **Equilibrium refinements** are additional criteria designed to eliminate these implausible equilibria and sharpen predictions.

The most intuitive refinement is **subgame perfection**, which requires that strategies form a Nash equilibrium in every subgame of the original game — not just the game as a whole. Consider a market entry game: an incumbent threatens to start a price war if a challenger enters. This threat can sustain an equilibrium where the challenger stays out. But if entry actually occurred, would the incumbent really follow through? A price war hurts the incumbent too. Subgame perfection requires that the incumbent's strategy be optimal even after entry happens, eliminating threats that are not credible when actually tested. You find subgame perfect equilibria through **backward induction**: start at the end of the game tree, determine optimal play at each final decision node, then work backwards. Any equilibrium that relies on a player acting against their own interest at some decision point is eliminated.

When games involve **incomplete information** — players are uncertain about others' types or previous actions — subgame perfection alone is insufficient because there may not be well-defined subgames to analyze. **Perfect Bayesian equilibrium** (PBE) addresses this by requiring two things simultaneously: strategies must be sequentially rational (optimal at every information set given beliefs), and beliefs must be consistent with strategies via **Bayes' rule** wherever possible. In a signaling game, for example, PBE pins down not just what the sender does and how the receiver responds, but what the receiver believes about the sender's type after observing each possible signal. Beliefs cannot be arbitrary — they must be updated rationally from prior probabilities and observed actions.

A third important refinement is **trembling-hand perfection**, which tests whether an equilibrium is robust to small mistakes. The idea is that every player has a tiny probability of "trembling" and playing any available strategy by accident. A trembling-hand perfect equilibrium must remain a best response even when opponents occasionally err. This eliminates equilibria that survive only because a player is indifferent between strategies and the equilibrium relies on them choosing a specific one that would be suboptimal if opponents ever deviated. Each refinement captures a different aspect of strategic plausibility — credibility of threats (subgame perfection), consistency of beliefs (PBE), or robustness to errors (trembling hand) — and the choice of which refinement to apply depends on the game's structure and what kind of implausibility you are trying to rule out.
