---
id: revelation-principle-mechanisms
title: The Revelation Principle
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games-incomplete-info
  type: hard
- id: mechanism-design-basics
  type: hard
builds-toward:
- vcg-auction-mechanism
tags:
- mechanism-design
- truth-telling
- incentive-compatibility
stage: advanced
status: draft
---

# The Revelation Principle

## Core Idea
The revelation principle states that any allocation implementable by some mechanism can be implemented by a direct mechanism where agents truthfully report their private information. Direct mechanisms simplify analysis by focusing on truth-telling equilibria rather than complex indirect mechanisms, dramatically reducing mechanism design complexity.

## Explainer

From Bayesian games, you know how to analyze strategic situations where players have private information. From mechanism design basics, you know that a designer can choose the rules of the game to achieve desired outcomes. The **revelation principle** is the result that makes mechanism design tractable — without it, the designer would face an impossibly large search problem over all conceivable game forms.

Here is the problem the revelation principle solves. Suppose you want to allocate a resource efficiently among agents who have private information about their valuations. You could design any kind of mechanism: an auction, a bargaining protocol, a lottery, a multi-round negotiation with complex messaging. Each mechanism induces a different game, and agents play different equilibrium strategies in each one. To find the best mechanism, you would seemingly need to search over every possible game form and every possible equilibrium — an intractable task. The revelation principle collapses this search dramatically.

The key insight is constructive. Take any mechanism M that implements some allocation in equilibrium. In M, each agent has a strategy that maps her private type to an action (a bid, a message, a signal). Now build a new **direct mechanism** D as follows: ask each agent to simply report her type, then apply the equilibrium strategy from M on her behalf and carry out the resulting allocation and payments. In this direct mechanism, truthful reporting replicates exactly what happens in the original equilibrium — so truth-telling is an equilibrium of D. The allocation implemented by the complex mechanism M is also implemented by the simple direct mechanism D where agents just announce their types honestly.

This means the mechanism designer can restrict attention to **direct, incentive-compatible mechanisms** — mechanisms where agents report their types and truth-telling is an equilibrium — without any loss of generality. Instead of searching over all possible game forms, you search over allocation rules and payment rules that satisfy incentive compatibility (no type wants to lie) and individual rationality (no type wants to opt out). This transforms mechanism design from an impossibly open-ended game design problem into a constrained optimization problem with well-defined mathematical structure. The revelation principle does not say that direct mechanisms are the best way to run things in practice — real-world auctions and negotiations have practical advantages — but it says that for the purpose of finding the optimal outcome, you never need to look beyond direct truth-telling mechanisms. Every outcome achievable by any mechanism whatsoever is achievable by asking people to tell the truth.
