---
id: game-theory-strategic-behavior-nash
title: 'Game Theory: Strategic Behavior and Nash Equilibrium'
domain: economics
course: microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- cournot-competition
- bertrand-competition
tags:
- game-theory
- strategic-interaction
- equilibrium
stage: advanced
status: draft
---

# Game Theory: Strategic Behavior and Nash Equilibrium

## Core Idea
Game theory models strategic interaction when each player's outcome depends on others' actions. A Nash equilibrium is a strategy profile where no player can improve by unilateral deviation. In oligopolies, firms choose quantities (Cournot) or prices (Bertrand), leading to different equilibrium outcomes. Game theory explains why oligopolists earn profits between competition and monopoly levels.

## How It's Best Learned
Solve simple games (2×2 matrices). Find dominant strategies, Nash equilibria. Compare equilibrium outcomes to monopoly and competition benchmarks.

## Common Misconceptions
- Nash equilibrium is optimal for society (it's individually rational but may be collectively suboptimal; e.g., prisoner's dilemma).
- There is always a unique Nash equilibrium (some games have multiple equilibria or none in pure strategies).

## Explainer

Game theory's central insight is that your best choice depends on what others do — and they know that, and you know they know that. This mutual dependency is what makes strategic situations fundamentally different from ordinary optimization. In a competitive market, each firm is so small it ignores rivals; but in an oligopoly with a few large firms, each firm's output decision directly affects the market price and therefore its rivals' profits. The framework for analyzing this is the **strategic game**: a set of players, a set of strategies available to each, and a payoff function mapping every combination of strategies to outcomes for each player.

A **Nash equilibrium** is a self-reinforcing outcome: given what everyone else is doing, no single player benefits from switching strategies unilaterally. It doesn't require communication — it's a state of mutual best responses. The prisoner's dilemma illustrates why Nash equilibrium is individually rational but potentially collectively inefficient. Two suspects, unable to communicate, each choose between confessing and staying silent. The Nash equilibrium (both confess) leaves both worse off than if they'd cooperated (both stayed silent), but it's stable because each player, taking the other's choice as fixed, strictly prefers to confess. This logic applies directly to oligopoly: firms would collectively earn more by colluding on monopoly output, but each firm has an individual incentive to undercut the cartel, pushing the equilibrium toward higher output and lower prices than the monopoly outcome.

In the **Cournot model**, firms simultaneously choose quantities. Each firm's **best response** is the profit-maximizing output given the rival's choice, yielding a best-response function. The Nash equilibrium is the intersection of these functions — the point where each firm is simultaneously on its own best-response curve. The Cournot outcome sits between competition (P = MC) and monopoly: firms exercise market power, but rivalry prevents full monopoly pricing. In the **Bertrand model**, firms compete on price with identical goods. The equilibrium is striking: with homogeneous products and constant marginal costs, both firms price at MC and earn zero economic profit — the competitive outcome emerges with just two firms, because any price above MC invites the rival to undercut by a penny and capture the entire market.

The Cournot vs. Bertrand distinction matters for real industries. When capacity is costly to change quickly (airlines, steel mills), quantity competition better describes behavior and Cournot predicts intermediate markups. When goods are homogeneous and prices adjust easily (retail, online markets), Bertrand's logic dominates and margins are thin. These two models show how the strategy variable firms compete on — quantity vs. price — fundamentally shapes market outcomes, even holding the number of firms fixed.
