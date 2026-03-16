---
id: bayesian-games-incomplete-info
title: Bayesian Games and Incomplete Information
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: bayes-theorem
  type: soft
- id: conditional-probability
  type: soft
- id: bayes-theorem-and-inference
  type: hard
- id: conditional-probability-fundamentals
  type: hard
builds-toward:
- perfect-bayesian-equilibrium
- mechanism-design-basics
tags:
- game-theory
- information-asymmetry
- types
stage: advanced
status: draft
---

# Bayesian Games and Incomplete Information

## Core Idea
Bayesian games model strategic situations where players have incomplete information about each other's payoffs or types. Players have private types drawn from a common prior distribution, and each player's strategy is conditioned on their type. Bayesian Nash equilibrium is a strategy profile where each player's type-contingent strategy is optimal given beliefs about others' types.

## Explainer

In the standard games you studied when learning Nash equilibrium, every player knows the full structure of the game — who the players are, what actions are available, and what payoffs result from each outcome. But real strategic situations are rarely so transparent. A firm entering a market does not know its rival's cost structure. A bidder at an auction does not know how much others value the item. A country negotiating a treaty does not know the other side's true resolve. **Bayesian games** extend game theory to handle exactly this kind of uncertainty.

The key modeling innovation is the concept of a **type**. Each player has a type that determines their payoffs, and this type is private information — known to the player but not to others. Before the game begins, nature draws each player's type from a probability distribution called the **common prior**. All players know this prior distribution (they agree on the statistical structure of uncertainty), but each player observes only their own realized type. So when Player 1 is deciding what to do, they know their own type but must form beliefs about Player 2's type using Bayes' theorem and the common prior — exactly the probabilistic reasoning you developed in your prerequisites.

A **strategy** in a Bayesian game is no longer a single action — it is a complete contingent plan that specifies an action for every possible type a player could be. Think of it as a function mapping types to actions. Player 1's strategy says: "If I'm the low-cost type, I'll do X; if I'm the high-cost type, I'll do Y." The solution concept, **Bayesian Nash equilibrium (BNE)**, requires that every type of every player is playing a best response, given their beliefs about others' type-contingent strategies. Each type maximizes their expected payoff, where the expectation is taken over the possible types of the other players, weighted by the prior.

Consider a concrete example: two firms simultaneously choosing whether to enter a market, where each firm's profitability depends on a cost parameter only it knows. A low-cost firm might enter regardless of what the other does, while a high-cost firm enters only if it believes the other is likely to stay out. In BNE, each firm's entry decision for each cost type must be optimal given the probability distribution over the rival's cost type and the rival's type-contingent entry strategy. The equilibrium captures the interplay of private information and strategic reasoning — each player's action reflects both what they know about themselves and what they can infer about others.

Bayesian games are the foundation for nearly everything in information economics. Auctions, bargaining under uncertainty, signaling, mechanism design, and the analysis of markets with asymmetric information all build on this framework. The common prior assumption — that players agree on the distribution of types even if they don't observe each other's realizations — is both the framework's great simplifying power and its most debated feature. It transforms a problem of radical uncertainty into a tractable probabilistic calculation, making equilibrium analysis possible even when players operate in the dark about each other's true characteristics.
