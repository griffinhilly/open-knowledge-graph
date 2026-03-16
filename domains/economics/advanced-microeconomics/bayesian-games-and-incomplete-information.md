---
id: bayesian-games-and-incomplete-information
title: Bayesian Games and Incomplete Information
domain: economics
course: advanced-microeconomics
prerequisites:
- id: strategic-form-games
  type: hard
- id: bayes-theorem
  type: hard
builds-toward:
- signaling-games-and-pooling-separating
- mechanism-design-and-vickrey-clarke-groves
tags:
- game-theory
- information-asymmetry
stage: advanced
status: draft
---

# Bayesian Games and Incomplete Information

## Core Idea
Bayesian games model incomplete information: players have private types drawn from a distribution, known only to themselves. A Bayesian Nash equilibrium specifies each type's strategy such that no type wants to deviate given beliefs about other types. Harsanyi's representation embeds incomplete-information games as perfect-information games with an exogenous first move by Nature assigning types.

## Explainer

In the strategic-form games you have already studied, every player knows the payoff matrix — who values what, and how much. But real strategic interactions rarely work that way. A seller may not know how much a buyer is willing to pay. A firm entering a market may not know whether the incumbent has low costs or high costs. A bidder in an auction does not know rival valuations. **Bayesian games** extend game theory to handle this pervasive uncertainty by giving each player a private **type** that determines their payoffs, and that other players can only guess at through probability distributions.

The key modeling trick, due to John Harsanyi, converts incomplete information into imperfect information. Instead of saying "Player 1 doesn't know Player 2's payoffs," we introduce a fictional player called **Nature** who moves first, randomly assigning each player a type according to a commonly known prior distribution. After Nature's move, each player observes their own type but not the types of others. This transforms an intractable problem — how do you strategize when you don't even know the game? — into a well-defined extensive-form game where you simply don't observe one of Nature's moves. You already know how to handle that from Bayes' theorem: update your beliefs given what you observe.

A **Bayesian Nash equilibrium** (BNE) specifies a strategy for every possible type of every player, such that each type's strategy is a best response given their beliefs about the distribution of other players' types. The critical shift from standard Nash equilibrium is that your strategy must be optimal not against a known opponent, but against a probability distribution over opponent types. Think of it as playing against a weighted average of all possible opponents simultaneously. If you are a high-cost firm choosing whether to enter a market, you must weigh your action against the probability that the incumbent is aggressive (low-cost) versus accommodating (high-cost), and your equilibrium strategy must be optimal across that entire distribution.

This framework is the foundation for nearly everything in information economics. Auction theory models bidders as having private value types. Signaling and screening models (which this topic builds toward) ask how informed players can credibly reveal — or strategically conceal — their types. Mechanism design asks how to structure the rules of a game so that players' equilibrium behavior in the Bayesian game achieves a desired outcome. Without the Bayesian game framework, none of these fields would have a rigorous strategic foundation, because they all depend on modeling what happens when players know things that others do not.
